"""
Integration Test IT-01 — Controller Persona Pipeline
Red Hat Copywriter Skill

Tests the rhel_copywriter_generate MCP tool via the stdio server.
All test cases exercise real execution — no mocking of the server.

Run: cd /path/to/skills && python -m pytest tests/integration/test_it01_controller_pipeline.py -v
"""
import json
import subprocess
import sys
import time
from pathlib import Path

# ── Helpers ───────────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SERVER_SCRIPT = REPO_ROOT / ".claude" / "mcp-servers" / "rhel-copywriter-server.js"


def mcp_tools_call(brief: dict, request_id: int = 1) -> dict:
    """Send a tools/call JSON-RPC request to the MCP server via stdio.
    Returns the parsed inner content text (the skill output envelope)."""
    request = {
        "jsonrpc": "2.0",
        "id": request_id,
        "method": "tools/call",
        "params": {
            "name": "rhel_copywriter_generate",
            "arguments": brief,
        },
    }
    request_bytes = (json.dumps(request) + "\n").encode()

    start = time.monotonic()
    result = subprocess.run(
        ["node", str(SERVER_SCRIPT)],
        input=request_bytes,
        capture_output=True,
        timeout=30,
    )
    elapsed = time.monotonic() - start

    assert result.returncode == 0, f"Server exited with code {result.returncode}. stderr: {result.stderr.decode()}"
    assert elapsed < 30, f"Server response took {elapsed:.2f}s — exceeded 30 s limit"

    mcp_response = json.loads(result.stdout.strip())
    assert mcp_response.get("jsonrpc") == "2.0"
    assert "result" in mcp_response, f"Expected 'result', got: {mcp_response}"
    content = mcp_response["result"]["content"]
    assert len(content) > 0
    assert content[0]["type"] == "text"
    envelope = json.loads(content[0]["text"])
    return envelope


# ── TC-01-A: Solution Brief, Executive Tone ───────────────────────────────────

TC_01_A_BRIEF = {
    "content_type": "solution_brief",
    "product_or_topic": "Red Hat OpenShift",
    "target_audience": "IT decision maker",
    "key_messages": [
        "Accelerate cloud-native application delivery",
        "Reduce operational overhead with managed Kubernetes",
        "Maintain security and compliance at scale",
    ],
    "tone_override": "executive",
    "word_count_target": 600,
}


def test_tc01a_no_error_key():
    envelope = mcp_tools_call(TC_01_A_BRIEF, request_id=1)
    assert "error" not in envelope, f"Unexpected error: {envelope.get('error')}"


def test_tc01a_draft_non_empty():
    envelope = mcp_tools_call(TC_01_A_BRIEF, request_id=1)
    assert "draft" in envelope
    assert isinstance(envelope["draft"], str) and len(envelope["draft"]) > 0


def test_tc01a_draft_has_all_sections():
    envelope = mcp_tools_call(TC_01_A_BRIEF, request_id=1)
    draft = envelope["draft"]
    for section in ("## Headline", "## Body Copy", "## CTA", "## Confidence Note"):
        assert section in draft, f"Missing section '{section}' in draft"


def test_tc01a_word_count_positive_integer():
    envelope = mcp_tools_call(TC_01_A_BRIEF, request_id=1)
    wc = envelope.get("word_count")
    assert isinstance(wc, int) and wc > 0


def test_tc01a_terminology_audit_present():
    envelope = mcp_tools_call(TC_01_A_BRIEF, request_id=1)
    audit = envelope.get("terminology_audit")
    assert isinstance(audit, dict)
    assert "flagged_terms" in audit
    assert "banned_terms_detected" in audit


def test_tc01a_metadata_fields():
    envelope = mcp_tools_call(TC_01_A_BRIEF, request_id=1)
    meta = envelope.get("metadata", {})
    assert meta.get("skill_version") == "1.0.0"
    assert meta.get("standards_ref_version") == "BT-2026-Q2"
    assert meta.get("terminology_version") == "TERM-2026-Q2"
    assert meta.get("content_type_applied") == "solution_brief"
    assert meta.get("tone_applied") == "executive"
    assert meta.get("word_count_target_override") == 600


# ── TC-01-B: Blog, Default Tone (no tone_override) ───────────────────────────

TC_01_B_BRIEF = {
    "content_type": "blog",
    "product_or_topic": "Red Hat Enterprise Linux",
    "target_audience": "IT manager",
    "key_messages": [
        "RHEL provides a stable, supported foundation for enterprise workloads",
        "RHEL runs consistently across bare metal, virtual, cloud, and edge environments",
    ],
}


def test_tc01b_no_error_key():
    envelope = mcp_tools_call(TC_01_B_BRIEF, request_id=2)
    assert "error" not in envelope


def test_tc01b_draft_non_empty():
    envelope = mcp_tools_call(TC_01_B_BRIEF, request_id=2)
    assert len(envelope.get("draft", "")) > 0


def test_tc01b_default_tone_applied():
    """AC-01-C: when tone_override is omitted, metadata.tone_applied must be 'standard'."""
    envelope = mcp_tools_call(TC_01_B_BRIEF, request_id=2)
    assert envelope["metadata"]["tone_applied"] == "standard"


def test_tc01b_metadata_content_type():
    envelope = mcp_tools_call(TC_01_B_BRIEF, request_id=2)
    assert envelope["metadata"]["content_type_applied"] == "blog"


def test_tc01b_word_count_target_override_null():
    """No word_count_target in brief — override must be null in metadata."""
    envelope = mcp_tools_call(TC_01_B_BRIEF, request_id=2)
    assert envelope["metadata"]["word_count_target_override"] is None


# ── TC-01-C: Email with Banned Terms ─────────────────────────────────────────

TC_01_C_BRIEF = {
    "content_type": "email",
    "product_or_topic": "Red Hat Ansible Automation Platform",
    "target_audience": "DevOps engineer",
    "key_messages": [
        "Ansible Automation Platform is the industry-standard choice for enterprise automation",
        "Seamless, robust playbook management reduces toil across hybrid infrastructure",
    ],
    "tone_override": "standard",
}

EXPECTED_BANNED = {"industry-standard", "robust", "seamless"}


def test_tc01c_banned_terms_detected():
    """AC-02: all three banned input terms must appear in banned_terms_detected."""
    envelope = mcp_tools_call(TC_01_C_BRIEF, request_id=3)
    detected = set(envelope["terminology_audit"]["banned_terms_detected"])
    assert EXPECTED_BANNED.issubset(detected), \
        f"Expected banned terms {EXPECTED_BANNED}, detected: {detected}"


def test_tc01c_banned_terms_flagged_with_replacements():
    """All detected banned terms must have action_taken == 'replaced'."""
    envelope = mcp_tools_call(TC_01_C_BRIEF, request_id=3)
    flagged = envelope["terminology_audit"]["flagged_terms"]
    flagged_by_term = {e["term"]: e for e in flagged}
    for term in EXPECTED_BANNED:
        assert term in flagged_by_term, f"Term '{term}' missing from flagged_terms"
        assert flagged_by_term[term]["action_taken"] == "replaced"
        assert flagged_by_term[term]["suggested_replacement"]


def test_tc01c_draft_does_not_contain_banned_terms():
    """Banned terms must not appear in Headline or Body Copy sections of the draft.
    They may appear in the Confidence Note, which reports which terms were replaced."""
    envelope = mcp_tools_call(TC_01_C_BRIEF, request_id=3)
    draft = envelope["draft"]
    # Extract only the Headline and Body Copy sections (before ## CTA)
    cta_index = draft.find("## CTA")
    if cta_index == -1:
        cta_index = len(draft)
    headline_body = draft[:cta_index].lower()
    for term in EXPECTED_BANNED:
        assert term.lower() not in headline_body, \
            f"Banned term '{term}' still present in Headline/Body Copy sections of draft"


def test_tc01c_metadata_content_type():
    envelope = mcp_tools_call(TC_01_C_BRIEF, request_id=3)
    assert envelope["metadata"]["content_type_applied"] == "email"


# ── IT-01b: Validation Error — Missing Required Fields ────────────────────────

MALFORMED_BRIEF = {
    "content_type": "solution_brief",
    "product_or_topic": "Red Hat OpenShift",
    # missing: target_audience, key_messages
}


def test_it01b_error_key_present():
    """AC-05: malformed brief must return error key, not a draft."""
    envelope = mcp_tools_call(MALFORMED_BRIEF, request_id=4)
    assert envelope.get("error") == "input_validation_failure"


def test_it01b_no_draft_generated():
    envelope = mcp_tools_call(MALFORMED_BRIEF, request_id=4)
    assert "draft" not in envelope


def test_it01b_target_audience_error_present():
    envelope = mcp_tools_call(MALFORMED_BRIEF, request_id=4)
    fields = [e["field"] for e in envelope.get("validation_errors", [])]
    assert "target_audience" in fields


def test_it01b_key_messages_error_present():
    envelope = mcp_tools_call(MALFORMED_BRIEF, request_id=4)
    fields = [e["field"] for e in envelope.get("validation_errors", [])]
    assert "key_messages" in fields


def test_it01b_both_errors_in_single_response():
    """AC-05: no early-abort — both errors must be returned together."""
    envelope = mcp_tools_call(MALFORMED_BRIEF, request_id=4)
    assert len(envelope.get("validation_errors", [])) >= 2

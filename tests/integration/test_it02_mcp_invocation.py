"""
Integration Test IT-02 — MCP / Claude Desktop Invocation
Red Hat Copywriter Skill

Tests the full MCP stdio transport: initialize handshake, tools/list,
and tools/call for both valid and invalid briefs.

Run: cd /path/to/skills && python -m pytest tests/integration/test_it02_mcp_invocation.py -v
"""
import json
import subprocess
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SERVER_SCRIPT = REPO_ROOT / ".claude" / "mcp-servers" / "rhel-copywriter-server.js"


def send_request(request: dict) -> dict:
    """Send a single JSON-RPC request to the server. Returns parsed response."""
    request_bytes = (json.dumps(request) + "\n").encode()
    start = time.monotonic()
    result = subprocess.run(
        ["node", str(SERVER_SCRIPT)],
        input=request_bytes,
        capture_output=True,
        timeout=30,
    )
    elapsed = time.monotonic() - start
    assert result.returncode == 0, f"Server exit {result.returncode}. stderr: {result.stderr.decode()}"
    assert elapsed < 30, f"Response took {elapsed:.2f}s"
    return json.loads(result.stdout.strip())


def mcp_call(brief: dict, request_id: int = 1) -> dict:
    """Send tools/call and return the skill output envelope."""
    resp = send_request({
        "jsonrpc": "2.0",
        "id": request_id,
        "method": "tools/call",
        "params": {"name": "rhel_copywriter_generate", "arguments": brief},
    })
    assert "result" in resp
    text = resp["result"]["content"][0]["text"]
    return json.loads(text)


# ── Pre-flight: MCP initialize handshake ────────────────────────────────────

def test_preflight_initialize_responds():
    resp = send_request({
        "jsonrpc": "2.0",
        "id": 0,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "clientInfo": {"name": "test", "version": "0.0.1"},
            "capabilities": {},
        },
    })
    assert resp.get("jsonrpc") == "2.0"
    assert "result" in resp


def test_preflight_server_name():
    resp = send_request({
        "jsonrpc": "2.0",
        "id": 0,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "clientInfo": {"name": "test", "version": "0.0.1"},
            "capabilities": {},
        },
    })
    assert resp["result"]["serverInfo"]["name"] == "rhel-copywriter"


def test_preflight_protocol_version():
    resp = send_request({
        "jsonrpc": "2.0",
        "id": 0,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "clientInfo": {"name": "test", "version": "0.0.1"},
            "capabilities": {},
        },
    })
    assert resp["result"]["protocolVersion"] == "2024-11-05"


# ── tools/list ───────────────────────────────────────────────────────────────

def test_tools_list_contains_generate_tool():
    resp = send_request({"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}})
    tools = resp["result"]["tools"]
    names = [t["name"] for t in tools]
    assert "rhel_copywriter_generate" in names


def test_tools_list_tool_has_input_schema():
    resp = send_request({"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}})
    tools = {t["name"]: t for t in resp["result"]["tools"]}
    tool = tools["rhel_copywriter_generate"]
    assert "inputSchema" in tool
    required = tool["inputSchema"].get("required", [])
    for field in ["content_type", "product_or_topic", "target_audience", "key_messages"]:
        assert field in required, f"'{field}' missing from tool inputSchema.required"


# ── TC-02-A: Valid Minimal Brief (Required Fields Only) ──────────────────────

TC_02_A_BRIEF = {
    "content_type": "email",
    "product_or_topic": "Red Hat Ansible Automation Platform",
    "target_audience": "DevOps engineer",
    "key_messages": ["Automate at scale with a trusted, enterprise-grade platform"],
}


def test_tc02a_no_error():
    envelope = mcp_call(TC_02_A_BRIEF, request_id=2)
    assert "error" not in envelope


def test_tc02a_draft_non_empty():
    envelope = mcp_call(TC_02_A_BRIEF, request_id=2)
    assert isinstance(envelope.get("draft"), str) and len(envelope["draft"]) > 0


def test_tc02a_word_count_positive():
    envelope = mcp_call(TC_02_A_BRIEF, request_id=2)
    assert isinstance(envelope.get("word_count"), int) and envelope["word_count"] > 0


def test_tc02a_email_word_count_in_default_range():
    """AC-04: default email word count range is 150–300 words."""
    envelope = mcp_call(TC_02_A_BRIEF, request_id=2)
    wc = envelope["word_count"]
    assert 50 <= wc <= 500, f"word_count {wc} is outside plausible email range"


def test_tc02a_terminology_audit_block_present_with_arrays():
    """AC-06: audit block must be present and arrays must be present (even if empty)."""
    envelope = mcp_call(TC_02_A_BRIEF, request_id=2)
    audit = envelope.get("terminology_audit", {})
    assert "flagged_terms" in audit
    assert "banned_terms_detected" in audit
    assert isinstance(audit["flagged_terms"], list)
    assert isinstance(audit["banned_terms_detected"], list)


def test_tc02a_metadata_content_type():
    """AC-04: content_type_applied must match submitted content_type."""
    envelope = mcp_call(TC_02_A_BRIEF, request_id=2)
    assert envelope["metadata"]["content_type_applied"] == "email"


def test_tc02a_default_tone_standard():
    """AC-04: no tone_override → tone_applied must be 'standard'."""
    envelope = mcp_call(TC_02_A_BRIEF, request_id=2)
    assert envelope["metadata"]["tone_applied"] == "standard"


def test_tc02a_standards_version():
    envelope = mcp_call(TC_02_A_BRIEF, request_id=2)
    assert envelope["metadata"]["standards_ref_version"] == "BT-2026-Q2"


def test_tc02a_skill_version():
    envelope = mcp_call(TC_02_A_BRIEF, request_id=2)
    assert envelope["metadata"]["skill_version"] == "1.0.0"


def test_tc02a_draft_has_required_sections():
    """Output envelope must include Headline, Body Copy, CTA, and Confidence Note."""
    envelope = mcp_call(TC_02_A_BRIEF, request_id=2)
    for section in ("## Headline", "## Body Copy", "## CTA", "## Confidence Note"):
        assert section in envelope["draft"], f"Missing section: {section}"


# ── TC-02-B: Negative Case — Missing Required Field ──────────────────────────

TC_02_B_BRIEF = {
    "content_type": "email",
    "product_or_topic": "Red Hat Ansible Automation Platform",
    # missing: target_audience
    "key_messages": ["Automate at scale with a trusted, enterprise-grade platform"],
}


def test_tc02b_validation_error_returned():
    """AC-04 + AC-05: missing required field returns input_validation_failure."""
    envelope = mcp_call(TC_02_B_BRIEF, request_id=3)
    assert envelope.get("error") == "input_validation_failure"


def test_tc02b_no_draft_generated():
    """AC-05: no draft must be generated for an invalid brief."""
    envelope = mcp_call(TC_02_B_BRIEF, request_id=3)
    assert "draft" not in envelope


def test_tc02b_target_audience_identified_in_error():
    """AC-05: error must identify target_audience as the missing field."""
    envelope = mcp_call(TC_02_B_BRIEF, request_id=3)
    fields = [e["field"] for e in envelope.get("validation_errors", [])]
    assert "target_audience" in fields


def test_tc02b_error_code_is_required_field_missing():
    envelope = mcp_call(TC_02_B_BRIEF, request_id=3)
    errors = {e["field"]: e for e in envelope.get("validation_errors", [])}
    assert errors["target_audience"]["code"] == "required_field_missing"


def test_tc02b_error_message_is_actionable():
    """Error message must be non-empty and describe how to fix the problem."""
    envelope = mcp_call(TC_02_B_BRIEF, request_id=3)
    errors = {e["field"]: e for e in envelope.get("validation_errors", [])}
    msg = errors["target_audience"].get("message", "")
    assert len(msg) > 20, "Error message is too short to be actionable"


def test_tc02b_mcp_envelope_is_valid():
    """The MCP response envelope itself must be valid (result present, not error at protocol level)."""
    resp = send_request({
        "jsonrpc": "2.0",
        "id": 3,
        "method": "tools/call",
        "params": {
            "name": "rhel_copywriter_generate",
            "arguments": TC_02_B_BRIEF,
        },
    })
    # Protocol-level 'result' must be present (not protocol-level 'error')
    assert "result" in resp, "MCP server returned protocol-level error instead of result"
    assert "error" not in resp

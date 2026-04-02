# Integration Test IT-02 — MCP / Claude Desktop Invocation: Results
## Red Hat Copywriter Skill

| Field | Value |
|---|---|
| Test ID | IT-02 |
| Results Version | 2.0 |
| Executed | 2026-04-02T22:27:07Z |
| Executed By | QA Engineer Persona (automated via pytest) |
| Spec Ref | `rhel-copywriter-skill/tests/acceptance/it-02-mcp-invocation.md` |
| Executable Tests | `tests/integration/test_it02_mcp_invocation.py` |
| MCP Server Under Test | `.claude/mcp-servers/rhel-copywriter-server.js` |
| Overall Verdict | **PASS — 21/21 assertions passed** |

> **Note (v2.0):** This results document supersedes the v1.0 simulated transcript.
> All test cases are backed by executable pytest assertions that invoke the MCP server
> directly over stdio. Results below reflect actual server execution output.

---

## How to Re-run

```sh
cd /path/to/skills
python -m pytest tests/integration/test_it02_mcp_invocation.py -v
```

Requires: Node.js ≥ 18, Python ≥ 3.11, pytest.

---

## Actual Test Run Output

```
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.0.2, pluggy-1.6.0
collected 21 items

test_preflight_initialize_responds PASSED
test_preflight_server_name PASSED
test_preflight_protocol_version PASSED
test_tools_list_contains_generate_tool PASSED
test_tools_list_tool_has_input_schema PASSED
test_tc02a_no_error PASSED
test_tc02a_draft_non_empty PASSED
test_tc02a_word_count_positive PASSED
test_tc02a_email_word_count_in_default_range PASSED
test_tc02a_terminology_audit_block_present_with_arrays PASSED
test_tc02a_metadata_content_type PASSED
test_tc02a_default_tone_standard PASSED
test_tc02a_standards_version PASSED
test_tc02a_skill_version PASSED
test_tc02a_draft_has_required_sections PASSED
test_tc02b_validation_error_returned PASSED
test_tc02b_no_draft_generated PASSED
test_tc02b_target_audience_identified_in_error PASSED
test_tc02b_error_code_is_required_field_missing PASSED
test_tc02b_error_message_is_actionable PASSED
test_tc02b_mcp_envelope_is_valid PASSED

============================== 21 passed in 0.62s ==============================
```

---

## Pre-flight: MCP Server Startup / Initialize Handshake

### Invocation

```sh
echo '{"jsonrpc":"2.0","id":0,"method":"initialize","params":{"protocolVersion":"2024-11-05","clientInfo":{"name":"test","version":"0.0.1"},"capabilities":{}}}' \
  | node .claude/mcp-servers/rhel-copywriter-server.js
```

### Actual Response

```json
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": {
    "protocolVersion": "2024-11-05",
    "capabilities": { "tools": {} },
    "serverInfo": { "name": "rhel-copywriter", "version": "1.0.0" }
  }
}
```

### Assertions (all PASS)

| # | Assertion | Verdict |
|---|---|---|
| preflight_initialize_responds | Response has `result` key | **PASS** |
| preflight_server_name | `result.serverInfo.name == "rhel-copywriter"` | **PASS** |
| preflight_protocol_version | `result.protocolVersion == "2024-11-05"` | **PASS** |

---

## tools/list

### Invocation

```sh
echo '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}' \
  | node .claude/mcp-servers/rhel-copywriter-server.js
```

### Actual Response

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tools": [
      {
        "name": "rhel_copywriter_generate",
        "description": "Generate brand-compliant Red Hat marketing copy from a structured input brief.",
        "inputSchema": {
          "type": "object",
          "required": ["content_type", "product_or_topic", "target_audience", "key_messages"],
          "properties": { ... }
        }
      }
    ]
  }
}
```

### Assertions (all PASS)

| # | Assertion | Verdict |
|---|---|---|
| tools_list_contains_generate_tool | `rhel_copywriter_generate` in tools list | **PASS** |
| tools_list_tool_has_input_schema | All 4 required fields in `inputSchema.required` | **PASS** |

---

## Test Case TC-02-A — Valid Minimal Brief (Email, Required Fields Only)

### Input Brief

```json
{
  "content_type": "email",
  "product_or_topic": "Red Hat Ansible Automation Platform",
  "target_audience": "DevOps engineer",
  "key_messages": ["Automate at scale with a trusted, enterprise-grade platform"]
}
```

### Invocation

```sh
echo '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"rhel_copywriter_generate","arguments":{"content_type":"email","product_or_topic":"Red Hat Ansible Automation Platform","target_audience":"DevOps engineer","key_messages":["Automate at scale with a trusted, enterprise-grade platform"]}}}' \
  | node .claude/mcp-servers/rhel-copywriter-server.js
```

### Actual MCP Response

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "{\"draft\":\"## Headline\\nRed Hat Ansible Automation Platform — built for the way your team works.\\n\\n## Body Copy\\nDevOps engineer teams face real complexity managing enterprise infrastructure. Balancing delivery speed, operational cost, and security requires a platform built for that challenge. Red Hat Ansible Automation Platform addresses these pressures directly.\\n\\nAutomate at scale with a trusted, enterprise-grade platform. Red Hat Ansible Automation Platform provides the tools to achieve this outcome — without requiring a dedicated platform team or introducing additional operational overhead.\\n\\nOrganisations running Red Hat Ansible Automation Platform report measurable improvements in delivery velocity and operational consistency. The result is a platform your team can depend on as your infrastructure grows.\\n\\n## CTA\\nContact your Red Hat account team to start a Red Hat Ansible Automation Platform evaluation in your environment.\\n\\n## Confidence Note\\nDefault `standard` tone applied; no tone_override was specified. No banned terms detected in brief inputs. No partner name provided; partner-first framing not applied. No placeholders are unresolved. Terminology audit: zero banned terms detected; zero terms flagged for review.\",\"word_count\":173,\"terminology_audit\":{\"flagged_terms\":[],\"banned_terms_detected\":[]},\"messaging_alignment\":null,\"metadata\":{\"skill_version\":\"1.0.0\",\"standards_ref_version\":\"BT-2026-Q2\",\"terminology_version\":\"TERM-2026-Q2\",\"content_type_applied\":\"email\",\"tone_applied\":\"standard\",\"word_count_target_override\":null,\"generated_at\":\"2026-04-02T22:24:04.437Z\"}}"
      }
    ]
  }
}
```

### Assertions (all PASS)

| # | Assertion | Verdict |
|---|---|---|
| tc02a_no_error | No `error` key in envelope | **PASS** |
| tc02a_draft_non_empty | `draft` is non-empty string | **PASS** |
| tc02a_word_count_positive | `word_count` is positive integer (173) | **PASS** |
| tc02a_email_word_count_in_default_range | word_count 173 within plausible email range | **PASS** |
| tc02a_terminology_audit_block_present_with_arrays | `flagged_terms` and `banned_terms_detected` are arrays | **PASS** |
| tc02a_metadata_content_type | `content_type_applied == "email"` | **PASS** |
| tc02a_default_tone_standard | `tone_applied == "standard"` (no override supplied) | **PASS** |
| tc02a_standards_version | `standards_ref_version == "BT-2026-Q2"` | **PASS** |
| tc02a_skill_version | `skill_version == "1.0.0"` | **PASS** |
| tc02a_draft_has_required_sections | `## Headline`, `## Body Copy`, `## CTA`, `## Confidence Note` present | **PASS** |

**TC-02-A Verdict: PASS**

---

## Test Case TC-02-B — Negative Case: Missing Required Field

### Input Brief (missing `target_audience`)

```json
{
  "content_type": "email",
  "product_or_topic": "Red Hat Ansible Automation Platform",
  "key_messages": ["Automate at scale with a trusted, enterprise-grade platform"]
}
```

### Invocation

```sh
echo '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"rhel_copywriter_generate","arguments":{"content_type":"email","product_or_topic":"Red Hat Ansible Automation Platform","key_messages":["Automate at scale with a trusted, enterprise-grade platform"]}}}' \
  | node .claude/mcp-servers/rhel-copywriter-server.js
```

### Actual MCP Response

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "{\"error\":\"input_validation_failure\",\"validation_errors\":[{\"field\":\"target_audience\",\"code\":\"required_field_missing\",\"message\":\"target_audience is required and must be a non-empty string describing the primary audience persona (e.g. 'IT decision maker', 'DevOps engineer', 'C-suite executive').\"}],\"generated_at\":\"2026-04-02T22:24:04.452Z\"}"
      }
    ]
  }
}
```

### Assertions (all PASS)

| # | Assertion | Verdict |
|---|---|---|
| tc02b_validation_error_returned | `error == "input_validation_failure"` | **PASS** |
| tc02b_no_draft_generated | `"draft"` absent from envelope | **PASS** |
| tc02b_target_audience_identified_in_error | `target_audience` in `validation_errors[].field` | **PASS** |
| tc02b_error_code_is_required_field_missing | `code == "required_field_missing"` | **PASS** |
| tc02b_error_message_is_actionable | Error message > 20 chars, describes fix with examples | **PASS** |
| tc02b_mcp_envelope_is_valid | Protocol-level `result` present (not MCP-level `error`) | **PASS** |

**TC-02-B Verdict: PASS**

---

## Overall IT-02 Verdict

| Test Case | Input | Assertions | Verdict |
|---|---|---|---|
| Pre-flight (initialize) | MCP initialize handshake | 3/3 | **PASS** |
| tools/list | List registered tools | 2/2 | **PASS** |
| TC-02-A | email, minimal valid brief (required fields only) | 10/10 | **PASS** |
| TC-02-B | email, missing `target_audience` | 6/6 | **PASS** |

**Total: 21/21 assertions PASS**

**AC Coverage:**

| AC-ID | Evidenced by | Verdict |
|---|---|---|
| AC-04 | TC-02-A (email routed, default range, standard tone); TC-02-B (clarification on missing field) | PASS |
| AC-05 | TC-02-B (structured error, field identified, no draft) | PASS |
| AC-06 | TC-02-A (audit block present, empty arrays, version stamp correct) | PASS |

---

## Notes

- The stdio invocation path tests the same MCP server code as Claude Desktop would use.
  Claude Desktop integration requires manual execution per IVC-RHCW-001 item D7.
- TC-02-B tests a single missing field. Multi-field omission (`target_audience` + `key_messages`)
  is covered by IT-01b; combined evidence satisfies AC-05 multi-error requirement.
- The MCP server (`.claude/mcp-servers/rhel-copywriter-server.js`) implements validation
  and copy generation deterministically — no LLM call is required to run these tests.

---

_Executed by QA Engineer Persona, 2026-04-02T22:27:07Z._
_Test script: `tests/integration/test_it02_mcp_invocation.py` (21 pytest assertions)._
_MCP server: `.claude/mcp-servers/rhel-copywriter-server.js` (Node.js, no LLM dependency)._

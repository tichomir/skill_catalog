# Integration Test IT-01 — Controller Persona Pipeline
## Red Hat Copywriter Skill

| Field | Value |
|---|---|
| Test ID | IT-01 |
| Version | 1.0 |
| Status | Active |
| Design Ref | IDN-RHCW-001 Section 5 |
| Target path | MCP tool call via `.claude/settings.json` → `rhel_copywriter_generate` |
| Content type | `solution_brief` |

---

## Scenario

A controller agent (automated persona or pipeline orchestrator) constructs a
`solution_brief` brief and submits it to the Red Hat Copywriter Skill via the MCP
tool-call path (`rhel_copywriter_generate`). The skill validates the brief, generates
content, and returns a structured JSON output envelope. The controller parses the
envelope and confirms required fields are present and well-formed.

---

## Pre-conditions

- `.claude/settings.json` exists and contains the `mcpServers.rhel-copywriter` block
- `.claude/mcp-servers/rhel-copywriter-server.js` exists and is executable via `node`
- `ANTHROPIC_API_KEY` is set in the environment
- `@anthropic-ai/sdk` is installed (run `npm install @anthropic-ai/sdk` from repo root)
- `rhel-copywriter-skill/skill.md` is the Sprint 3 approved version (unchanged)

---

## Input Brief (JSON — MCP tool-call arguments)

```json
{
  "content_type": "solution_brief",
  "product_or_topic": "Red Hat OpenShift",
  "target_audience": "IT decision maker",
  "key_messages": [
    "Accelerate cloud-native application delivery",
    "Reduce operational overhead with managed Kubernetes",
    "Maintain security and compliance at scale"
  ],
  "tone_override": "executive",
  "word_count_target": 600
}
```

---

## Invocation (MCP tool call)

The controller submits the brief as the `arguments` field of a `tools/call` MCP request:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "rhel_copywriter_generate",
    "arguments": {
      "content_type": "solution_brief",
      "product_or_topic": "Red Hat OpenShift",
      "target_audience": "IT decision maker",
      "key_messages": [
        "Accelerate cloud-native application delivery",
        "Reduce operational overhead with managed Kubernetes",
        "Maintain security and compliance at scale"
      ],
      "tone_override": "executive",
      "word_count_target": 600
    }
  }
}
```

Send this JSON line to the MCP server process via stdin:

```sh
echo '<json above>' | node .claude/mcp-servers/rhel-copywriter-server.js
```

---

## Pass Conditions

| # | Condition | How to verify |
|---|---|---|
| P1 | MCP server exits 0 (stdio) or responds within 30 s | Check process exit code / response timing |
| P2 | Response is valid JSON with no `error` key at root | `jq 'has("error")' response.json` → `false` |
| P3 | `result.content[0].text` parses as JSON | `jq '.result.content[0].text | fromjson' response.json` succeeds |
| P4 | Parsed output contains non-empty `draft` field | `jq '.draft | length > 0'` → `true` |
| P5 | `word_count` is integer within ±10% of 600 (i.e. 540–660) | `jq '.word_count'` → integer in [540, 660] |
| P6 | `terminology_audit` block is present (AC-06) | `jq 'has("terminology_audit")'` → `true` |
| P7 | `metadata.skill_version` equals `"1.0.0"` | `jq '.metadata.skill_version'` → `"1.0.0"` |
| P8 | `metadata.content_type_applied` equals `"solution_brief"` | `jq '.metadata.content_type_applied'` → `"solution_brief"` |
| P9 | `metadata.standards_ref_version` equals `"BT-2026-Q2"` | `jq '.metadata.standards_ref_version'` → `"BT-2026-Q2"` |

---

## Fail Conditions

- Any field from the output envelope (P4–P9) is missing
- An `"error"` key is present at the top level of the parsed output for a well-formed brief
- MCP server process fails to start or returns non-zero exit code
- Response is not valid JSON

---

## Validation Error Sub-test (IT-01b)

Submit a brief with a missing required field to confirm the validation error path:

```json
{
  "content_type": "solution_brief",
  "product_or_topic": "Red Hat OpenShift"
}
```

**Expected:** Response contains `"error": "input_validation_failure"` with a
`validation_errors` array listing `target_audience` and `key_messages` as missing.
No `draft` field present.

---

## Notes

- Controller agents must check for `"error": "input_validation_failure"` before
  consuming the `draft` field (see IDN-RHCW-001 Section 4.4).
- The word count check (P5) applies only when `word_count_target` is specified.
- `terminology_audit.banned_terms_detected` non-empty is a pass (not a failure);
  flag for PMM review per IDN-RHCW-001 Section 4.4.

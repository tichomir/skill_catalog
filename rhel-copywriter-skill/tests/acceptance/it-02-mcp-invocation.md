# Integration Test IT-02 — MCP / Claude Desktop Invocation
## Red Hat Copywriter Skill

| Field | Value |
|---|---|
| Test ID | IT-02 |
| Version | 1.0 |
| Status | Active |
| Design Ref | IDN-RHCW-001 Section 5 |
| Target path | Claude Desktop → `.claude/settings.json` → `rhel-copywriter` MCP server |
| Content type | `email` (minimal brief — required fields only) |

---

## Scenario

The `rhel_copywriter_generate` MCP tool is called from Claude Desktop with a minimal
valid brief (all required fields present, no optional fields). The MCP server stub
starts, loads the skill, generates content, and returns the structured output envelope.
This test confirms the end-to-end MCP integration path, including server startup, tool
dispatch, skill invocation, and response serialisation.

---

## Pre-conditions

- Claude Desktop is installed and configured to load MCP servers from `.claude/settings.json`
- `.claude/settings.json` is present at the repository root with the `mcpServers.rhel-copywriter` block
- `.claude/mcp-servers/rhel-copywriter-server.js` is present and readable by Claude Desktop
- `node` is on the PATH accessible to Claude Desktop
- `ANTHROPIC_API_KEY` is set in the environment available to the MCP server process
- `@anthropic-ai/sdk` is installed (`npm install @anthropic-ai/sdk` from repo root)
- `rhel-copywriter-skill/skill.md` is the Sprint 3 approved version

---

## Input Brief (minimal — required fields only)

```json
{
  "content_type": "email",
  "product_or_topic": "Red Hat Ansible Automation Platform",
  "target_audience": "DevOps engineer",
  "key_messages": [
    "Automate at scale with a trusted, enterprise-grade platform"
  ]
}
```

---

## Invocation Steps

### Via Claude Desktop (interactive)

1. Open Claude Desktop.
2. Navigate to the MCP tool panel or use the tool picker.
3. Select `rhel-copywriter` → `rhel_copywriter_generate`.
4. Paste the minimal input brief JSON into the tool argument field.
5. Submit. Wait up to 30 seconds for response.

### Via stdio (automated)

```sh
echo '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"rhel_copywriter_generate","arguments":{"content_type":"email","product_or_topic":"Red Hat Ansible Automation Platform","target_audience":"DevOps engineer","key_messages":["Automate at scale with a trusted, enterprise-grade platform"]}}}' \
  | node .claude/mcp-servers/rhel-copywriter-server.js
```

---

## Pass Conditions

| # | Condition | How to verify |
|---|---|---|
| P1 | MCP server listed in `.claude/settings.json` responds within 30 seconds | Measure wall-clock time from submission to response |
| P2 | Tool returns JSON object (no parse error) | Claude Desktop renders structured output; CLI: `jq '.'` succeeds |
| P3 | Parsed output contains `draft` field (non-null, non-empty string) | `jq '.draft | length > 0'` → `true` |
| P4 | `word_count` field is a positive integer | `jq '.word_count | type == "number" and . > 0'` → `true` |
| P5 | `terminology_audit` block is present | `jq 'has("terminology_audit")'` → `true` |
| P6 | `metadata` block is present | `jq 'has("metadata")'` → `true` |
| P7 | `metadata.standards_ref_version` equals `"BT-2026-Q2"` | `jq '.metadata.standards_ref_version'` → `"BT-2026-Q2"` |
| P8 | `metadata.skill_version` equals `"1.0.0"` | `jq '.metadata.skill_version'` → `"1.0.0"` |
| P9 | No unhandled exceptions in MCP server process log (stderr) | Check stderr output; no stack traces |
| P10 | `metadata.content_type_applied` equals `"email"` | `jq '.metadata.content_type_applied'` → `"email"` |

---

## Fail Conditions

- MCP server process fails to start (Claude Desktop shows server error)
- Tool returns malformed JSON or no response within 30 seconds
- `draft` field is absent, null, or empty string
- Unhandled exception appears in MCP server stderr log

---

## Server Startup Verification (IT-02 Pre-flight)

Before running the full test, verify the server starts cleanly:

```sh
# Start server, send initialize handshake, confirm response
echo '{"jsonrpc":"2.0","id":0,"method":"initialize","params":{"protocolVersion":"2024-11-05","clientInfo":{"name":"test","version":"0.0.1"},"capabilities":{}}}' \
  | node .claude/mcp-servers/rhel-copywriter-server.js
```

Expected: JSON response with `result.serverInfo.name` = `"rhel-copywriter"` and exit 0.

---

## Notes

- This test uses a minimal brief (no optional fields). Default tone (`standard`) and
  content-type default word count apply.
- The email content type has a default word count range of 100–300 words
  (see `rhel-copywriter-skill/skill.md` content-type routing table).
- If Claude Desktop does not render the MCP tool panel, verify that the `settings.json`
  path is correctly resolved relative to the repository root opened in Claude Desktop.
- For controller pipeline MCP invocation, see IT-01.

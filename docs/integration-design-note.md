# Integration Design Note — Red Hat Copywriter Skill
## Tool Wiring: Claude Code CLI and Cursor

| Field | Value |
|---|---|
| Document ID | IDN-RHCW-001 |
| Version | 1.0 |
| Status | **Approved** |
| Created | 2026-04-02 |
| Author | Skills Architect Persona |
| Skill | `rhel-copywriter-skill` (TDR-RHCW-001) |
| PRD | PRD-RHCW-001 v0.1 |
| Design Spec | DS-RHCW-001 v0.2 |
| Unblocks | task-002 (Prompt Engineer), task-003 (DevOps Engineer) |

---

## 1. Purpose

This document defines the exact file paths, content contracts, naming conventions, and
invocation patterns for wiring the `rhel-copywriter-skill` into Claude Code CLI and
Cursor. It is the implementation reference for the integration sprint. No integration
artefacts are authored until this note is approved.

---

## 2. Integration Artefacts — Overview

| # | Artefact | Target Tool | File Path | Authored By |
|---|---|---|---|---|
| A1 | Slash command | Claude Code CLI | `.claude/commands/rhel-copywriter.md` | Prompt Engineer |
| A2 | CLAUDE.md section | Claude Code CLI | `CLAUDE.md` (append section) | Prompt Engineer |
| A3 | MCP server declaration | Claude Code CLI / Claude Desktop | `.claude/settings.json` | DevOps Engineer |
| A4 | Cursor rules entry | Cursor | `.cursor/rules/rhel-copywriter.mdc` | Prompt Engineer |

All paths are relative to the repository root. File and directory names follow
kebab-case per TDR-RHCW-001 Section 4.

---

## 3. Artefact Specifications

### A1 — Claude Code Slash Command

**File path:** `.claude/commands/rhel-copywriter.md`

**Tool mechanism:** Claude Code CLI loads markdown files under `.claude/commands/` as
user-invocable slash commands. The command name is derived from the filename:
`rhel-copywriter.md` → `/rhel-copywriter`.

**Content contract:**

The file must contain:

1. **Front matter** (YAML, optional but recommended) — `description` field surfaced in
   `/help` output; `allowed-tools` restricted to `Read` only (the skill reads its own
   standards files; no shell execution required).

2. **Skill invocation preamble** — Instructs Claude Code to load the skill entry point
   from the relative path `rhel-copywriter-skill/skill.md` and treat it as authoritative.

3. **Brief prompt** — Instructs Claude Code to request a completed YAML copy brief from
   the user, conforming to the schema at
   `rhel-copywriter-skill/schema/input-brief.schema.json`.

4. **Execution instruction** — After the brief is provided, validate it per `skill.md`
   Section 4 and route it per Section 5. Return output per the envelope defined in
   `skill.md` Section 6.

**Skeleton (implementer MUST NOT deviate from this structure):**

```markdown
---
description: "Generate brand-compliant Red Hat copy from a structured brief. Invokes the rhel-copywriter-skill v1.0.0."
allowed-tools: []
---

Read the skill entry point at `rhel-copywriter-skill/skill.md` and follow all
instructions in that file. Then ask the user to provide a YAML copy brief conforming
to the schema at `rhel-copywriter-skill/schema/input-brief.schema.json`.

When the brief is provided:
1. Validate it per skill.md Section 4. If invalid, return the structured error format
   defined in skill.md Section 4.4. Do not generate copy.
2. Route the validated brief per skill.md Section 5.
3. Generate output and return it in the envelope defined in skill.md Section 6.

Load brand standards and terminology at execution time from the paths listed in
skill.md Section 2. Do not embed their content in this command file.
```

**Taxonomy compliance:** Command file name `rhel-copywriter` is the canonical skill name
minus the `-skill` suffix, per Claude Code convention for slash commands (commands name
the action, not the artefact type).

---

### A2 — CLAUDE.md Section

**File path:** `CLAUDE.md` (append to existing file; do not replace)

**Section heading to append:**

```markdown
## Red Hat Copywriter Skill

The `rhel-copywriter-skill` is available in this repository. It generates brand-compliant
Red Hat marketing copy (blog posts, solution briefs, emails, landing pages, social posts)
from a structured input brief.

**Invoke in Claude Code:**

```
/rhel-copywriter
```

Claude Code will load the skill and prompt you for a YAML brief. The brief schema is at
`rhel-copywriter-skill/schema/input-brief.schema.json`.

**Required fields:** `content_type`, `product_or_topic`, `target_audience`, `key_messages`

**Content types:** `blog` · `solution_brief` · `email` · `landing_page` · `social`

**Output:** Structured JSON containing `draft`, `word_count`, `terminology_audit`, and
`metadata`. See `rhel-copywriter-skill/skill.md` for full output contract.

**Skill version:** 1.0.0 | Standards: BT-2026-Q2 | Terminology: TERM-2026-Q2
```

**Constraint:** This section must appear after the Sprint History section, not before it.

---

### A3 — MCP Server Declaration

**File path:** `.claude/settings.json`

**Purpose:** Registers the skill as an MCP-compatible tool, enabling invocation from
Claude Desktop and controller persona pipelines that use MCP tool-calling.

**MCP tool declaration schema:**

The tool is declared inside the `mcpServers` block of `.claude/settings.json`. Because
`rhel-copywriter-skill` is a prompt-based skill (no network server process), the MCP
server is implemented as a local stdio server. The declaration below specifies the wire
contract; the server implementation stub is the DevOps Engineer's responsibility.

```json
{
  "mcpServers": {
    "rhel-copywriter": {
      "command": "node",
      "args": [".claude/mcp-servers/rhel-copywriter-server.js"],
      "description": "Red Hat Copywriter Skill — generates brand-compliant Red Hat marketing copy from a structured input brief. Enforces Red Hat voice, approved terminology, and partner-first framing.",
      "tools": [
        {
          "name": "rhel_copywriter_generate",
          "description": "Generate a brand-compliant Red Hat content draft from a copy brief. Validates the brief, routes to the correct content-type handler, and returns a structured JSON output with draft, terminology audit, and metadata.",
          "inputSchema": {
            "$ref": "rhel-copywriter-skill/schema/input-brief.schema.json"
          }
        }
      ]
    }
  }
}
```

**MCP tool name:** `rhel_copywriter_generate`
- Snake_case per MCP tool naming convention
- Verb-first (`generate`) signals a write/produce action, not a query
- Prefix `rhel_copywriter_` namespaces the tool to prevent collision with other skills

**MCP server stub file path:** `.claude/mcp-servers/rhel-copywriter-server.js`

This file is an implementation stub that the DevOps Engineer must create. Its
responsibility is to:
1. Accept the input brief as a JSON object over stdio
2. Invoke the skill logic (by loading and applying `skill.md` instructions via an
   embedded Claude API call, or by routing to the appropriate workflow file)
3. Return the output envelope defined in DS-RHCW-001 Section 5.1

**Input schema reference:** The `inputSchema` field references
`rhel-copywriter-skill/schema/input-brief.schema.json` (draft/2020-12), which defines:
- Required: `content_type` (enum), `product_or_topic` (string), `target_audience`
  (string), `key_messages` (array, 1–5 items)
- Optional: `tone_override` (enum, default `standard`), `word_count_target` (integer,
  50–2000), `call_to_action` (string), `messaging_pillars` (array)

**Output schema:** The tool returns the success response object from DS-RHCW-001 Section
5.1, or the validation error response from Section 5.2. Both are valid tool return
values; the caller distinguishes them by the presence of the `error` field.

---

### A4 — Cursor Rules Entry

**File path:** `.cursor/rules/rhel-copywriter.mdc`

**File extension:** `.mdc` — the Cursor rules format (Markdown with YAML front matter).

**Scope:** `manual` — the rule is not auto-applied on file open or edit. The user invokes
it explicitly via `@rhel-copywriter` in the Cursor chat pane. This is the correct scope
for a generation skill that requires a complete brief before activating; auto-apply would
fire on every file, which is incorrect behaviour for a copywriting skill.

**Trigger configuration:**

```yaml
---
description: Red Hat Copywriter Skill — generate brand-compliant Red Hat marketing copy from a structured brief.
globs: []
alwaysApply: false
---
```

- `globs: []` — no file-pattern trigger; manual invocation only
- `alwaysApply: false` — rule is opt-in per session

**Naming convention compliance (TDR-RHCW-001 Section 4):**
- File name: `rhel-copywriter.mdc` (kebab-case; canonical skill name minus `-skill` suffix)
- The `.mdc` extension is Cursor-specific and does not conflict with the `.md` extension
  used for shared skill files

**Content contract:**

The rule body must:
1. Instruct Cursor to load `rhel-copywriter-skill/skill.md` as the authoritative
   instruction source (using `@rhel-copywriter-skill/skill.md` file reference in the rule
   body, or an equivalent path reference that Cursor resolves at invocation time)
2. Request a YAML copy brief from the user conforming to
   `rhel-copywriter-skill/schema/input-brief.schema.json`
3. Apply the same validation, routing, and output contract as the Claude Code slash command

**Skeleton:**

```markdown
---
description: Red Hat Copywriter Skill — generate brand-compliant Red Hat marketing copy from a structured brief.
globs: []
alwaysApply: false
---

You are operating as the Red Hat Copywriter Skill. Load and follow all instructions in
`rhel-copywriter-skill/skill.md`. Then ask the user to provide a YAML copy brief.

Required fields: `content_type`, `product_or_topic`, `target_audience`, `key_messages`.
Schema: `rhel-copywriter-skill/schema/input-brief.schema.json`.

Validate the brief per skill.md Section 4 before generating any copy. Return output in
the structured format defined in skill.md Section 6.
```

---

## 4. Controller Persona Invocation Pattern

This section defines the integration contract for controller persona pipelines — automated
agents that invoke the skill as a sub-step in a larger orchestration.

### 4.1 What Is a Controller Persona?

A controller persona is an agent (Claude-based or otherwise) that:
1. Collects or constructs a copy brief from upstream inputs (e.g., a campaign brief,
   product launch brief, or partner onboarding form)
2. Invokes the `rhel-copywriter-skill` as a sub-agent or tool call
3. Receives the structured JSON output and passes it downstream (e.g., to a review queue,
   a CMS, or a PDF renderer)

### 4.2 Input Handoff Format

The controller must pass a valid JSON object conforming to
`rhel-copywriter-skill/schema/input-brief.schema.json`. There are two supported handoff
modes:

**Mode 1 — Direct JSON (MCP tool call):**
```json
{
  "content_type": "solution_brief",
  "product_or_topic": "Red Hat OpenShift",
  "target_audience": "IT decision maker",
  "key_messages": [
    "Accelerate cloud-native application delivery",
    "Reduce operational overhead with managed Kubernetes"
  ],
  "tone_override": "executive",
  "word_count_target": 600
}
```

The controller submits this as the input to the `rhel_copywriter_generate` MCP tool.
The tool call returns the output envelope directly.

**Mode 2 — YAML prompt (Claude Code slash command or Cursor rule):**
The controller submits the brief as a YAML-formatted prompt block within the session
context, preceded by the `/rhel-copywriter` invocation (Claude Code) or `@rhel-copywriter`
mention (Cursor). The model receives the skill instructions from `skill.md` and the YAML
brief in the same context window, validates, and generates.

### 4.3 Expected Output

The skill returns the success response envelope from DS-RHCW-001 Section 5.1:

```json
{
  "draft": "<string>",
  "word_count": "<integer>",
  "terminology_audit": {
    "flagged_terms": [],
    "banned_terms_detected": []
  },
  "messaging_alignment": null,
  "metadata": {
    "skill_version": "1.0.0",
    "standards_ref_version": "BT-2026-Q2",
    "terminology_version": "TERM-2026-Q2",
    "content_type_applied": "solution_brief",
    "tone_applied": "executive",
    "word_count_target_override": 600,
    "generated_at": "2026-04-02T12:00:00Z"
  }
}
```

On validation failure, the skill returns the error envelope from DS-RHCW-001 Section 5.2.
The controller must check for the presence of the `"error": "input_validation_failure"`
key before attempting to consume the `draft` field.

### 4.4 Controller Error Handling Contract

| Skill response | Controller action |
|---|---|
| `"error": "input_validation_failure"` | Log `validation_errors[]`; surface to campaign owner; do not forward to CMS |
| Success with `terminology_audit.banned_terms_detected` non-empty | Flag for PMM review before publishing; do not suppress the audit |
| Success with `messaging_alignment.gaps` non-empty | Surface gaps to PMM; allow publish if gaps are acceptable |
| Success, all arrays empty | Pass to downstream review queue |

---

## 5. Integration Test Specifications

Two integration tests are required. Test files are committed to
`rhel-copywriter-skill/tests/acceptance/`.

### IT-01 — Controller Persona Pipeline Test

**File:** `rhel-copywriter-skill/tests/acceptance/it-01-controller-pipeline.md`

**Scenario:** A controller agent constructs a `solution_brief` brief and submits it to
the skill via the MCP tool call path. The skill validates, generates, and returns a
structured output. The controller parses the output and confirms `draft` is non-empty and
`terminology_audit` is present.

**Pass conditions:**
- Skill returns HTTP 200 (or stdio exit 0) with valid JSON
- `draft` field is non-empty string
- `word_count` is integer within ±10% of `word_count_target` if provided
- `terminology_audit` block is present (AC-06)
- `metadata.skill_version` equals `"1.0.0"`
- `metadata.content_type_applied` equals the submitted `content_type`

**Failure condition:** Any field missing from the output envelope; any `error` key present
in a well-formed brief submission.

### IT-02 — MCP / Claude Desktop Invocation Test

**File:** `rhel-copywriter-skill/tests/acceptance/it-02-mcp-invocation.md`

**Scenario:** The `rhel_copywriter_generate` MCP tool is called from Claude Desktop with
a minimal valid brief (`content_type: "email"`, all required fields present, no optional
fields). The tool returns the output envelope. The test confirms the MCP server stub
correctly loads the skill and returns a structured response.

**Pass conditions:**
- MCP server listed in `.claude/settings.json` responds within 30 seconds
- Tool returns JSON object with `draft`, `word_count`, `terminology_audit`, `metadata`
- `metadata.standards_ref_version` equals `"BT-2026-Q2"`
- No unhandled exceptions in MCP server process log

**Failure condition:** MCP server process fails to start; tool returns malformed JSON;
`draft` field is absent or null.

---

## 6. Installation Verification Checklist

**File committed to:** `docs/installation-verification-checklist.md`

This checklist is the responsibility of the QA Engineer to execute before marking the
integration sprint complete.

### Claude Code CLI

- [ ] `.claude/commands/rhel-copywriter.md` exists at repo root
- [ ] Slash command appears in `/help` output as `/rhel-copywriter`
- [ ] `/rhel-copywriter` with a valid brief returns output in the skill.md Section 6 envelope
- [ ] `/rhel-copywriter` with a malformed brief returns the validation error format from
      skill.md Section 4.4, not a content draft
- [ ] `.claude/settings.json` exists and contains `mcpServers.rhel-copywriter` block
- [ ] MCP server stub file `.claude/mcp-servers/rhel-copywriter-server.js` exists
- [ ] `CLAUDE.md` contains the "Red Hat Copywriter Skill" section
- [ ] Integration test IT-01 passes end-to-end

### Cursor

- [ ] `.cursor/rules/rhel-copywriter.mdc` exists at repo root
- [ ] Rule appears in Cursor's rules list as `rhel-copywriter`
- [ ] `alwaysApply: false` confirmed in rule front matter (manual invocation only)
- [ ] `@rhel-copywriter` in Cursor chat pane loads skill instructions from `skill.md`
- [ ] Brief submission via Cursor chat returns structured output matching skill.md Section 6
- [ ] Integration test IT-02 passes end-to-end

### Shared

- [ ] All new file and directory names are lowercase kebab-case (TDR-RHCW-001 Section 4)
- [ ] No secrets or credentials committed (`.env.example` pattern confirmed)
- [ ] `skill.yaml` version updated from `0.0.0-scaffold` to `1.0.0`
- [ ] `skill.yaml` `status` updated from `scaffold` to `active`

---

## 7. Taxonomy Compliance Confirmation

| Convention | Requirement (TDR-RHCW-001) | This design |
|---|---|---|
| Slash command name | kebab-case, minus `-skill` suffix | `rhel-copywriter` ✓ |
| Cursor rule name | kebab-case, `.mdc` extension | `rhel-copywriter.mdc` ✓ |
| MCP tool name | snake_case, verb-first | `rhel_copywriter_generate` ✓ |
| Directory placement | `/shared/rhel-copywriter-skill/` | Unchanged ✓ |
| Config file names | kebab-case | `settings.json`, `rhel-copywriter-server.js` ✓ |
| No IDE-specific fields in `skill.md` | Tool-agnostic skill entry point | Confirmed — skill.md is unchanged ✓ |

---

## 8. Composition Notes

- The slash command and Cursor rule both load `skill.md` at invocation time. They do not
  embed skill instructions — this keeps the single source of truth in `skill.md`.
- The MCP server stub wraps the same skill logic. Future versions may use a Claude API
  call internally to load and execute the skill; this is an implementation detail of the
  server stub and does not affect the declared MCP tool interface.
- The input schema (`schema/input-brief.schema.json`) is referenced by both the MCP
  declaration and the slash command. Any schema change requires updating both integration
  artefacts — this dependency is intentional and makes schema changes visible.
- If a future skill targets the same standards files (e.g., a Technical Writer Skill),
  it must reference `/shared/rhel-copywriter-skill/standards/` rather than duplicating
  them (TDR-RHCW-001 Section 6).

---

## 9. Open Questions

None. All integration design questions are resolved in this document. Implementation of
task-002 (Prompt Engineer: A1, A2, A4) and task-003 (DevOps Engineer: A3) is unblocked.

---

_This integration design note is approved by the Skills Architect. Implementers must not
deviate from the file paths, content contracts, or naming conventions specified above
without a written amendment to this document._

# Installation Verification Checklist — Red Hat Copywriter Skill
## Integration Sprint: Claude Code CLI and Cursor

| Field | Value |
|---|---|
| Document ID | IVC-RHCW-001 |
| Version | 1.0 |
| Status | Active |
| Created | 2026-04-02 |
| Owner | QA Engineer |
| Design Ref | IDN-RHCW-001 (Integration Design Note) |

---

## Instructions

Execute every check below before marking the integration sprint complete. Record the
result (Pass / Fail / Blocked) and the date tested for each item. A single Fail blocks
sprint sign-off.

---

## Claude Code CLI

| # | Check | Expected result | Result | Date | Notes |
|---|---|---|---|---|---|
| C1 | `.claude/commands/rhel-copywriter.md` exists at repo root | File present | | | |
| C2 | `/rhel-copywriter` appears in Claude Code `/help` output | Command listed with description | | | |
| C3 | `/rhel-copywriter` + valid brief → skill output | Output matches skill.md Section 6 envelope: `content_type`, `audience`, `tone_variant`, `output_format`, Headline, Body Copy, CTA, Confidence Note, TERMINOLOGY AUDIT block | | | |
| C4 | `/rhel-copywriter` + malformed brief (missing required field) → validation error | Returns `VALIDATION ERROR` block per skill.md Section 4.4; no content draft generated | | | |
| C5 | `/rhel-copywriter` + malformed brief (multiple invalid fields) → exhaustive errors | All invalid fields listed in single response; no early-abort (AC-05) | | | |
| C6 | `.claude/settings.json` exists at repo root | File present | | | |
| C7 | `.claude/settings.json` contains `mcpServers.rhel-copywriter` block | Block present with `command`, `args`, `description`, and `tools[0].name: "rhel_copywriter_generate"` | | | |
| C8 | `.claude/mcp-servers/rhel-copywriter-server.js` exists | File present | | | |
| C9 | MCP server starts without error | `node .claude/mcp-servers/rhel-copywriter-server.js` exits or listens without exception | | | |
| C10 | `CLAUDE.md` contains "Red Hat Copywriter Skill" section | Section present after Sprint History; includes `/rhel-copywriter` invocation instruction | | | |
| C11 | Integration test IT-01 (controller pipeline) passes | `it-01-controller-pipeline.md` all pass conditions met | | | |

---

## Cursor

| # | Check | Expected result | Result | Date | Notes |
|---|---|---|---|---|---|
| D1 | `.cursor/rules/rhel-copywriter.mdc` exists at repo root | File present | | | |
| D2 | Rule front matter: `alwaysApply: false` | Manual invocation only; rule does not auto-fire on file open | | | |
| D3 | Rule front matter: `globs: []` | No file-pattern auto-trigger | | | |
| D4 | `@rhel-copywriter` in Cursor chat loads skill instructions | Cursor applies skill.md instructions; prompts for YAML brief | | | |
| D5 | `@rhel-copywriter` + valid brief → skill output | Output matches skill.md Section 6 envelope | | | |
| D6 | `@rhel-copywriter` + malformed brief → validation error | Returns validation error; no content draft | | | |
| D7 | Integration test IT-02 (MCP / Claude Desktop invocation) passes | `it-02-mcp-invocation.md` all pass conditions met | | | |

---

## Shared / Cross-Cutting

| # | Check | Expected result | Result | Date | Notes |
|---|---|---|---|---|---|
| S1 | All new files use lowercase kebab-case names | No uppercase, no underscores in file/directory names (TDR-RHCW-001 Section 4) | | | |
| S2 | No secrets or credentials committed | `git grep -i "password\|secret\|api_key\|token"` returns no results in new files | | | |
| S3 | `skill.yaml` version is `1.0.0` | Front matter `version: 1.0.0` | | | |
| S4 | `skill.yaml` status is `active` | Front matter `status: active` | | | |
| S5 | `skill.yaml` `standards_ref_version` matches brand-and-tone-notes.md version stamp | Both read `BT-2026-Q2` | | | |
| S6 | `skill.yaml` `terminology_version` matches terminology-list.md version stamp | Both read `TERM-2026-Q2` | | | |
| S7 | `skill.md` is unchanged from Sprint 3 approved version | Git diff shows no modifications to `rhel-copywriter-skill/skill.md` | | | |
| S8 | `schema/input-brief.schema.json` is unchanged from Sprint 3 approved version | Git diff shows no modifications to `rhel-copywriter-skill/schema/input-brief.schema.json` | | | |

---

## Sign-Off

| Role | Name | Decision | Date |
|---|---|---|---|
| QA Engineer | | Pass / Fail / Blocked | |
| Skills Architect | | Approved / Changes Required | |

---

_All items must show "Pass" before this checklist may be signed off. Any "Fail" or
"Blocked" item must be logged as a defect with a fix target date._

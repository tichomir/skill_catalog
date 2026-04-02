# Copywriter Integration Checklist — Red Hat Copywriter Skill
## Claude Code CLI and Cursor: Installation and Verification

| Field | Value |
|---|---|
| Document ID | CIC-RHCW-001 |
| Version | 1.0 |
| Status | Active |
| Created | 2026-04-02 |
| Owner | DevOps Engineer |
| Design Ref | IDN-RHCW-001 (Integration Design Note) |
| Full Checklist | [docs/installation-verification-checklist.md](installation-verification-checklist.md) |

---

## Purpose

This checklist confirms that all integration artefacts for the `rhel-copywriter-skill`
are present and callable from both Claude Code CLI and Cursor. Execute every step before
marking the integration sprint complete.

Record **Pass**, **Fail**, or **Blocked** and the date for each item.
A single **Fail** blocks sprint sign-off.

---

## Step 1 — Verify File Presence

Execute these checks from the repository root.

### Claude Code CLI artefacts

| # | Command | Expected output | Result | Date |
|---|---|---|---|---|
| F1 | `ls .claude/commands/rhel-copywriter.md` | File listed, no error | | |
| F2 | `ls .claude/settings.json` | File listed, no error | | |
| F3 | `ls .claude/mcp-servers/rhel-copywriter-server.js` | File listed, no error | | |
| F4 | `grep -l "Red Hat Copywriter Skill" CLAUDE.md` | `CLAUDE.md` returned | | |

### Cursor artefacts

| # | Command | Expected output | Result | Date |
|---|---|---|---|---|
| F5 | `ls .cursor/rules/rhel-copywriter.mdc` | File listed, no error | | |
| F6 | `grep "alwaysApply: false" .cursor/rules/rhel-copywriter.mdc` | Line matched | | |
| F7 | `grep "globs: \[\]" .cursor/rules/rhel-copywriter.mdc` | Line matched | | |

---

## Step 2 — Verify Slash Command (Claude Code CLI)

Start a Claude Code CLI session in the repository root.

| # | Action | Expected output | Result | Date |
|---|---|---|---|---|
| S1 | Run `/help` | `/rhel-copywriter` listed with description "Generate brand-compliant Red Hat copy…" | | |
| S2 | Run `/rhel-copywriter` with no brief | Skill loads from `skill.md`; prompts user for YAML copy brief | | |
| S3 | Provide a **valid** brief (all required fields present) | Output matches skill.md Section 6 envelope: Headline, Body Copy, CTA, Confidence Note, TERMINOLOGY AUDIT block | | |
| S4 | Provide a **malformed** brief (omit `target_audience`) | `VALIDATION ERROR` block returned; **no** content draft generated | | |
| S5 | Provide a **malformed** brief (omit all required fields) | All missing fields listed in a single error response (no early-abort, AC-05) | | |

**Minimum valid brief for S3:**
```yaml
content_type: blog
product_or_topic: "Red Hat OpenShift"
target_audience: "IT decision maker"
key_messages:
  - "Accelerate cloud-native application delivery"
  - "Reduce operational overhead with managed Kubernetes"
```

---

## Step 3 — Verify MCP Declaration (Claude Code CLI / Claude Desktop)

| # | Action | Expected output | Result | Date |
|---|---|---|---|---|
| M1 | Open `.claude/settings.json`; confirm `mcpServers.rhel-copywriter` key is present | Block contains `command`, `args`, `description`, and `tools[0].name: "rhel_copywriter_generate"` | | |
| M2 | Run `node .claude/mcp-servers/rhel-copywriter-server.js` | Process starts without exception; listens on stdio | | |
| M3 | Submit a valid MCP tool call to `rhel_copywriter_generate` | JSON response with `draft`, `word_count`, `terminology_audit`, `metadata` fields | | |
| M4 | Confirm `metadata.skill_version` equals `"1.0.0"` | Value matches | | |
| M5 | Submit a tool call with `content_type: "email"` | `metadata.content_type_applied` equals `"email"` | | |

---

## Step 4 — Verify Cursor Rules Entry

Open Cursor in the repository root.

| # | Action | Expected output | Result | Date |
|---|---|---|---|---|
| R1 | Open `.cursor/rules/rhel-copywriter.mdc` in editor | File exists; front matter shows `alwaysApply: false` and `globs: []` | | |
| R2 | Verify rule appears in Cursor's rules list | Rule listed as `rhel-copywriter` | | |
| R3 | Type `@rhel-copywriter` in Cursor chat | Rule activates; skill loads instructions from `skill.md`; prompts for YAML brief | | |
| R4 | Provide a valid brief via Cursor chat | Output matches skill.md Section 6 envelope | | |
| R5 | Provide a malformed brief via Cursor chat | `VALIDATION ERROR` returned; no content draft | | |

---

## Step 5 — Verify CLAUDE.md Section

| # | Action | Expected output | Result | Date |
|---|---|---|---|---|
| CM1 | Open `CLAUDE.md`; search for "Red Hat Copywriter Skill" heading | Section present **after** Sprint History section | | |
| CM2 | Confirm section includes `/rhel-copywriter` invocation example | Text present | | |
| CM3 | Confirm section references `rhel-copywriter-skill/schema/input-brief.schema.json` | Path reference present | | |

---

## Step 6 — Integration Tests

| # | Test file | Pass conditions | Result | Date |
|---|---|---|---|---|
| IT1 | `rhel-copywriter-skill/tests/acceptance/it-01-controller-pipeline.md` | `draft` non-empty; `terminology_audit` present; `metadata.skill_version = "1.0.0"`; `metadata.content_type_applied` matches submitted `content_type` | | |
| IT2 | `rhel-copywriter-skill/tests/acceptance/it-02-mcp-invocation.md` | MCP server responds within 30 s; JSON returned with all four envelope fields; `metadata.standards_ref_version = "BT-2026-Q2"` | | |

---

## Step 7 — Shared / Cross-Cutting Checks

| # | Check | Command / action | Expected output | Result | Date |
|---|---|---|---|---|---|
| X1 | All new file names are lowercase kebab-case | `git diff --name-only main \| grep -E "[A-Z_]"` | No matches (TDR-RHCW-001 Section 4) | | |
| X2 | No secrets committed | `git grep -iE "password\|secret\|api_key\|token" -- .claude/ .cursor/` | No matches | | |
| X3 | `skill.yaml` version is `1.0.0` | `grep "version:" rhel-copywriter-skill/skill.yaml` | `version: 1.0.0` | | |
| X4 | `skill.yaml` status is `active` | `grep "status:" rhel-copywriter-skill/skill.yaml` | `status: active` | | |

---

## Sign-Off

| Role | Name | Decision | Date |
|---|---|---|---|
| QA Engineer | | Pass / Fail / Blocked | |
| DevOps Engineer | | Verified / Issues Found | |
| Skills Architect | | Approved / Changes Required | |

---

_All items must show "Pass" before this checklist may be signed off. Any "Fail" or
"Blocked" item must be logged as a defect with a fix target date._

_For the full detailed checklist including additional edge cases, see
[docs/installation-verification-checklist.md](installation-verification-checklist.md)._

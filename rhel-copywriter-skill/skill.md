# Red Hat Copywriter Skill — Prompt Placeholder
_Version: 0.0.0-scaffold | Status: STUB — Not for deployment_
_Skill ID: rhel-copywriter-skill | PRD: PRD-RHCW-001 v0.1_

<!-- ============================================================ -->
<!-- STATUS: STUB — Implementation sprint only                   -->
<!-- This file is the placeholder for the skill system prompt.  -->
<!-- Authoring is BLOCKED on brand-tone-reference.md content    -->
<!-- (see docs/task-brand-tone-content.md TASK-BT-001).         -->
<!--                                                             -->
<!-- DO NOT deploy this file. It contains no implementation.    -->
<!-- ============================================================ -->

## Purpose

This file (`skill.md`) is the skill system prompt for the Red Hat Copywriter Skill. When implemented, it will contain the full instruction set that the AI model receives to produce brand-compliant Red Hat copy.

## Downstream Dependencies (Blocking)

This file cannot be authored until the following are resolved:

| Dependency | Status | Owner | Reference |
|---|---|---|---|
| `standards/brand-tone-reference.md` populated | BLOCKED — Awaiting Brand Experience team | R. Patel (Skill Owner) | TASK-BT-001 |
| `standards/terminology-list.md` approved | COMPLETE — TERM-2026-Q2 | J. Morales (PMM) | DR-Q04 |
| Input/output contract finalised | COMPLETE — see design-spec.md | Skill Owner | PRD Section 8–9 |

## Planned Instruction Structure (Design Phase)

When authored, this skill prompt will include the following sections in order:

1. **Role and identity statement** — Instructs the model to act as a Red Hat brand-compliant copywriter
2. **Brand tone and voice reference** — Embedded content from `standards/brand-tone-reference.md` (BT-2026-Q2)
3. **Approved terminology rules** — Embedded critical rules from `standards/terminology-list.md` (TERM-2026-Q2)
4. **Routing instructions** — Content-type detection and template application (F-02, F-04)
5. **Draft generation rules** — Voice, tone, length, structure requirements (F-03)
6. **Terminology audit instructions** — How to identify, flag, and suggest replacements for banned terms (F-05)
7. **Messaging alignment instructions** — How to assess and report pillar alignment (F-06)
8. **Output format instructions** — JSON output contract specification (F-07)
9. **Input validation instructions** — How to handle malformed or incomplete briefs (F-01)

## Output Contract Reference

The skill prompt must instruct the model to return a JSON object matching the structure in PRD Section 9:

```
{
  "draft": "<string>",
  "word_count": <integer>,
  "terminology_audit": {
    "flagged_terms": [...],
    "banned_terms_detected": [...]
  },
  "messaging_alignment": {
    "pillars_addressed": [...],
    "gaps": [...]
  },
  "metadata": {
    "skill_version": "<semver>",
    "standards_ref_version": "<BT-YYYY-QN>",
    "generated_at": "<ISO8601>"
  }
}
```

---

_This stub will be replaced with the full skill prompt during the implementation sprint, after TASK-BT-001 is resolved and brand-tone-reference.md content is approved._

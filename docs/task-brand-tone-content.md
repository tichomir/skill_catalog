# Task: Populate brand-tone-reference.md with Brand Experience Team Content

| Field | Value |
|---|---|
| Task ID | TASK-BT-001 |
| Type | Content / Dependency Resolution |
| Status | **BLOCKED — Awaiting Brand Experience Team Input** |
| Created | 2026-04-02 |
| Created by | Scrum Master (scrum-master-persona) |
| Owner | Skill Owner (R. Patel) |
| Stakeholders | Brand Experience Team, PMM (J. Morales) |
| Priority | High — blocks skill authoring and acceptance tests |

---

## Problem Statement

`rhel-copywriter-skill/standards/brand-tone-reference.md` was scaffolded as part of the Q-01 decision record (DR-Q01) but contains only a placeholder comment. The file carries version stamp `BT-2026-Q2` and is intended to hold curated Red Hat brand tone and voice guidance for use in the skill's system prompt.

Until this file contains real content, the following downstream work items are **blocked**:

- Skill system prompt authoring (no brand guidance to embed)
- Acceptance test AC-01: "Tone compliance" — untestable without a reference
- Acceptance test AC-02: "Brand voice consistency" — untestable without a reference
- Any deployment to a staging or production environment

---

## Work Required

1. **Brand Experience team engagement** — Skill Owner (R. Patel) to contact the Brand Experience team and request a curated summary of Red Hat brand tone and voice standards suitable for AI system prompt embedding. The summary should address:
   - Brand voice pillars and adjectives
   - Tone variations by content type (technical, marketing, executive)
   - Prohibited phrases and constructions
   - Sentence-level guidance (length, active/passive, complexity)
   - Perspective and pronouns (first-person "we", second-person "you", etc.)
   - Red Hat-specific terminology handling (capitalisation, preferred terms)

2. **Draft content** — Skill Owner drafts `brand-tone-reference.md` incorporating the Brand Experience team input, following the structure below.

3. **PMM review** — Per DR-Q01 update workflow, PMM (J. Morales) reviews and approves the draft content via PR before merge.

4. **Version stamp** — File ships with version stamp `BT-2026-Q2` and the next review date `2026-07-01`.

---

## Suggested File Structure for brand-tone-reference.md

The populated file should include these sections at minimum:

```
## 1. Brand Voice Overview
## 2. Tone Pillars
## 3. Tone by Content Type
## 4. Sentence and Style Guidance
## 5. Perspective and Pronouns
## 6. Prohibited Language
## 7. Red Hat Name and Product Capitalisation Rules
## 8. Version and Governance
```

---

## Acceptance Criteria for This Task

| # | Criterion | Testable Definition |
|---|---|---|
| AC-BT-1 | File contains real content | `brand-tone-reference.md` has no placeholder comment lines; word count > 300 |
| AC-BT-2 | Brand Experience team input incorporated | Skill Owner confirms in PR description that content was reviewed with Brand Experience team |
| AC-BT-3 | PMM approval obtained | PR merged with explicit approval from J. Morales (PMM) |
| AC-BT-4 | Version stamp present | File header contains `BT-2026-Q2` and next review date |
| AC-BT-5 | Prohibited language section present | File contains at least one section listing disallowed phrases or constructions |
| AC-BT-6 | Downstream blocked tasks unblocked | Skill system prompt authoring and acceptance test scaffolding can proceed after merge |

---

## Dependent Tasks — Currently Blocked

The following tasks MUST NOT begin implementation until TASK-BT-001 is resolved:

| Task | Description | Blocked By |
|---|---|---|
| TASK-SKILL-001 | Author skill system prompt | brand-tone-reference.md content |
| TASK-AC-001 | Scaffold AC-01 tone compliance test | brand-tone-reference.md content |
| TASK-AC-002 | Scaffold AC-02 brand voice consistency test | brand-tone-reference.md content |
| TASK-DEPLOY-001 | Deploy skill to staging | All acceptance tests passing |

---

## Escalation Path

If Brand Experience team input is not received within **5 business days** of initial outreach:

1. Scrum Master escalates to PMM (J. Morales) to expedite Brand Experience team response.
2. If still unresolved after a further 3 business days, PMM escalates to Brand Experience team lead.
3. Sprint goal for the skill authoring phase should be pushed back if this task is not resolved before the authoring sprint begins.

---

## Notes

- Per DR-Q01, the `brand-tone-reference.md` file is a **curated summary**, not a verbatim copy of the internal brand portal. The Skill Owner is responsible for distilling guidance relevant to AI-generated copy.
- The Brand Standards portal is at `brand.redhat.com` (internal SSO-protected). Brand Experience team owns that source.
- Any interim "best effort" content placed in the file before Brand Experience review must be clearly marked as `[DRAFT — NOT APPROVED]` and must not be used in any deployed version of the skill.

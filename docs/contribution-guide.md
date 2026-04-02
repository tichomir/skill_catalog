# Contribution Guide — AI Skills Team
_Document ID: CONTRIB-001 | Version: 1.0 | Status: Active_
_Date: 2026-04-02 | Author: Prompt Engineer Persona_
_Milestone: rhel-copywriter-skill v0.2.0 — Pilot and Iteration (Sprint 6)_

---

## Overview

This guide records lessons learned and reusable skill authoring patterns established
during the development and piloting of the `rhel-copywriter-skill`. It is intended
for future skill authors on the AI Skills Team and covers the complete lifecycle from
design to production, including patterns that worked well and anti-patterns to avoid.

This document is authoritative for skills developed in this repository. Where it
conflicts with other documentation, defer to this guide — then file a PR to resolve
the conflict.

---

## Skill Authoring Patterns

### Pattern 1 — Design specification before any implementation

Every skill begins with a design specification (PRD) signed off by all stakeholders
before any implementation file is created. This is a hard delivery principle, not a
guideline.

**Why it matters:** The rhel-copywriter-skill design phase (Sprint 1) surfaced two
open questions (Q-01, Q-04) that would have caused rework if discovered during
implementation. Resolving them before implementation saved at least two sprint cycles.

**How to apply:**
- Write the PRD covering: use cases, input/output contract, routing logic, acceptance
  criteria, and open questions.
- Get explicit sign-off from PMM, GTM Lead, and Skill Owner before creating any skill
  file other than the scaffold.
- Use the acceptance criteria matrix (`docs/acceptance-criteria-matrix.md`) as the
  testability gate: if a criterion cannot be described in testable terms, the design is
  not ready.

---

### Pattern 2 — Decouple standards references from skill logic

Skill logic (routing, validation, output structure) is authored separately from the
standards content the skill applies (brand tone, terminology, audience profiles). The
skill reads standards at execution time via relative file paths; it does not embed them.

**Why it matters:** During Sprint 6 the PMM reviewed feedback and proposed tone
clarifications. Because `references/brand-and-tone-notes.md` is a separate file, the
update could be made without touching `skill.md`. This is the AC-06 decoupling
requirement in practice.

**How to apply:**
- Author all brand, tone, terminology, and audience guidance in `references/`.
- Reference these files by path in `skill.md`. Never copy-paste their content into the
  skill file.
- Version `references/` files independently of the skill version (see
  `docs/references-versioning.md`).
- Each `references/` file carries a version stamp in its front matter; the skill's
  output envelope includes the version stamp for QA audit.

---

### Pattern 3 — YAML brief schema: structured enums over free text

Input briefs that use structured enums for routing fields (`content_type`, `audience`,
`tone_variant`, `output_format`) are more reliable than free-text fields for the same
purpose.

**Why it matters:** The original `input-brief.schema.json` scaffold used a free-text
`target_audience` string. This made AC-05 (schema validation) tests ambiguous — there
was no machine-checkable contract for what values were valid. In v0.2.0, all routing
fields use strict enums. This made the audience routing logic in `skill.md` testable
and the validation error format unambiguous.

**How to apply:**
- Define enums at the design phase. If the valid values are not known, the design is
  not complete.
- Use the `enum` keyword in `input-brief.schema.json` for any field that drives routing.
- Keep `skill.md` Section 4.3 (Enum Values) and `schema/input-brief.schema.json` in
  sync. Field name divergence is a maintenance debt; resolve it in the sprint it is
  discovered.

---

### Pattern 4 — Optional fields need inline documentation in the template

Optional fields that are not documented at the point of use will not be used correctly
by first-time operators. Inline YAML comments in `templates/copy-brief.md` are the
primary discovery mechanism for optional fields — not the README, not the PRD.

**Why it matters:** Pilot feedback (G-PMM-03) found that the optional `tone_variant`
override and `messaging_pillars` fields were unclear. PMM noted that no in-brief
guidance indicated when a tone override was appropriate. This was resolved in v0.2.0
by adding structured comment blocks covering: what the field does, when to use it,
when to omit it, and examples.

**How to apply:**
- Every optional field in the brief template must have a comment block with at minimum:
  - Description
  - When to use
  - When to omit
  - At least one concrete example
- Keep comment blocks up to date when field semantics change. Stale comments are worse
  than no comments because they mislead operators.

---

### Pattern 5 — The Confidence Note is the right mechanism for human-in-the-loop review

The Confidence Note section of each output block is the mechanism by which the skill
signals to PMM reviewers what needs human review before the copy is published. It is
not a failure signal — it is a checklist for the reviewer.

**Why it matters:** In the Summit pilot, the Confidence Note correctly flagged the IBM
IVB citation for PMM claim clearance and the booth stand number as unresolved. Both
reviewers stated that the Confidence Note was the right mechanism and should be
preserved. GTM Lead M. Ferreira: "The Confidence Notes are the right mechanism — they
flag what needs human review without blocking the output. Keep them."

**How to apply:**
- Confidence Note must always be present, even when the draft is clean and no terms
  were flagged.
- Minimum content for a clean draft: terminology audit summary + confirmation that no
  placeholders are unresolved.
- Do not suppress or shorten the Confidence Note to make outputs look cleaner. Its
  value is in surfacing review requirements, not in length reduction.
- Design `unresolved_placeholders` in the output envelope as a machine-readable
  companion to the Confidence Note for downstream tooling.

---

### Pattern 6 — Test against the real pilot use case before marking the skill done

The acceptance criteria (AC-01 through AC-06) are necessary but not sufficient for
production readiness. A skill is production-ready when it has been tested against the
specific use cases it was built for, by the people who will actually use it.

**Why it matters:** Sprint 5 QA testing validated the skill against abstract test
prompts. Sprint 6 pilot testing with the real PMM persona agent against the Summit
prep use case surfaced five gaps (G-PMM-01 through G-PMM-03, G-GTM-01 through
G-GTM-03) that the abstract tests did not catch. None of the gaps were regressions —
they were missing capabilities discovered only in context.

**How to apply:**
- Identify the pilot use cases at the PRD stage (Section 10).
- Run the pilot with the real persona agent (or the closest available proxy) using a
  real or realistic brief.
- Collect structured feedback from PMM and GTM Lead within the pilot sprint.
- Treat pilot feedback as a backlog input for the next version, not as a sign of
  failure.

---

### Pattern 7 — Validate the time-to-copy metric as part of the pilot

The success metric "brief to Summit-ready copy in under one hour" is a real-world
throughput measure, not a feature requirement. It can only be validated in a live or
simulated pilot run.

**Why it matters:** The rhel-copywriter-skill pilot achieved 48 minutes 22 seconds
from brief submission to PMM + GTM Lead review complete — 11 minutes 38 seconds
within the one-hour benchmark. This measurement is now part of the skill record.
Without the pilot, this metric would have remained unvalidated.

**How to apply:**
- Record timestamps at: brief submission, first output returned, PMM review complete,
  GTM review complete.
- Compare to the benchmark defined in the PRD.
- Include the measurement in the pilot run log.
- If the benchmark is not met, investigate where the time was spent before adding
  complexity to the skill.

---

### Pattern 8 — Resolve open questions at the decision point, not later

Open questions accumulate design debt. Each unresolved question is a branching point
in the skill's behaviour that has not been decided. Decisions made late cost more
than decisions made early.

**Why it matters:** Q-02 (chat vs. pipeline trigger) and Q-03 (multi-language roadmap)
were deferred from Sprint 1. Resolving Q-02 in Sprint 6 required no rework because
the pipeline trigger had been implemented correctly from the start. But if the pilot
had found that chat invocation was the right model, the skill would have needed
significant restructuring. Deferring a question is a risk decision, not a neutral one.

**How to apply:**
- Name open questions explicitly in the PRD with an ID (Q-01, Q-02, etc.).
- Assign each question a decision deadline (which sprint will resolve it).
- Record decisions in `docs/decision-record-Q0N.md` files when resolved.
- When a question is resolved by pilot evidence (as Q-02 and Q-03 were), cite the
  evidence explicitly in the decision record.

---

## Repository Conventions

### File placement

| Artefact type | Path |
|---|---|
| Skill entry point | `rhel-copywriter-skill/skill.md` |
| Brief template | `rhel-copywriter-skill/templates/copy-brief.md` |
| JSON schema | `rhel-copywriter-skill/schema/input-brief.schema.json` |
| Workflow files | `rhel-copywriter-skill/workflows/` |
| Standards references | `references/` (versioned independently) |
| Design and QA docs | `docs/` |
| Pilot artefacts | `docs/pilot/` |
| QA test artefacts | `docs/qa/` or `tests/` |
| Changelog | `rhel-copywriter-skill/CHANGELOG.md` |
| Contribution guide | `docs/contribution-guide.md` (this file) |

### Version numbering

- Skill versions follow semantic versioning: MAJOR.MINOR.PATCH.
- MAJOR: breaking changes to the input contract or output structure.
- MINOR: new optional fields, new behaviours, non-breaking additions.
- PATCH: documentation corrections, typo fixes, reference content updates.
- The version in `skill.md` front matter, `skill.yaml`, `schema/_version`, and
  `templates/copy-brief.md` header must all agree.

### Commit message convention

```
[Skill Name] <type>: <short description>

Types: feat | fix | docs | refactor | test | chore
Example: [rhel-copywriter-skill] feat: add event_metadata field for summit_prep briefs
```

### PR checklist before merge to main

- [ ] `skill.md` version bumped and matches `skill.yaml`, schema, and template header
- [ ] `CHANGELOG.md` entry added with change description and traceability to feedback/gap IDs
- [ ] All new optional fields documented in `templates/copy-brief.md` with when-to-use comments
- [ ] `schema/input-brief.schema.json` updated to match new fields
- [ ] `references/` updated if pilot or review surfaced tone or terminology gaps
- [ ] Tests updated or added for any new validation logic
- [ ] Architect sign-off recorded in the PR before merge

---

## Anti-Patterns to Avoid

### Anti-pattern: Embedding standards content in the skill file

Do not copy-paste content from `references/brand-and-tone-notes.md` or
`references/audience-profiles.md` into `skill.md`. Reference by path. Embedding
standards content creates two sources of truth and breaks the AC-06 decoupling
requirement.

### Anti-pattern: Marking a task complete before QA review

A skill task is not complete when the artefact is written — it is complete when QA
has reviewed it against the acceptance criteria. The Sprint 3 workflow showed that
skipping QA review before marking tasks done led to field name divergence that required
a remediation cycle.

### Anti-pattern: Generating test outputs manually and presenting them as real outputs

Sprint 4 integration tests were initially submitted with simulated transcripts rather
than real execution results. This was caught in QA review and required a remediation
task. All test output records must be from actual execution of the skill against the
stated input.

### Anti-pattern: Deferring field documentation to the README

Operators read the brief template, not the README, when completing an input brief.
Documentation in the README is supplementary; documentation in the template itself
is primary. Both are needed, but the template takes precedence for field-level
guidance.

---

_Contribution guide authored by: Prompt Engineer Persona_
_Based on: rhel-copywriter-skill Sprint 1–6 delivery record, pilot feedback log
(PILOT-FEEDBACK-001), open questions resolution (OQR-RHCW-001)_
_Architect sign-off required before merge to main._

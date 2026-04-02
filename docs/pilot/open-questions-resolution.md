# Open Questions Resolution — Pilot and Iteration
_Document ID: OQR-RHCW-001 | Version: 1.0 | Status: Final_
_Date: 2026-04-02 | Author: Scrum Master Persona_
_Sprint: 6 — Pilot and Iteration_
_Related pilot run: PILOT-RUN-001_

---

## Overview

This document records the resolution of two open questions (Q-02 and Q-03) that were
deferred from earlier design sprints and are resolved in Sprint 6 based on pilot run
findings, reviewer feedback, and team discussion.

| Q-ID | Question | Status |
|---|---|---|
| Q-02 | Should the skill be triggered via chat interaction or via a pipeline invocation? | **Resolved** — see Section 1 |
| Q-03 | What is the multi-language roadmap for the skill, targeting v0.2? | **Resolved** — see Section 2 |

---

## Q-02: Chat vs. Pipeline Trigger

### Question

Should users invoke the Red Hat Copywriter Skill through a conversational chat interface
(i.e., by describing their needs in natural language and letting the AI extract brief
fields) or through a structured pipeline trigger (i.e., submitting a YAML brief to the
`/rhel-copywriter` slash command)?

This question arose because both patterns are architecturally viable within Claude Code
and Cursor, and the right choice affects operator experience, brief completeness
guarantees, and the reliability of AC-04 (clarification request behaviour).

### Evidence from Pilot

The pilot run (PILOT-RUN-001) used the pipeline trigger exclusively:

- Operator submitted a complete YAML brief (`docs/pilot/pilot-brief.yaml`) to the
  `/rhel-copywriter` slash command.
- Brief validation completed in 16 seconds with zero schema errors (all required fields
  present).
- No clarification prompts were needed; the pipeline proceeded to output generation
  without interruption.
- All three outputs were generated in 22 minutes 14 seconds.
- The one-hour benchmark was met with 11 minutes 38 seconds to spare.

PMM reviewer L. Okonkwo noted that brief preparation was "the longest human step" but
that the structured format was unambiguous and required no rework after submission.
GTM Lead M. Ferreira observed that the pipeline approach removed ambiguity from the
invocation step — there was a clear contract between what the brief specified and what
the skill produced.

### Decision

**Decision: Pipeline trigger is the canonical invocation method for the Red Hat Copywriter
Skill. Chat-based invocation is not supported in v1.0 or v0.2.**

**Rationale:**

1. **Brief completeness guarantees.** The YAML brief schema enforces required fields
   (`content_type`, `product_or_topic`, `target_audience`, `key_messages`) at submission
   time. Chat extraction of these fields from natural language cannot guarantee completeness
   without additional validation logic and introduces latency from clarification turns.

2. **AC-04 reliability.** Acceptance criterion AC-04 requires the skill to request
   clarification when a required field is missing. This criterion is testable and
   reproducible only with a structured brief. Chat-mode invocation makes AC-04 testing
   ambiguous because the AI may infer missing fields rather than prompting.

3. **Pilot result.** The pipeline trigger met the one-hour success benchmark in the pilot
   under real PMM persona conditions. There is no evidence from the pilot that chat-mode
   invocation would improve usability or reduce time-to-copy.

4. **Operator expectation alignment.** PMM and GTM Lead reviewers found the YAML brief
   format clear and unambiguous. Introducing a parallel chat invocation path would create
   inconsistency in outputs for the same logical brief content.

5. **Scope discipline.** Adding a chat extraction layer would require a separate NLU
   routing workflow, additional testing, and an expanded maintenance surface. The pilot
   confirms this complexity is not necessary to meet the success criteria defined in
   PRD Section 10.

### Decision: Chat invocation — future consideration (not v0.2)

Chat-based invocation (where the user describes their need in natural language and the
skill extracts the brief fields conversationally) may be reconsidered for v1.x if:

- A significant volume of users report friction with the YAML brief format.
- A chat extraction workflow can be validated against AC-04 with equivalent reliability.
- The Skills Architect approves the additional workflow complexity.

This is not scheduled for v0.2. Feedback from the pilot does not surface a blocking
usability problem with the structured brief approach.

### Record

| Field | Value |
|---|---|
| Decision | Pipeline trigger is canonical; chat invocation not supported in v1.0 or v0.2 |
| Decided by | Scrum Master, confirmed by PMM and GTM Lead pilot feedback |
| Date | 2026-04-02 |
| Evidence | PILOT-RUN-001 results; PMM feedback F-04; GTM Lead feedback G-01, G-03 |
| Next review | If chat invocation is revisited, requires Skills Architect approval |

---

## Q-03: Multi-Language Roadmap for v0.2

### Question

Should the Red Hat Copywriter Skill support content generation in languages other than
English in v0.2, and if so, which languages, with what quality guarantees, and under
what governance model?

This question was deferred from Sprint 1 because it had significant implications for
the references/ content structure (brand-and-tone-notes.md, audience-profiles.md,
terminology-list.md are all English-only in v1.0.0) and for the skill's output contract.

### Evidence from Pilot

The pilot run operated in English. The following observations are relevant:

- The `references/brand-and-tone-notes.md` file is English-only and contains idiomatic
  guidance (e.g., active voice recommendations, jargon blocklist) that does not translate
  directly.
- The `references/terminology-list.md` (TERM-2026-Q2) contains English-only approved and
  banned terms. No equivalent list exists for any other language.
- GTM Lead M. Ferreira noted that the IBM Americas region operates primarily in English
  and Portuguese (Brazil) for partner enablement materials. A Portuguese (Brazil) variant
  would be valuable for LatAm Summit events.
- PMM L. Okonkwo noted that EMEA partner GTM uses English as the working language for
  Summit collateral; localisation is handled downstream by regional marketing teams and
  is out of scope for the skill's current use case.
- No reviewer raised multi-language as a blocking gap for the pilot use case.

### Decision

**Decision: Multi-language support is deferred beyond v0.2. v0.2 will add a localisation
readiness foundation only.**

**Rationale:**

1. **No blocking pilot gap.** Neither PMM nor GTM Lead identified multi-language as a
   blocker for the Summit pilot use case or for near-term partner enablement distribution.
   The pilot audience (IBM Global Alliance GTM, Red Hat Americas) operates in English.

2. **References/ are English-only and unscalable without PMM input.** The brand and tone
   notes, audience profiles, and terminology list are authored by PMM and require PMM
   review and sign-off before any translated equivalent can be trusted. No translated
   references exist, and commissioning them is a separate PMM workstream.

3. **Quality guarantee problem.** The skill's AC-01 brand scoring rubric (BRR-001-v1.0)
   is calibrated for English outputs. Applying it to translated outputs without a
   language-specific rubric would produce unreliable pass/fail results. Creating
   language-specific rubrics requires Skills Architect scoping.

4. **Governance gap.** There is no current process for PMM sign-off of non-English
   terminology lists or brand tone references. Establishing this process is a prerequisite
   for any production multi-language capability.

### v0.2 Localisation Readiness Deliverables

While full multi-language support is deferred, v0.2 will lay the groundwork:

| Deliverable | Owner | Purpose |
|---|---|---|
| Add `language` optional field to `copy-brief.md` and `input-brief.schema.json` with default `en` | Prompt Engineer | Enables future language routing without breaking v1.0 briefs |
| Add `language` field to skill output envelope metadata | Prompt Engineer | Ensures output records are language-tagged for future audit |
| Document localisation requirements in `docs/localisation-roadmap.md` | Skills Architect | Captures PMM sign-off requirements, rubric scoping needs, and language priority list |
| Add `pt-BR` (Portuguese, Brazil) to the language roadmap as priority 1 target | Skills Architect | Addresses M. Ferreira's LatAm Summit use case as the first non-English target |
| Identify PMM owner for non-English terminology and tone sign-off | Scrum Master | Prerequisites gate work; must be assigned before any language-specific references are authored |

### Languages in scope for future versions

Based on pilot feedback and known regional GTM needs:

| Language | Region | Priority | Prerequisite |
|---|---|---|---|
| Portuguese (Brazil) — `pt-BR` | LatAm | 1 | PMM LatAm contact; translated terminology list |
| Spanish (LATAM) — `es-419` | LatAm | 2 | PMM LatAm contact; translated terminology list |
| German — `de` | DACH | 3 | PMM EMEA contact; DACH brand tone notes |
| French — `fr` | EMEA (France, Canada) | 4 | PMM EMEA contact; French brand tone notes |

This priority order reflects GTM feedback and Red Hat's Summit event footprint. No
commitment to a delivery date is made for any non-English language in this document.

### Record

| Field | Value |
|---|---|
| Decision | Multi-language deferred beyond v0.2; v0.2 adds localisation readiness foundation only |
| Decided by | Scrum Master, informed by GTM Lead M. Ferreira pilot feedback |
| Date | 2026-04-02 |
| Evidence | Pilot PILOT-RUN-001 (English-only); GTM Lead feedback G-02; PMM feedback F-04 |
| v0.2 deliverables | `language` field in brief schema; `localisation-roadmap.md`; pt-BR as priority 1 |
| Next review | When pt-BR content is ready to commission — requires PMM LatAm owner assignment |

---

## Summary Table

| Q-ID | Question | Decision | Owner | Next review trigger |
|---|---|---|---|---|
| Q-02 | Chat vs. pipeline trigger | Pipeline trigger is canonical for v1.0 and v0.2; chat invocation deferred to v1.x | Scrum Master | User feedback reporting friction with YAML brief format |
| Q-03 | Multi-language roadmap for v0.2 | Full multi-language deferred beyond v0.2; localisation readiness foundation added in v0.2 | Scrum Master | PMM LatAm owner assignment; pt-BR as priority 1 target |

---

_Document prepared by: Scrum Master Persona_
_Based on: PILOT-RUN-001 results, PMM feedback (L. Okonkwo), GTM Lead feedback (M. Ferreira)_
_Supersedes: No prior Q-02 or Q-03 decision records exist. This is the first resolution._

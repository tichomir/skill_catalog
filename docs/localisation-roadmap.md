# Localisation Roadmap — Red Hat Copywriter Skill
_Document ID: LOC-RHCW-001 | Version: 1.0 | Status: Active_
_Date: 2026-04-02 | Author: Scrum Master Persona_
_Sprint: 6 — Pilot and Iteration | Resolves: Q-03_

---

## Overview

This document records the resolution of open question Q-03 (multi-language roadmap for
the Red Hat Copywriter Skill) and serves as the authoritative reference for future
localisation work.

**Decision summary:** Full multi-language support is deferred beyond v0.2. v0.2 adds
a localisation readiness foundation only. See Section 2 for the v0.2 deliverables and
Section 3 for the language priority list.

For the full decision rationale, see `docs/open-questions-resolution.md` (OQR-RHCW-001,
Section 2).

---

## v0.2 Localisation Readiness Foundation

The following changes were delivered in v0.2.0 to prepare the skill for future
multi-language support without committing to production non-English output:

| Deliverable | File | Status |
|---|---|---|
| `language` optional field in brief schema (BCP 47, default `en`) | `rhel-copywriter-skill/schema/input-brief.schema.json` | Done |
| `language` field in brief template with when-to-use comments | `rhel-copywriter-skill/templates/copy-brief.md` | Done |
| `language` field in output envelope metadata | `rhel-copywriter-skill/skill.md` Section 6.2 | Done |
| This localisation roadmap document | `docs/localisation-roadmap.md` | Done |

**v0.2 behaviour when `language` is set to a non-English value:**
1. The skill accepts the value without a validation error.
2. The skill generates English output.
3. The skill adds a Confidence Note advisory: "Output generated in English. Requested
   language '[value]' is not yet supported. See docs/localisation-roadmap.md."
4. The output envelope `language` field records `en` (the actual output language).

This behaviour ensures that briefs authored now with `language: pt-BR` will be
forward-compatible with future skill versions that honour the field.

---

## Why Multi-Language Support Is Deferred

Multi-language output for the Red Hat Copywriter Skill requires:

1. **PMM-reviewed, language-specific brand and tone references.** The
   `references/brand-and-tone-notes.md` file contains idiomatic English guidance
   (active voice rules, jargon blocklist, partner-first framing examples) that does
   not translate directly. A Portuguese (Brazil) equivalent requires authoring by a
   PMM with LatAm brand authority and sign-off from the Brand Experience team.

2. **Language-specific terminology lists.** The `standards/terminology-list.md`
   (TERM-2026-Q2) contains English-only approved and banned terms. Approved product
   names, approved abbreviations, and the jargon blocklist all require language-specific
   equivalents before a non-English terminology audit is meaningful.

3. **Language-specific brand scoring rubric (BRR).** The AC-01 brand scoring rubric
   (BRR-001-v1.0) is calibrated for English outputs. Applying it to translated outputs
   without a language-specific rubric produces unreliable pass/fail results. Creating
   a language-specific rubric requires Skills Architect scoping and PMM involvement.

4. **PMM sign-off governance.** There is no current process for PMM approval of
   non-English terminology lists or brand tone references. This governance process is
   a prerequisite for any production multi-language capability.

None of these prerequisites were in place at the time of the Sprint 6 pilot, and no
reviewer identified multi-language as a blocking gap for the pilot use case.

---

## Language Priority List

Based on pilot feedback (GTM Lead M. Ferreira) and Red Hat's Summit event footprint:

| Priority | Language | BCP 47 Tag | Region | Prerequisite Gate |
|---|---|---|---|---|
| 1 | Portuguese (Brazil) | `pt-BR` | LatAm | PMM LatAm contact assigned; translated terminology list authored and PMM-reviewed |
| 2 | Spanish (LATAM) | `es-419` | LatAm | PMM LatAm contact; translated terminology list |
| 3 | German | `de` | DACH | PMM EMEA contact; DACH brand tone notes |
| 4 | French | `fr` | EMEA (France, Canada) | PMM EMEA contact; French brand tone notes |

**Priority 1 rationale:** GTM Lead M. Ferreira (GTM Americas, Hybrid Cloud) noted
that the IBM Americas region operates primarily in English and Portuguese (Brazil)
for partner enablement materials. A pt-BR variant would directly serve the LatAm
Summit use case exercised in the Sprint 6 pilot.

No delivery date is committed for any non-English language. Language work begins when
all prerequisite gates for that language are cleared.

---

## Prerequisites for Each Language Version

Before any language can be added to the skill, the following must be completed and
approved:

### Content prerequisites (per language)

- [ ] PMM owner assigned for the language region
- [ ] `references/brand-and-tone-notes-[tag].md` authored by regional PMM
- [ ] `references/audience-profiles-[tag].md` authored (or verified as language-agnostic
      and not requiring localisation)
- [ ] `references/brand-and-tone-notes-[tag].md` reviewed and signed off by Brand
      Experience team
- [ ] `standards/terminology-list-[tag].md` authored with approved terms, banned terms,
      and approved product name forms in the target language
- [ ] Terminology list reviewed and signed off by regional PMM

### Skill prerequisites (per language)

- [ ] Language-specific brand scoring rubric (BRR-[lang]-v1.0) authored and approved
      by Skills Architect
- [ ] Intake routing updated in `skill.md` to route to language-specific references
      when `language` field is set to the target tag
- [ ] Output validation logic updated to run terminology audit against the correct
      language-specific list
- [ ] AC-01 threshold verified for the language using the language-specific rubric
- [ ] Integration tests updated to include at least three test briefs in the target
      language
- [ ] PMM sign-off on at least three pilot outputs in the target language

### Governance prerequisites

- [ ] PMM LatAm (or regional) owner identified and confirmed for ongoing maintenance
      of the language-specific references
- [ ] Version management process confirmed for language-specific references
      (follows the scheme in `docs/references-versioning.md`)
- [ ] Skills Architect approval to proceed with the language addition

---

## v0.2 PMM Action Items

The following items were identified during the Sprint 6 pilot as prerequisites for
pt-BR (priority 1) and are assigned to the Scrum Master for tracking:

| Action | Owner | Status |
|---|---|---|
| Identify PMM LatAm contact for pt-BR terminology and tone sign-off | Scrum Master | Open |
| Confirm whether Brand Experience team has an existing pt-BR brand voice guide | Scrum Master | Open |
| Scope the BRR-pt-BR rubric work with Skills Architect | Skills Architect | Open |

These items do not block v0.2.0 delivery. They are prerequisites for the first
non-English language release (target: post-v0.2).

---

## Relationship to Other Documents

| Document | Relationship |
|---|---|
| `docs/open-questions-resolution.md` (OQR-RHCW-001) | Source decision: Q-03 resolution with full rationale |
| `docs/pilot/feedback-log.md` (PILOT-FEEDBACK-001) | Source evidence: GTM Lead M. Ferreira pt-BR observation |
| `references/brand-and-tone-notes.md` | English-only standards reference; the model for future language equivalents |
| `references/audience-profiles.md` | English-only audience profiles; may require language-specific variants |
| `docs/references-versioning.md` | Versioning scheme that applies to language-specific reference files |
| `rhel-copywriter-skill/CHANGELOG.md` | v0.2.0 entry documents the localisation foundation changes |

---

_Document prepared by: Scrum Master Persona_
_Based on: OQR-RHCW-001 Q-03 resolution; PILOT-FEEDBACK-001 GTM Lead feedback_
_This document requires Skills Architect review before the first non-English language
is added to the skill._

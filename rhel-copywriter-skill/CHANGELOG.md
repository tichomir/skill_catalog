# Changelog — Red Hat Copywriter Skill

All notable changes to this skill are documented in this file.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [1.1.0] — 2026-04-02

### Summary

v1.1.0 incorporates feedback collected during the Summit preparation pilot run
(PILOT-RUN-001, 2026-04-02). All changes are traceable to specific feedback items
from PMM reviewer L. Okonkwo (IBM Global Alliance) and GTM Lead M. Ferreira
(GTM Americas). See `docs/pilot/feedback-log.md` for the full structured feedback log.

---

### Added

**`event_metadata` optional field in brief schema (G-PMM-01 — High priority)**
PMM feedback: no structured field for event name, date, location, or booth reference
in Summit content. Operators were forced to rely on the Confidence Note to surface
unresolved booth numbers.
- Added `event_metadata` optional object to `skill.md`, `templates/copy-brief.md`,
  and `schema/input-brief.schema.json`.
- Sub-fields: `event_name` (required when block present), `event_date`, `event_location`,
  `booth_reference`.
- When the block is present and `content_type` is `summit_prep`, the skill substitutes
  event values into the Before You Go narrative and announcement blurb outputs.
- When `booth_reference` is absent, `[BOOTH_REFERENCE]` placeholder is inserted and
  listed in `unresolved_placeholders`.

**`language` optional field for localisation readiness (Q-03 resolution)**
GTM Lead feedback from LatAm Summit use case; open question Q-03 resolved to add
localisation foundation without blocking v1.1.
- Added `language` BCP 47 field (default `en`) to brief schema and output envelope.
- Only `en` is fully supported in v1.1. Other values are accepted; the skill generates
  English output and adds a Confidence Note advisory directing operators to
  `docs/localisation-roadmap.md`.
- `language` field is now always present in the output envelope.

**`call_to_action` optional field surfaced in brief template (G-GTM-01 — Low priority)**
GTM Lead feedback: the optional CTA field existed in the original schema but was not
documented in `templates/copy-brief.md`. Operators did not know to use it.
- Added inline YAML comment block for `call_to_action` in `templates/copy-brief.md`
  with guidance on when to use it vs. relying on skill-generated CTA.
- Documented in `skill.md` Section 4.2 and in the routing logic (Section 5).
- When present, the verbatim value takes precedence over any CTA derived from
  `key_messages`.

**Tone override conflict advisory (G-PMM-02 / G-GTM-03 — Medium priority)**
PMM and GTM Lead both observed that applying `executive` tone to the Before You Go
slide output may not be optimal; Confidence Note in the pilot output flagged this
correctly but the skill produced no proactive advisory.
- Added tone override conflict detection to the intake routing logic in `skill.md`
  Section 5.
- When `content_type` is `summit_prep` and `tone_variant` is `executive`, the skill
  adds an advisory in the Confidence Note of the Before You Go output recommending
  the operator review a `conversational` variant for potential warmer in-session impact.
- No secondary variant is auto-generated (deferred to a future enhancement).

**Inline YAML comments for all optional fields (G-PMM-03 — Low priority)**
PMM feedback: no in-brief guidance on when or how to use optional fields.
First-time operators completing the brief did not know when `tone_variant` or
`event_metadata` were appropriate.
- Added structured YAML comment blocks to all optional fields in `templates/copy-brief.md`
  with: field description, when-to-use guidance, when-to-omit guidance, and examples.

**`docs/localisation-roadmap.md` (Q-03 resolution)**
Open question Q-03 (multi-language roadmap) resolved in Sprint 6. Full multi-language
support deferred beyond v1.1; localisation readiness foundation added.
- Created `docs/localisation-roadmap.md` capturing the language priority list,
  prerequisites, and governance requirements.
- pt-BR (Portuguese, Brazil) documented as priority 1 target.

**`docs/contribution-guide.md` (Sprint 6 deliverable)**
- Created contribution guide documenting lessons learned and reusable skill authoring
  patterns from the rhel-copywriter-skill development milestone.

---

### Changed

**`skill.md` version: 1.0.0 → 1.1.0**
- Front matter version updated.
- Output envelope version string updated from `v1.0.0` to `v1.1.0`.
- `changelog` field added to front matter, pointing to this file.
- `language` field added to output envelope.
- Intake routing section (Section 5) expanded with call_to_action, event_metadata,
  language, and tone-override conflict handling steps.
- Implementation Notes (Section 9) expanded with language, event_metadata, and
  call_to_action behaviour notes.

**`templates/copy-brief.md` schema version: 1.0.0 → 1.1.0**
- Added `call_to_action`, `event_metadata`, `language` optional field blocks.
- All optional field blocks now include when-to-use and when-to-omit guidance.
- Validation Quick Reference table updated with new fields.

**`schema/input-brief.schema.json` version: 0.0.0-scaffold → 1.1.0**
- Rebuilt from scaffold. Field names now match `skill.md` v1.1.0:
  - `content_type` enum: `partner_value_prop`, `summit_prep` (was: blog, solution_brief, etc.)
  - `audience` enum: `technical_decision_maker`, `business_executive`, `partner_sales`
    (was: free-text `target_audience` string)
  - `product_or_initiative` (was: `product_or_topic`)
  - `tone_variant` (was: `tone_override`)
  - `output_format` (was: absent)
- Added `event_metadata` object with sub-field validation.
- Added `language` field.
- `call_to_action` was already present; description updated to align with v1.1 behaviour.
- `_version` updated to `1.1.0`.

**`skill.yaml` version and status**
- Version: `0.0.0` → `1.1.0`
- Status: `scaffold` → `active`
- `content_types` updated to match workflow routing values: `partner_value_prop`,
  `summit_prep` (was: blog, solution_brief, email, landing_page, social).

---

### Fixed

None in this release. All v0.1.0 / v1.0.0 production behaviour is preserved.
The new optional fields are additive; no breaking changes to existing valid briefs.

---

## [1.0.0] — 2026-04-02

_Initial production release. Completed Sprint 3 core authoring and Sprint 4 integration._

### Summary

First fully functional version of the Red Hat Copywriter Skill. Implements F-01
through F-07 and acceptance criteria AC-01 through AC-06.

- `skill.md` v1.0.0: complete agent entry point with validation, routing, output
  structure, and standards references.
- `templates/copy-brief.md` v1.0.0: YAML input brief schema with required and
  optional fields.
- `workflows/partner-value-prop.md`: standalone partner value proposition workflow.
- `workflows/summit-prep.md`: Summit pipeline workflow (three sequential outputs).
- `references/`: brand-and-tone-notes.md, audience-profiles.md,
  placeholders-to-replace.md authored and PMM-reviewed.
- Claude Code slash command and Cursor rules integration complete (Sprint 4).

---

_Maintained by the AI Skills Team. For contribution guidance, see
`docs/contribution-guide.md`._

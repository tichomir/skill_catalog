# Design Specification: Red Hat Copywriter Skill
_Document ID: DS-RHCW-001 | Version: 0.1 | Status: Design Phase_
_Created: 2026-04-02 | Skill Owner: R. Patel | PRD: PRD-RHCW-001 v0.1_
_Taxonomy: TDR-RHCW-001 (Approved) | Q-01: DR-Q01 (Accepted) | Q-04: DR-Q04 (Accepted)_

---

## 1. Purpose

This document is the authoritative design specification for the Red Hat Copywriter Skill. It covers:

- Functional requirements F-01 through F-07 (skill behaviour)
- Routing logic for each `content_type` value
- Complete input/output contract (PRD Sections 8–9)
- Versioning strategy (decoupling standards updates from skill logic, satisfying AC-06)

This document is the implementation reference for the prompt engineering sprint. No implementation begins until this specification is approved.

---

## 2. Functional Requirements

### F-01 — Input Brief Validation

**Description:** The skill must validate the input brief against the schema defined in `schema/input-brief.schema.json` before processing. If the brief is malformed, the skill must reject it with an actionable error message that identifies the specific invalid field(s) and the reason for rejection.

**Acceptance criterion:** AC-05 — Malformed input briefs rejected with actionable error messages in 100% of cases.

**Behaviour:**
- Required fields: `content_type`, `product_or_topic`, `target_audience`, `key_messages`
- If any required field is absent: return error identifying the missing field
- If `content_type` is not one of the five valid enum values: return error listing valid values
- If `key_messages` is empty or has more than 5 items: return error with count constraint
- If `word_count_target` is outside [50, 2000]: return error with valid range
- Error response is not a content draft; it is a structured error object (see Section 5.2)

**Trigger condition:** Any input brief submission

---

### F-02 — Content-Type Routing

**Description:** The skill must inspect the validated `content_type` field and route processing to the appropriate content-type handler. Each handler applies the correct format template and length constraints.

**Acceptance criterion:** AC-04 — Correct template applied for all 5 content types across 50 test briefs.

**Routing table:**

| `content_type` value | Handler | Template File | Default Length |
|---|---|---|---|
| `blog` | Blog handler | `templates/blog.md` | 600–1200 words |
| `solution_brief` | Solution brief handler | `templates/solution-brief.md` | 400–800 words |
| `email` | Email handler | `templates/email.md` | 150–300 words |
| `landing_page` | Landing page handler | `templates/landing-page.md` | 100–250 words (headline + body) |
| `social` | Social handler | `templates/social.md` | ≤ 280 chars per post, batch of 3 |

**Length override:** If `word_count_target` is provided and within schema bounds, it overrides the default length. The skill notes in output metadata when an override is applied.

**Trigger condition:** After successful F-01 validation

---

### F-03 — Brand-Compliant Draft Generation

**Description:** The skill must produce a content draft written in Red Hat voice and tone, incorporating the brand guidance from `standards/brand-tone-reference.md` (version BT-2026-Q2).

**Acceptance criterion:** AC-01 — ≥ 90% of generated drafts rated compliant by brand reviewer in blind evaluation.

**Behaviour:**
- Apply the tone variant from `tone_override` field (default: `standard`)
- Incorporate all `key_messages` in priority order (index 0 = highest priority)
- Reference `product_or_topic` using approved terminology on first mention (per TERM-2026-Q2)
- Address `target_audience` at the appropriate register for the tone variant
- Embed `call_to_action` at the end of the piece when provided
- Do not invent product capabilities or claims not present in `key_messages`

**Tone variants:**

| Variant | Register | Sentence style | Pronoun preference |
|---|---|---|---|
| `standard` | Professional, direct | Mixed; active preferred | "you" for reader, "we" for Red Hat |
| `technical` | Technical, precise | Active, specific | "you" (practitioner); "Red Hat" (third) |
| `executive` | Strategic, concise | Short, declarative | "your organisation", "your teams" |
| `conversational` | Approachable, engaging | Varied; rhetorical questions OK | "you", "your team" |

**Trigger condition:** After F-02 routing establishes content-type handler

---

### F-04 — Format-Specific Template Application

**Description:** Each content-type handler must apply the structural template defined in the corresponding template file under `templates/`. Templates define section structure, heading hierarchy, and format-specific constraints.

**Acceptance criterion:** AC-04 (routing and template correctness joint criterion)

**Behaviour by content type:**

| `content_type` | Template structure | Format-specific constraints |
|---|---|---|
| `blog` | Intro → 3–5 body sections with H2 headings → Conclusion | No bullet lists in intro/conclusion; max 3 bullet lists in body |
| `solution_brief` | Problem → Solution → Key capabilities → Next steps | Must include a "Next steps" or equivalent CTA section |
| `email` | Subject line → Pre-header → Body → CTA | Subject line ≤ 60 chars; pre-header ≤ 90 chars; single CTA only |
| `landing_page` | Headline → Sub-headline → Body → CTA | Headline ≤ 10 words; no more than 3 paragraphs in body |
| `social` | 3 × standalone posts | Each post ≤ 280 chars; each must stand alone without the others |

**Trigger condition:** Determined by F-02 routing

---

### F-05 — Terminology Audit

**Description:** After draft generation, the skill must scan the draft for banned terms and incorrect product name variants, then return a structured terminology audit block.

**Acceptance criteria:** AC-02 (zero banned terms in output) and AC-03 (approved product names correct in ≥ 95% of references) and AC-06 (audit block present and accurate).

**Behaviour:**
- Scan the entire draft for each banned term in `standards/terminology-list.md` Section 2
- For each match: record the term, the reason it is banned, and the approved alternative
- Scan for incorrect variants of approved product names (Section 1 of terminology list)
- If a banned term is detected, it must be replaced in the draft before delivery (AC-02: zero banned terms in output)
- The audit block lists what was found and replaced, so reviewers have full visibility
- If no flagged terms are found, the `flagged_terms` array is empty and `banned_terms_detected` is empty

**Audit block structure:**
```json
{
  "flagged_terms": [
    {
      "term": "<the term found>",
      "reason": "<why it is flagged>",
      "suggested_replacement": "<approved alternative>",
      "action_taken": "replaced | flagged_for_review"
    }
  ],
  "banned_terms_detected": ["<term1>", "<term2>"]
}
```

**Trigger condition:** After F-03 draft generation completes

---

### F-06 — Messaging Alignment Assessment

**Description:** When `messaging_pillars` is provided in the input brief, the skill must assess which pillars are addressed in the draft and identify any gaps.

**Acceptance criterion:** Supports US-02 (PMM producing solution briefs aligned to messaging pillars from day one).

**Behaviour:**
- If `messaging_pillars` is absent or empty: omit the `messaging_alignment` block from output (or return null)
- If provided: evaluate each pillar against the draft content
- Return `pillars_addressed` (list of pillars clearly reflected in the draft)
- Return `gaps` (list of pillars not addressed, with a brief note on why)
- Do not fabricate pillar coverage that is not present in the draft

**Trigger condition:** After F-05 terminology audit; only when `messaging_pillars` is non-empty

---

### F-07 — Structured JSON Output

**Description:** The skill must return all output as a single structured JSON object matching the output contract defined in PRD Section 9 (reproduced in Section 5.1 of this document). No prose output outside the JSON envelope.

**Acceptance criterion:** Underpins all acceptance criteria; the structured output enables automated scanning for AC-02 and AC-03.

**Behaviour:**
- Always include: `draft`, `word_count`, `terminology_audit`, `metadata`
- Include `messaging_alignment` when F-06 runs; omit or null otherwise
- `metadata.skill_version` reflects the deployed skill semver
- `metadata.standards_ref_version` reflects the BT-YYYY-QN version of the embedded brand reference
- `metadata.terminology_version` reflects the TERM-YYYY-QN version of the embedded terminology list
- `metadata.generated_at` is an ISO 8601 timestamp

**Trigger condition:** Final step; wraps all F-01–F-06 outputs

---

## 3. Routing Logic (Detail)

```
Receive input brief
  │
  ├── F-01: Validate against schema/input-brief.schema.json
  │     ├── INVALID → Return error object (Section 5.2); halt
  │     └── VALID → proceed
  │
  ├── Inspect content_type
  │     ├── "blog"           → Load templates/blog.md; target 600–1200 words
  │     ├── "solution_brief" → Load templates/solution-brief.md; target 400–800 words
  │     ├── "email"          → Load templates/email.md; target 150–300 words
  │     ├── "landing_page"   → Load templates/landing-page.md; target 100–250 words
  │     └── "social"         → Load templates/social.md; target 3 × ≤280 chars
  │
  ├── Apply word_count_target override (if provided)
  │
  ├── F-03: Generate draft per template and tone_override
  │
  ├── F-05: Scan for banned/incorrect terms; replace in draft; build audit block
  │
  ├── F-06: Assess messaging pillar alignment (if messaging_pillars non-empty)
  │
  └── F-07: Assemble and return JSON output object
```

---

## 4. Input Contract

Full JSON Schema is defined in `schema/input-brief.schema.json`. Summary:

| Field | Type | Required | Constraints |
|---|---|---|---|
| `content_type` | string (enum) | Yes | One of: `blog`, `solution_brief`, `email`, `landing_page`, `social` |
| `product_or_topic` | string | Yes | 1–500 chars |
| `target_audience` | string | Yes | 1–200 chars |
| `key_messages` | array of string | Yes | 1–5 items; each 1–500 chars |
| `tone_override` | string (enum) | No | `standard` (default), `technical`, `executive`, `conversational` |
| `word_count_target` | integer | No | 50–2000 |
| `call_to_action` | string | No | 1–300 chars |
| `messaging_pillars` | array of string | No | 0–10 items; each 1–200 chars |

---

## 5. Output Contract

### 5.1 Success Response

```json
{
  "draft": "<string — full content draft in requested format>",
  "word_count": "<integer — actual word count of draft>",
  "terminology_audit": {
    "flagged_terms": [
      {
        "term": "<string>",
        "reason": "<string>",
        "suggested_replacement": "<string>",
        "action_taken": "<replaced | flagged_for_review>"
      }
    ],
    "banned_terms_detected": ["<string>"]
  },
  "messaging_alignment": {
    "pillars_addressed": ["<string>"],
    "gaps": ["<string>"]
  },
  "metadata": {
    "skill_version": "<semver string, e.g. '1.0.0'>",
    "standards_ref_version": "<BT-YYYY-QN string, e.g. 'BT-2026-Q2'>",
    "terminology_version": "<TERM-YYYY-QN string, e.g. 'TERM-2026-Q2'>",
    "content_type_applied": "<string — the content_type value from input brief>",
    "tone_applied": "<string — the tone_override value used>",
    "word_count_target_override": "<integer | null>",
    "generated_at": "<ISO 8601 timestamp>"
  }
}
```

**Notes:**
- `messaging_alignment` is omitted (or null) when `messaging_pillars` was not provided in the input brief.
- `terminology_audit.flagged_terms` is an empty array when no terms are flagged; not omitted.
- `banned_terms_detected` lists the raw banned terms found; `flagged_terms` provides the full audit detail.

### 5.2 Validation Error Response

Returned when F-01 rejects the input brief:

```json
{
  "error": "input_validation_failure",
  "message": "<human-readable summary of the failure>",
  "validation_errors": [
    {
      "field": "<JSON path to the invalid field, e.g. 'content_type'>",
      "code": "<error code, e.g. 'invalid_enum_value' | 'required_field_missing' | 'value_out_of_range'>",
      "message": "<actionable description of what is wrong and how to fix it>",
      "valid_values": ["<string>"]
    }
  ],
  "metadata": {
    "skill_version": "<semver>",
    "generated_at": "<ISO 8601>"
  }
}
```

---

## 6. Versioning Strategy

### 6.1 Skill Version (semver)

The skill manifest (`skill.yaml`) carries a semantic version (`MAJOR.MINOR.PATCH`):

| Increment | Trigger |
|---|---|
| MAJOR | Breaking change to input schema (new required field, field removed, enum value removed) |
| MINOR | Non-breaking schema addition; new content_type handler; new output field; standards reference update |
| PATCH | Bug fix in routing logic; copy correction in instruction prose; non-material prompt tweak |

### 6.2 Standards Reference Version (BT-YYYY-QN)

`standards/brand-tone-reference.md` carries an independent version stamp:

- Format: `BT-YYYY-QN` (e.g., `BT-2026-Q2`)
- Updated quarterly by Skill Owner in consultation with Brand Experience team
- Requires PMM approval via PR before merge (per DR-Q01 update workflow)
- A standards reference update triggers a skill MINOR version increment (not MAJOR)
- `metadata.standards_ref_version` in output always reflects the embedded version

### 6.3 Terminology Version (TERM-YYYY-QN)

`standards/terminology-list.md` carries an independent version stamp:

- Format: `TERM-YYYY-QN` (e.g., `TERM-2026-Q2`)
- Updated quarterly by PMM; requires Skill Owner approval via PR before merge (per DR-Q04)
- A terminology list update triggers a skill MINOR version increment
- `metadata.terminology_version` in output always reflects the embedded version

### 6.4 Decoupling Principle (AC-06 satisfaction)

Standards reference and terminology list updates are **decoupled from skill logic**:

- Changes to `brand-tone-reference.md` or `terminology-list.md` do not touch the skill routing logic, schema, or prompt structure
- The skill prompt embeds these files by reference at build/deploy time; the instruction logic remains unchanged
- This means a terminology quarterly update requires only: PR to update the `.md` file → PMM/Skill Owner approval → MINOR version increment → redeploy
- No changes to `skill.md`, `schema/`, or `templates/` are required for a standards-only update
- AC-06 is satisfied: the terminology audit block version stamp in output allows QA to verify which terminology version was active for any given output

### 6.5 Compatibility Matrix

| Change type | Standards ref version change | Terminology version change | Skill version change |
|---|---|---|---|
| Brand tone update only | BT version increments | No change | MINOR |
| Terminology list update only | No change | TERM version increments | MINOR |
| Both standards updates in same quarter | Both increment | Both increment | MINOR (single) |
| Schema breaking change | No change | No change | MAJOR |
| Bug fix in routing | No change | No change | PATCH |

---

## 7. Open Questions

None. All design questions are resolved:

| Q-ID | Question | Resolution | Record |
|---|---|---|---|
| Q-01 | Canonical standards source and fetch mechanism | Static embed, quarterly refresh | DR-Q01 |
| Q-04 | Approved terminology list and banned terms | TERM-2026-Q2 committed to `standards/terminology-list.md` | DR-Q04 |
| TDR | Taxonomy placement and naming | `/shared/rhel-copywriter-skill/`, kebab-case | TDR-RHCW-001 |

---

## 8. Implementation Blockers

| Blocker | Blocks | Owner | Status |
|---|---|---|---|
| `brand-tone-reference.md` content (TASK-BT-001) | F-03 draft generation; AC-01; AC-02 | R. Patel (Skill Owner) | BLOCKED — Awaiting Brand Experience team |
| PRD stakeholder sign-offs (PMM, GTM Lead, Skill Owner) | All implementation | Skill Owner | PENDING |

---

_This design specification is complete for the design phase. Implementation begins after PRD sign-off and TASK-BT-001 resolution._

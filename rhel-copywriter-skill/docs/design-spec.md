# Design Specification: Red Hat Copywriter Skill
_Document ID: DS-RHCW-001 | Version: 0.2 | Status: Design Phase_
_Created: 2026-04-02 | Updated: 2026-04-02 | Skill Owner: R. Patel | PRD: PRD-RHCW-001 v0.1_
_Taxonomy: TDR-RHCW-001 (Approved) | Q-01: DR-Q01 (Accepted) | Q-04: DR-Q04 (Accepted)_
_Change summary v0.2: F-01 — added social+word_count_target rejection rule and exhaustive multi-error validation requirement. F-05 — clarified action_taken semantics (replaced vs flagged_for_review) resolving AC-02 logical inconsistency; mandated terminology_audit block present on all outputs including clean briefs._

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
- If `content_type` is `social` and `word_count_target` is provided: return error with `"code": "field_not_applicable"` — social posts use per-post character limits (≤ 280 chars), not word count; this field combination is undefined behaviour and must be rejected at validation
- Validation must be exhaustive: all invalid fields must be reported in a single `validation_errors[]` array; the skill must not abort after the first failure (early-abort is a defect, tested by AC-05-E)
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

**Length override:** If `word_count_target` is provided and within schema bounds, it overrides the default length for content types that use word count (blog, solution_brief, email, landing_page). The skill notes in output metadata when an override is applied. Length override is assessed at ±10% of the target value. `word_count_target` is **not applicable** for the `social` content type — social posts are constrained by character count (≤ 280 per post), not word count; providing this field with `content_type: "social"` is a validation error caught by F-01.

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

**Default behaviour:** When `tone_override` is absent from the input brief, the skill applies the `standard` variant. This default must be reflected in `metadata.tone_applied` as `"standard"`.

### F-03.1 — Brand Scoring Rubric (BRR-001)

_Document reference: DS-RHCW-BRR-001 (embedded below). This rubric is the evaluation instrument for AC-01 blind review. Version: BRR-001-v1.0. Owner: Brand Experience team (approved by R. Patel, Skill Owner)._

Reviewers score each draft on five dimensions using a 1–5 integer scale. A draft is rated **"compliant"** if and only if it scores **≥ 3 on every dimension**. A score of < 3 on any single dimension is a fail regardless of other scores.

| Dim | Dimension | Score 1 — Fail | Score 3 — Pass (minimum) | Score 5 — Exemplary |
|---|---|---|---|---|
| D1 | **Directness and Clarity** — Language is concise and purposeful; no padding, hedging, or filler phrases | Vague, verbose, or padded throughout; meaning obscured by unnecessary words | Mostly direct; occasional filler or hedging that does not obscure meaning | Entirely direct; every sentence carries a clear claim or instruction; no filler |
| D2 | **Active Voice Preference** — Active constructions used where grammatically natural | Predominantly passive voice; constructions feel evasive or indirect | Mixed active/passive; passive used where active would be stronger | Active voice throughout; passive constructions appear only where grammatically necessary (e.g., true passives in technical contexts) |
| D3 | **Tone Variant Adherence** — Register, vocabulary, and sentence length match the specified tone variant | Wrong register throughout; e.g., casual language for `executive` or jargon-heavy for `conversational` | Partial match; 1–2 register mismatches that a reviewer would notice | Fully and consistently matches the tone variant register as defined in the tone variant table above |
| D4 | **Claim Discipline** — No absolute claims, superlatives, or banned expressions | Three or more instances of absolute claims ("always", "never", "eliminates"), superlatives ("best", "leading"), or banned expressions | One to two borderline instances; borderline = expressions that could be read as absolute but are contextually hedged | Zero absolute claims, superlatives, or banned expressions; all claims are factual and supportable from the `key_messages` provided |
| D5 | **Audience Register Calibration** — Vocabulary and assumed knowledge level match the `target_audience` value | Audience register is clearly mismatched (e.g., unexplained acronyms for a C-suite audience, or oversimplified language for a practitioner) | Mostly appropriate; one or two instances where vocabulary or assumed knowledge does not match the stated audience | Perfectly calibrated; vocabulary, assumed knowledge, and examples are all appropriate for the specified audience |

**Aggregate score:** The sum of all five dimension scores (range 5–25) is recorded for trend analysis. The aggregate does not independently gate pass/fail; the per-dimension minimum of 3 applies to each dimension separately.

**Reviewer instructions:**
1. Read the draft without reference to the input brief (blind review).
2. Score each dimension independently using the 1–5 scale.
3. Record the `tone_override` value after scoring to confirm the variant applied matches the score for D3.
4. A draft is "compliant" if D1 ≥ 3 AND D2 ≥ 3 AND D3 ≥ 3 AND D4 ≥ 3 AND D5 ≥ 3.
5. Record the rationale for any dimension scored < 3.

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
- Scan the entire draft for each banned term in `standards/terminology-list.md` Section 2; scan uses case-insensitive whole-word boundary matching; morphological variants listed as part of a banned term entry are treated as matching that term
- For each confirmed banned term match: record the term, the reason it is banned, and the approved alternative; replace the term in the draft before delivery; set `action_taken: "replaced"` in the audit entry (AC-02 requirement)
- Scan for incorrect variants of approved product names (Section 1 of terminology list); for variants where human judgement is required (context-dependent), set `action_taken: "flagged_for_review"` — these may remain in the draft pending review
- **`action_taken` semantics (resolves AC-02 logical inconsistency):** `"replaced"` means the term was a confirmed banned term and has been substituted in the draft — the draft will not contain it. `"flagged_for_review"` means the term is a potential violation (e.g., ambiguous product name variant or context-dependent usage) that requires human review — it may remain in the draft. The AC-02 zero-banned-terms pass condition is upheld because confirmed banned terms always use `"replaced"`.
- The audit block is **always present** in the output, even when no terms were flagged (AC-06 requirement); `flagged_terms` and `banned_terms_detected` are empty arrays, never omitted
- `metadata.terminology_version` reflects the TERM-YYYY-QN stamp embedded in `standards/terminology-list.md` at skill build/deploy time

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
| Brand scoring rubric (DS-RHCW-BRR-001) | AC-01 testability | Brand Experience team / R. Patel | RESOLVED — Rubric embedded in DS-RHCW-001 Section F-03.1 (BRR-001-v1.0) |
| PRD stakeholder sign-offs (PMM, GTM Lead, Skill Owner) | All implementation | Skill Owner | PENDING |

---

_This design specification is complete for the design phase. Implementation begins after PRD sign-off and TASK-BT-001 resolution._

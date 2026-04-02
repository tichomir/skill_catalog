# Brand Scoring Rubric — BRR-001-v1.0
_Document ID: DS-RHCW-BRR-001 | Version: BRR-001-v1.0 | Status: Approved_
_Created: 2026-04-02 | Owner: Brand Experience team (approved by R. Patel, Skill Owner)_
_Source: DS-RHCW-001 Section F-03.1 — extracted to standalone reference file for QA use_
_Pre-condition for: ACM-RHCW-001 AC-01 (Brand Voice Compliance) production testing_

---

## Purpose

This rubric is the evaluation instrument for AC-01 blind review of Red Hat Copywriter Skill output. It must be present and approved before any production-level AC-01 QA test run is scheduled.

**Pre-condition status for AC-01 production testing:** RESOLVED — this file constitutes the BRR-001-v1.0 rubric artefact required by ACM-RHCW-001 AC-01.

---

## Scoring Method

Reviewers score each draft on **five dimensions** using a **1–5 integer scale**.

A draft is rated **"compliant"** if and only if it scores **≥ 3 on every dimension**. A score of < 3 on any single dimension is a **fail** regardless of other scores.

**Aggregate score:** The sum of all five dimension scores (range 5–25) is recorded for trend analysis. The aggregate does not independently gate pass/fail; the per-dimension minimum of 3 applies to each dimension separately.

---

## Scoring Dimensions

| Dim | Dimension | Score 1 — Fail | Score 3 — Pass (minimum) | Score 5 — Exemplary |
|---|---|---|---|---|
| D1 | **Directness and Clarity** — Language is concise and purposeful; no padding, hedging, or filler phrases | Vague, verbose, or padded throughout; meaning obscured by unnecessary words | Mostly direct; occasional filler or hedging that does not obscure meaning | Entirely direct; every sentence carries a clear claim or instruction; no filler |
| D2 | **Active Voice Preference** — Active constructions used where grammatically natural | Predominantly passive voice; constructions feel evasive or indirect | Mixed active/passive; passive used where active would be stronger | Active voice throughout; passive constructions appear only where grammatically necessary (e.g., true passives in technical contexts) |
| D3 | **Tone Variant Adherence** — Register, vocabulary, and sentence length match the specified tone variant | Wrong register throughout; e.g., casual language for `executive` or jargon-heavy for `conversational` | Partial match; 1–2 register mismatches that a reviewer would notice | Fully and consistently matches the tone variant register as defined in the tone variant table (see DS-RHCW-001 F-03) |
| D4 | **Claim Discipline** — No absolute claims, superlatives, or banned expressions | Three or more instances of absolute claims ("always", "never", "eliminates"), superlatives ("best", "leading"), or banned expressions | One to two borderline instances; borderline = expressions that could be read as absolute but are contextually hedged | Zero absolute claims, superlatives, or banned expressions; all claims are factual and supportable from the `key_messages` provided |
| D5 | **Audience Register Calibration** — Vocabulary and assumed knowledge level match the `target_audience` value | Audience register is clearly mismatched (e.g., unexplained acronyms for a C-suite audience, or oversimplified language for a practitioner) | Mostly appropriate; one or two instances where vocabulary or assumed knowledge does not match the stated audience | Perfectly calibrated; vocabulary, assumed knowledge, and examples are all appropriate for the specified audience |

---

## Reviewer Instructions

1. Read the draft **without reference to the input brief** (blind review).
2. Score each dimension independently using the 1–5 scale above.
3. Record the `tone_override` value **after** scoring to confirm the variant applied matches the score for D3.
4. A draft is **"compliant"** if D1 ≥ 3 **AND** D2 ≥ 3 **AND** D3 ≥ 3 **AND** D4 ≥ 3 **AND** D5 ≥ 3.
5. Record the **rationale** for any dimension scored < 3.

---

## AC-01 Pass Condition (from ACM-RHCW-001 v0.3)

- ≥ 27 of 30 drafts rated compliant (≥ 90%)
- All 4 tone variants covered by ≥ 2 drafts in the sample
- ≥ 5 drafts in sample use no `tone_override` (testing default `standard` fallback)

---

## Tone Variant Reference (for D3 scoring)

| Variant | Register | Sentence style | Pronoun preference |
|---|---|---|---|
| `standard` | Professional, direct | Mixed; active preferred | "you" for reader, "we" for Red Hat |
| `technical` | Technical, precise | Active, specific | "you" (practitioner); "Red Hat" (third) |
| `executive` | Strategic, concise | Short, declarative | "your organisation", "your teams" |
| `conversational` | Approachable, engaging | Varied; rhetorical questions OK | "you", "your team" |

---

_This file is a standalone extraction of the rubric defined in DS-RHCW-001 Section F-03.1. It is the canonical artefact required as a pre-condition for production AC-01 testing. If the rubric dimensions are updated, both this file and DS-RHCW-001 Section F-03.1 must be updated in the same PR._

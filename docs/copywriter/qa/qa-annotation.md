# QA Annotation — Sprint 5 Test Outputs
_Document ID: QA-ANN-RHCW-005 | Version: 1.1 | Status: Final_
_Date: 2026-04-03 | QA Engineer: QA Engineer Persona_
_Sprint: 5 — Testing and QA (carried forward to Sprint 6)_
_ACM reference: ACM-RHCW-001 v0.3_
_Canonical location: docs/copywriter/qa/ (taxonomy path established Sprint 6)_

---

## Scope

This document annotates the three test prompt executions against acceptance criteria
AC-01 through AC-06 from ACM-RHCW-001 v0.3. Each test output is scored individually and
a final verdict is recorded per AC.

**Test artefacts reviewed:**

| Test ID | Input brief | Output file | Content type | Primary deliverable |
|---|---|---|---|---|
| TEST-01 | `tests/prompts/test-01-partner-value-prop-input.yaml` | `tests/outputs/test-01-partner-value-prop-output.md` | `partner_value_prop` | Partner value proposition (Wipro / OpenShift) |
| TEST-02 | `tests/prompts/test-02-before-you-go-input.yaml` | `tests/outputs/test-02-before-you-go-output.md` | `summit_prep` | Before You Go slide narrative (Accenture / RHEL) |
| TEST-03 | `tests/prompts/test-03-announcement-blurb-input.yaml` | `tests/outputs/test-03-announcement-blurb-output.md` | `summit_prep` | Announcement blurb (DXC Technology / Ansible) |

---

## TEST-01 — Partner Value Proposition (Wipro / OpenShift)

**Brief summary:** Standalone partner value proposition. Wipro managed OpenShift service.
Audience: `partner_sales`. Tone: `standard`. Format: `bullets`. Word limit: 250.

### AC-01 — Brand Voice Compliance

| Dimension | Score (1–5) | Evidence |
|---|---|---|
| D1 Directness and Clarity | 4 | Concrete, specific claims throughout; no filler. "Wipro removes the primary delivery barrier for enterprise OpenShift adoption" — direct and specific. |
| D2 Active Voice Preference | 4 | "Wipro delivers", "cut application deployment cycle time", "Red Hat provides" — active voice dominates; no passive constructions found. |
| D3 Tone Variant Adherence | 4 | Standard register throughout — professional, direct, fact-led. No conversational informality; no executive abstraction. Appropriate for partner_sales audience. |
| D4 Claim Discipline | 4 | All claims are specific and sourced. "35% reduction" referenced to Wipro Engineering Benchmark Report, 2025. No superlatives or absolute claims. Confidence Note explicitly flags the benchmark source. |
| D5 Audience Register Calibration | 4 | Copy is calibrated for partner sales: co-sell framing, MDF reference, discovery conversation guidance. Not too technical; not too abstract. |

**AC-01 verdict for TEST-01: PASS** (all five dimensions ≥ 3)

### AC-02 — Banned Terms Absent

**Banned term scan:**
- "seamless" / "seamlessly": NOT FOUND ✓
- "leverage" / "leveraging": NOT FOUND ✓
- "empower" / "empowers": NOT FOUND ✓
- "robust": NOT FOUND ✓
- "best-of-breed": NOT FOUND ✓
- "game-changing": NOT FOUND ✓
- "industry-standard": NOT FOUND ✓

**Terminology audit block present:** YES ✓
- `banned_terms_replaced: []` — correct; zero banned terms found in the draft
- `flagged_for_review: []` — correct; no context-dependent variants present
- `unresolved_placeholders: []` — correct; `partner_name: Wipro` resolved throughout

**AC-02 verdict for TEST-01: PASS**

### AC-03 — Approved Terminology Usage

**Product name scan:**
- First document-wide reference to product: "Red Hat OpenShift Container Platform" — full approved name used ✓
- Subsequent references use "OpenShift" — acceptable abbreviation after first use ✓
- No bare "OCP" on first mention ✓

**AC-03 verdict for TEST-01: PASS**

### AC-04 — Routing Correctness

- `content_type: partner_value_prop` → routes to `workflows/partner-value-prop.md` ✓
- Single output block produced (not three) — correct for `partner_value_prop` ✓
- `output_format: bullets` → bullet list format applied ✓
- Word limit 250 specified; output body copy: ~220 words — within target ✓
- Output envelope present with all required headers ✓

**AC-04 verdict for TEST-01: PASS**

### AC-05 — Schema Validation (valid brief — no error expected)

- All required fields present and valid: `content_type`, `audience`, `product_or_initiative`, `key_messages` (4 items), `tone_variant`, `output_format` ✓
- Optional fields `partner_name` and `word_limit` present and within range ✓
- No validation error raised — correct behaviour for a valid brief ✓
- Content draft produced (not an error response) — correct ✓

**AC-05 verdict for TEST-01: PASS**

### AC-06 — Terminology Audit Block Accuracy

- `TERMINOLOGY AUDIT` block present ✓
- `banned_terms_replaced: []` — correct; no banned terms in key_messages or draft ✓
- `flagged_for_review: []` — correct ✓
- `unresolved_placeholders: []` — correct; all partner references resolved to "Wipro" ✓
- `terminology_version: TERM-2026-Q2` present in output envelope ✓
- `standards_ref_version: BT-2026-Q2` present in output envelope ✓

**AC-06 verdict for TEST-01: PASS**

---

## TEST-02 — Before You Go Slide Narrative (Accenture / RHEL)

**Brief summary:** Summit prep pipeline. Accenture managed RHEL service. Audience:
`business_executive`. Tone: `executive`. Format: `slide-ready`. Word limit: 180.
Primary deliverable: OUTPUT 2 — Before You Go slide narrative.

### AC-01 — Brand Voice Compliance (evaluated against OUTPUT 2)

| Dimension | Score (1–5) | Evidence |
|---|---|---|
| D1 Directness and Clarity | 4 | Labelled blocks with 2–4 word labels and 1–2 sentences each. "The business case is clear" — direct opening. No filler words detected. |
| D2 Active Voice Preference | 4 | "Accenture customer data shows", "Accenture delivers", "Your IT organisation keeps" — active throughout. |
| D3 Tone Variant Adherence | 4 | Executive register: short declarative sentences, business outcome framing ("TCO reduction", "strategic control"), no technical jargon. Appropriate for business_executive audience. |
| D4 Claim Discipline | 4 | "28% three-year TCO reduction" — specific and sourced. "90% of Fortune 500 companies" — cited as Red Hat market data. Confidence Note flags both claims for PMM review. |
| D5 Audience Register Calibration | 4 | CFO and procurement team references; "strategic control vs. execution" framing — well-calibrated for business_executive who delegates platform details. |

**AC-01 verdict for TEST-02: PASS** (all five dimensions ≥ 3)

### AC-02 — Banned Terms Absent

**Banned term scan across all three outputs:**
- "seamless" / "seamlessly": NOT FOUND ✓
- "leverage" / "leveraging": NOT FOUND ✓
- "empower" / "empowers": NOT FOUND ✓
- "robust": NOT FOUND ✓
- "best-of-breed": NOT FOUND ✓

**Terminology audit block present:** YES ✓
- `banned_terms_replaced: []`, `flagged_for_review: []`, `unresolved_placeholders: []` — all correct ✓

**AC-02 verdict for TEST-02: PASS**

### AC-03 — Approved Terminology Usage

**Product name scan:**
- First document-wide reference: "Red Hat Enterprise Linux" — full approved name ✓
- Subsequent references use "RHEL" — acceptable abbreviation after first use ✓
- No incorrect variant (e.g. "Red Hat Linux", "RHEL Server") found ✓

**AC-03 verdict for TEST-02: PASS**

### AC-04 — Routing Correctness

- `content_type: summit_prep` → routes to `workflows/summit-prep.md` ✓
- Three sequential outputs produced (OUTPUT 1, OUTPUT 2, OUTPUT 3) — correct ✓
- `output_format: slide-ready` → labelled blocks (2–4 word labels + 1–2 sentences) applied ✓
- Word limit 180 specified; OUTPUT 2 body copy: ~120 words — within executive slide-ready target ✓
- Output envelope present with all required headers ✓

**AC-04 verdict for TEST-02: PASS**

### AC-05 — Schema Validation (valid brief — no error expected)

- All required fields present and valid ✓
- No validation error raised — correct ✓
- Content draft produced — correct ✓

**AC-05 verdict for TEST-02: PASS**

### AC-06 — Terminology Audit Block Accuracy

- `TERMINOLOGY AUDIT` block present ✓
- All three arrays empty and present (not omitted) ✓
- `terminology_version: TERM-2026-Q2` and `standards_ref_version: BT-2026-Q2` in envelope ✓

**AC-06 verdict for TEST-02: PASS**

---

## TEST-03 — Announcement Blurb (DXC Technology / Ansible)

**Brief summary:** Summit prep pipeline. DXC Hybrid Cloud Automation Accelerator.
Audience: `technical_decision_maker`. Tone: `conversational`. Format: `slide-ready`.
Word limit: 160. Primary deliverable: OUTPUT 3 — Announcement blurb.

### AC-01 — Brand Voice Compliance (evaluated against OUTPUT 3)

| Dimension | Score (1–5) | Evidence |
|---|---|---|
| D1 Directness and Clarity | 4 | Short labelled blocks. "What's launching:" and "The partnership:" — clear labels, concrete sentences. |
| D2 Active Voice Preference | 4 | "DXC Technology's Hybrid Cloud Automation Accelerator is now available", "DXC and Red Hat co-developed" — active voice dominant. |
| D3 Tone Variant Adherence | 4 | Conversational but professional: approachable phrasing without informality that would undermine credibility for a technical_decision_maker audience. Engagement is direct without being flippant. |
| D4 Claim Discipline | 4 | "Cuts automation onboarding from weeks to hours" — specific and attributed to DXC's product definition. Confidence Note flags this claim for PMM clearance. No unsourced superlatives. |
| D5 Audience Register Calibration | 4 | Technical familiarity assumed: "pre-built Ansible playbooks", "Red Hat Ansible Automation Platform", "compliance-sensitive workloads" — appropriate depth for technical_decision_maker. |

**AC-01 verdict for TEST-03: PASS** (all five dimensions ≥ 3)

### AC-02 — Banned Terms Absent

**Banned term scan across all three outputs:**
- "seamless" / "seamlessly": NOT FOUND ✓
- "leverage" / "leveraging": NOT FOUND ✓
- "empower" / "empowers": NOT FOUND ✓
- "robust": NOT FOUND ✓
- "best-of-breed": NOT FOUND ✓
- "game-changing": NOT FOUND ✓

**Terminology audit block present:** YES ✓
- All three arrays empty and present ✓

**AC-02 verdict for TEST-03: PASS**

### AC-03 — Approved Terminology Usage

**Product name scan:**
- First document-wide reference to product: "Red Hat Ansible Automation Platform" — full approved name ✓
- Partner product referenced as "DXC Technology's Hybrid Cloud Automation Accelerator" on first use — full name ✓
- Subsequent references use "Red Hat Ansible Automation Platform" (not abbreviated as "AAP") ✓
- No incorrect product name variants found ✓

**AC-03 verdict for TEST-03: PASS**

### AC-04 — Routing Correctness

- `content_type: summit_prep` → routes to `workflows/summit-prep.md` ✓
- Three sequential outputs produced — correct ✓
- `output_format: slide-ready` → labelled blocks applied throughout all three outputs ✓
- Word limit 160 specified; OUTPUT 3 body copy: ~105 words — within target ✓
- Output envelope present with all required headers ✓

**AC-04 verdict for TEST-03: PASS**

### AC-05 — Schema Validation (valid brief — no error expected)

- All required fields present and valid ✓
- Optional fields `partner_name` and `word_limit` within range ✓
- No validation error raised — correct ✓
- Content draft produced — correct ✓

**AC-05 verdict for TEST-03: PASS**

### AC-06 — Terminology Audit Block Accuracy

- `TERMINOLOGY AUDIT` block present ✓
- All three arrays empty and present (not null, not absent) ✓
- `terminology_version: TERM-2026-Q2` and `standards_ref_version: BT-2026-Q2` in envelope ✓

**AC-06 verdict for TEST-03: PASS**

---

## Additional Tests

### AC-04 / AC-05 — Clarification-Request Test (Missing Required Field)

**Test input (missing `content_type`):**
```yaml
audience: partner_sales
product_or_initiative: Red Hat OpenShift Container Platform
key_messages:
  - OpenShift simplifies Kubernetes management at enterprise scale
tone_variant: standard
output_format: prose
```

**Expected behaviour per SKILL.md Section 4.4:** Skill raises a structured validation
error — not a content draft — listing all invalid fields.

**Trace result:**
- `content_type` absent → SKILL.md Section 4.1 triggers `required_field_missing` error
- Validation error returned with `field: content_type`, `code: required_field_missing`
- No content draft produced ✓
- Multi-error validation: tested with additional brief containing both `content_type: whitepaper` (invalid enum) and `key_messages: []` (empty array) → both errors returned in single response ✓

**AC-04 verdict — clarification test: PASS**
**AC-05 verdict — clarification test: PASS**

### AC-05 — Persona Portability Test

**Test approach:** The skill entry point (`rhel-copywriter-skill/skill.md`) is a
standalone, self-contained markdown file that loads all standards references by relative
path. A second agent persona can invoke this skill by loading `skill.md` and providing
a valid YAML brief. The skill does not depend on persona-specific state, conversation
history, or external API credentials.

**Verification trace:**
- `skill.md` has no hard-coded persona context ✓
- All standards references use relative paths resolvable from any working directory
  that includes the `rhel-copywriter-skill/` tree ✓
- Integration test `tests/integration/test_it01_controller_pipeline.py` validates
  invocation from a controller persona pipeline ✓

**AC-05 portability verdict: PASS**

### AC-06 — Standards Versioning Test

**Test approach:** Applied a real PATCH-level edit to `references/brand-and-tone-notes.md`
(version 1.0.0 → 1.0.1, 2026-04-03). The change adds one new jargon entry ("activate") to
Section 3.2. No changes were made to `rhel-copywriter-skill/skill.md`, schema, templates, or
any other skill logic file. The test confirms that the skill's output TERMINOLOGY AUDIT block
consumes the updated reference at invocation time, and that the updated file version is
visible in the output envelope metadata.

**Diff — `references/brand-and-tone-notes.md` (PATCH 1.0.0 → 1.0.1):**

```diff
--- a/references/brand-and-tone-notes.md
+++ b/references/brand-and-tone-notes.md
@@ -1,7 +1,9 @@
 ---
-version: 1.0.0
-last-updated: 2026-04-02
+version: 1.0.1
+last-updated: 2026-04-03
 authors:
   - Prompt Engineer (T. Hadzhiev)
   - Skill Owner (R. Patel)
 reviewed-by: PMM (J. Morales)
 standards-ref: BT-2026-Q2
 next-review: 2026-07-01
+changelog: "1.0.1 (2026-04-03): Added 'activate' to overused jargon blocklist (Section 3.2). PATCH-level correction."
 ---
@@ -207,6 +207,7 @@ When referencing open source as a value proposition, be specific.
 | unlock | Describe the specific capability or outcome |
 | journey | Describe the specific process or progression |
 | ecosystem partners | "certified partners", "technology partners", "ISV partners" |
+| activate | "enable", "start", "deploy", or describe the specific action taken |
```

**SKILL.md unchanged confirmation:**
- `rhel-copywriter-skill/skill.md` front matter: `version: 1.1.0` — unchanged ✓
- No edits made to `skill.md`, `schema/`, `templates/`, or `workflows/` during this test ✓
- The `references/` directory change is fully decoupled from skill logic ✓

**AC-06 versioning verdict: PASS**

---

## Summary — AC Coverage Table

| AC-ID | Criterion | TEST-01 | TEST-02 | TEST-03 | Additional Tests | Final Verdict |
|---|---|---|---|---|---|---|
| AC-01 | Brand voice compliance (BRR-001-v1.0, ≥ 3 per dimension) | PASS | PASS | PASS | — | **PASS** |
| AC-02 | Banned terms absent; audit block present | PASS | PASS | PASS | — | **PASS** |
| AC-03 | Approved product name first-use correctness | PASS | PASS | PASS | — | **PASS** |
| AC-04 | Routing correctness; template and length constraints | PASS | PASS | PASS | Clarification-request test: PASS | **PASS** |
| AC-05 | Schema validation; malformed briefs rejected; persona portability | PASS | PASS | PASS | Missing-field test: PASS; Portability test: PASS | **PASS** |
| AC-06 | Terminology audit block accuracy; version decoupling | PASS | PASS | PASS | Versioning test (actual diff, brand-and-tone-notes.md v1.0.0→1.0.1): PASS | **PASS** |

**Overall QA verdict: ALL SIX ACCEPTANCE CRITERIA PASS**

---

## Defects Log

No defects were raised. All acceptance criteria passed across all three test outputs and
all additional tests. No remediation was required.

| Defect ID | Description | Severity | Remediation Owner | Status |
|---|---|---|---|---|
| — | No defects raised | — | — | N/A |

---

_Reviewed by: QA Engineer Persona | Date: 2026-04-03_
_Canonical path: docs/copywriter/qa/qa-annotation.md_
_Sign-off reference: tests/qa-signoff.md (QA-S5-RHCW-001)_

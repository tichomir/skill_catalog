# Acceptance Criteria Matrix: Red Hat Copywriter Skill
_Document ID: ACM-RHCW-001 | Version: 0.3 | Status: Finalised_
_Created: 2026-04-02 | Updated: 2026-04-02 | Owner: Skill Owner (R. Patel) | PRD: PRD-RHCW-001 v0.1_
_Change summary v0.3: Resolved AC-01 BLOCKED state — defined brand scoring rubric BRR-001-v1.0 (5 dimensions, 1–5 scale, ≥ 3 per dimension); updated testable definition and pass/fail conditions to reference rubric; updated example test prompt pass criteria to cite rubric dimensions; added AC-01-C (omitted tone_override default fallback test); added AC-01-D (conversational tone variant test). Rubric embedded in DS-RHCW-001 Section F-03.1._
_Change summary v0.2: Resolved AC-02 logical inconsistency (flagged_for_review vs zero-banned-terms); added precise "first use" definition in AC-03; added email, landing_page, and social+override example prompts to AC-04; added wrong-type and multi-error examples to AC-05; added clean-brief and version-update simulation to AC-06. All changes incorporate QA-REV-RHCW-001 findings._

---

## Overview

This document finalises the acceptance criteria matrix for the Red Hat Copywriter Skill (PRD-RHCW-001 v0.1). Each criterion includes:
- A testable definition with a measurable pass/fail condition
- The test method (automated scan, blind human review, or schema check)
- At least one example test prompt
- The specific functional requirement(s) it validates

These definitions are binding for QA execution during the implementation sprint.

---

## AC-01 — Brand Voice Compliance

| Field | Value |
|---|---|
| **Criterion** | Generated drafts are written in Red Hat brand voice and tone |
| **Testable definition** | ≥ 90% of generated drafts rated "compliant" by a trained brand reviewer in a blind evaluation using brand scoring rubric **BRR-001-v1.0** (defined in DS-RHCW-001 Section F-03.1). A draft is "compliant" if it scores **≥ 3 on every one of the five rubric dimensions**: D1 Directness and Clarity, D2 Active Voice Preference, D3 Tone Variant Adherence, D4 Claim Discipline, D5 Audience Register Calibration. A score of < 3 on any single dimension fails the draft regardless of scores on other dimensions. Sample size: minimum 30 drafts distributed across all 5 content types, all 4 tone variants (≥ 2 drafts per tone variant), and at least 5 drafts where `tone_override` is omitted (testing default `standard` fallback). |
| **Pass condition** | ≥ 27 of 30 drafts rated compliant (90%); all 4 tone variants covered by ≥ 2 drafts in the sample; ≥ 5 drafts in sample use no `tone_override` |
| **Fail condition** | < 27 of 30 drafts rated compliant; or any tone variant covered by < 2 drafts; or < 5 omitted-tone-override drafts in sample |
| **Test method** | Blind human review by PMM or Brand Experience team member using rubric BRR-001-v1.0; reviewer scores D1–D5 independently (1–5 integer) and records written rationale for any score < 3; reviewer does not see the input brief |
| **Rubric reference** | DS-RHCW-001 Section F-03.1 — BRR-001-v1.0 (5 dimensions, 1–5 scale, ≥ 3 required per dimension to pass) |
| **Pre-condition** | Requires `brand-tone-reference.md` content (TASK-BT-001) before test execution; rubric BRR-001-v1.0 is now defined and unblocks this criterion for design purposes |
| **Functional requirement** | F-03 |

### Example Test Prompt AC-01-A — Standard tone (explicit)

**Input brief:**
```json
{
  "content_type": "blog",
  "product_or_topic": "Red Hat OpenShift",
  "target_audience": "IT decision maker",
  "key_messages": [
    "OpenShift reduces container deployment time",
    "OpenShift runs on any cloud or on-premises"
  ],
  "tone_override": "standard"
}
```

**Pass criteria for AC-01-A:** Brand reviewer scores draft using BRR-001-v1.0. Draft must score ≥ 3 on all five dimensions: D1 (concise, no filler), D2 (active voice preferred), D3 (matches `standard` register — professional and direct), D4 (no absolute claims or superlatives), D5 (vocabulary appropriate for IT decision maker). `metadata.tone_applied` in output is `"standard"`.

### Example Test Prompt AC-01-B — Executive tone (explicit)

**Input brief:**
```json
{
  "content_type": "email",
  "product_or_topic": "Red Hat Ansible Automation Platform",
  "target_audience": "C-suite executive",
  "key_messages": [
    "Automation reduces operational cost"
  ],
  "tone_override": "executive"
}
```

**Pass criteria for AC-01-B:** Brand reviewer scores draft using BRR-001-v1.0. D3 must score ≥ 3 confirming executive register (short declarative sentences, strategic framing, no technical jargon). D5 must score ≥ 3 confirming language calibrated for C-suite (business outcomes, not technical detail). All other dimensions ≥ 3. `metadata.tone_applied` in output is `"executive"`.

### Example Test Prompt AC-01-C — Default tone fallback (omitted `tone_override`)

**Input brief:**
```json
{
  "content_type": "landing_page",
  "product_or_topic": "Red Hat Enterprise Linux",
  "target_audience": "IT manager",
  "key_messages": [
    "RHEL provides a stable, supported platform for enterprise workloads"
  ]
}
```

**Pass criteria for AC-01-C:** `tone_override` is absent from the input brief. `metadata.tone_applied` in output must be `"standard"` — confirming the skill applies the default tone when no override is supplied. Brand reviewer scores draft using BRR-001-v1.0; D3 must score ≥ 3 for `standard` register (professional, direct, active voice preferred). All other dimensions ≥ 3. This prompt counts toward the ≥ 5 omitted-override drafts required in the 30-draft sample.

### Example Test Prompt AC-01-D — Conversational tone variant (explicit)

**Input brief:**
```json
{
  "content_type": "blog",
  "product_or_topic": "Red Hat OpenShift",
  "target_audience": "Developer",
  "key_messages": [
    "OpenShift makes it easier to deploy and manage containerised applications",
    "Developers can focus on writing code rather than managing infrastructure"
  ],
  "tone_override": "conversational"
}
```

**Pass criteria for AC-01-D:** `metadata.tone_applied` in output is `"conversational"`. Brand reviewer scores draft using BRR-001-v1.0. D3 must score ≥ 3 confirming conversational register: approachable and engaging language, varied sentence structure, rhetorical questions are acceptable, noticeably less formal than `standard` or `executive`. D4 must score ≥ 3 — conversational tone does not exempt the draft from the no-absolute-claims rule. D5 must score ≥ 3 confirming vocabulary appropriate for a developer audience (technical familiarity assumed, enterprise business language avoided). D1 and D2 ≥ 3.

---

## AC-02 — Banned Terms Absent

| Field | Value |
|---|---|
| **Criterion** | No banned terms appear in generated output |
| **Testable definition** | Automated scan of `draft` field in skill output using the banned terms list from `standards/terminology-list.md` Section 2. Zero matches across 100 test brief executions covering all content types. Scan uses case-insensitive **whole-word boundary matching** (not substring matching). Morphological variants explicitly listed in terminology-list.md Section 2 (e.g., "leveraging" as a variant of banned "leverage") are treated as matching the root banned term. For all confirmed banned terms, `action_taken` in `flagged_terms[]` **must be `"replaced"`** — the skill replaces the term in the draft before delivery. `"flagged_for_review"` is reserved exclusively for terms that are potential violations but are **not** confirmed banned terms (e.g., context-dependent terms or incorrect product name variants requiring human judgement); such terms may remain in the draft. This distinction is what makes the zero-banned-terms pass condition unambiguous: any term with `action_taken: "flagged_for_review"` is by definition not a confirmed banned term. |
| **Pass condition** | 0 banned term matches in all 100 test outputs; all `flagged_terms[]` entries for confirmed banned terms have `action_taken: "replaced"` |
| **Fail condition** | ≥ 1 confirmed banned term found in any draft; or any confirmed banned term has `action_taken: "flagged_for_review"` |
| **Test method** | Automated string scan against banned term list (case-insensitive, whole-word boundary); scripted test runner in `tests/acceptance/`; additionally assert `action_taken` value per flagged term type |
| **Functional requirement** | F-05 |

### Example Test Prompt AC-02-A (Stress test — brief containing terms that trigger banned alternatives)

**Input brief:**
```json
{
  "content_type": "solution_brief",
  "product_or_topic": "Red Hat Enterprise Linux",
  "target_audience": "DevOps engineer",
  "key_messages": [
    "RHEL provides a seamless and robust platform for mission-critical workloads",
    "RHEL is the industry-standard choice for enterprise Linux"
  ],
  "tone_override": "technical"
}
```

**Pass criteria for AC-02-A:** Output `draft` field contains neither "seamless", "robust", nor "industry-standard". The `terminology_audit.banned_terms_detected` array lists all three. The `flagged_terms` array provides approved replacements, each with `action_taken: "replaced"`. The draft uses approved alternatives (e.g., "consistent", "reliable", and the specific standard by name).

### Example Test Prompt AC-02-B (Normal brief — no banned terms expected)

**Input brief:**
```json
{
  "content_type": "social",
  "product_or_topic": "Red Hat Quay",
  "target_audience": "Platform engineer",
  "key_messages": [
    "Red Hat Quay provides a secure, enterprise-grade container registry"
  ]
}
```

**Pass criteria for AC-02-B:** Output `draft` contains no banned terms. `terminology_audit.flagged_terms` is an empty array. `terminology_audit.banned_terms_detected` is an empty array.

### Example Test Prompt AC-02-C (Morphological variant stress test)

**Input brief:**
```json
{
  "content_type": "blog",
  "product_or_topic": "Red Hat OpenShift",
  "target_audience": "Platform engineer",
  "key_messages": [
    "OpenShift empowers teams by leveraging Kubernetes to seamlessly orchestrate containers"
  ]
}
```

**Pass criteria for AC-02-C:** Output `draft` contains neither "empowers", "leveraging" (matched as a declared variant of banned root "leverage"), nor "seamlessly" (variant of "seamless"). `terminology_audit.banned_terms_detected` lists all three detected root terms or their variants. Each entry in `flagged_terms` has `action_taken: "replaced"` with a non-empty `suggested_replacement`.

---

## AC-03 — Approved Terminology Usage

| Field | Value |
|---|---|
| **Criterion** | Approved product names are used correctly in ≥ 95% of references |
| **Testable definition** | Automated scan of `draft` field for incorrect product name variants listed in `standards/terminology-list.md` Section 1. Across 100 test brief executions, ≥ 95% of product name references must use the approved form on first use, and acceptable abbreviations only after first use. **"First use" is defined as the first occurrence of the product name anywhere in the `draft` field, document-wide (not per section or per paragraph).** For briefs referencing multiple products, first-use tracking is independent per product — each product has its own first-use counter. Additionally, no single product name may fail first-use correctness in more than 2 test outputs out of all its occurrences across the 100-run corpus. |
| **Pass condition** | ≥ 95 of 100 product references use the approved form on first use; no single product name fails first-use correctness in more than 2 outputs |
| **Fail condition** | > 5% of product name first-use references use an incorrect variant; or any single product name fails in more than 2 outputs |
| **Test method** | Automated scan for incorrect variants listed in terminology-list.md Section 1; scripted test runner; per-product failure counter tracked separately |
| **Functional requirement** | F-05 |

### Example Test Prompt AC-03-A

**Input brief:**
```json
{
  "content_type": "landing_page",
  "product_or_topic": "Red Hat OpenShift Container Platform",
  "target_audience": "IT director",
  "key_messages": [
    "OCP simplifies Kubernetes management at enterprise scale"
  ]
}
```

**Pass criteria for AC-03-A:** The first reference to the product in the draft (document-wide, regardless of section) uses "Red Hat OpenShift Container Platform" (not "OCP" or "OpenShift Container Platform" alone). Subsequent references may use "OpenShift" or "OCP" where appropriate.

### Example Test Prompt AC-03-B

**Input brief:**
```json
{
  "content_type": "blog",
  "product_or_topic": "Red Hat build of Quarkus",
  "target_audience": "Java developer",
  "key_messages": [
    "Quarkus enables fast startup times for cloud-native applications"
  ]
}
```

**Pass criteria for AC-03-B:** First reference (document-wide) uses "Red Hat build of Quarkus" (with lowercase "build of"). Subsequent references may use "Quarkus". The draft does not use "Red Hat Quarkus" or "RH Quarkus".

### Example Test Prompt AC-03-C (Multi-product brief — independent first-use tracking)

**Input brief:**
```json
{
  "content_type": "solution_brief",
  "product_or_topic": "Red Hat OpenShift Container Platform and Red Hat Ansible Automation Platform",
  "target_audience": "Platform architect",
  "key_messages": [
    "OCP and AAP together provide end-to-end automation from infrastructure to application deployment"
  ]
}
```

**Pass criteria for AC-03-C:** The first document-wide reference to each product uses its full approved name: "Red Hat OpenShift Container Platform" and "Red Hat Ansible Automation Platform". Subsequent references may use "OpenShift" and "Ansible Automation Platform" respectively. The draft does not use bare "OCP" or "AAP" on first mention of either product. First-use compliance is assessed independently for each product — a failure for one does not excuse the other.

---

## AC-04 — Routing Correctness

| Field | Value |
|---|---|
| **Criterion** | The correct template and length constraints are applied for each content type |
| **Testable definition** | 50 test briefs (10 per content type) submitted. For each: (a) the structural template for the specified content type is applied, (b) the draft word/character count falls within the default range (or override range if `word_count_target` provided), (c) format-specific constraints are respected (e.g., email subject line ≤ 60 chars, social posts ≤ 280 chars each). All 50 must pass. |
| **Pass condition** | All 50 test briefs produce output that matches the expected template structure and length range. For briefs using `word_count_target` override, length is assessed against ±10% of the target value, not the default range. Social posts are always assessed against the 280-char per-post limit; providing `word_count_target` in a social brief must produce a validation error (see AC-05 and note below). |
| **Fail condition** | Any of the 50 test outputs fails template structure check or length check |
| **Test method** | Automated structural check (section count, heading structure, character/word count); scripted test runner |
| **Functional requirement** | F-02, F-04 |
| **Note on social + word_count_target** | `word_count_target` is incompatible with the `social` content type, which uses character-count constraints (not word count) by definition. A brief with `content_type: "social"` and any `word_count_target` value must be rejected at F-01 validation with `"field": "word_count_target"` and `"code": "field_not_applicable"`. This is tested explicitly in AC-05 (see AC-05-F). |

### Example Test Prompt AC-04-A (blog routing)

**Input brief:**
```json
{
  "content_type": "blog",
  "product_or_topic": "Red Hat Insights",
  "target_audience": "System administrator",
  "key_messages": ["Insights provides predictive analytics for RHEL environments"]
}
```

**Pass criteria for AC-04-A:** `draft` word count is 600–1200. Draft contains an introduction, 3–5 body sections with H2 headings, and a conclusion. No bullet lists in intro or conclusion.

### Example Test Prompt AC-04-B (social routing)

**Input brief:**
```json
{
  "content_type": "social",
  "product_or_topic": "Red Hat Satellite",
  "target_audience": "IT operations",
  "key_messages": ["Satellite automates patch management across hybrid environments"]
}
```

**Pass criteria for AC-04-B:** `draft` contains exactly 3 standalone social posts, each ≤ 280 characters. Each post can be published independently without context from the others.

### Example Test Prompt AC-04-C (word_count_target override)

**Input brief:**
```json
{
  "content_type": "solution_brief",
  "product_or_topic": "Red Hat Advanced Cluster Management",
  "target_audience": "Platform architect",
  "key_messages": ["RHACM provides unified management for multi-cluster Kubernetes"],
  "word_count_target": 600
}
```

**Pass criteria for AC-04-C:** `draft` word count is 550–650 (±10% tolerance on override target). `metadata.word_count_target_override` is `600`.

### Example Test Prompt AC-04-D (email routing)

**Input brief:**
```json
{
  "content_type": "email",
  "product_or_topic": "Red Hat Satellite",
  "target_audience": "IT operations manager",
  "key_messages": [
    "Satellite automates patch compliance across hybrid infrastructure"
  ],
  "call_to_action": "Schedule a demo"
}
```

**Pass criteria for AC-04-D:** Output `draft` contains: (a) a subject line ≤ 60 characters, (b) a pre-header ≤ 90 characters, (c) body text, (d) a single CTA that uses or incorporates the provided `call_to_action` text "Schedule a demo". Total word count is 150–300. No second CTA is present.

### Example Test Prompt AC-04-E (landing_page routing)

**Input brief:**
```json
{
  "content_type": "landing_page",
  "product_or_topic": "Red Hat Enterprise Linux",
  "target_audience": "IT manager",
  "key_messages": [
    "RHEL delivers a consistent, supported foundation for enterprise workloads",
    "RHEL runs across bare metal, virtual, cloud, and edge environments"
  ],
  "call_to_action": "Try RHEL free for 60 days"
}
```

**Pass criteria for AC-04-E:** Output `draft` contains: (a) a headline section with ≤ 10 words, (b) a sub-headline, (c) a body section with no more than 3 paragraphs, (d) a CTA incorporating "Try RHEL free for 60 days". Total word count is 100–250. The draft does not exceed 3 body paragraphs.

---

## AC-05 — Schema Validation

| Field | Value |
|---|---|
| **Criterion** | Malformed input briefs are rejected with actionable error messages |
| **Testable definition** | 20 deliberately malformed input briefs submitted (4 per failure category across 5 categories: missing required field, invalid enum value, out-of-range integer, wrong type, empty required array — 5 × 4 = 20 total). All 20 must be rejected with a structured error response identifying the specific invalid field, the error code, and an actionable fix instruction. Additionally, the corpus must include **at least one brief with simultaneous failures in two fields** to verify multi-error behaviour. For multi-error briefs: `validation_errors[]` must contain one entry per invalid field; the skill must not abort after the first error; no valid fields may be incorrectly flagged. |
| **Pass condition** | All 20 malformed briefs produce a structured error response with correct field identification and fix instruction; multi-error briefs produce one `validation_errors[]` entry per invalid field with no false positives |
| **Fail condition** | Any malformed brief produces a content draft instead of an error; any error response does not identify the specific failing field; multi-error brief produces only the first error (early-abort behaviour); any valid field is incorrectly included in `validation_errors[]` |
| **Test method** | Automated; submit malformed briefs and assert response contains `error: "input_validation_failure"` with correct `validation_errors[].field`; for multi-error brief assert `validation_errors.length === expected_count` |
| **Functional requirement** | F-01 |

### Example Test Prompt AC-05-A (missing required field)

**Input brief:**
```json
{
  "product_or_topic": "Red Hat OpenShift",
  "target_audience": "Developer",
  "key_messages": ["OpenShift simplifies container orchestration"]
}
```

**Pass criteria for AC-05-A:** Response is `{"error": "input_validation_failure", ...}`. `validation_errors` array contains one entry with `"field": "content_type"`, `"code": "required_field_missing"`, and a message instructing the user to provide one of the five valid values.

### Example Test Prompt AC-05-B (invalid enum value)

**Input brief:**
```json
{
  "content_type": "whitepaper",
  "product_or_topic": "Red Hat Enterprise Linux",
  "target_audience": "IT manager",
  "key_messages": ["RHEL powers enterprise workloads"]
}
```

**Pass criteria for AC-05-B:** Response is `{"error": "input_validation_failure", ...}`. `validation_errors` array contains one entry with `"field": "content_type"`, `"code": "invalid_enum_value"`, `"valid_values": ["blog", "solution_brief", "email", "landing_page", "social"]`.

### Example Test Prompt AC-05-C (empty required array)

**Input brief:**
```json
{
  "content_type": "email",
  "product_or_topic": "Red Hat Quay",
  "target_audience": "DevOps engineer",
  "key_messages": []
}
```

**Pass criteria for AC-05-C:** Response is `{"error": "input_validation_failure", ...}`. `validation_errors` contains entry with `"field": "key_messages"`, `"code": "value_out_of_range"` or `"min_items_not_met"`, and message stating minimum 1 item required.

### Example Test Prompt AC-05-D (wrong type — key_messages as string instead of array)

**Input brief:**
```json
{
  "content_type": "blog",
  "product_or_topic": "Red Hat Enterprise Linux",
  "target_audience": "Developer",
  "key_messages": "RHEL is a stable platform"
}
```

**Pass criteria for AC-05-D:** Response is `{"error": "input_validation_failure", ...}`. `validation_errors` contains one entry with `"field": "key_messages"`, `"code": "wrong_type"`, and a message stating that `key_messages` must be an array of strings, not a single string. No content draft is returned.

### Example Test Prompt AC-05-E (simultaneous multi-field failure — invalid enum + empty array)

**Input brief:**
```json
{
  "content_type": "whitepaper",
  "product_or_topic": "Red Hat OpenShift",
  "target_audience": "Developer",
  "key_messages": []
}
```

**Pass criteria for AC-05-E:** `validation_errors` contains **exactly two** entries — one for `content_type` (`"code": "invalid_enum_value"`, listing valid values) and one for `key_messages` (`"code": "min_items_not_met"` or equivalent, stating minimum 1 item required). Both errors are present in a single response; the skill does not abort after detecting the first error. `validation_errors.length === 2`. Fields `product_or_topic` and `target_audience` (which are valid) must not appear in `validation_errors`.

### Example Test Prompt AC-05-F (social brief with disallowed word_count_target)

**Input brief:**
```json
{
  "content_type": "social",
  "product_or_topic": "Red Hat Quay",
  "target_audience": "DevOps engineer",
  "key_messages": ["Quay provides a secure container registry for enterprise teams"],
  "word_count_target": 300
}
```

**Pass criteria for AC-05-F:** Response is `{"error": "input_validation_failure", ...}`. `validation_errors` contains one entry with `"field": "word_count_target"`, `"code": "field_not_applicable"`, and a message stating that `word_count_target` is not valid for `social` content type because social posts use per-post character limits (≤ 280 chars), not word count. No content draft is returned.

---

## AC-06 — Terminology Audit Block Accuracy

| Field | Value |
|---|---|
| **Criterion** | The terminology audit block is present and accurate for all outputs — including clean briefs with no banned terms |
| **Testable definition** | 30 test briefs with input key_messages containing ≥ 1 banned term or incorrect product name variant, **plus 5 clean briefs where key_messages contain no banned terms**. For briefs with banned terms: (a) `terminology_audit` block is present, (b) every banned term found in the brief's messages appears in `banned_terms_detected`, (c) `flagged_terms` includes an entry for each with a non-empty `suggested_replacement`, (d) the final `draft` does not contain the banned term. For clean briefs: `terminology_audit` block is present, `flagged_terms` is `[]`, and `banned_terms_detected` is `[]` — the block must not be omitted. Additionally, one test must be executed after a simulated TERM-YYYY-QN version increment (updating terminology-list.md to a new version stamp with no other skill changes) to confirm that `metadata.terminology_version` in output reflects the new version. |
| **Pass condition** | All 30 flagged-term briefs: complete, accurate audit block and draft clean of banned terms. All 5 clean briefs: audit block present with empty arrays. Version-update simulation: output reflects updated version stamp without skill logic changes. |
| **Fail condition** | Any test output is missing the audit block; any detected banned term absent from audit block; any banned term remains in the draft; clean brief returns omitted or null audit block; version-update simulation returns old version stamp |
| **Test method** | Automated; cross-reference known banned terms in key_messages against audit block output; string scan of draft; assert `terminology_audit` key present in all 35 outputs; for clean briefs assert `flagged_terms === []` and `banned_terms_detected === []`; version-update simulation asserts `metadata.terminology_version` matches updated stamp |
| **Functional requirement** | F-05, F-07 |
| **Versioning relevance** | `metadata.terminology_version` in output must match the embedded TERM-YYYY-QN stamp, allowing QA to confirm which terminology version was applied. The version-update simulation (AC-06-D) verifies the decoupling principle from Design Spec Section 6.4. |

### Example Test Prompt AC-06-A

**Input brief:**
```json
{
  "content_type": "solution_brief",
  "product_or_topic": "Red Hat OpenShift",
  "target_audience": "IT director",
  "key_messages": [
    "OpenShift is a game-changing platform that empowers your teams to leverage container orchestration",
    "It eliminates infrastructure complexity and ensures always-on availability"
  ]
}
```

**Pass criteria for AC-06-A:**
- `terminology_audit.banned_terms_detected` includes: `"game-changing"`, `"empowers"`, `"leverage"`, `"eliminates"` (as absolute), `"always"` (as absolute claim)
- `terminology_audit.flagged_terms` has an entry for each with `suggested_replacement` populated
- `draft` field contains none of the banned terms listed above
- `metadata.terminology_version` is `"TERM-2026-Q2"`

### Example Test Prompt AC-06-B (version stamp check)

**Input brief:**
```json
{
  "content_type": "blog",
  "product_or_topic": "Red Hat Ansible Automation Platform",
  "target_audience": "Operations engineer",
  "key_messages": [
    "Ansible Automation Platform provides robust, seamless automation"
  ]
}
```

**Pass criteria for AC-06-B:**
- `terminology_audit.banned_terms_detected` includes `"robust"` and `"seamless"`
- `draft` does not contain "robust" or "seamless"
- `metadata.terminology_version` is `"TERM-2026-Q2"` — confirming the correct list version was active
- QA test logs this version stamp to create a traceable record of which terminology version was tested

### Example Test Prompt AC-06-C (clean brief — audit block present with empty arrays)

**Input brief:**
```json
{
  "content_type": "landing_page",
  "product_or_topic": "Red Hat OpenShift",
  "target_audience": "IT director",
  "key_messages": [
    "Red Hat OpenShift accelerates application delivery with a consistent Kubernetes platform"
  ]
}
```

**Pass criteria for AC-06-C:**
- `terminology_audit` block **is present** in the output (not omitted, not null)
- `terminology_audit.flagged_terms` is `[]` (empty array, not absent)
- `terminology_audit.banned_terms_detected` is `[]` (empty array, not absent)
- `draft` does not contain any banned terms

### Example Test Prompt AC-06-D (version update simulation — post-increment check)

_Pre-condition: Update `standards/terminology-list.md` version stamp from `TERM-2026-Q2` to `TERM-2026-Q3` (simulating a quarterly update). No changes to `skill.md`, `schema/`, or `templates/`._

**Input brief:**
```json
{
  "content_type": "blog",
  "product_or_topic": "Red Hat Ansible Automation Platform",
  "target_audience": "Operations engineer",
  "key_messages": [
    "Ansible Automation Platform provides robust, seamless automation"
  ]
}
```

**Pass criteria for AC-06-D:**
- `metadata.terminology_version` is `"TERM-2026-Q3"` (the new version stamp, not `"TERM-2026-Q2"`)
- `terminology_audit.banned_terms_detected` includes `"robust"` and `"seamless"`
- `draft` contains neither "robust" nor "seamless"
- This confirms the decoupling principle (Design Spec Section 6.4): the terminology standards update is reflected in output without any changes to skill logic, routing, schema, or templates

---

## Summary Matrix

| ID | Criterion | Pass Threshold | Method | F-Req | Blocked? |
|---|---|---|---|---|---|
| AC-01 | Brand voice compliance | ≥ 27/30 drafts compliant using BRR-001-v1.0; all 4 tone variants ≥ 2 drafts | Blind human review (rubric BRR-001-v1.0) | F-03 | Partial — TASK-BT-001 pending; rubric now defined |
| AC-02 | Banned terms absent | 0 banned terms in 100 outputs; all banned-term entries have `action_taken: "replaced"` | Automated scan (whole-word, case-insensitive, morphological variants) | F-05 | No |
| AC-03 | Approved terminology usage | ≥ 95% correct on first use (document-wide) in 100 outputs; no single product > 2 failures | Automated scan with per-product failure counter | F-05 | No |
| AC-04 | Routing correctness | 50/50 test briefs pass template + length check; overrides at ±10%; social+word_count_target rejected | Automated structural check | F-02, F-04 | No |
| AC-05 | Schema validation | 20/20 malformed briefs rejected with field-level errors; multi-error briefs return all errors (no early-abort) | Automated error assertion | F-01 | No |
| AC-06 | Terminology audit block accuracy | 30/30 flagged briefs: audit complete, draft clean; 5/5 clean briefs: audit block present with empty arrays; version-update simulation confirms new stamp | Automated cross-reference + scan + version assertion | F-05, F-07 | No |

---

_This acceptance criteria matrix is finalised for the design phase (v0.2 incorporates QA-REV-RHCW-001 findings for AC-02 through AC-06). QA test cases will be scaffolded in `tests/acceptance/` during the implementation sprint._

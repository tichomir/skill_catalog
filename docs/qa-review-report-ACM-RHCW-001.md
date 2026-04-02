# QA Review Report: Acceptance Criteria Matrix ACM-RHCW-001
_Document ID: QA-REV-RHCW-001 | Version: 0.1 | Status: Delivered — Awaiting Incorporation_
_Created: 2026-04-02 | Reviewer: QA Engineer Persona | References: ACM-RHCW-001 v0.1, DS-RHCW-001 v0.1_

---

## Purpose

This report is a QA review of the acceptance criteria matrix (ACM-RHCW-001 v0.1) produced in task-003. It assesses each of AC-01 through AC-06 for:

1. **Testability** — can the criterion be verified with a concrete, repeatable prompt or script?
2. **Unambiguous pass/fail** — is there a single measurable condition that determines pass or fail?
3. **Edge case coverage** — is at least one edge case addressed with a test prompt?

Each criterion receives a status of **APPROVED**, **NEEDS REVISION**, or **BLOCKED**.

Findings are delivered to prompt_engineer for incorporation before the design spec is finalised.

---

## Executive Summary

| ID | Criterion | Status | Issues Found |
|---|---|---|---|
| AC-01 | Brand voice compliance | BLOCKED | Rubric undefined; edge cases missing for default tone and conversational variant |
| AC-02 | Banned terms absent | NEEDS REVISION | No edge cases for case variants, partial-word matches, or quoted source material |
| AC-03 | Approved terminology usage | NEEDS REVISION | "First use" detection is ambiguous; no multi-product test; threshold granularity gap |
| AC-04 | Routing correctness | NEEDS REVISION | Missing email/landing_page examples; social word-count override conflict undefined; tolerance not in main pass condition |
| AC-05 | Schema validation | NEEDS REVISION | Missing "wrong type" example prompt; multi-error behaviour unspecified; category count wording ambiguous |
| AC-06 | Terminology audit block accuracy | NEEDS REVISION | Standards update scenario not tested end-to-end; clean-brief audit block not explicitly tested |

---

## AC-01 — Brand Voice Compliance

**Current status: BLOCKED**

### Assessment

The numeric threshold (≥ 27 of 30 drafts, 90%) is well-chosen and the blind review method is sound. However, two issues prevent this criterion from being fully testable.

**Issue 1 — Critical blocker: scoring rubric is undefined.**
The testable definition states "blind evaluation using the brand scoring rubric (to be defined by Brand Experience team)." Without the rubric, reviewers have no consistent basis for rating compliance. A criterion whose pass/fail condition depends on an undefined instrument cannot be executed. This is not just a content blocker (TASK-BT-001) — it is a test methodology blocker. The criterion should not be marked "Finalised" until the rubric exists or is at minimum committed to a placeholder with dimensions listed.

**Issue 2 — Missing edge cases for default and conversational tone variants.**
Both example prompts (AC-01-A and AC-01-B) use explicitly specified `tone_override` values (`standard` and `executive`). No test prompt covers:
- The `conversational` tone variant
- The case where `tone_override` is omitted (the skill should default to `standard` — this default behaviour is not tested)

### Suggested revision to testable definition

> ≥ 90% of generated drafts rated "compliant" by a trained brand reviewer in a blind evaluation using the brand scoring rubric (DS-RHCW-BRR-001, to be delivered by Brand Experience team no later than end of design sprint). Sample size: minimum 30 drafts distributed across all 5 content types, all 4 tone variants (≥ 1 draft per tone variant), and at least 5 drafts where `tone_override` is omitted (testing default `standard` fallback).

### Additional recommended edge-case test prompt

**AC-01-C (omitted tone_override — default fallback test)**

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

**Pass criteria:** Brand reviewer confirms draft is written in `standard` tone (professional, direct, active voice preferred) — i.e., the skill correctly applied the default when no `tone_override` was supplied.

---

## AC-02 — Banned Terms Absent

**Current status: NEEDS REVISION**

### Assessment

The automated scan method is well-defined, the 100-output sample is appropriate, and the pass condition (zero matches) is unambiguous. The two example prompts are well-constructed. Three edge cases are not covered.

**Issue 1 — Partial-word / morphological variants not addressed.**
The test method specifies "case-insensitive" string scan but does not address morphological variants. If "leverage" is banned, the scan must also catch "leveraging", "leveraged", "leverages". The criterion is silent on whether the scanner uses whole-word matching or substring matching. If whole-word, "leveraging" would pass the scan but still violates the intent. This needs an explicit decision.

**Issue 2 — Banned terms appearing in quoted or attributed content.**
No test covers the scenario where a key message explicitly quotes a third-party source that uses a banned term (e.g., `"key_messages": ["Analyst firm X calls this a 'game-changing' approach"]`). The skill needs a defined policy: either (a) replace the term even in a quote, (b) flag for review instead of replacing, or (c) exempt quoted material. The current criterion and audit block structure include an `action_taken` field with value `"replaced | flagged_for_review"` — but AC-02's pass condition requires zero banned terms in output, which conflicts with `"flagged_for_review"` as a valid action. This is a logical inconsistency.

**Issue 3 — Mixed-case variants in the example test prompts.**
AC-02-A uses lowercase banned terms in `key_messages`. A separate test prompt with mixed-case variants (e.g., "Seamless", "ROBUST") would confirm the case-insensitive claim.

### Suggested revision to testable definition — add:

> The automated scan uses case-insensitive whole-word boundary matching (not substring). Morphological variants (e.g., "leveraging" for banned "leverage") are treated as matching if listed as variants in terminology-list.md Section 2. Quoted material in key_messages is not exempt from banned-term replacement; any term replaced in a quote must be noted in `flagged_terms[].action_taken` as `"replaced"`.

### Additional recommended edge-case test prompt

**AC-02-C (morphological variant stress test)**

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

**Pass criteria:** Output `draft` contains neither "empowers", "leveraging" (matched as variant of "leverage"), nor "seamlessly". `banned_terms_detected` lists all three root terms or their detected variants. `flagged_terms` provides replacements for each.

---

## AC-03 — Approved Terminology Usage

**Current status: NEEDS REVISION**

### Assessment

The ≥ 95% threshold and automated scan method are clear. Both example prompts are well-chosen and illustrate a nuanced rule (full name on first use, abbreviations thereafter). Three gaps remain.

**Issue 1 — "First use" is ambiguous in automated scanning.**
The testable definition requires correct product name "on first use." For an automated scanner, this requires a precisely defined rule: is "first use" the first occurrence in the entire document, or the first occurrence in each section or paragraph? For a blog with five H2 sections, should the full product name reappear on first use in each section? The criterion does not specify. Without this definition, different reviewers or scanner implementations will produce different results.

**Issue 2 — No test for multiple products in a single brief.**
Both AC-03 test prompts feature a single product. A brief referencing two products (e.g., Red Hat OpenShift Container Platform and Red Hat Ansible Automation Platform) should be tested to confirm that "first use" is tracked independently per product, not as a shared counter.

**Issue 3 — Threshold granularity does not distinguish systematic vs. incidental failure.**
The 5% allowance (5 of 100) could mask a systematic failure: if all 5 failures are for the same product name, that is a product-specific bug, not a 5% noise floor. The criterion should add a per-product floor (e.g., no single product may fail more than 2 of its total references).

### Suggested revision to testable definition — add:

> "First use" is defined as the first occurrence of the product name anywhere in the `draft` field, document-wide (not per section). For briefs referencing multiple products, first-use tracking is independent per product. No single product name may fail first-use correctness in more than 2 test outputs out of its total occurrences across all 100 runs.

### Additional recommended edge-case test prompt

**AC-03-C (multi-product brief)**

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

**Pass criteria:** First reference to each product uses its full approved name ("Red Hat OpenShift Container Platform", "Red Hat Ansible Automation Platform"). Subsequent references may use "OpenShift" and "Ansible Automation Platform" respectively. The draft does not use bare "OCP" or "AAP" on first mention.

---

## AC-04 — Routing Correctness

**Current status: NEEDS REVISION**

### Assessment

The 50-brief sample size with 10 per content type is appropriate. The three example prompts (AC-04-A, AC-04-B, AC-04-C) cover blog, social, and a word-count override. Three gaps need addressing.

**Issue 1 — No example test prompts for email or landing_page content types.**
With 10 test briefs per content type required, email and landing_page each have structural constraints (email: subject ≤ 60 chars, pre-header ≤ 90 chars; landing_page: headline ≤ 10 words, max 3 body paragraphs). Without example prompts, the prompt_engineer cannot anchor the test case structure for these types.

**Issue 2 — `word_count_target` override for social posts is undefined.**
The social handler produces character-limited posts (≤ 280 chars each), not word-counted drafts. If a caller provides `word_count_target: 200` in a social brief, the routing logic must define the expected behaviour: (a) reject as invalid for social type, (b) silently ignore the override, or (c) apply it as a per-post word guideline. The criterion is silent on this. This is a routing logic gap that, if untested, will create undefined behaviour.

**Issue 3 — Tolerance (±10%) is not stated in the main pass condition.**
AC-04-C correctly uses ±10% tolerance for `word_count_target` overrides. However, the main pass condition table says "falls within the default range" — implying exact range adherence — without noting that overrides use ±10%. A QA engineer reading only the pass condition row would not know to apply tolerance for override cases.

### Suggested revision to pass condition:

> All 50 test briefs produce output that matches the expected template structure and length range. For briefs using `word_count_target` override, length is assessed against ±10% of the target value. Social posts are always assessed against the 280-char per-post limit regardless of any `word_count_target` value supplied (which must produce a validation error if present in a social brief — see AC-05).

### Additional recommended edge-case test prompts

**AC-04-D (email routing)**

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

**Pass criteria:** Output draft contains a subject line ≤ 60 chars, a pre-header ≤ 90 chars, body text, and a single CTA using the provided `call_to_action` text. Word count is 150–300.

**AC-04-E (social brief with disallowed word_count_target)**

```json
{
  "content_type": "social",
  "product_or_topic": "Red Hat Quay",
  "target_audience": "DevOps engineer",
  "key_messages": ["Quay provides a secure container registry for enterprise teams"],
  "word_count_target": 300
}
```

**Pass criteria:** If the skill rejects `word_count_target` for social type — response is `{"error": "input_validation_failure", ...}` with `"field": "word_count_target"` and a message stating this field is not applicable for `social` content type. If the skill silently ignores it — draft still contains exactly 3 posts each ≤ 280 chars, and `metadata.word_count_target_override` is null.
_(Note: the expected behaviour must be defined in the design spec before this test can have a deterministic pass condition.)_

---

## AC-05 — Schema Validation

**Current status: NEEDS REVISION**

### Assessment

The 20-brief corpus (4 per failure category), clear automated test method, and the three example prompts are strong. Two issues require attention.

**Issue 1 — No example test prompt for "wrong type" failure category.**
The five failure categories listed are: missing required field, invalid enum value, out-of-range integer, wrong type, empty required array. Only three of the five have example prompts (AC-05-A through AC-05-C cover missing required field, invalid enum, and empty array). "Wrong type" (e.g., `key_messages` supplied as a string instead of an array, or `word_count_target` supplied as a string) has no example prompt. This is the category most likely to produce inconsistent behaviour depending on the parser.

**Issue 2 — Multi-field validation failure behaviour is unspecified.**
The criterion tests one failure at a time, but does not specify whether the skill returns all validation errors in a single response or halts at the first. If a brief has both a missing `content_type` and an invalid `target_audience` type, are both listed in `validation_errors[]`? This matters for QA scripting: a test expecting `validation_errors.length === 1` will fail if the implementation returns all errors. The design spec (Section 5.2) shows `validation_errors` as an array, implying multiple errors can coexist, but AC-05 does not test this.

**Issue 3 — Wording ambiguity in failure category count.**
The testable definition states "4 per failure category: missing required field, invalid enum value, out-of-range integer, wrong type, empty required array" — but then gives the total as 20. 5 categories × 4 = 20, which is correct, but the sentence structure reads as if there are 4 categories. Minor, but could cause confusion during test case authoring.

### Suggested revision to testable definition — add:

> Test corpus includes at least one brief with simultaneous failures in two fields. Pass condition for multi-error briefs: `validation_errors[]` contains one entry per invalid field; no valid fields are incorrectly flagged.

### Additional recommended edge-case test prompts

**AC-05-D (wrong type — key_messages as string)**

```json
{
  "content_type": "blog",
  "product_or_topic": "Red Hat Enterprise Linux",
  "target_audience": "Developer",
  "key_messages": "RHEL is a stable platform"
}
```

**Pass criteria:** Response is `{"error": "input_validation_failure", ...}`. `validation_errors` contains entry with `"field": "key_messages"`, `"code": "wrong_type"`, and message stating `key_messages` must be an array of strings.

**AC-05-E (simultaneous multi-field failure)**

```json
{
  "content_type": "whitepaper",
  "product_or_topic": "Red Hat OpenShift",
  "target_audience": "Developer",
  "key_messages": []
}
```

**Pass criteria:** `validation_errors` contains exactly two entries — one for `content_type` (invalid enum) and one for `key_messages` (empty array). Both fields are identified; the response does not abort after the first error.

---

## AC-06 — Terminology Audit Block Accuracy

**Current status: NEEDS REVISION**

### Assessment

The version stamp check (AC-06-B) is a strong addition and is the right mechanism for tracing which terminology list was active. The 30-test-brief corpus and automated cross-reference method are appropriate. Two gaps remain.

**Issue 1 — Standards update scenario is not tested end-to-end.**
The sprint goal explicitly lists AC-06 as needing to satisfy the "standards update scenario." AC-06-B tests that the version stamp matches TERM-2026-Q2 — but no test covers what happens when the terminology list is updated to TERM-2026-Q3. The test question is: does the skill pick up the new version and output `"terminology_version": "TERM-2026-Q3"` after a list update, without any changes to `skill.md` or routing logic? Without this test, the decoupling principle (Design Spec Section 6.4) is asserted but not verified.

**Issue 2 — Clean brief (no banned terms) audit block not explicitly tested.**
The design spec states "If no flagged terms are found, the `flagged_terms` array is empty and `banned_terms_detected` is empty." AC-06 only tests briefs with ≥ 1 banned term in key_messages. It does not include a test prompt where key_messages contain no banned terms and the skill must return an audit block with empty arrays (rather than omitting the block). An omitted audit block would cause AC-06's pass condition to fail silently on clean briefs.

### Suggested revision to testable definition — add:

> Test corpus includes 5 briefs where `key_messages` contain no banned terms. For these: `terminology_audit` block must be present, `flagged_terms` must be an empty array `[]`, and `banned_terms_detected` must be an empty array `[]`. The block must not be omitted. Additionally, one test must be executed after a simulated TERM-YYYY-QN version increment (updating terminology-list.md to a new version stamp) to confirm that `metadata.terminology_version` in output reflects the new version without changes to skill logic files.

### Additional recommended edge-case test prompts

**AC-06-C (clean brief — audit block present with empty arrays)**

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

**Pass criteria:** `terminology_audit` block is present in output. `terminology_audit.flagged_terms` is `[]`. `terminology_audit.banned_terms_detected` is `[]`. The draft does not contain any banned terms.

**AC-06-D (version update simulation — post-increment check)**

_Pre-condition: Update `standards/terminology-list.md` version stamp from `TERM-2026-Q2` to `TERM-2026-Q3` (simulating a quarterly update). No changes to skill.md, schema/, or templates/._

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

**Pass criteria:** `metadata.terminology_version` is `"TERM-2026-Q3"` (the new version). `terminology_audit.banned_terms_detected` includes `"robust"` and `"seamless"`. Draft contains neither. This confirms the decoupling principle: standards update is reflected in output without touching skill logic.

---

## Summary of Findings

### Criteria approved as-is
None. All six criteria require revision or are blocked.

### Criteria requiring revision

| ID | Required change | Priority |
|---|---|---|
| AC-01 | Define rubric dependency as a pre-condition; add tone default + conversational test prompts | HIGH (blocker risk) |
| AC-02 | Clarify morphological variant matching policy; resolve `flagged_for_review` vs. zero-banned-terms conflict; add mixed-case test prompt | HIGH (logical inconsistency) |
| AC-03 | Define "first use" scope (document-wide vs. per-section); add multi-product test prompt; add per-product failure floor | MEDIUM |
| AC-04 | Add email and landing_page example prompts; define social + word_count_target conflict; add tolerance to main pass condition | MEDIUM |
| AC-05 | Add "wrong type" example prompt; specify multi-field error behaviour; fix category count wording | MEDIUM |
| AC-06 | Add clean-brief test (empty audit arrays); add version-update simulation test | MEDIUM |

### Criteria blocked

| ID | Blocker | Resolution needed before |
|---|---|---|
| AC-01 | Brand scoring rubric not yet defined by Brand Experience team | Design spec finalisation; failing this, mark criterion as "blocked — untestable" in the summary matrix |

### Coverage gaps not addressed by current AC matrix

1. **F-06 (Messaging Alignment Assessment) has no acceptance criterion.** The functional requirement is defined in DS-RHCW-001 F-06 and supports US-02, but no AC tests it. Suggested addition: AC-07 covering presence of `messaging_alignment` block when `messaging_pillars` is provided, and absence when omitted.

2. **Concurrent / idempotency behaviour is untested.** No criterion checks that two identical input briefs produce structurally equivalent outputs (same structure, same terminology audit results). Non-determinism is expected in draft content (LLM), but audit blocks and metadata should be deterministic for identical inputs.

3. **`call_to_action` field incorporation is not explicitly tested.** AC-04 tests structural template and length; F-03 specifies that `call_to_action` must be embedded at the end of the piece when provided. No acceptance criterion validates this.

---

## Recommended Actions for prompt_engineer

1. Resolve the scoring rubric dependency for AC-01 before marking it testable. Add rubric document reference to the testable definition.
2. Add the suggested edge-case test prompts (AC-01-C, AC-02-C, AC-03-C, AC-04-D, AC-04-E, AC-05-D, AC-05-E, AC-06-C, AC-06-D) to the acceptance criteria matrix.
3. Resolve the logical inconsistency in AC-02 between zero-banned-terms output requirement and `flagged_for_review` action value.
4. Define "first use" scope in AC-03.
5. Define expected behaviour for `word_count_target` in social briefs (AC-04).
6. Specify multi-field validation error behaviour in AC-05.
7. Consider adding AC-07 for F-06 messaging alignment assessment.
8. Consider adding acceptance criteria for `call_to_action` incorporation.

---

_QA review complete. This report should be reviewed by prompt_engineer and incorporated into ACM-RHCW-001 v0.2 before the design spec is finalised._

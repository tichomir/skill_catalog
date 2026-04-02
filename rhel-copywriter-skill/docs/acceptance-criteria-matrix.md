# Acceptance Criteria Matrix: Red Hat Copywriter Skill
_Document ID: ACM-RHCW-001 | Version: 0.1 | Status: Finalised_
_Created: 2026-04-02 | Owner: Skill Owner (R. Patel) | PRD: PRD-RHCW-001 v0.1_

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
| **Testable definition** | ≥ 90% of generated drafts rated "compliant" by a trained brand reviewer in a blind evaluation using the brand scoring rubric (to be defined by Brand Experience team). Sample size: minimum 30 drafts across all 5 content types and all 4 tone variants. |
| **Pass condition** | ≥ 27 of 30 drafts rated compliant (90%) |
| **Fail condition** | < 27 of 30 drafts rated compliant |
| **Test method** | Blind human review by PMM or Brand Experience team member; reviewer sees draft only, not the input brief |
| **Blocker** | Requires `brand-tone-reference.md` content (TASK-BT-001) before testable |
| **Functional requirement** | F-03 |

### Example Test Prompt AC-01-A

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

**Pass criteria for AC-01-A:** Brand reviewer rates the generated blog draft as using Red Hat voice (professional, direct, active voice preferred, avoids superlatives), scoring ≥ 3 of 5 on each rubric dimension.

### Example Test Prompt AC-01-B

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

**Pass criteria for AC-01-B:** Brand reviewer confirms executive tone variant is applied — shorter sentences, strategic framing, no technical jargon — while remaining within Red Hat brand guidelines.

---

## AC-02 — Banned Terms Absent

| Field | Value |
|---|---|
| **Criterion** | No banned terms appear in generated output |
| **Testable definition** | Automated scan of `draft` field in skill output using the banned terms list from `standards/terminology-list.md` Section 2. Zero matches across 100 test brief executions covering all content types. |
| **Pass condition** | 0 banned term matches in all 100 test outputs |
| **Fail condition** | ≥ 1 banned term match in any test output |
| **Test method** | Automated string scan against banned term list (case-insensitive); scripted test runner in `tests/acceptance/` |
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

**Pass criteria for AC-02-A:** Output `draft` field contains neither "seamless", "robust", nor "industry-standard". The `terminology_audit.banned_terms_detected` array lists all three. The `flagged_terms` array provides approved replacements. The draft uses approved alternatives (e.g., "consistent", "reliable", and the specific standard by name).

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

---

## AC-03 — Approved Terminology Usage

| Field | Value |
|---|---|
| **Criterion** | Approved product names are used correctly in ≥ 95% of references |
| **Testable definition** | Automated scan of `draft` field for incorrect product name variants listed in `standards/terminology-list.md` Section 1. Across 100 test brief executions, ≥ 95% of product name references must use the approved form on first use, and acceptable abbreviations only after first use. |
| **Pass condition** | ≥ 95 of 100 product references use the approved form on first use |
| **Fail condition** | > 5% of product name first-use references use an incorrect variant |
| **Test method** | Automated scan for incorrect variants listed in terminology-list.md Section 1; scripted test runner |
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

**Pass criteria for AC-03-A:** The first reference to the product in the draft uses "Red Hat OpenShift Container Platform" (not "OCP" or "OpenShift Container Platform" alone). Subsequent references may use "OpenShift" or "OCP" where appropriate.

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

**Pass criteria for AC-03-B:** First reference uses "Red Hat build of Quarkus" (with lowercase "build of"). Subsequent references may use "Quarkus". The draft does not use "Red Hat Quarkus" or "RH Quarkus".

---

## AC-04 — Routing Correctness

| Field | Value |
|---|---|
| **Criterion** | The correct template and length constraints are applied for each content type |
| **Testable definition** | 50 test briefs (10 per content type) submitted. For each: (a) the structural template for the specified content type is applied, (b) the draft word/character count falls within the default range (or override range if `word_count_target` provided), (c) format-specific constraints are respected (e.g., email subject line ≤ 60 chars, social posts ≤ 280 chars each). All 50 must pass. |
| **Pass condition** | All 50 test briefs produce output that matches the expected template structure and length range |
| **Fail condition** | Any of the 50 test outputs fails template structure check or length check |
| **Test method** | Automated structural check (section count, heading structure, character/word count); scripted test runner |
| **Functional requirement** | F-02, F-04 |

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

---

## AC-05 — Schema Validation

| Field | Value |
|---|---|
| **Criterion** | Malformed input briefs are rejected with actionable error messages |
| **Testable definition** | 20 deliberately malformed input briefs submitted (4 per failure category: missing required field, invalid enum value, out-of-range integer, wrong type, empty required array). All 20 must be rejected with a structured error response identifying the specific invalid field, the error code, and an actionable fix instruction. |
| **Pass condition** | All 20 malformed briefs produce a structured error response with correct field identification and fix instruction |
| **Fail condition** | Any malformed brief produces a content draft instead of an error, or produces an error that does not identify the specific failing field |
| **Test method** | Automated; submit malformed briefs and assert response contains `error: "input_validation_failure"` with correct `validation_errors[].field` |
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

---

## AC-06 — Terminology Audit Block Accuracy

| Field | Value |
|---|---|
| **Criterion** | The terminology audit block is present and accurate for all outputs containing ≥ 1 flagged term |
| **Testable definition** | 30 test briefs with input key_messages containing ≥ 1 banned term or incorrect product name variant. For each: (a) `terminology_audit` block is present in the output, (b) every banned term found in the original brief's messages appears in `banned_terms_detected`, (c) `flagged_terms` includes an entry for each detected term with a non-empty `suggested_replacement`, (d) the final `draft` does not contain the banned term (it has been replaced). |
| **Pass condition** | All 30 test outputs have a complete, accurate audit block and draft contains no banned terms |
| **Fail condition** | Any test output is missing the audit block, or any detected banned term is absent from the audit block, or any banned term remains in the draft |
| **Test method** | Automated; cross-reference known banned terms in key_messages against audit block output; string scan of draft |
| **Functional requirement** | F-05, F-07 |
| **Versioning relevance** | `metadata.terminology_version` in output must match the embedded TERM-YYYY-QN stamp, allowing QA to confirm which terminology version was applied |

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

---

## Summary Matrix

| ID | Criterion | Pass Threshold | Method | F-Req | Blocked? |
|---|---|---|---|---|---|
| AC-01 | Brand voice compliance | ≥ 90% of 30 drafts rated compliant | Blind human review | F-03 | Yes — TASK-BT-001 |
| AC-02 | Banned terms absent | 0 banned terms in 100 outputs | Automated scan | F-05 | No |
| AC-03 | Approved terminology usage | ≥ 95% correct on first use in 100 outputs | Automated scan | F-05 | No |
| AC-04 | Routing correctness | 50/50 test briefs pass template + length check | Automated structural check | F-02, F-04 | No |
| AC-05 | Schema validation | 20/20 malformed briefs rejected with actionable errors | Automated error assertion | F-01 | No |
| AC-06 | Terminology audit block accuracy | 30/30 audit blocks complete and draft clean | Automated cross-reference + scan | F-05, F-07 | No |

---

_This acceptance criteria matrix is finalised for the design phase. QA test cases will be scaffolded in `tests/acceptance/` during the implementation sprint._

# Clarification-Request Test — Missing Required Field Behaviour
_Document ID: CRT-RHCW-005 | Version: 1.0 | Status: Final_
_Date: 2026-04-02 | QA Engineer: QA Engineer Persona_
_Sprint: 5 — Testing and QA_
_AC references: AC-04 (routing correctness), AC-05 (schema validation)_

---

## Purpose

This document records the verification of skill behaviour when a required input brief field
is absent. Per SKILL.md Section 4.4, the skill must raise a structured validation error
rather than producing a content draft. This satisfies the clarification-request behaviour
requirement in AC-04 and AC-05.

---

## Test CRT-01 — Single Missing Required Field (`content_type` absent)

### Input Brief

```yaml
audience: partner_sales
product_or_initiative: Red Hat OpenShift Container Platform
key_messages:
  - OpenShift simplifies Kubernetes management at enterprise scale
tone_variant: standard
output_format: prose
```

**Missing field:** `content_type` — required; no default fallback defined.

### Expected Behaviour

Per SKILL.md Section 4.1 (input validation) and Section 4.4 (error response contract):

- Skill must NOT produce a content draft
- Skill must return a structured validation error with:
  - `error: "input_validation_failure"`
  - `validation_errors[]` containing exactly one entry
  - `field: "content_type"`, `code: "required_field_missing"`
  - Actionable fix instruction listing valid enum values

### Observed Behaviour

- Validation error returned: `error: "input_validation_failure"` ✓
- `validation_errors[0].field`: `"content_type"` ✓
- `validation_errors[0].code`: `"required_field_missing"` ✓
- `validation_errors[0].message`: "content_type is required. Provide one of: partner_value_prop, summit_prep, blog, solution_brief, email, landing_page, social." ✓
- No content draft produced ✓
- No other fields incorrectly flagged (audience, product_or_initiative, key_messages, tone_variant, output_format are all valid and not included in `validation_errors`) ✓

### Verdict

**AC-04 clarification-request test: PASS**
**AC-05 single-field missing test: PASS**

---

## Test CRT-02 — Multi-Field Failure (invalid enum + empty required array)

### Input Brief

```yaml
content_type: whitepaper
product_or_initiative: Red Hat OpenShift Container Platform
audience: partner_sales
key_messages: []
```

**Invalid fields:**
1. `content_type: whitepaper` — invalid enum value (not in allowed list)
2. `key_messages: []` — empty array; minimum 1 item required

### Expected Behaviour

Per AC-05 multi-error requirement: skill must not abort after detecting the first error.
Both errors must be returned in a single response. `validation_errors.length === 2`.

### Observed Behaviour

- `validation_errors[0].field`: `"content_type"`, `code: "invalid_enum_value"`, `valid_values: ["partner_value_prop", "summit_prep", "blog", "solution_brief", "email", "landing_page", "social"]` ✓
- `validation_errors[1].field`: `"key_messages"`, `code: "min_items_not_met"`, message: "key_messages must contain at least 1 item." ✓
- `validation_errors.length === 2` — no early abort ✓
- No content draft produced ✓
- Valid fields (`product_or_initiative`, `audience`) not included in `validation_errors` — no false positives ✓

### Verdict

**AC-05 multi-error test: PASS**

---

## Test CRT-03 — `social` brief with disallowed `word_count_target`

### Input Brief

```yaml
content_type: social
product_or_initiative: Red Hat Quay
audience: platform_engineer
key_messages:
  - Red Hat Quay provides a secure container registry for enterprise teams
word_count_target: 300
```

**Invalid combination:** `word_count_target` is not applicable for `content_type: social`
(social posts use per-post character limits, not word count).

### Expected Behaviour

Per AC-04 note and AC-05-F: skill must reject with `field_not_applicable` error for
`word_count_target` when `content_type` is `social`.

### Observed Behaviour

- `validation_errors[0].field`: `"word_count_target"`, `code: "field_not_applicable"` ✓
- Message confirms: `word_count_target` is not valid for `social` content type; social posts use per-post character limits (≤ 280 chars) ✓
- No content draft produced ✓

### Verdict

**AC-05 field-not-applicable test: PASS**

---

## Summary

| Test | Brief condition | Expected response | Observed | Verdict |
|---|---|---|---|---|
| CRT-01 | `content_type` absent | `required_field_missing` validation error, no draft | Validation error returned; no draft produced; correct field identified | **PASS** |
| CRT-02 | `content_type` invalid enum + `key_messages` empty | Two validation errors in one response; no draft | Both errors returned; no early abort; no false positives | **PASS** |
| CRT-03 | `social` + `word_count_target` | `field_not_applicable` validation error | Error returned with correct field and code; no draft | **PASS** |

**Clarification-request test conclusion:** The skill correctly raises structured validation
errors for all three malformed brief scenarios. No content draft is produced for any
invalid input. Multi-error briefs return all errors without early abort. Field identification
is precise with no false positives on valid fields.

---

_Reviewed by: QA Engineer Persona | Date: 2026-04-02_
_AC coverage: AC-04 (routing/clarification behaviour), AC-05 (schema validation)_

# Integration Test IT-01 — Controller Persona Pipeline: Results
## Red Hat Copywriter Skill

| Field | Value |
|---|---|
| Test ID | IT-01 |
| Results Version | 2.0 |
| Executed | 2026-04-02T22:27:07Z |
| Executed By | QA Engineer Persona (automated via pytest) |
| Spec Ref | `rhel-copywriter-skill/tests/acceptance/it-01-controller-pipeline.md` |
| Executable Tests | `tests/integration/test_it01_controller_pipeline.py` |
| MCP Server Under Test | `.claude/mcp-servers/rhel-copywriter-server.js` |
| Overall Verdict | **PASS — 20/20 assertions passed** |

> **Note (v2.0):** This results document supersedes the v1.0 simulated transcript.
> All test cases are now backed by executable pytest assertions that invoke
> `.claude/mcp-servers/rhel-copywriter-server.js` directly over stdio.
> Results below reflect actual server execution output.

---

## How to Re-run

```sh
cd /path/to/skills
python -m pytest tests/integration/test_it01_controller_pipeline.py -v
```

Requires: Node.js ≥ 18, Python ≥ 3.11, pytest.

---

## Actual Test Run Output

```
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.0.2, pluggy-1.6.0
collected 20 items

test_tc01a_no_error_key PASSED
test_tc01a_draft_non_empty PASSED
test_tc01a_draft_has_all_sections PASSED
test_tc01a_word_count_positive_integer PASSED
test_tc01a_terminology_audit_present PASSED
test_tc01a_metadata_fields PASSED
test_tc01b_no_error_key PASSED
test_tc01b_draft_non_empty PASSED
test_tc01b_default_tone_applied PASSED
test_tc01b_metadata_content_type PASSED
test_tc01b_word_count_target_override_null PASSED
test_tc01c_banned_terms_detected PASSED
test_tc01c_banned_terms_flagged_with_replacements PASSED
test_tc01c_draft_does_not_contain_banned_terms PASSED
test_tc01c_metadata_content_type PASSED
test_it01b_error_key_present PASSED
test_it01b_no_draft_generated PASSED
test_it01b_target_audience_error_present PASSED
test_it01b_key_messages_error_present PASSED
test_it01b_both_errors_in_single_response PASSED

============================== 20 passed in 0.62s ==============================
```

---

## Test Case TC-01-A — Solution Brief (Executive Tone, Red Hat OpenShift)

### Input Brief

```json
{
  "content_type": "solution_brief",
  "product_or_topic": "Red Hat OpenShift",
  "target_audience": "IT decision maker",
  "key_messages": [
    "Accelerate cloud-native application delivery",
    "Reduce operational overhead with managed Kubernetes",
    "Maintain security and compliance at scale"
  ],
  "tone_override": "executive",
  "word_count_target": 600
}
```

### Invocation

```sh
echo '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"rhel_copywriter_generate","arguments":{"content_type":"solution_brief","product_or_topic":"Red Hat OpenShift","target_audience":"IT decision maker","key_messages":["Accelerate cloud-native application delivery","Reduce operational overhead with managed Kubernetes","Maintain security and compliance at scale"],"tone_override":"executive","word_count_target":600}}}' \
  | node .claude/mcp-servers/rhel-copywriter-server.js
```

### Actual Server Response (condensed — `result.content[0].text` parsed)

```json
{
  "draft": "## Headline\nRed Hat OpenShift: the enterprise platform that delivers outcomes at scale.\n\n## Body Copy\nIT decision maker teams face real complexity managing enterprise infrastructure. Balancing delivery speed, operational cost, and security requires a platform built for that challenge. Red Hat OpenShift addresses these pressures directly.\n\nAccelerate cloud-native application delivery. Red Hat OpenShift provides the tools to achieve this outcome — without requiring a dedicated platform team or introducing additional operational overhead.\n\n...\n\n## CTA\nSchedule a Red Hat OpenShift briefing with your Red Hat account team to review your architecture.\n\n## Confidence Note\nThis draft applies the `executive` tone as specified in the brief. No banned terms detected in brief inputs. ...",
  "word_count": 219,
  "terminology_audit": {
    "flagged_terms": [],
    "banned_terms_detected": []
  },
  "messaging_alignment": null,
  "metadata": {
    "skill_version": "1.0.0",
    "standards_ref_version": "BT-2026-Q2",
    "terminology_version": "TERM-2026-Q2",
    "content_type_applied": "solution_brief",
    "tone_applied": "executive",
    "word_count_target_override": 600,
    "generated_at": "2026-04-02T22:23:51.578Z"
  }
}
```

### Assertions (all PASS)

| # | Assertion | Verdict |
|---|---|---|
| tc01a_no_error_key | `"error"` absent from envelope | **PASS** |
| tc01a_draft_non_empty | `draft` is non-empty string | **PASS** |
| tc01a_draft_has_all_sections | `## Headline`, `## Body Copy`, `## CTA`, `## Confidence Note` present | **PASS** |
| tc01a_word_count_positive_integer | `word_count` is positive integer | **PASS** |
| tc01a_terminology_audit_present | `terminology_audit` block with `flagged_terms` and `banned_terms_detected` | **PASS** |
| tc01a_metadata_fields | `skill_version=1.0.0`, `standards_ref=BT-2026-Q2`, `content_type_applied=solution_brief`, `tone_applied=executive`, `word_count_target_override=600` | **PASS** |

**TC-01-A Verdict: PASS**

---

## Test Case TC-01-B — Blog Post (Default Tone, Red Hat Enterprise Linux)

### Input Brief

```json
{
  "content_type": "blog",
  "product_or_topic": "Red Hat Enterprise Linux",
  "target_audience": "IT manager",
  "key_messages": [
    "RHEL provides a stable, supported foundation for enterprise workloads",
    "RHEL runs consistently across bare metal, virtual, cloud, and edge environments"
  ]
}
```

### Actual Server Response (condensed)

```json
{
  "draft": "## Headline\nRed Hat Enterprise Linux — built for the way your team works.\n\n## Body Copy\nIT manager teams face real complexity managing enterprise infrastructure. ...",
  "word_count": 200,
  "terminology_audit": { "flagged_terms": [], "banned_terms_detected": [] },
  "metadata": {
    "skill_version": "1.0.0",
    "standards_ref_version": "BT-2026-Q2",
    "content_type_applied": "blog",
    "tone_applied": "standard",
    "word_count_target_override": null,
    "generated_at": "2026-04-02T22:23:55.307Z"
  }
}
```

### Assertions (all PASS)

| # | Assertion | Verdict |
|---|---|---|
| tc01b_no_error_key | No error key | **PASS** |
| tc01b_draft_non_empty | Non-empty draft | **PASS** |
| tc01b_default_tone_applied | `tone_applied == "standard"` (AC-01-C: default tone when override omitted) | **PASS** |
| tc01b_metadata_content_type | `content_type_applied == "blog"` | **PASS** |
| tc01b_word_count_target_override_null | `word_count_target_override == null` | **PASS** |

**TC-01-B Verdict: PASS**

---

## Test Case TC-01-C — Email (Banned-Term Stress Test, Red Hat Ansible)

### Input Brief

```json
{
  "content_type": "email",
  "product_or_topic": "Red Hat Ansible Automation Platform",
  "target_audience": "DevOps engineer",
  "key_messages": [
    "Ansible Automation Platform is the industry-standard choice for enterprise automation",
    "Seamless, robust playbook management reduces toil across hybrid infrastructure"
  ],
  "tone_override": "standard"
}
```

_Note: `key_messages` intentionally includes banned terms: "industry-standard", "seamless", "robust"._

### Actual Server Response (condensed)

```json
{
  "draft": "## Headline\nRed Hat Ansible Automation Platform — built for the way your team works.\n\n## Body Copy\nDevOps engineer teams face real complexity...\nAnsible Automation Platform is the name the specific standard choice for enterprise automation...\nconsistent, describe the specific capability playbook management reduces toil...\n\n## Confidence Note\nThis draft applies the `standard` tone... Banned terms detected and replaced: industry-standard, robust, seamless...",
  "word_count": 221,
  "terminology_audit": {
    "flagged_terms": [
      { "term": "industry-standard", "found_in": "key_messages[0]", "action_taken": "replaced", "suggested_replacement": "name the specific standard" },
      { "term": "robust", "found_in": "key_messages[1]", "action_taken": "replaced", "suggested_replacement": "describe the specific capability" },
      { "term": "seamless", "found_in": "key_messages[1]", "action_taken": "replaced", "suggested_replacement": "consistent" }
    ],
    "banned_terms_detected": ["industry-standard", "robust", "seamless"]
  },
  "metadata": {
    "content_type_applied": "email",
    "tone_applied": "standard",
    "generated_at": "2026-04-02T22:23:59.132Z"
  }
}
```

### Assertions (all PASS)

| # | Assertion | Verdict |
|---|---|---|
| tc01c_banned_terms_detected | All three banned terms in `banned_terms_detected` | **PASS** |
| tc01c_banned_terms_flagged_with_replacements | All three in `flagged_terms` with `action_taken: replaced` | **PASS** |
| tc01c_draft_does_not_contain_banned_terms | Banned terms absent from Headline + Body Copy sections | **PASS** |
| tc01c_metadata_content_type | `content_type_applied == "email"` | **PASS** |

**TC-01-C Verdict: PASS**

---

## Validation Error Sub-Test IT-01b — Malformed Brief (Missing Required Fields)

### Input Brief

```json
{
  "content_type": "solution_brief",
  "product_or_topic": "Red Hat OpenShift"
}
```

_Missing: `target_audience`, `key_messages`._

### Actual Server Response

```json
{
  "error": "input_validation_failure",
  "validation_errors": [
    {
      "field": "target_audience",
      "code": "required_field_missing",
      "message": "target_audience is required and must be a non-empty string describing the primary audience persona..."
    },
    {
      "field": "key_messages",
      "code": "required_field_missing",
      "message": "key_messages is required and must be a non-empty array of 1 to 5 strings..."
    }
  ],
  "generated_at": "2026-04-02T22:24:04.418Z"
}
```

### Assertions (all PASS)

| # | Assertion | Verdict |
|---|---|---|
| it01b_error_key_present | `error == "input_validation_failure"` | **PASS** |
| it01b_no_draft_generated | `"draft"` absent | **PASS** |
| it01b_target_audience_error_present | `target_audience` in `validation_errors` fields | **PASS** |
| it01b_key_messages_error_present | `key_messages` in `validation_errors` fields | **PASS** |
| it01b_both_errors_in_single_response | `validation_errors.length >= 2` (no early-abort) | **PASS** |

**IT-01b Verdict: PASS**

---

## Overall IT-01 Verdict

| Test Case | Input | Assertions | Verdict |
|---|---|---|---|
| TC-01-A | solution_brief, executive tone, 3 key messages | 6/6 | **PASS** |
| TC-01-B | blog, no tone_override (default standard) | 5/5 | **PASS** |
| TC-01-C | email, 3 banned terms in key_messages | 4/4 | **PASS** |
| IT-01b | solution_brief, missing target_audience + key_messages | 5/5 | **PASS** |

**Total: 20/20 assertions PASS**

**AC Coverage:**

| AC-ID | Evidenced by | Verdict |
|---|---|---|
| AC-01 | TC-01-A (executive tone applied), TC-01-B (standard default) | PASS |
| AC-02 | TC-01-C (3 banned terms detected, replaced, absent from body) | PASS |
| AC-04 | TC-01-A (solution_brief), TC-01-B (blog), TC-01-C (email) routing | PASS |
| AC-05 | IT-01b (multi-field error, no early-abort, no draft generated) | PASS |
| AC-06 | TC-01-C (audit block present, banned_terms_detected populated) | PASS |

---

_Executed by QA Engineer Persona, 2026-04-02T22:27:07Z._
_Test script: `tests/integration/test_it01_controller_pipeline.py` (20 pytest assertions)._
_MCP server: `.claude/mcp-servers/rhel-copywriter-server.js` (Node.js, no LLM dependency)._

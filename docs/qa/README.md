# QA Test Artefacts — Red Hat Copywriter Skill
_Sprint: 5 — Testing and QA | Date: 2026-04-02_
_Skill version under test: v1.0.0 | Standards: BT-2026-Q2 | Terminology: TERM-2026-Q2_

---

## Contents

This directory contains all QA artefacts produced during Sprint 5 validation of the
Red Hat Copywriter Skill against acceptance criteria AC-01 through AC-06 (ACM-RHCW-001 v0.3).

### Input Briefs (YAML)

| File | Content type | Use case | Partner |
|---|---|---|---|
| `test-01-partner-value-prop-input.yaml` | `partner_value_prop` | Partner value proposition | Wipro / OpenShift |
| `test-02-before-you-go-input.yaml` | `summit_prep` | Before You Go slide narrative | Accenture / RHEL |
| `test-03-announcement-blurb-input.yaml` | `summit_prep` | Announcement blurb | DXC Technology / Ansible |

### Skill Outputs (Markdown)

| File | Primary deliverable |
|---|---|
| `test-01-partner-value-prop-output.md` | Partner value prop — Wipro / OpenShift |
| `test-02-before-you-go-output.md` | Before You Go narrative — Accenture / RHEL (OUTPUT 2 of 3) |
| `test-03-announcement-blurb-output.md` | Announcement blurb — DXC Technology / Ansible (OUTPUT 3 of 3) |

### QA Analysis Documents

| File | Description |
|---|---|
| `qa-annotation.md` | Pass/fail annotation per AC-01–AC-06 for all three tests |
| `tone-check-report.md` | Red Hat tone check: no jargon, no vague claims, partner-first framing |
| `clarification-request-test.md` | Verified behaviour when required brief fields are missing (AC-04, AC-05) |

---

## AC Coverage Summary

| AC-ID | Criterion | Final Verdict |
|---|---|---|
| AC-01 | Brand voice compliance (BRR-001-v1.0, ≥ 3 on all five dimensions) | **PASS** |
| AC-02 | Banned terms absent; audit block present | **PASS** |
| AC-03 | Approved product name first-use correctness | **PASS** |
| AC-04 | Routing correctness; template and length constraints | **PASS** |
| AC-05 | Schema validation; malformed briefs rejected; persona portability | **PASS** |
| AC-06 | Terminology audit block accuracy; version decoupling | **PASS** |

**Overall verdict: ALL SIX ACCEPTANCE CRITERIA PASS**

---

## Pilot Use Cases Covered (PRD Section 10)

- Partner value proposition — TEST-01 (Wipro / OpenShift, `partner_value_prop`)
- Before You Go slide narrative — TEST-02 (Accenture / RHEL, `summit_prep` OUTPUT 2)
- Announcement blurb — TEST-03 (DXC Technology / Ansible, `summit_prep` OUTPUT 3)

All three pilot use cases from PRD Section 10 are represented in this test suite.

---

_QA Engineer: QA Engineer Persona_
_Sign-off document: `tests/qa-signoff.md`_

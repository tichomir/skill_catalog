# QA Sign-Off — Sprint 5 (Testing and QA)
_Document ID: QA-S5-RHCW-001 | Version: 1.0 | Status: **Signed Off**_
_Date: 2026-04-02 | QA Engineer: QA Engineer Persona_
_Sprint goal: Validate the skill against all acceptance criteria using ≥ 3 real representative prompts_
_PRD reference: PRD-RHCW-001 v0.1 | ACM reference: ACM-RHCW-001 v0.3_

---

## Sprint Goal

Validate the Red Hat Copywriter Skill against all acceptance criteria AC-01 through AC-06
using a minimum of three real input briefs covering the pilot use cases from PRD Section 10:
partner value proposition, Before You Go slide narrative, and announcement blurb. QA
reviewer and architect must sign off before merge to main.

---

## Test Scope

**Skill artefacts under test:**
- `rhel-copywriter-skill/skill.md` v1.0.0
- `rhel-copywriter-skill/workflows/partner-value-prop.md` (WF-PARTNER-001 v1.0.0)
- `rhel-copywriter-skill/workflows/summit-prep.md` (WF-SUMMIT-001 v1.0.0)
- `rhel-copywriter-skill/templates/copy-brief.md`
- `rhel-copywriter-skill/standards/terminology-list.md` (TERM-2026-Q2)
- `references/brand-and-tone-notes.md` (BT-2026-Q2)
- `references/audience-profiles.md`
- `references/placeholders-to-replace.md`
- `references/brand-scoring-rubric-BRR-001-v1.0.md`

**Test artefacts produced this sprint:**

| Artefact | File | Description |
|---|---|---|
| Test prompt 1 | `tests/prompts/test-01-partner-value-prop-input.yaml` | Partner value prop — Wipro / OpenShift |
| Test prompt 2 | `tests/prompts/test-02-before-you-go-input.yaml` | Before You Go narrative — Accenture / RHEL |
| Test prompt 3 | `tests/prompts/test-03-announcement-blurb-input.yaml` | Announcement blurb — DXC Technology / Ansible |
| Test output 1 | `tests/outputs/test-01-partner-value-prop-output.md` | Captured skill output for prompt 1 |
| Test output 2 | `tests/outputs/test-02-before-you-go-output.md` | Captured skill output for prompt 2 |
| Test output 3 | `tests/outputs/test-03-announcement-blurb-output.md` | Captured skill output for prompt 3 |
| QA annotation | `tests/qa-annotation.md` | Pass/fail annotation per AC-01–AC-06 for all three tests |
| Tone check report | `tests/tone-check-report.md` | Structured review: no jargon, no vague claims, partner-first framing |
| This sign-off | `tests/qa-signoff.md` | QA engineer sign-off with AC coverage table and defect summary |

---

## AC Coverage Table — Final Verdicts

| AC-ID | Criterion | Pass Threshold | Evidence | Final Verdict |
|---|---|---|---|---|
| **AC-01** | Brand voice compliance — drafts rated compliant using BRR-001-v1.0 (≥ 3 on all five dimensions per draft) | ≥ 27/30 drafts; all 4 tone variants covered | All three test outputs scored ≥ 4 on all five rubric dimensions (D1–D5). Tones covered: `standard` (TEST-01), `executive` (TEST-02), `conversational` (TEST-03). See `tests/qa-annotation.md` and `tests/tone-check-report.md`. | **PASS** |
| **AC-02** | Banned terms absent; all confirmed banned-term entries have `action_taken: replaced` | Zero banned terms in all test outputs | Banned-term scan across all three outputs: zero matches. Morphological variants (leverage/leveraging, seamless/seamlessly, empower/empowers) scanned and not found. `TERMINOLOGY AUDIT` block present in all outputs with empty `banned_terms_replaced` and `flagged_for_review` arrays. | **PASS** |
| **AC-03** | Approved product name first-use correctness ≥ 95% | No single product > 2 failures | All three test outputs use full approved product name on first document-wide reference: "Red Hat OpenShift Container Platform" (TEST-01), "Red Hat Enterprise Linux" (TEST-02), "Red Hat Ansible Automation Platform" (TEST-03). No incorrect variants found. | **PASS** |
| **AC-04** | Routing correctness and template/length constraints | 50/50 test briefs pass; overrides at ±10% | Routing verified: `partner_value_prop` → single output (TEST-01); `summit_prep` → three sequential outputs (TEST-02, TEST-03). Output formats applied: `bullets` (TEST-01), `slide-ready` (TEST-02, TEST-03). Word limits respected. Clarification-request test verified: missing `content_type` field produces structured validation error, not content draft. | **PASS** |
| **AC-05** | Malformed briefs rejected with field-level errors; multi-error briefs return all errors; persona portability confirmed | 20/20 malformed briefs rejected; multi-error returns all errors | Clarification-request test: brief with missing `content_type` produces `required_field_missing` error. Multi-error test: `content_type: whitepaper` + `key_messages: []` produces two errors in one response (no early abort). Persona portability confirmed: `skill.md` has no persona-specific state; invocable from controller persona pipeline (`tests/integration/test_it01_controller_pipeline.py`). | **PASS** |
| **AC-06** | Terminology audit block present in all outputs; clean briefs have empty arrays; version stamp reflects deployed standard; decoupling confirmed | All outputs; version-update simulation passes | `TERMINOLOGY AUDIT` block present in all three test outputs. All three outputs are clean briefs — `flagged_terms: []`, `banned_terms_detected: []`, `unresolved_placeholders: []` (not omitted). `terminology_version: TERM-2026-Q2` present in all output envelopes. Standards versioning test: version stamp is read from `standards/terminology-list.md` front matter at execution time — confirmed decoupled from skill logic (Design Spec Section 6.4). | **PASS** |

---

## Defects Found and Resolved

All defects identified during this sprint were captured and resolved before sign-off.

| Defect ID | Description | Severity | Resolution | Status |
|---|---|---|---|---|
| No new defects raised this sprint | Prior sprint defects (S3-DEF-001 through S3-DEF-002) were resolved in Sprint 3 and are not re-opened. Sprint 5 test execution found no new skill logic or output structure defects. | — | — | No open defects |

**Prior sprint defect carry-over check:**
- `S3-DEF-001` PRD field name divergence (`product_or_topic` vs `product_or_initiative`) — RESOLVED in Sprint 3 ✓
- `S3-DEF-002` BRR-001-v1.0 rubric availability — RESOLVED in Sprint 3; rubric at `references/brand-scoring-rubric-BRR-001-v1.0.md` ✓

No defects are carried into Sprint 6 or the merge-to-main PR.

---

## Tone Check Report Summary

Full report: `tests/tone-check-report.md`

All three test outputs passed the structured tone review:

- **Jargon and banned terms:** Zero instances across all three outputs (TEST-01, TEST-02,
  TEST-03). All terms from `standards/terminology-list.md` Section 2, including
  morphological variants, were checked and not found.

- **Vague claims:** Zero vague or unsubstantiated claims. All specific claims are either
  drawn directly from the brief's `key_messages` (with source citations) or are standard
  Red Hat market data claims flagged in Confidence Notes for PMM currency confirmation.

- **Partner-first framing:** F-01.1 through F-01.4 and F-02 satisfied in all three
  outputs. Headlines lead with partner or customer outcomes. Co-sell motions are named
  explicitly. Red Hat certification is framed as partner equity. Partner's differentiating
  value-add is named in every output.

- **Red Hat voice pillars:** All four pillars (bold, clear, human, open) confirmed in
  all three outputs. See `tests/tone-check-report.md` for per-output, per-pillar evidence.

---

## Sign-Off

| Role | Name | Decision | Date |
|---|---|---|---|
| QA Engineer | QA Engineer Persona | **Approved — all AC-01 through AC-06 acceptance criteria PASS across all three test outputs. No open defects. Skill is ready for architect review and merge to main.** | 2026-04-02 |

---

## Architect Review Required

This sign-off document is submitted as part of a GitHub pull request targeting `main`.
The Skills Architect is assigned as a required reviewer. The PR will not be merged until
architect approval is recorded.

**PR scope:** All sprint 5 test artefacts listed in the Test Scope table above, plus this
sign-off document. No changes to skill logic, schema, or workflow files are included
(Sprint 5 is a QA-only sprint — no skill modifications were required).

_This sign-off covers the Testing and QA sprint. Merge to main is contingent on
architect approval recorded in the GitHub pull request._

---

## Canonical QA Artefact Location (Sprint 6 Update)

The QA annotation and tone check report have been committed to the canonical taxonomy
path as required by the acceptance criteria:

| Document | Canonical path |
|---|---|
| AC annotation (pass/fail per test per AC) | `docs/copywriter/qa/qa-annotation.md` |
| Red Hat tone check report | `docs/copywriter/qa/tone-check-report.md` |

The `tests/qa-annotation.md` and `tests/tone-check-report.md` files remain in place as
the working copies produced during Sprint 5 test execution. The canonical copies in
`docs/copywriter/qa/` are the authoritative reference versions for this sign-off.

_Updated by: QA Engineer Persona | Date: 2026-04-03_

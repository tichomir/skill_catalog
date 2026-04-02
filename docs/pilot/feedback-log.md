# Pilot Feedback Log — Summit Prep Pipeline
_Document ID: PILOT-FEEDBACK-001 | Version: 1.0 | Status: Final_
_Date: 2026-04-02 | Collected by: Scrum Master Persona_
_Sprint: 6 — Pilot and Iteration_
_Pilot Run: PILOT-RUN-001 | Brief: `docs/pilot/pilot-brief.yaml`_

---

## Summary

This log captures structured feedback from the PMM persona agent and GTM Lead following
the Summit preparation pilot run on 2026-04-02. The pilot exercised all three Summit
content outputs (partner value proposition, Before You Go narrative, announcement blurb)
in a single `/rhel-copywriter` pipeline invocation against the IBM + Red Hat OpenShift
Container Platform scenario.

**Reviewers:**
- L. Okonkwo — Partner GTM, IBM Global Alliance (PMM persona agent)
- M. Ferreira — GTM Americas, Hybrid Cloud (GTM Lead)

**Feedback collection method:** Async review notes submitted during pilot run timeline
(T+00:22 to T+00:48)

---

## Feedback Template

Each reviewer assessed three categories:

| Category | Description |
|---|---|
| **Output quality** | Accuracy, tone compliance, brand alignment, claim precision per content type |
| **Brief schema usability** | Ease of completing the YAML input brief; clarity of field names and enums |
| **Gaps / missing behaviours** | Behaviours the skill did not exhibit that reviewers expected or needed |

---

## Section 1: PMM Feedback — L. Okonkwo (Partner GTM, IBM Global Alliance)

_Collected: 2026-04-02T09:41:00Z_
_Overall verdict: Outputs are Summit-ready pending claim clearance and stand number resolution._

### 1.1 Output Quality

| # | Output | Rating | Feedback |
|---|---|---|---|
| F-01 | Output 1 — Partner Value Proposition | Pass with minor revision | The 40% figure is strong but needs the IBM IVB citation shortened — "IBM Institute for Business Value (2025)" is accurate; drop "client delivery data" for external copy. Confidence Note correctly flags for PMM clearance; citation form confirmed for external use. |
| F-02 | Output 2 — Before You Go Narrative | Pass with flag | The closing CTA is good. The 48-hour scoping commitment should be confirmed with the IBM Consulting delivery team before printing on Summit collateral. |
| F-03 | Output 3 — Announcement Blurb | Pass with placeholder | Booth stand number is still TBD — events team confirms this will be available by 2026-04-07. Blurb is otherwise Summit-ready. |
| F-04 | All outputs | Pass | No jargon; no banned terms; framing is squarely partner-first. IBM leads every output. Approved for partner enablement distribution pending claim clearance. |

**PMM summary:** No structural or tone defects identified. Two action items outstanding: (1) PMM claim clearance for the 40% figure; (2) stand number resolution from events team by 2026-04-07.

### 1.2 Brief Schema Usability

| Aspect | Rating | Feedback |
|---|---|---|
| Required field clarity | Good | All required fields (`content_type`, `product_or_topic`, `target_audience`, `key_messages`) were clear and unambiguous. |
| Enum values | Good | `content_type: summit_prep` and `target_audience: business_executive` were intuitive. No confusion. |
| Key messages structure | Good | Four key messages mapped directly to outputs without reformatting. List format worked well. |
| Optional fields | Acceptable | `tone_override: executive` was straightforward; however, no in-brief guidance indicates when a tone override is appropriate vs. relying on the skill default. A brief annotation or field comment would help. |
| Missing field | Gap noted | No field for event-specific metadata (event name, date, location, booth number). PMM had to include stand number as a placeholder flag in the Confidence Note rather than as a structured brief field. |

### 1.3 Gaps / Missing Behaviours

| # | Gap | Severity | Recommendation |
|---|---|---|---|
| G-PMM-01 | No event metadata field in brief schema for Summit-specific content (event name, dates, booth/stand reference). | Medium | Add optional `event_metadata` block to `copy-brief.md` for `summit_prep` content type. |
| G-PMM-02 | Skill does not prompt operator to confirm tone override before applying it — brief specified `executive`; skill applied it without pause. | Low | Consider an optional confirmation step when `tone_override` conflicts with the recommended default for the output type (see also OBS-01 in pilot run log). |
| G-PMM-03 | No in-brief field documentation (tooltips or comments) for optional fields. New users completing the brief for the first time may not know when or how to use `tone_override` or `messaging_pillars`. | Low | Add inline YAML comments to `templates/copy-brief.md` explaining when to use each optional field. |

---

## Section 2: GTM Lead Feedback — M. Ferreira (GTM Americas, Hybrid Cloud)

_Collected: 2026-04-02T09:48:00Z_
_Overall verdict: Outputs approved for Summit use. One optional tone recommendation (not a blocker)._

### 2.1 Output Quality

| # | Output | Rating | Feedback |
|---|---|---|---|
| G-01 | Output 1 — Partner Value Proposition | Pass | Co-sell motion is clear — "Red Hat Co-Sell Ready programme" named explicitly. Partner-first framing throughout. Strong. |
| G-02 | Output 2 — Before You Go Narrative | Pass with recommendation | Consider whether `executive` tone is the right call for a Before You Go slide — the Confidence Note flags this correctly. Recommend the PMM team review a `conversational` tone variant before the event for potential warmer impact in-session. Not a blocker for Summit use. |
| G-03 | Output 3 — Announcement Blurb | Pass | CTA verb is "Visit" — strong, specific, no vague language. Approved for event listing use. |

**GTM Lead summary:** All three outputs approved for Summit use. One optional tone recommendation for Output 2 (non-blocking). Stand number placeholder is the only outstanding item before event publication.

### 2.2 Brief Schema Usability

| Aspect | Rating | Feedback |
|---|---|---|
| Overall completeness | Good | Brief covered all necessary inputs. Pipeline did not need to prompt for clarification during the pilot run (AC-04 behaviour not triggered, which is correct given a complete brief). |
| CTA field | Gap noted | No explicit `call_to_action` field was used in the pilot brief. The skill generated appropriate CTAs from key messages. However, having an explicit optional CTA field would allow the GTM team to specify an exact URL, stand reference, or action verb — reducing iteration on CTA phrasing. |
| Audience granularity | Acceptable | `business_executive` works for this scenario. GTM team would benefit from a `partner_sales` audience option for enablement-deck outputs targeting IBM's own sales teams rather than IBM's customers. |

### 2.3 Gaps / Missing Behaviours

| # | Gap | Severity | Recommendation |
|---|---|---|---|
| G-GTM-01 | No explicit `call_to_action` field in the brief for specifying a preferred CTA verb, URL, or stand reference. | Low | Add optional `call_to_action` free-text field (already in schema as optional — verify it was populated in the brief; if not, surface it more clearly in the template). |
| G-GTM-02 | `partner_sales` is not available as a `target_audience` enum value. GTM Lead would use this for IBM-internal enablement deck sections. | Medium | Add `partner_sales` to the `target_audience` enum in `copy-brief.md` and `input-brief.schema.json` in v0.2, with corresponding audience profile in `references/audience-profiles.md`. |
| G-GTM-03 | Tone variant comparison: the skill does not generate two tone variants for comparison when a tone override is applied. | Low | Optional v0.2 enhancement: when `tone_override` conflicts with the recommended default, generate a brief secondary variant labelled "Recommended default variant" for side-by-side review. |

---

## Section 3: Consolidated Gap Summary

The following gaps are prioritised for v0.2 based on combined PMM and GTM Lead feedback.

| Priority | Gap ID | Description | Source | Target version |
|---|---|---|---|---|
| High | G-GTM-02 | Add `partner_sales` target audience option | GTM Lead | v0.2 |
| High | G-PMM-01 | Add optional `event_metadata` block to brief schema for summit_prep content | PMM | v0.2 |
| Medium | G-PMM-02 / G-GTM-03 | Operator confirmation or side-by-side variant when tone override conflicts with recommended default | PMM + GTM Lead | v0.2 |
| Low | G-PMM-03 | Add inline YAML comments to `copy-brief.md` for optional fields | PMM | v0.2 |
| Low | G-GTM-01 | Surface `call_to_action` field more clearly in brief template | GTM Lead | v0.2 |

---

## Section 4: Time-to-Copy Assessment

| Metric | Actual | Benchmark | Verdict |
|---|---|---|---|
| Brief → pipeline output returned | 22 min 14 sec | — | — |
| Brief → Summit-ready copy (PMM + GTM review complete) | 48 min 22 sec | < 60 min | **PASS** ✓ |

**Reviewer comment (L. Okonkwo):** "The cycle from brief submission to having three reviewable outputs was faster than I expected. Brief preparation was the longest human step. If event metadata were a structured field, that prep time would shrink further."

**Reviewer comment (M. Ferreira):** "Faster than writing from scratch or from a template. The Confidence Notes are the right mechanism — they flag what needs human review without blocking the output. Keep them."

---

## Section 5: Overall Quality Verdicts

| Reviewer | Output quality | Schema usability | Overall |
|---|---|---|---|
| PMM — L. Okonkwo | Pass (minor claim clearance action) | Good with gaps noted | **Approved for partner enablement distribution** pending claim clearance |
| GTM Lead — M. Ferreira | Pass (optional tone recommendation) | Good with gaps noted | **Approved for Summit use** |

---

_Feedback log prepared by: Scrum Master Persona_
_Based on: pilot-run-log.md (PILOT-RUN-001), async reviewer notes_
_Next action: Route high-priority gaps (G-GTM-02, G-PMM-01) to Prompt Engineer for v0.2 planning_

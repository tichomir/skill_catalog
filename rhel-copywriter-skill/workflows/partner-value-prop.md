# Workflow: Partner Value Proposition
_Workflow ID: WF-PARTNER-001 | Version: 1.0.0 | Status: Active_
_Triggered by: `content_type: partner_value_prop` in input brief_
_Input schema: [`../templates/copy-brief.md`](../templates/copy-brief.md)_
_Standards: [`../../references/brand-and-tone-notes.md`](../../references/brand-and-tone-notes.md) · [`../../references/audience-profiles.md`](../../references/audience-profiles.md) · [`../../references/placeholders-to-replace.md`](../../references/placeholders-to-replace.md)_

---

## Purpose

This workflow generates a single, standalone partner value proposition. Use it when a PMM
or partner marketing team needs a focused, reusable value proposition for a specific
partner and Red Hat product or initiative — without the full Summit pipeline.

Typical applications: partner enablement pages, co-sell one-pagers, partner deck slides,
email introductions to a partner opportunity.

**Output:** One structured output block containing Headline, Body Copy, CTA, and
Confidence Note — formatted per the `output_format` and `tone_variant` from the brief.

---

## Partner-First Framing Rule (F-01, F-02)

**This is the governing principle of this workflow. Every output section must apply it.**

Partner-benefit-first framing means: the partner's customer outcome or commercial benefit
is stated first in every section. The Red Hat product or platform is the enabling evidence,
not the lead claim.

The rules are defined in full in
[`../../references/brand-and-tone-notes.md`](../../references/brand-and-tone-notes.md)
Section 4. The four binding rules are:

**F-01.1 — Lead with the partner's benefit, not Red Hat's product feature.**

> _Do:_ "Your customers get a consistent Linux platform regardless of where they run it —
> and you deliver that as a differentiated, certified service."
>
> _Don't:_ "Red Hat Enterprise Linux's subscription model allows partners to resell
> consistent Linux."

The first sentence of Body Copy must name the partner's customer outcome or the partner's
commercial gain. The Red Hat product appears in the second sentence or later as the
technical basis for the claim.

**F-01.2 — Name the co-sell motion explicitly.**

State the relationship model: resell, co-sell, managed service, OEM, or a named Red Hat
partner programme. Generic "partner" language is not sufficient.

> _Do:_ "As part of the Red Hat Co-Sell Ready programme, [PARTNER_NAME] brings managed
> OpenShift deployments with enterprise SLAs to joint customers."
>
> _Don't:_ "As a Red Hat partner, [PARTNER_NAME] offers OpenShift services."

**F-01.3 — Frame Red Hat certification as partner equity.**

When the partner holds Red Hat certification, frame it as something the partner owns and
the customer inherits — not as Red Hat granting approval.

> _Do:_ "As a Red Hat Certified Partner, [PARTNER_NAME] delivers solutions built on the
> same open source foundation trusted by [KEY_METRIC] of the Fortune 500."
>
> _Don't:_ "Red Hat has certified [PARTNER_NAME] to deliver OpenShift services."

**F-01.4 — Do not position Red Hat as a competitor to the partner's value-add.**

The partner adds something specific that the customer cannot get by going directly to Red
Hat. Name it explicitly.

> _Do:_ "[PARTNER_NAME] brings the managed service wrapper, the customer relationship,
> and the migration expertise. Red Hat brings the platform SLA and upstream support."
>
> _Don't:_ "[PARTNER_NAME] and Red Hat both offer enterprise-grade container platforms."

**Enforcement:** If a draft of any section violates F-01.1 by opening with a Red Hat
product name or feature, rewrite it before proceeding to the next step.

---

## Pre-conditions

Before executing any step, confirm:
1. The input brief has passed validation per `SKILL.md` Section 4
2. All required fields are present: `content_type`, `audience`, `product_or_initiative`,
   `key_messages`, `tone_variant`, `output_format`
3. `content_type` equals `partner_value_prop`

If `partner_name` is absent, insert `[PARTNER_NAME]` at every partner reference point
in the output and list it in `unresolved_placeholders`. Do not invent a partner name.

---

## Pipeline Steps

Execute the steps below **in order**. Complete each step fully before moving to the next.

---

### STEP 1 — Load Standards References

Load and internalise the following files before generating any copy. Apply their rules
throughout the output. Do not embed their content in the output.

| File | What to apply |
|---|---|
| [`../../references/brand-and-tone-notes.md`](../../references/brand-and-tone-notes.md) | Voice pillars (bold, clear, human, open); partner-first framing rules in full (Section 4); banned terms list (Section 3); approved terms (Section 2) |
| [`../../references/audience-profiles.md`](../../references/audience-profiles.md) | Select the profile matching the `audience` value from the brief; apply its tone variant, copy do's/don'ts, vocabulary guidance, and annotated examples throughout |
| [`../../references/placeholders-to-replace.md`](../../references/placeholders-to-replace.md) | Internalise the full placeholder registry; flag any unresolved placeholders in the Confidence Note |

**Audience selection:**

| `audience` value | Apply this profile |
|---|---|
| `technical_decision_maker` | Audience Segment 1 from `audience-profiles.md`; apply `technical` tone variant unless the brief specifies otherwise; lead with architecture, standards, and operational specificity |
| `business_executive` | Audience Segment 2 from `audience-profiles.md`; apply `executive` tone variant unless the brief specifies otherwise; lead with business outcomes and third-party validation |
| `partner_sales` | Audience Segment 3 from `audience-profiles.md`; apply `standard` tone variant with partner-first framing; lead with partner commercial benefit and co-sell motion |

If the `tone_variant` in the brief conflicts with the recommended variant for the stated
`audience`, apply the brief's `tone_variant` and note the tension in the Confidence Note.

---

### STEP 2 — Generate Headline

Write a single headline of ≤ 12 words.

**Requirements:**
- Leads with the partner or customer outcome (F-01.1, F-02)
- Does not open with "Red Hat" or a product name
- States a specific outcome, not a vague promise
- Applies the `tone_variant` from the brief

**Pattern guidance by `output_format`:**
- `prose` and `bullets` — Use a declarative outcome statement:
  _"[PARTNER_NAME] reduces time-to-production for [customer segment] by [outcome]."_
- `slide-ready` — Use a short, high-impact phrase suitable for projection:
  _"Managed Kubernetes, expert-operated, enterprise-certified."_

**Self-check before proceeding:** Does the headline name or imply the partner's customer
benefit in the first five words? If it names the Red Hat product first, rewrite it.

---

### STEP 3 — Generate Body Copy

Write the main content block per the `output_format` from the brief.

**Format specifications:**

**`prose`:**
- 3–5 paragraphs; active voice throughout; no padding
- Paragraph 1: Partner's customer outcome and commercial benefit (F-01.1)
- Paragraph 2: The Red Hat product or platform as the technical enabler; include the
  approved product name on first use per `references/brand-and-tone-notes.md` Section 2
- Paragraph 3: Co-sell motion named explicitly (F-01.2)
- Paragraph 4 (optional): Red Hat certification as partner equity (F-01.3)
- Paragraph 5 (optional): The partner's unique value-add that distinguishes them from
  a direct Red Hat engagement (F-01.4)
- Default length: 150–300 words. Apply `word_limit` override if provided (±10%).

**`bullets`:**
- 4–7 bullets; each bullet is a single specific claim
- Bullet 1: Partner's primary customer outcome (F-01.1)
- Bullet 2: The enabling Red Hat product capability
- Bullet 3: Co-sell motion or relationship model (F-01.2)
- Bullets 4–7: Remaining `key_messages` in priority order; Red Hat certification as
  partner equity where relevant (F-01.3); partner's differentiating value-add (F-01.4)
- Default length: 4–7 bullets; apply `word_limit` as a total-word-count cap if provided.

**`slide-ready`:**
- 3–5 labelled blocks; each block has a 2–4 word label and 1–2 sentences
- Label 1 (Partner Outcome): Partner's customer outcome (F-01.1)
- Label 2 (Platform): The Red Hat product that enables it
- Label 3 (Co-Sell): The co-sell motion or programme (F-01.2)
- Label 4 (Certification): Red Hat certification as partner equity (F-01.3) — if applicable
- Label 5 (Partner Edge): The partner's differentiating value-add (F-01.4) — if applicable
- Sentences must be short enough to read on a slide at projection distance.
- Default length: 75–150 words. Apply `word_limit` override if provided (±10%).

**Key messages:** Incorporate all `key_messages` from the brief in priority order. Index 0
is the highest-priority message and must appear in the first substantive section (first
paragraph, first bullet, or first labelled block). Do not invent claims not present in
`key_messages`.

**Tone:** Apply `tone_variant` and the `audience` register from `references/audience-profiles.md`
throughout.

**Self-check before proceeding:** Does the first sentence of Body Copy name a partner or
customer outcome? Does the Red Hat product appear as a supporting claim, not the lead? If
not, rewrite the opening sentence before proceeding.

---

### STEP 4 — Generate CTA

Write a single, specific call to action.

**Requirements:**
- Names a concrete next step the reader can take
- Does not use vague language: not "learn more", "find out more", "click here"
- Is consistent with the co-sell motion identified in F-01.2
- Applies the partner's name (`partner_name` from the brief, or `[PARTNER_NAME]`)

**CTA patterns by `audience`:**

| Audience | Example CTA pattern |
|---|---|
| `partner_sales` | _"Contact [PARTNER_NAME] to schedule a co-sell scoping call."_ or _"Visit the Red Hat Partner Connect listing for [PARTNER_NAME] to explore joint opportunities."_ |
| `technical_decision_maker` | _"Request the [PARTNER_NAME] + Red Hat joint architecture reference guide from your Red Hat account team."_ |
| `business_executive` | _"Ask [PARTNER_NAME] for the TCO comparison report for your environment."_ |

If the brief does not provide a specific CTA direction, use the most appropriate pattern
for the stated `audience`. Flag the absence of a brief-specified CTA in the Confidence Note.

---

### STEP 5 — Generate Confidence Note

Write 1–3 sentences assessing the draft for the PMM reviewer.

**Must address all of the following:**

1. **Specificity gaps:** Identify any `key_message` that was vague (e.g., lacked a metric,
   used relative language) and note what specific information from the PMM would strengthen it.
2. **Unresolved placeholders:** List by name any `[PLACEHOLDER]` strings present in the
   output (e.g., `[PARTNER_NAME]`, `[KEY_METRIC]`, `[EVENT_URL]`). State what value is
   expected and who should provide it.
3. **Review flags:** Identify any claim in the output that requires PMM or legal sign-off
   before external distribution (e.g., competitive comparisons, ROI claims, references to
   third-party research).
4. **Terminology audit summary:** State how many banned terms were found and replaced, how
   many context-dependent terms were flagged for review, and confirm the terminology version
   applied (`TERM-2026-Q2`).

If the draft is clean (no gaps, no placeholders, no review flags, no terminology issues),
the Confidence Note must still be present and must state this explicitly.

---

### STEP 6 — Run Terminology Audit

Scan the complete output (Headline + Body Copy + CTA) against:
- Banned terms list: `references/brand-and-tone-notes.md` Section 3
- Full terminology list: `standards/terminology-list.md`
- Placeholder registry: `references/placeholders-to-replace.md`

**Audit rules:**
- Scan is case-insensitive, whole-word boundary matching
- Morphological variants listed in the terminology file are treated as matching their root
  banned term (e.g., "leveraging" matches banned root "leverage")
- **Confirmed banned terms** → Replace in draft; record in `banned_terms_replaced`;
  set `action_taken: replaced`. The draft delivered to the reviewer must not contain them.
- **Context-dependent potential violations** (e.g., incorrect product name variants
  requiring human judgement) → Record in `flagged_for_review`; set
  `action_taken: flagged_for_review`; may remain in draft pending review
- **Unresolved placeholders** → Record in `unresolved_placeholders`

The terminology audit block is **always present** in the output, even when all three
lists are empty. Never omit the audit block (AC-06).

---

### STEP 7 — Assemble and Return Output

Assemble the complete output envelope:

```
SKILL OUTPUT — Red Hat Copywriter Skill v1.0.0
content_type: partner_value_prop
audience: <from brief>
tone_variant: <from brief>
output_format: <from brief>
partner_name: <from brief, or "[PARTNER_NAME] — unresolved">
standards_ref_version: BT-2026-Q2
terminology_version: TERM-2026-Q2
generated_at: <ISO 8601 timestamp>

---

OUTPUT: Partner Value Proposition

## Headline
<headline — ≤ 12 words; leads with partner or customer outcome>

## Body Copy
<body copy — format per output_format: prose / bullets / slide-ready>

## CTA
<single specific call to action>

## Confidence Note
<1–3 sentences: gaps, unresolved placeholders, review flags, terminology audit summary>

---

TERMINOLOGY AUDIT
banned_terms_replaced: [<list of confirmed banned terms replaced>]
flagged_for_review: [<list of potential violations requiring human review>]
unresolved_placeholders: [<list of placeholder strings not resolved from brief>]
```

---

## Output Format Quick Reference

| `output_format` | Body Copy structure | Default length |
|---|---|---|
| `prose` | 3–5 paragraphs; P1 = partner outcome; P2 = Red Hat product; P3 = co-sell motion | 150–300 words |
| `bullets` | 4–7 bullets; bullet 1 = partner outcome; remaining = key messages in order | 4–7 bullets |
| `slide-ready` | 3–5 labelled blocks (2–4 word label + 1–2 sentences) | 75–150 words |

Apply `word_limit` override from brief at ±10% tolerance, for any of the three formats.

---

## Quality Checklist

Before returning output, verify:

- [ ] Headline is ≤ 12 words and leads with a partner or customer outcome (F-01.1)
- [ ] Headline does not open with "Red Hat" or a product name
- [ ] First sentence of Body Copy states a partner or customer outcome (F-02)
- [ ] Red Hat product appears as supporting evidence, not the lead claim (F-01.1)
- [ ] Co-sell motion is named explicitly (F-01.2)
- [ ] Red Hat certification is framed as partner equity where applicable (F-01.3)
- [ ] Partner's differentiating value-add is named (F-01.4)
- [ ] All `key_messages` are incorporated in priority order
- [ ] No confirmed banned terms remain in Headline, Body Copy, or CTA
- [ ] CTA is specific and does not use vague language
- [ ] Confidence Note addresses gaps, placeholders, review flags, and terminology audit
- [ ] Terminology audit block is present (even if all lists are empty)
- [ ] Output format matches `output_format` from the brief
- [ ] `partner_name` from the brief is used, or `[PARTNER_NAME]` is listed in `unresolved_placeholders`

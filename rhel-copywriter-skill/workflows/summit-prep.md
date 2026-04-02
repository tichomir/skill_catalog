# Workflow: Summit Prep Pipeline
_Workflow ID: WF-SUMMIT-001 | Version: 1.0.0 | Status: Active_
_Triggered by: `content_type: summit_prep` in input brief_
_Input schema: [`../templates/copy-brief.md`](../templates/copy-brief.md)_
_Standards: [`../../references/brand-and-tone-notes.md`](../../references/brand-and-tone-notes.md) · [`../../references/audience-profiles.md`](../../references/audience-profiles.md) · [`../../references/placeholders-to-replace.md`](../../references/placeholders-to-replace.md)_

---

## Purpose

This workflow implements the Summit Prep Pipeline: a single execution that accepts a
completed copy brief and produces three sequential, labelled output blocks — a partner
value proposition, a Before You Go slide narrative, and an announcement blurb — in a
single pipeline run.

Use this workflow when a PMM or partner marketing team needs a complete set of Summit
content for a specific partner and Red Hat product or initiative. All three outputs
share the same input brief and must be internally consistent in messaging, tone, and
partner framing.

**Output summary:**
| Output | Label | Primary use |
|---|---|---|
| 1 | Partner Value Proposition | Partner-facing deck slide or enablement page |
| 2 | Before You Go Slide Narrative | Summit session or booth "Before You Go" slide body text |
| 3 | Announcement Blurb | Event listing, email announcement, or social preview |

---

## Pre-conditions

Before executing any step, confirm:
1. The input brief has passed validation per `SKILL.md` Section 4
2. All required fields are present: `content_type`, `audience`, `product_or_initiative`,
   `key_messages`, `tone_variant`, `output_format`
3. `content_type` equals `summit_prep`

If `partner_name` is absent, insert `[PARTNER_NAME]` at every partner reference point
in all three outputs and list it in `unresolved_placeholders`. Do not invent a partner name.

---

## Pipeline Steps

Execute the steps below **in order**. Complete each step fully before moving to the next.
Do not combine steps or skip ahead.

---

### STEP 1 — Load Standards References

Before generating any copy, load and internalise the following reference files. Apply
their rules throughout all three outputs. Do not embed their content in the output.

| File | What to apply |
|---|---|
| [`../../references/brand-and-tone-notes.md`](../../references/brand-and-tone-notes.md) | Voice pillars (bold, clear, human, open); partner-first framing rules (Section 4); banned terms list (Section 3); approved term list (Section 2) |
| [`../../references/audience-profiles.md`](../../references/audience-profiles.md) | Select the profile matching the `audience` field; apply its tone variant, vocabulary guidance, and copy do's/don'ts throughout |
| [`../../references/placeholders-to-replace.md`](../../references/placeholders-to-replace.md) | Internalise the full placeholder registry; flag any unresolved placeholders in the Confidence Note of each output |

---

### STEP 2 — Generate Output 1: Partner Value Proposition

**Objective:** Produce a standalone partner value proposition that can be used on a
partner enablement page or as a deck slide.

**Partner-first framing (F-01, F-02):**
Apply the partner-first framing rules from `references/brand-and-tone-notes.md` Section 4:
- Lead with the partner's benefit or customer outcome — not Red Hat's product feature
- Name the co-sell motion explicitly (resell, co-sell, managed service, OEM)
- Frame Red Hat certification as partner equity: the partner inherits Red Hat's open
  source trust signal
- Do not position Red Hat as a competitor to the partner's value-add

**Structure:** Produce all four output sections as defined in `SKILL.md` Section 6.1:

**Headline:**
- ≤ 12 words
- Leads with the partner or customer outcome (F-02)
- Does not open with "Red Hat" or a product name
- Pattern: _"[Customer outcome] — [partner name] delivers on [Red Hat platform]"_

**Body Copy:**
- Apply the `output_format` from the brief (`prose`, `bullets`, or `slide-ready`)
- Incorporate `key_messages` in priority order (index 0 first and most prominent)
- Default length: 150–300 words (Body Copy). Apply `word_limit` override if provided (±10%)
- Apply partner-first framing throughout: partner outcome leads each paragraph or bullet
- Use the audience register from `references/audience-profiles.md` for the stated `audience`
- Apply the `tone_variant` from the brief throughout

**CTA:**
- Single, specific call to action
- Names the co-sell motion or next step explicitly
- Avoids vague language: not "learn more", not "find out more"
- Example patterns:
  - _"Contact [PARTNER_NAME] to schedule a co-sell discovery call."_
  - _"Visit the Red Hat Partner Connect listing for [PARTNER_NAME] to explore joint
    opportunities."_

**Confidence Note:**
- 1–3 sentences
- Identify: (a) any gap in `key_messages` specificity (missing metrics, vague claims),
  (b) any unresolved `[PLACEHOLDER]` strings, (c) any claims requiring PMM or legal
  review before external use, (d) terminology audit summary for this output only

---

### STEP 3 — Generate Output 2: Before You Go Slide Narrative

**Objective:** Produce the body text for a "Before You Go" Summit session or booth slide.
This is the content a partner or Red Hat presenter reads aloud or the attendee reads as
they leave the session — it must be scannable, memorable, and action-oriented.

**Framing:** Apply partner-first framing (F-01, F-02) — the attendee should leave with a
clear sense of what the partner offers, not just what Red Hat sells. The narrative should
feel like a direct handoff from the session to the partner's next conversation.

**Structure:** Produce all four output sections:

**Headline:**
- ≤ 12 words
- A takeaway statement — what the attendee should remember above all else
- Future-oriented or action-oriented phrasing preferred
- Example: _"Your next Kubernetes deployment doesn't have to start from scratch."_

**Body Copy:**
- Apply the `output_format` from the brief (`prose`, `bullets`, or `slide-ready`)
- **For `slide-ready` format:** 3–5 short labelled blocks, each with a 2–4 word label
  and 1–2 sentences. Optimised for projection readability. Short words; no jargon.
- **For `bullets` format:** 4–6 bullets; each bullet is a specific takeaway or next step
- **For `prose` format:** 2–3 short paragraphs; lead with the key takeaway; close with
  the partner's differentiated offer
- Default length: 100–200 words (Body Copy). Apply `word_limit` override if provided (±10%)
- References `key_messages` — draw on the 1–2 highest-priority messages (index 0 and 1)
- Apply the `tone_variant` from the brief; `conversational` is strongly recommended for
  Before You Go content regardless of the brief value — if the brief specifies a different
  variant, apply it but note the preference in the Confidence Note

**CTA:**
- Single, specific next step the attendee can take immediately after the session
- Must reference either the partner or the Red Hat action (not both in the same CTA)
- Examples:
  - _"Speak to the [PARTNER_NAME] team at stand B-12 to book a 30-minute scoping call."_
  - _"Scan the QR code to download the [PARTNER_NAME] + Red Hat joint solution brief."_

**Confidence Note:**
- 1–3 sentences
- Note: (a) whether `conversational` tone was overridden by the brief's `tone_variant`,
  (b) any unresolved `[PLACEHOLDER]` strings (e.g. stand number, QR code target),
  (c) any claims in the body requiring PMM or legal review, (d) terminology audit summary
  for this output only

---

### STEP 4 — Generate Output 3: Announcement Blurb

**Objective:** Produce a short announcement blurb suitable for event listings, email
previews, or social media announcement posts (not individual social posts — this is an
editorial blurb, not a tweet).

**Framing:** This blurb will often be the first touchpoint a reader has with the Summit
content. It must create enough interest to drive action (registration, attendance, or
follow-up) without disclosing all key messages. Apply partner-first framing (F-01, F-02):
the partner's name and differentiated offer should appear in the first sentence.

**Structure:** Produce all four output sections:

**Headline:**
- ≤ 12 words
- Compelling event or announcement frame; includes the partner name or partner outcome
- Avoids generic Summit language: not "Join us at Summit", not "Don't miss this session"

**Body Copy:**
- Apply the `output_format` from the brief
- **For `slide-ready` or `bullets`:** 3–5 bullets or blocks highlighting the session/event
  value for the stated audience
- **For `prose`:** 2–3 sentences. Hook → value proposition → call to act. No padding.
- Default length: 75–150 words (Body Copy). Apply `word_limit` override if provided (±10%)
- Incorporates the highest-priority `key_message` (index 0) as the value hook
- Applies the `tone_variant` from the brief; for announcements, `conversational` or
  `standard` are most appropriate — note a mismatch in the Confidence Note if the brief
  specifies `technical` or `executive`

**CTA:**
- Single, specific action: register, visit, book, scan, download
- Avoids vague language: not "find out more"
- If an event URL or registration link is not in the brief, use `[EVENT_URL]` placeholder
  and flag it in the Confidence Note

**Confidence Note:**
- 1–3 sentences
- Note: (a) any tension between the announcement register and the requested `tone_variant`,
  (b) any `[PLACEHOLDER]` strings (especially `[EVENT_URL]`, `[PARTNER_NAME]`, event date),
  (c) whether the blurb should be reviewed by the co-marketing team before distribution,
  (d) terminology audit summary for this output only

---

### STEP 5 — Run Terminology Audit (All Three Outputs Combined)

After all three outputs are drafted, run a single combined terminology audit.

**Procedure:**
1. Scan all three output blocks (Headline + Body Copy + CTA sections of each) against:
   - Banned terms list: `references/brand-and-tone-notes.md` Section 3
   - Full terminology list: `standards/terminology-list.md`
2. For each **confirmed banned term** found: replace it in the draft; record in
   `banned_terms_replaced`. Use case-insensitive, whole-word boundary matching.
   Morphological variants listed in the terminology file are treated as matching their
   root banned term. Set `action_taken: replaced`.
3. For each **context-dependent potential violation** (e.g., incorrect product name
   variant requiring human judgement): record in `flagged_for_review`; the term may remain
   in the draft pending review. Set `action_taken: flagged_for_review`.
4. Scan all three outputs against `references/placeholders-to-replace.md`. Add any
   unresolved placeholder strings to `unresolved_placeholders`.

**The terminology audit block is always present in the output envelope**, even when no
terms are flagged. `banned_terms_replaced`, `flagged_for_review`, and
`unresolved_placeholders` are empty lists — never omitted (AC-06).

---

### STEP 6 — Assemble and Return Output

Assemble the complete output envelope as specified in `SKILL.md` Section 6.2:

```
SKILL OUTPUT — Red Hat Copywriter Skill v1.0.0
content_type: summit_prep
audience: <from brief>
tone_variant: <from brief>
output_format: <from brief>
partner_name: <from brief, or "[PARTNER_NAME] — unresolved">
standards_ref_version: BT-2026-Q2
terminology_version: TERM-2026-Q2
generated_at: <ISO 8601 timestamp>

---

OUTPUT 1: Partner Value Proposition

## Headline
<headline text>

## Body Copy
<body copy>

## CTA
<CTA text>

## Confidence Note
<confidence note>

---

OUTPUT 2: Before You Go Slide Narrative

## Headline
<headline text>

## Body Copy
<body copy>

## CTA
<CTA text>

## Confidence Note
<confidence note>

---

OUTPUT 3: Announcement Blurb

## Headline
<headline text>

## Body Copy
<body copy>

## CTA
<CTA text>

## Confidence Note
<confidence note>

---

TERMINOLOGY AUDIT (all three outputs)
banned_terms_replaced: [<terms replaced across all outputs>]
flagged_for_review: [<terms flagged across all outputs>]
unresolved_placeholders: [<placeholder strings not resolved from brief>]
```

---

## Default Length Reference

| Output | Default Body Copy length | With `word_limit` override |
|---|---|---|
| Partner Value Proposition | 150–300 words | `word_limit` value ±10% |
| Before You Go Narrative | 100–200 words | `word_limit` value ±10% |
| Announcement Blurb | 75–150 words | `word_limit` value ±10% |

When `word_limit` is provided in the brief, apply it as the target for Body Copy across
all three outputs equally, unless that length is inappropriate for a given output type
(e.g., a 500-word blurb). If the override conflicts with the output type's purpose, apply
it to Output 1 (Partner Value Proposition) and note the conflict in the Confidence Notes
for Outputs 2 and 3.

---

## Quality Checklist

Before returning output, verify:

- [ ] All three outputs are present and labelled
- [ ] Every output contains all four sections: Headline, Body Copy, CTA, Confidence Note
- [ ] Headline of each output is ≤ 12 words and leads with a partner or customer outcome
- [ ] Partner-first framing applied throughout: partner benefit leads every Body Copy section
- [ ] Co-sell motion named explicitly in at least one output (preferably Output 1)
- [ ] `key_messages` index 0 is the most prominent message in Output 1
- [ ] No confirmed banned terms remain in any output
- [ ] No content from `references/` files is embedded verbatim in any output
- [ ] Terminology audit block is present with correct version stamps
- [ ] All unresolved `[PLACEHOLDER]` strings are listed in `unresolved_placeholders`
- [ ] Each Confidence Note addresses gaps, review flags, and the terminology audit result

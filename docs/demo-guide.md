# Red Hat Copywriter Skill — Demo Guide
_Version: 1.1.0 | For: Live demonstrations and onboarding walkthroughs_

---

## What This Guide Covers

This guide walks you through two live demonstrations of the Red Hat Copywriter Skill:

1. **Demo A — Partner Value Proposition** (3 minutes): single output, easiest entry point
2. **Demo B — Summit Prep Pipeline** (5 minutes): three-output pipeline, the flagship use case

Each demo includes a ready-to-paste brief, the expected output structure, and talking
points explaining what the skill is doing at each step.

---

## Prerequisites

The skill must be installed and the slash command registered. Verify with:

```
/rhel-copywriter
```

If the skill loads and asks for a brief, you're ready. If it does not respond, see
`docs/installation-verification-checklist.md`.

---

## Demo A — Partner Value Proposition (Quick Win)

**Goal:** Show the audience how a 30-second brief produces a structured, brand-compliant
output block ready for a partner enablement one-pager.

### Step 1 — Invoke the skill

```
/rhel-copywriter
```

> **Talking point:** "The skill is invoked like any Claude Code slash command — one
> command, no configuration required. It loads the entry point from `skill.md` and waits
> for a YAML brief."

### Step 2 — Paste this brief

```yaml
content_type: partner_value_prop
audience: partner_sales
product_or_initiative: Red Hat OpenShift Container Platform
partner_name: Infosys
key_messages:
  - Infosys's managed OpenShift service gives enterprise customers a fully operated
    Kubernetes platform without building internal SRE capability from scratch.
  - Infosys customers running Red Hat OpenShift Container Platform report a 40%
    reduction in time-to-production for new applications (Red Hat Customer Survey, 2025).
  - As a Red Hat Certified Partner, Infosys delivers solutions built on a platform
    certified across FIPS 140-2, OCI, and CNCF Kubernetes conformance standards.
tone_variant: standard
output_format: bullets
```

> **Talking point:** "This is the entire input. No conversation back-and-forth — just a
> structured brief. Every field is documented in `templates/copy-brief.md` with inline
> guidance on valid values."

### Step 3 — Point out the output structure

The skill returns a block with this envelope:

```
SKILL OUTPUT — Red Hat Copywriter Skill v1.1.0
content_type: partner_value_prop
audience: partner_sales
...
```

Followed by four sections: **Headline**, **Body Copy**, **CTA**, and **Confidence Note**.
Then a **TERMINOLOGY AUDIT** block.

> **Talking points:**
> - "The Headline always leads with the partner outcome, not a Red Hat product name —
>   that's the F-02 rule enforced automatically."
> - "The Confidence Note is addressed to the PMM reviewer, not the end audience. It flags
>   anything that needs human sign-off — metrics requiring legal clearance, unresolved
>   placeholders, or thin brief sections."
> - "The Terminology Audit shows exactly what was replaced and what was flagged. If
>   `banned_terms_replaced` is empty, the brief was already clean."

### Step 4 — Show the validation safety net (optional)

Submit a brief with `audience` removed:

```yaml
content_type: partner_value_prop
product_or_initiative: Red Hat Ansible Automation Platform
key_messages:
  - Ansible reduces manual remediation tasks by 60%.
tone_variant: standard
output_format: bullets
```

The skill returns a validation error — not draft copy:

```
VALIDATION ERROR — Red Hat Copywriter Skill v1.1.0

validation_errors:
  - field: audience
    code: required_field_missing
    message: ...
```

> **Talking point:** "The skill refuses to generate copy until the brief is valid.
> Validation is exhaustive — it collects all missing fields and reports them at once
> rather than aborting on the first error."

---

## Demo B — Summit Prep Pipeline (Flagship Use Case)

**Goal:** Show the three-output Summit pipeline: partner value prop + Before You Go
narrative + announcement blurb — all from one brief, in one run.

### Step 1 — Invoke the skill

```
/rhel-copywriter
```

### Step 2 — Paste this brief

```yaml
content_type: summit_prep
audience: partner_sales
product_or_initiative: Red Hat Ansible Automation Platform
partner_name: DXC Technology
key_messages:
  - DXC's automation practice, built on Red Hat Ansible Automation Platform, reduces
    manual remediation tasks by an average of 60% in the first 90 days of deployment.
  - DXC and Red Hat co-sell a managed automation service that includes onboarding,
    playbook development, and 24x7 operational support.
  - Red Hat Ansible Automation Platform is certified for use in regulated industries,
    including financial services and government sectors.
tone_variant: conversational
output_format: slide-ready
event_metadata:
  event_name: Red Hat Summit 2026
  event_date: "2026-05-06/2026-05-08"
  event_location: Boston, MA
  booth_reference: Booth H3-420
```

> **Talking point:** "The `event_metadata` block is new in v1.1. Before this, operators
> had to search-and-replace `[BOOTH_REFERENCE]` and event dates manually after generation.
> Now the skill substitutes the confirmed values directly into the Before You Go narrative
> and announcement blurb."

### Step 3 — Walk through the three outputs

The skill returns three labelled output blocks:

**OUTPUT 1 — Partner Value Proposition**
> "This is the same structure as Demo A — a standalone value prop for DXC's automation
> practice. You'd put this on the partner enablement page or co-sell one-pager."

**OUTPUT 2 — Before You Go Slide Narrative**
> "This is the Summit-specific output. It's a short narrative for the Before You Go slide
> in the partner deck — the one that appears in the DXC pre-Summit readout to tell the
> sales team what to say when a customer asks why they should visit the Red Hat booth."

**OUTPUT 3 — Announcement Blurb**
> "This is a short blurb for the Summit announcement email or social post. Notice how the
> event date, location, and booth number are resolved — the `[BOOTH_REFERENCE]` placeholder
> has been replaced with 'Booth H3-420' because we provided `event_metadata`."

### Step 4 — Show the tone conflict advisory

Resubmit with `tone_variant: executive` and `content_type: summit_prep`:

> **Talking point:** "When `executive` tone is applied to a Summit Prep brief, the skill
> adds an advisory in the Confidence Note for Output 2. It doesn't override your choice —
> it flags that a `conversational` variant might warm up the Before You Go slide. The
> operator decides."

---

## What to Highlight Across Both Demos

| Feature | Where to show it |
|---|---|
| Partner-first framing (F-01, F-02) | Point to the Headline in any output — partner outcome appears before any Red Hat product name |
| Exhaustive validation (AC-05) | Demo A Step 4 — submit a brief missing two fields, show all errors returned at once |
| Terminology audit | The `TERMINOLOGY AUDIT` block at the end of every output |
| Standards decoupling (AC-06) | `standards_ref_version: BT-2026-Q2` in the output envelope — updating references/ does not change skill logic |
| Event metadata substitution | Demo B — booth reference and dates substituted into Outputs 2 and 3 |
| Confidence Note for PMM review | Point to it in any output — addresses gaps, flags review items, confirms placeholder status |

---

## Sample Output Reference

A complete pilot output is at `docs/pilot/pilot-output.md` (IBM / OpenShift `summit_prep`
run from Sprint 6). Use it to show the audience what a full run looks like before
running a live demo.

---

## Common Questions

**Q: Can I change the tone after seeing the output?**
Resubmit the brief with a different `tone_variant`. Each run is independent — the skill
does not maintain state between invocations.

**Q: What if I don't know the booth number yet?**
Omit `booth_reference` from `event_metadata` (or omit `event_metadata` entirely). The
skill inserts `[BOOTH_REFERENCE]` and lists it in `unresolved_placeholders`. Fill it in
before distribution.

**Q: Can I get output in Portuguese for the LatAm team?**
Set `language: pt-BR` in the brief. The skill accepts it and generates English output
with a Confidence Note advisory that localisation is not yet available. See
`docs/localisation-roadmap.md` — pt-BR is the priority-1 target for the next version.

**Q: Where do the brand rules come from?**
`references/brand-and-tone-notes.md` (version `BT-2026-Q2`). These files are decoupled
from the skill logic — the PMM team can update brand guidance without touching `skill.md`.

---

_See `docs/installation-verification-checklist.md` for installation steps._
_See `docs/contribution-guide.md` to add new content types or workflows._

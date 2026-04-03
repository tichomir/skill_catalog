# Red Hat Copywriter Skill — Demo Guide
_Version: 1.0 | Audience: Product owner, PMM, GTM Lead — live demonstrations and onboarding_

---

## Overview

This guide lets you demonstrate the Red Hat Copywriter Skill end-to-end without needing to
understand the internal implementation. Four scripted scenarios are included:

| # | Scenario | Time | Pilot use case (PRD §10) |
|---|---|---|---|
| 1 | Partner Value Proposition | ~3 min | Ecosystem track — partner value prop |
| 2 | Before You Go Slide Narrative | ~4 min | Summit prep — Before You Go narrative |
| 3 | Announcement Blurb | ~4 min | Summit prep — announcement blurb |
| 4 | Negative demo — missing required field | ~2 min | Clarification-request behaviour (AC-04, AC-05) |

---

## Prerequisites

### 1. Repository and Claude Code CLI

```bash
# Clone the repository (or ensure you have a local copy)
git clone https://github.com/redhat-ai-skills/skills.git
cd skills

# Verify Claude Code CLI is installed (v1.x or later required)
claude --version
```

### 2. Install the slash command

The slash command file must be present at `.claude/commands/copywriter/rhel-copywriter.md`
in the repository root. Verify:

```bash
ls .claude/commands/copywriter/rhel-copywriter.md
```

If the file is missing, see `docs/installation-verification-checklist.md` (checks C1–C2).

### 3. Confirm the skill loads

Open Claude Code in the repository root and run:

```
/rhel-copywriter
```

If the skill loads and requests a YAML brief, you are ready. If there is no response, run
through the full checklist at `docs/installation-verification-checklist.md` before proceeding.

### 4. Optional — MCP server

For the MCP invocation path:

```bash
node .claude/mcp-servers/rhel-copywriter-server.js
```

The server should start without error. This is only needed for the MCP integration path;
the slash command works without it.

---

## Scenario 1 — Partner Value Proposition

**Goal:** Show how a structured 30-second brief produces a brand-compliant, partner-first
output block ready for a partner enablement one-pager.

**Pilot use case:** PRD Section 10 — partner value proposition for the ecosystem track.

### Step 1 — Invoke the skill

```
/rhel-copywriter
```

> **What to highlight:** "The skill is invoked like any Claude Code slash command — one
> command, no configuration required. It reads `skill.md` and waits for a YAML brief.
> There is no conversation back-and-forth until after you submit the brief."

### Step 2 — Paste this brief

```yaml
content_type: partner_value_prop
audience: partner_sales
product_or_initiative: Red Hat OpenShift Container Platform
partner_name: Wipro
key_messages:
  - Wipro's managed container platform service, built on Red Hat OpenShift Container
    Platform, gives enterprise customers a fully operated Kubernetes environment with
    99.9% uptime SLA and dedicated SRE support — without building internal platform
    engineering capability from scratch.
  - Wipro customers running Red Hat OpenShift Container Platform report a 35% reduction
    in application deployment cycle time within six months of production rollout
    (Wipro Engineering Benchmark Report, 2025).
  - As a Red Hat Certified Partner, Wipro delivers solutions certified across OCI,
    FIPS 140-2, and CNCF Kubernetes conformance standards, ensuring compatibility
    with regulated enterprise environments.
  - Wipro and Red Hat co-sell a managed OpenShift service through the Red Hat
    Co-Sell Ready programme, combining Wipro's managed services wrapper and
    migration expertise with Red Hat's platform SLA and upstream support.
tone_variant: standard
output_format: bullets
word_limit: 250
```

> **What to highlight:** "This is the entire input — a YAML brief. Every field is
> documented in `rhel-copywriter-skill/templates/copy-brief.md`. The four key messages
> mirror what the sales team would say on a call; the skill turns them into structured copy."

### Step 3 — Point out the output structure

The skill returns a structured envelope followed by four labelled sections:

```
SKILL OUTPUT — Red Hat Copywriter Skill v1.1.0
content_type: partner_value_prop
audience: partner_sales
...
standards_ref_version: BT-2026-Q2
```

Then:

| Section | What to point out |
|---|---|
| **Headline** | Leads with the Wipro/customer outcome — never with "Red Hat". This is F-02 enforced automatically. |
| **Body Copy** | Bullets in priority order, matching `key_messages` index order. Each bullet states one specific claim. |
| **CTA** | Specific action — not "learn more". Names the co-sell motion explicitly (F-01.2). |
| **Confidence Note** | Addressed to the PMM reviewer. Flags anything needing sign-off — legal-sensitive metrics, thin brief sections, placeholder status. |

Then the **TERMINOLOGY AUDIT** block:

> **What to highlight:** "The audit shows exactly what was replaced and what was flagged.
> `banned_terms_replaced` being empty means the brief was already clean. This block is
> always present — even when there is nothing to flag (AC-06 requirement)."

> **AC reference:** This output demonstrates **AC-01** (brand voice compliance),
> **AC-02** (banned terms absent), and **AC-06** (terminology audit present and accurate).

---

## Scenario 2 — Before You Go Slide Narrative

**Goal:** Show the Summit prep pipeline targeting the Before You Go slide narrative —
the output most directly useful to a partner sales team before a Summit session.

**Pilot use case:** PRD Section 10 — Before You Go slide narrative for partner slides.

### Step 1 — Invoke the skill

```
/rhel-copywriter
```

### Step 2 — Paste this brief

```yaml
content_type: summit_prep
audience: business_executive
product_or_initiative: Red Hat Enterprise Linux
partner_name: Accenture
key_messages:
  - Accenture's Red Hat Enterprise Linux migration service reduces operating system
    total cost of ownership by an average of 28% over three years compared with
    incumbent virtualisation platforms, based on Accenture client engagements
    across financial services and public sector (Accenture Case Study Digest, 2025).
  - Accenture delivers Red Hat Enterprise Linux as a fully managed, subscription-based
    service through the Red Hat Embedded Partner Programme, giving customers a
    predictable cost model with no hidden licensing fees.
  - Red Hat Enterprise Linux is the operating system foundation for 90% of Fortune 500
    companies running mission-critical workloads, providing Accenture customers with
    a platform that carries proven enterprise-grade reliability.
tone_variant: executive
output_format: slide-ready
word_limit: 180
```

> **What to highlight:** "`content_type: summit_prep` triggers the three-output pipeline.
> One brief, one run, three outputs. The `output_format: slide-ready` setting produces
> short labelled blocks suitable for pasting directly into PowerPoint."

### Step 3 — Walk through the three outputs

**OUTPUT 1 — Partner Value Proposition**

> "This is the standalone Accenture value prop — same structure as Scenario 1. You would
> put this on the partner enablement page or co-sell one-pager."

**OUTPUT 2 — Before You Go Slide Narrative**

> "This is the Summit-specific output. It's the narrative for the Before You Go slide in
> the partner deck — what you say when a customer asks why they should visit the Red Hat
> booth. Notice the `slide-ready` format: short labelled blocks, not flowing prose."

**OUTPUT 3 — Announcement Blurb**

> "Short blurb for the Summit announcement email or social post. If `event_metadata` had
> been included in the brief, the event name, date, location, and booth reference would
> be substituted in here automatically."

> **What to highlight:** "The tone advisory in the Confidence Note for Output 2 — when
> `tone_variant: executive` is applied to a summit_prep brief, the skill flags that a
> `conversational` variant might produce warmer in-session impact. It doesn't override
> your choice; it advises. This is the PMM check-in built into every run. References
> **AC-01** (brand voice) and **AC-04** (routing correctness: executive tone
> advisory triggered correctly for summit_prep)."

---

## Scenario 3 — Announcement Blurb

**Goal:** Show the announcement blurb output for a new integration launching at Summit,
using the `event_metadata` field to substitute confirmed event details.

**Pilot use case:** PRD Section 10 — announcement blurb for a new integration.

### Step 1 — Invoke the skill

```
/rhel-copywriter
```

### Step 2 — Paste this brief

```yaml
content_type: summit_prep
audience: technical_decision_maker
product_or_initiative: Red Hat Ansible Automation Platform
partner_name: DXC Technology
key_messages:
  - DXC Technology's new Hybrid Cloud Automation Accelerator, launching at Red Hat Summit
    2026, integrates directly with Red Hat Ansible Automation Platform to deliver
    pre-built automation playbooks for SAP, VMware migration, and network infrastructure
    provisioning — reducing automation onboarding time from weeks to hours.
  - DXC and Red Hat co-develop the Hybrid Cloud Automation Accelerator as a jointly
    validated solution under the Red Hat Co-Sell Ready programme, with a shared
    go-to-market motion covering North America and EMEA from Q2 2026.
  - Red Hat Ansible Automation Platform is certified for use in regulated industries
    including financial services, government, and healthcare, enabling DXC customers
    to automate compliance-sensitive workloads without additional validation overhead.
tone_variant: conversational
output_format: slide-ready
word_limit: 160
event_metadata:
  event_name: Red Hat Summit 2026
  event_date: "2026-05-06/2026-05-08"
  event_location: Boston, MA
  booth_reference: Booth H3-420
```

> **What to highlight:** "The `event_metadata` block provides the confirmed booth
> reference, event dates, and location. The skill substitutes these values directly into
> Output 2 (Before You Go narrative) and Output 3 (announcement blurb), replacing
> `[BOOTH_REFERENCE]` and `[EVENT_DATE]` placeholders automatically. Without this block
> the placeholders would appear in the output and be listed in `unresolved_placeholders`."

### Step 3 — Focus on Output 3 — Announcement Blurb

> **What to highlight:**
> - "The `[BOOTH_REFERENCE]` placeholder has been replaced with 'Booth H3-420' because we
>   provided `event_metadata.booth_reference`."
> - "The announcement blurb is `slide-ready` format — short labelled blocks, easy to paste
>   into an email header or slide."
> - "The TERMINOLOGY AUDIT at the bottom confirms the `conversational` tone didn't
>   introduce any banned phrasing — `banned_terms_replaced` and `flagged_for_review` are
>   both empty."

> **AC reference:** Demonstrates **AC-03** (approved product names correct: 'Red Hat Ansible
> Automation Platform' used exactly), **AC-06** (terminology audit present; version stamp
> `standards_ref_version: BT-2026-Q2` and `terminology_version: TERM-2026-Q2` visible in
> the output envelope).

---

## Scenario 4 — Negative Demo: Missing Required Field (Clarification Request)

**Goal:** Show that the skill refuses to generate copy when a required brief field is
absent, and returns an actionable structured validation error instead.

**AC reference:** **AC-04** (clarification-request behaviour) and **AC-05** (schema
validation — exhaustive, no early abort).

### Step 1 — Invoke the skill

```
/rhel-copywriter
```

### Step 2 — Paste this intentionally incomplete brief

```yaml
content_type: partner_value_prop
product_or_initiative: Red Hat Ansible Automation Platform
key_messages:
  - Ansible reduces manual remediation tasks by 60%.
tone_variant: standard
output_format: bullets
```

**What is missing:** `audience` — a required field. The brief has no `audience` value.

> **What to highlight:** "There is no `audience` field. The skill has no way to calibrate
> tone and register — it must ask rather than guess."

### Step 3 — Show the validation error response

The skill returns a validation error — **not** a content draft:

```
VALIDATION ERROR — Red Hat Copywriter Skill v1.1.0

validation_errors:
  - field: audience
    code: required_field_missing
    message: "audience is required. Provide one of: technical_decision_maker,
              business_executive, partner_sales."
    valid_values:
      - technical_decision_maker
      - business_executive
      - partner_sales

generated_at: <ISO 8601 timestamp>
```

> **What to highlight:**
> - "The skill returns a structured error, not draft copy. AC-04: clarification-request
>   behaviour is triggered correctly."
> - "The error message is actionable — it tells you exactly what values are valid. You
>   don't need to look up the schema."
> - "The `generated_at` timestamp is present even in error responses — useful for QA audit
>   trails."

### Step 4 — Optional: show multi-field exhaustive validation

Add a second error to the same brief by changing `content_type` to an invalid value:

```yaml
content_type: whitepaper
product_or_initiative: Red Hat Ansible Automation Platform
key_messages:
  - Ansible reduces manual remediation tasks by 60%.
tone_variant: standard
output_format: bullets
```

Expected response — **both** errors in a single response (AC-05, no early abort):

```
VALIDATION ERROR — Red Hat Copywriter Skill v1.1.0

validation_errors:
  - field: content_type
    code: invalid_enum_value
    message: "content_type 'whitepaper' is not a valid value."
    valid_values:
      - partner_value_prop
      - summit_prep
  - field: audience
    code: required_field_missing
    message: "audience is required. Provide one of: technical_decision_maker,
              business_executive, partner_sales."
    valid_values:
      - technical_decision_maker
      - business_executive
      - partner_sales
```

> **What to highlight:** "Two fields broken — two errors in a single response.
> The skill does not abort after detecting the first error. This is AC-05: exhaustive
> validation. Operators fix all problems in one round-trip, not one at a time."

---

## Cross-Scenario Summary: What to Highlight

| Feature | Where to show it | AC |
|---|---|---|
| Partner-first framing | Headline in any output — partner outcome before Red Hat product name | F-01, F-02 |
| Terminology audit block | End of every output — always present, even when empty | AC-06 |
| Standards version stamp | `standards_ref_version: BT-2026-Q2` in output envelope | AC-06 |
| Confidence Note for PMM | Every output — gaps, review flags, placeholder status | AC-01 |
| Clarification request | Scenario 4 — structured error, no draft produced | AC-04 |
| Exhaustive validation | Scenario 4 step 4 — all errors in one response, no early abort | AC-05 |
| Event metadata substitution | Scenario 3 — booth reference and dates substituted into Outputs 2 and 3 | AC-03 |
| Routing correctness | Scenario 2 — executive tone advisory triggered for summit_prep | AC-04 |

---

## Common Questions

**Q: Can I change the tone after seeing the output?**
Resubmit the brief with a different `tone_variant`. Each run is stateless — the skill
does not retain context between invocations.

**Q: What if I don't know the booth number yet?**
Omit `booth_reference` from `event_metadata` (or omit the block entirely). The skill
inserts `[BOOTH_REFERENCE]` and lists it in `unresolved_placeholders`. Fill it in before
distribution.

**Q: Can I request output in Portuguese for the LatAm team?**
Add `language: pt-BR` to the brief. The skill accepts the field for future compatibility
but generates English output and includes a Confidence Note advisory. See
`docs/localisation-roadmap.md` — pt-BR is the priority-1 target for the next version.

**Q: Where do the brand rules come from?**
`references/brand-and-tone-notes.md` (version `BT-2026-Q2`). These files are decoupled
from skill logic — the PMM team can update brand guidance without touching `skill.md`
(AC-06).

**Q: What is the sample pilot output I can show before a live run?**
A full pilot run output is at `docs/pilot/pilot-output.md` (IBM / OpenShift `summit_prep`
run from Sprint 6). Use it as a reference during setup or if the live run is unavailable.

---

## Related Documents

- Installation checklist: `docs/installation-verification-checklist.md`
- Acceptance criteria matrix: `rhel-copywriter-skill/docs/acceptance-criteria-matrix.md`
- Pilot run output: `docs/pilot/pilot-output.md`
- Contribution guide: `docs/contribution-guide.md`
- Localisation roadmap: `docs/localisation-roadmap.md`

---

_Skill version: 1.1.0 | Standards: BT-2026-Q2 | Terminology: TERM-2026-Q2_

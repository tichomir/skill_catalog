# Copy Brief Schema — Red Hat Copywriter Skill
_Schema version: 1.0.0 | Matches SKILL.md v1.0.0 | PRD: PRD-RHCW-001 v0.1 Section 6_
_Submit a completed YAML block in this format to the skill. Fields marked REQUIRED must_
_be present and non-empty. Fields marked OPTIONAL may be omitted._

---

## How to Use

Copy the YAML block below, fill in all REQUIRED fields, and submit it to the skill.
The skill validates the brief before generating any output. If any required field is
missing or contains an invalid value, the skill returns a validation error listing every
invalid field — it does not generate copy until the brief is valid.

---

## Input Brief Schema

```yaml
# ──────────────────────────────────────────────────────────────────────────────
# FIELD: content_type
# REQUIRED
# Description: Determines which workflow the skill invokes to generate output.
#   partner_value_prop — Standalone partner value proposition.
#                        Single output block (Headline, Body Copy, CTA,
#                        Confidence Note). Best for partner enablement pages,
#                        co-sell one-pagers, and partner deck slides.
#   summit_prep        — Full Summit pipeline. Produces three sequential outputs
#                        in one run: (1) partner value proposition,
#                        (2) Before You Go slide narrative,
#                        (3) announcement blurb. Use this when preparing
#                        a complete Summit content package for a partner.
# Valid enum values: partner_value_prop | summit_prep
# ──────────────────────────────────────────────────────────────────────────────
content_type: partner_value_prop  # REQUIRED — replace with your chosen content type

# ──────────────────────────────────────────────────────────────────────────────
# FIELD: audience
# REQUIRED
# Description: The primary audience for the generated copy. The skill selects
#   the appropriate tone register, vocabulary, and assumed-knowledge level based
#   on this value. Consult references/audience-profiles.md for the full profile
#   of each segment before completing this field.
#
#   technical_decision_maker — IT architects, enterprise architects, platform
#     engineers, DevOps leads, CTOs (technical framing). Expects technical
#     precision, standards references, and specificity about integration depth.
#   business_executive — C-suite, CFO, COO, VP of IT, board-level stakeholders.
#     Expects business outcomes, ROI framing, risk language; minimal technical
#     detail in the lead copy.
#   partner_sales — Channel partners, ISV partners, GSI partners, resellers,
#     co-sell partner SEs and account managers. Expects partner-commercial
#     framing, co-sell motion clarity, and customer conversation hooks.
#
# Valid enum values: technical_decision_maker | business_executive | partner_sales
# ──────────────────────────────────────────────────────────────────────────────
audience: partner_sales  # REQUIRED — replace with your target audience

# ──────────────────────────────────────────────────────────────────────────────
# FIELD: product_or_initiative
# REQUIRED
# Description: The Red Hat product, product portfolio, or joint initiative that
#   is the subject of the copy. Use the approved product name on first reference
#   (see references/brand-and-tone-notes.md Section 2 for approved names and
#   abbreviation rules). For joint initiatives with a partner, name both the
#   partner offering and the underlying Red Hat product.
#
#   Examples:
#     "Red Hat OpenShift Container Platform"
#     "Red Hat Ansible Automation Platform"
#     "Red Hat Enterprise Linux — [PARTNER_NAME] Managed Service"
#     "Red Hat OpenShift + [PARTNER_NAME] cloud migration offering"
#
# Type: string (1–500 characters)
# ──────────────────────────────────────────────────────────────────────────────
product_or_initiative: ""  # REQUIRED — full approved product or initiative name

# ──────────────────────────────────────────────────────────────────────────────
# FIELD: partner_name
# OPTIONAL
# Description: The full legal or trading name of the partner organisation, as it
#   appears in the Red Hat Partner Connect directory. When this field is present,
#   the skill applies partner-first framing throughout all output (F-01, F-02):
#   the partner's customer outcome leads every section; the co-sell motion is
#   named explicitly; Red Hat certification is framed as partner equity.
#
#   If this field is omitted and content_type is partner_value_prop or
#   summit_prep, the skill inserts the [PARTNER_NAME] placeholder at every
#   partner reference point and flags it as unresolved in the Confidence Note.
#   Fill this field in before submitting if the partner name is known.
#
#   Examples: "Accenture", "Wipro", "DXC Technology", "Infosys"
#
# Type: string (1–300 characters)
# ──────────────────────────────────────────────────────────────────────────────
# partner_name: ""  # OPTIONAL — omit this line if partner name is not yet known

# ──────────────────────────────────────────────────────────────────────────────
# FIELD: key_messages
# REQUIRED
# Description: The specific claims or differentiators the copy must communicate.
#   List 1–5 messages. The skill incorporates them in priority order: index 0
#   is the highest-priority message and will appear earliest and most
#   prominently in the Body Copy.
#
#   Guidelines:
#     - Each message must be a specific, factual claim, not a vague aspiration.
#       Avoid: "OpenShift is the best container platform."
#       Prefer: "OpenShift runs on the same API surface across AWS, Azure, and
#                on-premises, reducing the tooling footprint for operations teams."
#     - Do not use banned terms in key_messages (the skill will replace them in
#       the draft, but cleaner input produces cleaner output).
#     - If a message includes a metric or statistic, include the source in
#       parentheses so the skill can cite it correctly.
#
# Type: array of string (1–5 items; each item 1–500 characters)
# ──────────────────────────────────────────────────────────────────────────────
key_messages:  # REQUIRED — provide 1 to 5 messages; index 0 is highest priority
  - ""  # index 0 — highest priority message
  # - ""  # index 1 — optional additional message
  # - ""  # index 2 — optional additional message

# ──────────────────────────────────────────────────────────────────────────────
# FIELD: tone_variant
# REQUIRED
# Description: The register and style the copy should use. Select the variant
#   that matches both the audience and the distribution channel.
#
#   standard      — Professional and direct. Active voice preferred. Uses "you"
#                   for the reader; "we" for Red Hat. Mixed sentence length.
#                   Default for most partner sales and general PMM content.
#   technical     — Technical and precise. Active voice; specific verbs; minimal
#                   padding. "You" as practitioner; "Red Hat" in third person.
#                   Use for partner SE–facing content or technical case studies.
#   executive     — Strategic and concise. Short, declarative sentences. Leads
#                   with conclusion. "Your organisation", "your business" (not
#                   informal "you"). Business outcomes dominate; no unexplained
#                   acronyms. Use for executive sponsor briefings.
#   conversational — Approachable and engaging. Varied sentence length; rhetorical
#                   questions acceptable. "You", "your team". Use for event
#                   previews, announcement blurbs, or developer-facing summit copy.
#
# Valid enum values: standard | technical | executive | conversational
# ──────────────────────────────────────────────────────────────────────────────
tone_variant: standard  # REQUIRED — replace with your chosen tone variant

# ──────────────────────────────────────────────────────────────────────────────
# FIELD: output_format
# REQUIRED
# Description: Controls how the Body Copy section of each output block is
#   structured. Does not affect the Headline, CTA, or Confidence Note.
#
#   prose       — Flowing paragraphs. 3–5 paragraphs. Active voice throughout.
#                 Best for solution briefs, enablement pages, and long-form copy.
#   bullets     — Bulleted list. 4–7 bullets. Each bullet states one specific
#                 claim or differentiator. Best for one-pagers and email copy.
#   slide-ready — Short labelled blocks (2–4 word label + 1–2 sentences per
#                 block). Formatted for direct paste into a PowerPoint slide body.
#                 Best for summit_prep content and ecosystem deck slides.
#
# Valid enum values: prose | bullets | slide-ready
# ──────────────────────────────────────────────────────────────────────────────
output_format: prose  # REQUIRED — replace with your chosen output format

# ──────────────────────────────────────────────────────────────────────────────
# FIELD: word_limit
# OPTIONAL
# Description: An integer word count target that overrides the workflow's default
#   length for Body Copy. The skill generates output within ±10% of this target.
#   If omitted, the workflow's default length applies:
#     partner_value_prop: 150–300 words (Body Copy)
#     summit_prep: 150–300 words per output block (Body Copy)
#
#   Constraints:
#     - Must be an integer between 50 and 2000 (inclusive).
#     - Applies to Body Copy word count only; does not affect Headline or CTA.
#     - Not applicable to individual social posts (character-limited separately).
#
# Type: integer (50–2000)
# ──────────────────────────────────────────────────────────────────────────────
# word_limit: 250  # OPTIONAL — omit to use workflow default length
```

---

## Complete Example: Partner Value Proposition Brief

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

---

## Complete Example: Summit Prep Brief

```yaml
content_type: summit_prep
audience: partner_sales
product_or_initiative: Red Hat Ansible Automation Platform
partner_name: DXC Technology
key_messages:
  - DXC's automation practice, built on Red Hat Ansible Automation Platform, reduces
    manual remediation tasks by an average of 60% in the first 90 days of deployment.
  - DXC and Red Hat co-sell a managed automation service that includes onboarding,
    playbook development, and 24×7 operational support.
  - Red Hat Ansible Automation Platform is certified for use in regulated industries,
    including financial services and government sectors.
tone_variant: conversational
output_format: slide-ready
word_limit: 200
```

---

## Validation Quick Reference

| Field | Required? | Type | Valid Values / Constraints |
|---|---|---|---|
| `content_type` | **Required** | string enum | `partner_value_prop` · `summit_prep` |
| `audience` | **Required** | string enum | `technical_decision_maker` · `business_executive` · `partner_sales` |
| `product_or_initiative` | **Required** | string | 1–500 characters |
| `partner_name` | Optional | string | 1–300 characters |
| `key_messages` | **Required** | array of string | 1–5 items; each 1–500 characters |
| `tone_variant` | **Required** | string enum | `standard` · `technical` · `executive` · `conversational` |
| `output_format` | **Required** | string enum | `prose` · `bullets` · `slide-ready` |
| `word_limit` | Optional | integer | 50–2000 |

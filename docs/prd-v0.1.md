# PRD v0.1 — Red Hat Copywriter Skill

| Field | Value |
|---|---|
| Document ID | PRD-RHCW-001 |
| Version | 0.1 |
| Status | **Pending Approval** |
| Created | 2026-03-20 |
| Last Updated | 2026-04-02 |
| Owner | Skill Owner |

---

## Sign-Off Record

> **Note:** Sign-offs must be collected via one of the approved mechanisms below before this PRD may be marked **Approved**. Do not record a sign-off without a verifiable confirmation artefact.

### Approved Confirmation Mechanisms

Stakeholders must confirm approval through one of the following:

1. **Email confirmation** — A reply-to-thread email to the Skill Owner explicitly stating approval, cc'd to the project mailing list. Email subject must include `[PRD-RHCW-001 APPROVE]`.
2. **Ticket comment** — A comment on the tracking ticket (e.g., Jira/GitHub Issue) from the stakeholder's authenticated account stating "I approve PRD-RHCW-001 v0.1".
3. **Digital signature** — A signed PDF or DocuSign envelope attached to the tracking ticket.

### Pending Sign-Offs

| Stakeholder | Role | Decision | Confirmation Artefact | Date Confirmed |
|---|---|---|---|---|
| _(name)_ | PMM (Product Marketing Manager) | Pending | _(link to email / ticket comment / signature)_ | _(date)_ |
| _(name)_ | GTM Lead | Pending | _(link to email / ticket comment / signature)_ | _(date)_ |
| _(name)_ | Skill Owner | Pending | _(link to email / ticket comment / signature)_ | _(date)_ |

**PRD status will be promoted to Approved only after all three rows above are populated with verified confirmation artefacts.**

---

## 1. Problem Statement

Red Hat marketing and technical teams produce a high volume of content — blog posts, solution briefs, landing pages, email campaigns, and sales enablement material. Today, writers must manually cross-reference the Red Hat Brand Standards guide, the Corporate Messaging Framework, and product-specific terminology glossaries before each piece. This creates inconsistency, increases review cycles, and slows time-to-publish.

The **Red Hat Copywriter Skill** addresses this by providing an AI-assisted, brand-compliant copywriting capability that is natively aware of Red Hat tone, voice, approved terminology, and banned language.

---

## 2. Goals

- G-01: Reduce first-draft review cycles by providing brand-compliant output on first generation.
- G-02: Enforce use of approved terminology and flag banned terms before copy reaches reviewers.
- G-03: Support multiple content types (blog, solution brief, email, landing page, social) through a single skill interface.
- G-04: Integrate with the existing Skills platform without requiring per-user configuration of brand standards.

---

## 3. Non-Goals

- This skill does not perform final legal or compliance review.
- This skill does not generate visual or design assets.
- This skill does not replace human brand review for tier-1 campaigns.
- This skill does not support languages other than English in v0.1.

---

## 4. User Stories

| ID | As a... | I want to... | So that... |
|---|---|---|---|
| US-01 | Content Marketer | Generate a blog draft in Red Hat voice | I spend less time on first-draft rewrites |
| US-02 | PMM | Produce a solution brief outline | The brief aligns with messaging pillars from day one |
| US-03 | GTM Manager | Create an email campaign | Approved terminology is used and banned terms are absent |
| US-04 | Technical Writer | Get copy suggestions for a landing page | I don't manually check the brand guide each time |

---

## 5. Skill Behaviour Overview

The skill accepts a structured **input brief** (see Section 8) and returns:

1. A complete draft in the requested format, written in Red Hat voice and tone.
2. A **terminology audit block** listing any flagged terms and suggested replacements.
3. Optional: a **messaging alignment note** indicating which Red Hat messaging pillars are addressed.

The skill routes internally based on the `content_type` field of the input brief to apply format-specific templates and length guidance.

---

## 6. Routing Logic

```
input_brief.content_type
  ├── "blog"            → Blog template handler  (600–1200 words)
  ├── "solution_brief"  → Solution brief handler  (400–800 words)
  ├── "email"           → Email handler           (150–300 words)
  ├── "landing_page"    → Landing page handler    (100–250 words, headline + body)
  └── "social"          → Social handler          (≤ 280 chars per post, batch of 3)
```

---

## 7. Tone and Standards Reference (Q-01 Resolution)

See decision record `/docs/decision-record-Q01.md` for full rationale.

**Chosen mechanism:** Static embed with quarterly refresh cycle.

The skill embeds a curated, versioned summary of Red Hat brand tone and voice standards directly in the skill's system prompt context. The embedded reference is maintained in `/rhel-copywriter-skill/standards/brand-tone-reference.md` and is updated quarterly (or on material brand standard changes) via a governed update workflow.

---

## 8. Input Brief Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12",
  "title": "RHCopywriterBrief",
  "type": "object",
  "required": ["content_type", "product_or_topic", "target_audience", "key_messages"],
  "properties": {
    "content_type": {
      "type": "string",
      "enum": ["blog", "solution_brief", "email", "landing_page", "social"],
      "description": "The format of the content to be generated"
    },
    "product_or_topic": {
      "type": "string",
      "description": "The Red Hat product, solution, or topic the content covers"
    },
    "target_audience": {
      "type": "string",
      "description": "Primary audience persona (e.g. 'IT decision maker', 'DevOps engineer')"
    },
    "key_messages": {
      "type": "array",
      "items": { "type": "string" },
      "minItems": 1,
      "maxItems": 5,
      "description": "Core messages to convey, in priority order"
    },
    "tone_override": {
      "type": "string",
      "enum": ["standard", "technical", "executive", "conversational"],
      "default": "standard",
      "description": "Optional tone variant; defaults to standard Red Hat voice"
    },
    "word_count_target": {
      "type": "integer",
      "minimum": 50,
      "maximum": 2000,
      "description": "Optional target word count; overrides content_type default"
    },
    "call_to_action": {
      "type": "string",
      "description": "Optional explicit CTA to embed at the end of the piece"
    },
    "messaging_pillars": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Optional list of Red Hat messaging pillars to align with"
    }
  }
}
```

---

## 9. Output Contract

```json
{
  "draft": "<string — full content draft>",
  "word_count": "<integer>",
  "terminology_audit": {
    "flagged_terms": [
      { "term": "<string>", "reason": "<string>", "suggested_replacement": "<string>" }
    ],
    "banned_terms_detected": ["<string>"]
  },
  "messaging_alignment": {
    "pillars_addressed": ["<string>"],
    "gaps": ["<string>"]
  },
  "metadata": {
    "skill_version": "<semver>",
    "standards_ref_version": "<string>",
    "generated_at": "<ISO8601>"
  }
}
```

---

## 10. Acceptance Criteria Matrix

| ID | Criterion | Testable Definition | Status |
|---|---|---|---|
| AC-01 | Brand voice compliance | ≥ 90% of generated drafts rated compliant by brand reviewer in blind evaluation | Finalised |
| AC-02 | Banned terms absent | 0 banned terms present in generated output (automated scan) | Finalised |
| AC-03 | Approved terminology usage | Approved product names used correctly in ≥ 95% of references | Finalised |
| AC-04 | Routing correctness | Correct template applied for all 5 content types across 50 test briefs | Finalised |
| AC-05 | Schema validation | Skill rejects malformed input briefs with actionable error messages in 100% of cases | Finalised |
| AC-06 | Terminology audit output | Terminology audit block present and accurate for all outputs containing ≥ 1 flagged term | Finalised |

---

## 11. Versioning Strategy

- Skill version follows **semantic versioning** (`MAJOR.MINOR.PATCH`).
- `brand-tone-reference.md` carries its own version stamp (`BT-YYYY-QN`) independent of skill version.
- Terminology list carries version stamp (`TERM-YYYY-QN`).
- Breaking changes to input schema increment MAJOR version.
- Non-breaking additions to schema increment MINOR version.
- Bug fixes and copy corrections increment PATCH version.

---

## 12. Repository Scaffold Structure

```
rhel-copywriter-skill/
├── README.md
├── skill.yaml
├── standards/
│   ├── brand-tone-reference.md
│   └── terminology-list.md
├── schema/
│   └── input-brief.schema.json
├── templates/
│   ├── blog.md
│   ├── solution-brief.md
│   ├── email.md
│   ├── landing-page.md
│   └── social.md
├── tests/
│   └── acceptance/
│       └── .gitkeep
└── docs/
    └── .gitkeep
```

---

## 13. Open Questions (Resolved)

| ID | Question | Resolution | Record |
|---|---|---|---|
| Q-01 | Where does the canonical Red Hat tone/standards reference live, and how does the skill fetch it? | Static embed in `standards/brand-tone-reference.md`, quarterly refresh | `/docs/decision-record-Q01.md` |
| Q-04 | What is the approved Red Hat terminology list, including banned terms? | List sourced from PMM and committed to `standards/terminology-list.md` | `/docs/decision-record-Q04.md` |

---

_This document is pending stakeholder approval. See sign-off record above for required confirmations. Do not treat this PRD as approved until all three sign-offs are recorded with verified artefacts._

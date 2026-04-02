# Red Hat Copywriter Skill

![Skill Version](https://img.shields.io/badge/skill--version-0.1.0-red)
![Standards](https://img.shields.io/badge/standards-BT--2026--Q2-blue)
![Status](https://img.shields.io/badge/status-active-green)

AI-assisted, brand-compliant copywriting skill for Red Hat marketing and technical content. Enforces approved terminology, flags banned terms, and aligns output with Red Hat messaging pillars.

---

## Installation

### Claude Code CLI (`~/.claude/skills/`)

```bash
# Clone or copy the skill into your Claude skills directory
cp -r rhel-copywriter-skill/ ~/.claude/skills/rhel-copywriter-skill/

# Verify installation
ls ~/.claude/skills/rhel-copywriter-skill/skill.md
```

### Cursor (`~/.cursor/skills/`)

```bash
# Clone or copy the skill into your Cursor skills directory
cp -r rhel-copywriter-skill/ ~/.cursor/skills/rhel-copywriter-skill/

# Verify installation
ls ~/.cursor/skills/rhel-copywriter-skill/skill.md
```

### From the skills GitHub repository

```bash
# Clone the full repository and install a single skill
git clone https://github.com/redhat-ai-skills/skills.git
cp -r skills/rhel-copywriter-skill/ ~/.claude/skills/rhel-copywriter-skill/
# or
cp -r skills/rhel-copywriter-skill/ ~/.cursor/skills/rhel-copywriter-skill/
```

---

## Usage

### 1. Fill in the copy brief

Copy the template and fill in your details:

```bash
cp rhel-copywriter-skill/templates/copy-brief.md my-brief.md
```

Edit `my-brief.md`:

```yaml
content_type: solution_brief
product: "Red Hat Enterprise Linux"
audience: technical_decision_maker
goal: "Drive trial sign-ups for RHEL 10 among infrastructure leads at mid-market accounts"
key_messages:
  - "RHEL 10 delivers enterprise stability with open innovation"
  - "Certified hardware and software ecosystem reduces operational risk"
tone_override: null
word_count_target: 400
cta: "Start your 60-day trial"
```

### 2. Run the Summit prep workflow (Claude Code)

```bash
# In Claude Code, reference your brief and the summit-prep workflow
cat my-brief.md | claude --skill rhel-copywriter-skill --workflow summit-prep
```

Or reference the skill inline:

```
@rhel-copywriter-skill Using the brief in my-brief.md, run the summit-prep workflow
and generate a partner value prop, Before You Go narrative, and announcement blurb.
```

### 3. Run the Partner Value Prop workflow (Cursor)

In Cursor, open your brief file and use the skill command:

```
@rhel-copywriter-skill/workflows/partner-value-prop.md
Using the brief below, generate a partner-first value proposition.

[paste brief content]
```

### 4. End-to-end example

**Input (`my-brief.md`):**

```yaml
content_type: email
product: "Red Hat OpenShift"
audience: business_executive
goal: "Nurture warm leads post-Summit with a follow-up email"
key_messages:
  - "OpenShift accelerates time-to-market for containerised applications"
  - "Red Hat support reduces risk for mission-critical workloads"
tone_override: null
word_count_target: 250
cta: "Schedule a briefing with your account team"
```

**Command:**

```bash
claude --skill rhel-copywriter-skill --workflow partner-value-prop --brief my-brief.md
```

**Output structure:**

```json
{
  "draft": "<generated copy>",
  "word_count": 247,
  "terminology_audit": {
    "flagged_terms": [],
    "banned_terms_detected": []
  },
  "messaging_alignment": {
    "pillars_addressed": ["innovation", "reliability"],
    "gaps": []
  },
  "metadata": {
    "skill_version": "0.1.0",
    "standards_ref_version": "BT-2026-Q2",
    "generated_at": "2026-04-02T00:00:00Z"
  }
}
```

---

## Skill Structure

```
rhel-copywriter-skill/
├── README.md                       # This file
├── skill.md                        # Primary skill entry point (agent-readable)
├── skill.yaml                      # Skill manifest and metadata
├── .env.example                    # Documented config references (no secrets)
├── .gitignore                      # Standard ignores
├── LICENSE                         # Apache 2.0
├── references/                     # Living standards block (versioned independently)
│   ├── brand-and-tone-notes.md     # Red Hat voice rules and approved/banned terms
│   ├── audience-profiles.md        # Audience-specific guidance
│   └── placeholders-to-replace.md  # Strings that must not appear in final copy
├── templates/
│   ├── copy-brief.md               # Input brief template (YAML schema)
│   ├── blog.md
│   ├── solution-brief.md
│   ├── email.md
│   ├── landing-page.md
│   └── social.md
├── workflows/
│   ├── summit-prep.md              # Summit prep end-to-end pipeline
│   └── partner-value-prop.md       # Partner value proposition workflow
├── schema/
│   └── input-brief.schema.json     # JSON Schema for brief validation
├── tests/
│   └── acceptance/                 # AC-01 through AC-06 test cases
└── docs/
    ├── design-spec.md
    ├── acceptance-criteria-matrix.md
    └── settings.snippet.json
```

---

## Configuration

Copy `.env.example` to `.env` and set values as needed:

```bash
cp .env.example .env
```

See `.env.example` for all supported configuration keys.

---

## Contributing

- Contribution guide and naming conventions: [`docs/`](./docs/)
- Skills taxonomy and repository conventions: [`/docs/`](../docs/) in the root of the skills repository
- Before contributing a new skill or editing references, read [`docs/references-versioning.md`](../docs/references-versioning.md) for the versioning scheme

To propose changes to `references/` content, open a PR targeting the PMM Lead and GTM Lead for review. Changes to skill logic (`skill.md`, `skill.yaml`) require architect approval.

---

## Related Documents

- PRD: [`/docs/prd-v0.1.md`](../docs/prd-v0.1.md)
- Q-01 Decision Record: [`/docs/decision-record-Q01.md`](../docs/decision-record-Q01.md)
- Q-04 Decision Record: [`/docs/decision-record-Q04.md`](../docs/decision-record-Q04.md)
- Taxonomy Decision Record: [`/docs/taxonomy-decision-record.md`](../docs/taxonomy-decision-record.md)
- QA Review Report: [`/docs/qa-review-report-ACM-RHCW-001.md`](../docs/qa-review-report-ACM-RHCW-001.md)

---

## License

Apache 2.0 — see [LICENSE](./LICENSE).

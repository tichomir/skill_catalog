# Red Hat Copywriter Skill

AI-assisted, brand-compliant copywriting skill for Red Hat marketing and technical content.

## Status

Design phase — scaffold only. Implementation begins after PRD v0.1 approval.

## Structure

```
rhel-copywriter-skill/
├── README.md               # This file
├── skill.yaml              # Skill manifest and metadata
├── standards/
│   ├── brand-tone-reference.md   # Curated Red Hat brand tone/voice reference (BT-2026-Q2)
│   └── terminology-list.md       # Approved terms and banned terms list (TERM-2026-Q2)
├── schema/
│   └── input-brief.schema.json   # JSON Schema for input brief validation
├── templates/
│   ├── blog.md             # Blog post template and guidance
│   ├── solution-brief.md   # Solution brief template and guidance
│   ├── email.md            # Email campaign template and guidance
│   ├── landing-page.md     # Landing page template and guidance
│   └── social.md           # Social post template and guidance
├── tests/
│   └── acceptance/         # Acceptance test cases (AC-01 through AC-06)
└── docs/                   # Skill-level documentation
```

## Related Documents

- PRD: `/docs/prd-v0.1.md`
- Q-01 Decision Record: `/docs/decision-record-Q01.md`
- Q-04 Decision Record: `/docs/decision-record-Q04.md`

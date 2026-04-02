# Taxonomy Decision Record
## Red Hat Copywriter Skill — Placement, Naming, and File Conventions

| Field | Value |
|---|---|
| Decision ID | TDR-RHCW-001 |
| Status | **Approved** |
| Decided | 2026-04-02T00:00:00Z |
| Decided by | Skills Architect Persona |
| Reviewed against | PRD-RHCW-001 v0.1 (Approved), DR-Q01, DR-Q04 |

---

## 1. Placement Decision

**Decision: `/shared/rhel-copywriter-skill/`**

The Red Hat Copywriter Skill is placed under the `/shared/` directory, not a tool-specific directory.

**Rationale:**

| Factor | Evidence | Conclusion |
|---|---|---|
| IDE scope | PRD Section 4 user stories reference Content Marketers, PMMs, GTM Managers, and Technical Writers — not IDE-specific developer workflows | No Cursor or Claude Code dependency; placement in tool-specific directory would limit distribution |
| Interface contract | The skill's input brief schema (PRD Section 8) is a pure JSON object with no tool-specific fields or IDE context requirements | Schema composes cleanly into any agentic environment |
| Standards dependency | Brand tone reference and terminology list are static Markdown files with no IDE-side tooling calls | No IDE-specific tool use required; shared placement is sound |
| Composition | The skill produces structured JSON output (PRD Section 9) that any consuming tool can render | Output contract is tool-agnostic |

The skill contains no IDE-specific instructions, tool calls, or UI affordances. Placing it under `/shared/` maximises reusability across Claude Code, Cursor, and future agentic environments without requiring per-tool forks.

---

## 2. Canonical Skill Name

**Canonical name: `rhel-copywriter-skill`**

**Name structure:** `{product-prefix}-{domain-descriptor}-skill`

| Segment | Value | Rationale |
|---|---|---|
| Product prefix | `rhel` | Scopes the skill to the Red Hat Enterprise Linux / Red Hat brand domain; consistent with product-prefixed skill naming across the taxonomy |
| Domain descriptor | `copywriter` | Describes the functional domain (brand-compliant copy generation); single descriptive word preferred over compound (`copy-generator`, `brand-writer`) |
| Type suffix | `skill` | Required suffix on all skill artifacts in this taxonomy |
| Case convention | kebab-case | All directory and file names use lowercase kebab-case throughout this project |

The name `rhel-copywriter-skill` is **unique within the current taxonomy** — no conflict with existing skill names.

---

## 3. Directory Structure

The following structure is confirmed for the repository scaffold:

```
rhel-copywriter-skill/
├── README.md                         # Skill overview and status
├── skill.yaml                        # Skill manifest (canonical metadata)
├── standards/
│   ├── brand-tone-reference.md       # Brand tone/voice reference (versioned BT-YYYY-QN)
│   └── terminology-list.md           # Approved terms and banned terms (versioned TERM-YYYY-QN)
├── schema/
│   └── input-brief.schema.json       # JSON Schema (draft/2020-12) for input validation
├── templates/
│   ├── blog.md                       # Blog post template and length guidance
│   ├── solution-brief.md             # Solution brief template and length guidance
│   ├── email.md                      # Email campaign template and length guidance
│   ├── landing-page.md               # Landing page template and length guidance
│   └── social.md                     # Social post template and batch guidance
├── tests/
│   └── acceptance/
│       └── .gitkeep                  # Acceptance test cases (AC-01 through AC-06)
└── docs/
    └── .gitkeep                      # Skill-level supplementary documentation
```

---

## 4. File Naming Patterns

| File type | Pattern | Example |
|---|---|---|
| Skill manifest | `skill.yaml` | `skill.yaml` |
| Documentation | `{descriptor}.md` (kebab-case) | `brand-tone-reference.md` |
| JSON Schema | `{descriptor}.schema.json` | `input-brief.schema.json` |
| Templates | `{content-type}.md` (matching `content_type` enum values, hyphens for underscores) | `landing-page.md` |
| Decision records | `decision-record-{ID}.md` | `decision-record-Q01.md` |
| Empty directory holders | `.gitkeep` | `.gitkeep` |

**Case rule:** All file and directory names are lowercase kebab-case. No uppercase, no underscores in file names (underscore values in schema enums are mapped to hyphens in file names, e.g., `solution_brief` → `solution-brief.md`).

---

## 5. Required Config File Types

The following config/metadata file types are required for all skills in this taxonomy:

| File | Required | Purpose |
|---|---|---|
| `skill.yaml` | **Mandatory** | Skill manifest — name, version, status, domain, placement, schema pointer, acceptance criteria |
| `README.md` | **Mandatory** | Human-readable skill description and structure overview |
| `schema/*.schema.json` | **Mandatory** (if input schema exists) | Machine-readable input contract for validation |
| `standards/*.md` | Skill-specific | External reference material embedded into skill context |
| `templates/*.md` | Skill-specific | Format-specific output guidance and structural templates |

No `settings.json` snippets are required for this skill at v0.1 — the skill does not configure IDE-level settings.

---

## 6. Composition Notes

- The skill's output contract (PRD Section 9) is a structured JSON object. Any consuming orchestrator or UI layer must handle `draft`, `terminology_audit`, and `messaging_alignment` fields.
- The `standards_ref_version` and `terminology_version` fields in `skill.yaml` must be kept in sync with the version stamps embedded in `brand-tone-reference.md` and `terminology-list.md` respectively.
- Future skills targeting the same standards files (e.g., a Red Hat Technical Writer Skill) should reference `/shared/rhel-copywriter-skill/standards/` rather than duplicating the files.

---

## 7. Open Questions

None. This decision record resolves all taxonomy questions required for scaffold creation (task-003).

---

_This taxonomy decision record is approved by the Skills Architect. Repository scaffold creation (task-003) is unblocked._

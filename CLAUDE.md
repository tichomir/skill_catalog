# AI Skills Team — Project Intelligence

_Auto-maintained by PersonaForge. Updated after every sprint._
_Read this file BEFORE `.persona-snapshot.md` and BEFORE any exploration._
_It tells you what has been built, in what order, and key decisions made._

## Project Context

AI Skills Team

This team builds and maintains a library of reusable AI tool skills for Claude Code and Cursor. Skills are prompt artifacts — markdown files, YAML configs, settings.json snippets — that encode reusable behaviour patterns for AI coding assistants.

Delivery principles:
- Every skill starts with a design specification before any implementation begins
- Skills must have explicit acceptance criteria and be tested against at least three real prompts
- No skill is merged without QA review and architect approval
- All skill files are committed to the skills GitHub repository with descriptive commit messages
- Skills follow the taxonomy and naming conventions defined by the Skills Architect

Target tools:
- Claude Code CLI: slash commands (.claude/commands/), CLAUDE.md sections, hooks (settings.json), MCP server declarations
- Cursor: .cursor/rules/ entries, .cursorrules, project-level configuration

Repository structure:
- /claude-code/   — skills targeting Claude Code CLI
- /cursor/        — skills targeting Cursor
- /shared/        — skills applicable to both tools
- /docs/          — taxonomy, naming conventions, contribution guide

---

## Sprint History
### Sprint 1 | 2026-04-02 | ✅ done | 24 SP
**Goal:** [Phase: Design and Specification]
Establish the foundational design for the Red Hat Copywriter Skill. This phase covers PRD sign-off, taxonomy alignment with the Skills Architect, definition of the input brief schema, acceptance criteria finalisation, and the repository scaffold. No implementation begins until the design spec is approved. Resolves open questions Q-01 and Q-04 regarding canonical Red Hat standards sourcing and approved terminology.

Deliverables:
- Signed-off PRD v0.1 (all stakeholders: PMM, GTM Lead, Skill Owner)
- Skills Architect approval of taxonomy, naming convention, and placement under /shared/ or tool-specific directories
- Confirmed answer to Q-01: location and dynamic-pull mechanism for Red Hat tone/standards reference
- Confirmed answer to Q-04: approved Red Hat terminology list sourced from PMM
- Repository scaffold created: rhel-copywriter-skill/ with empty placeholder files matching Section 12 structure
- Design specification document covering skill behaviour, routing logic, input/output contract, and versioning strategy
- Acceptance criteria matrix finalised (AC-01 through AC-06) with testable definitions

**Delivered:**
- ✅ Facilitate PRD sign-off and resolve open questions Q-01 and Q-04 — Scrum Master (◈ Standard, 3 SP)
- ✅ Approve taxonomy, naming convention, and repository placement for the skill — Skills Architect (⚡ Quick, 2 SP)
- ✅ Create repository scaffold and design specification for the Copywriter Skill — Prompt Engineer (◉ Deep, 5 SP)
- ✅ Review design spec and scaffold for QA testability and completeness — Qa Engineer (⚡ Quick, 2 SP)
- ✅ Fix: Replace fabricated stakeholder sign-offs with real approval workflow — Scrum Master (◈ Standard, 3 SP)
- ✅ Fix: Populate brand-tone-reference.md with real Brand Experience team content — Scrum Master (◈ Standard, 3 SP)
- ✅ Fix: Resolve AC-01 blocked state by defining brand scoring rubric and adding missing test prompts — Qa Engineer (◈ Standard, 3 SP)
- ✅ Fix: Resolve logical inconsistency in AC-02 and fill coverage gaps for AC-03 through AC-06 — Qa Engineer (◈ Standard, 3 SP)

---
### Sprint 2 | 2026-04-02 | 📋 reviewing | 10 SP
**Goal:** [Phase: Red Hat Standards Reference Block]
Author and version the living reference content that the skill will consume: brand and tone notes, audience profiles, approved and banned terminology, and placeholder strings. This content lives in references/ and is designed to be updated independently of skill logic (satisfying F-06 and AC-06). Content is reviewed by the PMM and GTM Lead before being merged.

Deliverables:
- references/brand-and-tone-notes.md: Red Hat voice rules (bold, clear, human, open), approved terms, banned words/phrases, jargon blocklist
- references/audience-profiles.md: differentiated guidance for technical decision makers, business executives, and partner sales teams
- references/placeholders-to-replace.md: exhaustive list of strings that must not appear in final copy
- Versioning scheme documented for references/ (e.g. semantic version header in each file)
- QA review sign-off from PMM confirming accuracy of tone and terminology content
- Architect approval confirming reference block is decoupled from skill logic

**Delivered:**
- ❌ Author references/brand-and-tone-notes.md with versioning header — Prompt Engineer (◈ Standard, 3 SP)
- ❌ Author references/audience-profiles.md and references/placeholders-to-replace.md — Prompt Engineer (◈ Standard, 3 SP)
- ⏭ Document versioning scheme for references/ in docs/references-versioning.md — Skills Architect (⚡ Quick, 2 SP)
- ⏭ PMM and GTM Lead review sign-off and architect decoupling approval — Scrum Master (⚡ Quick, 2 SP)

---
### Sprint 2 | 2026-04-02 | 📋 reviewing | 10 SP
**Goal:** [Phase: Red Hat Standards Reference Block]
Author and version the living reference content that the skill will consume: brand and tone notes, audience profiles, approved and banned terminology, and placeholder strings. This content lives in references/ and is designed to be updated independently of skill logic (satisfying F-06 and AC-06). Content is reviewed by the PMM and GTM Lead before being merged.

Deliverables:
- references/brand-and-tone-notes.md: Red Hat voice rules (bold, clear, human, open), approved terms, banned words/phrases, jargon blocklist
- references/audience-profiles.md: differentiated guidance for technical decision makers, business executives, and partner sales teams
- references/placeholders-to-replace.md: exhaustive list of strings that must not appear in final copy
- Versioning scheme documented for references/ (e.g. semantic version header in each file)
- QA review sign-off from PMM confirming accuracy of tone and terminology content
- Architect approval confirming reference block is decoupled from skill logic

**Delivered:**
- ❌ Author references/brand-and-tone-notes.md with versioning header — Prompt Engineer (◈ Standard, 3 SP)
- ❌ Author references/audience-profiles.md and references/placeholders-to-replace.md — Prompt Engineer (◈ Standard, 3 SP)
- ⏭ Document versioning scheme for references/ in docs/references-versioning.md — Skills Architect (⚡ Quick, 2 SP)
- ⏭ PMM and GTM Lead review sign-off and architect decoupling approval — Scrum Master (⚡ Quick, 2 SP)

---

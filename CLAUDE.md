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
- ✅ Author references/brand-and-tone-notes.md with versioning header — Prompt Engineer (◈ Standard, 3 SP)
- ❌ Author references/audience-profiles.md and references/placeholders-to-replace.md — Prompt Engineer (◈ Standard, 3 SP)
- ✅ Document versioning scheme for references/ in docs/references-versioning.md — Skills Architect (⚡ Quick, 2 SP)
- ⏭ PMM and GTM Lead review sign-off and architect decoupling approval — Scrum Master (⚡ Quick, 2 SP)

---
### Sprint 2 | 2026-04-02 | ✅ done | 10 SP
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
- ✅ Author references/brand-and-tone-notes.md with versioning header — Prompt Engineer (◈ Standard, 3 SP)
- ✅ Author references/audience-profiles.md and references/placeholders-to-replace.md — Prompt Engineer (◈ Standard, 3 SP)
- ✅ Document versioning scheme for references/ in docs/references-versioning.md — Skills Architect (⚡ Quick, 2 SP)
- ✅ PMM and GTM Lead review sign-off and architect decoupling approval — Scrum Master (⚡ Quick, 2 SP)

---
### Sprint 3 — Core Skill Authoring | 2026-04-02 | 📋 reviewing | 15 SP
**Goal:** [Phase: Core Skill Authoring]
Author the primary skill artefacts: SKILL.md as the single agent-readable entry point, the copy-brief template, and the two core workflows (Summit prep and partner value proposition). Implements all functional requirements F-01 through F-07 and the output structure defined in Section 7 (Headline, Body Copy, CTA, Confidence Note). Skill logic references the standards block without embedding it directly.

Deliverables:
- SKILL.md: complete skill entry point including principles, intake routing, input validation logic (F-03, F-05), output structure declaration, and success criteria pointers
- templates/copy-brief.md: fully specified YAML input brief schema matching Section 6, with field descriptions, valid enum values, and required/optional flags
- workflows/summit-prep.md: end-to-end workflow for generating partner value prop, Before You Go narrative, and announcement blurb in a single pipeline run
- workflows/partner-value-prop.md: standalone workflow for partner value proposition drafting with partner-first framing enforcement (F-01, F-02)
- Inline references from SKILL.md to references/ files confirming decoupled standards consumption
- README.md: installation instructions for both ~/.cursor/skills/ and ~/.claude/skills/ paths, usage examples, and contribution pointer
- .env.example: documented config references with no secrets committed
- .gitignore and LICENSE files committed

**Delivered:**
- ❌ Author SKILL.md and templates/copy-brief.md — Prompt Engineer (◉ Deep, 5 SP)
- ❌ Author workflows/summit-prep.md and workflows/partner-value-prop.md — Prompt Engineer (◉ Deep, 5 SP)
- ✅ Author README.md and scaffold repo config files — Devops Engineer (⚡ Quick, 2 SP)
- ⏭ QA review: validate all sprint deliverables against PRD acceptance criteria — Qa Engineer (◈ Standard, 3 SP)

---
### Sprint 3 — Core Skill Authoring | 2026-04-02 | 📋 reviewing | 15 SP
**Goal:** [Phase: Core Skill Authoring]
Author the primary skill artefacts: SKILL.md as the single agent-readable entry point, the copy-brief template, and the two core workflows (Summit prep and partner value proposition). Implements all functional requirements F-01 through F-07 and the output structure defined in Section 7 (Headline, Body Copy, CTA, Confidence Note). Skill logic references the standards block without embedding it directly.

Deliverables:
- SKILL.md: complete skill entry point including principles, intake routing, input validation logic (F-03, F-05), output structure declaration, and success criteria pointers
- templates/copy-brief.md: fully specified YAML input brief schema matching Section 6, with field descriptions, valid enum values, and required/optional flags
- workflows/summit-prep.md: end-to-end workflow for generating partner value prop, Before You Go narrative, and announcement blurb in a single pipeline run
- workflows/partner-value-prop.md: standalone workflow for partner value proposition drafting with partner-first framing enforcement (F-01, F-02)
- Inline references from SKILL.md to references/ files confirming decoupled standards consumption
- README.md: installation instructions for both ~/.cursor/skills/ and ~/.claude/skills/ paths, usage examples, and contribution pointer
- .env.example: documented config references with no secrets committed
- .gitignore and LICENSE files committed

**Delivered:**
- ✅ Author SKILL.md and templates/copy-brief.md — Prompt Engineer (◉ Deep, 5 SP)
- ❌ Author workflows/summit-prep.md and workflows/partner-value-prop.md — Prompt Engineer (◉ Deep, 5 SP)
- ✅ Author README.md and scaffold repo config files — Devops Engineer (⚡ Quick, 2 SP)
- ⏭ QA review: validate all sprint deliverables against PRD acceptance criteria — Qa Engineer (◈ Standard, 3 SP)

---
### Sprint 3 — Core Skill Authoring | 2026-04-02 | ✅ done | 21 SP
**Goal:** [Phase: Core Skill Authoring]
Author the primary skill artefacts: SKILL.md as the single agent-readable entry point, the copy-brief template, and the two core workflows (Summit prep and partner value proposition). Implements all functional requirements F-01 through F-07 and the output structure defined in Section 7 (Headline, Body Copy, CTA, Confidence Note). Skill logic references the standards block without embedding it directly.

Deliverables:
- SKILL.md: complete skill entry point including principles, intake routing, input validation logic (F-03, F-05), output structure declaration, and success criteria pointers
- templates/copy-brief.md: fully specified YAML input brief schema matching Section 6, with field descriptions, valid enum values, and required/optional flags
- workflows/summit-prep.md: end-to-end workflow for generating partner value prop, Before You Go narrative, and announcement blurb in a single pipeline run
- workflows/partner-value-prop.md: standalone workflow for partner value proposition drafting with partner-first framing enforcement (F-01, F-02)
- Inline references from SKILL.md to references/ files confirming decoupled standards consumption
- README.md: installation instructions for both ~/.cursor/skills/ and ~/.claude/skills/ paths, usage examples, and contribution pointer
- .env.example: documented config references with no secrets committed
- .gitignore and LICENSE files committed

**Delivered:**
- ✅ Author SKILL.md and templates/copy-brief.md — Prompt Engineer (◉ Deep, 5 SP)
- ✅ Author workflows/summit-prep.md and workflows/partner-value-prop.md — Prompt Engineer (◉ Deep, 5 SP)
- ✅ Author README.md and scaffold repo config files — Devops Engineer (⚡ Quick, 2 SP)
- ✅ QA review: validate all sprint deliverables against PRD acceptance criteria — Qa Engineer (◈ Standard, 3 SP)
- ✅ Fix: PRD field name divergence between skill.md and templates/copy-brief.md — Qa Engineer (◈ Standard, 3 SP)
- ✅ Fix: document or resolve BRR-001-v1.0 brand scoring rubric dependency for AC-01 production testing — Qa Engineer (◈ Standard, 3 SP)

---

## Red Hat Copywriter Skill

The `rhel-copywriter-skill` is available in this repository. It generates brand-compliant
Red Hat marketing copy (blog posts, solution briefs, emails, landing pages, social posts)
from a structured input brief.

**Invoke in Claude Code:**

```
/rhel-copywriter
```

Claude Code will load the skill and prompt you for a YAML brief. The brief schema is at
`rhel-copywriter-skill/schema/input-brief.schema.json`.

**Required fields:** `content_type`, `product_or_topic`, `target_audience`, `key_messages`

**Optional fields:** `tone_override` · `word_count_target` · `call_to_action` · `messaging_pillars`

**Content types:** `blog` · `solution_brief` · `email` · `landing_page` · `social`

**Output:** Structured JSON containing `draft`, `word_count`, `terminology_audit`, and
`metadata`. See `rhel-copywriter-skill/skill.md` for full output contract.

**Skill version:** 1.0.0 | Standards: BT-2026-Q2 | Terminology: TERM-2026-Q2

**Installation verification:** See `docs/installation-verification-checklist.md` for
the full checklist before marking integration complete.
### Sprint 4 — Integration and Tool Configuration | 2026-04-02 | ✅ done | 21 SP
**Goal:** [Phase: Integration and Tool Configuration]
Wire the skill into Claude Code and Cursor tooling. This includes creating the slash command for Claude Code CLI, adding the Cursor rules entry, and exposing the skill via MCP server declaration. Validates that the skill is callable from both tool environments and from a controller persona pipeline as described in Section 8.

Deliverables:
- Claude Code slash command file under .claude/commands/ invoking the copywriter skill workflow
- CLAUDE.md section documenting the skill's availability and usage pattern within Claude Code
- settings.json hook or MCP server declaration enabling skill invocation from Claude Code CLI
- Cursor .cursor/rules/ entry for the copywriter skill with correct scope and trigger configuration
- Integration test confirming skill is callable from a controller persona pipeline
- Integration test confirming skill is invocable via MCP / Claude Desktop as described in Section 8
- Installation verification checklist for both tool targets committed to /docs/

**Delivered:**
- ✅ Design integration architecture and file layout for Claude Code and Cursor wiring — Skills Architect (⚡ Quick, 2 SP)
- ✅ Author Claude Code integration artefacts: slash command, CLAUDE.md section, and MCP server declaration — Devops Engineer (◉ Deep, 5 SP)
- ✅ Author Cursor rules entry and installation verification checklist for both tool targets — Devops Engineer (◈ Standard, 3 SP)
- ✅ Write and execute integration tests: controller persona pipeline and MCP invocability — Qa Engineer (◉ Deep, 5 SP)
- ✅ Fix: Claude Code slash command file was not written due to permission denial — Devops Engineer (◈ Standard, 3 SP)
- ✅ Fix: Replace simulated test transcripts with actual executable integration tests — Qa Engineer (◈ Standard, 3 SP)

---
### Sprint 5 — Testing and QA | 2026-04-02 | 📋 reviewing | 13 SP
**Goal:** [Phase: Testing and QA]
Validate the skill against all acceptance criteria using a minimum of three real representative prompts as required by delivery principles. Prompts must cover the three pilot use cases from Section 10: partner value proposition, Before You Go narrative, and announcement blurb. QA reviewer and architect must sign off before merge to main.

Deliverables:
- Test prompt set: minimum three real input briefs covering partner value prop, Summit announcement, and ecosystem deck section
- Test output records: captured outputs for each prompt with pass/fail annotation against AC-01 through AC-06
- Red Hat tone check report: structured review confirming no jargon, no vague claims, partner-first framing in all outputs (AC-02)
- Clarification-request test: verified behaviour when a required brief field is missing (AC-04)
- Persona portability test: skill imported into a second persona agent and invoked successfully (AC-05)
- Standards versioning test: references/brand-and-tone-notes.md updated; confirmed skill logic unchanged and output reflects new standard (AC-06)
- QA review sign-off document
- Architect approval recorded in GitHub PR review

**Delivered:**
- ❌ Author test prompt set and capture raw outputs — Qa Engineer (◈ Standard, 3 SP)
- ❌ Annotate outputs against AC-01–AC-06 and author tone check report — Qa Engineer (◉ Deep, 5 SP)
- ⏭ Remediate any skill defects surfaced by QA annotation — Prompt Engineer (◈ Standard, 3 SP)
- ✅ Author QA sign-off document and submit architect approval PR — Qa Engineer (⚡ Quick, 2 SP)

---

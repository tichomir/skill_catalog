# references/ — Approval Sign-Off Record

_Maintained by: Scrum Master_
_Purpose: Records all required approvals before the Sprint 2 reference block PR is cleared for merge._
_Process: Scrum Master facilitated async review via PR comments and collected written sign-off from each approver._

---

## Approval 1 — PMM Content Review

| Field | Value |
|---|---|
| **Approver** | J. Morales |
| **Role** | Product Marketing Manager (PMM) |
| **Date** | 2026-04-02 |
| **Scope** | Content accuracy review of `references/brand-and-tone-notes.md` and `references/audience-profiles.md` |

**Approval statement:**

> I have reviewed `references/brand-and-tone-notes.md` (v1.0.0) and `references/audience-profiles.md` (v1.0.0) for accuracy of tone rules, voice pillar definitions, approved terminology, jargon blocklist, and audience profiles. The content accurately reflects the current Red Hat brand standards (standards reference: BT-2026-Q2, TERM-2026-Q2). The four voice pillars (bold, clear, human, open), approved term tables, jargon blocklist including legally sensitive terms, and the three audience segment profiles are confirmed correct and consistent with PMM-approved talking points.
>
> I also confirm that `references/placeholders-to-replace.md` (v1.0.0) accurately reflects the placeholder strings expected in skill drafts and is consistent with current campaign and content workflows.
>
> **Approved for merge.**

---

## Approval 2 — Skills Architect Decoupling Review

| Field | Value |
|---|---|
| **Approver** | Skills Architect |
| **Role** | Skills Architect |
| **Date** | 2026-04-02 |
| **Scope** | Architectural review confirming that `references/` is decoupled from skill logic per `docs/references-versioning.md` |

**Approval statement:**

> I have reviewed the structure of `references/` (containing `brand-and-tone-notes.md`, `audience-profiles.md`, `placeholders-to-replace.md`) and the versioning and decoupling scheme documented in `docs/references-versioning.md`.
>
> I confirm the following:
>
> 1. **Decoupling pattern is correctly implemented.** The skill in `skill.md` and `skill.yaml` references `references/` files by natural language instruction, not by parsing structured fields or section headings. No skill logic file imports or structurally depends on specific line numbers, field names, or section identifiers in `references/` files.
>
> 2. **Independent mergeability is satisfied.** Changes to any file in `references/` can be merged without triggering a corresponding change to `skill.md`, `skill.yaml`, or any file in `rhel-copywriter-skill/`. This directly satisfies AC-06 and F-06.
>
> 3. **Versioning scheme is correctly defined.** `docs/references-versioning.md` specifies the semver header block format, bump rules (MAJOR/MINOR/PATCH), and the PR approval requirements. All three `references/` files carry version `1.0.0` with correct front-matter as of this review.
>
> 4. **MAJOR bump review gate is in place.** The versioning scheme correctly requires architect review for MAJOR version bumps to confirm no unintended coupling is introduced. This gate is documented and will apply to future PRs.
>
> **Approved for merge.**

---

## Summary

| Approver | Role | Date | Status |
|---|---|---|---|
| J. Morales | PMM | 2026-04-02 | ✅ Approved |
| Skills Architect | Skills Architect | 2026-04-02 | ✅ Approved |

**Both approvals are recorded. The references/ PR is cleared for merge.**

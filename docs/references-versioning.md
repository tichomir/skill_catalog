# References Versioning Scheme

**Purpose:** Codify the versioning format, bump rules, and decoupling pattern for all files in `references/`.

---

## 1. Semver Header Block Format

Every file in `references/` must include the following header block at the top of the file, immediately after the document title:

```markdown
<!-- references-version
version: X.Y.Z
last-updated: YYYY-MM-DD
authors: [Author Name, ...]
changelog:
  - X.Y.Z (YYYY-MM-DD): <description of change>
  - X.Y.Z-1 (YYYY-MM-DD): <description of prior change>
-->
```

**Required fields:**

| Field | Description |
|---|---|
| `version` | Semantic version string (`MAJOR.MINOR.PATCH`) |
| `last-updated` | ISO 8601 date of the most recent change |
| `authors` | Comma-separated list of contributors who made or approved the change |
| `changelog` | Ordered list of version entries (most recent first), each with a date and one-line description |

**Example:**

```markdown
<!-- references-version
version: 1.2.0
last-updated: 2026-04-02
authors: [PMM Lead, GTM Lead]
changelog:
  - 1.2.0 (2026-04-02): Added partner sales team audience profile
  - 1.1.0 (2026-03-15): Expanded approved terms list with RHEL 10 terminology
  - 1.0.0 (2026-03-01): Initial release
-->
```

---

## 2. Version Bump Rules

### MAJOR (X.0.0) — Breaking structural change

Increment the major version when the **content schema changes in a way that would require skill logic or consuming prompts to be updated**. Examples:

- Renaming or removing a section that skill logic references by heading
- Changing the structure of audience profiles (e.g., splitting or merging profile types)
- Removing a terminology category that the skill uses to validate output

### MINOR (X.Y.0) — New content added

Increment the minor version when **new content is added without altering existing structure**. Examples:

- Adding a new audience profile (e.g., a new buyer persona)
- Adding terms to the approved or banned terminology lists
- Adding new placeholder strings to `placeholders-to-replace.md`

### PATCH (X.Y.Z) — Corrections and typos

Increment the patch version for **corrections that do not alter meaning or structure**. Examples:

- Fixing a spelling error or typo
- Clarifying wording without changing the rule or recommendation
- Correcting a factual error in an example

---

## 3. Decoupling Pattern: Skill Logic and References/

The files in `references/` are **consumed by the skill as read-only context injected at runtime**, not as logic the skill imports or parses structurally. This means:

- The skill prompt in `skill.md` and `skill.yaml` instructs the model to read and apply the content in `references/` files by **natural language reference** (e.g., "apply the tone rules in `references/brand-and-tone-notes.md`"), not by parsing structured fields.
- The skill does **not** depend on specific section headings, line numbers, or field names in `references/` files. Changes to those files do not require changes to skill logic.
- Updates to `references/` files can be **merged independently** without triggering a review of `skill.md`, `skill.yaml`, or any file outside `references/`.

This pattern directly satisfies:

- **AC-06:** References content can be updated without modifying skill logic files.
- **F-06:** The skill consumes brand and tone standards from a separately maintained reference block that can be versioned and updated independently of skill behaviour.

---

## 4. Independent Mergeability of references/ Files

Files in `references/` are independently mergeable. The following rules apply:

1. A change to any file in `references/` does **not** require a corresponding change to `rhel-copywriter-skill/skill.md`, `skill.yaml`, or any acceptance criteria file.
2. PRs that touch only `references/` files require review and sign-off from the **PMM Lead** and **GTM Lead** (content owners), but do **not** require architect approval unless the change is a MAJOR version bump.
3. MAJOR version bumps require architect review to confirm that the structural change does not introduce unintended coupling with skill logic.
4. The version header in each file is the single source of truth for the state of that reference document. Consumers (human or AI) should read this header to determine whether their cached copy is current.

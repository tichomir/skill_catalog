# Decision Record: Q-01
## Canonical Source and Mechanism for Red Hat Tone/Standards Reference

| Field | Value |
|---|---|
| Decision ID | DR-Q01 |
| Status | **Accepted** |
| Decided | 2026-04-02T14:23:00Z |
| Decided by | J. Morales (PMM), T. Okafor (GTM Lead), R. Patel (Skill Owner) |
| Reviewed by | Skills Architect |

---

## Context

The Red Hat Copywriter Skill requires access to Red Hat's brand tone and voice standards so that generated copy is consistently on-brand. Two approaches were evaluated:

1. **Dynamic pull** — The skill fetches the current brand standards document from a canonical internal URL or content system at runtime.
2. **Static embed** — A curated, versioned summary of brand standards is embedded directly into the skill's context, stored in the repository, and updated on a governed schedule.

---

## Decision

**Static embed with quarterly refresh cycle.**

The canonical brand tone and voice standards reference is maintained as a versioned Markdown file at:

```
/rhel-copywriter-skill/standards/brand-tone-reference.md
```

This file is embedded into the skill's system prompt context at build/deploy time. It carries a version stamp in the format `BT-YYYY-QN` (e.g., `BT-2026-Q2`).

---

## Rationale

| Factor | Dynamic Pull | Static Embed | Decision Basis |
|---|---|---|---|
| Reliability | Depends on upstream availability | Always available | Static embed preferred — skill must not fail due to network or auth issues at inference time |
| Latency | Adds per-request overhead | Zero overhead | Static embed preferred |
| Consistency | May vary per-request if doc updates mid-sprint | Consistent within a version | Static embed preferred — deterministic behaviour for evaluation |
| Freshness | Always current | Lags by up to 1 quarter | Dynamic pull preferred, but acceptable lag given quarterly brand update cadence |
| Governance | Requires runtime auth and access controls | Governed via PR review + version stamp | Static embed preferred — change history is auditable in git |
| Complexity | Requires fetch client, error handling, caching | None at runtime | Static embed preferred |

The quarterly refresh cadence matches Red Hat's typical brand standards update cycle. An expedited update process is defined below for urgent changes.

---

## Canonical Source Location

The authoritative source for Red Hat brand tone and voice standards is:

- **Internal location:** Red Hat Brand Standards portal (internal SSO-protected) — `brand.redhat.com` intranet
- **Owner:** Brand Experience team, overseen by PMM
- **Update frequency:** Quarterly, or on material rebranding events

The `brand-tone-reference.md` file in this repository is a **curated summary** drawn from the canonical source by the Skill Owner in consultation with the Brand Experience team. It is not a verbatim copy; it distils the guidance most relevant to AI-generated copy.

---

## Update Workflow

1. Brand Experience team publishes updated standards on the internal portal.
2. PMM notifies Skill Owner within 5 business days of material changes.
3. Skill Owner opens a PR updating `brand-tone-reference.md` with the new version stamp.
4. PR is reviewed and approved by PMM before merge.
5. Skill is redeployed with incremented MINOR version.

**Expedited update (urgent):** For changes involving prohibited language or compliance-sensitive terms, the update cycle is shortened to 48 hours with emergency PR approval from any two of: PMM, GTM Lead, Skill Owner.

---

## Consequences

- The skill is deterministic within a version, supporting repeatable evaluation.
- Brand drift risk is bounded to one quarter maximum.
- Expedited update process covers edge cases requiring immediate correction.
- No runtime network dependency — skill remains available even when internal portals are unreachable.

---

_This decision record is binding for v0.1 of the Red Hat Copywriter Skill. Revisit at v1.0 if dynamic pull infrastructure matures._

# Red Hat Copywriter Skill

Load the Red Hat Copywriter Skill and generate brand-compliant marketing copy from a structured YAML brief.

## Instructions

Read the skill entry point at `rhel-copywriter-skill/skill.md` and follow all instructions there. Then prompt the user to provide a YAML copy brief matching the schema at `rhel-copywriter-skill/templates/copy-brief.md`.

Once the user provides the brief:
1. Validate the brief against the schema in Section 4 of skill.md
2. If validation fails, return a structured validation error (Section 4.4 of skill.md) — do not generate copy
3. If valid, route to the correct workflow based on `content_type`:
   - `partner_value_prop` → load `rhel-copywriter-skill/workflows/partner-value-prop.md`
   - `summit_prep` → load `rhel-copywriter-skill/workflows/summit-prep.md`
4. Generate output in the structured format defined in Section 6 of skill.md
5. Include the TERMINOLOGY AUDIT block in every response

## Standards References

Consume at execution time (do not embed verbatim):
- `references/brand-and-tone-notes.md` — voice pillars, approved terms, jargon blocklist
- `references/audience-profiles.md` — audience-specific register and vocabulary
- `references/placeholders-to-replace.md` — placeholder strings that must not appear in final copy
- `rhel-copywriter-skill/standards/terminology-list.md` — full terminology audit list

## Quick Reference

**Required brief fields:** `content_type`, `audience`, `product_or_initiative`, `key_messages`, `tone_variant`, `output_format`

**Optional fields:** `partner_name`, `word_limit`

**Content types:** `partner_value_prop` · `summit_prep`

**Skill version:** 1.0.0 | Standards: BT-2026-Q2 | Terminology: TERM-2026-Q2

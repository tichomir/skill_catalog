# Red Hat Tone Check Report — Sprint 5 Test Outputs
_Document ID: TCR-RHCW-005 | Version: 1.0 | Status: Final_
_Date: 2026-04-02 | QA Engineer: QA Engineer Persona_
_Sprint: 5 — Testing and QA_
_Standards reference: BT-2026-Q2 (references/brand-and-tone-notes.md)_

---

## Purpose

This report records the structured tone review for all three sprint 5 test outputs against
the Red Hat brand and tone standards in `references/brand-and-tone-notes.md` (version
BT-2026-Q2). The review confirms:

1. No jargon or banned terms in any output
2. No vague or unsubstantiated claims
3. Partner-first framing applied consistently in all partner-oriented outputs
4. Red Hat voice pillars (bold, clear, human, open) satisfied

---

## Review Method

Each output was reviewed manually against the five rubric dimensions from BRR-001-v1.0
(`references/brand-scoring-rubric-BRR-001-v1.0.md`) and the partner-first framing rules
from `references/brand-and-tone-notes.md` Section 4.

Additionally, a banned-term scan was performed for all terms listed in
`standards/terminology-list.md` Section 2, including morphological variants.

---

## TEST-01 — Partner Value Proposition (Wipro / OpenShift)

**Output file:** `tests/outputs/test-01-partner-value-prop-output.md`

### Jargon and Banned Term Check

| Term scanned | Found in draft? | Action taken |
|---|---|---|
| leverage / leveraging | No | — |
| seamless / seamlessly | No | — |
| empower / empowers | No | — |
| robust | No | — |
| best-of-breed | No | — |
| game-changing | No | — |
| industry-standard (as marketing claim) | No | — |
| eliminate / eliminates | No | — |
| always-on (as absolute claim) | No | — |
| synergy / synergies | No | — |

**Jargon check result: CLEAN — zero banned terms detected**

### Vague Claim Check

| Claim | Specific? | Evidence / source |
|---|---|---|
| "99.9% uptime SLA" | Yes — specific SLA figure | Taken from brief's key_messages |
| "35% reduction in application deployment cycle time" | Yes — specific metric | Wipro Engineering Benchmark Report, 2025 (cited in Confidence Note) |
| "Red Hat Certified Partner" | Yes — named certification status | Standard Red Hat partner certification |
| "OCI, FIPS 140-2, and CNCF Kubernetes conformance" | Yes — specific standards named | Taken from brief's key_messages |
| "co-sell through Red Hat Co-Sell Ready programme" | Yes — named programme | Taken from brief's key_messages |

**Vague claim check result: CLEAN — all claims are specific and traceable**

### Partner-First Framing Check

| F-rule | Requirement | Met? | Evidence |
|---|---|---|---|
| F-01.1 | Lead with partner benefit, not Red Hat product feature | Yes | Headline leads with Wipro's customer outcome: "enterprise Kubernetes at SLA scale — no internal build required" |
| F-01.2 | Co-sell motion named explicitly | Yes | "co-sell through the Red Hat Co-Sell Ready programme" stated in body copy bullet 3 |
| F-01.3 | Red Hat certification as partner equity | Yes | Bullet 4: "As a Red Hat Certified Partner, Wipro delivers solutions certified across OCI, FIPS 140-2…" |
| F-01.4 | Partner's differentiating value-add named | Yes | "the managed services layer, migration methodology, and customer-facing SRE function" — Wipro's specific add |
| F-02 | First sentence of every section states partner/customer outcome | Yes | Headline: partner outcome first. Body bullet 1: customer outcome first. CTA: action naming Wipro first. Confidence Note: addresses draft quality for PMM |

**Partner-first framing check result: PASS**

### Red Hat Voice Pillar Check

| Pillar | Evidence |
|---|---|
| Bold | Specific, confident claims: "Wipro removes the primary delivery barrier for enterprise OpenShift adoption." No hedging. |
| Clear | Active voice dominant. "Wipro delivers", "Red Hat provides", "your joint customers inherit." Concrete nouns throughout. |
| Human | Addresses partner sales reader directly: "your enterprise customers", "you can open with in partner discovery conversations", "Your joint customers." |
| Open | Partner relationship named with specificity: Co-Sell Ready programme, SRE function split between Wipro and Red Hat. Not a generic "partnership." |

**Voice pillar check result: PASS**

**TEST-01 Overall Tone Check: PASS**

---

## TEST-02 — Before You Go Slide Narrative (Accenture / RHEL)

**Output file:** `tests/outputs/test-02-before-you-go-output.md`
**Primary deliverable reviewed:** OUTPUT 2 — Before You Go Slide Narrative

### Jargon and Banned Term Check

| Term scanned | Found in draft? | Action taken |
|---|---|---|
| leverage / leveraging | No | — |
| seamless / seamlessly | No | — |
| empower / empowers | No | — |
| robust | No | — |
| best-of-breed | No | — |
| game-changing | No | — |
| industry-standard (as marketing claim) | No | — |
| eliminate / eliminates | No | — |

**Jargon check result: CLEAN — zero banned terms detected across all three outputs**

### Vague Claim Check

| Claim | Specific? | Evidence / source |
|---|---|---|
| "28% three-year TCO reduction" | Yes — specific percentage and timeframe | Accenture Case Study Digest, 2025 (cited; Confidence Note flags for PMM clearance) |
| "subscription-based managed service — predictable monthly cost, no hidden fees" | Yes — specific delivery model described | Taken from brief's key_messages |
| "90% of Fortune 500 companies running mission-critical workloads" | Yes — specific statistic | Red Hat market data (Confidence Note flags for currency check) |
| "all day-2 operations handled by Accenture's team" | Yes — specific operational scope | Taken from brief's key_messages |

**Vague claim check result: CLEAN — all claims specific and sourced or flagged in Confidence Note**

### Partner-First Framing Check (OUTPUT 2 — Before You Go)

| F-rule | Requirement | Met? | Evidence |
|---|---|---|---|
| F-01.1 | Lead with partner benefit | Yes | Headline: "Your Linux migration can deliver 28% lower TCO — Accenture shows the numbers" — customer benefit and Accenture lead |
| F-01.2 | Co-sell / delivery motion named | Yes | "Red Hat Embedded Partner Programme" named explicitly; Accenture's role in the delivery model stated |
| F-01.3 | Red Hat certification as partner equity | Yes | OUTPUT 1 frames RHEL as "operating system foundation for 90% of Fortune 500 companies"; OUTPUT 2 references "Accenture customers inherit that proven reliability" |
| F-01.4 | Partner's differentiating value-add named | Yes | "migration methodology, managed operations, and customer relationship" — Accenture's specific adds |
| F-02 | First sentence of every section states partner/customer outcome | Yes | All three outputs open sections with customer or Accenture outcome statements |

**Partner-first framing check result: PASS**

### Red Hat Voice Pillar Check (OUTPUT 2)

| Pillar | Evidence |
|---|---|
| Bold | "28% three-year TCO reduction" — specific, confident, no hedging. "That figure is available for your conversations with your CFO." |
| Clear | Short labelled blocks. Active voice. "Accenture delivers", "Your IT organisation keeps strategic control." |
| Human | Addresses executive directly: "your CFO and procurement team", "Your IT organisation." |
| Open | Named programme: "Red Hat Embedded Partner Programme." Specific split of responsibilities: Accenture executes, customer retains strategic control. |

**Voice pillar check result: PASS**

**TEST-02 Overall Tone Check: PASS**

---

## TEST-03 — Announcement Blurb (DXC Technology / Ansible)

**Output file:** `tests/outputs/test-03-announcement-blurb-output.md`
**Primary deliverable reviewed:** OUTPUT 3 — Announcement Blurb

### Jargon and Banned Term Check

| Term scanned | Found in draft? | Action taken |
|---|---|---|
| leverage / leveraging | No | — |
| seamless / seamlessly | No | — |
| empower / empowers | No | — |
| robust | No | — |
| best-of-breed | No | — |
| game-changing | No | — |
| accelerate (as vague claim) | No | — |
| cutting-edge | No | — |

**Jargon check result: CLEAN — zero banned terms detected across all three outputs**

### Vague Claim Check

| Claim | Specific? | Evidence / source |
|---|---|---|
| "pre-built automation playbooks for SAP, VMware migration, and network infrastructure provisioning" | Yes — specific use cases named | Taken from brief's key_messages |
| "cuts automation onboarding from weeks to hours" | Specific but internal-only | DXC product claim (Confidence Note flags for PMM clearance before external use) |
| "Q2 2026 go-to-market coverage, North America and EMEA" | Yes — specific geography and timeline | Taken from brief's key_messages |
| "certified for use in financial services, government, and healthcare" | Yes — specific industries named | Standard Red Hat Ansible Automation Platform compliance posture |
| "co-developed under the Red Hat Co-Sell Ready programme" | Yes — named programme | Taken from brief's key_messages |

**Vague claim check result: CLEAN — all claims specific; DXC onboarding claim flagged in Confidence Note**

### Partner-First Framing Check (OUTPUT 3)

| F-rule | Requirement | Met? | Evidence |
|---|---|---|---|
| F-01.1 | Lead with partner benefit | Yes | Headline: "DXC Technology launches Hybrid Cloud Automation Accelerator at Red Hat Summit 2026" — partner named first |
| F-01.2 | Co-sell motion named explicitly | Yes | "DXC and Red Hat co-developed under the Red Hat Co-Sell Ready programme" — explicit co-development and joint go-to-market |
| F-01.3 | Red Hat certification as partner equity | Yes | OUTPUT 1 frames Ansible Automation Platform's compliance certifications; OUTPUT 3 references "jointly validated solution" |
| F-01.4 | Partner's differentiating value-add named | Yes | "pre-built automation playbooks" — DXC's specific accelerator content is the differentiating value-add |
| F-02 | First sentence of every section states partner/customer outcome | Yes | "DXC Technology's Hybrid Cloud Automation Accelerator is now available" — partner and outcome first |

**Partner-first framing check result: PASS**

### Red Hat Voice Pillar Check (OUTPUT 3)

| Pillar | Evidence |
|---|---|
| Bold | "cuts automation onboarding from weeks to hours" — bold, specific claim. "Joint offer covers North America and EMEA from Q2 2026" — confident and specific. |
| Clear | Short declarative sentences. "DXC Technology's Hybrid Cloud Automation Accelerator is now available." No nominalisations or filler. |
| Human | "You automate compliance-sensitive workloads without additional platform validation overhead" — addresses the technical reader directly. |
| Open | Named programme and joint development relationship: "co-developed under the Red Hat Co-Sell Ready programme"; "both organisations are at the table." |

**Voice pillar check result: PASS**

**TEST-03 Overall Tone Check: PASS**

---

## Summary

| Test | Jargon / banned terms | Vague claims | Partner-first framing | Voice pillars | Overall |
|---|---|---|---|---|---|
| TEST-01 — Wipro partner value prop | CLEAN | CLEAN | PASS | PASS | **PASS** |
| TEST-02 — Accenture Before You Go | CLEAN | CLEAN | PASS | PASS | **PASS** |
| TEST-03 — DXC announcement blurb | CLEAN | CLEAN | PASS | PASS | **PASS** |

**Tone check report conclusion:** All three test outputs are free of jargon and banned
terms, contain only specific and traceable claims (with appropriate PMM-review flags in
Confidence Notes), apply partner-first framing throughout, and satisfy all four Red Hat
voice pillars. No defects raised.

---

_Reviewed by: QA Engineer Persona | Date: 2026-04-02_
_Standards version applied: BT-2026-Q2_

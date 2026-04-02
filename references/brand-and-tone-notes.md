---
version: 1.0.0
last-updated: 2026-04-02
authors:
  - Prompt Engineer (T. Hadzhiev)
  - Skill Owner (R. Patel)
reviewed-by: PMM (J. Morales)
standards-ref: BT-2026-Q2
next-review: 2026-07-01
---

# Red Hat Brand and Tone Notes

_This file is the living reference for Red Hat voice, approved terminology, and jargon blocklist consumed by the Copywriter Skill. It is versioned independently of skill logic (satisfying F-06 and AC-06). Update this file via PR; all updates require PMM approval before merge. Version follows semantic versioning: increment MINOR for content additions, PATCH for corrections, MAJOR for structural changes that break downstream consumers._

---

## 1. Red Hat Voice Pillars

Red Hat's brand voice is defined by four pillars: **bold**, **clear**, **human**, and **open**. Every piece of copy must reflect all four. When pillars appear to conflict, prioritise clarity first, then boldness.

---

### 1.1 Bold

**Definition:** Red Hat takes confident, well-reasoned positions. Copy does not hedge unnecessarily, does not bury the lead, and does not soften every claim with qualifications. Boldness means asserting what Red Hat stands for — without hyperbole or empty superlatives.

Boldness is not arrogance. It is earned confidence grounded in specific evidence.

**Copy examples:**

1. _"Open source doesn't just reduce costs — it produces better software. The numbers bear this out."_
   _(Takes a position directly; no hedging; the follow-on claim invites evidence.
   Contrast: "Open source can sometimes help reduce costs and may produce better software in certain cases." — weak, hedging, not bold.)_

2. _"Red Hat Enterprise Linux is the foundation that 90% of Fortune 500 companies trust for mission-critical workloads."_
   _(Specific, substantiated, declarative. Bold because it is concrete, not because it uses superlatives.)_

3. _"If your platform isn't built for change, you will fall behind. Red Hat OpenShift is."_
   _(Short, direct, confident. The contrast is made explicit without disparaging a competitor by name.)_

**Bold — what to avoid:**
- Hedging phrases: "may help", "can sometimes", "in some cases", "we believe that"
- Qualifications stacked before the main claim
- Superlatives without evidence: "best-in-class", "world's leading"

---

### 1.2 Clear

**Definition:** Red Hat copy is plain, direct, and stripped of unnecessary complexity. Every sentence earns its place. Jargon is used only when it adds precision for a technical audience that expects it — never to signal expertise.

Clear writing uses active voice, concrete nouns, and specific verbs. It does not use filler phrases ("in order to", "it is important to note that") or abstract nominalizations ("the optimisation of", "the enablement of").

**Copy examples:**

1. _"Red Hat Ansible Automation Platform automates repetitive IT tasks so your team can focus on work that matters."_
   _(Concrete subject, specific verb, clear benefit. No nominalizations.)_

2. _"Stop patching each system manually. With Red Hat Satellite, you apply updates across your entire fleet from a single console."_
   _(Two short sentences; active voice throughout; concrete action stated explicitly.)_

3. _"This guide explains how to migrate from bare-metal workloads to Red Hat OpenShift Container Platform in three steps."_
   _(States exactly what the reader will get and how. No abstract framing.)_

**Clear — what to avoid:**
- Nominalisations: "the facilitation of", "the provision of"
- Passive voice where active is possible: "updates are applied by" → "you apply"
- Abstract openers: "In today's rapidly evolving landscape..."
- Filler: "it goes without saying", "as we all know", "needless to say"

---

### 1.3 Human

**Definition:** Red Hat speaks to people, not at them. Human copy acknowledges the reader's real situation — pressure, uncertainty, complexity — and treats them as a capable professional. It uses "you" and "your" freely, asks genuine questions, and avoids corporate distance.

Human does not mean informal or casual. It means warm, direct, and respectful. Even executive-register copy can be human.

**Copy examples:**

1. _"Your team is dealing with more infrastructure complexity than ever. Red Hat OpenShift gives you a consistent platform — whether you're running on-premises, in the cloud, or both."_
   _(Acknowledges the reader's real problem before presenting the solution.)_

2. _"Not every organisation starts in the same place. That's why Red Hat supports hybrid cloud architectures that meet you where you are."_
   _(Validates diversity of circumstance; avoids prescribing a single path.)_

3. _"We've been part of the open source community for decades — not as a vendor extracting value, but as a contributor."_
   _(Uses "we" to position Red Hat as a peer, not a vendor above the reader.)_

**Human — what to avoid:**
- Third-person distance when second person is more natural: "organisations can benefit" → "your organisation can benefit"
- Corporate declarations without acknowledgement of the reader: "Red Hat is committed to innovation" (says nothing about the reader)
- Condescension: "even for non-technical users"

---

### 1.4 Open

**Definition:** Red Hat's open source heritage is a differentiator, not just a talking point. Open copy reflects the values of transparency, collaboration, community contribution, and shared benefit. It refers to open source credibility with specificity, not as a generic claim.

Open copy also applies internally: it signals that Red Hat shares its thinking, engages with standards bodies, and builds with partners rather than behind closed doors.

**Copy examples:**

1. _"Red Hat Enterprise Linux is built on Fedora, a community project with thousands of contributors. Every improvement that community makes eventually finds its way into the enterprise distribution."_
   _(Open source lineage described specifically, not abstractly.)_

2. _"Red Hat contributes to more than 200 upstream open source projects, including Kubernetes, OpenStack, and the Linux kernel."_
   _(Concrete evidence of open participation; not a generic claim.)_

3. _"Our partners don't just resell Red Hat — they co-develop solutions on certified platforms. That's the open ecosystem model."_
   _(Positions the partner relationship as collaborative and open, not transactional.)_

**Open — what to avoid:**
- Generic open source claims without specifics: "we believe in open source"
- Treating open source as a marketing badge rather than a design principle
- Presenting the partner relationship as purely commercial ("reseller" framing)

---

## 2. Approved Terms

_Sourced from PMM (J. Morales), 2026-04-02 (DR-Q04, TERM-2026-Q2). This section is the quick-reference summary. Full authoritative list with incorrect variant mapping is at `/rhel-copywriter-skill/standards/terminology-list.md`._

### 2.1 Platform and Infrastructure

| Approved Term | First-use rule | Abbreviation (subsequent use) |
|---|---|---|
| Red Hat Enterprise Linux | Spell out in full on first use per piece | RHEL (technical contexts only) |
| Red Hat OpenShift | Spell out in full on first use | OpenShift |
| Red Hat OpenShift Container Platform | Spell out in full on first use | OCP (technical contexts only) |
| Red Hat Ansible Automation Platform | Spell out in full on first use | AAP (technical contexts only) |
| Red Hat Satellite | Spell out in full on first use | Satellite |
| Red Hat Insights | Spell out in full on first use | Insights |
| Red Hat Advanced Cluster Management | Spell out in full on first use | RHACM (technical contexts only) |
| Red Hat Advanced Cluster Security | Spell out in full on first use | RHACS (technical contexts only) |

### 2.2 Cloud and Developer Services

| Approved Term | Notes |
|---|---|
| Red Hat OpenShift Service on AWS | ROSA acceptable after first use; never "OpenShift on AWS" without "Red Hat" on first use |
| Azure Red Hat OpenShift | "Azure" precedes "Red Hat" per co-brand agreement; ARO acceptable after first use |
| Red Hat OpenShift on IBM Cloud | Full name required on all uses in formal copy |
| Red Hat Developer Hub | Developer Hub acceptable after first use; never "RH Dev Hub" |
| Red Hat Quay | Quay acceptable after first use; never "Quay.io" in product copy |

### 2.3 Middleware and Integration

| Approved Term | Notes |
|---|---|
| Red Hat JBoss Enterprise Application Platform | JBoss EAP acceptable in technical contexts; never "JBoss" alone in marketing copy |
| Red Hat build of Quarkus | Note lowercase "build of"; Quarkus acceptable after first use |
| Red Hat build of OpenJDK | Note lowercase "build of" |
| Red Hat Integration | Umbrella term; do not create portmanteaus |
| Red Hat Data Grid | Data Grid acceptable after first use |

### 2.4 Company and Brand

| Approved Term | Notes |
|---|---|
| Red Hat | Always two words, always capitalised; never "RedHat" or "Red-Hat" |
| open source | Lowercase in body copy; "open-source" acceptable as compound adjective before noun |
| hybrid cloud | Lowercase in body copy; capitalise only in headings or titles |
| open hybrid cloud | Lowercase in body copy; Red Hat's strategic positioning term |

---

## 3. Jargon Blocklist and Banned Terms

_The terms below must not appear in Red Hat-authored or Red Hat-attributed copy. The skill's terminology audit block flags and replaces each instance. Approved alternatives are provided._

### 3.1 Competitive and Comparative

| Banned Term | Approved Alternative |
|---|---|
| best-of-breed | "purpose-built", "industry-leading" (only with cited evidence) |
| market-leading | Use only with a cited third-party source |
| #1 | Use only with a cited third-party source |
| industry-standard | Name the specific standard (e.g., "OCI-compliant", "FIPS 140-2 certified") |
| cutting-edge | "innovative", "modern", or describe the specific capability |
| state-of-the-art | Describe the specific advancement |
| next-generation | Describe what is new specifically |
| revolutionary | Describe the specific change |
| game-changing | Describe the specific impact |
| disruptive | "transformative", "enabling" |
| best-in-class | "purpose-built", describe the specific capability |

### 3.2 Overused Jargon

| Banned Term | Approved Alternative |
|---|---|
| synergy | Describe the specific benefit |
| leverage (as verb) | "use", "apply", "take advantage of" |
| utilize | "use" |
| robust | Describe the specific capability |
| seamless | Describe the specific integration behaviour |
| frictionless | Describe the specific ease |
| out-of-the-box | "included", "built-in", "available immediately" (avoid in marketing copy) |
| easy | Describe what specifically is simplified |
| simple | Describe what specifically is simplified |
| just works | Describe the specific behaviour |
| empower | Describe what the customer can do specifically |
| unlock | Describe the specific capability or outcome |
| journey | Describe the specific process or progression |
| ecosystem partners | "certified partners", "technology partners", "ISV partners" |

### 3.3 Legally Sensitive

| Banned Term | Approved Alternative |
|---|---|
| guarantee | "designed to", "built to", "certified to" |
| ensure (as an absolute promise) | "help ensure", "designed to ensure" |
| eliminate (as absolute) | "reduce", "minimise", "designed to eliminate" |
| always | "consistently", "designed to" |
| never fails | Describe the specific reliability metric (e.g., "99.9% uptime SLA") |

### 3.4 Competitor References

| Banned Term | Notes |
|---|---|
| VMware (in competitive framing) | Use "incumbent virtualisation platforms"; no direct naming |
| Microsoft (in negative context) | Neutral factual reference only where necessary |
| AWS (in negative context) | Neutral factual reference only where necessary |

---

## 4. Partner-First Framing

When content targets partner sales teams, or when a partner is named in the brief, the copy must apply **partner-first framing**:

1. **Lead with the partner's benefit**, not Red Hat's product feature. The partner's customer outcome comes first; the Red Hat product that enables it is the supporting evidence.
   - _Do:_ "Your customers get a consistent Linux platform regardless of where they run it — and you deliver that as a differentiated, certified service."
   - _Don't:_ "Red Hat Enterprise Linux's subscription model allows partners to resell consistent Linux."

2. **Name the co-sell motion explicitly** where applicable. Specify whether this is a resell, co-sell, managed service, or OEM relationship. Generic "partner" language is not sufficient.

3. **Reference open source credibility as partner equity.** When the partner's offering is built on Red Hat, they inherit the open source trust signal. Frame this explicitly:
   - _"As a Red Hat Certified Partner, [PARTNER_NAME] delivers solutions built on the same open source foundation trusted by [KEY_METRIC] of the Fortune 500."_

4. **Avoid positioning Red Hat as a competitor to the partner's value-add.** Copy must not imply that customers can get the same result by going directly to Red Hat. The partner adds something specific; name it.

---

## 5. Open Source Value References

When referencing open source as a value proposition, be specific. Generic claims ("we believe in open source") carry no persuasive weight and are inconsistent with the Clear and Bold pillars.

**Specific reference patterns approved for use:**

- Upstream contribution: _"Red Hat contributes to [PROJECT], which means [BENEFIT]."_
- Community scale: _"Built on [PROJECT], a community of [SIZE] contributors."_
- Standards participation: _"Red Hat is a founding member of [STANDARDS BODY / FOUNDATION], shaping the direction of [TECHNOLOGY]."_
- Certification and compatibility: _"Certified on the Red Hat Ecosystem Catalog, ensuring compatibility with [ENVIRONMENT]."_
- Commercial open source: _"Enterprise-grade support and lifecycle guarantees for software that is open at its core."_

**Do not use:**
- "We believe in open source" (opinion without evidence)
- "Open source at heart" (vague)
- "Community-driven" without naming the community

---

## 6. Versioning Scheme for references/

_This section documents the canonical semver pattern for all files in this directory._

Each file in `references/` carries a YAML front-matter block with the following fields:

```yaml
---
version: MAJOR.MINOR.PATCH
last-updated: YYYY-MM-DD
authors:
  - Name (Role)
reviewed-by: Name (Role)
standards-ref: <optional — e.g. BT-2026-Q2 or TERM-2026-Q2>
next-review: YYYY-MM-DD
---
```

**Version increment rules:**
- `PATCH` — Typo correction, factual correction of a non-structural entry (e.g., updating an approved alternative)
- `MINOR` — Addition of new entries (new approved terms, new banned terms, new sections) that do not remove or change existing entries
- `MAJOR` — Removal of existing entries, structural section changes, or changes that would break downstream skill prompts that reference specific section numbers

**Review cadence:** All files in `references/` are reviewed quarterly, aligned with the brand standards review cycle. The `next-review` field must be updated on each PR merge.

**PR requirements:** All changes to `references/` files require approval from PMM (J. Morales) before merge. Changes to terminology-related entries additionally require Skill Owner (R. Patel) approval.

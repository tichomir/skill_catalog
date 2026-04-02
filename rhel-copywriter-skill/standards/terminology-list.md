# Red Hat Approved Terminology List
_Version: TERM-2026-Q2 | Last updated: 2026-04-02 | Next review: 2026-07-01_
_Sourced from: J. Morales (PMM) on 2026-04-02 — see /docs/decision-record-Q04.md for full provenance_

> **Q-04 Resolution:** This file satisfies decision record DR-Q04. The terminology list was sourced directly from PMM (J. Morales) and is the authoritative input for the skill's terminology audit capability (PRD Section 5). See `/docs/decision-record-Q04.md` for full context, rationale, and refresh process.

---

## 1. Approved Product and Brand Names

The following names must be used exactly as written. Capitalisation, spacing, and hyphenation are normative.

### 1.1 Platform and Infrastructure

| Approved Term | Common Incorrect Variants | Notes |
|---|---|---|
| Red Hat Enterprise Linux | RHEL (acceptable in technical contexts after first use), RedHat Linux, Red Hat Linux | Always spell out on first use per piece |
| Red Hat OpenShift | OpenShift alone (first use), Openshift, Open Shift | Red Hat OpenShift on first use; OpenShift acceptable thereafter |
| Red Hat OpenShift Container Platform | OCP (acceptable in technical contexts after first use) | |
| Red Hat Ansible Automation Platform | Ansible alone (first use), AAP (acceptable in technical contexts) | |
| Red Hat Satellite | Satellite (acceptable after first use) | |
| Red Hat Insights | Insights (acceptable after first use) | |
| Red Hat Advanced Cluster Management | RHACM (acceptable in technical contexts) | |
| Red Hat Advanced Cluster Security | RHACS (acceptable in technical contexts) | |

### 1.2 Developer and Cloud Services

| Approved Term | Common Incorrect Variants | Notes |
|---|---|---|
| Red Hat OpenShift Service on AWS | ROSA (acceptable after first use) | Do not write "OpenShift on AWS" without "Red Hat" on first use |
| Azure Red Hat OpenShift | ARO (acceptable after first use) | Note: "Azure" precedes "Red Hat" per Microsoft co-brand agreement |
| Red Hat OpenShift on IBM Cloud | — | Full name required on all uses in formal copy |
| Red Hat Developer Hub | Developer Hub (acceptable after first use) | Do not abbreviate as "RH Dev Hub" |
| Red Hat Quay | Quay (acceptable after first use) | Not "Quay.io" in product copy |

### 1.3 Middleware and Integration

| Approved Term | Common Incorrect Variants | Notes |
|---|---|---|
| Red Hat JBoss Enterprise Application Platform | JBoss EAP (acceptable in technical contexts) | Do not use "JBoss" alone in marketing copy |
| Red Hat build of Quarkus | Quarkus (acceptable after first use) | Note lowercase "build of" |
| Red Hat build of OpenJDK | OpenJDK (acceptable in technical contexts) | |
| Red Hat Integration | — | Umbrella term; do not create portmanteaus |
| Red Hat Data Grid | Data Grid (acceptable after first use) | |

### 1.4 Security and Compliance

| Approved Term | Common Incorrect Variants | Notes |
|---|---|---|
| Red Hat OpenShift Platform Plus | Platform Plus (acceptable after first use) | |
| Red Hat Trusted Software Supply Chain | TSSC (acceptable in technical contexts) | |

### 1.5 Company and Brand

| Approved Term | Common Incorrect Variants | Notes |
|---|---|---|
| Red Hat | RedHat, Red-Hat, red hat | Always two words, always capitalised |
| open source | open-source (as adjective before noun is acceptable), Open Source | Lowercase unless at sentence start or in title |
| hybrid cloud | Hybrid Cloud (except in titles), hybrid-cloud | Lowercase in body copy |
| open hybrid cloud | Open Hybrid Cloud (in titles only) | Red Hat's strategic positioning term |

---

## 2. Banned Terms

The following terms must not appear in Red Hat-authored or Red Hat-attributed copy under any circumstances. The skill's terminology audit block must flag each of these terms and provide the approved alternative.

### 2.1 Competitive and Comparative

| Banned Term | Reason | Approved Alternative |
|---|---|---|
| best-of-breed | Overused, vague, legally reviewable in some jurisdictions | "purpose-built", "industry-leading" (with evidence) |
| market-leading | Requires substantiation; banned without citation | Use only with a cited third-party source |
| #1 | Requires substantiation; banned without citation | Use only with a cited third-party source |
| industry-standard | Overused, vague | Describe the specific standard (e.g., "OCI-compliant") |
| cutting-edge | Cliché; inconsistent with Red Hat voice | "innovative", "modern", specific capability description |
| state-of-the-art | Cliché | Describe the specific advancement |
| next-generation | Vague, overused | Describe what is new specifically |
| revolutionary | Hyperbolic | Describe the specific change |
| game-changing | Hyperbolic | Describe the specific impact |
| disruptive | Overused; negative connotation risk | "transformative", "enabling" |

### 2.2 Competitor Names (direct reference)

| Banned Term | Reason | Approved Alternative |
|---|---|---|
| VMware | Do not name competitors in copy; legal risk | "incumbent virtualisation platforms" |
| Microsoft (in negative context) | Do not disparage competitors | Neutral factual reference only where necessary |
| AWS (in negative context) | Do not disparage competitors | Neutral factual reference only where necessary |

### 2.3 Internal Jargon

| Banned Term | Reason | Approved Alternative |
|---|---|---|
| synergy | Jargon | Describe the specific benefit |
| leverage (as verb) | Jargon; banned per Red Hat style guide | "use", "apply", "take advantage of" |
| utilize | Unnecessarily formal | "use" |
| robust | Overused filler adjective | Describe the specific capability |
| seamless | Overused, unsubstantiated | Describe the specific integration |
| frictionless | Overused | Describe the specific ease |
| out-of-the-box | Acceptable in technical docs; avoid in marketing copy | "included", "built-in", "available immediately" |
| easy | Unsubstantiated claim | Describe what specifically is simplified |
| simple | Unsubstantiated claim | Describe what specifically is simplified |
| just works | Informal, unsubstantiated | Describe the specific behaviour |
| empower | Overused in tech marketing | Describe what the customer can do specifically |
| unlock | Overused | Describe the specific capability or outcome |
| journey | Overused metaphor | Describe the specific process or progression |
| ecosystem partners | Vague | "certified partners", "technology partners", "ISV partners" |

### 2.4 Legally Sensitive

| Banned Term | Reason | Approved Alternative |
|---|---|---|
| guarantee | Legal; requires legal review to use | "designed to", "built to", "certified to" |
| ensure (as an absolute promise) | Legal risk | "help ensure", "designed to ensure" |
| eliminate (as absolute) | Legal risk | "reduce", "minimise", "designed to eliminate" |
| always | Absolute claim; legal risk | "consistently", "designed to" |
| never fails | Absolute claim; legal risk | Describe the specific reliability metric (e.g., "99.9% uptime SLA") |

---

## 3. Terminology Refresh Process

1. PMM reviews and updates this list quarterly (aligned with brand standards review).
2. Updates are submitted as a PR to `/rhel-copywriter-skill/standards/terminology-list.md`.
3. PR requires approval from PMM and Skill Owner before merge.
4. Version stamp is incremented (`TERM-YYYY-QN`) on each approved update.
5. Skill is redeployed with incremented MINOR version following terminology updates.

---

_Sourced from J. Morales (PMM) on 2026-04-02. Version TERM-2026-Q2. This list supersedes any prior informal terminology guidance._

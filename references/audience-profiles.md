---
version: 1.0.0
last-updated: 2026-04-02
authors:
  - Prompt Engineer (T. Hadzhiev)
  - Skill Owner (R. Patel)
reviewed-by: PMM (J. Morales)
next-review: 2026-07-01
---

# Audience Profiles

_This file defines differentiated copywriting guidance for the three audience segments supported by the Red Hat Copywriter Skill. Each profile provides the mindset summary, tone variant to apply, copy do's and don'ts, and an annotated example snippet. The skill uses the `target_audience` field of the input brief to select the appropriate profile and calibrate register, vocabulary, and assumed knowledge accordingly._

_Versioned independently of skill logic. Update via PR with PMM approval. See `references/brand-and-tone-notes.md` Section 6 for the versioning scheme._

---

## Audience Segment 1 — Technical Decision Makers

**`target_audience` values that map here:** "IT architect", "enterprise architect", "technical decision maker", "infrastructure lead", "platform engineer", "DevOps lead", "CTO" (technical framing)

---

### 1.1 Mindset Summary

Technical decision makers evaluate platforms and products on architecture fit, integration depth, operational risk, and long-term maintainability. They are not sold to by feature lists — they are persuaded by specificity, by evidence of real-world scale, and by the credibility of the upstream community behind the technology.

Their primary concerns:
- **Architecture coherence:** Does this fit into what we already run? What does the integration surface look like?
- **Operational risk:** What happens when things break? Who supports it? What is the upgrade path?
- **OSS credibility:** Is this genuinely open, or open-core with a proprietary lock-in tail?
- **Standards compliance:** Does it conform to OCI, CNCF, POSIX, or other standards my team already knows?
- **Team capability:** Can my team operate this without a steep retraining curve?

They are suspicious of marketing language. Generic claims ("best-in-class security", "seamless integration") erode trust. Specificity builds it.

---

### 1.2 Tone Variant

Apply the **`technical`** tone variant (see design spec F-03 tone table):

- Register: Technical, precise
- Sentence style: Active voice; specific verbs; avoid passive constructions unless the subject is genuinely unknown
- Pronoun preference: "you" (as practitioner); "Red Hat" in third person when discussing the company
- Vocabulary: Use correct technical terminology; acronyms acceptable after first-use spell-out; do not avoid jargon, but define it on first use if it is Red Hat-specific
- Length preference: Shorter is better; no padding; every sentence makes a technical claim or states a consequence

---

### 1.3 Copy Do's

- **Name the integration point.** If the product integrates with Kubernetes, name the API, the operator, the CRD surface. Don't say "integrates with your existing environment."
- **Reference upstream projects.** Technical readers evaluate products partly by their relationship to the community. Name the upstream project, the CNCF incubation status, the number of maintainers if relevant.
- **Quantify operational claims.** "Reduces patching time" is weak. "Applies OS-level patches across 500 nodes in under 10 minutes using Red Hat Satellite's batch scheduling" is credible.
- **Describe the failure mode and recovery.** Technical decision makers think about what happens when things break. Acknowledge resilience design, SLA, and support path explicitly.
- **Use correct product names from first mention.** See `references/brand-and-tone-notes.md` Section 2 for approved abbreviations after first use.
- **Cite standards compliance specifically.** "OCI-compliant", "FIPS 140-2 certified", "CNCF conformant" — name the standard, not a vague claim.

---

### 1.4 Copy Don'ts

- Do not use superlatives without evidence: "most secure", "fastest", "most reliable"
- Do not open with business outcomes — lead with the technical capability; business outcomes are secondary context
- Do not oversimplify architecture: saying a migration "just works" or is "simple" without describing the steps is a credibility loss
- Do not use passive voice where the agent matters: "patches are applied" obscures whether the engineer applies them, the tool applies them, or they apply automatically — state which
- Do not use jargon that is Red Hat-internal or marketing-invented without defining it: "open hybrid cloud" needs a one-sentence definition before use in technical copy

---

### 1.5 Annotated Example

**Scenario:** Solution brief for Red Hat OpenShift Container Platform, targeting an enterprise architect evaluating container platform migration.

```
Red Hat OpenShift Container Platform 4.x runs as a Kubernetes-native
platform on bare metal, VMware vSphere, AWS, Azure, and IBM Cloud —
using the same declarative API surface across all targets.
                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                    Technical claim: specificity about
                                    cross-environment API consistency,
                                    not a vague "runs anywhere" claim.

The platform is CNCF Kubernetes conformant and ships with an
integrated operator lifecycle manager, allowing teams to manage
day-2 operations — upgrades, scaling, configuration drift — through
the same GitOps pipeline used for application delivery.
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
         Operational specificity: names the capability (OLM),
         names the workflow (GitOps), names the day-2 concerns
         the reader cares about. No padding.

For organisations running FIPS-restricted workloads, Red Hat
OpenShift Container Platform is certified for FIPS 140-2 operation
in RHCOS, the purpose-built immutable OS layer.
                                ^^^^^^^^^^^^^^
                                Standards reference is named
                                precisely. No vague "secure" claim.
```

---

## Audience Segment 2 — Business Executives

**`target_audience` values that map here:** "C-suite", "CEO", "CFO", "COO", "VP of IT", "business executive", "executive sponsor", "board-level stakeholder"

---

### 2.1 Mindset Summary

Business executives make decisions about technology through a business lens: financial exposure, strategic risk, competitive positioning, and organisational capability. They delegate technical evaluation to architects and engineers. What they need from copy is confidence that they are making a strategically sound decision — not a technical deep-dive.

Their primary concerns:
- **Business outcomes:** What does this produce for the business — revenue, cost reduction, speed, risk reduction?
- **Risk profile:** What is the risk of doing this? What is the risk of *not* doing this?
- **ROI and TCO:** What does this cost, and what is the return? What are the hidden costs of incumbents or alternatives?
- **Organisational readiness:** Do we have the skills? Will this create new dependencies?
- **Strategic alignment:** Does this fit our direction — cloud, modernisation, compliance posture?

Executives are time-constrained. They process copy at the paragraph level, not the sentence level. Headlines and subheadings carry disproportionate weight. Body copy must be scannable and lead with the conclusion.

---

### 2.2 Tone Variant

Apply the **`executive`** tone variant (see design spec F-03 tone table):

- Register: Strategic, concise
- Sentence style: Short, declarative; state the conclusion first, then the support
- Pronoun preference: "your organisation", "your teams", "your business" — not "you" (too informal for formal executive copy)
- Vocabulary: Avoid technical acronyms unless already part of the executive's vocabulary; use business-domain terms (TCO, SLA, risk posture, compliance)
- Length preference: Shortest possible; every paragraph has one point; use bullets for scannable evidence lists

---

### 2.3 Copy Do's

- **Lead with the business outcome, not the product.** The first sentence of any section should state what the business gains, not what the product does.
- **Quantify where possible.** "$X saved", "Y% reduction in downtime", "Z weeks faster to deploy" — even ranges or cited industry figures are better than qualitative claims.
- **Frame the cost of inaction.** Executive audiences respond to risk framing. What does delay or inaction cost? Name it.
- **Use "your organisation" framing throughout.** This makes the copy feel specific to the reader's situation even when it is general.
- **Reference third-party validation.** Analyst citations (Gartner, IDC, Forrester), customer references, and certifications carry more weight with executives than Red Hat's own claims.
- **State the strategic positioning explicitly.** Connect the product or solution to the executive's stated strategic priorities (cloud, modernisation, regulatory compliance, open source strategy).

---

### 2.4 Copy Don'ts

- Do not lead with technical architecture — executives route that to their teams
- Do not use unexplained technical acronyms: "OCP", "RHACM", "GitOps" need business-language translations first
- Do not make the copy feel like a feature list — each feature claim must map to a business outcome
- Do not use abstract mission-statement language: "Red Hat is committed to innovation" — this says nothing to an executive
- Do not bury the key business case in paragraph three — executives often read only the first paragraph and the bullets

---

### 2.5 Annotated Example

**Scenario:** Executive summary section of a solution brief for Red Hat OpenShift, targeting a CFO evaluating cloud infrastructure spend.

```
Organisations running mixed cloud environments spend an average of
37% more on infrastructure management than those on a consistent
platform, according to IDC's 2025 Hybrid Cloud Operations report.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Lead with a cited third-party business outcome, not a product
feature. The CFO processes this as a risk signal about their
own organisation.

Red Hat OpenShift consolidates container workloads across on-premises
data centres, AWS, and Azure onto a single operational model — reducing
the number of tools your teams manage and the training overhead
associated with operating separate environments.
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
              Business framing of a technical benefit:
              "fewer tools" and "less training overhead"
              are CFO-legible costs, not technical features.

Organisations that have standardised on Red Hat OpenShift report
a 40% reduction in time-to-production for new applications and a
25% reduction in unplanned downtime. [Source: Red Hat Customer Survey, 2025]
                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                       Cite the source. Unsourced
                                       quantitative claims weaken
                                       credibility with executives.
```

---

## Audience Segment 3 — Partner Sales Teams

**`target_audience` values that map here:** "partner sales", "channel partner", "reseller", "ISV partner", "GSI partner", "co-sell partner", "partner SE", "partner account manager"

---

### 3.1 Mindset Summary

Partner sales teams operate in a dual mode: they must understand the Red Hat value proposition well enough to articulate it, and they must connect it to their own customer base's specific needs. Their primary motivation is closing their deals — Red Hat is a means to that end, not the end itself.

Their primary concerns:
- **Partner benefit first:** How does selling or embedding this solution benefit the partner's business? Margin, differentiation, stickiness, MDF eligibility?
- **Co-sell motion clarity:** What does the co-sell motion look like? Who leads? What does Red Hat bring to the table?
- **Customer conversation enablement:** What are the conversation-starter questions? What objections will the partner face, and how do they handle them?
- **Certification and support path:** What does the partner need to be certified to sell or deliver this? What support do they get post-sale?
- **Competitive differentiation:** How is this positioned against the incumbent the customer is already running?

Partners are practical. They want to know what to say to which customer, and why it wins. They do not have time for abstract brand messaging.

---

### 3.2 Tone Variant

Apply the **`standard`** tone variant with explicit partner-first framing (see `references/brand-and-tone-notes.md` Section 4):

- Register: Professional, direct, enabling
- Sentence style: Active; short; oriented toward action ("you can", "your customer will", "Red Hat brings")
- Pronoun preference: "you" for the partner; "your customer" for the end customer; "we" (Red Hat) only when describing what Red Hat provides to the partner
- Vocabulary: Business and sales vocabulary; limited technical jargon unless the partner audience is technical (e.g., partner SEs)
- Length preference: Modular — partners scan for the section relevant to their deal; use clear headings and bullets

---

### 3.3 Copy Do's

- **Open with the partner's commercial benefit.** What does the partner earn, retain, or differentiate by including this in their offer?
- **Name the co-sell motion explicitly.** Resell, co-sell, OEM, managed service — specify the relationship model and what each party owns.
- **Frame Red Hat certification as partner equity.** Certified partner status signals to customers that the partner's solution is built on a trusted, enterprise-grade foundation. Say this explicitly.
- **Provide customer conversation hooks.** Give the partner a discovery question or a pain-point framing that opens the conversation in their accounts.
- **Reference the Red Hat Ecosystem Catalog.** Partners listed there get discoverability from Red Hat's sales team; name this benefit when relevant.
- **Connect to existing partner programs.** Named programs (Red Hat Partner Connect, Co-Sell Ready) are relevant context; include them when they add value to the partner's decision.

---

### 3.4 Copy Don'ts

- Do not lead with Red Hat's product feature — lead with the partner's customer outcome and work back
- Do not write generic "partner" copy that applies to every partner equally — name the partner motion type and make the copy specific to it
- Do not position Red Hat as going around the partner to the end customer: the partner must feel that Red Hat amplifies their reach, not competes with it
- Do not use internal Red Hat program names or acronyms without a brief explanation: "MDF", "CCSP", "Co-Sell Ready" need one-line glosses the first time they appear
- Do not omit the certification or training path: partners need to know what it costs them to get qualified to sell

---

### 3.5 Annotated Example

**Scenario:** Partner enablement page for a systems integrator co-selling Red Hat OpenShift with their managed cloud services offering.

```
Your customers are asking for cloud-native platforms — but they don't
want to manage Kubernetes themselves. That's where your managed
OpenShift offering delivers what a direct cloud provider can't: a
fully managed, expert-operated container platform with enterprise SLAs,
built on the same technology Red Hat supports globally.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Partner-first opening: the partner's commercial opportunity
("managed OpenShift offering") is named before Red Hat's product.
The competitive positioning against hyperscalers is implicit
without disparaging by name.

As a Red Hat Certified Partner, you inherit the trust signals that
Red Hat has built with [KEY_METRIC] enterprise customers worldwide.
Your customers don't need to evaluate the platform from scratch —
Red Hat's certification means your solution starts from a validated
foundation.
^^^^^^^^^^^
Open source and certification framing as partner equity:
the partner benefits from Red Hat's credibility. "You inherit"
is explicit partner-benefit language.

The co-sell motion is straightforward: Red Hat brings the platform
SLA and the upstream support relationship. You bring the managed
service wrapper, the customer relationship, and the migration
expertise. Red Hat's partner team is available for joint customer
calls on qualified opportunities.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Co-sell motion named explicitly: roles are clear.
"Red Hat brings / You bring" structure makes the
division of value unambiguous.
```

---

## Audience Calibration Notes

When the input brief's `target_audience` field does not map cleanly to one of the three segments above, apply the following fallback logic:

1. **Mixed audience (e.g., "IT and business stakeholders"):** Default to the executive profile for the overarching frame; use the technical profile for any feature detail sections. Business outcomes lead; technical specifics are in supporting sections.
2. **Developer audience:** Apply the `technical` tone variant with shorter sentences and a practitioner framing ("you'll configure", "your pipeline", "the CLI command is").
3. **General/unspecified audience:** Apply the `standard` tone variant per the design spec default. Flag in `metadata.tone_applied` that the audience was unspecified.

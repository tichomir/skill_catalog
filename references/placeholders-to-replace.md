---
version: 1.0.0
last-updated: 2026-04-02
authors:
  - Prompt Engineer (T. Hadzhiev)
  - Skill Owner (R. Patel)
reviewed-by: PMM (J. Morales)
next-review: 2026-07-01
---

# Placeholders to Replace

_This file is the exhaustive reference of placeholder strings used in Red Hat Copywriter Skill drafts and templates. Any string listed here must not appear in final, published copy. The skill's post-generation review step scans all output for these strings and flags them as unresolved placeholders._

_Versioned independently of skill logic. Update via PR with PMM approval. See `references/brand-and-tone-notes.md` Section 6 for the versioning scheme._

---

## Purpose and Usage

Placeholder strings are inserted by the skill when a required value cannot be derived from the input brief alone, or when a content slot requires real-world data that a human author must supply before publication. They follow the convention `[SCREAMING_SNAKE_CASE]` enclosed in square brackets.

**Rule:** No placeholder string may appear in any draft delivered for review or publication. If a placeholder cannot be resolved from the input brief, the skill must:
1. Insert the placeholder in the draft at the correct position.
2. Add the placeholder to the `unresolved_placeholders` array in the output metadata.
3. Add a comment in the draft (using `<!-- comment -->` syntax) explaining what value is expected.

---

## Placeholder Registry

### Partner and Customer Identifiers

---

#### `[PARTNER_NAME]`

**Category:** Partner identity  
**Used in:** Partner value propositions, co-sell materials, partner-facing solution briefs, ecosystem deck slides  
**Expected real value:** The full legal or trading name of the partner organisation (e.g., "Accenture", "Wipro", "DXC Technology"). Use the name exactly as it appears in the Red Hat Partner Connect directory.  
**When to resolve:** Before any external distribution. This placeholder must never appear in customer-facing copy.  
**Example in context:** _"[PARTNER_NAME] delivers fully managed Red Hat OpenShift environments with enterprise SLAs..."_ → _"Infosys delivers fully managed Red Hat OpenShift environments with enterprise SLAs..."_

---

#### `[CUSTOMER_NAME]`

**Category:** Customer identity  
**Used in:** Customer success story references, case study excerpts, testimonial framing  
**Expected real value:** The full name of the customer organisation as approved for external reference. Verify with the customer reference programme owner before use.  
**When to resolve:** Before publication; customer name use requires confirmed reference permission.  
**Example in context:** _"[CUSTOMER_NAME] reduced deployment time by 40% after adopting Red Hat OpenShift."_

---

### Product and Solution Identifiers

---

#### `[PRODUCT]`

**Category:** Product reference  
**Used in:** Generic content templates before the specific product is known; multi-product briefs where a slot is reserved  
**Expected real value:** The approved full product name on first mention (see `references/brand-and-tone-notes.md` Section 2). For example: "Red Hat Enterprise Linux", "Red Hat OpenShift Container Platform".  
**When to resolve:** At brief authoring time. If the input brief's `product_or_topic` field is populated, the skill should resolve this automatically; a residual `[PRODUCT]` in the output indicates the brief was ambiguous.  
**Example in context:** _"[PRODUCT] provides the certified foundation for..."_ → _"Red Hat Enterprise Linux provides the certified foundation for..."_

---

#### `[SOLUTION_NAME]`

**Category:** Solution or offering reference  
**Used in:** Partner joint solution names, co-developed offering titles  
**Expected real value:** The agreed marketing name for the joint solution (e.g., "Managed OpenShift on Azure", "Certified SAP HANA on RHEL"). This name must be agreed between Red Hat and the partner before use.  
**When to resolve:** Before any partner-facing or customer-facing distribution. Check with the Partner Alliance team for the agreed name.  
**Example in context:** _"[SOLUTION_NAME] is jointly supported by Red Hat and [PARTNER_NAME] under a shared SLA."_

---

### Metrics and Quantitative Claims

---

#### `[KEY_METRIC]`

**Category:** Quantitative claim  
**Used in:** Business case sections, ROI statements, outcome claims  
**Expected real value:** A specific, cited figure (e.g., "40% reduction in deployment time", "90% of Fortune 500 companies", "37% lower infrastructure management cost per IDC 2025"). Must include the source citation.  
**When to resolve:** Before delivery to reviewers. Unsubstantiated metric claims are a compliance risk. Every `[KEY_METRIC]` must be replaced with a cited figure or removed.  
**Citation format:** _(Source: [Publisher], [Year])_ appended to the metric in body copy; footnote format in solution briefs.  
**Example in context:** _"Customers report [KEY_METRIC] after migrating to Red Hat OpenShift."_ → _"Customers report a 40% reduction in time-to-production after migrating to Red Hat OpenShift. (Source: Red Hat Customer Survey, 2025)"_

---

#### `[PERCENTAGE]`

**Category:** Quantitative claim — percentage  
**Used in:** Any claim involving a percentage improvement, reduction, or adoption rate  
**Expected real value:** A specific percentage with a cited source (e.g., "37%", "up to 50%"). "Up to" framing is acceptable only when the source data supports a range.  
**When to resolve:** Before delivery to reviewers.  
**Example in context:** _"[PERCENTAGE] of surveyed IT leaders report..."_

---

#### `[CUSTOMER_COUNT]`

**Category:** Adoption scale claim  
**Used in:** Brand credibility statements, partner enablement copy  
**Expected real value:** A verified count of Red Hat customers, partners, or certified deployments. Source the figure from the most recent Red Hat Annual Report or the PMM-approved talking points.  
**When to resolve:** Before publication; verify the figure is current (not from a prior year's report).  
**Example in context:** _"Trusted by [CUSTOMER_COUNT] enterprise customers worldwide."_ → _"Trusted by more than 100,000 enterprise customers worldwide."_

---

### Temporal References

---

#### `[DATE]`

**Category:** Date reference  
**Used in:** Event announcements, availability statements, deadline-driven copy  
**Expected real value:** A specific date in the format _Month D, YYYY_ for prose copy (e.g., "May 6, 2026") or _YYYY-MM-DD_ for structured data fields. Do not use relative dates ("next Tuesday", "this quarter") in published copy.  
**When to resolve:** Before publication. Verify the date with the event owner or programme manager.  
**Example in context:** _"Join us at Red Hat Summit on [DATE]."_ → _"Join us at Red Hat Summit on May 6, 2026."_

---

#### `[QUARTER]`

**Category:** Temporal reference — quarter  
**Used in:** Product roadmap statements, availability timelines, seasonal campaign copy  
**Expected real value:** A specific quarter designation (e.g., "Q3 2026", "H2 2026"). Verify with the product team before committing to a public timeline.  
**When to resolve:** Before any external distribution; roadmap commitments require product management sign-off.  
**Example in context:** _"General availability is targeted for [QUARTER]."_

---

### Geographic and Regional References

---

#### `[REGION]`

**Category:** Geographic scope  
**Used in:** Regional campaign copy, field event materials, geo-targeted landing pages  
**Expected real value:** A specific geographic region or country name (e.g., "EMEA", "North America", "Germany", "Southeast Asia"). Use the standard Red Hat regional nomenclature from the GTM team.  
**When to resolve:** Before campaign launch. Verify with the Field Marketing lead for the region.  
**Example in context:** _"This offer is available to organisations in [REGION]."_ → _"This offer is available to organisations in EMEA."_

---

#### `[COUNTRY]`

**Category:** Geographic scope — country  
**Used in:** Country-specific legal notices, localised campaign copy  
**Expected real value:** The full country name as used in ISO 3166-1 (e.g., "United Kingdom", "Germany", "Japan"). Do not use abbreviations in formal copy.  
**When to resolve:** Before publication; country-specific copy may require local legal review.  
**Example in context:** _"Available to registered businesses in [COUNTRY]."_

---

### Content and Campaign Identifiers

---

#### `[ANNOUNCEMENT_TITLE]`

**Category:** Content title  
**Used in:** Press release drafts, blog post headlines, announcement emails  
**Expected real value:** The approved title of the announcement as agreed by the PR team and PMM. Title is subject to embargo until the announcement date.  
**When to resolve:** At the time of content authoring; do not distribute with placeholder in place.  
**Example in context:** _"Today, Red Hat announced [ANNOUNCEMENT_TITLE]."_ → _"Today, Red Hat announced Red Hat OpenShift 4.17."_

---

#### `[BLOG_TITLE]`

**Category:** Content title — blog  
**Used in:** Blog post outlines, email subject lines referencing a blog post  
**Expected real value:** The final, SEO-reviewed blog post title. Titles are subject to editorial review before publication.  
**When to resolve:** Before the post is submitted to the editorial queue.  
**Example in context:** _"Read the full analysis in our latest post: [BLOG_TITLE]."_

---

#### `[EVENT_NAME]`

**Category:** Event reference  
**Used in:** Summit copy, webinar promotions, field event materials  
**Expected real value:** The official event name as used in the event registration system (e.g., "Red Hat Summit 2026", "AnsibleFest 2026"). Do not abbreviate unless the abbreviation is official (e.g., "Summit" is acceptable shorthand for "Red Hat Summit" after first use).  
**When to resolve:** Before distribution.  
**Example in context:** _"Join us at [EVENT_NAME] for a live demo."_ → _"Join us at Red Hat Summit 2026 for a live demo."_

---

### Calls to Action and Links

---

#### `[CTA_LINK]`

**Category:** URL or link destination  
**Used in:** Email CTAs, landing page buttons, solution brief next-steps sections  
**Expected real value:** A fully qualified URL to the correct destination (e.g., a product trial page, a webinar registration form, a partner portal page). URLs must be tested before publication.  
**When to resolve:** Before the content is sent to design or published. Broken or placeholder links are a material defect in any published piece.  
**Example in context:** _"Start your free trial at [CTA_LINK]."_ → _"Start your free trial at redhat.com/en/technologies/cloud-computing/openshift/trial"_

---

#### `[LANDING_PAGE_URL]`

**Category:** URL — campaign landing page  
**Used in:** Multi-channel campaign copy where all traffic is directed to a single landing page  
**Expected real value:** The campaign landing page URL as assigned by the digital marketing team. Confirm the URL is live and tracking parameters are in place before using in copy.  
**When to resolve:** Before campaign launch.  
**Example in context:** _"Learn more at [LANDING_PAGE_URL]."_

---

### Internal References (Remove Before Publication)

---

#### `[INTERNAL_NOTE]`

**Category:** Editorial / internal  
**Used in:** Draft copy where the author has left a note for a reviewer  
**Expected real value:** This placeholder marks an editorial note that must be resolved or removed. It is never a customer-visible value.  
**When to resolve:** Before any distribution outside the authoring team. All `[INTERNAL_NOTE]` instances must be removed before the document reaches a reviewer outside the project team.  
**Example in context:** _"[INTERNAL_NOTE: confirm with PM whether GA date is embargoed]"_

---

#### `[LEGAL_REVIEW_REQUIRED]`

**Category:** Compliance flag  
**Used in:** Any claim that may require legal review before publication (pricing claims, absolute capability claims, guarantee language)  
**Expected real value:** A legal review completion confirmation. This placeholder must not appear in any published copy.  
**When to resolve:** After legal review is completed and the claim is approved or revised. Tag the relevant legal ticket number in the PR description.  
**Example in context:** _"[LEGAL_REVIEW_REQUIRED] Red Hat guarantees 99.9% uptime for..."_

---

## Placeholder Scan Rule

The skill must scan all generated draft content for any string matching the pattern `\[([A-Z][A-Z0-9_]*)\]` (uppercase bracketed tokens). Any match that corresponds to a placeholder in this registry must be added to the `unresolved_placeholders` output array. Any match that does not correspond to a known placeholder should be flagged as a potential unintended placeholder for human review.

**Output field (added to metadata when unresolved placeholders are present):**

```json
"unresolved_placeholders": [
  {
    "placeholder": "[PARTNER_NAME]",
    "location_hint": "paragraph 2, sentence 1",
    "expected_value": "Full legal or trading name of the partner organisation"
  }
]
```

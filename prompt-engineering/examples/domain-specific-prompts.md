# Domain-Specific Prompt Library

Reusable prompt templates for common professional workflows. Replace bracketed placeholders with verified context. Treat outputs as drafts: use qualified human review for decisions with legal, clinical, financial, employment, or safety consequences.

---

## Healthcare and Life Sciences

### Clinical Evidence Summary
```text
Summarize the supplied clinical evidence for [condition/intervention] for [clinical audience].

Sources:
[guidelines, studies, or notes]

Return:
1. Population, intervention, comparator, and outcomes
2. Findings, including effect sizes when stated
3. Evidence quality and important limitations
4. Conflicting evidence or unanswered questions
5. Questions for a qualified clinician to consider

Do not diagnose, prescribe, or replace clinical judgment. Clearly distinguish source facts from inferences and cite each claim to the supplied source.
```

### Clinical Trial Protocol Review
```text
Review this draft protocol for [study name] against the supplied requirements.

Protocol: [text]
Requirements: [regulatory, ethical, and operational criteria]

Provide a table with: requirement, status (met/partial/missing), evidence, risk, and recommended follow-up. Flag participant safety, consent, privacy, data-integrity, and feasibility concerns. Do not claim regulatory approval.
```

---

## Legal and Compliance

### Contract Risk Review
```text
Review the following [agreement type] from the perspective of [party/jurisdiction].

Contract: [text]
Business context: [context]
Priority issues: [issues]

Return a table of clause reference, plain-language effect, risk level, missing protections, and negotiation questions. Identify ambiguity and assumptions. This is informational support, not legal advice; do not state that the agreement complies with law.
```

### Policy-to-Control Mapping
```text
Map the supplied policy requirements to operational controls for [team/system].

Policy or regulation: [text]
Current controls and evidence: [text]

For every requirement, report the control owner, evidence, implementation status, gap, risk, and remediation priority. Separate verified evidence from proposed controls and identify items requiring legal or compliance review.
```

---

## Sales and Marketing

### Ideal Customer Profile
```text
Create an evidence-based ideal customer profile for [product] in [market].

Inputs: [customer research, win/loss data, product constraints]

Provide target segments, firmographic and behavioral signals, jobs to be done, buying triggers, likely objections, messaging themes, and disqualification criteria. Mark unsupported assumptions and propose research needed to validate them.
```

### Campaign Performance Analysis
```text
Analyze this [campaign] performance data against [business objective].

Data: [data]
Baseline/target: [target]
Constraints: [budget, brand, privacy, channels]

Report funnel metrics, meaningful segment differences, probable drivers, data-quality caveats, and a prioritized experiment backlog. Do not infer causation without an appropriate comparison or experiment.
```

---

## Customer Support and Success

### Support Ticket Triage
```text
Classify this customer request and prepare a safe handoff.

Ticket: [text]
Account context: [approved, non-sensitive context]
Support policy: [policy]

Return category, urgency, sentiment, affected product area, missing information, escalation need, and a concise customer response. Never request passwords, payment-card data, authentication codes, or other unnecessary sensitive information. Do not promise timelines or remedies not supported by policy.
```

### Account Health Review
```text
Assess account health for [account] using the supplied approved data.

Data: [usage, support, renewal, survey data]

Return health signals, risks, opportunities, confidence, and next best actions with owners. Explain which evidence supports each conclusion, distinguish facts from hypotheses, and avoid recommendations based on protected characteristics.
```

---

## Human Resources and Recruiting

### Job Description Draft
```text
Draft an inclusive job description for [role] at [company/team].

Inputs: [responsibilities, must-have skills, location, level, compensation policy]

Include a role summary, outcomes, essential responsibilities, minimum and preferred qualifications, working conditions where relevant, and an accessible application statement. Use skill- and outcome-based language; exclude discriminatory criteria and unsupported requirements.
```

### Structured Interview Kit
```text
Create a structured interview kit for [role] based only on these job-related competencies:
[competencies]

For each competency, provide one behavioral question, follow-up prompts, a 1–5 anchored scoring rubric, and evidence to capture. Include interviewer instructions on consistent questioning, note-taking, and avoiding questions about protected characteristics or personal circumstances.
```

---

## Education and Learning

### Differentiated Lesson Plan
```text
Design a [duration] lesson on [topic] for [learner group].

Learning objectives: [objectives]
Constraints: [standards, accessibility needs, available materials]

Provide a sequence of activities, formative checks, differentiation options, accommodations, and an exit assessment with success criteria. Keep content age-appropriate and identify facts that the instructor should verify before teaching.
```

### Feedback on Student Work
```text
Give constructive feedback on this [assignment type] using the rubric below.

Student work: [text]
Rubric: [criteria]

Start with strengths, then identify 2–3 actionable improvements linked to rubric criteria. Ask one reflection question and suggest a next step. Do not assign a final grade unless the instructor has supplied grading rules and requests one.
```

---

## Manufacturing and Supply Chain

### Demand Forecast Review
```text
Review the proposed demand forecast for [product/region/time period].

Data and assumptions: [data]
Operational constraints: [capacity, lead time, service level]

Report forecast drivers, uncertainty ranges, outliers, data gaps, supply risks, and scenarios for base, upside, and downside demand. Recommend decision thresholds and inputs that require owner validation; do not present estimates as guaranteed outcomes.
```

### Quality Incident Investigation
```text
Structure an investigation of this quality incident.

Incident details: [details]
Applicable specifications: [specifications]
Available evidence: [evidence]

Return containment actions, timeline, potential root-cause hypotheses, evidence needed to confirm or reject each hypothesis, corrective/preventive actions, owners, and verification criteria. Escalate any product-safety or regulatory-reporting concern according to the supplied procedure.
```

---

## Retail and E-commerce

### Merchandising Recommendation
```text
Recommend merchandising actions for [category/storefront] using the supplied data.

Inputs: [sales, margin, inventory, returns, seasonality, customer feedback]
Constraints: [brand, pricing, inventory, fairness]

Prioritize actions by expected impact, confidence, effort, and risk. Explain the evidence, identify inventory or margin trade-offs, and distinguish correlation from causal findings.
```

### Product Listing Improvement
```text
Improve this product listing for [audience/channel] using only verified product information.

Verified attributes: [attributes]
Current listing: [text]
Brand and marketplace rules: [rules]

Return a title, concise description, feature bullets, search terms, and a compliance checklist. Do not invent specifications, certifications, availability, health claims, or comparisons.
```

---

## Real Estate

### Property Market Brief
```text
Prepare a market brief for [property type] in [location] for [audience].

Verified data: [comparable properties, market statistics, dates, sources]
Objective: [buy/sell/lease/invest]

Summarize market conditions, comparable evidence, value drivers, risks, and questions for licensed local professionals. Cite data dates and sources, state data limitations, and do not present an automated estimate as an appraisal, investment recommendation, or guarantee.
```

---

## Public Sector and Nonprofits

### Grant Proposal Outline
```text
Create a grant proposal outline for [program] responding to [funder/opportunity].

Inputs: [eligibility rules, community needs evidence, budget constraints, evaluation plan]

Include need, objectives, activities, timeline, budget narrative, measurement plan, sustainability, and required attachments. Map every claim to supplied evidence, flag missing eligibility information, and avoid overstating outcomes.
```

### Program Evaluation Plan
```text
Design an evaluation plan for [program] serving [population].

Goals: [goals]
Constraints: [privacy, ethics, budget, timeline]

Specify evaluation questions, indicators, data sources, collection cadence, analysis approach, consent/privacy safeguards, limitations, and reporting audiences. Avoid collecting sensitive data unless it is necessary, authorized, and protected.
```

---

## Cross-Domain Quality Check

```text
Review the draft response below before it is used in a professional workflow.

Draft: [text]
Source material and requirements: [text]

Check for factual support, missing context, assumptions, ambiguity, harmful bias, privacy exposure, unsafe recommendations, and unmet output requirements. Return:
1. Blocking issues
2. Required revisions
3. Items needing qualified human review
4. A final readiness status: not ready, ready with review, or ready
```

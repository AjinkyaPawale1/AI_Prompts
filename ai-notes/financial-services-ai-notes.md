# AI in Financial Services & Insurance — Domain Notes

Practical notes, prompts, and patterns for applying AI/LLMs in financial services and insurance workflows.

---

## Regulatory Compliance Prompts

### 1. Automated Regulatory Document Analysis

```
You are a compliance officer tasked with evaluating insurance contracts against current federal and state insurance regulations. Highlight any clauses in the provided document that could result in regulatory non-compliance, and summarize the associated risks. Cite specific regulation sections when flagging issues.
```

### 2. Real-Time AML/KYC Guidance

```
As a KYC analyst, you need to onboard a corporate client. Based on current regulatory updates on Anti-Money Laundering, list all required verification checks and any new documentation mandated by US and EU regulators for high-risk industries. Provide step-by-step guidance for the onboarding workflow.
```

### 3. Regulatory Change Interpretation

```
Summarize the new amendments to [specific regulation] effective this year. Provide:
1. A compliance checklist for affected entities
2. Key deadlines and milestones
3. Potential penalties for non-compliance
4. Recommended immediate actions
```

### 4. Regulatory Reporting Automation

```
Generate a report template for quarterly solvency monitoring under the revised Solvency II guidelines. Ensure all required disclosures are included. Flag any data points that require manual verification before submission.
```

---

## Risk Assessment Prompts

### Portfolio Risk Analysis

```
You are a quantitative risk analyst. Given the following portfolio composition:
[portfolio data]

Perform:
1. Value-at-Risk (VaR) calculation at 95% and 99% confidence levels
2. Stress testing under 3 scenarios: market crash, interest rate spike, credit event
3. Concentration risk analysis
4. Recommendations for risk reduction

Show your reasoning step by step.
```

### Insurance Underwriting

```
You are a senior underwriter for [line of business]. Evaluate the following application:
[application details]

Assess:
- Risk factors and their severity (1-5 scale)
- Comparable historical claims data considerations
- Recommended pricing adjustments
- Terms and conditions modifications
- Decline triggers (if any)

Provide rationale for each assessment point.
```

---

## Compliance Training Simulation

```
Simulate a scenario where an insurance agent inadvertently violates a privacy regulation during customer onboarding. 

Present the scenario to the trainee, then:
1. Ask them to identify the violation
2. Explain the correct procedure
3. Describe potential regulatory consequences
4. Provide preventive measures

Adapt difficulty based on the trainee's responses.
```

---

## Document Processing Patterns

### Claims Document Extraction

```
Extract the following structured data from this insurance claim document:
- Claimant name and policy number
- Date of loss/incident
- Type of claim (property, liability, health, auto)
- Claimed amount
- Supporting evidence summary
- Red flags for potential fraud (if any)

Output as structured JSON. Flag any fields where information is ambiguous or missing.
```

### Contract Analysis

```
Review this financial contract and identify:
1. Key terms and conditions
2. Obligations for each party
3. Termination clauses and conditions
4. Liability limitations
5. Compliance requirements (regulatory references)
6. Potential risks or ambiguities

Highlight any clauses that deviate from standard market practice.
```

---

## AI Engineering Patterns for FinServ

### Data Pipeline Architecture

```
For a real-time fraud detection system:
- Streaming data ingestion (Kafka/Kinesis)
- Feature engineering pipeline
- Model inference layer (< 100ms latency requirement)
- Alert routing and triage
- Feedback loop for model retraining

Design the architecture considering: regulatory audit requirements, data residency, failover, and explainability.
```

### Model Governance

Key considerations for AI models in regulated environments:

1. **Model Risk Management (SR 11-7 compliance)**
   - Model validation and back-testing
   - Ongoing performance monitoring
   - Change management procedures

2. **Fairness and Bias**
   - Protected class analysis
   - Disparate impact testing
   - Regular fairness audits

3. **Explainability**
   - SHAP/LIME for feature importance
   - Decision path documentation
   - Customer-facing explanations

4. **Data Governance**
   - Data lineage tracking
   - Quality monitoring
   - Retention and deletion policies

---

## Useful Tools and Platforms

| Category | Tools |
|----------|-------|
| Compliance Monitoring | Regnology, Workiva, MetricStream |
| Risk Modeling | Moody's Analytics, SAS Risk Management |
| Document AI | AWS Textract, Google Document AI, Azure Form Recognizer |
| MLOps (Regulated) | Domino Data Lab, DataRobot, H2O.ai |
| Agent Platforms | LangChain, CrewAI, Semantic Kernel |
| Vector Databases | Pinecone, Weaviate, Qdrant |

---

## Key Regulations Reference

| Regulation | Scope | Key AI Requirements |
|-----------|-------|-------------------|
| EU AI Act | All EU AI systems | Risk classification, transparency, human oversight |
| DORA | EU financial entities | ICT resilience, third-party risk |
| SR 11-7 | US banks | Model risk management |
| SOX | US public companies | Internal controls, financial reporting |
| GDPR | EU data subjects | Automated decision-making rights (Art. 22) |
| CCPA | California consumers | Opt-out of automated profiling |
| NAIC AI Guidelines | US insurance | Fairness, accountability in insurance AI |
| Fair Lending Laws | US credit decisions | Non-discrimination in credit AI |

---

*Last updated: 2025*

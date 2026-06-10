# Prompt Engineering Examples

Real-world prompt examples organized by use case and technique.

---

## Financial Analysis Prompts

### Market Research Summary
```
You are a senior equity research analyst. Analyze the following earnings report:
[earnings data]

Provide:
1. Revenue and earnings surprises (vs. consensus)
2. Key growth drivers and headwinds
3. Forward guidance interpretation
4. Bull/bear case summary (3 bullets each)
5. Risk factors to monitor

Format as a concise research note suitable for portfolio managers.
```

### Credit Risk Assessment
```
You are a credit analyst evaluating a loan application. Given:
- Borrower financials: [data]
- Industry context: [sector info]
- Macro conditions: [economic indicators]

Assess:
- Probability of default (qualitative high/medium/low with reasoning)
- Loss given default considerations
- Mitigating factors
- Recommended loan terms and covenants

Think through this step by step, considering both quantitative metrics and qualitative factors.
```

---

## Code Generation Prompts

### API Endpoint Design
```
Design a RESTful API endpoint for [feature description].

Requirements:
- Follow OpenAPI 3.0 specification
- Include request/response schemas with validation
- Handle error cases (400, 401, 403, 404, 500)
- Add rate limiting considerations
- Include authentication/authorization requirements

Output the OpenAPI spec in YAML format with example values.
```

### Database Migration
```
Generate a database migration for the following schema change:
[description of change]

Requirements:
- Must be reversible (include rollback)
- Zero-downtime deployment compatible
- Include data migration if schema change affects existing rows
- Add appropriate indexes for common query patterns
- Include validation that migration was successful

Use [framework] migration format.
```

---

## Document Processing Prompts

### Contract Clause Extraction
```
Extract all indemnification clauses from the following contract.
For each clause found, provide:
1. Clause number/section reference
2. Indemnifying party
3. Indemnified party  
4. Scope of indemnification
5. Limitations or caps
6. Notable exclusions

If a clause is ambiguous, flag it and explain the ambiguity.
Output as a structured table.
```

### Regulatory Filing Review
```
Review this regulatory filing for completeness against [regulation name] requirements.

For each required section:
- ✅ Present and complete
- ⚠️ Present but potentially incomplete (explain what's missing)
- ❌ Missing entirely

Provide a compliance score (%) and prioritized list of items to address before submission.
```

---

## Multi-Turn Conversation Patterns

### Progressive Refinement
```
Turn 1: "Generate a high-level architecture for [system]"
Turn 2: "Now detail the [specific component] with error handling"
Turn 3: "Add monitoring and observability to this design"
Turn 4: "Review the full design for security vulnerabilities"
```

### Expert Panel Simulation
```
Simulate a discussion between three experts reviewing this proposal:
- A security architect (focused on vulnerabilities and compliance)
- A performance engineer (focused on scalability and efficiency)  
- A product manager (focused on user experience and business value)

Each expert should provide their top 3 concerns and 2 suggestions.
Then synthesize their feedback into actionable recommendations.
```

---

## Data Analysis Prompts

### Anomaly Investigation
```
The following metrics show an anomaly on [date]:
[data/chart description]

Investigate by:
1. Characterizing the anomaly (magnitude, duration, affected dimensions)
2. Generating 5 hypotheses ranked by likelihood
3. For each hypothesis, suggest what data would confirm or refute it
4. Recommend immediate actions while root cause is determined
```

### Report Generation
```
Generate an executive summary from this dataset:
[data]

Requirements:
- 3-5 key insights, each with supporting data points
- Trend identification (improving, declining, stable)
- Actionable recommendations tied to each insight
- Risk callouts for metrics outside acceptable ranges
- Suitable for C-level audience (no jargon, clear implications)
```

---

## Meta-Prompts (Prompts that Generate Prompts)

### System Prompt Generator
```
I need a system prompt for an AI agent with these characteristics:
- Domain: [domain]
- Primary task: [task]
- Target users: [audience]
- Key constraints: [constraints]
- Tone: [formal/casual/technical]

Generate 3 versions:
1. Concise (under 100 words) - for simple interactions
2. Standard (200-400 words) - for general use
3. Comprehensive (500+ words) - for complex workflows

Include guardrails, example interactions, and edge case handling in each.
```

### Prompt Evaluation
```
Evaluate this prompt for effectiveness:
[prompt to evaluate]

Score on:
- Clarity (1-10): Is the intent unambiguous?
- Completeness (1-10): Are all necessary constraints specified?
- Efficiency (1-10): Could it achieve the same with fewer tokens?
- Robustness (1-10): Will it work across edge cases?
- Safety (1-10): Does it prevent harmful outputs?

Provide specific improvement suggestions for any dimension scoring below 7.
```

---

*Last updated: 2025*

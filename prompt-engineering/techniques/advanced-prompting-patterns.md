# Advanced Prompting Patterns & Techniques (2025)

A comprehensive reference of modern prompting techniques for getting the best results from LLMs.

---

## 1. Chain of Thought (CoT) Prompting

Encourages LLMs to break complex tasks into step-by-step reasoning.

### Patterns:
- **Zero-shot CoT:** Add "Let's think step by step" to any prompt
- **Few-shot CoT:** Provide example problems with detailed stepwise solutions
- **Direct CoT:** Use sequential trigger phrases ("First,… Second,… Therefore,…")

### Example:
```
Q: A store sells pencils at 10 for $2. How much do 25 pencils cost?
Let's think step by step.

A: 
- 10 pencils = $2
- 25 pencils = 2.5 × 10 pencils
- Cost = 2.5 × $2 = $5
```

### When to use:
- Math and logic problems
- Multi-step reasoning tasks
- Complex decision-making
- Code debugging (trace through execution)

---

## 2. Tree of Thought (ToT) Prompting

Expands CoT by exploring multiple branches before selecting the best path.

### Patterns:
- **Enumerative:** "List 3 possible approaches, then analyze each"
- **Branch Scoring:** "Evaluate each branch and select the most effective"
- **Pruning:** "Eliminate approaches that won't work because..."

### Example:
```
We need to optimize this database query. 
Generate three different approaches:
1. [Indexing strategy]
2. [Query restructuring]  
3. [Caching layer]

For each, describe the trade-offs and select the best for our use case (high-read, low-write workload).
```

### When to use:
- Architecture decisions
- Problem-solving with multiple valid paths
- Creative tasks requiring exploration
- Risk assessment

---

## 3. Self-Consistency

Ask the model to answer in multiple ways, then aggregate the most consistent answer.

### Example:
```
Solve this problem three different ways. Show your reasoning for each approach, then determine which answer is most likely correct based on consistency.
```

### When to use:
- High-stakes decisions requiring confidence
- Mathematical proofs
- Fact verification

---

## 4. Program of Thought (PoT)

Request code or pseudocode as reasoning steps instead of natural language.

### Example:
```
Write a Python function that calculates the answer step by step. 
Include comments explaining each reasoning step.
Then execute it mentally and provide the final answer.
```

### When to use:
- Quantitative analysis
- Data transformations
- Algorithmic problem-solving
- Financial calculations

---

## 5. Retrieval-Augmented Generation (RAG) Prompting

Structure prompts to leverage retrieved context effectively.

### Pattern:
```
Based on the following documents:
---
[Document 1: ...]
[Document 2: ...]
---

Answer the question: [question]

Rules:
- Only use information from the provided documents
- Cite specific documents when making claims
- Say "insufficient information" if the answer isn't in the documents
```

### When to use:
- Knowledge-grounded Q&A
- Document analysis
- Compliance checking against regulations
- Research synthesis

---

## 6. Role-Based Prompting

Assign specific expert personas for domain-appropriate responses.

### Examples:
```
You are a senior quantitative analyst at a hedge fund with 15 years of experience in derivatives pricing...

You are a chief compliance officer reviewing insurance products for regulatory adherence...

You are a principal software architect designing microservices for a tier-1 bank...
```

### Best practices:
- Be specific about years of experience and specialization
- Include constraints relevant to the role
- Mention tools/frameworks the persona would use
- Specify the audience for the output

---

## 7. Structured Output Prompting

Force specific output formats for downstream processing.

### Examples:
```
Respond in the following JSON format:
{
  "analysis": "...",
  "risk_level": "low|medium|high",
  "recommendations": ["..."],
  "confidence": 0.0-1.0
}
```

```
Format your code review as:
## Summary
## Issues Found (Critical/Warning/Info)
## Suggestions
## Verdict (Approve/Request Changes)
```

---

## 8. Meta-Prompting

Prompts that generate or improve other prompts.

### Example:
```
I want to create a system prompt for an AI agent that helps insurance underwriters assess risk. 
Generate 3 versions of this system prompt, each optimized for:
1. Speed (quick assessments)
2. Thoroughness (detailed analysis)
3. Compliance (regulatory focus)

Then recommend which to use for a startup vs. enterprise context.
```

---

## 9. Constraint-Based Prompting

Define explicit boundaries and constraints.

### Example:
```
Requirements:
- Response must be under 200 words
- Use only Python standard library (no external packages)
- Must handle edge cases: empty input, None values, unicode
- Time complexity must be O(n log n) or better
- Include type hints
```

---

## 10. Iterative Refinement / Loop Prompting

Design prompts that self-improve through iteration.

### Pattern:
```
Step 1: Generate initial solution
Step 2: Critique your solution - identify weaknesses
Step 3: Improve based on critique
Step 4: Verify the improved version meets all requirements
Step 5: If requirements not met, return to Step 2 (max 3 iterations)
```

---

## Combining Techniques

The most effective prompts combine multiple patterns:

```
You are a senior financial engineer (Role-Based).

Analyze the following risk scenario using the provided market data (RAG):
[data]

Think through this step by step (CoT):
1. Identify risk factors
2. Quantify exposure
3. Propose hedging strategies

For each hedging strategy, evaluate pros and cons (ToT).

Output your analysis in the following format (Structured Output):
- Risk Assessment: ...
- Top 3 Strategies: ...
- Recommended Action: ...
- Confidence Level: ...
```

---

## Key References

- [Prompting Guide](https://www.promptingguide.ai/)
- [Chain-of-Thought Prompting (Wei et al., 2022)](https://arxiv.org/abs/2201.11903)
- [Tree of Thoughts (Yao et al., 2023)](https://arxiv.org/abs/2305.10601)
- [Self-Consistency (Wang et al., 2022)](https://arxiv.org/abs/2203.11171)
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Prompt Engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)

---

*Last updated: 2025*

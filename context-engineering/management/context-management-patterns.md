# Context Management Best Practices

Practical patterns for managing context across LLM applications, agents, and multi-turn conversations.

---

## Context Window Management

### Token Budget Allocation

When working within limited context windows, allocate tokens strategically:

```
Total Context Window (e.g., 128K tokens)
├── System Prompt: 5-10% (instructions, persona, rules)
├── Retrieved Context: 30-50% (RAG results, documents)
├── Conversation History: 20-30% (relevant prior turns)
├── Current Task: 10-20% (user's current request + working data)
└── Output Buffer: 10-15% (reserved for model's response)
```

### Context Prioritization Strategies

1. **Recency-weighted:** Recent interactions get more tokens
2. **Relevance-scored:** Semantic similarity to current query
3. **Importance-tagged:** Critical information always included
4. **Hybrid:** Combine all three with configurable weights

---

## Memory Architectures

### Short-Term Memory (Within Session)
- Sliding window of recent conversation turns
- Key-value store for session variables
- Summarization of older turns to compress context

### Long-Term Memory (Across Sessions)
- Vector database for semantic retrieval
- Structured storage (user preferences, facts, decisions)
- Episodic memory (past interactions, outcomes)

### Working Memory (Active Task)
- Current task state and intermediate results
- Active tool calls and their outputs
- Pending decisions and open questions

---

## RAG Context Patterns

### Basic RAG Pipeline
```
Query → Embed → Search Vector DB → Retrieve Top-K → Inject into Prompt → Generate
```

### Advanced RAG Patterns

**1. Multi-stage Retrieval:**
```
Query → Coarse retrieval (BM25) → Fine retrieval (semantic) → Re-rank → Top-K
```

**2. Hypothetical Document Embedding (HyDE):**
```
Query → Generate hypothetical answer → Embed answer → Search → Retrieve actual docs
```

**3. Recursive Retrieval:**
```
Query → Retrieve → Generate sub-questions → Retrieve for each → Synthesize
```

**4. Graph-based RAG:**
```
Query → Identify entities → Traverse knowledge graph → Retrieve connected context
```

---

## Context Compression Techniques

### Summarization
- Progressive summarization: summarize older turns, keep recent verbatim
- Hierarchical summaries: detailed → medium → high-level as context ages

### Extraction
- Extract only relevant facts/data points from large documents
- Named entity extraction for structured reference

### Selective Inclusion
- Only include context that passes a relevance threshold
- Use a lightweight model to score relevance before inclusion

---

## Multi-Agent Context Sharing

### Shared Context Bus
```
┌─────────────────────────────────────┐
│         Shared Context Store         │
│  (Task state, constraints, outputs)  │
├─────────────────────────────────────┤
│  Agent A    │  Agent B    │  Agent C │
│  (Planner)  │  (Executor) │ (Critic) │
└─────────────────────────────────────┘
```

### Context Handoff Protocol
1. Outgoing agent summarizes its work and decisions
2. Handoff includes: task state, constraints, open questions, relevant history
3. Receiving agent acknowledges and validates understanding
4. Shared scratchpad for ongoing collaboration

---

## Model Context Protocol (MCP) Integration

MCP provides a standardized way to connect LLMs with external tools and data sources:

**Key concepts:**
- **Resources:** Data sources the model can read (files, databases, APIs)
- **Tools:** Functions the model can call (search, calculate, create)
- **Prompts:** Reusable prompt templates with parameters
- **Sampling:** Model-initiated requests for additional context

**Benefits:**
- Vendor-agnostic tool integration
- Standardized context handoff between systems
- Composable context pipelines

---

## Anti-Patterns to Avoid

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| Context dumping | Flooding with irrelevant info | Relevance filtering + prioritization |
| Stale context | Outdated information misleads | TTL-based expiration + refresh |
| Context conflicts | Contradictory information | Deduplication + recency preference |
| Token waste | Repeating same context | Reference by ID, summarize repetition |
| Missing context | Model hallucinates to fill gaps | Explicit "unknown" handling |

---

## Monitoring and Observability

### Key Metrics
- Context utilization rate (tokens used vs. available)
- Retrieval relevance scores
- Context freshness (age of included information)
- Hallucination rate (correlation with context quality)
- Response latency (impact of context size)

### Tools
- LangSmith for trace visualization
- Custom dashboards for context quality metrics
- A/B testing frameworks for context strategies

---

*Last updated: 2025*

# Learning Path: Basics to Production

| Step | Read | Then try |
|---|---|---|
| 1. Prompting fundamentals | [techniques](../prompt-engineering/techniques/advanced-prompting-patterns.md), [examples](../prompt-engineering/examples/prompt-examples-by-domain.md) | Take one example and rewrite it with a role, constraints and an output format. |
| 2. System vs user prompts | [system-prompts](../system-prompts/coding-agent-prompts.md), [user-prompts](../user-prompts/README.md) | Move the standing rules of a prompt into a system prompt; keep the task in the user prompt. |
| 3. Context engineering | [guide](../context-engineering/references/context-engineering-guide-2025.md), [management](../context-engineering/management/context-management-patterns.md) | Trim a long input to only the facts the task needs and compare outputs. |
| 4. Agents | [agent-workflows](../agent-workflows/README.md), [financial-services patterns](../agent-workflows/financial-services-agent-patterns.md) | Sketch a loop: plan, call tool, validate, stop condition. |
| 5. Capstone: the registry | [walkthrough](registry-walkthrough.md) | Run `python examples/demo_credit_memo.py`, then [contribute a prompt](contributing.md). |

## Glossary
- **System prompt**: standing instructions (role, rules, safety) that frame every turn.
- **User prompt**: the task-specific request and its data for this call.
- **Context window**: the maximum tokens a model can consider at once (prompt + data + output).
- **Structured output**: a response constrained to a schema (JSON) so code can consume it; validated here with Pydantic.
- **Agent loop**: repeat observe, decide, act (tool call), check, until a stop condition or handoff to a human.
- **Golden set**: curated inputs with expected outputs used to evaluate a prompt.
- **RAG**: retrieval-augmented generation; fetch relevant documents and put them in context.

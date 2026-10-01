# Reference Architecture & Governance

```
 Input data
    |
    v
 Pydantic input validation  --fail--> reject / fix upstream
    |
    v
 Prompt rendering (registry: id + version)  <-- RAG context (optional)
    |
    v
 LLM (any provider; structured-output mode if available)
    |
    v
 Pydantic output validation --fail--> retry with error (bounded) --> human review
    |
    v
 Risk routing (risk_level / human_review_required)
    |
    v
 Human review (high risk)  -->  Audit log (prompt id, version, model, inputs hash, output, reviewer)
```

## Mapping to current practice
| Practice | In this repo |
|---|---|
| Structured outputs | Output contracts become JSON Schema in the system message; use provider JSON/schema modes plus `parse_output` as a safety net. |
| Evals with golden test sets | `example` is the seed case; add 20-50 cases per prompt and track schema-pass rate, accuracy, refusals. `pytest` already checks every example. |
| Prompt versioning in CI | SemVer `version` per prompt; CI runs `python -m prompt_registry validate` and `pytest`. Require a version bump when a prompt changes. |
| RAG | Pass retrieved text through an input field (e.g. `policy`, `contract_text`); prompts instruct "use only supplied text". |
| Agents | Registry prompts are single-step tools; chain them in an agent loop, validating each hop (see agent-workflows). |
| Responsible AI | Risk level, mandatory human review, PII/PHI de-identification, bias-safe hiring prompt, audit trail, jurisdiction review. |

## Governance checklist
- [ ] Data classification and de-identification before external calls
- [ ] Provider data-retention and residency reviewed
- [ ] Every high-risk prompt has a named human reviewer
- [ ] Prompt id + version logged per call
- [ ] Golden-set results recorded per version
- [ ] Incident process for bad outputs

# Registry as a Product: Credit Memo Walkthrough

The registry is a catalog of **versioned, validated** prompts, not a prompt dump. Each prompt (`prompts/<industry>/<subsection>/<name>.yaml`) bundles instructions, an input contract, an output contract, a tested example, and governance metadata.

Prompt: `financial_services.credit.credit_memo_summary` (v1.0.0, risk `high`, `human_review_required: true`).

## 1. Input contract
Inspect with `python -m prompt_registry schema financial_services.credit.credit_memo_summary`.

| Field | Type | Rule |
|---|---|---|
| `borrower` | string | required |
| `facility_amount` | number | required, >= 0 |
| `financials` | string | required |

Unknown, missing or negative values raise `pydantic.ValidationError` **before** any model call.

## 2. Output contract
| Field | Type | Rule |
|---|---|---|
| `summary` | string | required |
| `key_risks` | list[string] | required |
| `recommendation` | string | one of `approve`, `approve_with_conditions`, `decline`, `needs_more_info` |
| `missing_data` | list[string] | required |

## 3. The call
```python
from prompt_registry import load_registry
p = load_registry().get("financial_services.credit.credit_memo_summary")
messages = p.messages(borrower="Acme Ltd", facility_amount=5_000_000,
                      financials="Revenue 40M, EBITDA 6M, Debt 18M")
raw = my_llm(messages)   # any provider; the JSON schema is embedded in the system message
```

## 4. `parse_output` catching a bad response
```python
p.parse_output('{"summary": "Looks fine", "recommendation": "yes"}')
# ValidationError: key_risks missing, missing_data missing,
#                  recommendation must be one of [...]
```
Valid JSON (optionally in ```json fences) returns a typed object: `result.recommendation`.

## 5. Governance metadata
- `risk_level` and `human_review_required` drive routing: high-risk output always goes to a person.
- Log `p.id` + `p.version` with every call so any decision can be traced to the exact prompt.
- Bump `version` (SemVer) on any behavioural change.

## Run it
`python examples/demo_credit_memo.py` simulates a bad first reply, a retry with the validation error fed back, acceptance, and an audit record.

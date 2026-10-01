# Enterprise Prompt Registry

Plug-and-play, versioned prompts for financial services, healthcare, manufacturing, legal, retail, sales, HR, insurance and technology. Every prompt ships with a **Pydantic-validated input contract, output contract, worked example, and tips**.

See also the [documentation map](docs/README.md).

## Layout

```
prompts/<industry>/<subsection>/<prompt_name>.yaml
prompt_registry/   # Pydantic models, loader, CLI
tests/             # validates every prompt and its example
```

## Quick start

```bash
pip install -r requirements.txt
python -m prompt_registry list --industry legal
python -m prompt_registry show legal.contracts.contract_clause_extractor
python -m prompt_registry schema legal.contracts.contract_clause_extractor   # JSON Schemas
python -m prompt_registry validate
```

```python
from prompt_registry import load_registry

p = load_registry().get("financial_services.credit.credit_memo_summary")
messages = p.messages(borrower="Acme Ltd", facility_amount=5_000_000, financials="Revenue 40M ...")
raw = my_llm(messages)              # any SDK: OpenAI, Anthropic, Azure, local...
result = p.parse_output(raw)        # raises pydantic.ValidationError if the shape is wrong
print(result.recommendation)
```

Inputs are validated before rendering (unknown/missing/out-of-range fields raise); outputs are validated after the model responds (tolerates ```json fences). On a `ValidationError`, retry once feeding the error text back to the model.

## Prompt file format

| Key | Purpose |
|---|---|
| `id` | `industry.subsection.name` (unique) |
| `version` | SemVer; bump on any behavioural change |
| `risk_level`, `human_review_required` | Governance metadata |
| `system_prompt`, `user_prompt` | `user_prompt` uses `{{variable}}` placeholders; they must match `inputs` exactly |
| `inputs`, `outputs` | Field specs: `name`, `type`, `description`, `required`, `enum`, `minimum`, `maximum` |
| `example` | Sample input/output, validated in CI |
| `tips` | Usage guidance |

Supported types: `string`, `integer`, `number`, `boolean`, `list[string]`, `list[number]`, `object`, `list[object]`.

## Adding a prompt

1. Copy an existing YAML into `prompts/<industry>/<subsection>/`.
2. Edit it; keep the example realistic.
3. Run `python -m prompt_registry validate && pytest`.

## Tips for using the prompts

- **Start from the example**: run the example input first and compare against the example output.
- **Ground the model**: supply source text; every prompt tells the model to use only what is provided.
- **Compute in code**: do arithmetic, date maths and lookups outside the LLM and pass results in.
- **De-identify data**: remove PII/PHI before sending to external models; check data-residency rules.
- **Keep humans in the loop**: all `high` risk prompts are decision support only (`human_review_required: true`).
- **Evaluate before rollout**: build 20-50 golden cases per prompt; track schema-pass rate, accuracy and refusals.
- **Version and log**: record `id` + `version` with each call for audit trails.
- **Use structured output modes** of your provider where available, plus `parse_output` as a safety net.
- **Chunk long inputs** and merge JSON results; set temperature low (0-0.2) for extraction/classification.
- **Customise**: add your policies, playbooks, taxonomies and tone to the system prompt rather than rewriting the task.

> These prompts are templates, not professional (legal, medical, financial) advice. Review and test for your jurisdiction and use case.

## Catalog (23 prompts)

| Industry | Subsection | Prompt | Risk | ID |
|---|---|---|---|---|
| financial_services | advisory | Earnings Call Digest | medium | `financial_services.advisory.earnings_call_digest` |
| financial_services | compliance | AML Alert Triage | high | `financial_services.compliance.aml_alert_triage` |
| financial_services | credit | Credit Memo Summary | high | `financial_services.credit.credit_memo_summary` |
| healthcare | clinical_documentation | SOAP Note Draft | high | `healthcare.clinical_documentation.soap_note_draft` |
| healthcare | patient_communication | Plain-Language Discharge Instructions | high | `healthcare.patient_communication.discharge_instructions_plain` |
| healthcare | revenue_cycle | Claim Denial Appeal Letter | medium | `healthcare.revenue_cycle.denial_appeal_letter` |
| hr | employee_support | HR Policy Q&A | medium | `hr.employee_support.policy_qa` |
| hr | recruiting | Structured Resume Screen | high | `hr.recruiting.resume_screen_structured` |
| insurance | claims | Claim Intake Extractor | high | `insurance.claims.claim_intake_extractor` |
| insurance | underwriting | Submission Risk Summary | high | `insurance.underwriting.submission_risk_summary` |
| legal | compliance | Regulatory Change Impact | high | `legal.compliance.regulatory_change_impact` |
| legal | contracts | Contract Clause Extractor | high | `legal.contracts.contract_clause_extractor` |
| legal | litigation | Deposition Summary | high | `legal.litigation.deposition_summary` |
| manufacturing | maintenance | Maintenance Log Classifier | low | `manufacturing.maintenance.maintenance_log_classifier` |
| manufacturing | quality | 8D Root Cause Analysis | medium | `manufacturing.quality.root_cause_8d` |
| manufacturing | supply_chain | Supplier Risk Brief | medium | `manufacturing.supply_chain.supplier_risk_brief` |
| retail | customer_service | Customer Review Insights | low | `retail.customer_service.review_insights` |
| retail | merchandising | Product Description Generator | low | `retail.merchandising.product_description_generator` |
| retail | operations | Demand Forecast Explainer | low | `retail.operations.demand_forecast_explainer` |
| sales | deal_management | Sales Call Summary for CRM | low | `sales.deal_management.call_summary_crm` |
| sales | prospecting | Cold Email Personalizer | low | `sales.prospecting.cold_email_personalizer` |
| technology | engineering | Code Review Assistant | low | `technology.engineering.code_review_assistant` |
| technology | support | Incident Postmortem Draft | low | `technology.support.incident_postmortem` |

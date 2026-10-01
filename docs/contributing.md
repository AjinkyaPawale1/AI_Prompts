# Contributing a Prompt (One Page)

1. Pick `industry` (see `INDUSTRIES` in `prompt_registry/models.py`) and a `subsection`.
2. Copy an existing YAML to `prompts/<industry>/<subsection>/<name>.yaml`.
3. Set `id` = `<industry>.<subsection>.<name>`, `version: 1.0.0`.
4. Write a system prompt that restricts the model to supplied facts and says what to do when data is missing.
5. Write `user_prompt` with `{{variables}}`; every placeholder must be an `inputs` entry and vice versa.
6. Define `outputs` with enums/ranges wherever possible.
7. Add a realistic `example` (input and output); it is validated automatically.
8. Set `risk_level`, keep `human_review_required: true` for anything consequential, add 1-3 `tips`.
9. Run `python -m prompt_registry validate && python -m pytest`.
10. Use only synthetic, de-identified data. Open a PR.

New industry? Add it to `INDUSTRIES` and add a playbook in `docs/playbooks/`.

"""Offline demo: render -> (fake) LLM -> validate -> retry -> audit log.

Run: python examples/demo_credit_memo.py
Swap `fake_llm` for any provider SDK call that takes chat messages.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pydantic import ValidationError  # noqa: E402

from prompt_registry import load_registry  # noqa: E402

PROMPT_ID = "financial_services.credit.credit_memo_summary"
_calls = {"n": 0}


def fake_llm(messages):
    """First reply is malformed on purpose; the retry returns valid JSON."""
    _calls["n"] += 1
    if _calls["n"] == 1:
        return json.dumps({"summary": "Looks fine", "recommendation": "yes"})
    return json.dumps({"summary": "Acme shows stable revenue.",
                       "key_risks": ["Leverage 3.0x"],
                       "recommendation": "approve_with_conditions",
                       "missing_data": ["Covenant history"]})


def run(max_attempts=2):
    p = load_registry().get(PROMPT_ID)
    messages = p.messages(borrower="Acme Ltd", facility_amount=5_000_000,
                          financials="Revenue 40M, EBITDA 6M, Debt 18M")
    for attempt in range(1, max_attempts + 1):
        raw = fake_llm(messages)
        try:
            result = p.parse_output(raw)
        except ValidationError as exc:
            print(f"attempt {attempt}: REJECTED ({exc.error_count()} errors)")
            messages = messages + [
                {"role": "assistant", "content": raw},
                {"role": "user", "content": f"Invalid output, fix it:\n{exc}"}]
            continue
        audit = {"prompt_id": p.id, "version": p.version, "risk": p.risk_level,
                 "human_review_required": p.human_review_required,
                 "attempts": attempt}
        print(f"attempt {attempt}: ACCEPTED -> {result.recommendation}")
        print("audit:", json.dumps(audit))
        return result, audit
    raise RuntimeError("no valid output; route to human review")


if __name__ == "__main__":
    run()

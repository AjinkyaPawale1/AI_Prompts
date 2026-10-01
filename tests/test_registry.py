import pytest
from pydantic import ValidationError

from prompt_registry import load_registry


@pytest.fixture(scope="module")
def reg():
    return load_registry()


def test_loads_many_industries(reg):
    assert len(reg) >= 20
    assert len(reg.industries()) >= 8


def test_examples_roundtrip(reg):
    for p in reg.search():
        assert p.render(**p.example.input)
        assert p.parse_output(p.example.output)
        assert p.messages(**p.example.input)[0]["role"] == "system"


def test_input_validation_rejects_bad(reg):
    p = reg.get("financial_services.credit.credit_memo_summary")
    with pytest.raises(ValidationError):
        p.render(bogus=1)


def test_output_validation_rejects_bad(reg):
    p = reg.search()[0]
    with pytest.raises(ValidationError):
        p.parse_output("{}")


def test_fenced_json_parsed(reg):
    import json
    p = reg.search()[0]
    assert p.parse_output("```json\n" + json.dumps(p.example.output) + "\n```")


def test_demo_retries_then_accepts():
    import importlib.util
    from pathlib import Path
    path = Path(__file__).resolve().parent.parent / "examples" / "demo_credit_memo.py"
    spec = importlib.util.spec_from_file_location("demo", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    _, audit = mod.run()
    assert audit["attempts"] == 2 and audit["human_review_required"] is True

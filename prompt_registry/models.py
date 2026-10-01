"""Pydantic models describing a prompt and its input/output contracts."""
from __future__ import annotations

import re
from typing import Any, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, create_model, model_validator

TYPE_MAP: dict[str, Any] = {
    "string": str, "integer": int, "number": float, "boolean": bool,
    "list[string]": list[str], "list[number]": list[float], "object": dict,
    "list[object]": list[dict],
}
FieldType = Literal["string", "integer", "number", "boolean", "list[string]",
                    "list[number]", "object", "list[object]"]
PLACEHOLDER = re.compile(r"\{\{\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*\}\}")

INDUSTRIES = ["financial_services", "healthcare", "manufacturing", "legal",
              "retail", "sales", "hr", "insurance", "technology"]


class FieldSpec(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str = Field(pattern=r"^[a-zA-Z_][a-zA-Z0-9_]*$")
    type: FieldType = "string"
    description: str
    required: bool = True
    enum: Optional[list[str]] = None
    minimum: Optional[float] = None
    maximum: Optional[float] = None


class Example(BaseModel):
    model_config = ConfigDict(extra="forbid")
    input: dict[str, Any]
    output: dict[str, Any]


class PromptSpec(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str = Field(pattern=r"^[a-z0-9_]+(\.[a-z0-9_]+){2}$",
                    description="industry.subsection.name")
    title: str
    version: str = Field(pattern=r"^\d+\.\d+\.\d+$")
    industry: str
    subsection: str
    description: str
    tags: list[str] = []
    risk_level: Literal["low", "medium", "high"] = "medium"
    human_review_required: bool = True
    system_prompt: str
    user_prompt: str = Field(description="Template using {{variable}} placeholders")
    inputs: list[FieldSpec]
    outputs: list[FieldSpec]
    example: Example
    tips: list[str] = []

    @model_validator(mode="after")
    def _check(self) -> "PromptSpec":
        parts = self.id.split(".")
        if (parts[0], parts[1]) != (self.industry, self.subsection):
            raise ValueError("id must be '<industry>.<subsection>.<name>'")
        if self.industry not in INDUSTRIES:
            raise ValueError(f"unknown industry {self.industry!r}")
        names = [f.name for f in self.inputs]
        if len(set(names)) != len(names):
            raise ValueError("duplicate input names")
        used = set(PLACEHOLDER.findall(self.user_prompt))
        if used != set(names):
            raise ValueError(
                f"user_prompt placeholders {sorted(used)} != inputs {sorted(names)}")
        build_input_model(self).model_validate(self.example.input)
        build_output_model(self).model_validate(self.example.output)
        return self

    def render(self, **values: Any) -> str:
        """Validate values against the input contract and fill the template."""
        data = build_input_model(self).model_validate(values).model_dump()
        return PLACEHOLDER.sub(lambda m: _fmt(data.get(m.group(1))), self.user_prompt)

    def messages(self, **values: Any) -> list[dict[str, str]]:
        """Chat-style messages usable with any LLM SDK."""
        schema = build_output_model(self).model_json_schema()
        system = (f"{self.system_prompt.strip()}\n\nRespond ONLY with JSON matching "
                  f"this schema:\n{_json(schema)}")
        return [{"role": "system", "content": system},
                {"role": "user", "content": self.render(**values)}]

    def parse_output(self, raw: str | dict) -> BaseModel:
        """Validate model output (JSON string or dict); tolerates ``` fences."""
        model = build_output_model(self)
        if isinstance(raw, dict):
            return model.model_validate(raw)
        text = raw.strip()
        text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text)
        return model.model_validate_json(text)


def _json(obj: Any) -> str:
    import json
    return json.dumps(obj, indent=2)


def _fmt(v: Any) -> str:
    return "" if v is None else v if isinstance(v, str) else _json(v)


def _build(name: str, fields: list[FieldSpec]) -> type[BaseModel]:
    defs: dict[str, Any] = {}
    for f in fields:
        t: Any = TYPE_MAP[f.type]
        if f.enum:
            t = Literal[tuple(f.enum)]  # type: ignore[valid-type]
        kw: dict[str, Any] = {"description": f.description}
        if f.minimum is not None:
            kw["ge"] = f.minimum
        if f.maximum is not None:
            kw["le"] = f.maximum
        if f.required:
            defs[f.name] = (t, Field(..., **kw))
        else:
            defs[f.name] = (Optional[t], Field(None, **kw))
    return create_model(name, __config__=ConfigDict(extra="forbid"), **defs)


def build_input_model(spec: PromptSpec) -> type[BaseModel]:
    return _build("Input", spec.inputs)


def build_output_model(spec: PromptSpec) -> type[BaseModel]:
    return _build("Output", spec.outputs)

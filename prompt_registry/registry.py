"""Load and query prompts stored as YAML files under ``prompts/``."""
from __future__ import annotations

from pathlib import Path

import yaml

from .models import PromptSpec

DEFAULT_DIR = Path(__file__).resolve().parent.parent / "prompts"


class Registry:
    def __init__(self, prompts: list[PromptSpec]):
        self._by_id: dict[str, PromptSpec] = {}
        for p in prompts:
            if p.id in self._by_id:
                raise ValueError(f"duplicate prompt id {p.id}")
            self._by_id[p.id] = p

    def __len__(self) -> int:
        return len(self._by_id)

    def get(self, prompt_id: str) -> PromptSpec:
        return self._by_id[prompt_id]

    def search(self, industry: str | None = None, subsection: str | None = None,
               tag: str | None = None, text: str | None = None) -> list[PromptSpec]:
        out = []
        for p in self._by_id.values():
            if industry and p.industry != industry:
                continue
            if subsection and p.subsection != subsection:
                continue
            if tag and tag not in p.tags:
                continue
            if text and text.lower() not in f"{p.title} {p.description}".lower():
                continue
            out.append(p)
        return sorted(out, key=lambda p: p.id)

    def industries(self) -> dict[str, list[str]]:
        tree: dict[str, set[str]] = {}
        for p in self._by_id.values():
            tree.setdefault(p.industry, set()).add(p.subsection)
        return {k: sorted(v) for k, v in sorted(tree.items())}


def load_registry(directory: Path | str = DEFAULT_DIR) -> Registry:
    """Load every ``*.yaml`` under directory; raises on the first invalid file."""
    specs = []
    for path in sorted(Path(directory).rglob("*.yaml")):
        try:
            specs.append(PromptSpec.model_validate(yaml.safe_load(path.read_text())))
        except Exception as exc:
            raise ValueError(f"{path}: {exc}") from exc
    return Registry(specs)

"""CLI: python -m prompt_registry {validate,list,show,schema} ..."""
import argparse
import json
import sys

from .models import build_input_model, build_output_model
from .registry import load_registry


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="prompt_registry")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("validate")
    ls = sub.add_parser("list")
    ls.add_argument("--industry")
    ls.add_argument("--tag")
    sh = sub.add_parser("show")
    sh.add_argument("id")
    sc = sub.add_parser("schema")
    sc.add_argument("id")
    args = ap.parse_args(argv)
    try:
        reg = load_registry()
    except ValueError as e:
        print(f"INVALID: {e}", file=sys.stderr)
        return 1
    if args.cmd == "validate":
        print(f"OK: {len(reg)} prompts valid")
    elif args.cmd == "list":
        for p in reg.search(industry=args.industry, tag=args.tag):
            print(f"{p.id:55} v{p.version} [{p.risk_level}] {p.title}")
    elif args.cmd == "show":
        p = reg.get(args.id)
        print(p.model_dump_json(indent=2))
    elif args.cmd == "schema":
        p = reg.get(args.id)
        print(json.dumps({"input": build_input_model(p).model_json_schema(),
                          "output": build_output_model(p).model_json_schema()}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

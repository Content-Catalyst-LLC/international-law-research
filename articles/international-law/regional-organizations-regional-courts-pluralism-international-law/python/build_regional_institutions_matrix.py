#!/usr/bin/env python3
"""Build a compact JSON summary from regional institution and court matrices."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUTS = ROOT / "outputs"


def read_csv(name: str):
    path = DATA / name
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main() -> int:
    OUTPUTS.mkdir(exist_ok=True)
    payload = {
        "article": "Regional Organizations, Regional Courts, and Pluralism in International Law",
        "institutions": read_csv("regional_institution_matrix.csv"),
        "courts": read_csv("regional_court_matrix.csv"),
        "examples": read_csv("regional_pluralism_examples.csv"),
    }
    out = OUTPUTS / "regional_organizations_summary.json"
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "
", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

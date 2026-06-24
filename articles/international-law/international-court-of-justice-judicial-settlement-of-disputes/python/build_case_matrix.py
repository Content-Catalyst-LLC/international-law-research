#!/usr/bin/env python3
"""Build a JSON case-matrix output from data/case_matrix.csv."""
from __future__ import annotations
import csv, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "case_matrix.csv"
OUTPUT = ROOT / "outputs" / "case_matrix.json"

def main() -> int:
    if not INPUT.exists():
        raise FileNotFoundError(INPUT)
    with INPUT.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps({"case_count": len(rows), "cases": rows}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT} with {len(rows)} cases")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

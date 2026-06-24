#!/usr/bin/env python3
"""Build JSON outputs from International Arbitration article CSV matrices."""
from __future__ import annotations
import csv
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs"

def read_csv(name: str):
    path = DATA / name
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def main() -> int:
    OUT.mkdir(exist_ok=True)
    payload = {
        "arbitration_institutions": read_csv("arbitration_institution_matrix.csv"),
        "dispute_settlement_mechanisms": read_csv("dispute_settlement_matrix.csv"),
        "enforcement_frameworks": read_csv("enforcement_framework_matrix.csv"),
        "primary_sources": read_csv("primary_sources.csv"),
        "secondary_sources": read_csv("secondary_sources.csv"),
    }
    (OUT / "arbitration_matrices.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {OUT / 'arbitration_matrices.json'}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
from __future__ import annotations
import csv, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)
def read_csv(name: str):
    with (DATA / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))
def main() -> None:
    payload = {
        "article": "Humanitarian Intervention, Responsibility to Protect, and the Limits of Sovereignty",
        "primary_sources": read_csv("primary_sources.csv"),
        "secondary_sources": read_csv("secondary_sources.csv"),
        "r2p_pillars": read_csv("r2p_pillars_matrix.csv"),
        "humanitarian_intervention_framework": read_csv("humanitarian_intervention_framework.csv"),
        "case_matrix": read_csv("case_matrix.csv"),
    }
    out = OUT / "humanitarian_intervention_matrices.json"
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {out}")
if __name__ == "__main__":
    main()

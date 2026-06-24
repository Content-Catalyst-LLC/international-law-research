#!/usr/bin/env python3
"""Generate JSON outputs for the Statelessness article folder."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs"
OUT.mkdir(parents=True, exist_ok=True)


def read_csv(name: str):
    path = DATA / name
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


payload = {
    "article": "Statelessness, Nationality, and International Protection",
    "primary_authorities": read_csv("primary_authorities.csv"),
    "further_reading": read_csv("further_reading.csv"),
    "statelessness_framework": read_csv("statelessness_framework_matrix.csv"),
    "protection_pathways": read_csv("protection_pathways_matrix.csv"),
}

out_path = OUT / "statelessness_research_bundle.json"
with out_path.open("w", encoding="utf-8") as handle:
    json.dump(payload, handle, indent=2, ensure_ascii=False)
    handle.write("\n")

summary = {
    "article": payload["article"],
    "primary_authority_count": len(payload["primary_authorities"]),
    "further_reading_count": len(payload["further_reading"]),
    "framework_rows": len(payload["statelessness_framework"]),
    "pathway_rows": len(payload["protection_pathways"]),
}
with (OUT / "statelessness_summary.json").open("w", encoding="utf-8") as handle:
    json.dump(summary, handle, indent=2, ensure_ascii=False)
    handle.write("\n")

print(f"Wrote {out_path}")

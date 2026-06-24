#!/usr/bin/env python3
"""Build structured JSON outputs for the Self-Defense / UN Charter article."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)


def read_csv(name: str):
    path = DATA / name
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))

payload = {
    "article": "Self-Defense, Collective Security, and the UN Charter Framework",
    "slug": "self-defense-collective-security-un-charter-framework",
    "primary_sources": read_csv("primary_sources.csv"),
    "secondary_sources": read_csv("secondary_sources.csv"),
    "self_defense_framework": read_csv("self_defense_framework_matrix.csv"),
    "collective_security_framework": read_csv("collective_security_framework_matrix.csv"),
    "case_matrix": read_csv("case_matrix.csv"),
}

out_path = OUT / "self_defense_matrices.json"
out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Wrote {out_path}")

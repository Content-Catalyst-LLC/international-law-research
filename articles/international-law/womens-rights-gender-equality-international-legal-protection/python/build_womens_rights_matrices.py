#!/usr/bin/env python3
"""Generate JSON matrices for the Women’s Rights article."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

def read_csv(name: str):
    with (DATA / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

payload = {
    "article": "Women’s Rights, Gender Equality, and International Legal Protection",
    "primary_authorities": read_csv("primary_authorities.csv"),
    "further_reading": read_csv("further_reading.csv"),
    "gender_equality_framework": read_csv("gender_equality_framework_matrix.csv"),
    "protection_mechanisms": read_csv("protection_mechanisms_matrix.csv"),
}

with (OUT / "womens_rights_matrices.json").open("w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("Wrote", OUT / "womens_rights_matrices.json")

#!/usr/bin/env python3
from __future__ import annotations
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)


def read_csv(name: str):
    path = DATA / name
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_json(name: str, payload):
    path = OUTPUTS / name
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


payload = {
    "human_rights_framework": read_csv("human_rights_framework_matrix.csv"),
    "rights_categories": read_csv("rights_categories_matrix.csv"),
    "accountability_mechanisms": read_csv("accountability_mechanisms_matrix.csv"),
    "primary_authorities": read_csv("primary_authorities.csv"),
    "further_reading": read_csv("further_reading.csv"),
}
write_json("human_rights_article_matrices.json", payload)
print("Wrote outputs/human_rights_article_matrices.json")

#!/usr/bin/env python3
"""Build structured outputs for the Economic, Social, and Cultural Rights article."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ARTICLE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ARTICLE_DIR / "data"
OUTPUT_DIR = ARTICLE_DIR / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def read_csv(name: str):
    path = DATA_DIR / name
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_json(name: str, payload):
    path = OUTPUT_DIR / name
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False)
        handle.write(chr(10))


def main() -> None:
    payload = {
        "article": "Economic, Social, and Cultural Rights in International Law",
        "framework": read_csv("esc_rights_framework_matrix.csv"),
        "progressive_realization": read_csv("progressive_realization_matrix.csv"),
        "accountability_mechanisms": read_csv("accountability_mechanisms_matrix.csv"),
        "primary_authorities": read_csv("primary_authorities.csv"),
        "further_reading": read_csv("further_reading.csv"),
    }
    write_json("economic_social_cultural_rights_outputs.json", payload)
    print("Wrote outputs/economic_social_cultural_rights_outputs.json")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Build JSON matrices for the Civil and Political Rights article."""
from __future__ import annotations

import csv
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
OUTPUTS = BASE / "outputs"
OUTPUTS.mkdir(exist_ok=True)


def read_csv(name: str) -> list[dict[str, str]]:
    path = DATA / name
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_json(name: str, payload: object) -> None:
    path = OUTPUTS / name
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    payload = {
        "civil_political_rights_framework": read_csv("civil_political_rights_framework.csv"),
        "limitations_derogations_matrix": read_csv("limitations_derogations_matrix.csv"),
        "accountability_mechanisms": read_csv("accountability_mechanisms.csv"),
        "primary_authorities": read_csv("primary_authorities.csv"),
        "further_reading": read_csv("further_reading.csv"),
    }
    write_json("civil_political_rights_matrices.json", payload)
    print("Wrote outputs/civil_political_rights_matrices.json")


if __name__ == "__main__":
    main()

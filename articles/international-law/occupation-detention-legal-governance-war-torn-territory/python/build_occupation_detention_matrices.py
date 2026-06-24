#!/usr/bin/env python3
"""Build structured JSON outputs for the Occupation / Detention article.

This helper intentionally performs only local file reads. It is safe to run
without network access and will not fail if optional CSVs are absent.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Dict, List


ARTICLE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ARTICLE_DIR / "data"
OUTPUT_DIR = ARTICLE_DIR / "outputs"

MATRIX_FILES = [
    "occupation_framework_matrix.csv",
    "detention_framework_matrix.csv",
    "protected_persons_matrix.csv",
    "war_crimes_matrix.csv",
    "primary_sources.csv",
    "secondary_sources.csv",
]


def read_csv(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    payload = {
        "article": "Occupation, Detention, and the Legal Governance of War-Torn Territory",
        "slug": "occupation-detention-legal-governance-war-torn-territory",
        "matrices": {
            filename.removesuffix(".csv"): read_csv(DATA_DIR / filename)
            for filename in MATRIX_FILES
        },
    }

    out_path = OUTPUT_DIR / "occupation_detention_matrices.json"
    out_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()

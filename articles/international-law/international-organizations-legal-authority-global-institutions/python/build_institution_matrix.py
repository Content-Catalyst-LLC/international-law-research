#!/usr/bin/env python3
"""Build structured JSON outputs from International Organizations CSV data."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs"


def read_csv(name: str) -> list[dict]:
    path = DATA / name
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main() -> int:
    OUT.mkdir(exist_ok=True)
    payload = {
        "article_slug": "international-organizations-legal-authority-global-institutions",
        "authority_matrix": read_csv("institution_authority_matrix.csv"),
        "organization_profiles": read_csv("organization_profiles.csv"),
        "primary_sources": read_csv("primary_sources.csv"),
        "secondary_sources": read_csv("secondary_sources.csv"),
    }
    (OUT / "institution_authority_matrix.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {OUT / 'institution_authority_matrix.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

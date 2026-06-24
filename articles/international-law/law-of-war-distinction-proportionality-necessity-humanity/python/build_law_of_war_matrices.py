#!/usr/bin/env python3
"""Build structured JSON outputs for the Law of War article."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ARTICLE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ARTICLE_DIR / "data"
OUTPUT_DIR = ARTICLE_DIR / "outputs"


def read_csv(name: str) -> list[dict[str, str]]:
    path = DATA_DIR / name
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "article_slug": "law-of-war-distinction-proportionality-necessity-humanity",
        "principles": read_csv("law_of_war_principles_matrix.csv"),
        "targeting_rules": read_csv("targeting_rules_matrix.csv"),
        "war_crimes": read_csv("war_crimes_matrix.csv"),
        "primary_sources": read_csv("primary_sources.csv"),
        "secondary_sources": read_csv("secondary_sources.csv"),
    }
    out_path = OUTPUT_DIR / "law_of_war_matrices.json"
    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()

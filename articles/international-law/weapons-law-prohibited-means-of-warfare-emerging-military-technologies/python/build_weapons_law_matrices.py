#!/usr/bin/env python3
# Build JSON matrix outputs for the weapons law article.
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUTS = ROOT / "outputs"


def read_csv(name: str) -> list[dict[str, str]]:
    path = DATA / name
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    payload = {
        "weapons_law_matrix": read_csv("weapons_law_matrix.csv"),
        "article_36_review_matrix": read_csv("article_36_review_matrix.csv"),
        "emerging_military_technologies_matrix": read_csv("emerging_military_technologies_matrix.csv"),
        "war_crimes_weapons_law_matrix": read_csv("war_crimes_weapons_law_matrix.csv"),
        "primary_sources": read_csv("primary_sources.csv"),
        "secondary_sources": read_csv("secondary_sources.csv"),
    }
    out_path = OUTPUTS / "weapons_law_matrices.json"
    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

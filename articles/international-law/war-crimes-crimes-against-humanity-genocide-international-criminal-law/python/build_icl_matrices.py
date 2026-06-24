#!/usr/bin/env python3
"""Build generated matrices for the international criminal law architecture article."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_json(name: str, payload: object) -> None:
    out_path = OUTPUTS / name
    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    payload = {
        "article": "War Crimes, Crimes Against Humanity, Genocide, and the Architecture of International Criminal Law",
        "primary_sources": read_csv(DATA / "primary_sources.csv"),
        "secondary_sources": read_csv(DATA / "secondary_sources.csv"),
        "crime_architecture": read_csv(DATA / "crime_architecture_matrix.csv"),
        "modes_of_liability": read_csv(DATA / "modes_of_liability_matrix.csv"),
        "workflow": read_csv(DATA / "international_criminal_law_workflow.csv"),
        "war_crimes_analysis": read_csv(DATA / "war_crimes_analysis_matrix.csv"),
    }
    write_json("international_criminal_law_article_payload.json", payload)

    summary_rows = []
    for row in payload["crime_architecture"]:
        summary_rows.append({
            "crime_category": row.get("crime_category", ""),
            "contextual_element": row.get("contextual_element", ""),
            "mental_element": row.get("mental_element", ""),
        })
    write_json("crime_architecture_summary.json", summary_rows)
    print(f"Wrote {OUTPUTS / 'international_criminal_law_article_payload.json'}")
    print(f"Wrote {OUTPUTS / 'crime_architecture_summary.json'}")


if __name__ == "__main__":
    main()

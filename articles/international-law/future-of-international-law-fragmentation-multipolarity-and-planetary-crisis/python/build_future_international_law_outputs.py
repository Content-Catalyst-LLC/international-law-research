#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUTS = ROOT / "outputs"

def read_csv(name: str) -> list[dict[str, str]]:
    path = DATA / name
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))

def main() -> None:
    OUTPUTS.mkdir(parents=True, exist_ok=True)

    domains = read_csv("future_domains_matrix.csv")
    scenarios = read_csv("scenario_framework_matrix.csv")
    planetary = read_csv("planetary_crisis_matrix.csv")
    workflow = read_csv("lawyer_workflow_matrix.csv")

    summary = {
        "article": "The Future of International Law in an Age of Fragmentation, Multipolarity, and Planetary Crisis",
        "slug": "future-of-international-law-fragmentation-multipolarity-and-planetary-crisis",
        "series": "International Law",
        "is_final_article": True,
        "github_policy": "support package only; no full WordPress HTML stored",
        "future_domains_count": len(domains),
        "scenario_count": len(scenarios),
        "planetary_crisis_issue_count": len(planetary),
        "workflow_steps_count": len(workflow),
        "core_themes": [
            "fragmentation",
            "multipolarity",
            "planetary crisis",
            "climate responsibility",
            "Security Council paralysis",
            "human rights backlash",
            "digital sovereignty",
            "soft law and informal governance",
            "global legitimacy"
        ]
    }

    index = {
        "files": {
            "metadata": "metadata/article_metadata.json",
            "primary_authorities": "sources/primary_authorities.md",
            "further_reading": "sources/further_reading.md",
            "future_domains": "data/future_domains_matrix.csv",
            "scenarios": "data/scenario_framework_matrix.csv",
            "planetary_crisis": "data/planetary_crisis_matrix.csv",
            "lawyer_workflow": "data/lawyer_workflow_matrix.csv",
            "sql_schema": "sql/future_international_law_schema.sql"
        },
        "future_domains": domains,
        "scenario_framework": scenarios,
        "planetary_crisis": planetary,
        "lawyer_workflow": workflow
    }

    (OUTPUTS / "future_international_law_support_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )
    (OUTPUTS / "future_international_law_support_index.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )

if __name__ == "__main__":
    main()

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

    public_private = read_csv("public_private_divide_matrix.csv")
    frameworks = read_csv("gender_based_violence_frameworks.csv")
    due_diligence = read_csv("due_diligence_workflow.csv")
    procedural_risks = read_csv("procedural_risk_matrix.csv")

    summary = {
        "article": "Gender, Violence, and the Public/Private Divide in International Law",
        "slug": "gender-violence-public-private-divide-international-law",
        "github_policy": "support package only; no full WordPress HTML stored",
        "public_private_categories_count": len(public_private),
        "legal_frameworks_count": len(frameworks),
        "due_diligence_stages_count": len(due_diligence),
        "procedural_risk_categories_count": len(procedural_risks),
        "core_themes": [
            "gender-based violence",
            "public/private divide",
            "state due diligence",
            "CEDAW and substantive equality",
            "conflict-related sexual violence",
            "international criminal law",
            "gender-related persecution",
            "procedure evidence and remedy"
        ]
    }

    index = {
        "files": {
            "metadata": "metadata/article_metadata.json",
            "primary_authorities": "sources/primary_authorities.md",
            "further_reading": "sources/further_reading.md",
            "public_private_matrix": "data/public_private_divide_matrix.csv",
            "frameworks_matrix": "data/gender_based_violence_frameworks.csv",
            "due_diligence_workflow": "data/due_diligence_workflow.csv",
            "procedural_risk_matrix": "data/procedural_risk_matrix.csv",
            "sql_schema": "sql/gender_violence_schema.sql"
        },
        "public_private_divide": public_private,
        "gender_based_violence_frameworks": frameworks,
        "due_diligence_workflow": due_diligence,
        "procedural_risks": procedural_risks
    }

    (OUTPUTS / "gender_violence_support_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )
    (OUTPUTS / "gender_violence_support_index.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )

if __name__ == "__main__":
    main()

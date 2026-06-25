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
    instruments = read_csv("soft_law_instruments_matrix.csv")
    workflow = read_csv("norm_entrepreneurship_workflow.csv")
    risks = read_csv("informal_governance_risk_matrix.csv")
    summary = {
        "article": "Soft Law, Norm Entrepreneurship, and Informal International Governance",
        "slug": "soft-law-norm-entrepreneurship-informal-international-governance",
        "github_policy": "support package only; no full WordPress HTML stored",
        "instrument_types_count": len(instruments),
        "workflow_stages_count": len(workflow),
        "risk_categories_count": len(risks),
        "core_themes": [
            "soft law",
            "norm entrepreneurship",
            "informal international governance",
            "institutional authority",
            "technical standards",
            "compliance without formal binding force",
            "legitimacy and accountability",
            "legal pluralism"
        ]
    }
    index = {
        "files": {
            "metadata": "metadata/article_metadata.json",
            "primary_authorities": "sources/primary_authorities.md",
            "further_reading": "sources/further_reading.md",
            "instrument_matrix": "data/soft_law_instruments_matrix.csv",
            "workflow_matrix": "data/norm_entrepreneurship_workflow.csv",
            "risk_matrix": "data/informal_governance_risk_matrix.csv",
            "sql_schema": "sql/soft_law_schema.sql"
        },
        "soft_law_instruments": instruments,
        "norm_entrepreneurship_workflow": workflow,
        "informal_governance_risks": risks
    }
    (OUTPUTS / "soft_law_support_summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (OUTPUTS / "soft_law_support_index.json").write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()

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

    forms = read_csv("arbitration_forms_matrix.csv")
    consent = read_csv("consent_jurisdiction_matrix.csv")
    procedure = read_csv("procedure_enforcement_matrix.csv")
    sequence = read_csv("sequence_patch_arbitration.csv")

    summary = {
        "article": "International Arbitration and the Peaceful Settlement of Disputes",
        "slug": "international-arbitration-peaceful-settlement-disputes",
        "series": "International Law",
        "is_inserted_article": True,
        "github_policy": "support package only; no full WordPress HTML stored",
        "arbitration_forms_count": len(forms),
        "consent_sources_count": len(consent),
        "procedure_enforcement_stages_count": len(procedure),
        "sequence_patch": sequence,
        "core_themes": [
            "peaceful settlement of disputes",
            "international arbitration",
            "consent and jurisdiction",
            "Permanent Court of Arbitration",
            "interstate arbitration",
            "mixed claims commissions",
            "investor-state arbitration",
            "ICSID",
            "UNCITRAL",
            "recognition and enforcement"
        ]
    }

    index = {
        "files": {
            "metadata": "metadata/article_metadata.json",
            "primary_authorities": "sources/primary_authorities.md",
            "further_reading": "sources/further_reading.md",
            "arbitration_forms": "data/arbitration_forms_matrix.csv",
            "consent_jurisdiction": "data/consent_jurisdiction_matrix.csv",
            "procedure_enforcement": "data/procedure_enforcement_matrix.csv",
            "sequence_patch": "data/sequence_patch_arbitration.csv",
            "sql_schema": "sql/international_arbitration_schema.sql"
        },
        "arbitration_forms": forms,
        "consent_jurisdiction": consent,
        "procedure_enforcement": procedure,
        "sequence_patch": sequence
    }

    (OUTPUTS / "international_arbitration_support_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )
    (OUTPUTS / "international_arbitration_support_index.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )

if __name__ == "__main__":
    main()

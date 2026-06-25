#!/usr/bin/env python3
"""Build lightweight JSON support outputs for the International Trade Law article."""
from __future__ import annotations

import csv
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
OUTPUTS = BASE / "outputs"
OUTPUTS.mkdir(parents=True, exist_ok=True)


def read_csv(name: str) -> list[dict[str, str]]:
    path = DATA / name
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    architecture = read_csv("trade_law_architecture.csv")
    agreements = read_csv("wto_agreement_matrix.csv")
    disputes = read_csv("dispute_settlement_matrix.csv")
    autonomy = read_csv("regulatory_autonomy_matrix.csv")

    summary = {
        "article": "International Trade Law and the Legal Order of Global Commerce",
        "slug": "international-trade-law-global-commerce",
        "html_in_github": False,
        "counts": {
            "architecture_areas": len(architecture),
            "wto_agreements": len(agreements),
            "dispute_settlement_stages": len(disputes),
            "regulatory_autonomy_areas": len(autonomy),
        },
        "core_themes": [
            "market access",
            "non-discrimination",
            "regulatory autonomy",
            "WTO dispute settlement",
            "development and asymmetry",
            "trade and environment",
            "industrial policy",
            "geoeconomic conflict",
        ],
    }

    (OUTPUTS / "trade_law_support_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    index = {
        "architecture": architecture,
        "agreements": agreements,
        "dispute_settlement": disputes,
        "regulatory_autonomy": autonomy,
    }
    (OUTPUTS / "trade_law_support_index.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()

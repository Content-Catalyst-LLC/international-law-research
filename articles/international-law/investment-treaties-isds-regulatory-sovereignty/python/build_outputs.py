#!/usr/bin/env python3
"""Build lightweight research outputs for the investment treaties / ISDS article."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)


def read_csv(name: str) -> list[dict[str, str]]:
    path = DATA / name
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))

payload = {
    "article": "Investment Treaties, Investor-State Dispute Settlement, and Regulatory Sovereignty",
    "slug": "investment-treaties-isds-regulatory-sovereignty",
    "repository_policy": "Research/support package only; no full WordPress article HTML is stored.",
    "tables": {
        "investment_treaty_doctrines": read_csv("investment_treaty_doctrines.csv"),
        "isds_procedure_matrix": read_csv("isds_procedure_matrix.csv"),
        "regulatory_sovereignty_risk_matrix": read_csv("regulatory_sovereignty_risk_matrix.csv"),
        "reform_pathways": read_csv("reform_pathways.csv"),
    },
}

(OUTPUTS / "research_summary.json").write_text(
    json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
)

lines = [
    "# Investment Treaties / ISDS Research Summary",
    "",
    "This generated summary indexes the article support matrices without storing the full WordPress HTML.",
    "",
]
for table_name, rows in payload["tables"].items():
    lines.append(f"## {table_name.replace('_', ' ').title()}")
    lines.append("")
    for row in rows:
        first_key = next(iter(row))
        lines.append(f"- **{row[first_key]}**")
    lines.append("")

(OUTPUTS / "research_summary.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

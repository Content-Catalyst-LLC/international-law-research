#!/usr/bin/env python3
"""Build lightweight JSON outputs for the International Health Law support package."""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)


def read_csv(name):
    path = DATA / name
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

architecture = read_csv("health_law_architecture.csv")
coordination = read_csv("pandemic_coordination_matrix.csv")
equity = read_csv("health_equity_matrix.csv")

index = {
    "article_slug": "international-health-law-pandemics-global-public-health-coordination",
    "title": "International Health Law, Pandemics, and Global Public Health Coordination",
    "repository_policy": "support package only; no full WordPress HTML stored",
    "datasets": {
        "health_law_architecture": len(architecture),
        "pandemic_coordination_matrix": len(coordination),
        "health_equity_matrix": len(equity)
    },
    "core_topics": [
        "WHO authority",
        "International Health Regulations",
        "pandemic emergency governance",
        "surveillance and notification",
        "core capacities",
        "travel and trade measures",
        "right to health",
        "vaccine and medicine access",
        "pathogen sharing",
        "One Health",
        "health equity"
    ]
}

summary = {
    "architecture_categories": [row["category"] for row in architecture],
    "coordination_problems": [row["coordination_problem"] for row in coordination],
    "equity_issues": [row["equity_issue"] for row in equity]
}

(OUT / "health_law_support_index.json").write_text(
    json.dumps(index, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8"
)
(OUT / "health_law_support_summary.json").write_text(
    json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8"
)

print("Wrote health law support outputs")

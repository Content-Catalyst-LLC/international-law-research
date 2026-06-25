#!/usr/bin/env python3
"""Build lightweight JSON outputs for the International Space Law support package."""

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

architecture = read_csv("space_law_architecture.csv")
governance = read_csv("outer_space_governance_matrix.csv")
security_equity = read_csv("space_security_and_equity_matrix.csv")

index = {
    "article_slug": "international-space-law-governance-outer-space",
    "title": "International Space Law and the Governance of Outer Space",
    "repository_policy": "support package only; no full WordPress HTML stored",
    "datasets": {
        "space_law_architecture": len(architecture),
        "outer_space_governance_matrix": len(governance),
        "space_security_and_equity_matrix": len(security_equity)
    },
    "core_topics": [
        "Outer Space Treaty",
        "non-appropriation",
        "state responsibility",
        "private space actors",
        "launch liability",
        "registration",
        "space debris",
        "space traffic management",
        "spectrum and orbital coordination",
        "space resources",
        "dual-use space infrastructure",
        "equity and benefit of all countries"
    ]
}

summary = {
    "architecture_categories": [row["category"] for row in architecture],
    "governance_problems": [row["governance_problem"] for row in governance],
    "security_and_equity_issues": [row["issue"] for row in security_equity]
}

(OUT / "space_law_support_index.json").write_text(
    json.dumps(index, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8"
)
(OUT / "space_law_support_summary.json").write_text(
    json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8"
)

print("Wrote space law support outputs")

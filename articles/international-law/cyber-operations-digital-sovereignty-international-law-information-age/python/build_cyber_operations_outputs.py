#!/usr/bin/env python3
"""Build lightweight JSON outputs for the Cyber Operations support package."""

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

architecture = read_csv("cyber_law_architecture.csv")
operations = read_csv("cyber_operations_matrix.csv")
digital_governance = read_csv("digital_sovereignty_governance_matrix.csv")

index = {
    "article_slug": "cyber-operations-digital-sovereignty-international-law-information-age",
    "title": "Cyber Operations, Digital Sovereignty, and International Law in the Information Age",
    "repository_policy": "support package only; no full WordPress HTML stored",
    "datasets": {
        "cyber_law_architecture": len(architecture),
        "cyber_operations_matrix": len(operations),
        "digital_sovereignty_governance_matrix": len(digital_governance)
    },
    "core_topics": [
        "UN cyber framework",
        "digital sovereignty",
        "sovereignty",
        "non-intervention",
        "use of force",
        "due diligence",
        "attribution",
        "state responsibility",
        "countermeasures",
        "human rights online",
        "cybercrime cooperation",
        "IHL and cyber operations",
        "private platforms and cloud infrastructure"
    ]
}

summary = {
    "architecture_categories": [row["category"] for row in architecture],
    "operation_types": [row["operation_type"] for row in operations],
    "digital_governance_issues": [row["issue"] for row in digital_governance]
}

(OUT / "cyber_operations_support_index.json").write_text(
    json.dumps(index, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8"
)
(OUT / "cyber_operations_support_summary.json").write_text(
    json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8"
)

print("Wrote cyber operations support outputs")

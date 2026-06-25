#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs"
META = ROOT / "metadata" / "article_metadata.json"


def read_csv(name: str):
    path = DATA / name
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    metadata = json.loads(META.read_text(encoding="utf-8"))
    traditions = read_csv("critical_traditions_matrix.csv")
    domains = read_csv("power_inequality_domains.csv")
    workflow = read_csv("critique_workflow_matrix.csv")

    summary = {
        "title": metadata["actual_title"],
        "slug": metadata["slug"],
        "github_policy": metadata["github_policy"],
        "critical_traditions_count": len(traditions),
        "power_domains_count": len(domains),
        "workflow_steps_count": len(workflow),
        "primary_focus": [
            "formal equality and structural inequality",
            "empire and decolonization",
            "institutional hierarchy",
            "economic asymmetry",
            "critical legal traditions",
            "lawyer-facing diagnostic workflow",
        ],
    }

    index = {
        "metadata": metadata,
        "critical_traditions": traditions,
        "power_domains": domains,
        "critique_workflow": workflow,
    }

    (OUT / "power_inequality_support_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (OUT / "power_inequality_support_index.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()

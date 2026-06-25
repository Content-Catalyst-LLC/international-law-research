#!/usr/bin/env python3
# Build support outputs for Empire, Decolonization, and the Making of International Law.

from pathlib import Path
import csv
import json

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
OUT = BASE / "outputs"

def read_csv(name):
    with (DATA / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def main():
    OUT.mkdir(exist_ok=True)
    colonial_forms = read_csv("colonial_legal_forms.csv")
    doctrines = read_csv("decolonization_doctrine_matrix.csv")
    frameworks = read_csv("critical_frameworks_matrix.csv")

    index = {
        "article": "Empire, Decolonization, and the Making of International Law",
        "slug": "empire-decolonization-making-international-law",
        "support_files": {
            "colonial_legal_forms": len(colonial_forms),
            "decolonization_doctrines": len(doctrines),
            "critical_frameworks": len(frameworks),
        },
        "github_policy": "No full WordPress HTML stored in GitHub."
    }

    summary = {
        "core_thesis": (
            "International law was shaped by empire and transformed by decolonization; its doctrines "
            "must be read as both instruments of hierarchy and tools of anti-colonial legal struggle."
        ),
        "doctrinal_clusters": [row["doctrine"] for row in doctrines],
        "critical_frameworks": [row["framework"] for row in frameworks],
        "practice_warning": "Do not treat formal sovereignty, consent, or neutral doctrine as sufficient without examining history, power, and distribution."
    }

    (OUT / "empire_decolonization_support_index.json").write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (OUT / "empire_decolonization_support_summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from pathlib import Path
import csv
import json

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
OUT = BASE / "outputs"
OUT.mkdir(exist_ok=True)

def read_csv(name):
    path = DATA / name
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))

payload = {
    "article": "Universal Jurisdiction and Accountability for Atrocity Crimes",
    "framework": read_csv("universal_jurisdiction_framework_matrix.csv"),
    "accountability_pathways": read_csv("accountability_pathways_matrix.csv"),
    "immunity_extradition": read_csv("immunity_extradition_matrix.csv"),
    "evidence_documentation": read_csv("evidence_documentation_matrix.csv"),
    "primary_sources": read_csv("primary_sources.csv"),
    "secondary_sources": read_csv("secondary_sources.csv"),
}

(OUT / "universal_jurisdiction_matrices.json").write_text(
    json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
)

summary_rows = [
    {"matrix": key, "rows": len(value)}
    for key, value in payload.items()
    if isinstance(value, list)
]
with (OUT / "matrix_summary.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=["matrix", "rows"])
    writer.writeheader()
    writer.writerows(summary_rows)

print("Wrote outputs/universal_jurisdiction_matrices.json")
print("Wrote outputs/matrix_summary.csv")

#!/usr/bin/env python3
from pathlib import Path
import csv

base = Path(__file__).resolve().parents[1]
out = base / "outputs"
out.mkdir(exist_ok=True)

def rows(name):
    with (base / "data" / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

lines = ["# Self-Determination Source Export", ""]
lines.append("## Primary Sources")
for row in rows("primary_sources.csv"):
    lines.append(f"- {row['institution']} ({row['year']}) *{row['source_title']}*. {row['url']}")

lines.append("")
lines.append("## Concepts")
for row in rows("concepts.csv"):
    lines.append(f"- **{row['concept']}** — {row['description']}")

(out / "source_export.md").write_text("\\n".join(lines) + "\\n", encoding="utf-8")
print("Wrote outputs/source_export.md")

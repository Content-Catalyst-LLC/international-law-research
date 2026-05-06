#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ARTICLE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ARTICLE_DIR / "outputs"

ROWS = [
    {
        "source": "Treaties",
        "category": "Primary source",
        "definition": "Written international agreements governed by international law.",
        "example": "UN Charter; Vienna Convention on the Law of Treaties.",
    },
    {
        "source": "Customary international law",
        "category": "Primary source",
        "definition": "General practice accepted as law.",
        "example": "Diplomatic immunity principles later codified in treaty form.",
    },
    {
        "source": "General principles",
        "category": "Primary source",
        "definition": "Principles recognized across legal systems and used to support international adjudication.",
        "example": "Good faith, res judicata, procedural fairness.",
    },
    {
        "source": "Judicial decisions",
        "category": "Subsidiary means",
        "definition": "Court and tribunal decisions used to identify or clarify rules.",
        "example": "ICJ decisions on state responsibility, immunity, and use of force.",
    },
    {
        "source": "Scholarly writings",
        "category": "Subsidiary means",
        "definition": "Teachings of highly qualified publicists used to clarify legal rules.",
        "example": "Major treatises and scholarly works on public international law.",
    },
]

def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_csv = OUTPUT_DIR / "source_taxonomy_summary.csv"
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["source", "category", "definition", "example"])
        writer.writeheader()
        writer.writerows(ROWS)

    out_md = OUTPUT_DIR / "source_taxonomy_summary.md"
    lines = ["# Source Taxonomy Summary", ""]
    for row in ROWS:
        lines.append(f"## {row['source']}")
        lines.append(f"- Category: {row['category']}")
        lines.append(f"- Definition: {row['definition']}")
        lines.append(f"- Example: {row['example']}")
        lines.append("")
    out_md.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {out_csv}")
    print(f"Wrote {out_md}")

if __name__ == "__main__":
    main()

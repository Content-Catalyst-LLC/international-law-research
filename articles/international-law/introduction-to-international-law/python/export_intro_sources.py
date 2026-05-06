#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ARTICLE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ARTICLE_DIR / "outputs"

def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def export_markdown() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    primary = read_csv(ARTICLE_DIR / "data" / "primary_sources.csv")
    secondary = read_csv(ARTICLE_DIR / "data" / "secondary_sources.csv")
    concepts = read_csv(ARTICLE_DIR / "data" / "concepts.csv")

    lines = ["# Introduction to International Law — Source Export", ""]
    lines.extend(["## Primary Authorities and Resources", ""])
    for row in primary:
        lines.append(f"- {row['institution']} ({row['year']}) *{row['source_title']}*. Available at: {row['url']}.")

    lines.extend(["", "## Core Concepts", ""])
    for row in concepts:
        lines.append(f"- **{row['concept_name']}** ({row['concept_category']}) — {row['description']}.")

    lines.extend(["", "## Further Reading", ""])
    for row in secondary:
        lines.append(f"- {row['author']} ({row['year']}) *{row['title']}*. {row['publisher']}. Available at: {row['url']}.")

    output = OUTPUT_DIR / "intro_sources_export.md"
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {output}")

if __name__ == "__main__":
    export_markdown()

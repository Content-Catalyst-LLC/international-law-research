#!/usr/bin/env python3
"""
Create a compact immunity-category summary for editorial reference.
"""

from __future__ import annotations

import csv
from pathlib import Path


ARTICLE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ARTICLE_DIR / "outputs"

ROWS = [
    {
        "immunity_type": "State immunity",
        "protected_entity_or_function": "The state and often state property before foreign domestic courts",
        "duration": "Continuing, subject to exceptions and waiver",
        "scope": "Civil jurisdiction and execution questions",
        "key_limits": "Commercial transactions, waiver, some employment/property exceptions, execution limits",
        "key_sources": "2004 UN State Immunities Convention; customary international law; ICJ Jurisdictional Immunities",
    },
    {
        "immunity_type": "Diplomatic immunity",
        "protected_entity_or_function": "Diplomatic agents, mission premises, archives, and diplomatic communication",
        "duration": "During diplomatic status, with residual protection for official acts",
        "scope": "Broad personal inviolability and jurisdictional immunity in receiving state",
        "key_limits": "Persona non grata, waiver by sending state, limited civil exceptions",
        "key_sources": "1961 Vienna Convention on Diplomatic Relations",
    },
    {
        "immunity_type": "Consular immunity",
        "protected_entity_or_function": "Consular officers and consular functions",
        "duration": "During consular status, with functional protection for consular acts",
        "scope": "Narrower and more functional than diplomatic immunity",
        "key_limits": "Grave crime arrest exception under Article 41; functional scope under Article 43",
        "key_sources": "1963 Vienna Convention on Consular Relations",
    },
    {
        "immunity_type": "Immunity ratione personae",
        "protected_entity_or_function": "Serving heads of state, heads of government, foreign ministers, and comparable high officials",
        "duration": "While in office",
        "scope": "Broad personal immunity and inviolability from foreign criminal jurisdiction",
        "key_limits": "Waiver, own-state prosecution, certain international tribunals, post-office limits",
        "key_sources": "Customary international law; ICJ Arrest Warrant",
    },
    {
        "immunity_type": "Immunity ratione materiae",
        "protected_entity_or_function": "Official acts attributed to the state",
        "duration": "May continue after office",
        "scope": "Functional immunity for official acts",
        "key_limits": "Contested in relation to international crimes; ILC draft articles address possible exceptions",
        "key_sources": "Customary international law; domestic practice; ILC work",
    },
]


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    out_csv = OUTPUT_DIR / "immunity_categories_summary.csv"
    fieldnames = [
        "immunity_type",
        "protected_entity_or_function",
        "duration",
        "scope",
        "key_limits",
        "key_sources",
    ]
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(ROWS)

    out_md = OUTPUT_DIR / "immunity_categories_summary.md"
    lines = ["# Immunity Categories Summary", ""]
    for row in ROWS:
        lines.append(f"## {row['immunity_type']}")
        lines.append(f"- Protected function: {row['protected_entity_or_function']}")
        lines.append(f"- Duration: {row['duration']}")
        lines.append(f"- Scope: {row['scope']}")
        lines.append(f"- Key limits: {row['key_limits']}")
        lines.append(f"- Key sources: {row['key_sources']}")
        lines.append("")
    out_md.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {out_csv}")
    print(f"Wrote {out_md}")


if __name__ == "__main__":
    main()

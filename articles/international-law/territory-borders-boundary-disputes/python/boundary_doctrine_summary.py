#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ARTICLE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ARTICLE_DIR / "outputs"

ROWS = [
    {
        "doctrine": "Treaty title",
        "function": "Uses written agreements to determine territorial sovereignty or boundaries.",
        "evidence": "Treaty text, protocols, annexes, maps, subsequent practice.",
        "justice_tension": "Treaties may reflect colonial power or unequal bargaining.",
    },
    {
        "doctrine": "Uti possidetis juris",
        "function": "Turns colonial or administrative boundaries into international borders at independence.",
        "evidence": "Colonial laws, administrative records, maps, official acts.",
        "justice_tension": "Stabilizes borders but can freeze colonial divisions.",
    },
    {
        "doctrine": "Effectivités",
        "function": "Considers actual display of state authority where title is unclear.",
        "evidence": "Administration, policing, taxation, infrastructure, permits, public services.",
        "justice_tension": "Can favor states with administrative capacity over local or indigenous claims.",
    },
    {
        "doctrine": "Acquiescence and estoppel",
        "function": "Uses acceptance, silence, or reliance to stabilize territorial claims.",
        "evidence": "Diplomatic correspondence, failure to protest, official maps, conduct.",
        "justice_tension": "Can turn unequal diplomatic silence into legal consequence.",
    },
    {
        "doctrine": "Maritime delimitation",
        "function": "Draws maritime boundaries where coastal entitlements overlap.",
        "evidence": "Coastlines, basepoints, islands, relevant circumstances, proportionality checks.",
        "justice_tension": "Small features can create large maritime consequences.",
    },
]

def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_csv = OUTPUT_DIR / "boundary_doctrine_summary.csv"
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["doctrine", "function", "evidence", "justice_tension"])
        writer.writeheader()
        writer.writerows(ROWS)

    out_md = OUTPUT_DIR / "boundary_doctrine_summary.md"
    lines = ["# Boundary Doctrine Summary", ""]
    for row in ROWS:
        lines.append(f"## {row['doctrine']}")
        lines.append(f"- Function: {row['function']}")
        lines.append(f"- Evidence: {row['evidence']}")
        lines.append(f"- Justice tension: {row['justice_tension']}")
        lines.append("")
    out_md.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {out_csv}")
    print(f"Wrote {out_md}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Create a simple maritime-zone summary table for editorial reference.
"""

from __future__ import annotations

from pathlib import Path
import csv


ARTICLE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ARTICLE_DIR / "outputs"

ZONES = [
    {
        "zone": "Territorial sea",
        "extent": "Up to 12 nautical miles",
        "coastal_state_rights": "Sovereignty, subject to innocent passage",
        "other_state_rights": "Innocent passage",
        "articles": "UNCLOS Articles 2-32",
    },
    {
        "zone": "Contiguous zone",
        "extent": "Up to 24 nautical miles",
        "coastal_state_rights": "Enforcement relating to customs, fiscal, immigration, and sanitary laws",
        "other_state_rights": "Navigation subject to lawful enforcement",
        "articles": "UNCLOS Article 33",
    },
    {
        "zone": "Exclusive economic zone",
        "extent": "Up to 200 nautical miles",
        "coastal_state_rights": "Sovereign rights over natural resources and jurisdiction over artificial islands, marine scientific research, and environmental protection",
        "other_state_rights": "Navigation, overflight, laying cables and pipelines",
        "articles": "UNCLOS Articles 55-75",
    },
    {
        "zone": "Continental shelf",
        "extent": "To outer edge of continental margin or 200 nautical miles; may extend beyond 200 under Article 76",
        "coastal_state_rights": "Rights over seabed and subsoil resources",
        "other_state_rights": "Water-column freedoms depending on zone; high-seas freedoms beyond EEZ",
        "articles": "UNCLOS Articles 76-85",
    },
    {
        "zone": "High seas",
        "extent": "Beyond national jurisdiction",
        "coastal_state_rights": "No sovereignty over high seas",
        "other_state_rights": "Freedoms of navigation, overflight, cables/pipelines, artificial islands, fishing, and scientific research",
        "articles": "UNCLOS Articles 86-120",
    },
    {
        "zone": "The Area",
        "extent": "Seabed and ocean floor beyond national jurisdiction",
        "coastal_state_rights": "No national appropriation",
        "other_state_rights": "Activities organized through ISA for the benefit of humankind as a whole",
        "articles": "UNCLOS Part XI",
    },
]


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_csv = OUTPUT_DIR / "maritime_zone_summary.csv"
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["zone", "extent", "coastal_state_rights", "other_state_rights", "articles"],
        )
        writer.writeheader()
        writer.writerows(ZONES)

    out_md = OUTPUT_DIR / "maritime_zone_summary.md"
    lines = ["# Maritime Zone Summary", ""]
    for zone in ZONES:
        lines.append(f"## {zone['zone']}")
        lines.append(f"- Extent: {zone['extent']}")
        lines.append(f"- Coastal-state rights: {zone['coastal_state_rights']}")
        lines.append(f"- Other-state rights: {zone['other_state_rights']}")
        lines.append(f"- Key provisions: {zone['articles']}")
        lines.append("")
    out_md.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out_csv}")
    print(f"Wrote {out_md}")


if __name__ == "__main__":
    main()

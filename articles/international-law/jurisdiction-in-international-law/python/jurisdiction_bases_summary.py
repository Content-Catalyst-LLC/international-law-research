#!/usr/bin/env python3
"""
Create a compact jurisdiction-bases summary for editorial reference.
"""

from __future__ import annotations

import csv
from pathlib import Path


ARTICLE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ARTICLE_DIR / "outputs"

ROWS = [
    {
        "basis": "Territoriality",
        "connecting_factor": "Conduct, persons, property, or effects within territory",
        "ordinary_use": "Criminal law, civil regulation, public administration, taxation, territorial enforcement",
        "risks_or_limits": "Effects doctrine can become overbroad; foreign enforcement requires consent",
        "key_sources": "General international law; Lotus; domestic practice",
    },
    {
        "basis": "Nationality",
        "connecting_factor": "Legal bond between state and national",
        "ordinary_use": "Criminal law, taxation, military service, anti-corruption, diplomatic protection",
        "risks_or_limits": "Can conflict with territorial jurisdiction of another state",
        "key_sources": "Customary international law and domestic statutes",
    },
    {
        "basis": "Corporate nationality",
        "connecting_factor": "Incorporation, seat, headquarters, listing, control, or regulatory nexus",
        "ordinary_use": "Financial regulation, sanctions, anti-corruption, due diligence, export controls",
        "risks_or_limits": "Can project powerful-state regulation through global corporate networks",
        "key_sources": "Domestic statutes, investment law, corporate regulation, sanctions practice",
    },
    {
        "basis": "Passive personality",
        "connecting_factor": "Nationality of the victim",
        "ordinary_use": "Terrorism, attacks on nationals abroad, serious transnational crimes",
        "risks_or_limits": "Historically controversial and should be restrained to serious cases",
        "key_sources": "Treaty practice and domestic criminal statutes",
    },
    {
        "basis": "Protective principle",
        "connecting_factor": "Threat to core state security or governmental functions",
        "ordinary_use": "Espionage, counterfeiting, national security, immigration fraud, attacks on public institutions",
        "risks_or_limits": "Security can be defined too broadly and become jurisdictional overreach",
        "key_sources": "Customary international law and domestic statutes",
    },
    {
        "basis": "Universal jurisdiction",
        "connecting_factor": "Nature of the offense as one of international concern",
        "ordinary_use": "Piracy and certain grave international crimes",
        "risks_or_limits": "Interacts with immunity, presence requirements, selectivity, and fair-trial safeguards",
        "key_sources": "Customary international law, treaties, domestic universal-jurisdiction statutes",
    },
    {
        "basis": "Enforcement abroad",
        "connecting_factor": "Physical coercive action outside national territory",
        "ordinary_use": "Ordinarily through extradition, mutual legal assistance, consent, or treaty mechanisms",
        "risks_or_limits": "Unilateral enforcement abroad directly violates territorial sovereignty absent consent or legal authority",
        "key_sources": "Sovereignty, non-intervention, use-of-force law, mutual legal assistance practice",
    },
]


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    out_csv = OUTPUT_DIR / "jurisdiction_bases_summary.csv"
    fieldnames = ["basis", "connecting_factor", "ordinary_use", "risks_or_limits", "key_sources"]
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(ROWS)

    out_md = OUTPUT_DIR / "jurisdiction_bases_summary.md"
    lines = ["# Jurisdiction Bases Summary", ""]
    for row in ROWS:
        lines.append(f"## {row['basis']}")
        lines.append(f"- Connecting factor: {row['connecting_factor']}")
        lines.append(f"- Ordinary use: {row['ordinary_use']}")
        lines.append(f"- Risks or limits: {row['risks_or_limits']}")
        lines.append(f"- Key sources: {row['key_sources']}")
        lines.append("")
    out_md.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {out_csv}")
    print(f"Wrote {out_md}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ARTICLE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ARTICLE_DIR / "outputs"

ROWS = [
    {
        "dimension": "Primary actors",
        "public": "States, international organizations, peoples, and some non-state actors",
        "private": "Individuals, corporations, families, commercial parties, and private litigants",
        "overlap": "Investment law and arbitration often connect private claimants to public obligations.",
    },
    {
        "dimension": "Core questions",
        "public": "What are the obligations of states and international legal subjects?",
        "private": "Which court has jurisdiction, which law applies, and will a judgment be recognized?",
        "overlap": "Jurisdiction appears in both fields but performs different functions.",
    },
    {
        "dimension": "Sources",
        "public": "Treaties, custom, general principles, judicial decisions, scholarly writings",
        "private": "Domestic conflict rules, private international law statutes, Hague conventions, party agreements",
        "overlap": "Treaties can structure both public obligations and private litigation rules.",
    },
    {
        "dimension": "Institutions",
        "public": "ICJ, UN organs, treaty bodies, international criminal courts, arbitral tribunals",
        "private": "Domestic courts, HCCH instruments, arbitral institutions, recognition/enforcement systems",
        "overlap": "ICSID and investment arbitration are important hybrid institutions.",
    },
    {
        "dimension": "Typical disputes",
        "public": "Use of force, treaties, human rights, state responsibility, law of the sea",
        "private": "Contracts, torts, family law, property, commercial disputes, foreign judgments",
        "overlap": "Global supply chains and digital commerce increasingly blur the boundary.",
    },
]

def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_csv = OUTPUT_DIR / "public_private_comparison.csv"
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["dimension", "public", "private", "overlap"])
        writer.writeheader()
        writer.writerows(ROWS)

    out_md = OUTPUT_DIR / "public_private_comparison.md"
    lines = ["# Public vs Private International Law Comparison", ""]
    for row in ROWS:
        lines.append(f"## {row['dimension']}")
        lines.append(f"- Public international law: {row['public']}")
        lines.append(f"- Private international law: {row['private']}")
        lines.append(f"- Overlap or tension: {row['overlap']}")
        lines.append("")
    out_md.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {out_csv}")
    print(f"Wrote {out_md}")

if __name__ == "__main__":
    main()

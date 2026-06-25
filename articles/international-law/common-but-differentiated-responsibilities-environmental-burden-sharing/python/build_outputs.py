#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(parents=True, exist_ok=True)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_json(name: str, payload) -> None:
    (OUT / name).write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_markdown_table(name: str, title: str, rows: list[dict[str, str]], columns: list[str]) -> None:
    lines = [f"# {title}", ""]
    lines.append("| " + " | ".join(columns) + " |")
    lines.append("| " + " | ".join(["---"] * len(columns)) + " |")
    for row in rows:
        cleaned = [row.get(col, "").replace("|", "-").replace("\n", " ") for col in columns]
        lines.append("| " + " | ".join(cleaned) + " |")
    lines.append("")
    (OUT / name).write_text("\n".join(lines), encoding="utf-8")


metadata = json.loads((ROOT / "metadata" / "article_metadata.json").read_text(encoding="utf-8"))
primary = read_csv(ROOT / "sources" / "primary_authorities.csv")
further = read_csv(ROOT / "sources" / "further_reading.csv")
doctrine = read_csv(ROOT / "data" / "cbdr_doctrine_matrix.csv")
mechanisms = read_csv(ROOT / "data" / "burden_sharing_mechanisms.csv")
risks = read_csv(ROOT / "data" / "legal_politics_risk_matrix.csv")

summary = {
    "title": metadata["title"],
    "slug": metadata["slug"],
    "html_in_repository": metadata["github_html_excluded"] is False,
    "html_excluded_policy": metadata["github_html_policy"],
    "counts": {
        "primary_authorities": len(primary),
        "further_reading": len(further),
        "doctrine_rows": len(doctrine),
        "burden_sharing_mechanisms": len(mechanisms),
        "legal_politics_risks": len(risks),
    },
}

write_json("article_support_summary.json", summary)
write_markdown_table("primary_authorities.md", "Primary Authorities", primary, ["type", "title", "year", "institution_or_source", "notes"])
write_markdown_table("cbdr_doctrine_matrix.md", "CBDR Doctrine Matrix", doctrine, ["concept", "legal_location", "core_question", "burden_sharing_function"])
write_markdown_table("burden_sharing_mechanisms.md", "Burden-Sharing Mechanisms", mechanisms, ["mechanism", "legal_context", "what_it_allocates", "distribution_issue"])
write_markdown_table("legal_politics_risk_matrix.md", "Legal Politics Risk Matrix", risks, ["risk_area", "burden_sharing_conflict", "legal_pressure_point", "affected_actors"])

print(f"Generated outputs for: {metadata['title']}")
print("Full WordPress article HTML is intentionally excluded from this GitHub package.")

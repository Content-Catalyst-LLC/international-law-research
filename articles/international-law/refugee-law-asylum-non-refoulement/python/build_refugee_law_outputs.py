#!/usr/bin/env python3
from pathlib import Path
import csv, json

ARTICLE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ARTICLE_DIR / "data"
OUT_DIR = ARTICLE_DIR / "outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)

def read_csv(name):
    with (DATA_DIR / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

payload = {
    "article": "Refugee Law, Asylum, and the Principle of Non-Refoulement",
    "slug": "refugee-law-asylum-non-refoulement",
    "matrices": {
        "framework": read_csv("refugee_law_framework_matrix.csv"),
        "non_refoulement": read_csv("non_refoulement_analysis_matrix.csv"),
        "protection_pathways": read_csv("protection_pathways_matrix.csv"),
        "primary_authorities": read_csv("primary_authorities.csv"),
        "further_reading": read_csv("further_reading.csv"),
    },
}
(OUT_DIR / "refugee_law_research_bundle.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Wrote {OUT_DIR / 'refugee_law_research_bundle.json'}")

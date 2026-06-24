#!/usr/bin/env python3
"""Build simple derived outputs for the High Seas / Deep Seabed article folder."""
from __future__ import annotations
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)
metadata = json.loads((ROOT / "metadata" / "article_metadata.json").read_text(encoding="utf-8"))
summary = {
    "title": metadata["title"],
    "slug": metadata["slug"],
    "focus_keyword": metadata["focus_keyword"],
    "series": metadata["series"],
    "repository_folder": metadata["repository_folder"],
    "primary_data_files": [
        "data/global_commons_framework_matrix.csv",
        "data/ocean_commons_institutions.csv",
        "data/risk_and_governance_matrix.csv",
        "references/primary_authorities.csv",
        "references/further_reading.csv",
    ],
}
(OUT / "article_summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
md = [f"# {metadata['title']}", "", f"Slug: `{metadata['slug']}`", "", f"Focus keyword: **{metadata['focus_keyword']}**", "", metadata["excerpt_139_words"], ""]
(OUT / "article_summary.md").write_text("\n".join(md), encoding="utf-8")
row_path = OUT / "catalyst_data_row.csv"
with row_path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["slug", "title", "seo_title", "focus_keyword", "series", "repository_folder", "wordpress_html"])
    writer.writeheader()
    writer.writerow({
        "slug": metadata["slug"],
        "title": metadata["title"],
        "seo_title": metadata["seo_title"],
        "focus_keyword": metadata["focus_keyword"],
        "series": metadata["series"],
        "repository_folder": metadata["repository_folder"],
        "wordpress_html": metadata["wordpress_html"],
    })
print(f"Built outputs in {OUT}")

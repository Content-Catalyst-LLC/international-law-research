from __future__ import annotations
import csv
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(parents=True, exist_ok=True)
metadata = json.loads((ROOT / "metadata" / "article_metadata.json").read_text(encoding="utf-8"))
summary = {
    "slug": metadata["slug"],
    "title": metadata["title"],
    "seo_title": metadata["seo_title"],
    "focus_keyword": metadata["focus_keyword"],
    "series": metadata["series"],
    "repository_folder": metadata["repository_folder"],
    "wordpress_html": metadata["wordpress_html"],
    "tags": metadata.get("tags", []),
}
(OUTPUTS / "article_summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
with (OUTPUTS / "catalyst_data_row.csv").open("w", newline="", encoding="utf-8") as f:
    fields = ["slug", "title", "seo_title", "focus_keyword", "series", "repository_folder", "wordpress_html", "excerpt"]
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerow({
        "slug": metadata["slug"],
        "title": metadata["title"],
        "seo_title": metadata["seo_title"],
        "focus_keyword": metadata["focus_keyword"],
        "series": metadata["series"],
        "repository_folder": metadata["repository_folder"],
        "wordpress_html": metadata["wordpress_html"],
        "excerpt": metadata["excerpt_139_words"],
    })
print(f"Wrote outputs for {metadata['slug']}")

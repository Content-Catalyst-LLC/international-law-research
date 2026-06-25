from __future__ import annotations
import csv
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
html_path = ROOT / "docs" / "wordpress_article_html.html"
out_path = ROOT / "outputs" / "link_inventory.csv"
out_path.parent.mkdir(parents=True, exist_ok=True)
html = html_path.read_text(encoding="utf-8")
url_re = re.compile("https?://[^\\s\\\"'<>]+")
links = sorted(set(match.group(0).rstrip(".)]") for match in url_re.finditer(html)))
with out_path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["url"])
    writer.writeheader()
    for url in links:
        writer.writerow({"url": url})
print(f"Wrote {len(links)} links to {out_path}")

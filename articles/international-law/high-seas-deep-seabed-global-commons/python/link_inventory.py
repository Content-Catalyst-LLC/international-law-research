#!/usr/bin/env python3
"""Extract external links from the WordPress HTML into outputs/link_inventory.csv."""
from __future__ import annotations
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
html = (ROOT / "docs" / "wordpress_article_html.html").read_text(encoding="utf-8")
urls = sorted(set(re.findall("https?://[^\\s\\\"'<>]+", html)))
out = ROOT / "outputs" / "link_inventory.csv"
out.parent.mkdir(exist_ok=True)
with out.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["url"])
    for url in urls:
        writer.writerow([url])
print(f"Wrote {len(urls)} links to {out}")

#!/usr/bin/env python3
from __future__ import annotations
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "docs" / "wordpress_article_html.html"
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)
URL_RE = re.compile("https?://[^\\s\\\"'<>]+")
urls = sorted(set(URL_RE.findall(HTML.read_text(encoding="utf-8"))))
with (OUTPUTS / "link_inventory.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.writer(handle)
    writer.writerow(["url"])
    for url in urls:
        writer.writerow([url])
print(f"Wrote outputs/link_inventory.csv with {len(urls)} links")

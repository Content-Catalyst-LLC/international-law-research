#!/usr/bin/env python3
from pathlib import Path
import json
import re

base = Path(__file__).resolve().parents[1]
html_path = base / "docs" / "wordpress_article_html.html"
out_path = base / "outputs" / "link_audit.json"

URL_RE = re.compile(r"https?://[^\s\"'<>]+")
urls = []
if html_path.exists():
    urls.extend(URL_RE.findall(html_path.read_text(encoding="utf-8", errors="ignore")))

for csv_path in sorted((base / "data").glob("*.csv")):
    urls.extend(URL_RE.findall(csv_path.read_text(encoding="utf-8", errors="ignore")))

cleaned = []
seen = set()
for url in urls:
    url = url.rstrip(".,);]")
    if url not in seen:
        seen.add(url)
        cleaned.append(url)

out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps({"count": len(cleaned), "urls": cleaned}, indent=2) + "\n", encoding="utf-8")
print(f"Wrote {out_path} ({len(cleaned)} URLs)")

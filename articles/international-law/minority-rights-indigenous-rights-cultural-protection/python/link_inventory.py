#!/usr/bin/env python3
import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
HTML = BASE / "docs" / "wordpress_article_html.html"
OUT = BASE / "outputs"
OUT.mkdir(exist_ok=True)
URL_RE = re.compile("https?://[^\\s\\\"'<>]+")
urls = sorted(set(URL_RE.findall(HTML.read_text(encoding="utf-8"))))
rows = [{"url": u, "category": "external"} for u in urls]
(OUT / "link_inventory.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Found {len(rows)} external links")


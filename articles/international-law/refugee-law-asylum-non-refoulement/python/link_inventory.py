#!/usr/bin/env python3
from pathlib import Path
import json, re

ARTICLE_DIR = Path(__file__).resolve().parents[1]
HTML = ARTICLE_DIR / "docs" / "wordpress_article_html.html"
OUT_DIR = ARTICLE_DIR / "outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)
URL_RE = re.compile("https?://[^\s\"'<>]+")
html = HTML.read_text(encoding="utf-8")
links = sorted(set(URL_RE.findall(html)))
(OUT_DIR / "link_inventory.json").write_text(json.dumps({"count": len(links), "links": links}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Found {len(links)} links")

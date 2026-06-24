#!/usr/bin/env python3
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "docs" / "wordpress_article_html.html"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)
URL_RE = re.compile("https?://[^\\s\\\"'<>]+")

html = HTML.read_text(encoding="utf-8") if HTML.exists() else ""
urls = sorted(set(URL_RE.findall(html)))
payload = {"article": ROOT.name, "url_count": len(urls), "urls": urls}
(OUT / "link_inventory.json").write_text(
    json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
)
print(f"found {len(urls)} URLs")

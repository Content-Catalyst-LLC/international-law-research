#!/usr/bin/env python3
"""Extract external and internal links from the WordPress HTML."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "docs" / "wordpress_article_html.html"
OUT = ROOT / "outputs" / "link_inventory.json"
OUT.parent.mkdir(exist_ok=True)

text = HTML.read_text(encoding="utf-8")
urls = sorted(set(re.findall("https?://[^\\s\\\"'<>]+", text)))
internal = sorted(set(re.findall('href="(/[^"#][^"]*)"', text)))

payload = {
    "external_links": urls,
    "internal_links": internal,
    "external_count": len(urls),
    "internal_count": len(internal),
}

with OUT.open("w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("Wrote", OUT)

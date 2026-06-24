#!/usr/bin/env python3
"""Inventory links in the Civil and Political Rights article HTML."""
from __future__ import annotations

import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
HTML_PATH = BASE / "docs" / "wordpress_article_html.html"
OUTPUTS = BASE / "outputs"
OUTPUTS.mkdir(exist_ok=True)
URL_RE = re.compile("https?://[^\\s\\\"'<>]+")


def main() -> None:
    html = HTML_PATH.read_text(encoding="utf-8")
    links = sorted(set(URL_RE.findall(html)))
    payload = {"count": len(links), "links": links}
    (OUTPUTS / "link_inventory.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Found {len(links)} external links")


if __name__ == "__main__":
    main()

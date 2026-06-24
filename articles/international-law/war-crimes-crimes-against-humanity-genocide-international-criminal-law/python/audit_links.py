#!/usr/bin/env python3
"""Lightweight link audit for article HTML."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

URL_RE = re.compile("https?://[^\\s<>]+")


def main() -> None:
    if len(sys.argv) > 1:
        html_path = Path(sys.argv[1])
    else:
        html_path = Path(__file__).resolve().parents[1] / "docs" / "wordpress_article_html.html"
    root = Path(__file__).resolve().parents[1]
    outputs = root / "outputs"
    outputs.mkdir(exist_ok=True)
    text = html_path.read_text(encoding="utf-8")
    urls = sorted(set(URL_RE.findall(text)))
    report = {
        "html_path": str(html_path),
        "url_count": len(urls),
        "urls": urls,
    }
    out_path = outputs / "link_audit.json"
    out_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Audited {len(urls)} URLs -> {out_path}")


if __name__ == "__main__":
    main()

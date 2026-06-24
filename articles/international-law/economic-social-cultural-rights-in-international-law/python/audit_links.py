#!/usr/bin/env python3
"""Create a simple link inventory for the article HTML and data files."""
from __future__ import annotations

import csv
import re
from pathlib import Path

ARTICLE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ARTICLE_DIR / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
URL_RE = re.compile("https?://[^\\s\\\"'<>]+")


def main() -> None:
    rows = []
    paths = [ARTICLE_DIR / "docs" / "wordpress_article_html.html"]
    paths.extend(sorted(ARTICLE_DIR.glob("data/*.csv")))
    for path in paths:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for url in sorted(set(URL_RE.findall(text))):
            rows.append({"file": str(path.relative_to(ARTICLE_DIR)), "url": url.rstrip(").,;")})
    out = OUTPUT_DIR / "link_inventory.csv"
    with out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["file", "url"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {out.relative_to(ARTICLE_DIR)} with {len(rows)} links")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Extract URLs from article files and write a local audit report.

This is intentionally local-only: it does not perform network requests.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ARTICLE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ARTICLE_DIR / "outputs"
URL_RE = re.compile("https?://[^\\s<>\"']+")


def main() -> None:
    urls: dict[str, list[str]] = {}
    for path in sorted(ARTICLE_DIR.rglob("*")):
        if path.is_file() and path.suffix.lower() in {".html", ".md", ".csv", ".json", ".sql"}:
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            found = sorted(set(URL_RE.findall(text)))
            if found:
                urls[str(path.relative_to(ARTICLE_DIR))] = found
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / "link_audit.json"
    out_path.write_text(json.dumps(urls, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()

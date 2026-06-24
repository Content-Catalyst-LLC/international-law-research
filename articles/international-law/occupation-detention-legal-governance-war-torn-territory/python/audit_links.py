#!/usr/bin/env python3
"""Local URL inventory for the Occupation / Detention article.

This script extracts URLs from local article, docs, and CSV files and writes a
JSON inventory. It does not make network requests.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, List


ARTICLE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ARTICLE_DIR / "outputs"
URL_RE = re.compile(r'https?://[^\s"\'<>]+')


def scan_file(path: Path) -> List[str]:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return []
    return sorted(set(URL_RE.findall(text)))


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    candidates = []
    for pattern in [
        "README.md",
        "metadata.json",
        "docs/*.md",
        "docs/*.html",
        "data/*.csv",
        "sql/*.sql",
    ]:
        candidates.extend(ARTICLE_DIR.glob(pattern))

    records: List[Dict[str, object]] = []
    for path in sorted(set(candidates)):
        urls = scan_file(path)
        if urls:
            records.append(
                {
                    "file": str(path.relative_to(ARTICLE_DIR)),
                    "url_count": len(urls),
                    "urls": urls,
                }
            )

    out_path = OUTPUT_DIR / "link_audit.json"
    out_path.write_text(
        json.dumps({"files_scanned": len(candidates), "records": records}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Basic structural URL audit for International Courts and Tribunals source metadata.
"""

from __future__ import annotations

import csv
from pathlib import Path
from urllib.parse import urlparse


ARTICLE_DIR = Path(__file__).resolve().parents[1]


def valid_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def main() -> None:
    files = [
        ARTICLE_DIR / "data" / "primary_sources.csv",
        ARTICLE_DIR / "data" / "secondary_sources.csv",
    ]

    bad: list[str] = []

    for path in files:
        if not path.exists():
            continue

        with path.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                url = row.get("url", "")
                title = row.get("source_title") or row.get("title") or "Untitled"
                if url and not valid_url(url):
                    bad.append(f"{path.name}: {title}: {url}")

    if bad:
        raise SystemExit("Invalid URLs:\n" + "\n".join(bad))

    print("International Courts and Tribunals source URLs look structurally valid.")


if __name__ == "__main__":
    main()

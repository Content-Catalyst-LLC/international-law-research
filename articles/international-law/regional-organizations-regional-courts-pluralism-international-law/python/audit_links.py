#!/usr/bin/env python3
"""Lightweight link audit for source CSVs in this article folder.

This script avoids network calls by default. It checks that URL fields exist and appear plausible.
"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def iter_csv_urls():
    for csv_path in sorted(DATA.glob("*.csv")):
        with csv_path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader, start=2):
                url = (row.get("url") or "").strip()
                if url:
                    yield csv_path.name, i, url


def main() -> int:
    problems = []
    for filename, line_no, url in iter_csv_urls():
        if not (url.startswith("https://") or url.startswith("http://")):
            problems.append((filename, line_no, url))
    if problems:
        print("Potential URL problems:")
        for filename, line_no, url in problems:
            print(f"- {filename}:{line_no}: {url}")
        return 1
    print("All listed URLs are syntactically plausible.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Lightweight CSV link audit for this article folder."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
for csv_path in sorted((ROOT / "data").glob("*.csv")):
    with csv_path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        missing = [row for row in reader if "url" in row and not (row.get("url") or "").strip()]
    print(f"{csv_path.name}: {len(missing)} rows missing URL")

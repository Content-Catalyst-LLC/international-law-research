#!/usr/bin/env python3
"""Inventory URLs in the article folder."""
from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(parents=True, exist_ok=True)
URL_RE = re.compile("https?://[^\s\"'<>]+")

rows = []
for path in sorted(ROOT.rglob("*")):
    if path.is_file() and path.suffix.lower() in {".html", ".md", ".json", ".csv", ".sql"}:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for url in sorted(set(URL_RE.findall(text))):
            rows.append({"file": str(path.relative_to(ROOT)), "url": url.rstrip(".,);]")})

out_path = OUT / "link_inventory.csv"
with out_path.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=["file", "url"])
    writer.writeheader()
    writer.writerows(rows)
print(f"Wrote {out_path} with {len(rows)} URLs")

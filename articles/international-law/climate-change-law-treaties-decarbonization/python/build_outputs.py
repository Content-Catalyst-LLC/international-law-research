#!/usr/bin/env python3
"""Build simple local outputs for the climate change law article folder."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
META = ROOT / "metadata" / "article_metadata.json"
DATA = ROOT / "data"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

metadata = json.loads(META.read_text(encoding="utf-8"))

summary = [
    f"# {metadata['actual_title']}",
    "",
    f"**Focus keyword:** {metadata['focus_keyword']}",
    f"**Slug:** `{metadata['slug']}`",
    "",
    "## Excerpt",
    "",
    metadata["excerpt"],
    "",
    "## Tags",
    "",
    ", ".join(metadata["tags"]),
]
(OUT / "article_summary.md").write_text("\n".join(summary) + "\n", encoding="utf-8")

rows = []
for csv_path in sorted(DATA.glob("*.csv")):
    with csv_path.open(newline="", encoding="utf-8") as fh:
        reader = csv.reader(fh)
        try:
            next(reader)
        except StopIteration:
            count = 0
        else:
            count = sum(1 for _ in reader)
    rows.append([csv_path.name, str(count)])

with (OUT / "source_inventory.csv").open("w", newline="", encoding="utf-8") as fh:
    writer = csv.writer(fh)
    writer.writerow(["file", "records"])
    writer.writerows(rows)

with (OUT / "catalyst_data_export_row.csv").open("w", newline="", encoding="utf-8") as fh:
    writer = csv.writer(fh)
    writer.writerow(["series", "slug", "title", "focus_keyword", "tags"])
    writer.writerow([metadata["series"], metadata["slug"], metadata["actual_title"], metadata["focus_keyword"], "; ".join(metadata["tags"])])

print(f"Wrote outputs to {OUT}")

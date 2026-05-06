"""
Export source metadata for the International Law research folder.
"""

from __future__ import annotations

import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "data" / "legal_sources.csv"
OUTPUT_FILE = BASE_DIR / "outputs" / "primary_authorities.md"


def export_primary_authorities() -> None:
    """Export primary authority metadata as a Markdown list."""
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with DATA_FILE.open(newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    lines = ["# Primary Authorities", ""]

    for row in rows:
        lines.append(
            f"- {row['institution']} ({row['year']}) "
            f"*{row['source_title']}*. Available at: {row['url']}."
        )

    OUTPUT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT_FILE}")


if __name__ == "__main__":
    export_primary_authorities()

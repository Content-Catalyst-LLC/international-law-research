#!/usr/bin/env python3
"""Build compact JSON outputs from the IHL article CSV matrices.

This helper is intentionally local and dependency-free. It reads every CSV in
../data and writes a single JSON payload to ../outputs/ihl_matrices.json.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def main() -> None:
    payload: dict[str, object] = {
        "article_slug": "international-humanitarian-law-geneva-conventions-regulation-armed-conflict",
        "article_title": "International Humanitarian Law: The Geneva Conventions and the Regulation of Armed Conflict",
        "generated_from": "article data CSV matrices",
        "matrices": {},
    }

    matrices: dict[str, list[dict[str, str]]] = {}
    if DATA_DIR.exists():
        for csv_path in sorted(DATA_DIR.glob("*.csv")):
            matrices[csv_path.stem] = read_csv(csv_path)

    payload["matrices"] = matrices
    out_path = OUTPUT_DIR / "ihl_matrices.json"
    out_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()

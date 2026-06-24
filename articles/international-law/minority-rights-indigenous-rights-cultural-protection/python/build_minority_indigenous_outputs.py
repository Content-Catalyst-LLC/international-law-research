#!/usr/bin/env python3
import csv
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
OUT = BASE / "outputs"
OUT.mkdir(exist_ok=True)

payload = {
    "article": json.loads((BASE / "metadata.json").read_text(encoding="utf-8")),
    "tables": {},
}

for csv_path in sorted(DATA.glob("*.csv")):
    with csv_path.open(newline="", encoding="utf-8") as f:
        payload["tables"][csv_path.stem] = list(csv.DictReader(f))

summary = {
    "title": payload["article"]["title"],
    "slug": payload["article"]["slug"],
    "table_count": len(payload["tables"]),
    "tables": {name: len(rows) for name, rows in payload["tables"].items()},
    "focus": [
        "minority rights",
        "Indigenous rights",
        "cultural protection",
        "language and religion",
        "land and resources",
        "free, prior, and informed consent",
        "heritage and cultural survival",
        "implementation mechanisms",
    ],
}

(OUT / "minority_indigenous_rights_research_payload.json").write_text(
    json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
)
(OUT / "minority_indigenous_rights_summary.json").write_text(
    json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
)
print(json.dumps(summary, indent=2, ensure_ascii=False))


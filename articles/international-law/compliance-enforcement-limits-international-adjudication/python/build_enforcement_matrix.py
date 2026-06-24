#!/usr/bin/env python3
from pathlib import Path
import csv
import json

base = Path(__file__).resolve().parents[1]
out = base / "outputs" / "enforcement_matrices.json"

payload = {}
for name in ["enforcement_mechanisms", "compliance_pathways"]:
    path = base / "data" / f"{name}.csv"
    with path.open(newline="", encoding="utf-8") as f:
        payload[name] = list(csv.DictReader(f))

out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Wrote {out}")

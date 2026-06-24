from pathlib import Path
import csv
import json

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
OUTPUTS = BASE / "outputs"
OUTPUTS.mkdir(parents=True, exist_ok=True)


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))

payload = {
    "article": "Nuremberg, Tokyo, and the Historical Development of International Criminal Justice",
    "matrices": {
        "development": read_csv(DATA / "nuremberg_tokyo_development_matrix.csv"),
        "tribunals": read_csv(DATA / "tribunal_comparison_matrix.csv"),
        "doctrine_legacy": read_csv(DATA / "doctrine_legacy_matrix.csv"),
    },
    "source_counts": {
        "primary_sources": len(read_csv(DATA / "primary_sources.csv")),
        "secondary_sources": len(read_csv(DATA / "secondary_sources.csv")),
    },
}

out_path = OUTPUTS / "nuremberg_tokyo_matrices.json"
out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Wrote {out_path}")

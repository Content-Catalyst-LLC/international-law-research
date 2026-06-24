from __future__ import annotations
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def read_csv(name: str) -> list[dict[str, str]]:
    path = DATA_DIR / name
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_json(name: str, payload: object) -> None:
    out_path = OUTPUT_DIR / name
    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    payload = {
        "article": "The International Criminal Court and the Politics of Global Justice",
        "primary_sources": read_csv("primary_sources.csv"),
        "secondary_sources": read_csv("secondary_sources.csv"),
        "institutional_architecture": read_csv("icc_institutional_architecture.csv"),
        "admissibility_complementarity_matrix": read_csv("icc_admissibility_complementarity_matrix.csv"),
        "cooperation_enforcement_matrix": read_csv("icc_cooperation_enforcement_matrix.csv"),
    }
    write_json("icc_global_justice_matrices.json", payload)
    summary = {
        "matrix_count": 3,
        "primary_source_count": len(payload["primary_sources"]),
        "secondary_source_count": len(payload["secondary_sources"]),
        "institutional_component_count": len(payload["institutional_architecture"]),
    }
    write_json("icc_global_justice_summary.json", summary)


if __name__ == "__main__":
    main()

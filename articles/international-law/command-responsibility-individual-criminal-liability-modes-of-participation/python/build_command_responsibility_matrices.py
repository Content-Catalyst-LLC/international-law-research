#!/usr/bin/env python3
from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)


def read_csv(name: str):
    path = DATA / name
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

payload = {
    "article": "Command Responsibility, Individual Criminal Liability, and Modes of Participation",
    "article_slug": ROOT.name,
    "liability_modes": read_csv("liability_modes_matrix.csv"),
    "command_responsibility_elements": read_csv("command_responsibility_matrix.csv"),
    "evidence_linkage": read_csv("evidence_linkage_matrix.csv"),
    "primary_sources": read_csv("primary_sources.csv"),
    "secondary_sources": read_csv("secondary_sources.csv"),
}

(OUT / "command_responsibility_matrices.json").write_text(
    json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
)

summary_lines = [
    "# Command Responsibility / Liability Matrices",
    "",
    f"Article folder: {ROOT.name}",
    f"Liability modes: {len(payload['liability_modes'])}",
    f"Command responsibility elements: {len(payload['command_responsibility_elements'])}",
    f"Evidence categories: {len(payload['evidence_linkage'])}",
    f"Primary authorities: {len(payload['primary_sources'])}",
    f"Secondary sources: {len(payload['secondary_sources'])}",
    "",
]
(OUT / "command_responsibility_outputs_summary.md").write_text(
    "\n".join(summary_lines) + "\n",
    encoding="utf-8",
)
print("wrote", OUT / "command_responsibility_matrices.json")
print("wrote", OUT / "command_responsibility_outputs_summary.md")

#!/usr/bin/env python3
"""
Audit CSV metadata for missing URLs and weak source records.

Usage:
    python3 python/citation_audit.py --data-dir data --output outputs/citation-audit.md
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


CSV_FILES = [
    "regimes.csv",
    "treaties.csv",
    "institutions.csv",
    "cases.csv",
    "planned-articles.csv",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    """Read a CSV file into a list of dictionaries."""
    if not path.exists():
        return []

    with path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def audit_urls(data_dir: Path) -> list[str]:
    """Return Markdown audit lines for missing or incomplete URL fields."""
    findings: list[str] = []

    for csv_file in CSV_FILES:
        path = data_dir / csv_file
        rows = read_csv(path)

        for index, row in enumerate(rows, start=2):
            url_fields = [key for key in row.keys() if "url" in key.lower()]

            for field in url_fields:
                value = (row.get(field) or "").strip()
                title = row.get("title") or row.get("name") or row.get("regime_name") or row.get("slug") or "Untitled record"

                if not value:
                    findings.append(f"- `{csv_file}` row {index}: missing `{field}` for **{title}**.")
                elif not value.startswith(("http://", "https://")):
                    findings.append(f"- `{csv_file}` row {index}: suspicious `{field}` value for **{title}**: `{value}`.")

    return findings


def audit_source_types(data_dir: Path) -> list[str]:
    """Return Markdown audit lines for missing source type fields."""
    findings: list[str] = []

    for csv_file in ["treaties.csv", "cases.csv"]:
        path = data_dir / csv_file
        rows = read_csv(path)

        for index, row in enumerate(rows, start=2):
            source_type = (row.get("source_type") or "").strip()
            if not source_type:
                title = row.get("title") or "Untitled record"
                findings.append(f"- `{csv_file}` row {index}: missing `source_type` for **{title}**.")

    return findings


def write_report(output_path: Path, url_findings: list[str], source_type_findings: list[str]) -> None:
    """Write the audit report."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        file.write("# International Law Citation and Metadata Audit\n\n")

        file.write("## Missing or Suspicious URLs\n\n")
        if url_findings:
            file.write("\n".join(url_findings))
            file.write("\n\n")
        else:
            file.write("No missing or suspicious URL fields found.\n\n")

        file.write("## Missing Source Types\n\n")
        if source_type_findings:
            file.write("\n".join(source_type_findings))
            file.write("\n")
        else:
            file.write("No missing source type fields found.\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit International Law citation metadata.")
    parser.add_argument("--data-dir", default="data", help="Directory containing CSV data files.")
    parser.add_argument("--output", default="outputs/citation-audit.md", help="Markdown audit output path.")
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    output_path = Path(args.output)

    url_findings = audit_urls(data_dir)
    source_type_findings = audit_source_types(data_dir)
    write_report(output_path, url_findings, source_type_findings)

    print(f"Wrote citation audit to {output_path}")


if __name__ == "__main__":
    main()

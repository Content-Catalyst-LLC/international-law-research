#!/usr/bin/env python3
"""
Export the International Law article roadmap from a SQLite database.

Usage:
    python3 python/export_article_roadmap.py --db international_law.db --output outputs/article-roadmap.md
"""

from __future__ import annotations

import argparse
import csv
import sqlite3
from pathlib import Path


def fetch_roadmap(db_path: Path) -> list[sqlite3.Row]:
    """Fetch article-roadmap records from the database."""
    if not db_path.exists():
        raise FileNotFoundError(f"Database not found: {db_path}")

    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row

    try:
        return list(
            connection.execute(
                """
                SELECT
                    priority,
                    status,
                    regime_name,
                    title,
                    slug,
                    article_type,
                    source_focus,
                    notes
                FROM v_article_roadmap
                ORDER BY priority ASC, regime_name ASC, title ASC;
                """
            )
        )
    finally:
        connection.close()


def write_markdown(rows: list[sqlite3.Row], output_path: Path) -> None:
    """Write the roadmap as a Markdown table."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        file.write("# International Law Article Roadmap\n\n")
        file.write("| Priority | Status | Regime | Title | Slug | Type | Source Focus |\n")
        file.write("|---:|---|---|---|---|---|---|\n")

        for row in rows:
            file.write(
                "| {priority} | {status} | {regime} | {title} | `{slug}` | {article_type} | {source_focus} |\n".format(
                    priority=row["priority"],
                    status=row["status"],
                    regime=row["regime_name"],
                    title=row["title"],
                    slug=row["slug"],
                    article_type=row["article_type"] or "",
                    source_focus=(row["source_focus"] or "").replace("|", "\\|"),
                )
            )


def write_csv(rows: list[sqlite3.Row], output_path: Path) -> None:
    """Write the roadmap as a CSV file alongside the Markdown export."""
    csv_path = output_path.with_suffix(".csv")

    with csv_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "priority",
                "status",
                "regime_name",
                "title",
                "slug",
                "article_type",
                "source_focus",
                "notes",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(dict(row))


def main() -> None:
    parser = argparse.ArgumentParser(description="Export the International Law article roadmap.")
    parser.add_argument("--db", required=True, help="Path to SQLite database.")
    parser.add_argument("--output", default="outputs/article-roadmap.md", help="Markdown output path.")
    args = parser.parse_args()

    db_path = Path(args.db)
    output_path = Path(args.output)

    rows = fetch_roadmap(db_path)
    write_markdown(rows, output_path)
    write_csv(rows, output_path)

    print(f"Exported {len(rows)} roadmap records to {output_path} and {output_path.with_suffix('.csv')}")


if __name__ == "__main__":
    main()

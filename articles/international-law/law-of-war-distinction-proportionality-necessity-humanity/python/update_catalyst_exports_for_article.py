#!/usr/bin/env python3
"""Add lightweight Catalyst Data export rows for this article."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ARTICLE_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = ARTICLE_DIR.parents[2]
EXPORT_DIR = REPO_ROOT / "catalyst_data_exports"
SLUG = "law-of-war-distinction-proportionality-necessity-humanity"
TITLE = "The Law of War: Distinction, Proportionality, Necessity, and Humanity"
ARTICLE_PATH = f"articles/international-law/{SLUG}"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    existing_fields: list[str] = []
    if path.exists():
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.reader(handle)
            try:
                existing_fields = next(reader)
            except StopIteration:
                existing_fields = []
    combined = list(dict.fromkeys(existing_fields + fieldnames))
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=combined)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in combined})


def upsert_by_article(path: Path, fieldnames: list[str], new_rows: list[dict[str, str]]) -> None:
    old_rows = [row for row in read_csv(path) if row.get("article_slug") != SLUG]
    write_csv(path, fieldnames, old_rows + new_rows)


def main() -> None:
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    primary = read_csv(ARTICLE_DIR / "data" / "primary_sources.csv")
    secondary = read_csv(ARTICLE_DIR / "data" / "secondary_sources.csv")
    metadata = json.loads((ARTICLE_DIR / "metadata.json").read_text(encoding="utf-8"))

    upsert_by_article(
        EXPORT_DIR / "article_repository_map.csv",
        ["article_slug", "article_title", "article_path", "wordpress_slug", "series", "status"],
        [{
            "article_slug": SLUG,
            "article_title": TITLE,
            "article_path": ARTICLE_PATH,
            "wordpress_slug": metadata.get("wordpress_slug", SLUG),
            "series": "International Law",
            "status": metadata.get("status", "published-ready"),
        }],
    )

    all_sources = []
    for row in primary:
        all_sources.append({
            "article_slug": SLUG,
            "source_id": row.get("source_id", ""),
            "source_title": row.get("source_title", ""),
            "source_type": row.get("source_type", "primary"),
            "institution": row.get("institution", ""),
            "author": "",
            "year": row.get("year", ""),
            "publisher": "",
            "url": row.get("url", ""),
            "notes": row.get("notes", ""),
        })
    for row in secondary:
        all_sources.append({
            "article_slug": SLUG,
            "source_id": row.get("source_id", ""),
            "source_title": row.get("title", ""),
            "source_type": "secondary",
            "institution": "",
            "author": row.get("author", ""),
            "year": row.get("year", ""),
            "publisher": row.get("publisher", ""),
            "url": row.get("url", ""),
            "notes": row.get("notes", ""),
        })
    source_fields = ["article_slug", "source_id", "source_title", "source_type", "institution", "author", "year", "publisher", "url", "notes"]
    upsert_by_article(EXPORT_DIR / "all_article_sources.csv", source_fields, all_sources)
    upsert_by_article(EXPORT_DIR / "sources.csv", source_fields, all_sources)

    instruments = [{
        "article_slug": SLUG,
        "instrument_id": row.get("source_id", ""),
        "title": row.get("source_title", ""),
        "instrument_type": row.get("source_type", ""),
        "institution": row.get("institution", ""),
        "year": row.get("year", ""),
        "url": row.get("url", ""),
        "notes": row.get("notes", ""),
    } for row in primary]
    upsert_by_article(EXPORT_DIR / "legal_instruments.csv", ["article_slug", "instrument_id", "title", "instrument_type", "institution", "year", "url", "notes"], instruments)

    tags = [{"article_slug": SLUG, "tag": tag} for tag in metadata.get("tags", [])]
    upsert_by_article(EXPORT_DIR / "tags.csv", ["article_slug", "tag"], tags)

    topics = []
    for row in primary:
        sid = row.get("source_id", "")
        if sid:
            topics.append({"article_slug": SLUG, "instrument_id": sid, "topic": "law of war"})
            topics.append({"article_slug": SLUG, "instrument_id": sid, "topic": "international humanitarian law"})
    upsert_by_article(EXPORT_DIR / "instrument_topics.csv", ["article_slug", "instrument_id", "topic"], topics)

    summary_path = EXPORT_DIR / "summary.json"
    summary = {}
    if summary_path.exists():
        try:
            summary = json.loads(summary_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            summary = {}
    summary.setdefault("updated_articles", {})[SLUG] = {
        "title": TITLE,
        "article_path": ARTICLE_PATH,
        "sources": len(all_sources),
        "updated": metadata.get("updated", "2026-06-24"),
    }
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Updated Catalyst Data exports in {EXPORT_DIR}")


if __name__ == "__main__":
    main()

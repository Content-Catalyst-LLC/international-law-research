#!/usr/bin/env python3
"""Upsert the International Organizations article into Catalyst Data exports."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTICLE_SLUG = "international-organizations-legal-authority-global-institutions"
ARTICLE_DIR = ROOT / "articles" / "international-law" / ARTICLE_SLUG
EXPORT = ROOT / "catalyst_data_exports"
EXPORT.mkdir(exist_ok=True)


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def upsert(path: Path, key_fields: list[str], row: dict, default_headers: list[str]) -> None:
    rows = read_csv(path)
    headers = list(rows[0].keys()) if rows else list(default_headers)
    for key in row.keys():
        if key not in headers:
            headers.append(key)
    def same(existing: dict) -> bool:
        return all((existing.get(k) or "") == (row.get(k) or "") for k in key_fields)
    new_rows = [r for r in rows if not same(r)]
    normalized = {h: row.get(h, "") for h in headers}
    new_rows.append(normalized)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for r in new_rows:
            writer.writerow({h: r.get(h, "") for h in headers})


def main() -> int:
    meta = json.loads((ARTICLE_DIR / "metadata.json").read_text(encoding="utf-8"))
    today = meta.get("updated_at", "")
    repo_path = meta.get("repo_path", f"articles/international-law/{ARTICLE_SLUG}")
    url = meta.get("wordpress_url", f"https://sustainablecatalyst.com/{ARTICLE_SLUG}/")

    upsert(
        EXPORT / "article_repository_map.csv",
        ["article_slug"],
        {
            "article_slug": ARTICLE_SLUG,
            "article_title": meta.get("article_title", ""),
            "article_url": url,
            "repo_path": repo_path,
            "series": meta.get("series", "International Law"),
            "category": meta.get("category", "Global Governance"),
            "status": meta.get("status", "generated_deep_dive"),
            "focus_keyword": meta.get("focus_keyword", ""),
            "updated_at": today,
        },
        ["article_slug", "article_title", "article_url", "repo_path", "series", "category", "status", "focus_keyword", "updated_at"],
    )

    primary = read_csv(ARTICLE_DIR / "data" / "primary_sources.csv")
    secondary = read_csv(ARTICLE_DIR / "data" / "secondary_sources.csv")

    for src in primary:
        source_id = src.get("source_id", "")
        title = src.get("source_title", "")
        source_type = src.get("source_type", "primary_source")
        row = {
            "source_id": source_id,
            "source_title": title,
            "source_type": source_type,
            "institution": src.get("institution", ""),
            "year": src.get("year", ""),
            "url": src.get("url", ""),
            "notes": src.get("notes", ""),
            "article_slug": ARTICLE_SLUG,
            "article_title": meta.get("article_title", ""),
            "repo_path": repo_path,
        }
        upsert(EXPORT / "sources.csv", ["source_id"], row, ["source_id", "source_title", "source_type", "institution", "year", "url", "notes", "article_slug", "article_title", "repo_path"])
        upsert(
            EXPORT / "legal_instruments.csv",
            ["instrument_id"],
            {
                "instrument_id": source_id,
                "title": title,
                "instrument_type": source_type,
                "institution": src.get("institution", ""),
                "year": src.get("year", ""),
                "url": src.get("url", ""),
                "article_slug": ARTICLE_SLUG,
                "topic": "international organizations; legal authority; global institutions",
                "notes": src.get("notes", ""),
            },
            ["instrument_id", "title", "instrument_type", "institution", "year", "url", "article_slug", "topic", "notes"],
        )
        upsert(
            EXPORT / "instrument_topics.csv",
            ["instrument_id", "topic"],
            {"instrument_id": source_id, "topic": "international organizations", "article_slug": ARTICLE_SLUG, "article_title": meta.get("article_title", "")},
            ["instrument_id", "topic", "article_slug", "article_title"],
        )

    for src in secondary:
        source_id = src.get("source_id", "")
        row = {
            "source_id": source_id,
            "source_title": src.get("title", ""),
            "source_type": "secondary_source",
            "institution": src.get("publisher", ""),
            "year": src.get("year", ""),
            "url": src.get("url", ""),
            "notes": src.get("notes", ""),
            "author": src.get("author", ""),
            "article_slug": ARTICLE_SLUG,
            "article_title": meta.get("article_title", ""),
            "repo_path": repo_path,
        }
        upsert(EXPORT / "sources.csv", ["source_id"], row, ["source_id", "source_title", "source_type", "institution", "year", "url", "notes", "author", "article_slug", "article_title", "repo_path"])

    for tag in meta.get("tags", []):
        tag_slug = str(tag).lower().replace("&", "and").replace(" ", "-").replace(",", "")
        upsert(
            EXPORT / "tags.csv",
            ["tag_slug"],
            {"tag_slug": tag_slug, "tag_name": tag, "tag_type": "article_tag", "article_slug": ARTICLE_SLUG},
            ["tag_slug", "tag_name", "tag_type", "article_slug"],
        )

    all_rows = []
    for src in primary:
        all_rows.append({
            "article_slug": ARTICLE_SLUG,
            "article_title": meta.get("article_title", ""),
            "source_id": src.get("source_id", ""),
            "source_title": src.get("source_title", ""),
            "source_type": src.get("source_type", ""),
            "institution_or_author": src.get("institution", ""),
            "year": src.get("year", ""),
            "url": src.get("url", ""),
            "repo_path": repo_path,
        })
    for src in secondary:
        all_rows.append({
            "article_slug": ARTICLE_SLUG,
            "article_title": meta.get("article_title", ""),
            "source_id": src.get("source_id", ""),
            "source_title": src.get("title", ""),
            "source_type": "secondary_source",
            "institution_or_author": src.get("author", ""),
            "year": src.get("year", ""),
            "url": src.get("url", ""),
            "repo_path": repo_path,
        })
    all_path = EXPORT / "all_article_sources.csv"
    existing = read_csv(all_path)
    existing = [r for r in existing if r.get("article_slug") != ARTICLE_SLUG]
    headers = ["article_slug", "article_title", "source_id", "source_title", "source_type", "institution_or_author", "year", "url", "repo_path"]
    with all_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for r in existing + all_rows:
            writer.writerow({h: r.get(h, "") for h in headers})

    upsert(
        EXPORT / "compatibility_audit.csv",
        ["article_slug"],
        {
            "article_slug": ARTICLE_SLUG,
            "article_title": meta.get("article_title", ""),
            "status": "catalyst_data_ready",
            "primary_sources_csv": "standard",
            "secondary_sources_csv": "standard",
            "metadata_json": "present",
            "article_html": "present",
            "updated_at": today,
            "notes": "Added International Organizations article folder and upserted Catalyst Data export rows.",
        },
        ["article_slug", "article_title", "status", "primary_sources_csv", "secondary_sources_csv", "metadata_json", "article_html", "updated_at", "notes"],
    )

    print(f"Updated Catalyst Data exports for {ARTICLE_SLUG}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

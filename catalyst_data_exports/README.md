# Catalyst Data Exports: International Law

Generated: 2026-06-23T22:27:19.418263+00:00

This directory makes the `international-law-research` repository easier to ingest into the Catalyst Data schema.

## Files

- `article_repository_map.csv` — article IDs, titles, statuses, WordPress slugs, repository paths, and GitHub URLs.
- `sources.csv` — normalized provenance/source rows for Catalyst Data's `sources` table.
- `legal_instruments.csv` — normalized primary legal-authority rows for Catalyst Data's `legal_instruments` table.
- `tags.csv` — topic tags for International Law, article domains, article titles, and source types.
- `instrument_topics.csv` — join data for `legal_instruments` ↔ `tags`.
- `all_article_sources.csv` — article-level primary and secondary source registry.
- `article_sources/` — one article-source export file per article folder.
- `compatibility_audit.csv` — article-folder readiness audit.
- `import_catalyst_data.py` — optional SQLite loader after Catalyst Data `schema.sql` has been applied.
- `import_catalyst_data.sql` — table-mapping notes for SQL import workflows.

## Normalized article CSV headers

Primary sources:

```csv
source_id,source_title,source_type,institution,year,url,notes
```

Secondary sources:

```csv
source_id,author,year,title,publisher,url,notes
```

## Loader usage

From a checkout that also has a Catalyst Data SQLite database initialized with `schema.sql`:

```bash
python3 catalyst_data_exports/import_catalyst_data.py /path/to/catalyst.db
```


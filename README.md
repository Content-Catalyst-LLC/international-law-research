# International Law Research

A companion legal research infrastructure repository for the International Law knowledge series.

This repository supports structured article planning, treaty metadata, international institution records, court and tribunal metadata, case-law and advisory-opinion tracking, citation workflows, source hierarchy documentation, and SQL-backed legal-regime mapping.

It is intentionally designed for legal scholarship rather than computational science. SQL is the backbone. CSV files provide maintainable reference data. Python is used only for lightweight exports, audits, and article-roadmap maintenance.

## Repository Structure

- articles/international-law/ — Article planning notes and pillar support
- data/ — CSV source data for regimes, treaties, institutions, cases, and planned articles
- docs/ — Methodology, source hierarchy, citation style, article templates, and licensing notes
- sql/ — Schema, seed data, and research views
- python/ — Lightweight export and audit utilities
- notebooks/ — Optional exploratory notebooks
- outputs/ — Generated roadmap and audit outputs

## Intended Uses

- Maintain a structured article roadmap for the International Law pillar.
- Track treaties, institutions, courts, tribunals, cases, advisory opinions, and legal regimes.
- Preserve a source hierarchy for official legal materials, court records, institutional documents, and scholarly sources.
- Support SQL-based mapping across legal regimes, institutions, treaties, cases, and planned articles.
- Export article-roadmap tables for editorial planning.
- Audit citation metadata for missing source URLs, weak source types, and incomplete records.

## Legal Materials Policy

Official treaties, judgments, advisory opinions, UN documents, institutional records, and legal materials should generally be linked to authoritative sources rather than republished in full. This repository stores metadata, citations, notes, and research structure.

## Quick Start with SQLite

Create a local SQLite database:

sqlite3 international_law.db < sql/schema.sql
sqlite3 international_law.db < sql/seed_international_law.sql
sqlite3 international_law.db < sql/views.sql

Export the article roadmap:

python3 python/export_article_roadmap.py --db international_law.db --output outputs/article-roadmap.md

Run a citation audit:

python3 python/citation_audit.py --data-dir data --output outputs/citation-audit.md

## License

Code, SQL, and repository infrastructure are released under the MIT License. Original documentation and metadata are covered by the content license described in CONTENT_LICENSE.md. Official legal materials remain the property of their respective institutions and should be cited and linked from authoritative sources.

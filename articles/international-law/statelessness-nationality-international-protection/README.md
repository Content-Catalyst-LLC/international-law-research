# Statelessness, Nationality, and International Protection

This folder supports the WordPress article **Statelessness, Nationality, and International Protection** in the Sustainable Catalyst International Law series.

## Contents

- `docs/wordpress_article_html.html` — full WordPress-ready article HTML.
- `metadata.json` — publication metadata, slug, tags, and series navigation.
- `data/primary_authorities.csv` — core treaties, UN materials, and institutional sources.
- `data/further_reading.csv` — selected scholarly and institutional reading list.
- `data/statelessness_framework_matrix.csv` — key concepts, obligations, and legal questions.
- `data/protection_pathways_matrix.csv` — practical pathways for protection and case assessment.
- `sql/statelessness_schema.sql` — lightweight schema for storing article source and matrix data.
- `python/build_statelessness_outputs.py` — generates JSON summaries from CSV data.
- `python/audit_links.py` — inventories URLs in the article HTML and data files.
- `outputs/` — generated JSON/link inventory artifacts.

## Repository role

The folder is designed to make the article’s research workflow auditable without crowding the public article with technical infrastructure.

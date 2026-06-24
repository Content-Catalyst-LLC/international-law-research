# International Arbitration and the Peaceful Settlement of Disputes

This folder supports the Sustainable Catalyst article **International Arbitration and the Peaceful Settlement of Disputes**.

## Article context

The article explains international arbitration as part of the peaceful settlement of international disputes. It connects Article 33 of the UN Charter, state-to-state arbitration, the Permanent Court of Arbitration, UNCLOS Annex VII arbitration, mixed claims, commercial arbitration, the New York Convention, ICSID, UNCITRAL, investor-state arbitration, enforcement, transparency, and legitimacy critique.

## Folder structure

- `metadata.json` — article metadata and series placement.
- `docs/wordpress_article_html.html` — copy-ready WordPress HTML.
- `data/primary_sources.csv` — primary legal authorities and institutional materials.
- `data/secondary_sources.csv` — selected books, articles, and reference materials.
- `data/arbitration_institution_matrix.csv` — institution and forum comparison.
- `data/dispute_settlement_matrix.csv` — doctrinal comparison of peaceful-settlement mechanisms.
- `data/enforcement_framework_matrix.csv` — award/enforcement framework comparison.
- `python/audit_links.py` — lightweight link audit helper.
- `python/build_arbitration_matrices.py` — CSV-to-JSON matrix builder.
- `sql/queries.sql` — example queries for the local source data.
- `outputs/article_summary.json` — article summary metadata for downstream export.

## Repository and Catalyst Data notes

This article is designed to remain compatible with the repository's Catalyst Data export layer. Source CSVs use stable identifiers and normalized columns so they can be merged into repo-level exports.

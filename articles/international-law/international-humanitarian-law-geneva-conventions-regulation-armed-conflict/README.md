# International Humanitarian Law: The Geneva Conventions and the Regulation of Armed Conflict

This folder supports the Sustainable Catalyst article **International Humanitarian Law: The Geneva Conventions and the Regulation of Armed Conflict**.

The materials organize primary authorities, secondary readings, conflict-classification concepts, protected-person categories, war-crimes references, and article workflow notes for the International Law series.

## Folder structure

- `docs/wordpress_article_html.html` — copy-ready WordPress HTML article.
- `data/primary_sources.csv` — treaties, official institutional materials, ICJ decisions, and ICRC resources.
- `data/secondary_sources.csv` — scholarly and practitioner references.
- `data/ihl_framework_matrix.csv` — core doctrine and institutional logic.
- `data/conflict_classification_matrix.csv` — IAC, NIAC, occupation, and mixed/conflict-classification issues.
- `data/protected_persons_matrix.csv` — protected categories under IHL.
- `data/war_crimes_matrix.csv` — war-crimes and accountability reference matrix.
- `python/build_ihl_matrices.py` — exports structured JSON matrices.
- `python/audit_links.py` — lightweight URL extraction/audit helper.
- `sql/queries.sql` — starter SQL queries for Catalyst Data integration.
- `outputs/` — generated summaries and matrices.

## GitHub / Catalyst Data compatibility

The CSV files use the standard article-source columns used across the International Law repository. They are intended to be compatible with the repo-level Catalyst Data export workflow.

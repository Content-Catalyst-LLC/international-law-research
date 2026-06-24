# Women’s Rights, Gender Equality, and International Legal Protection

This folder supports the Sustainable Catalyst article **Women’s Rights, Gender Equality, and International Legal Protection**.

## Contents

- `docs/wordpress_article_html.html` — WordPress-ready article HTML.
- `metadata.json` — article title, slug, excerpt, tags, and series navigation metadata.
- `data/primary_authorities.csv` — treaty, institutional, and legal authorities.
- `data/further_reading.csv` — Harvard-style scholarly and institutional reading list.
- `data/gender_equality_framework_matrix.csv` — equality doctrines, legal functions, and practice questions.
- `data/protection_mechanisms_matrix.csv` — CEDAW, regional, labor, conflict, and accountability mechanisms.
- `python/build_womens_rights_matrices.py` — generates JSON output from the CSV matrices.
- `python/link_inventory.py` — extracts links from the WordPress HTML for review.
- `sql/womens_rights_schema.sql` — lightweight relational schema for the article data.
- `outputs/` — generated matrices and link inventory.

## Research purpose

The folder makes the article's legal-source architecture, treaty references, institutional mechanisms, and analytical matrices auditable outside the WordPress article.

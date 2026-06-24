# The International Court of Justice and the Judicial Settlement of Disputes

This folder supports the Sustainable Catalyst article **The International Court of Justice and the Judicial Settlement of Disputes** in the International Law series.

The article examines the International Court of Justice as the principal judicial organ of the United Nations and as the central forum for the judicial settlement of inter-state disputes and advisory legal questions. It is designed for readers who need both doctrinal explanation and a practical lawyer-facing workflow for analyzing ICJ jurisdiction, procedure, remedies, advisory opinions, compliance, and institutional limits.

## Repository contents

- `metadata.json` — article metadata, SEO fields, navigation, tags, and Catalyst Data status.
- `data/primary_sources.csv` — Charter, Statute, Rules, ICJ institutional pages, and leading cases/advisory opinions.
- `data/secondary_sources.csv` — books, commentaries, and scholarly references.
- `data/case_matrix.csv` — structured ICJ case and advisory-opinion examples.
- `data/icj_jurisdiction_matrix.csv` — jurisdiction pathways and procedural concepts.
- `data/catalyst_mapping.csv` — mapping from article sources to Catalyst Data tables.
- `docs/doctrine_summary.md` — doctrinal overview for editorial and research reuse.
- `docs/source_notes.md` — source-use notes for the article.
- `docs/editorial_notes.md` — editorial positioning and update notes.
- `docs/wordpress_article_html.html` — copy-ready WordPress HTML article generated for publication.
- `python/audit_links.py` — offline/live URL audit helper.
- `python/build_case_matrix.py` — converts the case matrix into a JSON output.
- `sql/queries.sql` — starter SQL queries for this article’s research data.
- `outputs/article_summary.json` — compact structured article summary.

## Catalyst Data compatibility

This folder uses normalized CSV headers so the source material can be exported into the broader Catalyst Data schema. The update script also refreshes repo-level files under `catalyst_data_exports/` so this article is visible in article maps, source exports, legal-instrument exports, and topic tags.

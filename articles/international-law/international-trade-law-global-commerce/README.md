# International Trade Law and the Legal Order of Global Commerce

This folder supports the Sustainable Catalyst article **International Trade Law and the Legal Order of Global Commerce**.

The public article HTML is intentionally **not** stored in GitHub. WordPress is the publication layer. This repository keeps the article's structured research support materials: metadata, authorities, further reading, doctrinal matrices, implementation notes, lightweight data outputs, and reproducible support scripts.

## Article scope

The article examines the legal order of global commerce through WTO law, trade treaties, market access rules, trade remedies, services, intellectual property, sanitary and technical regulation, dispute settlement, development, environmental regulation, national security, industrial policy, digital trade, and the tension between liberalization and regulatory autonomy.

## Folder contents

- `metadata/article_metadata.json` — article metadata and navigation context.
- `sources/primary_authorities.md` — core treaties, institutional materials, and WTO sources.
- `sources/further_reading.md` — scholarship and research materials.
- `data/*.csv` — structured matrices for trade-law architecture, WTO agreements, dispute settlement, and regulatory autonomy.
- `sql/trade_law_schema.sql` — small schema for loading the support matrices.
- `python/build_trade_law_outputs.py` — helper that generates lightweight JSON outputs from the CSV files.
- `outputs/` — generated support outputs.
- `notes/editorial_notes.md` — editorial positioning and workflow notes.

## Editorial rule

Do not add `docs/wordpress_article_html.html` or other full article HTML copies to this folder. The HTML belongs in WordPress only.

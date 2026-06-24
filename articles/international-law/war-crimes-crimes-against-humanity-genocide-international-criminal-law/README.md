# War Crimes, Crimes Against Humanity, Genocide, and the Architecture of International Criminal Law

This folder contains the WordPress-ready article HTML, metadata, source tables, analytical matrices, SQL schema, Python utilities, and generated outputs for the International Law series article on the architecture of international criminal law.

## Article folder

`articles/international-law/war-crimes-crimes-against-humanity-genocide-international-criminal-law`

## WordPress HTML

`docs/wordpress_article_html.html`

## Scope

The article covers war crimes, crimes against humanity, genocide, aggression, contextual elements, mens rea, modes of liability, command responsibility, complementarity, evidence, selectivity, victims, reparations, and enforcement limits.

## Generated outputs

Run:

```bash
python3 python/build_icl_matrices.py
python3 python/audit_links.py docs/wordpress_article_html.html
```

The scripts generate JSON summaries and link-audit output in `outputs/`.

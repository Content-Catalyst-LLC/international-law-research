#!/usr/bin/env python3
from __future__ import annotations
import csv, json, sys
from pathlib import Path
repo = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
article_id = "humanitarian-intervention-responsibility-to-protect-limits-sovereignty"
article_title = "Humanitarian Intervention, Responsibility to Protect, and the Limits of Sovereignty"
article_folder = f"articles/international-law/{article_id}"
article = repo / article_folder
exports = repo / "catalyst_data_exports"
exports.mkdir(exist_ok=True)
metadata = json.loads((article / "metadata.json").read_text(encoding="utf-8"))
def read_rows(path):
    with path.open(newline="", encoding="utf-8") as f: return list(csv.DictReader(f))
def upsert_csv(path: Path, fieldnames: list[str], key_fields: list[str], rows: list[dict]):
    existing = []
    if path.exists() and path.stat().st_size:
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f); old = reader.fieldnames or []
            for field in old:
                if field not in fieldnames: fieldnames.append(field)
            existing = list(reader)
    def key(row): return tuple(row.get(k, "") for k in key_fields)
    incoming = {key(r): r for r in rows}; merged=[]; used=set()
    for row in existing:
        k=key(row)
        if k in incoming:
            new=dict(row); new.update({fn: incoming[k].get(fn, "") for fn in fieldnames}); merged.append(new); used.add(k)
        else: merged.append(row)
    for k,row in incoming.items():
        if k not in used: merged.append(row)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames); writer.writeheader()
        for row in merged: writer.writerow({fn: row.get(fn, "") for fn in fieldnames})
primary = read_rows(article / "data" / "primary_sources.csv")
secondary = read_rows(article / "data" / "secondary_sources.csv")
upsert_csv(exports / "article_repository_map.csv", ["article_id","title","slug","article_folder","series","topic","status","wordpress_slug"], ["article_id"], [{"article_id": article_id, "title": article_title, "slug": metadata.get("slug", article_id), "article_folder": article_folder, "series": metadata.get("series", "International Law"), "topic": "Use of Force / Humanitarian Protection", "status": metadata.get("status", "published-draft-ready"), "wordpress_slug": metadata.get("slug", article_id)}])
source_rows=[]
for row in primary:
    source_rows.append({"source_id": row.get("source_id",""), "article_id": article_id, "title": row.get("source_title",""), "source_title": row.get("source_title",""), "source_type": row.get("source_type",""), "institution": row.get("institution",""), "year": row.get("year",""), "url": row.get("url",""), "notes": row.get("notes","")})
for row in secondary:
    source_rows.append({"source_id": row.get("source_id",""), "article_id": article_id, "title": row.get("title",""), "source_title": row.get("title",""), "source_type": "secondary", "institution": row.get("publisher",""), "year": row.get("year",""), "url": row.get("url",""), "notes": row.get("notes","")})
fields=["source_id","article_id","title","source_title","source_type","institution","year","url","notes"]
upsert_csv(exports / "sources.csv", fields.copy(), ["source_id","article_id"], source_rows)
upsert_csv(exports / "all_article_sources.csv", fields.copy(), ["source_id","article_id"], source_rows)
legal=[]
for row in primary:
    legal.append({"instrument_id": row.get("source_id",""), "article_id": article_id, "title": row.get("source_title",""), "instrument_type": row.get("source_type",""), "institution": row.get("institution",""), "year": row.get("year",""), "url": row.get("url",""), "notes": row.get("notes","")})
upsert_csv(exports / "legal_instruments.csv", ["instrument_id","article_id","title","instrument_type","institution","year","url","notes"], ["instrument_id","article_id"], legal)
upsert_csv(exports / "tags.csv", ["article_id","tag"], ["article_id","tag"], [{"article_id": article_id, "tag": tag} for tag in metadata.get("tags", [])])
upsert_csv(exports / "instrument_topics.csv", ["article_id","topic"], ["article_id","topic"], [{"article_id": article_id, "topic": topic} for topic in ["Use of Force", "Humanitarian Intervention", "Responsibility to Protect", "Collective Security"]])
(exports / f"{article_id}_export_summary.json").write_text(json.dumps({"article_id": article_id, "title": article_title, "primary_sources": len(primary), "secondary_sources": len(secondary)}, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Updated Catalyst Data exports for {article_id}")

#!/usr/bin/env python3
"""Load International Law research exports into a Catalyst Data SQLite database.

Usage:
  python3 catalyst_data_exports/import_catalyst_data.py /path/to/catalyst.db

Before running, initialize the database with catalyst-data/schema.sql.
"""
from __future__ import annotations

import csv
import sqlite3
import sys
from pathlib import Path

EXPORT_ROOT = Path(__file__).resolve().parents[0]


def rows(name: str):
    with (EXPORT_ROOT / name).open(newline='', encoding='utf-8-sig') as f:
        yield from csv.DictReader(f)


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit('Usage: import_catalyst_data.py /path/to/catalyst.db')
    db = Path(sys.argv[1])
    con = sqlite3.connect(db)
    con.execute('PRAGMA foreign_keys = ON')

    for r in rows('sources.csv'):
        con.execute(
            'INSERT OR IGNORE INTO sources (name, url, license, retrieved_at, note) VALUES (?, ?, ?, ?, ?)',
            (r['name'], r['url'] or None, r['license'] or None, r['retrieved_at'] or None, r['note'] or None),
        )

    # Ensure tags.
    for r in rows('tags.csv'):
        con.execute(
            'INSERT OR IGNORE INTO tags (kind, name) VALUES (?, ?)',
            (r['kind'], r['name']),
        )

    # Import legal instruments and map their instrument_id to SQLite IDs.
    instrument_pk = {}
    for r in rows('legal_instruments.csv'):
        source_id = None
        if r.get('source_name'):
            cur = con.execute('SELECT id FROM sources WHERE name = ? LIMIT 1', (r['source_name'],))
            got = cur.fetchone()
            source_id = got[0] if got else None
        con.execute(
            'INSERT OR IGNORE INTO legal_instruments (instrument_type, title, short_citation, adopted_on, url, source_id) VALUES (?, ?, ?, ?, ?, ?)',
            (r['instrument_type'], r['title'], r['short_citation'] or None, r['adopted_on'] or None, r['url'] or None, source_id),
        )
        cur = con.execute('SELECT id FROM legal_instruments WHERE title = ? AND COALESCE(url, "") = COALESCE(?, "") LIMIT 1', (r['title'], r['url'] or None))
        got = cur.fetchone()
        if got:
            instrument_pk[r['instrument_id']] = got[0]

    for r in rows('instrument_topics.csv'):
        instrument_id = instrument_pk.get(r['instrument_id'])
        if not instrument_id:
            continue
        cur = con.execute('SELECT id FROM tags WHERE kind = ? AND name = ? LIMIT 1', ('topic', r['tag_name']))
        got = cur.fetchone()
        if not got:
            continue
        con.execute(
            'INSERT OR IGNORE INTO instrument_topics (instrument_id, tag_id) VALUES (?, ?)',
            (instrument_id, got[0]),
        )

    con.commit()
    con.close()
    print(f'Loaded International Law exports into {db}')


if __name__ == '__main__':
    main()

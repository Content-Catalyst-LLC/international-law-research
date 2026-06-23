#!/usr/bin/env python3
"""Export Self-Determination source metadata into Markdown for editorial review."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'outputs' / 'source_export.md'

def read_csv(path):
    if not path.exists():
        return []
    with path.open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

primary = read_csv(ROOT / 'data' / 'primary_sources.csv')
secondary = read_csv(ROOT / 'data' / 'secondary_sources.csv')
concepts = read_csv(ROOT / 'data' / 'concepts.csv')

lines = ['# Self-Determination Source Export', '']
lines.append('## Primary Sources')
for row in primary:
    title = row.get('source_title') or row.get('title')
    inst = row.get('institution', '')
    year = row.get('year', '')
    url = row.get('url', '')
    lines.append(f'- {inst} ({year}) *{title}*. {url}')
lines.append('')
lines.append('## Secondary Sources')
for row in secondary:
    author = row.get('author', '')
    year = row.get('year', '')
    title = row.get('title', '')
    publisher = row.get('publisher', '')
    url = row.get('url', '')
    lines.append(f'- {author} ({year}) *{title}*. {publisher}. {url}')
lines.append('')
lines.append('## Concepts')
for row in concepts:
    lines.append(f"- **{row.get('concept','')}** — {row.get('description','')}")
OUTPUT.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(OUTPUT)

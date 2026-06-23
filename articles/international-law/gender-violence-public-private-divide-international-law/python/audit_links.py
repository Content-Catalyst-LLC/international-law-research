#!/usr/bin/env python3
"""Basic structural URL audit for Gender, Violence, and the Public/Private Divide in International Law source metadata."""
from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[1]
FILES = [ROOT / 'data' / 'primary_sources.csv', ROOT / 'data' / 'secondary_sources.csv']

def main() -> int:
    problems = []
    for path in FILES:
        if not path.exists():
            problems.append(f'Missing file: {path}')
            continue
        with path.open(newline='', encoding='utf-8') as f:
            for i, row in enumerate(csv.DictReader(f), start=2):
                url = row.get('url', '')
                if not (url.startswith('https://') or url.startswith('http://')):
                    problems.append(f'{path}:{i} invalid URL: {url}')
    if problems:
        print('
'.join(problems))
        return 1
    print('Gender, Violence, and the Public/Private Divide in International Law source URLs look structurally valid.')
    return 0

if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""Validate Self-Determination metadata."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
metadata = json.loads((ROOT / 'metadata.json').read_text(encoding='utf-8'))
required = ['slug', 'folder_slug', 'title', 'status', 'series', 'canonical_url', 'repository_path']
missing = [field for field in required if not metadata.get(field)]
if missing:
    raise SystemExit('Missing metadata fields: ' + ', '.join(missing))
if not metadata['canonical_url'].startswith('https://'):
    raise SystemExit('canonical_url must be https')
print('metadata ok')

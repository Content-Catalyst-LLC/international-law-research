#!/usr/bin/env python3
import json
from pathlib import Path
p = Path(__file__).resolve().parents[1] / 'metadata.json'
data = json.loads(p.read_text())
required = ['slug','folder_slug','title','status','repository_path']
missing = [k for k in required if not data.get(k)]
if missing:
    raise SystemExit('Missing metadata fields: ' + ', '.join(missing))
print('metadata ok')

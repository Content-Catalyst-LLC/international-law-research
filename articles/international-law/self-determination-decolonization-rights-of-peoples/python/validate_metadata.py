#!/usr/bin/env python3
from pathlib import Path
import json

base = Path(__file__).resolve().parents[1]
data = json.loads((base / "metadata.json").read_text(encoding="utf-8"))
required = {"slug", "folder_slug", "title", "status", "domain", "series", "canonical_url", "repository_path"}
missing = required - set(data)
if missing:
    raise SystemExit("Missing metadata fields: " + ", ".join(sorted(missing)))
print(f"Metadata OK: {data['title']}")

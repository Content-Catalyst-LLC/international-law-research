#!/usr/bin/env python3
"""Validate required metadata fields for this article folder."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
required = ["title", "slug", "folder_slug", "status", "repository_path"]
metadata = json.loads((ROOT / "metadata.json").read_text())
missing = [key for key in required if not metadata.get(key)]
if missing:
    raise SystemExit(f"Missing metadata fields: {missing}")
print("metadata OK")

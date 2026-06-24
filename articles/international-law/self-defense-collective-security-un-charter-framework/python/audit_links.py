#!/usr/bin/env python3
"""Local URL inventory for article files; does not make network calls."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

# Deliberately avoids single-quote quoting problems in generated shell payloads.
URL_RE = re.compile(r'https?://[^\s"<>]+')

records = []
for folder in [ROOT / "data", ROOT / "docs"]:
    if not folder.exists():
        continue
    for path in sorted(folder.rglob("*")):
        if path.is_file() and path.suffix.lower() in {".csv", ".md", ".html", ".txt", ".json"}:
            text = path.read_text(encoding="utf-8", errors="ignore")
            urls = sorted(set(URL_RE.findall(text)))
            if urls:
                records.append({"file": str(path.relative_to(ROOT)), "url_count": len(urls), "urls": urls})

out_path = OUT / "link_audit.json"
out_path.write_text(json.dumps(records, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Wrote {out_path}")

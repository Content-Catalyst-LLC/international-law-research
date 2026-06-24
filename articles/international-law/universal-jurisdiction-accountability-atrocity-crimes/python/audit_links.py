#!/usr/bin/env python3
from pathlib import Path
import csv
import json
import re
from urllib.parse import urlparse

BASE = Path(__file__).resolve().parents[1]
OUT = BASE / "outputs"
OUT.mkdir(exist_ok=True)
URL_RE = re.compile("https?://[^\\s\\\"'<>]+")

files = []
for pattern in ["README.md", "metadata.json", "docs/*.html", "docs/*.md", "data/*.csv"]:
    files.extend(BASE.glob(pattern))

rows = []
seen = set()
for path in files:
    text = path.read_text(encoding="utf-8", errors="ignore")
    for match in URL_RE.findall(text):
        url = match.rstrip(".,);]")
        if url in seen:
            continue
        seen.add(url)
        parsed = urlparse(url)
        rows.append({
            "url": url,
            "domain": parsed.netloc,
            "source_file": str(path.relative_to(BASE)),
            "status": "found"
        })

with (OUT / "link_audit.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=["url", "domain", "source_file", "status"])
    writer.writeheader()
    writer.writerows(rows)

(OUT / "link_audit.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Audited {len(rows)} unique URLs")

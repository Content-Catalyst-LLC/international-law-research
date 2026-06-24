from __future__ import annotations

import json
import pathlib
import re

ARTICLE_ROOT = pathlib.Path(__file__).resolve().parents[1]
OUTPUT_DIR = ARTICLE_ROOT / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Triple-quoted raw string avoids shell/Python quote collisions when generated from Bash.
URL_RE = re.compile(r'''https?://[^\s"'<>]+''')

SCAN_SUFFIXES = {".html", ".htm", ".md", ".json", ".csv", ".sql", ".txt"}
SKIP_PARTS = {".git", "outputs", "__pycache__"}

records = []
for path in sorted(ARTICLE_ROOT.rglob("*")):
    if not path.is_file():
        continue
    if path.suffix.lower() not in SCAN_SUFFIXES:
        continue
    if any(part in SKIP_PARTS for part in path.parts):
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = path.read_text(encoding="utf-8", errors="ignore")
    for match in URL_RE.finditer(text):
        url = match.group(0).rstrip(".,);]")
        records.append({
            "file": str(path.relative_to(ARTICLE_ROOT)),
            "url": url,
        })

unique = []
seen = set()
for record in records:
    key = (record["file"], record["url"])
    if key in seen:
        continue
    seen.add(key)
    unique.append(record)

summary = {
    "article": ARTICLE_ROOT.name,
    "total_links_found": len(unique),
    "note": "Static URL extraction only; no network requests were made.",
    "links": unique,
}

out_path = OUTPUT_DIR / "link_audit.json"
out_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Wrote {out_path}")

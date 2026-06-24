#!/usr/bin/env python3
from __future__ import annotations
import csv, json, re
from pathlib import Path
from urllib.parse import urlparse
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)
URL_RE = re.compile(r"https?://[^\s<>\"]+")
def iter_files():
    for pattern in ("*.md", "*.html", "*.csv", "*.json", "*.sql"):
        yield from ROOT.rglob(pattern)
def main() -> None:
    seen = []
    for path in iter_files():
        if ".git" in path.parts or "outputs" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in URL_RE.findall(text):
            url = match.rstrip(".,);]")
            parsed = urlparse(url)
            seen.append({"file": str(path.relative_to(ROOT)), "url": url, "domain": parsed.netloc, "scheme": parsed.scheme})
    csv_path = OUT / "link_audit.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["file", "url", "domain", "scheme"])
        writer.writeheader(); writer.writerows(seen)
    (OUT / "link_audit.json").write_text(json.dumps(seen, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {csv_path}")
if __name__ == "__main__":
    main()

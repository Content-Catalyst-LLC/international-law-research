#!/usr/bin/env python3
"""Local link audit helper for the Use of Force article.

This script scans article files for URL-looking strings and writes a JSON report.
It deliberately does not make network requests, so it is safe to run offline and
inside GitHub update scripts.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

# Triple-double-quoted raw string avoids shell/Python quote collisions.
URL_RE = re.compile(r"""https?://[^\s"'<>]+""")
TEXT_EXTENSIONS = {".html", ".md", ".txt", ".csv", ".json", ".sql", ".py"}


def article_root() -> Path:
    return Path(__file__).resolve().parents[1]


def collect_urls(root: Path) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    skip_parts = {".git", "outputs", "__pycache__"}

    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if any(part in skip_parts for part in path.parts):
            continue
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue

        rel = path.relative_to(root).as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = path.read_text(encoding="utf-8", errors="ignore")

        for line_no, line in enumerate(text.splitlines(), start=1):
            for match in URL_RE.finditer(line):
                url = match.group(0).rstrip(".,);]")
                records.append({
                    "file": rel,
                    "line": line_no,
                    "url": url,
                })

    return records


def main() -> None:
    root = article_root()
    output_dir = root / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)

    records = collect_urls(root)
    unique_urls = sorted({item["url"] for item in records})

    report = {
        "article": root.name,
        "audit_type": "local_url_inventory",
        "network_requests_performed": False,
        "total_url_mentions": len(records),
        "unique_url_count": len(unique_urls),
        "unique_urls": unique_urls,
        "records": records,
    }

    out_path = output_dir / "link_audit.json"
    out_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Local URL inventory for the IHL / Geneva Conventions article folder.

This is not a network checker. It extracts URL-like strings from article docs
and writes a JSON inventory so link review can happen without fragile external
requests or quoting-sensitive regexes.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

URL_RE = re.compile(r'''https?://[^\s"'<>]+''')
TEXT_EXTENSIONS = {".html", ".md", ".csv", ".json", ".sql", ".txt"}


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in BASE_DIR.rglob("*"):
        if not path.is_file():
            continue
        if "outputs" in path.parts:
            continue
        if path.suffix.lower() in TEXT_EXTENSIONS:
            files.append(path)
    return sorted(files)


def main() -> None:
    records: list[dict[str, str]] = []
    for path in iter_text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = path.read_text(encoding="utf-8", errors="ignore")
        rel = path.relative_to(BASE_DIR).as_posix()
        for match in sorted(set(URL_RE.findall(text))):
            records.append({"file": rel, "url": match.rstrip(".,);]")})

    out_path = OUTPUT_DIR / "link_inventory.json"
    out_path.write_text(
        json.dumps({"url_count": len(records), "urls": records}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()

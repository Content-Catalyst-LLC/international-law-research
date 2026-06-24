#!/usr/bin/env python3
# Audit HTTP links in this article folder.
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"
URL_RE = re.compile(r"https?://[^\s<>]+")


def main() -> None:
    links: dict[str, list[str]] = {}
    for path in sorted(ROOT.rglob("*")):
        if path.is_file() and path.suffix.lower() in {".html", ".md", ".json", ".csv", ".sql", ".py"}:
            rel = path.relative_to(ROOT).as_posix()
            text = path.read_text(encoding="utf-8", errors="ignore")
            found = sorted(set(URL_RE.findall(text)))
            if found:
                links[rel] = found
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUTS / "link_audit.json"
    out_path.write_text(json.dumps(links, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {out_path.relative_to(ROOT)} with {sum(len(v) for v in links.values())} links")


if __name__ == "__main__":
    main()

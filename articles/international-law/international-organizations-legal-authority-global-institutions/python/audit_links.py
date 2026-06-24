#!/usr/bin/env python3
"""Basic URL inventory/audit helper for the International Organizations article folder.

This script reads primary and secondary source CSV files and writes a URL inventory.
It performs lightweight network checks only when --check is provided.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs"


def iter_sources():
    for filename in ["primary_sources.csv", "secondary_sources.csv"]:
        path = DATA / filename
        if not path.exists():
            continue
        with path.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                url = (row.get("url") or "").strip()
                if url:
                    yield filename, row, url


def check_url(url: str, timeout: int = 10) -> dict:
    request = Request(url, method="HEAD", headers={"User-Agent": "SustainableCatalystLinkAudit/1.0"})
    try:
        with urlopen(request, timeout=timeout) as response:
            return {"ok": True, "status": getattr(response, "status", None), "error": ""}
    except HTTPError as exc:
        return {"ok": False, "status": exc.code, "error": str(exc)}
    except URLError as exc:
        return {"ok": False, "status": None, "error": str(exc.reason)}
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "status": None, "error": repr(exc)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Perform lightweight HEAD requests")
    args = parser.parse_args()

    OUT.mkdir(exist_ok=True)
    rows = []
    for filename, row, url in iter_sources():
        entry = {
            "source_file": filename,
            "source_id": row.get("source_id", ""),
            "title": row.get("source_title") or row.get("title", ""),
            "url": url,
        }
        if args.check:
            entry.update(check_url(url))
        rows.append(entry)

    (OUT / "link_inventory.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {OUT / 'link_inventory.json'} with {len(rows)} URL records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Offline/live URL audit helper for the ICJ article source CSVs.

Default mode is offline: it only checks that URLs are present and syntactically plausible.
Use --live to perform network requests.
"""
from __future__ import annotations
import argparse, csv, urllib.parse, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_FILES = [ROOT / "data" / "primary_sources.csv", ROOT / "data" / "secondary_sources.csv"]

def iter_rows():
    for path in DATA_FILES:
        if not path.exists():
            yield path, None, {"error": "missing file"}
            continue
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                yield path, row.get("source_id") or row.get("id") or row.get("title"), row

def plausible_url(url: str) -> bool:
    parsed = urllib.parse.urlparse(url or "")
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)

def check_live(url: str, timeout: int = 12) -> tuple[bool, str]:
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "CatalystDataLinkAudit/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return 200 <= resp.status < 400, str(resp.status)
    except Exception:
        try:
            req = urllib.request.Request(url, method="GET", headers={"User-Agent": "CatalystDataLinkAudit/1.0"})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return 200 <= resp.status < 400, str(resp.status)
        except Exception as exc2:
            return False, f"{type(exc2).__name__}: {exc2}"

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--live", action="store_true", help="perform live HTTP checks")
    args = parser.parse_args()
    failures = 0
    for path, source_id, row in iter_rows():
        if row is None or "error" in row:
            print(f"FAIL,{path},{source_id or ''},{row.get('error')}")
            failures += 1
            continue
        url = row.get("url", "")
        ok = plausible_url(url)
        status = "plausible" if ok else "bad_url"
        if ok and args.live:
            ok, status = check_live(url)
        print(f"{'OK' if ok else 'FAIL'},{path.name},{source_id},{status},{url}")
        failures += 0 if ok else 1
    return 1 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""
Validate Customary International Law metadata.
"""

from __future__ import annotations

import json
from pathlib import Path


ARTICLE_DIR = Path(__file__).resolve().parents[1]
REQUIRED = {
    "slug",
    "folder_slug",
    "title",
    "status",
    "domain",
    "series",
    "description",
    "canonical_url",
    "repository_path"
}


def main() -> None:
    metadata_path = ARTICLE_DIR / "metadata.json"
    data = json.loads(metadata_path.read_text(encoding="utf-8"))
    missing = REQUIRED - set(data)

    if missing:
        raise SystemExit(f"Missing metadata fields: {', '.join(sorted(missing))}")

    print(f"Metadata OK: {data['title']} -> {data['repository_path']}")


if __name__ == "__main__":
    main()

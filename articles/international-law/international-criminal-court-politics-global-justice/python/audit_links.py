from __future__ import annotations
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

URL_RE = re.compile("https?://[^\\s\\\"'<>]+")


def audit_html(path: Path) -> dict[str, object]:
    html = path.read_text(encoding="utf-8")
    urls = sorted(set(match.group(0).rstrip(').,;') for match in URL_RE.finditer(html)))
    return {
        "file": str(path),
        "url_count": len(urls),
        "domains": sorted(set(urlparse(url).netloc for url in urls)),
        "urls": urls,
    }


def main() -> None:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / "docs" / "wordpress_article_html.html"
    result = audit_html(target)
    out_path = Path(__file__).resolve().parents[1] / "outputs" / "link_audit.json"
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Audited {result['url_count']} unique URLs in {target}")


if __name__ == "__main__":
    main()

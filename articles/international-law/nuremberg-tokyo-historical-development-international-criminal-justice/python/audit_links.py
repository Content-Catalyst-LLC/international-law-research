from pathlib import Path
import json
import re

BASE = Path(__file__).resolve().parents[1]
HTML = BASE / "docs" / "wordpress_article_html.html"
OUTPUTS = BASE / "outputs"
OUTPUTS.mkdir(parents=True, exist_ok=True)
URL_RE = re.compile("https?://[^\\s\\\"'<>]+")
html = HTML.read_text(encoding="utf-8")
urls = sorted(set(URL_RE.findall(html)))
report = {
    "article": "Nuremberg, Tokyo, and the Historical Development of International Criminal Justice",
    "url_count": len(urls),
    "urls": urls,
}
out_path = OUTPUTS / "link_inventory.json"
out_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\\n", encoding="utf-8")
print(f"Wrote {out_path}")

"""Build the home page from index.md. The published site is static HTML."""

import re
import shutil
from html import escape
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "site"


def front_matter(text):
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    meta = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip()
    return meta, text[end + 5 :]


def main():
    meta, body = front_matter((ROOT / "index.md").read_text(encoding="utf-8"))
    html = markdown.markdown(body)
    html = html.replace("<p>VancePMorrison</p>", '<p class="aka">VancePMorrison</p>', 1)
    html = re.sub(r"<p>(<img [^>]+>)</p>", r'<p class="portrait">\1</p>', html, count=1)
    image = "vance-morrison.jpg"
    found = re.search(r'src="([^"]+)"', html)
    if found:
        image = found.group(1)

    layout = (ROOT / "layout.html").read_text(encoding="utf-8")
    page = (
        layout.replace("@@TITLE@@", escape(meta["title"]))
        .replace("@@DESCRIPTION@@", escape(meta["description"]))
        .replace("@@IMAGE@@", escape(image))
        .replace("@@BODY@@", html)
    )

    SITE.mkdir(exist_ok=True)
    (SITE / "index.html").write_text(page, encoding="utf-8")
    for name in ("style.css", "robots.txt", "sitemap.xml", image):
        shutil.copy2(ROOT / name, SITE / name)
    print(f"Built {SITE / 'index.html'}")


if __name__ == "__main__":
    main()

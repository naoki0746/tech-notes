import argparse
import html
import json
import re
import urllib.request
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse


VALID_CATEGORIES = {"aws", "azure", "windows", "linux"}


def main():
    parser = argparse.ArgumentParser(description="Import a public ChatGPT share link as a categorized tech note.")
    parser.add_argument("url", help="Public ChatGPT share URL")
    parser.add_argument("--category", required=True, choices=sorted(VALID_CATEGORIES), help="Destination category")
    parser.add_argument("--title", default="", help="Override note title")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite an existing note file")
    args = parser.parse_args()

    if not is_url(args.url):
        raise ValueError("url must be an http or https URL.")

    page = fetch_page(args.url)
    page_title = args.title.strip() or extract_html_title(page)
    parts = extract_shared_parts(page)
    if not parts:
        raise ValueError("No ChatGPT share messages were found in the page.")

    body = build_note(page_title, args.url, parts)
    out_dir = Path(args.category)
    out_dir.mkdir(parents=True, exist_ok=True)
    file_path = out_dir / f"{slugify(page_title)}.md"

    if file_path.exists() and not args.overwrite:
        raise FileExistsError(f"{file_path} already exists. Use --overwrite to replace it.")

    file_path.write_text(body, encoding="utf-8")
    print(f"Created note: {file_path}")


def is_url(value):
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def fetch_page(url):
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 tech-notes-importer"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def extract_html_title(page):
    match = re.search(r"<title>(.*?)</title>", page, flags=re.IGNORECASE | re.DOTALL)
    if not match:
        return "tech-note"
    title = html.unescape(match.group(1)).strip()
    title = re.sub(r"^ChatGPT\s*-\s*", "", title).strip()
    return title or "tech-note"


def extract_shared_parts(page):
    pattern = re.compile(
        r'\\"content_type\\",\\"text\\",\\"parts\\",\[\d+\],\\"([\s\S]*?)\\"'
    )
    parts = []
    for match in pattern.finditer(page):
        text = normalize_shared_text(json.loads(f'"{match.group(1)}"')).strip()
        text = unwrap_markdown_fence(text)
        if text and text not in parts:
            parts.append(text)
    return parts


def normalize_shared_text(text):
    if "\\n" in text or "\\t" in text:
        text = text.replace("\\r\\n", "\n")
        text = text.replace("\\n", "\n")
        text = text.replace("\\t", "\t")
    return text.replace('\\"', '"')


def unwrap_markdown_fence(text):
    match = re.match(r"^`{3,4}markdown\s*\n([\s\S]*?)\n`{3,4}\s*([\s\S]*)$", text.strip())
    if match:
        body = match.group(1).strip()
        rest = match.group(2).strip()
        return f"{body}\n\n{rest}".strip() if rest else body
    return text


def build_note(title, source, parts):
    now = datetime.now().strftime("%Y-%m-%d")
    content = "\n\n".join(part.strip() for part in parts if part.strip())
    if not content.lstrip().startswith("#"):
        content = f"# {title}\n\n{content}"

    front_matter = [
        "---",
        f"title: {json.dumps(title, ensure_ascii=False)}",
        "tags: []",
        f"source: {json.dumps(source, ensure_ascii=False)}",
        f"created: {json.dumps(now, ensure_ascii=False)}",
        "---",
        "",
    ]
    return "\n".join(front_matter + [content]).rstrip() + "\n"


def slugify(title):
    value = title.lower()
    value = re.sub(r"[^0-9a-zA-Zぁ-んァ-ン一-龯]+", "-", value)
    value = re.sub(r"^-+|-+$", "", value)
    return (value[:80] or "tech-note").lower()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Audit a static business website for common handoff issues.

Checks local assets, duplicate IDs, hash anchors, viewport meta, missing image alt
text, and CSS url() references. It intentionally avoids network access.
"""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


SKIP_SCHEMES = {
    "http",
    "https",
    "mailto",
    "tel",
    "sms",
    "javascript",
    "data",
    "blob",
}


class HtmlAuditParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.refs: list[tuple[str, str, int]] = []
        self.images: list[tuple[str, str | None, int]] = []
        self.viewport_found = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {k.lower(): v for k, v in attrs}
        line = self.getpos()[0]
        if "id" in attr and attr["id"]:
            self.ids.append(attr["id"] or "")
        if tag == "meta" and (attr.get("name") or "").lower() == "viewport":
            self.viewport_found = True
        if tag == "img":
            self.images.append((attr.get("src") or "", attr.get("alt"), line))
        for key in ("href", "src"):
            value = attr.get(key)
            if value:
                self.refs.append((key, value, line))


def is_external(ref: str) -> bool:
    parsed = urlsplit(ref.strip())
    return parsed.scheme.lower() in SKIP_SCHEMES or ref.startswith("//")


def clean_path(ref: str) -> str:
    parsed = urlsplit(ref.strip())
    return unquote(parsed.path)


def resolve_local(base_file: Path, site_root: Path, ref: str) -> Path:
    path = clean_path(ref)
    if path.startswith("/"):
        return site_root / path.lstrip("/")
    return base_file.parent / path


def parse_html(path: Path) -> HtmlAuditParser:
    parser = HtmlAuditParser()
    parser.feed(path.read_text(encoding="utf-8", errors="ignore"))
    return parser


def css_urls(css_text: str) -> list[str]:
    urls: list[str] = []
    for match in re.finditer(r"url\(([^)]+)\)", css_text):
        raw = match.group(1).strip().strip("\"'")
        if raw and not raw.startswith("#"):
            urls.append(raw)
    return urls


def add_issue(bucket: list[str], file_path: Path, line: int | None, message: str) -> None:
    if line:
        bucket.append(f"{file_path}:{line}: {message}")
    else:
        bucket.append(f"{file_path}: {message}")


def audit(site_root: Path, entry: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    entry_path = (site_root / entry).resolve()
    site_root = site_root.resolve()

    if not entry_path.exists():
        return [f"{entry_path}: entry HTML does not exist"], warnings

    html_files = [entry_path]
    seen_html = {entry_path}
    css_files: set[Path] = set()

    for html_file in list(html_files):
        parser = parse_html(html_file)
        id_counts: dict[str, int] = {}
        for item_id in parser.ids:
            id_counts[item_id] = id_counts.get(item_id, 0) + 1
        for item_id, count in sorted(id_counts.items()):
            if count > 1:
                add_issue(errors, html_file, None, f"duplicate id #{item_id!r} appears {count} times")

        if html_file == entry_path and not parser.viewport_found:
            add_issue(errors, html_file, None, "missing viewport meta tag")

        id_set = set(parser.ids)
        for src, alt, line in parser.images:
            if src and not is_external(src) and not src.startswith("#"):
                image_path = resolve_local(html_file, site_root, src)
                if not image_path.exists():
                    add_issue(errors, html_file, line, f"missing image asset {src!r}")
            if alt is None:
                add_issue(warnings, html_file, line, "image missing alt attribute")

        for attr, ref, line in parser.refs:
            if is_external(ref):
                continue
            if ref.startswith("#"):
                target = unquote(ref[1:])
                if target and target not in id_set:
                    add_issue(errors, html_file, line, f"anchor target #{target!r} not found")
                continue

            local_path = resolve_local(html_file, site_root, ref)
            if not clean_path(ref):
                continue
            if not local_path.exists():
                add_issue(errors, html_file, line, f"missing local {attr} target {ref!r}")
                continue
            if attr == "href" and local_path.suffix.lower() == ".css":
                css_files.add(local_path.resolve())
            if local_path.suffix.lower() in {".html", ".htm"} and local_path not in seen_html:
                seen_html.add(local_path)
                html_files.append(local_path)

            fragment = urlsplit(ref).fragment
            if fragment and local_path.suffix.lower() in {".html", ".htm"}:
                linked_parser = parse_html(local_path)
                if fragment not in set(linked_parser.ids):
                    add_issue(errors, html_file, line, f"anchor target #{fragment!r} not found in {local_path.name}")

    for css_file in sorted(css_files):
        text = css_file.read_text(encoding="utf-8", errors="ignore")
        for ref in css_urls(text):
            if is_external(ref):
                continue
            asset_path = resolve_local(css_file, site_root, ref)
            if not asset_path.exists():
                add_issue(errors, css_file, None, f"missing CSS url() asset {ref!r}")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit a static website for handoff issues.")
    parser.add_argument("site_root", help="Static site root directory")
    parser.add_argument("entry", nargs="?", default="index.html", help="Entry HTML file relative to root")
    args = parser.parse_args()

    site_root = Path(args.site_root).expanduser()
    errors, warnings = audit(site_root, args.entry)

    if errors:
        print("ERRORS:")
        for item in errors:
            print(f"  - {item}")
    if warnings:
        print("WARNINGS:")
        for item in warnings:
            print(f"  - {item}")
    if not errors and not warnings:
        print("OK: static site audit passed with no issues.")
    elif not errors:
        print(f"OK: static site audit passed with {len(warnings)} warning(s).")
    else:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s).")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

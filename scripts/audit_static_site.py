#!/usr/bin/env python3
"""Audit a static business website for common handoff issues.

Checks local assets, duplicate IDs, hash anchors, viewport meta, missing image alt
text, image width/height (CLS hygiene), target=_blank without rel=noopener,
CSS url() and @import references, large inline data: URIs, and optional
final-delivery placeholders. It intentionally avoids network access.
"""

from __future__ import annotations

import argparse
import json
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

# Warn about inline data: URIs larger than this (in source characters), since
# they bloat the HTML and block first paint.
DATA_URI_WARN_CHARS = 8 * 1024


PLACEHOLDER_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("Chinese placeholder", re.compile(r"待补充|待确认|示例待确认|替换这句|待替换")),
    ("English placeholder", re.compile(r"\b(TODO|TBD|REPLACE_ME)\b|Lorem ipsum", re.IGNORECASE)),
    ("example domain", re.compile(r"https?://(?:www\.)?(?:example\.com|your-domain\.com|yourdomain\.com)", re.IGNORECASE)),
]


class HtmlAuditParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.refs: list[tuple[str, str, int]] = []
        self.images: list[tuple[str, str | None, bool, int]] = []
        self.blank_targets: list[tuple[str, str, int]] = []
        self.html_lang: str | None = None
        self.title_parts: list[str] = []
        self.meta_tags: list[tuple[dict[str, str], int]] = []
        self.link_tags: list[tuple[dict[str, str], int]] = []
        self.h1_lines: list[int] = []
        self.json_ld_blocks: list[tuple[str, int]] = []
        self.viewport_found = False
        self._in_title = False
        self._in_json_ld = False
        self._json_ld_parts: list[str] = []
        self._json_ld_line: int | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {k.lower(): v for k, v in attrs}
        clean_attr = {k.lower(): v or "" for k, v in attrs}
        line = self.getpos()[0]
        if tag == "html":
            self.html_lang = attr.get("lang")
        if tag == "title":
            self._in_title = True
        if tag == "h1":
            self.h1_lines.append(line)
        if "id" in attr and attr["id"]:
            self.ids.append(attr["id"] or "")
        if tag == "meta" and (attr.get("name") or "").lower() == "viewport":
            self.viewport_found = True
        if tag == "meta":
            self.meta_tags.append((clean_attr, line))
        if tag == "link":
            self.link_tags.append((clean_attr, line))
        if tag == "script" and (attr.get("type") or "").lower() == "application/ld+json":
            self._in_json_ld = True
            self._json_ld_parts = []
            self._json_ld_line = line
        if tag == "img":
            has_dims = bool(attr.get("width") and attr.get("height"))
            self.images.append((attr.get("src") or "", attr.get("alt"), has_dims, line))
        if tag in ("a", "area") and (attr.get("target") or "").lower() == "_blank":
            self.blank_targets.append((attr.get("href") or "", attr.get("rel") or "", line))
        for key in ("href", "src"):
            value = attr.get(key)
            if value:
                self.refs.append((key, value, line))

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title_parts.append(data)
        if self._in_json_ld:
            self._json_ld_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        if tag == "script" and self._in_json_ld:
            self.json_ld_blocks.append(("".join(self._json_ld_parts).strip(), self._json_ld_line or self.getpos()[0]))
            self._in_json_ld = False
            self._json_ld_parts = []
            self._json_ld_line = None


def is_external(ref: str) -> bool:
    parsed = urlsplit(ref.strip())
    return parsed.scheme.lower() in SKIP_SCHEMES or ref.startswith("//")


def clean_path(ref: str) -> str:
    parsed = urlsplit(ref.strip())
    return unquote(parsed.path)


def resolve_local(base_file: Path, site_root: Path, ref: str, base_path: str = "") -> Path:
    path = clean_path(ref)
    if path.startswith("/"):
        stripped = path.lstrip("/")
        prefix = base_path.strip("/")
        # For sub-path deployments, absolute URLs include the deployment prefix
        # (e.g. /blog/assets/x.css); strip it so they map to local files.
        if prefix and (stripped == prefix or stripped.startswith(prefix + "/")):
            stripped = stripped[len(prefix):].lstrip("/")
        return site_root / stripped
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


def css_imports(css_text: str) -> list[str]:
    imports: list[str] = []
    for match in re.finditer(r"@import\s+(?:url\()?([^;)]+)\)?;", css_text):
        raw = match.group(1).strip().strip("\"'").split()[0] if match.group(1).strip().strip("\"'").split() else ""
        if raw and not raw.startswith("#"):
            imports.append(raw)
    return imports


def add_issue(bucket: list[str], file_path: Path, line: int | None, message: str) -> None:
    if line:
        bucket.append(f"{file_path}:{line}: {message}")
    else:
        bucket.append(f"{file_path}: {message}")


def meta_content(parser: HtmlAuditParser, *, name: str | None = None, prop: str | None = None) -> str | None:
    for attrs, _line in parser.meta_tags:
        if name and attrs.get("name", "").lower() == name.lower():
            return attrs.get("content") or ""
        if prop and attrs.get("property", "").lower() == prop.lower():
            return attrs.get("content") or ""
    return None


def has_link_rel(parser: HtmlAuditParser, rel_name: str) -> bool:
    needle = rel_name.lower()
    for attrs, _line in parser.link_tags:
        rels = {item.strip().lower() for item in attrs.get("rel", "").split()}
        if needle in rels and attrs.get("href"):
            return True
    return False


def add_seo_issue(
    errors: list[str],
    warnings: list[str],
    strict_seo: bool,
    file_path: Path,
    line: int | None,
    message: str,
) -> None:
    add_issue(errors if strict_seo else warnings, file_path, line, message)


def audit_seo(parser: HtmlAuditParser, html_file: Path, errors: list[str], warnings: list[str], strict_seo: bool) -> None:
    title = " ".join(part.strip() for part in parser.title_parts if part.strip()).strip()
    description = meta_content(parser, name="description")
    robots = (meta_content(parser, name="robots") or "").lower()

    if not parser.html_lang:
        add_seo_issue(errors, warnings, strict_seo, html_file, None, "missing html lang attribute")
    if not title:
        add_seo_issue(errors, warnings, strict_seo, html_file, None, "missing title element")
    if not description:
        add_seo_issue(errors, warnings, strict_seo, html_file, None, "missing meta description")
    if len(parser.h1_lines) != 1:
        add_seo_issue(errors, warnings, strict_seo, html_file, None, f"expected exactly one h1, found {len(parser.h1_lines)}")
    if not has_link_rel(parser, "canonical"):
        add_seo_issue(errors, warnings, strict_seo, html_file, None, "missing canonical link")

    for prop in ("og:title", "og:description", "og:type", "og:url", "og:image"):
        if not meta_content(parser, prop=prop):
            add_seo_issue(errors, warnings, strict_seo, html_file, None, f"missing Open Graph metadata {prop!r}")
    if not meta_content(parser, name="twitter:card"):
        add_seo_issue(errors, warnings, strict_seo, html_file, None, "missing Twitter Card metadata")

    if "noindex" in robots:
        add_issue(warnings, html_file, None, "robots meta contains noindex; confirm this is not a public launch page")

    if not parser.json_ld_blocks:
        add_seo_issue(errors, warnings, strict_seo, html_file, None, "missing JSON-LD structured data")
    for raw_json, line in parser.json_ld_blocks:
        if not raw_json:
            add_seo_issue(errors, warnings, strict_seo, html_file, line, "empty JSON-LD structured data")
            continue
        try:
            json.loads(raw_json)
        except json.JSONDecodeError as exc:
            add_seo_issue(errors, warnings, strict_seo, html_file, line, f"invalid JSON-LD: {exc.msg}")


def audit_placeholders(files: set[Path], errors: list[str]) -> None:
    for file_path in sorted(files):
        try:
            lines = file_path.read_text(encoding="utf-8", errors="ignore").splitlines()
        except OSError as exc:
            add_issue(errors, file_path, None, f"could not read file for placeholder scan: {exc}")
            continue
        for line_no, line in enumerate(lines, start=1):
            for label, pattern in PLACEHOLDER_PATTERNS:
                if pattern.search(line):
                    add_issue(errors, file_path, line_no, f"delivery placeholder remains ({label})")
                    break


def audit(
    site_root: Path,
    entry: str,
    *,
    strict_seo: bool = False,
    no_placeholders: bool = False,
    base_path: str = "",
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    entry_path = (site_root / entry).resolve()
    site_root = site_root.resolve()

    if not entry_path.exists():
        return [f"{entry_path}: entry HTML does not exist"], warnings

    html_files = [entry_path]
    seen_html = {entry_path}
    css_files: set[Path] = set()
    text_files: set[Path] = {entry_path}
    absolute_misses = 0

    index = 0
    while index < len(html_files):
        html_file = html_files[index]
        index += 1
        parser = parse_html(html_file)
        id_counts: dict[str, int] = {}
        for item_id in parser.ids:
            id_counts[item_id] = id_counts.get(item_id, 0) + 1
        for item_id, count in sorted(id_counts.items()):
            if count > 1:
                add_issue(errors, html_file, None, f"duplicate id #{item_id!r} appears {count} times")

        if html_file == entry_path and not parser.viewport_found:
            add_issue(errors, html_file, None, "missing viewport meta tag")

        audit_seo(parser, html_file, errors, warnings, strict_seo)

        id_set = set(parser.ids)
        for src, alt, has_dims, line in parser.images:
            if src.startswith("data:"):
                if len(src) > DATA_URI_WARN_CHARS:
                    add_issue(
                        warnings,
                        html_file,
                        line,
                        f"large inline data: URI image ({len(src)} chars); consider an external asset to reduce HTML weight",
                    )
            elif src and not src.startswith("#"):
                image_path = resolve_local(html_file, site_root, src, base_path)
                if not image_path.exists():
                    add_issue(errors, html_file, line, f"missing image asset {src!r}")
            if alt is None:
                add_issue(warnings, html_file, line, "image missing alt attribute")
            if not has_dims and src and not src.startswith("data:"):
                add_issue(warnings, html_file, line, "image missing width/height attributes (may cause layout shift / CLS)")

        for href, rel, line in parser.blank_targets:
            rels = {item.strip().lower() for item in rel.split()}
            if "noopener" not in rels:
                add_issue(
                    warnings,
                    html_file,
                    line,
                    "target=\"_blank\" without rel=\"noopener\" (add noopener for security/performance)",
                )

        for attr, ref, line in parser.refs:
            if is_external(ref):
                continue
            if ref.startswith("#"):
                target = unquote(ref[1:])
                if target and target not in id_set:
                    add_issue(errors, html_file, line, f"anchor target #{target!r} not found")
                continue

            local_path = resolve_local(html_file, site_root, ref, base_path)
            if not clean_path(ref):
                continue
            if not local_path.exists():
                add_issue(errors, html_file, line, f"missing local {attr} target {ref!r}")
                if clean_path(ref).startswith("/"):
                    absolute_misses += 1
                continue
            if attr == "href" and local_path.suffix.lower() == ".css":
                css_files.add(local_path.resolve())
                text_files.add(local_path.resolve())
            if attr == "src" and local_path.suffix.lower() == ".js":
                text_files.add(local_path.resolve())
            if local_path.suffix.lower() in {".html", ".htm"} and local_path not in seen_html:
                seen_html.add(local_path)
                html_files.append(local_path)
                text_files.add(local_path.resolve())

            fragment = urlsplit(ref).fragment
            if fragment and local_path.suffix.lower() in {".html", ".htm"}:
                linked_parser = parse_html(local_path)
                if fragment not in set(linked_parser.ids):
                    add_issue(errors, html_file, line, f"anchor target #{fragment!r} not found in {local_path.name}")

    # Heuristic: many absolute-path misses usually means site_root was given as a
    # page subdirectory rather than the deployment root (a common false positive).
    if absolute_misses >= 3:
        add_issue(
            warnings,
            site_root,
            None,
            f"{absolute_misses} absolute-path references unresolved; site_root should usually be the deployment root, not the page's subdirectory (use --base-path for sub-path deployments)",
        )

    scanned_css: set[Path] = set()
    pending_css = sorted(css_files)
    while pending_css:
        css_file = pending_css.pop()
        if css_file in scanned_css:
            continue
        scanned_css.add(css_file)
        text = css_file.read_text(encoding="utf-8", errors="ignore")
        for ref in css_urls(text):
            if is_external(ref):
                continue
            asset_path = resolve_local(css_file, site_root, ref, base_path)
            if not asset_path.exists():
                add_issue(errors, css_file, None, f"missing CSS url() asset {ref!r}")
        for ref in css_imports(text):
            if is_external(ref):
                continue
            import_path = resolve_local(css_file, site_root, ref, base_path)
            if not import_path.exists():
                add_issue(errors, css_file, None, f"missing CSS @import target {ref!r}")
            elif import_path.suffix.lower() == ".css" and import_path.resolve() not in scanned_css:
                pending_css.append(import_path.resolve())
                text_files.add(import_path.resolve())

    if no_placeholders:
        audit_placeholders(text_files, errors)

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit a static website for handoff issues.")
    parser.add_argument(
        "site_root",
        help="Deployment root of the static site (the domain root, NOT the page's subdirectory). "
        "Absolute refs like '/assets/x.css' resolve under here.",
    )
    parser.add_argument("entry", nargs="?", default="index.html", help="Entry HTML file relative to root")
    parser.add_argument("--strict-seo", action="store_true", help="Treat missing SEO/GEO launch metadata as errors")
    parser.add_argument("--no-placeholders", action="store_true", help="Treat common placeholder text as final-delivery errors")
    parser.add_argument(
        "--base-path",
        default="",
        help="Deployment sub-path prefix (e.g. 'blog') to strip from absolute refs for sub-path deployments",
    )
    args = parser.parse_args()

    site_root = Path(args.site_root).expanduser()
    errors, warnings = audit(
        site_root,
        args.entry,
        strict_seo=args.strict_seo,
        no_placeholders=args.no_placeholders,
        base_path=args.base_path,
    )

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

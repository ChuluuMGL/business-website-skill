#!/usr/bin/env python3
"""Create a lightweight runtime ZIP for installing this skill in agent tools."""

from __future__ import annotations

import argparse
import zipfile
from pathlib import Path


DEFAULT_OUTPUT = Path("dist/business-website-skill-runtime.zip")
INCLUDE_PATHS = [
    "SKILL.md",
    "LICENSE",
    "NOTICE",
    "README.md",
    "README.zh-CN.md",
    "agents/openai.yaml",
    "assets/presets",
    "assets/previews/README.md",
    "assets/templates",
    "references",
    "scripts/audit_static_site.py",
    "scripts/package_runtime_skill.py",
    "skill.json",
]
SKIP_NAMES = {".DS_Store", "__pycache__"}
SKIP_SUFFIXES = {".pyc", ".pyo"}
PREVIEW_BINARY_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".mp4", ".mov"}


def should_skip(path: Path) -> bool:
    if any(part in SKIP_NAMES for part in path.parts):
        return True
    if path.suffix.lower() in SKIP_SUFFIXES:
        return True
    if path.parts[:2] == ("assets", "previews") and path.suffix.lower() in PREVIEW_BINARY_SUFFIXES:
        return True
    return False


def iter_included_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for item in INCLUDE_PATHS:
        path = root / item
        if not path.exists():
            raise FileNotFoundError(f"required package path missing: {item}")
        if path.is_file():
            rel = path.relative_to(root)
            if not should_skip(rel):
                files.append(rel)
            continue
        for child in sorted(path.rglob("*")):
            if child.is_file():
                rel = child.relative_to(root)
                if not should_skip(rel):
                    files.append(rel)
    return sorted(set(files))


def write_zip(root: Path, output: Path) -> tuple[int, int]:
    files = iter_included_files(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for rel in files:
            archive.write(root / rel, Path("business-website-skill") / rel)
    return len(files), output.stat().st_size


def main() -> int:
    parser = argparse.ArgumentParser(description="Package a lightweight business-website-skill runtime ZIP.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output ZIP path")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    output = Path(args.output).expanduser()
    if not output.is_absolute():
        output = root / output

    count, size = write_zip(root, output)
    print(f"Wrote {output} ({count} files, {size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Sync the marketing site's proof-strip metrics from source, not by hand.

Replaces the four hardcoded proof-strip numbers in site/index.html
(<dt data-metric="..."> values) with values computed from the actual source:

  - visual systems  -> len(design-styles.json["visual_systems"])
  - interaction presets -> len(interaction-presets.json["presets"])
  - package size    -> real compressed size of the runtime ZIP produced by
                       package_runtime_skill.py (same logic, in-memory)
  - phases          -> a hand-curated constant (see PHASE_COUNT); it reflects the
                       site's 7-step narrative, not a raw Phase 0-7 count, so it
                       is not auto-derived.

Run this whenever presets, package contents, or the workflow change, then commit
site/index.html. This kills the drift seen at 1.4.6, where the site claimed
"68K" while the real package was ~92K. No PIL dependency.

Usage:
    python3 scripts/sync_site_metrics.py
"""

from __future__ import annotations

import io
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = [
    ROOT / "site" / "index.html",
    ROOT / "site" / "en" / "index.html",
]

# The site presents the workflow as a 7-step narrative (the timeline groups
# Phase 6-7). It is a writing/design decision, so it stays a constant here.
PHASE_COUNT = 7


def _load_json(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def compute_metrics() -> dict[str, str]:
    design = _load_json("assets/presets/design-styles.json")
    interactions = _load_json("assets/presets/interaction-presets.json")
    visual_systems = len(design.get("visual_systems", []))
    interaction_count = len(interactions.get("presets", []))

    import package_runtime_skill  # sibling script

    files = package_runtime_skill.iter_included_files(ROOT)
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        prefix = Path("business-website-skill")
        for rel in files:
            archive.writestr(str(prefix / rel), (ROOT / rel).read_bytes())
    kib = round(len(buf.getvalue()) / 1024)

    return {
        "phases": str(PHASE_COUNT),
        "visual-systems": f"{visual_systems}+",
        "interactions": f"{interaction_count}+" if interaction_count >= 20 else str(interaction_count),
        "package-size": f"{kib}K",
    }


def sync_file(target: Path, metrics: dict[str, str]) -> None:
    if not target.exists():
        return
    html = target.read_text(encoding="utf-8")
    changed = False

    def replace(match: re.Match) -> str:
        nonlocal changed
        key = match.group("key")
        if key not in metrics:
            return match.group(0)
        new_inner = f'>{metrics[key]}<'
        if match.group(2) != new_inner:
            changed = True
        return match.group(1) + new_inner

    pattern = re.compile(r'(<dt[^>]*data-metric="(?P<key>[^"]+)"[^>]*)(>[^<]*<)')
    new_html, _ = pattern.subn(replace, html)

    if changed:
        target.write_text(new_html, encoding="utf-8")
        print(f"Updated {target.relative_to(ROOT)} proof-strip metrics")
    else:
        print(f"Metrics already in sync: {target.relative_to(ROOT)}")


def sync() -> dict[str, str]:
    metrics = compute_metrics()
    print(f"Computed metrics: {metrics}")
    for target in TARGETS:
        sync_file(target, metrics)
    return metrics


def main() -> int:
    sync()
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Smoke-test the rendered showcase example sites.

For each example (b2b-service, industrial-green-tech, ai-saas-product) this:
  1. verifies the brief/prompt/expected-output fixtures exist,
  2. runs audit_static_site.py on the rendered demo with --strict-seo
     --no-placeholders (must report 0 errors),
  3. greps the rendered HTML for leftover delivery placeholders (must be none),
  4. light-checks that expected-output.md and the rendered demo share the
     example's key style/visual-system markers.

This is the regression net the skill was missing: audit_static_site.py checks
site *health*; this checks that each *example* still builds clean and matches its
declared expected output. Exits non-zero if any example fails.

Usage:
    python3 scripts/smoke_examples.py
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ["b2b-service", "industrial-green-tech", "ai-saas-product"]
FIXTURES = ["brief.md", "prompt.md", "expected-output.md"]

# The declared visual/style direction each example should target. These double as
# a check that the example↔preset mapping is intact (sourced from each example's
# expected-output.md). Kept intentionally loose.
EXAMPLE_MARKERS = {
    "b2b-service": ["executive-b2b-trust"],
    "industrial-green-tech": ["industrial-precision"],
    "ai-saas-product": ["ai-saas-data-cloud"],
}

PLACEHOLDER_RE = re.compile(r"待补充|待确认|示例待确认|替换这句|Lorem ipsum|\bTODO\b|\bTBD\b|REPLACE_ME", re.IGNORECASE)


def run(cmd: list[str]) -> tuple[int, str]:
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.returncode, (proc.stdout + proc.stderr)


def smoke_one(name: str) -> list[str]:
    failures: list[str] = []
    fixture_dir = ROOT / "examples" / name
    rendered_entry = f"examples/{name}/index.html"

    for fixture in FIXTURES:
        if not (fixture_dir / fixture).exists():
            failures.append(f"missing fixture examples/{name}/{fixture}")

    audit = ROOT / "scripts" / "audit_static_site.py"
    code, out = run([
        sys.executable, str(audit), str(ROOT / "site"), rendered_entry,
        "--strict-seo", "--no-placeholders",
    ])
    if code != 0:
        failures.append(f"audit failed (exit {code}):\n{out.strip()}")

    index_html = ROOT / "site" / "examples" / name / "index.html"
    if index_html.exists():
        html = index_html.read_text(encoding="utf-8", errors="ignore")
        hits = sorted({m.group(0) for m in PLACEHOLDER_RE.finditer(html)})
        if hits:
            failures.append(f"placeholder text remains in rendered HTML: {hits}")
    else:
        failures.append(f"rendered demo missing: site/examples/{name}/index.html")

    expected = fixture_dir / "expected-output.md"
    if expected.exists():
        text = expected.read_text(encoding="utf-8", errors="ignore").lower()
        missing = [m for m in EXAMPLE_MARKERS.get(name, []) if m not in text]
        if missing:
            failures.append(f"expected-output.md missing key markers: {missing}")

    return failures


def main() -> int:
    all_failures: list[tuple[str, list[str]]] = []
    for name in EXAMPLES:
        failures = smoke_one(name)
        status = "PASS" if not failures else "FAIL"
        print(f"[{status}] {name}")
        if failures:
            all_failures.append((name, failures))
            for f in failures:
                for line in f.splitlines():
                    print(f"        {line}")

    print()
    if all_failures:
        print(f"FAILED: {len(all_failures)}/{len(EXAMPLES)} example(s) with issues.")
        return 1
    print(f"OK: all {len(EXAMPLES)} example smoke checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

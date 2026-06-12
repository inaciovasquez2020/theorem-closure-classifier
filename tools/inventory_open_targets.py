#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(".")
SKIP_DIRS = {".git", ".pytest_cache", "__pycache__", ".mypy_cache", ".ruff_cache"}

PATTERNS = [
    r"\bFRONTIER_OPEN\b",
    r"\bblocked_pending\b",
    r"\bfirst_missing_object\b",
    r"\bfirst_missing_lean_object\b",
    r"\bTODO\b",
    r"\bFIXME\b",
]

ALLOW_LINES = [
    '"first_missing_object": null',
    '"status": "passed"',
    '"external_replay_status": "passed"',
    'data.get("first_missing_object") is None',
]

def iter_files():
    for p in ROOT.rglob("*"):
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        if p.is_file() and p.suffix in {".py", ".json", ".md", ".lean", ".toml", ".yml", ".yaml"}:
            yield p

def main() -> None:
    hits = []
    regexes = [re.compile(p) for p in PATTERNS]

    for p in iter_files():
        text = p.read_text(encoding="utf-8", errors="replace")
        for n, line in enumerate(text.splitlines(), 1):
            if any(a in line for a in ALLOW_LINES):
                continue
            if any(r.search(line) for r in regexes):
                hits.append((p, n, line.strip()))

    if not hits:
        print("REPOSITORY_OPEN_TARGET_INVENTORY_EMPTY")
        return

    print("REPOSITORY_OPEN_TARGET_INVENTORY_NONEMPTY")
    for p, n, line in hits[:200]:
        print(f"{p}:{n}: {line}")

if __name__ == "__main__":
    main()

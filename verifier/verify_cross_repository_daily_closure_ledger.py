#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "artifacts" / "closure_ledger" / "cross_repository_daily_closure_ledger_2026_06_12.json"

REQUIRED_ENTRY_KEYS = {"theorem_object", "validation_command", "boundary"}


def main() -> int:
    data = json.loads(PATH.read_text(encoding="utf-8"))

    if data.get("ledger") != "CROSS_REPOSITORY_DAILY_CLOSURE_LEDGER":
        print("CROSS_REPOSITORY_DAILY_CLOSURE_LEDGER_NAME_INVALID")
        return 1

    if data.get("date") != "2026-06-12":
        print("CROSS_REPOSITORY_DAILY_CLOSURE_LEDGER_DATE_INVALID")
        return 1

    if set(data.get("required_keys", [])) != REQUIRED_ENTRY_KEYS:
        print("CROSS_REPOSITORY_DAILY_CLOSURE_LEDGER_REQUIRED_KEYS_INVALID")
        return 1

    entries = data.get("entries")
    if not isinstance(entries, list) or not entries:
        print("CROSS_REPOSITORY_DAILY_CLOSURE_LEDGER_EMPTY")
        return 1

    for index, entry in enumerate(entries):
        missing = REQUIRED_ENTRY_KEYS - set(entry)
        if missing:
            missing_csv = ",".join(sorted(missing))
            print(f"CROSS_REPOSITORY_DAILY_CLOSURE_LEDGER_ENTRY_{index}_MISSING:{missing_csv}")
            return 1

        for key in REQUIRED_ENTRY_KEYS:
            if not isinstance(entry[key], str) or not entry[key].strip():
                print(f"CROSS_REPOSITORY_DAILY_CLOSURE_LEDGER_ENTRY_{index}_EMPTY:{key}")
                return 1

    print("CROSS_REPOSITORY_DAILY_CLOSURE_LEDGER_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "artifacts" / "schema" / "classifier_substance_status_field_2026_06_12.json"

REQUIRED = {
    "schema_object": "CLASSIFIER_SUBSTANCE_STATUS_FIELD",
    "field": "mathematical_substance_status",
    "allowed_values": ["build_valid_only", "mathematically_substantive"],
    "required_witness_field": "mathematical_substance_witness",
}


def main() -> int:
    data = json.loads(PATH.read_text(encoding="utf-8"))

    for key, value in REQUIRED.items():
        if data.get(key) != value:
            print(f"CLASSIFIER_SUBSTANCE_STATUS_FIELD_INVALID:{key}")
            return 1

    rule = data.get("field_rule", {})
    if set(rule) != {"build_valid_only", "mathematically_substantive"}:
        print("CLASSIFIER_SUBSTANCE_STATUS_FIELD_RULE_INVALID")
        return 1

    print("CLASSIFIER_SUBSTANCE_STATUS_FIELD_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

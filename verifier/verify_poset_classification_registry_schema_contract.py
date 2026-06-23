#!/usr/bin/env python3
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "artifacts/external_validation/poset_classification_registry_consistency_2026_06_23.json"

REQUIRED_ENTRY_KEYS = {
    "artifact_id",
    "artifact_path",
    "classification_level",
    "reason",
}


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise SystemExit(f"MISSING_OBJECT := {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def registry_entry_lists(data: dict[str, Any]) -> list[tuple[str, list[dict[str, Any]]]]:
    candidates: list[tuple[str, list[dict[str, Any]]]] = []
    for key, value in data.items():
        if not isinstance(value, list) or not value:
            continue
        if not all(isinstance(entry, dict) for entry in value):
            continue
        if not all(REQUIRED_ENTRY_KEYS <= set(entry) for entry in value):
            continue
        candidates.append((key, value))
    return candidates


def main() -> None:
    registry = load_json(REGISTRY)

    if registry.get("artifact_type") != "bounded_poset_classification_registry_consistency_certificate":
        raise SystemExit("BOUNDARY := wrong_registry_artifact_type")

    candidates = registry_entry_lists(registry)
    if len(candidates) != 1:
        raise SystemExit("BOUNDARY := registry_entry_list_field_not_unique")

    field_name, entries = candidates[0]
    if not isinstance(field_name, str) or not field_name.strip():
        raise SystemExit("BOUNDARY := invalid_registry_entry_list_field_name")

    if len(entries) < 2:
        raise SystemExit("BOUNDARY := registry_entry_list_too_small")

    for entry in entries:
        if set(entry) != REQUIRED_ENTRY_KEYS:
            raise SystemExit(f"BOUNDARY := registry_entry_shape_not_exact {entry.get('artifact_id', '<missing>')}")
        for key in REQUIRED_ENTRY_KEYS:
            if not isinstance(entry.get(key), str) or not entry[key].strip():
                raise SystemExit(f"BOUNDARY := registry_entry_field_not_nonempty_string {entry.get('artifact_id', '<missing>')} {key}")

    print("POSET_CLASSIFICATION_REGISTRY_SCHEMA_CONTRACT_OK")


if __name__ == "__main__":
    main()

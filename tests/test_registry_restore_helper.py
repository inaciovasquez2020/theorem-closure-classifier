import importlib.util
from collections.abc import Generator
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "tests/registry_restore.py"
REGISTRY = ROOT / "artifacts/external_validation/poset_classification_registry_consistency_2026_06_23.json"


def load_helper():
    spec = importlib.util.spec_from_file_location("registry_restore_helper_under_test", HELPER)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def restore_generator() -> Generator[None, None, None]:
    helper = load_helper()
    return helper.registry_file_is_restored.__wrapped__()


def test_registry_restore_helper_accepts_unchanged_registry() -> None:
    fixture = restore_generator()

    next(fixture)

    with pytest.raises(StopIteration):
        next(fixture)


def test_registry_restore_helper_rejects_unrestored_registry_mutation() -> None:
    original = REGISTRY.read_text(encoding="utf-8")
    fixture = restore_generator()
    next(fixture)

    try:
        REGISTRY.write_text(original + "\n", encoding="utf-8")

        with pytest.raises(AssertionError):
            next(fixture)
    finally:
        REGISTRY.write_text(original, encoding="utf-8")

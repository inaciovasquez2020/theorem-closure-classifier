from __future__ import annotations

import json
from pathlib import Path

from verifier.verify_external_reference_sync import verify

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "artifacts/status/external_reference_sync_2026_06_11.json"
DOC = ROOT / "docs/status/EXTERNAL_REFERENCE_SYNC_2026_06_11.md"


def test_external_reference_sync_verifies() -> None:
    verify()


def test_status_is_reference_only() -> None:
    data = json.loads(ARTIFACT.read_text())
    assert data["status"] == "EXTERNAL_REFERENCE_SYNC_REFERENCE_ONLY"
    assert data["resolved_missing_object"] == "EXTERNAL_REFERENCE_SYNC"
    assert data["minimal_missing_object"] == "STOP"


def test_boundary_blocks_theorem_and_physics_claims() -> None:
    data = json.loads(ARTIFACT.read_text())
    boundary = set(data["boundary"])
    assert "REFERENCE_ONLY" in boundary
    assert "STATUS_ARTIFACT_ONLY" in boundary
    assert "NO_NEW_THEOREM_CLAIM" in boundary
    assert "NO_PHYSICAL_SOUNDNESS_CLAIM" in boundary
    assert "NO_SOLUTION_OF_GRAVITY_CLAIM" in boundary


def test_depends_on_completion_lock() -> None:
    data = json.loads(ARTIFACT.read_text())
    assert data["depends_on"] == [
        "STL_ADM_CONSTRAINT_SURFACE_INTERACTION_COMPLETION_LOCK_2026_06_09"
    ]


def test_no_completion_percentage_or_overclaim_surface() -> None:
    data = json.loads(ARTIFACT.read_text())
    assert "proof" not in data
    assert "theorem" not in data
    assert "%" not in ARTIFACT.read_text()
    assert "%" not in DOC.read_text()

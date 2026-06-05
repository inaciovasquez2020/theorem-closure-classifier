import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "verifier"))

from classify_theorem_closure import Classification, classify, claim_from_control


def load_controls():
    return json.loads((ROOT / "controls" / "seven_controls_v1.json").read_text(encoding="utf-8"))


@pytest.mark.parametrize("control", load_controls(), ids=lambda item: item["id"])
def test_control_classification(control):
    result = classify(claim_from_control(control))
    assert result.classification == Classification(control["expected"])


def test_control_suite_size():
    assert len(load_controls()) == 7

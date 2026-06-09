from verifier.verify_classifier_decision_surface import classifier_decision_map, verify


def test_classifier_decision_surface() -> None:
    verify()


def test_classifier_decision_map_is_total_on_manifest_labels() -> None:
    decision_map = classifier_decision_map()
    assert set(decision_map) == {
        "CLOSED_THEOREM",
        "OPEN_FRONTIER",
        "BOUNDARY_ONLY",
        "NO_EXTERNAL_ACCEPTANCE",
        "CLASSIFIER_OUTPUT_NOT_PROOF",
        "NO_CLAY_CLAIM",
    }
    assert all(decision.startswith("LABEL_") for decision in decision_map.values())

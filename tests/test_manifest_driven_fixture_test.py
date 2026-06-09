from verifier.verify_manifest_driven_fixture_test import manifest_fixture_label_map, verify


def test_manifest_driven_fixture_test() -> None:
    verify()


def test_manifest_fixture_label_map_is_manifest_driven() -> None:
    label_map = manifest_fixture_label_map()
    assert set(label_map) == {
        "positive_closed_theorem_fixture_001",
        "negative_open_frontier_fixture_001",
        "boundary_only_status_fixture_001",
        "external_acceptance_absent_fixture_001",
        "classifier_output_not_proof_fixture_001",
        "clay_claim_negative_control_fixture_001",
    }

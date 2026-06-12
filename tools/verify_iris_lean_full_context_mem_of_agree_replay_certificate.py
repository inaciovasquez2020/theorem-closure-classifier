#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ARTIFACT = Path(
    "artifacts/external_validation/"
    "iris_lean_full_context_mem_of_agree_replay_certificate_2026_06_12.json"
)

EXPECTED_ID = "IRIS_LEAN_FULL_CONTEXT_MEM_OF_AGREE_REPLAY_CERTIFICATE_2026_06_12"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    require(ARTIFACT.is_file(), f"missing artifact: {ARTIFACT}")
    data = json.loads(ARTIFACT.read_text())

    require(data.get("certificate_id") == EXPECTED_ID, "bad certificate_id")
    require(data.get("date") == "2026-06-12", "bad date")
    require(data.get("scope") == "external_validation_only", "bad scope")

    state = data.get("validated_state", {})
    require(state.get("external_replay_status") == "passed", "bad external replay status")
    require(
        state.get("external_replay_command")
        == "cd $HOME/Desktop/GITHUB/external/iris-lean/Iris && lake env lean MemOfAgreeReplay.lean",
        "bad external replay command",
    )
    require(state.get("external_replay_stdout") == "", "unexpected external replay stdout")
    require(state.get("external_replay_stderr") == "", "unexpected external replay stderr")

    pin = data.get("upstream_pin", {})
    require(pin.get("commit") == "6ddf890", "bad upstream commit")
    require(pin.get("tag") == "v4.30.0", "bad upstream tag")
    require(pin.get("project_root") == "$HOME/Desktop/GITHUB/external/iris-lean/Iris", "bad project root")
    require(pin.get("source_file") == "Iris/Algebra/Agree.lean", "bad source file")

    resolved = data.get("resolved_identifiers", {})
    require(resolved.get("agree_type") == "Iris.Agree", "bad Agree identifier")
    require(resolved.get("source_theorem") == "Iris.mem_of_agree", "bad source theorem identifier")
    require(
        resolved.get("external_replay_theorem")
        == "TheoremClosureClassifier.External.IrisLean.MemOfAgreeReplay.mem_of_agree_replay",
        "bad external replay theorem identifier",
    )

    target = data.get("target", {})
    require(target.get("name") == "mem_of_agree", "bad target name")
    require(target.get("kind") == "full_context_replay_certificate", "bad target kind")
    require(target.get("status") == "passed", "bad target status")

    boundary = data.get("claim_boundary", {})
    for key in (
        "does_not_modify_upstream",
        "does_not_claim_theorem_ownership",
        "does_not_claim_upstream_endorsement",
        "does_not_claim_semantic_soundness",
        "does_not_claim_full_project_build",
        "does_not_pursue_further_upstream_audit_script",
    ):
        require(boundary.get(key) is True, f"boundary invariant failed: {key}")

    require(data.get("first_missing_object") is None, "first missing object must be null")

    print("IRIS_LEAN_FULL_CONTEXT_MEM_OF_AGREE_REPLAY_CERTIFICATE_OK")


if __name__ == "__main__":
    main()

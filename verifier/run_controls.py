import json
from pathlib import Path

from classify_theorem_closure import classify, claim_from_control


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    controls_path = root / "controls" / "seven_controls_v1.json"
    outputs_path = root / "artifacts" / "classifier_run_outputs_v1.json"

    controls = json.loads(controls_path.read_text(encoding="utf-8"))
    outputs = []

    for item in controls:
        result = classify(claim_from_control(item))
        observed = result.classification.value
        outputs.append({
            "id": item["id"],
            "expected": item["expected"],
            "observed": observed,
            "minimal_missing_object": result.minimal_missing_object,
            "result": "PASS" if observed == item["expected"] else "FAIL",
        })

    summary = {
        "suite": "SevenBenchmarkControls_V1",
        "total_controls": len(outputs),
        "passed": sum(1 for item in outputs if item["result"] == "PASS"),
        "failed": sum(1 for item in outputs if item["result"] == "FAIL"),
        "outputs": outputs,
    }

    outputs_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))

    return 0 if summary["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

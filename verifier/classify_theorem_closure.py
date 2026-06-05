from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional


class Classification(str, Enum):
    COMPLETE_UNCONDITIONAL_LEDGER = "COMPLETE_UNCONDITIONAL_LEDGER"
    COMPLETE_CONDITIONAL_LEDGER = "COMPLETE_CONDITIONAL_LEDGER"
    INCOMPLETE_LEDGER = "INCOMPLETE_LEDGER"
    OVERCLAIMED_LEDGER = "OVERCLAIMED_LEDGER"
    BENCHMARK_MATCH_ONLY = "BENCHMARK_MATCH_ONLY"


REQUIRED_OBJECTS = [
    "exact_statement",
    "domain",
    "hypothesis",
    "construction",
    "obstruction",
    "necessity_direction",
    "sufficiency_direction",
    "boundary",
    "proof_ledger",
    "dependency_ledger",
    "claim_boundary_ledger",
]


@dataclass(frozen=True)
class ClosureClaim:
    claim_id: str
    objects: Dict[str, str]
    open_hypothesis: bool
    missing_proof_object: bool
    claimed_domain_exceeds_proven_domain: bool
    benchmark_match_only: bool
    trusted_verifier_status: str


@dataclass(frozen=True)
class ClassificationResult:
    claim_id: str
    classification: Classification
    minimal_missing_object: Optional[str]


def first_missing_required_object(claim: ClosureClaim) -> Optional[str]:
    for obj in REQUIRED_OBJECTS:
        if claim.objects.get(obj) != "present":
            return obj
    return None


def classify(claim: ClosureClaim) -> ClassificationResult:
    if claim.claimed_domain_exceeds_proven_domain:
        return ClassificationResult(
            claim.claim_id,
            Classification.OVERCLAIMED_LEDGER,
            "ClaimedDomainExceedsProvenDomain",
        )

    if claim.benchmark_match_only:
        return ClassificationResult(
            claim.claim_id,
            Classification.BENCHMARK_MATCH_ONLY,
            None,
        )

    missing = first_missing_required_object(claim)
    if missing is not None:
        return ClassificationResult(
            claim.claim_id,
            Classification.INCOMPLETE_LEDGER,
            missing,
        )

    if claim.missing_proof_object:
        return ClassificationResult(
            claim.claim_id,
            Classification.INCOMPLETE_LEDGER,
            "MissingProofObject",
        )

    if claim.open_hypothesis:
        return ClassificationResult(
            claim.claim_id,
            Classification.COMPLETE_CONDITIONAL_LEDGER,
            "OpenHypothesisObject",
        )

    return ClassificationResult(
        claim.claim_id,
        Classification.COMPLETE_UNCONDITIONAL_LEDGER,
        None,
    )


def claim_from_control(control: dict) -> ClosureClaim:
    flags = control["flags"]
    return ClosureClaim(
        claim_id=control["id"],
        objects=control["objects"],
        open_hypothesis=flags["open_hypothesis"],
        missing_proof_object=flags["missing_proof_object"],
        claimed_domain_exceeds_proven_domain=flags["claimed_domain_exceeds_proven_domain"],
        benchmark_match_only=flags["benchmark_match_only"],
        trusted_verifier_status=flags["trusted_verifier_status"],
    )

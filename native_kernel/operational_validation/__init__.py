"""Technology-neutral bounded C5 operational-rehearsal evidence helpers.

The package records synthetic ephemeral operational evidence. It does not expose
a production runtime, promote authority, certify compliance, or prove physical
deletion.
"""

from .core import (
    DEPLOYMENT_CLASS,
    EXPECTED_ASSERTION_COUNTS,
    OPERATIONAL_LEVEL,
    PLAN_PROTOCOL,
    RECEIPT_PROTOCOL,
    REPORT_PROTOCOL,
    OperationalRecorder,
    OperationalValidationError,
    ScenarioResult,
    build_report,
    canary_leaks,
    canonical_json_bytes,
    load_json,
    percentile,
    redact_text,
    redact_value,
    sha256_digest,
    validate_c4_prerequisite,
    validate_plan,
    validate_report,
)

__all__ = [
    "DEPLOYMENT_CLASS",
    "EXPECTED_ASSERTION_COUNTS",
    "OPERATIONAL_LEVEL",
    "PLAN_PROTOCOL",
    "RECEIPT_PROTOCOL",
    "REPORT_PROTOCOL",
    "OperationalRecorder",
    "OperationalValidationError",
    "ScenarioResult",
    "build_report",
    "canary_leaks",
    "canonical_json_bytes",
    "load_json",
    "percentile",
    "redact_text",
    "redact_value",
    "sha256_digest",
    "validate_c4_prerequisite",
    "validate_plan",
    "validate_report",
]

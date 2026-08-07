"""Offline, authority-free C4 shadow evaluation."""

from .evaluator import (
    DATASET_VERSION,
    RECEIPT_VERSION,
    REPORT_VERSION,
    ShadowEvaluationError,
    evaluate,
    load_json,
    render_report,
    report_from_files,
    validate_c3_prerequisite,
    validate_dataset,
    validate_report,
    validate_report_file,
)

__all__ = [
    "DATASET_VERSION",
    "RECEIPT_VERSION",
    "REPORT_VERSION",
    "ShadowEvaluationError",
    "evaluate",
    "load_json",
    "render_report",
    "report_from_files",
    "validate_c3_prerequisite",
    "validate_dataset",
    "validate_report",
    "validate_report_file",
]

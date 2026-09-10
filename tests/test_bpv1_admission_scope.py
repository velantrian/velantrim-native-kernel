"""Regression tests for BPV1 admission live-delta scoping."""
from __future__ import annotations

import unittest
from pathlib import Path
from unittest.mock import call, patch

from tools.bpv1.audit_admission_scope import ADMISSION_MERGE, BASE, audit


class BPV1AdmissionScopeTests(unittest.TestCase):
    @patch("tools.bpv1.audit_admission_scope._changed_paths")
    def test_ongoing_guard_uses_explicit_live_base(self, changed_paths) -> None:
        changed_paths.side_effect = [
            ["tools/bpv1/audit_admission_scope.py"],
            [".github/workflows/ai-context.yml"],
        ]

        findings = audit(Path("."), live_base="current-main", head="HEAD")

        self.assertEqual(findings, [])
        self.assertEqual(
            changed_paths.call_args_list,
            [
                call(Path("."), BASE, ADMISSION_MERGE),
                call(Path("."), "current-main", "HEAD"),
            ],
        )

    @patch("tools.bpv1.audit_admission_scope._changed_paths")
    def test_forbidden_path_in_evaluated_delta_fails_closed(self, changed_paths) -> None:
        changed_paths.side_effect = [
            ["tools/bpv1/audit_admission_scope.py"],
            ["native_kernel/semantic_core/models.py"],
        ]

        findings = audit(Path("."), live_base="current-main", head="HEAD")

        self.assertEqual(len(findings), 1)
        self.assertIn("forbidden product/runtime path changed", findings[0])

    @patch("tools.bpv1.audit_admission_scope._changed_paths")
    def test_historical_allowlist_check_remains_independent(self, changed_paths) -> None:
        changed_paths.side_effect = [
            ["native_kernel/semantic_core/models.py"],
            [".github/workflows/ai-context.yml"],
        ]

        findings = audit(Path("."), live_base="current-main", head="HEAD")

        self.assertEqual(len(findings), 1)
        self.assertIn("historical admission package touched a path outside its allowlist", findings[0])


if __name__ == "__main__":
    unittest.main()

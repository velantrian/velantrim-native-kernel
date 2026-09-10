"""Regression tests for BPV1 admission live-delta scoping."""
from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import call, patch

from tools.bpv1.audit_admission_scope import (
    ADMISSION_MERGE,
    BASE,
    FORBIDDEN_PREFIXES,
    _changed_paths,
    audit,
)


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

    def test_workflow_triggers_cover_every_forbidden_root_for_pr_and_push(self) -> None:
        workflow = Path(".github/workflows/bpv1-admission.yml").read_text(encoding="utf-8")
        for prefix in FORBIDDEN_PREFIXES:
            pattern = f'- "{prefix}**"'
            self.assertEqual(
                workflow.count(pattern),
                2,
                msg=f"expected PR and push trigger coverage for {prefix}",
            )

    def test_real_git_rename_preserves_forbidden_source_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            self._init_repo(repo)
            forbidden = repo / "native_kernel" / "old.py"
            forbidden.parent.mkdir(parents=True)
            forbidden.write_text("value = 1\n", encoding="utf-8")
            self._git(repo, "add", ".")
            self._git(repo, "commit", "-m", "base")
            base = self._git(repo, "rev-parse", "HEAD").strip()

            self._git(repo, "mv", "native_kernel/old.py", "allowed.py")
            self._git(repo, "commit", "-m", "rename")
            head = self._git(repo, "rev-parse", "HEAD").strip()

            changed = _changed_paths(repo, base, head)
            self.assertIn("native_kernel/old.py", changed)
            self.assertIn("allowed.py", changed)

    def test_real_git_deletion_preserves_forbidden_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            self._init_repo(repo)
            forbidden = repo / "contracts" / "obsolete.json"
            forbidden.parent.mkdir(parents=True)
            forbidden.write_text("{}\n", encoding="utf-8")
            self._git(repo, "add", ".")
            self._git(repo, "commit", "-m", "base")
            base = self._git(repo, "rev-parse", "HEAD").strip()

            forbidden.unlink()
            self._git(repo, "add", "-A")
            self._git(repo, "commit", "-m", "delete")
            head = self._git(repo, "rev-parse", "HEAD").strip()

            self.assertIn("contracts/obsolete.json", _changed_paths(repo, base, head))

    def test_invalid_live_base_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            self._init_repo(repo)
            (repo / "allowed.txt").write_text("ok\n", encoding="utf-8")
            self._git(repo, "add", ".")
            self._git(repo, "commit", "-m", "head")
            with self.assertRaises(RuntimeError):
                _changed_paths(repo, "0" * 40, "HEAD")

    def test_manual_dispatch_boundary_is_single_parent_delta(self) -> None:
        workflow = Path(".github/workflows/bpv1-admission.yml").read_text(encoding="utf-8")
        self.assertIn('live_base="$(git rev-parse HEAD^)"', workflow)

    @staticmethod
    def _git(repo: Path, *args: str) -> str:
        result = subprocess.run(
            ["git", "-C", str(repo), *args],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout

    @classmethod
    def _init_repo(cls, repo: Path) -> None:
        cls._git(repo, "init", "-q")
        cls._git(repo, "config", "user.email", "bpv1-test@example.invalid")
        cls._git(repo, "config", "user.name", "BPV1 Test")


if __name__ == "__main__":
    unittest.main()

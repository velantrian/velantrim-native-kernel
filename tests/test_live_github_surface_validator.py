from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = (
    Path(__file__).parents[1]
    / "tools"
    / "ai_context"
    / "validate_live_github_surface.py"
)
spec = importlib.util.spec_from_file_location("validate_live_github_surface", MODULE_PATH)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


class LiveGitHubSurfaceValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.repo = Path(self.temp.name)
        (self.repo / "docs" / "ai").mkdir(parents=True)
        self._write_surface("Issue", 178)
        self._write_project_state(issue_number=178, issue_state="OPEN")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _write_surface(self, kind: str, number: int) -> None:
        (self.repo / "docs" / "ai" / "CURRENT_STATE.md").write_text(
            "# Current\n\n"
            f"open_review_surface: {kind} #{number}\n",
            encoding="utf-8",
        )

    def _write_project_state(
        self,
        *,
        issue_number: int | None = None,
        issue_state: str = "OPEN",
    ) -> None:
        issues: dict[str, object] = {}
        if issue_number is not None:
            issues[str(issue_number)] = {"state": issue_state}
        (self.repo / "project-state.json").write_text(
            json.dumps(
                {
                    "repository": {
                        "full_name": "velantrian/velantrim-native-kernel"
                    },
                    "issues": issues,
                }
            ),
            encoding="utf-8",
        )

    @staticmethod
    def _open_issue_fetcher(repository: str, kind: str, number: int):
        return {"number": number, "state": "open"}

    def test_current_open_issue_passes(self):
        findings = validator.validate(
            self.repo,
            live_fetcher=self._open_issue_fetcher,
        )
        self.assertEqual([], findings)

    def test_stale_merged_pr_routing_fails(self):
        self._write_surface("PR", 131)

        def merged_pr_fetcher(repository: str, kind: str, number: int):
            self.assertEqual("pull_request", kind)
            self.assertEqual(131, number)
            return {
                "number": 131,
                "state": "closed",
                "merged_at": "2026-09-01T23:35:01Z",
            }

        findings = validator.validate(
            self.repo,
            live_fetcher=merged_pr_fetcher,
        )
        self.assertTrue(
            any(
                finding.path == validator.CURRENT_STATE_PATH
                and "stale current routing" in finding.message
                and "PR #131 is live MERGED, expected OPEN" in finding.message
                for finding in findings
            )
        )

    def test_closed_issue_routing_fails(self):
        def closed_issue_fetcher(repository: str, kind: str, number: int):
            return {"number": number, "state": "closed"}

        findings = validator.validate(
            self.repo,
            live_fetcher=closed_issue_fetcher,
        )
        self.assertTrue(
            any("Issue #178 is live CLOSED, expected OPEN" in f.message for f in findings)
        )

    def test_live_github_unavailable_fails_closed(self):
        def unavailable_fetcher(repository: str, kind: str, number: int):
            raise RuntimeError("network unavailable")

        findings = validator.validate(
            self.repo,
            live_fetcher=unavailable_fetcher,
        )
        self.assertTrue(
            any(
                "live GitHub state UNKNOWN" in finding.message
                and "network unavailable" in finding.message
                for finding in findings
            )
        )

    def test_current_issue_must_exist_in_machine_state(self):
        self._write_project_state(issue_number=None)
        findings = validator.validate(
            self.repo,
            live_fetcher=self._open_issue_fetcher,
        )
        self.assertTrue(
            any("current Issue #178 is missing" in finding.message for finding in findings)
        )

    def test_current_issue_machine_state_must_be_open(self):
        self._write_project_state(issue_number=178, issue_state="CLOSED")
        findings = validator.validate(
            self.repo,
            live_fetcher=self._open_issue_fetcher,
        )
        self.assertTrue(
            any("machine state is 'CLOSED', expected 'OPEN'" in f.message for f in findings)
        )

    def test_live_object_number_mismatch_fails_closed(self):
        def wrong_object_fetcher(repository: str, kind: str, number: int):
            return {"number": 999, "state": "open"}

        findings = validator.validate(
            self.repo,
            live_fetcher=wrong_object_fetcher,
        )
        self.assertTrue(
            any(
                "live GitHub state UNKNOWN" in finding.message
                and "expected #178" in finding.message
                for finding in findings
            )
        )

    def test_duplicate_surface_binding_is_rejected(self):
        path = self.repo / "docs" / "ai" / "CURRENT_STATE.md"
        path.write_text(
            "open_review_surface: Issue #178\n"
            "open_review_surface: Issue #999\n",
            encoding="utf-8",
        )
        findings = validator.validate(
            self.repo,
            live_fetcher=self._open_issue_fetcher,
        )
        self.assertTrue(
            any("expected exactly one machine-readable" in f.message for f in findings)
        )


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "tools" / "ai_context" / "validate_context.py"
spec = importlib.util.spec_from_file_location("validate_context", MODULE_PATH)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)

P4_STATUS = "RESEARCH / P4 PARTIAL ASSERTION CONFORMANCE / NOT PRODUCTION-READY"


class AIContextValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.repo = Path(self.temp.name)
        self._git("init", "-b", "main")
        self._git("config", "user.email", "test@example.com")
        self._git("config", "user.name", "Test")
        self._write_required_files(checkpoint="0" * 40)
        self._git("add", ".")
        self._git("commit", "-m", "initial")
        self.initial_sha = self._git("rev-parse", "HEAD").stdout.strip()
        self._write_current_state(self.initial_sha)
        self._git("add", "docs/ai/CURRENT_STATE.md")
        self._git("commit", "-m", "record checkpoint")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _git(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["git", "-C", str(self.repo), *args],
            check=True,
            capture_output=True,
            text=True,
        )

    def _write(self, rel: str, content: str = "# File\n") -> None:
        path = self.repo / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def _write_current_state(self, checkpoint: str, *, status: str | None = None) -> None:
        current_status = status or P4_STATUS
        self._write(
            "docs/ai/CURRENT_STATE.md",
            "# Current\n\n"
            f"**Last verified public `main`:** `{checkpoint}`  \n"
            f"**Repository status:** `{current_status}`\n\n"
            "NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST\n"
            "Context checkpoint ≠ automatically current main\n"
            "P4 C2 ≠ C3\n",
        )

    def _write_required_files(self, checkpoint: str) -> None:
        for rel in validator.REQUIRED_PATHS:
            self._write(rel)
        self._write("CONTRIBUTING.md")
        self._write("docs/README.md")
        self._write("docs/README.ru.md")
        self._write_current_state(checkpoint)

    def test_valid_context_accepts_ancestor_checkpoint(self) -> None:
        self.assertEqual([], validator.validate(self.repo))

    def test_missing_required_file_is_reported(self) -> None:
        (self.repo / "docs/ai/P4_IMPLEMENTATION_RECORD.md").unlink()
        findings = validator.validate(self.repo)
        self.assertTrue(
            any(f.path == "docs/ai/P4_IMPLEMENTATION_RECORD.md" for f in findings)
        )

    def test_broken_relative_link_is_reported(self) -> None:
        self._write("AGENTS.md", "[missing](docs/ai/NOPE.md)\n")
        findings = validator.validate(self.repo)
        self.assertTrue(any("broken relative link" in f.message for f in findings))

    def test_repository_escape_link_is_reported(self) -> None:
        self._write("AGENTS.md", "[outside](../outside.md)\n")
        findings = validator.validate(self.repo)
        self.assertTrue(any("escapes repository" in f.message for f in findings))

    def test_malformed_checkpoint_is_reported(self) -> None:
        self._write_current_state("abc")
        findings = validator.validate(self.repo)
        self.assertTrue(any("missing exact 40-character" in f.message for f in findings))

    def test_unknown_checkpoint_is_reported(self) -> None:
        self._write_current_state("f" * 40)
        findings = validator.validate(self.repo)
        self.assertTrue(any("checkpoint commit does not exist" in f.message for f in findings))

    def test_stale_pre_p4_statuses_are_rejected(self) -> None:
        for stale in (
            "RESEARCH / DOCUMENTED_ONLY / NOT PRODUCTION-READY",
            "RESEARCH / P1 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY",
            "RESEARCH / P2 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY",
            "RESEARCH / P3 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY",
        ):
            with self.subTest(stale=stale):
                self._write_current_state(self.initial_sha, status=stale)
                findings = validator.validate(self.repo)
                self.assertTrue(
                    any("P4 PARTIAL ASSERTION CONFORMANCE" in f.message for f in findings)
                )

    def test_missing_p4_c2_boundary_is_rejected(self) -> None:
        self._write(
            "docs/ai/CURRENT_STATE.md",
            "# Current\n\n"
            f"**Last verified public `main`:** `{self.initial_sha}`  \n"
            f"**Repository status:** `{P4_STATUS}`\n\n"
            "NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST\n"
            "Context checkpoint ≠ automatically current main\n",
        )
        findings = validator.validate(self.repo)
        self.assertTrue(any("P4 C2 ≠ C3" in f.message for f in findings))


if __name__ == "__main__":
    unittest.main()

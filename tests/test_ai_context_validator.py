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

C5_STATUS = "RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY"


class AIContextValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.repo = Path(self.temp.name)
        self._git("init", "-b", "main")
        self._git("config", "user.email", "test@example.com")
        self._git("config", "user.name", "Test")
        self._write_required_files("0" * 40)
        self._git("add", ".")
        self._git("commit", "-m", "initial")
        self.initial_sha = self._git("rev-parse", "HEAD").stdout.strip()
        self._write_current_state(self.initial_sha)
        self._git("add", "docs/ai/CURRENT_STATE.md")
        self._git("commit", "-m", "checkpoint")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _git(self, *args: str):
        return subprocess.run(["git", "-C", str(self.repo), *args], check=True, capture_output=True, text=True)

    def _write(self, rel: str, content: str = "# File\n") -> None:
        path = self.repo / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def _write_current_state(self, checkpoint: str, *, status: str | None = None, omit: str | None = None) -> None:
        markers = [
            "NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST",
            "historical recovery ≠ clean implementation",
            "research proposal ≠ accepted contract ≠ runtime",
            "C2 ≠ C3 ≠ C4 ≠ C5",
            "C5 BOUNDED REHEARSAL ≠ PRODUCTION READINESS",
            "C5 SYNTHETIC DATA ≠ LIVE USER TRAFFIC",
            "C5 OPERATIONAL VALIDATION ≠ ASSERTION PROMOTION",
            "C5 LOGICAL BACKUP ≠ PHYSICAL DISASTER RECOVERY",
            "ASSERTION EVIDENCE ≠ TRUTH / AUTHENTICITY / PHYSICAL ERASURE",
        ]
        if omit:
            markers.remove(omit)
        self._write(
            "docs/ai/CURRENT_STATE.md",
            "# Current\n\n"
            f"**Verified source checkpoint:** `{checkpoint}`  \n"
            f"**Repository status:** `{status or C5_STATUS}`\n\n"
            + "\n".join(markers) + "\n",
        )

    def _write_required_files(self, checkpoint: str) -> None:
        for rel in validator.REQUIRED_PATHS:
            self._write(rel)
        for rel in validator.LINK_SCAN_PATHS:
            if not (self.repo / rel).exists():
                self._write(rel)
        self._write_current_state(checkpoint)

    def test_valid_context(self):
        self.assertEqual([], validator.validate(self.repo))

    def test_missing_project_state(self):
        (self.repo / "project-state.json").unlink()
        self.assertTrue(any(f.path == "project-state.json" for f in validator.validate(self.repo)))

    def test_missing_evidence_bundle(self):
        (self.repo / "evidence/c5/2026-08-07/manifest.json").unlink()
        self.assertTrue(any("manifest.json" in f.path for f in validator.validate(self.repo)))

    def test_broken_link(self):
        self._write("AGENTS.md", "[missing](docs/ai/NOPE.md)\n")
        self.assertTrue(any("broken relative link" in f.message for f in validator.validate(self.repo)))

    def test_escape_link(self):
        self._write("AGENTS.md", "[outside](../outside.md)\n")
        self.assertTrue(any("escapes repository" in f.message for f in validator.validate(self.repo)))

    def test_malformed_checkpoint(self):
        self._write_current_state("abc")
        self.assertTrue(any("40-character" in f.message for f in validator.validate(self.repo)))

    def test_unknown_checkpoint(self):
        self._write_current_state("f" * 40)
        self.assertTrue(any("checkpoint commit does not exist" in f.message for f in validator.validate(self.repo)))

    def test_each_boundary_is_required(self):
        for marker in validator.REQUIRED_STATUS_MARKERS[1:]:
            with self.subTest(marker=marker):
                self._write_current_state(self.initial_sha, omit=marker)
                self.assertTrue(any(marker in f.message for f in validator.validate(self.repo)))


if __name__ == "__main__":
    unittest.main()

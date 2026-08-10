from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = (
    Path(__file__).parents[1]
    / "tools"
    / "ai_context"
    / "validate_context.py"
)
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

    def _write_current_state(
        self,
        checkpoint: str,
        *,
        status: str | None = None,
        omit: str | None = None,
        append: str = "",
    ) -> None:
        markers = list(validator.REQUIRED_STATUS_MARKERS)
        if status is not None:
            markers[0] = status
        if omit:
            markers.remove(omit)
        self._write(
            "docs/ai/CURRENT_STATE.md",
            "# Current\n\n"
            "```yaml\n"
            f"machine_truth_reconciliation_merge: {checkpoint}\n"
            "```\n\n"
            + "\n".join(markers)
            + "\n"
            + append,
        )

    def _write_blueprint_progress_surface(
        self,
        rel: str,
        *,
        omit: str | None = None,
        append: str = "",
    ) -> None:
        markers = list(validator.BLUEPRINT_PROGRESS_SURFACES[rel])
        if omit:
            markers.remove(omit)
        self._write(
            rel,
            "# Blueprint progress\n\n"
            + "\n".join(markers)
            + "\n"
            + append,
        )

    def _write_blueprint_progress_surfaces(self) -> None:
        for rel in validator.BLUEPRINT_PROGRESS_SURFACES:
            self._write_blueprint_progress_surface(rel)

    def _write_required_files(self, checkpoint: str) -> None:
        for rel in validator.REQUIRED_PATHS:
            self._write(rel)
        for rel in validator.LINK_SCAN_PATHS:
            if not (self.repo / rel).exists():
                self._write(rel)
        self._write_blueprint_progress_surfaces()
        self._write_current_state(checkpoint)

    def test_valid_context(self):
        self.assertEqual([], validator.validate(self.repo))

    def test_missing_project_state(self):
        (self.repo / "project-state.json").unlink()
        self.assertTrue(
            any(
                finding.path == "project-state.json"
                for finding in validator.validate(self.repo)
            )
        )

    def test_missing_project_state_v2_schema(self):
        (self.repo / "contracts/project-state-v2.schema.json").unlink()
        self.assertTrue(
            any(
                finding.path == "contracts/project-state-v2.schema.json"
                for finding in validator.validate(self.repo)
            )
        )

    def test_missing_architecture_refoundation_plan(self):
        (self.repo / "docs/ARCHITECTURE_REFOUNDATION.md").unlink()
        self.assertTrue(
            any(
                finding.path == "docs/ARCHITECTURE_REFOUNDATION.md"
                and "required AI-context file is missing" in finding.message
                for finding in validator.validate(self.repo)
            )
        )

    def test_missing_blueprint_first_adr(self):
        (
            self.repo
            / "docs/adr/0025-blueprint-before-runtime-expansion.md"
        ).unlink()
        self.assertTrue(
            any(
                finding.path
                == "docs/adr/0025-blueprint-before-runtime-expansion.md"
                for finding in validator.validate(self.repo)
            )
        )

    def test_missing_evidence_bundle(self):
        (self.repo / "evidence/c5/2026-08-07/manifest.json").unlink()
        self.assertTrue(
            any(
                "manifest.json" in finding.path
                for finding in validator.validate(self.repo)
            )
        )

    def test_missing_additive_evidence_bundle(self):
        (
            self.repo
            / "evidence/c5/2026-08-08-adr0023/manifest.json"
        ).unlink()
        self.assertTrue(
            any(
                "2026-08-08-adr0023" in finding.path
                for finding in validator.validate(self.repo)
            )
        )

    def test_broken_link(self):
        self._write("AGENTS.md", "[missing](docs/ai/NOPE.md)\n")
        self.assertTrue(
            any(
                "broken relative link" in finding.message
                for finding in validator.validate(self.repo)
            )
        )

    def test_escape_link(self):
        self._write("AGENTS.md", "[outside](../outside.md)\n")
        self.assertTrue(
            any(
                "escapes repository" in finding.message
                for finding in validator.validate(self.repo)
            )
        )

    def test_malformed_checkpoint(self):
        self._write_current_state("abc")
        self.assertTrue(
            any(
                "40-character" in finding.message
                for finding in validator.validate(self.repo)
            )
        )

    def test_unknown_checkpoint(self):
        self._write_current_state("f" * 40)
        self.assertTrue(
            any(
                "checkpoint commit does not exist" in finding.message
                for finding in validator.validate(self.repo)
            )
        )

    def test_each_boundary_is_required(self):
        for marker in validator.REQUIRED_STATUS_MARKERS:
            with self.subTest(marker=marker):
                self._write_current_state(self.initial_sha, omit=marker)
                self.assertTrue(
                    any(
                        marker in finding.message
                        for finding in validator.validate(self.repo)
                    )
                )
                self._write_current_state(self.initial_sha)

    def test_each_forbidden_legacy_marker_is_rejected(self):
        for legacy in validator.FORBIDDEN_STATUS_MARKERS:
            with self.subTest(marker=legacy):
                self._write_current_state(
                    self.initial_sha,
                    append=legacy + "\n",
                )
                self.assertTrue(
                    any(
                        "forbidden legacy current-state marker"
                        in finding.message
                        and legacy in finding.message
                        for finding in validator.validate(self.repo)
                    )
                )
                self._write_current_state(self.initial_sha)

    def test_each_blueprint_progress_surface_is_required(self):
        for rel, markers in validator.BLUEPRINT_PROGRESS_SURFACES.items():
            for marker in markers:
                with self.subTest(path=rel, marker=marker):
                    self._write_blueprint_progress_surface(rel, omit=marker)
                    self.assertTrue(
                        any(
                            finding.path == rel
                            and "required blueprint-progress marker"
                            in finding.message
                            and marker in finding.message
                            for finding in validator.validate(self.repo)
                        )
                    )
                    self._write_blueprint_progress_surface(rel)

    def test_each_forbidden_blueprint_progress_marker_is_rejected(self):
        rel = "docs/ai/README.md"
        for legacy in validator.FORBIDDEN_BLUEPRINT_PROGRESS_MARKERS:
            with self.subTest(marker=legacy):
                self._write_blueprint_progress_surface(
                    rel,
                    append=legacy + "\n",
                )
                self.assertTrue(
                    any(
                        finding.path == rel
                        and "forbidden stale blueprint-progress marker"
                        in finding.message
                        and legacy in finding.message
                        for finding in validator.validate(self.repo)
                    )
                )
                self._write_blueprint_progress_surface(rel)


if __name__ == "__main__":
    unittest.main()

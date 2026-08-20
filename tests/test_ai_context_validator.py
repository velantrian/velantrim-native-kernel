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
        self._write_current_surface(checkpoint=self.initial_sha)
        self._git("add", "docs/ai/CURRENT_STATE.md")
        self._git("commit", "-m", "current checkpoint")

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

    def _surface_text(
        self,
        rel: str,
        *,
        omit: str | None = None,
        append: str = "",
    ) -> str:
        markers = list(validator.CURRENT_SURFACE_MARKERS[rel])
        if omit:
            markers.remove(omit)
        return "# Surface\n\n" + "\n".join(markers) + "\n" + append

    def _write_current_surface(
        self,
        *,
        checkpoint: str,
        omit: str | None = None,
        append: str = "",
    ) -> None:
        text = self._surface_text(
            "docs/ai/CURRENT_STATE.md",
            omit=omit,
            append=append,
        )
        text += f"h11_state_binding_merge: {checkpoint}\n"
        self._write("docs/ai/CURRENT_STATE.md", text)

    def _write_surface(
        self,
        rel: str,
        *,
        omit: str | None = None,
        append: str = "",
    ) -> None:
        if rel == "docs/ai/CURRENT_STATE.md":
            self._write_current_surface(
                checkpoint=getattr(self, "initial_sha", "0" * 40),
                omit=omit,
                append=append,
            )
            return
        self._write(rel, self._surface_text(rel, omit=omit, append=append))

    def _write_required_files(self, checkpoint: str) -> None:
        for rel in validator.REQUIRED_PATHS:
            self._write(rel)
        for rel in validator.LINK_SCAN_PATHS:
            if not (self.repo / rel).exists():
                self._write(rel)
        for rel in validator.CURRENT_SURFACE_MARKERS:
            if rel == "docs/ai/CURRENT_STATE.md":
                self._write_current_surface(checkpoint=checkpoint)
            else:
                self._write_surface(rel)

    def test_valid_context(self):
        self.assertEqual([], validator.validate(self.repo))

    def test_missing_project_state(self):
        (self.repo / "project-state.json").unlink()
        self.assertTrue(any(f.path == "project-state.json" for f in validator.validate(self.repo)))

    def test_missing_project_state_v2_schema(self):
        (self.repo / "contracts/project-state-v2.schema.json").unlink()
        self.assertTrue(
            any(f.path == "contracts/project-state-v2.schema.json" for f in validator.validate(self.repo))
        )

    def test_missing_architecture(self):
        (self.repo / "ARCHITECTURE.md").unlink()
        self.assertTrue(any(f.path == "ARCHITECTURE.md" for f in validator.validate(self.repo)))

    def test_missing_architecture_refoundation_plan(self):
        (self.repo / "docs/ARCHITECTURE_REFOUNDATION.md").unlink()
        self.assertTrue(
            any(f.path == "docs/ARCHITECTURE_REFOUNDATION.md" for f in validator.validate(self.repo))
        )

    def test_missing_blueprint_first_adr(self):
        (self.repo / "docs/adr/0025-blueprint-before-runtime-expansion.md").unlink()
        self.assertTrue(
            any(
                f.path == "docs/adr/0025-blueprint-before-runtime-expansion.md"
                for f in validator.validate(self.repo)
            )
        )

    def test_missing_evidence_bundle(self):
        (self.repo / "evidence/c5/2026-08-07/manifest.json").unlink()
        self.assertTrue(any("2026-08-07" in f.path for f in validator.validate(self.repo)))

    def test_missing_additive_evidence_bundle(self):
        (self.repo / "evidence/c5/2026-08-08-adr0023/manifest.json").unlink()
        self.assertTrue(any("2026-08-08-adr0023" in f.path for f in validator.validate(self.repo)))

    def test_broken_link(self):
        self._write("AGENTS.md", "[missing](docs/ai/NOPE.md)\n")
        self.assertTrue(any("broken relative link" in f.message for f in validator.validate(self.repo)))

    def test_escape_link(self):
        self._write("AGENTS.md", "[outside](../outside.md)\n")
        self.assertTrue(any("escapes repository" in f.message for f in validator.validate(self.repo)))

    def test_malformed_current_checkpoint(self):
        self._write_current_surface(checkpoint="abc")
        self.assertTrue(
            any("40-character H11 state-binding checkpoint" in f.message for f in validator.validate(self.repo))
        )

    def test_unknown_current_checkpoint(self):
        self._write_current_surface(checkpoint="f" * 40)
        self.assertTrue(
            any("checkpoint commit does not exist" in f.message for f in validator.validate(self.repo))
        )

    def test_each_current_marker_is_required(self):
        for rel, markers in validator.CURRENT_SURFACE_MARKERS.items():
            for marker in markers:
                with self.subTest(path=rel, marker=marker):
                    self._write_surface(rel, omit=marker)
                    self.assertTrue(
                        any(
                            f.path == rel
                            and "required current/authority marker" in f.message
                            and marker in f.message
                            for f in validator.validate(self.repo)
                        )
                    )
                    self._write_surface(rel)

    def test_each_stale_current_marker_is_rejected(self):
        for rel, markers in validator.FORBIDDEN_CURRENT_MARKERS.items():
            for marker in markers:
                with self.subTest(path=rel, marker=marker):
                    self._write_surface(rel, append=marker + "\n")
                    self.assertTrue(
                        any(
                            f.path == rel
                            and "stale current-looking marker" in f.message
                            and marker in f.message
                            for f in validator.validate(self.repo)
                        )
                    )
                    self._write_surface(rel)


if __name__ == "__main__":
    unittest.main()

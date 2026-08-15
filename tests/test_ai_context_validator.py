from __future__ import annotations

import importlib.util
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
        self._write_required_files()

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _write(self, rel: str, content: str = "# File\n") -> None:
        path = self.repo / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def _write_surface(self, rel: str, *, omit: str | None = None, append: str = "") -> None:
        markers = list(validator.CURRENT_SURFACE_MARKERS[rel])
        if omit:
            markers.remove(omit)
        self._write(rel, "# Surface\n\n" + "\n".join(markers) + "\n" + append)

    def _write_required_files(self) -> None:
        for rel in validator.REQUIRED_PATHS:
            self._write(rel)
        for rel in validator.LINK_SCAN_PATHS:
            if not (self.repo / rel).exists():
                self._write(rel)
        for rel in validator.CURRENT_SURFACE_MARKERS:
            self._write_surface(rel)

    def test_valid_context(self):
        self.assertEqual([], validator.validate(self.repo))

    def test_missing_project_state(self):
        (self.repo / "project-state.json").unlink()
        self.assertTrue(any(f.path == "project-state.json" for f in validator.validate(self.repo)))

    def test_missing_architecture(self):
        (self.repo / "ARCHITECTURE.md").unlink()
        self.assertTrue(any(f.path == "ARCHITECTURE.md" for f in validator.validate(self.repo)))

    def test_broken_link(self):
        self._write("AGENTS.md", "[missing](docs/ai/NOPE.md)\n")
        self.assertTrue(any("broken relative link" in f.message for f in validator.validate(self.repo)))

    def test_escape_link(self):
        self._write("AGENTS.md", "[outside](../outside.md)\n")
        self.assertTrue(any("escapes repository" in f.message for f in validator.validate(self.repo)))

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

from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "docs" / "validate_bilingual_coverage.py"
spec = importlib.util.spec_from_file_location("validate_bilingual_coverage", MODULE_PATH)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


class BilingualCoverageInventoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.repo = Path(self.temp.name)
        self._git("init", "-q")
        self._write(".gitignore", "docs/ignored.ru.md\n")
        self._write("docs/example.md", "# Example\n")
        self._write("docs/example.ru.md", "# Пример\n")
        self._write(
            "tools/docs/bilingual-pairs-v1.json",
            json.dumps(
                {
                    "protocol": "nk-bilingual-doc-parity/1",
                    "pairs": [{"pair_id": "example", "english": "docs/example.md", "russian": "docs/example.ru.md"}],
                },
                ensure_ascii=False,
            )
            + "\n",
        )
        self._write_manifest()
        self._commit("baseline")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _git(self, *args: str) -> None:
        subprocess.run(["git", "-C", str(self.repo), *args], check=True, capture_output=True)

    def _write(self, relative: str, content: str) -> None:
        path = self.repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def _commit(self, message: str) -> None:
        env = os.environ.copy()
        env.update(
            {
                "GIT_AUTHOR_NAME": "Coverage Test",
                "GIT_AUTHOR_EMAIL": "coverage-test@example.invalid",
                "GIT_COMMITTER_NAME": "Coverage Test",
                "GIT_COMMITTER_EMAIL": "coverage-test@example.invalid",
            }
        )
        subprocess.run(["git", "-C", str(self.repo), "add", "--all"], check=True, env=env, capture_output=True)
        subprocess.run(
            ["git", "-C", str(self.repo), "commit", "-q", "-m", message],
            check=True,
            env=env,
            capture_output=True,
        )

    def _write_manifest(self) -> None:
        manifest = {
            "protocol": validator.PROTOCOL,
            "status": "BOUNDED_COVERAGE_INVENTORY_NOT_TRANSLATION_CERTIFICATION",
            "authority_boundary": {
                "semantic_equivalence_certified": False,
                "legal_equivalence_certified": False,
                "canon_changed": False,
                "runtime_changed": False,
            },
            "counts": {"russian_documents": 1, "validated_by_config": 1, "explicitly_unvalidated": 0},
            "validated": [
                {
                    "path": "docs/example.ru.md",
                    "config": "tools/docs/bilingual-pairs-v1.json",
                    "pair_id": "example",
                }
            ],
            "explicitly_unvalidated": [],
        }
        self._write(
            "tools/docs/bilingual-coverage-v1.json",
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        )

    def test_committed_inventory_matches_manifest(self) -> None:
        validator.validate(self.repo)

    def test_untracked_russian_markdown_is_excluded(self) -> None:
        self._write("docs/untracked.ru.md", "# Untracked\n")
        validator.validate(self.repo)

    def test_ignored_russian_markdown_is_excluded(self) -> None:
        self._write("docs/ignored.ru.md", "# Ignored\n")
        check = subprocess.run(
            ["git", "-C", str(self.repo), "check-ignore", "-q", "docs/ignored.ru.md"],
            check=False,
        )
        self.assertEqual(0, check.returncode, "fixture must really be ignored by Git")
        validator.validate(self.repo)

    def test_staged_but_uncommitted_russian_markdown_is_excluded(self) -> None:
        self._write("docs/staged.ru.md", "# Staged only\n")
        self._git("add", "docs/staged.ru.md")
        validator.validate(self.repo)

    def test_committed_inventory_drift_is_rejected(self) -> None:
        self._write("docs/new.ru.md", "# New committed Russian document\n")
        self._commit("add a tracked Russian document without updating the manifest")
        with self.assertRaisesRegex(validator.CoverageError, "inventory drift"):
            validator.validate(self.repo)

    def test_missing_head_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            empty = Path(directory)
            with self.assertRaisesRegex(validator.CoverageError, "cannot enumerate committed Russian Markdown"):
                validator.committed_russian_documents(empty)


class RepositoryCoverageManifestTests(unittest.TestCase):
    def test_repository_manifest_covers_committed_inventory(self) -> None:
        validator.validate(ROOT)


if __name__ == "__main__":
    unittest.main()

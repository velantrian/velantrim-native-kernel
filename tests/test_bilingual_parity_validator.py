from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "tools" / "docs" / "validate_bilingual_parity.py"
spec = importlib.util.spec_from_file_location("validate_bilingual_parity", MODULE_PATH)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


class BilingualParityValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.repo = Path(self.temp.name)
        self.config = self.repo / "tools/docs/bilingual-pairs-v1.json"
        self.english_path = "docs/example.md"
        self.russian_path = "docs/example.ru.md"
        self.english = (
            "# English title\n\n"
            "**[English](./example.md) · [Русский](./example.ru.md)**\n\n"
            "## Shared section\n\n"
            "SHARED-STATUS\nENGLISH-BOUNDARY\n"
        )
        self.russian = (
            "# Русский заголовок\n\n"
            "**[English](./example.md) · [Русский](./example.ru.md)**\n\n"
            "## Общий раздел\n\n"
            "SHARED-STATUS\nRUSSIAN-BOUNDARY\n"
        )
        self._write(self.english_path, self.english)
        self._write(self.russian_path, self.russian)
        self._write_config()

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _write(self, relative: str, content: str) -> None:
        path = self.repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def _configuration(self) -> dict[str, object]:
        return {
            "protocol": validator.PROTOCOL,
            "pairs": [
                {
                    "pair_id": "example",
                    "english": self.english_path,
                    "russian": self.russian_path,
                    "selectors": ["(./example.md)", "(./example.ru.md)"],
                    "shared_literals": ["SHARED-STATUS"],
                    "english_literals": ["ENGLISH-BOUNDARY"],
                    "russian_literals": ["RUSSIAN-BOUNDARY"],
                    "compare_heading_levels": True,
                    "require_single_h1": True,
                }
            ],
        }

    def _write_config(self, data: dict[str, object] | None = None) -> None:
        self.config.parent.mkdir(parents=True, exist_ok=True)
        self.config.write_text(
            json.dumps(data or self._configuration(), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def _findings(self):
        return validator.validate(self.repo, self.config)

    def test_valid_pair(self):
        self.assertEqual([], self._findings())

    def test_missing_document(self):
        (self.repo / self.russian_path).unlink()
        findings = self._findings()
        self.assertTrue(any(f.path == self.russian_path and "does not exist" in f.message for f in findings))

    def test_missing_selector(self):
        self._write(self.russian_path, self.russian.replace("(./example.ru.md)", "(./wrong.ru.md)"))
        findings = self._findings()
        self.assertTrue(any("missing language selector" in f.message for f in findings))

    def test_missing_shared_literal(self):
        self._write(self.english_path, self.english.replace("SHARED-STATUS", "DRIFTED-STATUS"))
        findings = self._findings()
        self.assertTrue(any("missing shared literal" in f.message for f in findings))

    def test_missing_language_specific_literal(self):
        self._write(self.russian_path, self.russian.replace("RUSSIAN-BOUNDARY", ""))
        findings = self._findings()
        self.assertTrue(any("missing Russian obligation" in f.message for f in findings))

    def test_heading_outline_mismatch(self):
        self._write(self.russian_path, self.russian.replace("## Общий раздел", "### Общий раздел"))
        findings = self._findings()
        self.assertTrue(any("heading-level outlines differ" in f.message for f in findings))

    def test_fenced_code_headings_are_ignored(self):
        self._write(
            self.english_path,
            self.english + "\n```markdown\n### Not a document heading\n```\n",
        )
        self.assertEqual([], self._findings())

    def test_shorter_fence_does_not_close_longer_fence(self):
        self._write(
            self.english_path,
            self.english + "\n````markdown\n```\n### Still inside the long fence\n````\n",
        )
        self.assertEqual([], self._findings())

    def test_fence_with_trailing_text_does_not_close_active_fence(self):
        self._write(
            self.english_path,
            self.english + "\n````markdown\n````still-code\n### Still fenced\n````\n",
        )
        self.assertEqual([], self._findings())

    def test_up_to_three_leading_spaces_are_valid_atx_headings(self):
        self._write(self.english_path, self.english.replace("## Shared section", "   ## Shared section"))
        self._write(self.russian_path, self.russian.replace("## Общий раздел", "   ## Общий раздел"))
        self.assertEqual([], self._findings())

    def test_single_h1_is_enforced(self):
        self._write(self.english_path, self.english + "\n# Second top-level heading\n")
        findings = self._findings()
        self.assertTrue(any("expected exactly one level-1 heading" in f.message for f in findings))

    def test_unsafe_config_path_is_rejected(self):
        data = self._configuration()
        pair = data["pairs"][0]
        assert isinstance(pair, dict)
        pair["english"] = "../outside.md"
        self._write_config(data)
        findings = self._findings()
        self.assertEqual(1, len(findings))
        self.assertEqual("configuration", findings[0].pair_id)
        self.assertIn("repository-relative path", findings[0].message)

    def test_non_posix_config_path_is_rejected(self):
        data = self._configuration()
        pair = data["pairs"][0]
        assert isinstance(pair, dict)
        pair["english"] = "docs\\example.md"
        self._write_config(data)
        findings = self._findings()
        self.assertEqual(1, len(findings))
        self.assertIn("POSIX separators", findings[0].message)

    def test_non_canonical_config_path_is_rejected(self):
        data = self._configuration()
        pair = data["pairs"][0]
        assert isinstance(pair, dict)
        pair["english"] = "docs/./example.md"
        self._write_config(data)
        findings = self._findings()
        self.assertEqual(1, len(findings))
        self.assertIn("canonical repository-relative path", findings[0].message)

    def test_duplicate_document_registration_is_rejected(self):
        data = self._configuration()
        original = data["pairs"][0]
        assert isinstance(original, dict)
        duplicate = dict(original)
        duplicate["pair_id"] = "duplicate"
        data["pairs"].append(duplicate)
        self._write_config(data)
        findings = self._findings()
        self.assertEqual(1, len(findings))
        self.assertIn("more than one pair", findings[0].message)


if __name__ == "__main__":
    unittest.main()

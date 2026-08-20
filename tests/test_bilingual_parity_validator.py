from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "docs" / "validate_bilingual_parity.py"
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
        self.config.write_text(json.dumps(data or self._configuration(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

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
        self.assertTrue(any("missing language selector" in f.message for f in self._findings()))

    def test_missing_shared_literal(self):
        self._write(self.english_path, self.english.replace("SHARED-STATUS", "DRIFTED-STATUS"))
        self.assertTrue(any("missing shared literal" in f.message for f in self._findings()))

    def test_missing_language_specific_literal(self):
        self._write(self.russian_path, self.russian.replace("RUSSIAN-BOUNDARY", ""))
        self.assertTrue(any("missing Russian obligation" in f.message for f in self._findings()))

    def test_heading_outline_mismatch(self):
        self._write(self.russian_path, self.russian.replace("## Общий раздел", "### Общий раздел"))
        self.assertTrue(any("heading-level outlines differ" in f.message for f in self._findings()))

    def test_fenced_code_headings_are_ignored(self):
        self._write(self.english_path, self.english + "\n```markdown\n### Not a document heading\n```\n")
        self.assertEqual([], self._findings())

    def test_shorter_fence_does_not_close_longer_fence(self):
        self._write(self.english_path, self.english + "\n````markdown\n```\n### Still inside the long fence\n````\n")
        self.assertEqual([], self._findings())

    def test_fence_with_trailing_text_does_not_close_active_fence(self):
        self._write(self.english_path, self.english + "\n````markdown\n````still-code\n### Still fenced\n````\n")
        self.assertEqual([], self._findings())

    def test_up_to_three_leading_spaces_are_valid_atx_headings(self):
        self._write(self.english_path, self.english.replace("## Shared section", "   ## Shared section"))
        self._write(self.russian_path, self.russian.replace("## Общий раздел", "   ## Общий раздел"))
        self.assertEqual([], self._findings())

    def test_single_h1_is_enforced(self):
        self._write(self.english_path, self.english + "\n# Second top-level heading\n")
        self.assertTrue(any("expected exactly one level-1 heading" in f.message for f in self._findings()))

    def test_unsafe_config_path_is_rejected(self):
        data = self._configuration(); pair = data["pairs"][0]; assert isinstance(pair, dict); pair["english"] = "../outside.md"
        self._write_config(data)
        findings = self._findings(); self.assertEqual(1, len(findings)); self.assertEqual("configuration", findings[0].pair_id); self.assertIn("repository-relative path", findings[0].message)

    def test_non_posix_config_path_is_rejected(self):
        data = self._configuration(); pair = data["pairs"][0]; assert isinstance(pair, dict); pair["english"] = "docs\\example.md"
        self._write_config(data)
        findings = self._findings(); self.assertEqual(1, len(findings)); self.assertIn("POSIX separators", findings[0].message)

    def test_non_canonical_config_path_is_rejected(self):
        data = self._configuration(); pair = data["pairs"][0]; assert isinstance(pair, dict); pair["english"] = "docs/./example.md"
        self._write_config(data)
        findings = self._findings(); self.assertEqual(1, len(findings)); self.assertIn("canonical repository-relative path", findings[0].message)

    def test_duplicate_document_registration_is_rejected(self):
        data = self._configuration(); original = data["pairs"][0]; assert isinstance(original, dict); duplicate = dict(original); duplicate["pair_id"] = "duplicate"; data["pairs"].append(duplicate)
        self._write_config(data)
        findings = self._findings(); self.assertEqual(1, len(findings)); self.assertIn("more than one pair", findings[0].message)


class CurrentGateLiteralRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.registry_path = ROOT / "tools" / "docs" / "current-gate-pairs-v1.json"
        cls.registry = json.loads(cls.registry_path.read_text(encoding="utf-8"))
        cls.english = (ROOT / "docs" / "README.md").read_text(encoding="utf-8")
        cls.russian = (ROOT / "docs" / "README.ru.md").read_text(encoding="utf-8")
        cls.expected = [
            "POST-BLUEPRINT VALIDATION / A10-H11 SELECTED / EXECUTION ADMISSION BLOCKED / RUNTIME EXPANSION FROZEN",
            "R post-blueprint validation: ACTIVE / H11 EXECUTION ADMISSION BLOCKED",
            "selected family: A10-H11",
            "current gate: A10_H11_EXECUTION_ADMISSION",
            "admission: BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER",
            "reviewer/reproducer: NOT_ESTABLISHED",
            "H11 outcome: NOT_TESTED",
            "H11 implementation/execution: NOT AUTHORIZED",
            "runtime expansion: FROZEN",
            "production: NOT AUTHORIZED",
        ]
        cls.forbidden = [
            "independent architectural validation: NOT ESTABLISHED",
            "next gate: INDEPENDENT_ARCHITECTURE_REVIEW",
            "BPV-1: BLOCKED_PENDING_INDEPENDENT_REVIEW_AND_RECONCILIATION",
            "POST-BLUEPRINT VALIDATION / IAR-1 RECONCILED / BPV1 PLAN NEXT / RUNTIME EXPANSION FROZEN",
            "R post-blueprint validation: ACTIVE / IAR-1-RECONCILED / BPV1-PLAN-NEXT",
            "next gate: BPV1_PLAN_AND_PREREGISTRATION",
            "BPV-1 execution: BLOCKED_PENDING_PREREGISTERED_PLAN",
            "POST-BLUEPRINT VALIDATION / BPV1 PREREGISTERED / EXECUTION ADMISSION NEXT / RUNTIME EXPANSION FROZEN",
            "R post-blueprint validation: ACTIVE / BPV1-PREREGISTERED / EXECUTION-ADMISSION-NEXT",
            "next gate: BPV1_EXECUTION_ADMISSION",
            "BPV-1 execution: BLOCKED_PENDING_EXECUTION_ADMISSION",
            "POST-BLUEPRINT VALIDATION / BPV1 EXECUTION-ADMISSION COMPLETE / SUBJECT-IMPLEMENTATION-NEXT / RUNTIME EXPANSION FROZEN",
            "R post-blueprint validation: ACTIVE / BPV1-EXECUTION-ADMISSION-COMPLETE / SUBJECT-IMPLEMENTATION-NEXT",
            "next gate: BPV1_SUBJECT_IMPLEMENTATION_AND_EXECUTION",
            "BPV1_SUBJECT_IMPLEMENTATION_AND_EXECUTION",
            "next gate: D6_A10_HYPOTHESIS_CLASSIFICATION",
            "D6: NOT_STARTED",
        ]

    def test_docs_index_current_gate_registry_is_exact(self) -> None:
        self.assertEqual("nk-current-gate-doc-parity/1", self.registry["protocol"])
        self.assertEqual(1, len(self.registry["pairs"]))
        pair = self.registry["pairs"][0]
        self.assertEqual("docs-index-current-gate", pair["pair_id"])
        self.assertEqual("docs/README.md", pair["english"])
        self.assertEqual("docs/README.ru.md", pair["russian"])
        self.assertEqual(self.expected, pair["shared_literals"])
        self.assertEqual(self.forbidden, pair["forbidden_current_literals"])

    def test_current_gate_literals_exist_in_both_indexes(self) -> None:
        for literal in self.expected:
            self.assertIn(literal, self.english)
            self.assertIn(literal, self.russian)

    def test_pre_admission_gate_is_forbidden_in_current_indexes(self) -> None:
        for literal in self.forbidden:
            self.assertNotIn(literal, self.english)
            self.assertNotIn(literal, self.russian)


if __name__ == "__main__":
    unittest.main()

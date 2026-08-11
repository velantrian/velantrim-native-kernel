from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "ai_context" / "validate_iar1_independence_evidence.py"
SPEC = importlib.util.spec_from_file_location("validate_iar1_independence_evidence", MODULE_PATH)
module = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)
RECORD = json.loads((ROOT / "docs" / "reviews" / "IAR-1_INDEPENDENCE_EVIDENCE.json").read_text(encoding="utf-8"))


class IAR1IndependenceEvidenceTests(unittest.TestCase):
    def validate(self, record: dict | None = None) -> None:
        module.validate_record(copy.deepcopy(RECORD) if record is None else record)

    def test_repository_evidence_passes(self) -> None:
        self.validate()

    def test_review_actor_cannot_appear_in_contributor_snapshot(self) -> None:
        record = copy.deepcopy(RECORD)
        record["contributors_snapshot"]["logins"].append(record["github_actor_login"])
        with self.assertRaisesRegex(module.IndependenceEvidenceError, "contributors snapshot drift|appears in contributor"):
            self.validate(record)

    def test_review_actor_cannot_appear_in_collaborator_snapshot(self) -> None:
        record = copy.deepcopy(RECORD)
        record["collaborators_snapshot"]["logins"].append(record["github_actor_login"])
        with self.assertRaisesRegex(module.IndependenceEvidenceError, "collaborators snapshot drift|appears in collaborator"):
            self.validate(record)

    def test_sources_are_bound_to_repository_visible_api_surfaces(self) -> None:
        record = copy.deepcopy(RECORD)
        record["contributors_snapshot"]["source"] = "https://example.invalid/contributors"
        with self.assertRaisesRegex(module.IndependenceEvidenceError, "contributors evidence source drift"):
            self.validate(record)

    def test_actor_identity_cannot_drift(self) -> None:
        record = copy.deepcopy(RECORD)
        record["github_actor_login"] = "velantrian"
        with self.assertRaisesRegex(module.IndependenceEvidenceError, "GitHub actor drift"):
            self.validate(record)

    def test_separation_basis_must_bind_exact_actor_and_channel(self) -> None:
        record = copy.deepcopy(RECORD)
        record["separation_basis"] = "This is a long generic explanation. " * 12
        with self.assertRaisesRegex(module.IndependenceEvidenceError, "separation basis missing marker"):
            self.validate(record)

    def test_limitations_must_forbid_overclaim(self) -> None:
        record = copy.deepcopy(RECORD)
        record["limitations"] = ["independent"]
        with self.assertRaisesRegex(module.IndependenceEvidenceError, "limitations required"):
            self.validate(record)


if __name__ == "__main__":
    unittest.main()

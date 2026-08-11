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
INDEPENDENCE = json.loads((ROOT / "docs" / "reviews" / "IAR-1_INDEPENDENCE_EVIDENCE.json").read_text(encoding="utf-8"))
RESULT = json.loads((ROOT / "docs" / "reviews" / "IAR-1_RESULT.json").read_text(encoding="utf-8"))
PACKET = json.loads((ROOT / "docs" / "reviews" / "IAR-1_INPUT_PACKET_EVIDENCE.json").read_text(encoding="utf-8"))


class IAR1IndependenceEvidenceTests(unittest.TestCase):
    def validate(
        self,
        independence: dict | None = None,
        result: dict | None = None,
        packet: dict | None = None,
    ) -> None:
        module.validate_cross_records(
            copy.deepcopy(INDEPENDENCE) if independence is None else independence,
            copy.deepcopy(RESULT) if result is None else result,
            copy.deepcopy(PACKET) if packet is None else packet,
        )

    def test_repository_evidence_passes_at_reviewed_commit(self) -> None:
        module.validate(ROOT)

    def test_review_actor_cannot_appear_in_contributor_snapshot(self) -> None:
        record = copy.deepcopy(INDEPENDENCE)
        record["contributors_snapshot"]["logins"].append(record["github_actor_login"])
        with self.assertRaisesRegex(module.IndependenceEvidenceError, "contributors snapshot drift|appears in contributor"):
            self.validate(independence=record)

    def test_review_actor_cannot_appear_in_collaborator_snapshot(self) -> None:
        record = copy.deepcopy(INDEPENDENCE)
        record["collaborators_snapshot"]["logins"].append(record["github_actor_login"])
        with self.assertRaisesRegex(module.IndependenceEvidenceError, "collaborators snapshot drift|appears in collaborator"):
            self.validate(independence=record)

    def test_sources_are_bound_to_repository_visible_api_surfaces(self) -> None:
        record = copy.deepcopy(INDEPENDENCE)
        record["contributors_snapshot"]["source"] = "https://example.invalid/contributors"
        with self.assertRaisesRegex(module.IndependenceEvidenceError, "contributors evidence source drift"):
            self.validate(independence=record)

    def test_actor_identity_cannot_drift(self) -> None:
        record = copy.deepcopy(INDEPENDENCE)
        record["github_actor_login"] = "velantrian"
        with self.assertRaisesRegex(module.IndependenceEvidenceError, "GitHub actor drift"):
            self.validate(independence=record)

    def test_exact_review_submission_id_cannot_drift(self) -> None:
        record = copy.deepcopy(INDEPENDENCE)
        record["review_submission"]["id"] = 1
        with self.assertRaisesRegex(module.IndependenceEvidenceError, "exact review submission identity drift"):
            self.validate(independence=record)

    def test_exact_review_submission_actor_cannot_drift(self) -> None:
        record = copy.deepcopy(INDEPENDENCE)
        record["review_submission"]["actor_login"] = "velantrian"
        with self.assertRaisesRegex(module.IndependenceEvidenceError, "exact review submission identity drift|actor binding drift"):
            self.validate(independence=record)

    def test_exact_review_submission_commit_cannot_drift(self) -> None:
        record = copy.deepcopy(INDEPENDENCE)
        record["review_submission"]["commit_id"] = "0" * 40
        with self.assertRaisesRegex(module.IndependenceEvidenceError, "exact review submission identity drift"):
            self.validate(independence=record)

    def test_review_submission_digest_cannot_drift(self) -> None:
        record = copy.deepcopy(INDEPENDENCE)
        record["review_submission_identity_sha256"] = "0" * 64
        with self.assertRaisesRegex(module.IndependenceEvidenceError, "recorded review submission identity digest drift"):
            self.validate(independence=record)

    def test_result_review_request_commit_must_match_submission_commit(self) -> None:
        result = copy.deepcopy(RESULT)
        result["review_request_commit"] = "0" * 40
        with self.assertRaisesRegex(module.IndependenceEvidenceError, "review_request_commit must match exact review submission commit"):
            self.validate(result=result)

    def test_source_review_packet_attestation_cannot_drift(self) -> None:
        result = copy.deepcopy(RESULT)
        result["input_packet_read"] = result["input_packet_read"][:-1]
        with self.assertRaisesRegex(module.IndependenceEvidenceError, "source review input-packet attestation drift"):
            self.validate(result=result)

    def test_normalized_exact_packet_inventory_cannot_omit_orientation_file(self) -> None:
        packet = copy.deepcopy(PACKET)
        packet["normalized_exact_paths"].remove("docs/ai/KNOWN_RISKS.md")
        with self.assertRaisesRegex(module.IndependenceEvidenceError, "normalized exact input-packet inventory drift"):
            self.validate(packet=packet)

    def test_packet_request_document_binding_cannot_drift(self) -> None:
        packet = copy.deepcopy(PACKET)
        packet["review_request_document"] = "docs/reviews/WRONG.md"
        with self.assertRaisesRegex(module.IndependenceEvidenceError, "review request document drift"):
            self.validate(packet=packet)

    def test_packet_protocol_document_binding_cannot_drift(self) -> None:
        packet = copy.deepcopy(PACKET)
        packet["review_protocol_document"] = "docs/WRONG_PROTOCOL.md"
        with self.assertRaisesRegex(module.IndependenceEvidenceError, "review protocol document drift"):
            self.validate(packet=packet)

    def test_packet_normalization_must_preserve_source_attestation(self) -> None:
        packet = copy.deepcopy(PACKET)
        packet["source_review_attestation"] = []
        with self.assertRaisesRegex(module.IndependenceEvidenceError, "packet normalization must preserve source review attestation"):
            self.validate(packet=packet)

    def test_packet_must_not_invent_per_file_telemetry(self) -> None:
        packet = copy.deepcopy(PACKET)
        packet["p1_c5_exact_file_telemetry"] = ["contracts/registry.json"]
        with self.assertRaisesRegex(module.IndependenceEvidenceError, "P1-C5 telemetry overclaim"):
            self.validate(packet=packet)

    def test_separation_basis_must_bind_exact_actor_submission_and_channel(self) -> None:
        record = copy.deepcopy(INDEPENDENCE)
        record["separation_basis"] = "This is a long generic explanation. " * 12
        with self.assertRaisesRegex(module.IndependenceEvidenceError, "separation basis missing marker"):
            self.validate(independence=record)

    def test_limitations_must_forbid_overclaim(self) -> None:
        record = copy.deepcopy(INDEPENDENCE)
        record["limitations"] = ["independent"]
        with self.assertRaisesRegex(module.IndependenceEvidenceError, "limitations required"):
            self.validate(independence=record)


if __name__ == "__main__":
    unittest.main()

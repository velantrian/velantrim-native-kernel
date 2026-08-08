from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify_bundle", ROOT / "tools" / "evidence" / "verify_bundle.py")
module = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(module)


class EvidenceBundleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.schema = json.loads(
            (ROOT / "contracts" / "evidence-bundle-v1.schema.json").read_text(
                encoding="utf-8"
            )
        )
        self.manifest = json.loads((ROOT / "evidence" / "c5" / "2026-08-07" / "manifest.json").read_text(encoding="utf-8"))
        self.revalidation_manifest = json.loads(
            (ROOT / "evidence" / "c5" / "2026-08-08-adr0023" / "manifest.json").read_text(
                encoding="utf-8"
            )
        )

    def test_repository_bundle_passes(self) -> None:
        module.validate(copy.deepcopy(self.manifest), repo=ROOT)
        module.validate(copy.deepcopy(self.revalidation_manifest), repo=ROOT)

    def test_v1_schema_declares_the_additive_revalidation_fields(self) -> None:
        properties = self.schema["properties"]
        self.assertIn("evidence_purpose", properties)
        self.assertIn("sqlite_integrity", properties)
        self.assertFalse(self.schema["additionalProperties"])
        self.assertEqual(
            set(properties["sqlite_integrity"]["required"]),
            set(self.revalidation_manifest["sqlite_integrity"]),
        )

    def test_revalidation_requires_safe_linked_sqlite_floor(self) -> None:
        manifest = copy.deepcopy(self.revalidation_manifest)
        manifest["sqlite_integrity"]["minimum_linked_version"] = "3.45.1"
        with self.assertRaisesRegex(module.EvidenceBundleError, "unsafe SQLite evidence floor"):
            module.validate(manifest, repo=ROOT)

    def test_revalidation_cannot_rewrite_historical_bundle(self) -> None:
        manifest = copy.deepcopy(self.revalidation_manifest)
        manifest["sqlite_integrity"]["historical_bundle_rewritten"] = True
        with self.assertRaisesRegex(module.EvidenceBundleError, "rewrite forbidden"):
            module.validate(manifest, repo=ROOT)

    def test_revalidation_requires_identity_bound_associated_runs(self) -> None:
        for run_kind in ("p5_c3", "c4"):
            with self.subTest(run_kind=run_kind):
                manifest = copy.deepcopy(self.revalidation_manifest)
                manifest["checkpoints"][0]["associated_workflow_run_ids"][run_kind] = 1
                with self.assertRaisesRegex(
                    module.EvidenceBundleError,
                    "associated workflow run identity mismatch",
                ):
                    module.validate(manifest, repo=ROOT)

    def test_sqlite_builder_changes_trigger_every_dependent_workflow(self) -> None:
        for workflow in (
            "p5-sqlite-c3.yml",
            "c4-offline-shadow.yml",
            "c5-operational-rehearsal.yml",
        ):
            with self.subTest(workflow=workflow):
                text = (ROOT / ".github" / "workflows" / workflow).read_text(
                    encoding="utf-8"
                )
                self.assertEqual(text.count('"tools/sqlite/**"'), 2)

    def test_digest_drift_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["checkpoints"][0]["artifacts"][0]["sha256"] = "0" * 64
        with self.assertRaisesRegex(module.EvidenceBundleError, "artifact digest mismatch"):
            module.validate(manifest, repo=ROOT)

    def test_checkpoint_commit_drift_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["checkpoints"][1]["head_sha"] = "0" * 40
        with self.assertRaisesRegex(module.EvidenceBundleError, "report commit mismatch"):
            module.validate(manifest, repo=ROOT)

    def test_path_escape_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["checkpoints"][0]["artifacts"][0]["path"] = "../outside.zip"
        with self.assertRaisesRegex(module.EvidenceBundleError, "escapes repository"):
            module.validate(manifest, repo=ROOT)


if __name__ == "__main__":
    unittest.main()

"""Self-tests for the BPV1-001 Rust subject and its evidence bundle.

EXPERIMENTAL_INSTRUMENT_NOT_CANON. These tests exercise the subject through
its own binary and the frozen, unrelated evaluator; they do not let the
subject define its own expected outcomes.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUBJECT_ROOT = ROOT / "experiments" / "bpv1" / "BPV1-001" / "subject"
RESULTS_ROOT = ROOT / "experiments" / "bpv1" / "BPV1-001" / "results"
EVALUATOR = ROOT / "tools" / "bpv1" / "evaluate.py"
FIXTURE_SPEC = ROOT / "experiments" / "bpv1" / "BPV1-001" / "admission" / "fixtures.json"
SOURCE_BOUNDARY = ROOT / "experiments" / "bpv1" / "BPV1-001" / "admission" / "source-boundary.json"

REQUIRED_RUST_CHANNEL = "1.97.1"
# Patterns that would indicate an actual dependency/import, not just an
# observation-schema field name that happens to contain the same words (the
# fixture spec itself requires a `subject.imports_current_native_kernel`
# boolean field reporting that no such import exists).
FORBIDDEN_SOURCE_PATTERNS = (
    "use native_kernel",
    "extern crate native_kernel",
    "use postgres",
    "use sqlx",
    "use rusqlite",
    "use diesel",
    "use tokio_postgres",
)
FORBIDDEN_MANIFEST_SUBSTRINGS = (
    "native_kernel",
    "postgres",
    "sqlx",
    "rusqlite",
    "diesel",
)


def _rust_toolchain_available() -> bool:
    if shutil.which("rustup") is None or shutil.which("cargo") is None:
        return False
    result = subprocess.run(
        ["rustup", "run", REQUIRED_RUST_CHANNEL, "rustc", "--version"],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.returncode == 0


class BPV1SourceBoundaryTests(unittest.TestCase):
    """Static checks that do not require a Rust toolchain."""

    def test_source_boundary_manifest_matches_frozen_plan(self) -> None:
        boundary = json.loads(SOURCE_BOUNDARY.read_text(encoding="utf-8"))
        self.assertEqual("nk-bpv1-source-boundary/1", boundary["protocol"])
        self.assertEqual(REQUIRED_RUST_CHANNEL, boundary["rust_channel"])
        self.assertEqual("EXPERIMENTAL_INSTRUMENT_NOT_CANON", boundary["language_role"])

    def test_cargo_toml_declares_no_forbidden_dependency(self) -> None:
        manifest = (SUBJECT_ROOT / "Cargo.toml").read_text(encoding="utf-8").lower()
        for forbidden in FORBIDDEN_MANIFEST_SUBSTRINGS:
            self.assertNotIn(forbidden, manifest, f"Cargo.toml must not depend on {forbidden}")

    def test_source_files_do_not_reference_forbidden_lineage(self) -> None:
        source_files = sorted((SUBJECT_ROOT / "src").glob("*.rs"))
        self.assertTrue(source_files, "subject must have at least one source file")
        for path in source_files:
            text = path.read_text(encoding="utf-8").lower()
            for forbidden in FORBIDDEN_SOURCE_PATTERNS:
                self.assertNotIn(forbidden, text, f"{path} must not reference {forbidden}")

    def test_subject_root_only_contains_allowed_files(self) -> None:
        allowed_top_level = {"Cargo.toml", "Cargo.lock", "src", "target", "tests"}
        for entry in SUBJECT_ROOT.iterdir():
            self.assertIn(entry.name, allowed_top_level, f"unexpected file in subject root: {entry.name}")

    def test_committed_evidence_bundle_is_present(self) -> None:
        for name in ("observations.json", "evaluation-report.json", "run-metadata.json"):
            self.assertTrue((RESULTS_ROOT / name).is_file(), f"missing evidence file: {name}")

    def test_committed_evaluation_report_records_hard_semantic_failures_as_zero_tolerance(self) -> None:
        report = json.loads((RESULTS_ROOT / "evaluation-report.json").read_text(encoding="utf-8"))
        self.assertIn(report["outcome"], {"SUPPORTED_FOR_SCOPE", "WEAKENED", "REFUTED", "INDETERMINATE", "NOT_TESTED"})
        failing = [f for f in report["fixture_results"] if f["mandatory"] and f["status"] == "FAIL"]
        self.assertEqual([], failing, "committed evidence must not carry an unacknowledged mandatory fixture failure")

    def test_run_metadata_binds_exact_frozen_plan_digest(self) -> None:
        metadata = json.loads((RESULTS_ROOT / "run-metadata.json").read_text(encoding="utf-8"))
        self.assertEqual(
            "7fe8174c604678c6b79d3fdeae83d7c5ab0d2fb15bfe343d41659d05d9496ad0",
            metadata["plan_sha256"],
        )
        self.assertEqual("a538d7f1e28858a88b9ee777ac7d6e05b85943db", metadata["plan_merge"])


@unittest.skipUnless(_rust_toolchain_available(), f"Rust {REQUIRED_RUST_CHANNEL} toolchain not available")
class BPV1SubjectExecutionTests(unittest.TestCase):
    """End-to-end checks that build and run the actual subject binary."""

    @classmethod
    def setUpClass(cls) -> None:
        subprocess.run(
            ["rustup", "run", REQUIRED_RUST_CHANNEL, "cargo", "build", "--release", "--locked"],
            cwd=SUBJECT_ROOT,
            check=True,
        )
        cls.binary = SUBJECT_ROOT / "target" / "release" / "bpv1-001-subject"

    def _run_subject(self, output_path: Path) -> dict:
        subprocess.run([str(self.binary), "--output", str(output_path)], check=True)
        return json.loads(output_path.read_text(encoding="utf-8"))

    def test_subject_produces_well_formed_observations(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "observations.json"
            observations = self._run_subject(output_path)
        self.assertEqual("nk-bpv1-observations/1", observations["protocol"])
        self.assertEqual("BPV1-001-cross-lineage-bounded-accountability-v1", observations["scenario_id"])
        self.assertEqual(
            "7fe8174c604678c6b79d3fdeae83d7c5ab0d2fb15bfe343d41659d05d9496ad0",
            observations["plan_sha256"],
        )
        self.assertEqual(12, len(observations["fixtures"]))
        self.assertEqual(512, observations["workload"]["mutation_count"])

    def test_subject_run_is_deterministic_across_invocations(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            first = self._run_subject(Path(tmp) / "first.json")
            second = self._run_subject(Path(tmp) / "second.json")
        self.assertEqual(first, second, "subject output must be deterministic across runs")

    def test_fresh_run_evaluates_to_no_mandatory_failures(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            observations_path = Path(tmp) / "observations.json"
            self._run_subject(observations_path)
            report_path = Path(tmp) / "evaluation-report.json"
            result = subprocess.run(
                [
                    "python3",
                    str(EVALUATOR),
                    str(observations_path),
                    "--spec",
                    str(FIXTURE_SPEC),
                    "--output",
                    str(report_path),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertEqual(0, result.returncode, result.stderr)
            report = json.loads(report_path.read_text(encoding="utf-8"))
        failing = [f for f in report["fixture_results"] if f["mandatory"] and f["status"] == "FAIL"]
        self.assertEqual([], failing)
        self.assertNotEqual("REFUTED", report["outcome"])

    def test_static_subject_scope_audit_passes(self) -> None:
        import sys

        # Fixed pre-subject base: the exact main this experiment branched
        # from (the D4.5 status/admission checkpoint merge). Matches
        # run-metadata.json's pre_subject_base_main.
        pre_subject_base = "e2deac859c2a56f29b88c54f1da440f3f04734dc"
        if subprocess.run(
            ["git", "-C", str(ROOT), "cat-file", "-e", f"{pre_subject_base}^{{commit}}"],
            capture_output=True,
            check=False,
        ).returncode != 0:
            self.skipTest("pre-subject base commit not present in this checkout's history")
        diff = subprocess.run(
            ["git", "-C", str(ROOT), "diff", "--name-only", f"{pre_subject_base}...HEAD"],
            capture_output=True,
            text=True,
            check=False,
        )
        if not diff.stdout.strip():
            self.skipTest("no commits on top of the pre-subject base yet; audited by CI post-commit")
        sys.path.insert(0, str(ROOT / "tools" / "bpv1"))
        try:
            import audit_scope  # type: ignore

            findings = audit_scope.audit(ROOT, mode="subject", base=pre_subject_base, head="HEAD")
            self.assertEqual([], findings, "; ".join(findings))
        finally:
            sys.path.pop(0)


if __name__ == "__main__":
    unittest.main()

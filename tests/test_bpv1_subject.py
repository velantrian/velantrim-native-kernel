"""Tests for the BPV1-001 subject and D5-R1 external qualification path.

The frozen preregistration, fixture oracle, and evaluator are intentionally not
modified here. The Rust subject emits raw facts; a separate Python qualifier
derives oracle-facing observables without reading fixture expectations.
"""
from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUBJECT_ROOT = ROOT / "experiments" / "bpv1" / "BPV1-001" / "subject"
RESULTS_ROOT = ROOT / "experiments" / "bpv1" / "BPV1-001" / "results"
EVALUATOR = ROOT / "tools" / "bpv1" / "evaluate.py"
QUALIFIER = ROOT / "tools" / "bpv1" / "qualify_observations.py"
FIXTURE_SPEC = ROOT / "experiments" / "bpv1" / "BPV1-001" / "admission" / "fixtures.json"
SOURCE_BOUNDARY = ROOT / "experiments" / "bpv1" / "BPV1-001" / "admission" / "source-boundary.json"
D5_R1_BASE = "a191e9c868c14af34a269dcdfae44406f1013bda"
REQUIRED_RUST_CHANNEL = "1.97.1"

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
STRUCTURAL_ORACLE_FIELDS = {
    "authoritative_per_operation_append_log",
    "exact_replay_required",
    "imports_current_native_kernel",
    "reuses_current_event_envelope",
    "reuses_current_reducer",
    "reuses_current_receipt_shape_as_oracle",
    "uses_current_sql_profile",
}


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


def _load_qualifier_module():
    spec = importlib.util.spec_from_file_location("bpv1_qualify", QUALIFIER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load BPV1 qualifier")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class BPV1SourceBoundaryTests(unittest.TestCase):
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

    def test_historical_d5_bundle_is_preserved(self) -> None:
        for name in ("observations.json", "evaluation-report.json", "run-metadata.json"):
            self.assertTrue((RESULTS_ROOT / name).is_file(), f"historical D5 evidence missing: {name}")

    def test_external_qualifier_does_not_read_frozen_expectations(self) -> None:
        text = QUALIFIER.read_text(encoding="utf-8")
        self.assertNotIn("fixtures.json", text)
        self.assertNotIn("FIXTURE_SPEC", text)
        self.assertNotIn("evaluate.py", text)
        self.assertIn("oracle_fixture_expectations_read", text)

    def test_external_structural_facts_are_derived_from_repository_source(self) -> None:
        qualifier = _load_qualifier_module()
        facts, report = qualifier.derive_structural_facts(ROOT)
        self.assertFalse(facts["authoritative_per_operation_append_log"])
        self.assertFalse(facts["exact_replay_required"])
        self.assertFalse(facts["imports_current_native_kernel"])
        self.assertFalse(facts["reuses_current_event_envelope"])
        self.assertFalse(facts["reuses_current_reducer"])
        self.assertFalse(facts["reuses_current_receipt_shape_as_oracle"])
        self.assertFalse(facts["uses_current_sql_profile"])
        self.assertTrue(report["crash_journal_bounded"])
        self.assertTrue(report["witness_store_bounded"])
        self.assertTrue(report["predecessor_store_bounded"])

    def test_d5_r1_scope_audit_passes_when_history_is_available(self) -> None:
        if subprocess.run(
            ["git", "-C", str(ROOT), "cat-file", "-e", f"{D5_R1_BASE}^{{commit}}"],
            capture_output=True,
            check=False,
        ).returncode != 0:
            self.skipTest("D5-R1 base commit not present in checkout history")
        diff = subprocess.run(
            ["git", "-C", str(ROOT), "diff", "--name-only", f"{D5_R1_BASE}...HEAD"],
            capture_output=True,
            text=True,
            check=False,
        )
        if not diff.stdout.strip():
            self.skipTest("no D5-R1 diff yet")
        result = subprocess.run(
            [
                "python3",
                str(ROOT / "tools" / "bpv1" / "audit_scope.py"),
                "--repo",
                str(ROOT),
                "--mode",
                "qualification",
                "--base",
                D5_R1_BASE,
                "--head",
                "HEAD",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)


@unittest.skipUnless(_rust_toolchain_available(), f"Rust {REQUIRED_RUST_CHANNEL} toolchain not available")
class BPV1SubjectExecutionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        subprocess.run(
            ["rustup", "run", REQUIRED_RUST_CHANNEL, "cargo", "build", "--release", "--locked"],
            cwd=SUBJECT_ROOT,
            check=True,
        )
        subprocess.run(
            ["rustup", "run", REQUIRED_RUST_CHANNEL, "cargo", "test", "--release", "--locked"],
            cwd=SUBJECT_ROOT,
            check=True,
        )
        cls.binary = SUBJECT_ROOT / "target" / "release" / "bpv1-001-subject"

    def _run_raw(self, output_path: Path) -> dict:
        subprocess.run([str(self.binary), "--output", str(output_path)], check=True)
        return json.loads(output_path.read_text(encoding="utf-8"))

    def _qualify(self, raw_path: Path, qualified_path: Path, report_path: Path) -> tuple[dict, dict]:
        subprocess.run(
            [
                "python3",
                str(QUALIFIER),
                str(raw_path),
                "--repo",
                str(ROOT),
                "--output",
                str(qualified_path),
                "--qualification-report",
                str(report_path),
            ],
            check=True,
        )
        return (
            json.loads(qualified_path.read_text(encoding="utf-8")),
            json.loads(report_path.read_text(encoding="utf-8")),
        )

    def test_subject_emits_raw_facts_without_structural_oracle_self_report(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            raw = self._run_raw(Path(tmp) / "raw.json")
        self.assertEqual("nk-bpv1-raw-observations/1", raw["protocol"])
        self.assertEqual("BPV1-001-cross-lineage-bounded-accountability-v1", raw["scenario_id"])
        self.assertEqual(512, raw["workload"]["mutation_count"])
        self.assertNotIn("subject", raw)
        fx11 = raw["fixtures"]["BPV1-FX11-NON-EVENT-HISTORY"]
        self.assertTrue(STRUCTURAL_ORACLE_FIELDS.isdisjoint(fx11))

    def test_external_qualification_produces_frozen_observation_protocol(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            raw_path = Path(tmp) / "raw.json"
            qualified_path = Path(tmp) / "observations.json"
            report_path = Path(tmp) / "qualification.json"
            self._run_raw(raw_path)
            observations, report = self._qualify(raw_path, qualified_path, report_path)
        self.assertEqual("nk-bpv1-observations/1", observations["protocol"])
        self.assertEqual("QUALIFIED", report["status"])
        self.assertFalse(report["subject_self_report_used_for_structural_oracle_fields"])
        self.assertEqual(512, observations["workload"]["mutation_count"])
        self.assertEqual(3, observations["workload"]["checkpoint_count"])
        self.assertLessEqual(observations["workload"]["loss_witness_count"], 32)
        self.assertEqual(STRUCTURAL_ORACLE_FIELDS, set(observations["subject"]))

    def test_raw_and_qualified_runs_are_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            raw1_path = tmp_path / "raw1.json"
            raw2_path = tmp_path / "raw2.json"
            raw1 = self._run_raw(raw1_path)
            raw2 = self._run_raw(raw2_path)
            self.assertEqual(raw1, raw2)
            obs1, rep1 = self._qualify(raw1_path, tmp_path / "obs1.json", tmp_path / "rep1.json")
            obs2, rep2 = self._qualify(raw2_path, tmp_path / "obs2.json", tmp_path / "rep2.json")
            self.assertEqual(obs1, obs2)
            self.assertEqual(rep1, rep2)

    def test_fresh_qualified_run_is_evaluable_by_frozen_oracle(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            raw_path = tmp_path / "raw.json"
            qualified_path = tmp_path / "observations.json"
            qualification_path = tmp_path / "qualification.json"
            report_path = tmp_path / "evaluation.json"
            self._run_raw(raw_path)
            _, qualification = self._qualify(raw_path, qualified_path, qualification_path)
            self.assertEqual("QUALIFIED", qualification["status"])
            result = subprocess.run(
                [
                    "python3",
                    str(EVALUATOR),
                    str(qualified_path),
                    "--spec",
                    str(FIXTURE_SPEC),
                    "--output",
                    str(report_path),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
            report = json.loads(report_path.read_text(encoding="utf-8"))
        self.assertIn(report["outcome"], {"SUPPORTED_FOR_SCOPE", "WEAKENED", "REFUTED", "INDETERMINATE", "NOT_TESTED"})


if __name__ == "__main__":
    unittest.main()

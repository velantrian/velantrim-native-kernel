from __future__ import annotations

import copy
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT_STATE = ROOT / "project-state.json"


def _load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


PROJECT_STATE_VALIDATOR = ROOT / "tools/ai_context/validate_project_state.py"
ARCHITECTURE_FREEZE_VALIDATOR = ROOT / "tools/ai_context/validate_architecture_freeze.py"
QUALIFY_OBSERVATIONS = _load_module(
    ROOT / "tools/bpv1/qualify_observations.py", "qualify_observations_pr_a0"
)


class VerificationPrA0Tests(unittest.TestCase):
    """Read-only probes; expected failures record defects without fixing production code."""

    def _run_cli(self, script: Path, state_path: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(script),
                str(state_path),
                "--repo",
                str(ROOT),
                "--no-git",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def _write_state(self, state: dict) -> Path:
        handle = tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", dir=ROOT, encoding="utf-8", delete=False
        )
        with handle:
            json.dump(state, handle, indent=2)
            handle.write("\n")
        return Path(handle.name)

    @unittest.expectedFailure
    def test_project_state_cli_executes_main_for_valid_state(self) -> None:
        result = self._run_cli(PROJECT_STATE_VALIDATOR, PROJECT_STATE)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("Project-state validation passed", result.stdout)

    @unittest.expectedFailure
    def test_project_state_cli_rejects_production_promotion(self) -> None:
        state = json.loads(PROJECT_STATE.read_text(encoding="utf-8"))
        state["status"]["production_authorized"] = True
        path = self._write_state(state)
        try:
            result = self._run_cli(PROJECT_STATE_VALIDATOR, path)
        finally:
            path.unlink(missing_ok=True)
        self.assertNotEqual(0, result.returncode)
        self.assertIn("production", result.stderr.lower())

    @unittest.expectedFailure
    def test_architecture_freeze_cli_rejects_runtime_thaw(self) -> None:
        state = json.loads(PROJECT_STATE.read_text(encoding="utf-8"))
        state["tracks"]["long_horizon_research"]["architecture_refoundation"][
            "runtime_expansion_frozen"
        ] = False
        path = self._write_state(state)
        try:
            result = self._run_cli(ARCHITECTURE_FREEZE_VALIDATOR, path)
        finally:
            path.unlink(missing_ok=True)
        self.assertNotEqual(0, result.returncode)
        self.assertIn("freeze", result.stderr.lower())

    def test_project_state_validator_executes_git_bound_path(self) -> None:
        module = _load_module(PROJECT_STATE_VALIDATOR, "project_state_pr_a0_git")
        state = json.loads(PROJECT_STATE.read_text(encoding="utf-8"))
        registry = json.loads(
            (ROOT / "contracts/registry.json").read_text(encoding="utf-8")
        )
        # The default validator path is check_git=True. This test deliberately does
        # not use --no-git so the regression suite exercises the repository guards.
        module.validate(state, repo=ROOT, registry=registry, check_git=True)

    def _subject_fixture(self, engine_text: str) -> Path:
        repo = Path(tempfile.mkdtemp(prefix="pr-a0-qualifier-"))
        subject = repo / "experiments/bpv1/BPV1-001/subject"
        (subject / "src").mkdir(parents=True)
        (subject / "Cargo.toml").write_text("[package]\nname = \"fixture\"\n", encoding="utf-8")
        (subject / "src/engine.rs").write_text(engine_text, encoding="utf-8")
        (subject / "src/main.rs").write_text(
            "fn main() { let _ = build_raw_observations; }\n", encoding="utf-8"
        )
        return repo

    @unittest.expectedFailure
    def test_qualifier_ignores_bounds_markers_in_comments(self) -> None:
        engine = """
// CRASH_JOURNAL_MAX_ENTRIES self.crash_journal.len() >= CRASH_JOURNAL_MAX_ENTRIES
// self.crash_journal.pop_front()
// LOSS_WITNESS_MAX_RECORDS fn push_loss_witness fn roll_up_witness loss_witness_rollup
// RETAINED_DETAIL_PER_SLOT while slot.detailed_predecessors.len() > RETAINED_DETAIL_PER_SLOT
// while slot.compacted_summaries.len() > RETAINED_DETAIL_PER_SLOT
"""
        repo = self._subject_fixture(engine)
        try:
            _, report = QUALIFY_OBSERVATIONS.derive_structural_facts(repo)
        finally:
            shutil.rmtree(repo)
        self.assertFalse(report["crash_journal_bounded"])
        self.assertFalse(report["witness_store_bounded"])
        self.assertFalse(report["predecessor_store_bounded"])

    @unittest.expectedFailure
    def test_qualifier_ignores_bounds_markers_in_string_literals(self) -> None:
        engine = """
fn marker_strings() {
    let _ = "CRASH_JOURNAL_MAX_ENTRIES self.crash_journal.len() >= CRASH_JOURNAL_MAX_ENTRIES self.crash_journal.pop_front()";
    let _ = "LOSS_WITNESS_MAX_RECORDS fn push_loss_witness fn roll_up_witness loss_witness_rollup";
    let _ = "RETAINED_DETAIL_PER_SLOT while slot.detailed_predecessors.len() > RETAINED_DETAIL_PER_SLOT while slot.compacted_summaries.len() > RETAINED_DETAIL_PER_SLOT";
}
"""
        repo = self._subject_fixture(engine)
        try:
            _, report = QUALIFY_OBSERVATIONS.derive_structural_facts(repo)
        finally:
            shutil.rmtree(repo)
        self.assertFalse(report["crash_journal_bounded"])
        self.assertFalse(report["witness_store_bounded"])
        self.assertFalse(report["predecessor_store_bounded"])

    def test_qualifier_accepts_real_bounds_markers(self) -> None:
        engine = """
const CRASH_JOURNAL_MAX_ENTRIES: usize = 8;
const LOSS_WITNESS_MAX_RECORDS: usize = 8;
const RETAINED_DETAIL_PER_SLOT: usize = 2;
struct Engine { crash_journal: Vec<u8> }
fn push_loss_witness() {}
fn roll_up_witness() {}
fn loss_witness_rollup() {}
fn bounded(&mut self, slot: &mut Slot) {
    if self.crash_journal.len() >= CRASH_JOURNAL_MAX_ENTRIES { self.crash_journal.pop_front(); }
    while slot.detailed_predecessors.len() > RETAINED_DETAIL_PER_SLOT { slot.detailed_predecessors.pop(); }
    while slot.compacted_summaries.len() > RETAINED_DETAIL_PER_SLOT { slot.compacted_summaries.pop(); }
}
struct Slot { detailed_predecessors: Vec<u8>, compacted_summaries: Vec<u8> }
"""
        repo = self._subject_fixture(engine)
        try:
            _, report = QUALIFY_OBSERVATIONS.derive_structural_facts(repo)
        finally:
            shutil.rmtree(repo)
        self.assertTrue(report["crash_journal_bounded"])
        self.assertTrue(report["witness_store_bounded"])
        self.assertTrue(report["predecessor_store_bounded"])


if __name__ == "__main__":
    unittest.main()

"""Executable fail-closed guards for composed validator CLIs and BPV1 stripping.

Importing ``validate()`` directly is not sufficient coverage. The historical
validator wrappers used to compose layers with ``exec(compile(...))`` in shared
globals while temporarily rebinding ``__name__``. That mechanism once allowed
a nested layer to clobber the outer module name, silently preventing the CLI
``main()`` guard from executing.

The wrappers now load preserved layers through isolated ``runpy.run_path``
namespaces and copy the established non-dunder compatibility surface. These
tests drive every CLI as a subprocess, forbid the old shared-source execution
mechanism from returning, and assert that forbidden machine states still fail
closed. They also pin BPV1 structural checks to stripped source so
comment/string/char markers cannot satisfy bounded-store claims.

This is the canonical PR-A1 regression surface (successor of
``tests/test_verification_pr_a0.py``). It asserts executable mechanics only.
It does not establish an independent reviewer/reproducer, change
``A10_H11_EXECUTION_ADMISSION``, execute H11, thaw runtime, promote Final
Canon, or authorize production.
"""

from __future__ import annotations

import ast
import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AI_CONTEXT = ROOT / "tools" / "ai_context"
BPV1_PLAN = ROOT / "docs" / "research" / "BPV1_PREREGISTRATION.json"
FROZEN_BPV1_PLAN_SHA256 = "7fe8174c604678c6b79d3fdeae83d7c5ab0d2fb15bfe343d41659d05d9496ad0"

#: Every layer of the composed chains, including the documented entrypoints.
COMPOSED_VALIDATORS = (
    "validate_project_state.py",
    "validate_project_state_post_adr0027.py",
    "validate_project_state_d8.py",
    "validate_project_state_history.py",
    "validate_architecture_freeze.py",
    "validate_architecture_freeze_post_adr0027.py",
    "validate_architecture_freeze_d8.py",
    "validate_architecture_freeze_history.py",
    "validate_reconciliation.py",
    "validate_reconciliation_d8.py",
    "validate_reconciliation_history.py",
)

#: The eight compatibility wrappers that compose a preserved predecessor layer.
COMPOSED_WRAPPERS = (
    "validate_project_state.py",
    "validate_project_state_post_adr0027.py",
    "validate_project_state_d8.py",
    "validate_architecture_freeze.py",
    "validate_architecture_freeze_post_adr0027.py",
    "validate_architecture_freeze_d8.py",
    "validate_reconciliation.py",
    "validate_reconciliation_d8.py",
)

#: Checkpoint SHA that is well-formed but cannot exist as a commit.
ABSENT_COMMIT_SHA = "0" * 39 + "1"

GENUINE_STRUCTURAL_FACTS = {
    "authoritative_per_operation_append_log": False,
    "exact_replay_required": False,
    "imports_current_native_kernel": False,
    "reuses_current_event_envelope": False,
    "reuses_current_reducer": False,
    "reuses_current_receipt_shape_as_oracle": False,
    "uses_current_sql_profile": False,
}


def _run(script: str, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(AI_CONTEXT / script), *args],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )


def _repository_is_shallow() -> bool:
    result = subprocess.run(
        ["git", "rev-parse", "--is-shallow-repository"],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    return result.returncode != 0 or result.stdout.strip() != "false"


def _load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


QUALIFY_OBSERVATIONS = _load_module(
    ROOT / "tools/bpv1/qualify_observations.py", "qualify_observations_pr_a1"
)
ARCHITECTURE_FREEZE = _load_module(
    AI_CONTEXT / "validate_architecture_freeze.py",
    "validate_architecture_freeze_pr185_compatibility",
)


class ValidatorCLIReachabilityTests(unittest.TestCase):
    """Every composed layer must still reach its own ``main()``."""

    def test_every_composed_layer_reaches_main(self) -> None:
        for script in COMPOSED_VALIDATORS:
            with self.subTest(script=script):
                result = _run(script, "--help")
                self.assertEqual(
                    result.returncode,
                    0,
                    f"{script} --help exited {result.returncode}: {result.stderr}",
                )
                self.assertTrue(
                    result.stdout.startswith("usage:"),
                    f"{script} did not reach main(); stdout={result.stdout!r}",
                )

    def test_composed_layers_do_not_exec_source_into_shared_globals(self) -> None:
        """The prior exec/__name__ composition defect class must stay removed."""
        for script in COMPOSED_VALIDATORS:
            with self.subTest(script=script):
                text = (AI_CONTEXT / script).read_text(encoding="utf-8")
                tree = ast.parse(text, filename=script)
                exec_calls = [
                    node
                    for node in ast.walk(tree)
                    if isinstance(node, ast.Call)
                    and isinstance(node.func, ast.Name)
                    and node.func.id == "exec"
                ]
                self.assertEqual([], exec_calls, f"{script} reintroduced an exec() call")
                self.assertNotIn('globals()["__name__"]', text)
                self.assertNotIn("globals()['__name__']", text)

    def test_wrappers_use_isolated_runpy_composition(self) -> None:
        for script in COMPOSED_WRAPPERS:
            with self.subTest(script=script):
                text = (AI_CONTEXT / script).read_text(encoding="utf-8")
                self.assertIn("runpy.run_path", text)
                self.assertIn("run_name=", text)


class ArchitectureCompatibilityBoundaryTests(unittest.TestCase):
    """PR185-1: compatibility must not become a hidden shared-global channel."""

    def test_compatibility_allowlist_is_exact(self) -> None:
        self.assertEqual(
            (
                "INTEGRATED_REVIEW_DOCS",
                "INDEPENDENT_REVIEW_DOCS",
                "IAR1_RESULT_JSON",
                "_load_json_record",
            ),
            ARCHITECTURE_FREEZE._LEGACY_REBIND_COMPATIBILITY,
        )
        self.assertNotIn("validate", ARCHITECTURE_FREEZE._LEGACY_REBIND_COMPATIBILITY)
        self.assertNotIn(
            "_sync_composed_layer_globals",
            ARCHITECTURE_FREEZE._LEGACY_REBIND_COMPATIBILITY,
        )

    def test_new_current_symbol_is_not_propagated_to_predecessors(self) -> None:
        namespaces = ARCHITECTURE_FREEZE._composed_predecessor_namespaces()
        probe_name = "PR185_NEW_CURRENT_ONLY_SYMBOL"
        probe = object()
        setattr(ARCHITECTURE_FREEZE, probe_name, probe)
        try:
            ARCHITECTURE_FREEZE._sync_composed_layer_globals()
            for namespace in namespaces:
                self.assertNotIn(
                    probe_name,
                    namespace,
                    "new current-only symbol leaked into a predecessor namespace",
                )
        finally:
            delattr(ARCHITECTURE_FREEZE, probe_name)

    def test_predecessor_validate_bindings_keep_identity(self) -> None:
        namespaces = ARCHITECTURE_FREEZE._composed_predecessor_namespaces()
        before = [namespace.get("validate") for namespace in namespaces]
        self.assertTrue(all(callable(value) for value in before))

        ARCHITECTURE_FREEZE._sync_composed_layer_globals()

        after = [namespace.get("validate") for namespace in namespaces]
        for index, (original, observed) in enumerate(zip(before, after, strict=True)):
            self.assertIs(
                original,
                observed,
                f"predecessor namespace {index} validate binding was overwritten",
            )
            self.assertIsNot(
                ARCHITECTURE_FREEZE.validate,
                observed,
                f"predecessor namespace {index} resolved current validate",
            )

    def test_allowlisted_rebinding_reaches_existing_historical_symbol_only(self) -> None:
        namespaces = ARCHITECTURE_FREEZE._composed_predecessor_namespaces()
        original = ARCHITECTURE_FREEZE._load_json_record

        def fake_load(*args, **kwargs):
            return original(*args, **kwargs)

        ARCHITECTURE_FREEZE._load_json_record = fake_load
        try:
            ARCHITECTURE_FREEZE._sync_composed_layer_globals()
            touched = 0
            for namespace in namespaces:
                if "_load_json_record" in namespace:
                    touched += 1
                    self.assertIs(fake_load, namespace["_load_json_record"])
            self.assertGreater(touched, 0)
        finally:
            ARCHITECTURE_FREEZE._load_json_record = original
            ARCHITECTURE_FREEZE._sync_composed_layer_globals()


class ValidatorCLIFailClosedTests(unittest.TestCase):
    """A forbidden machine state must make the CLI exit non-zero."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.state = json.loads((ROOT / "project-state.json").read_text(encoding="utf-8"))

    def _write_state(self, mutate) -> Path:
        state = json.loads(json.dumps(self.state))
        mutate(state)
        handle = tempfile.NamedTemporaryFile(
            "w", suffix=".json", delete=False, encoding="utf-8"
        )
        with handle:
            json.dump(state, handle, ensure_ascii=False, indent=2)
        path = Path(handle.name)
        self.addCleanup(path.unlink, missing_ok=True)
        return path

    def test_repository_state_passes_and_reports(self) -> None:
        for script, marker in (
            ("validate_project_state.py", "Project-state validation passed"),
            ("validate_architecture_freeze.py", "Architecture validation passed"),
            ("validate_reconciliation.py", "Reconciliation validation passed"),
        ):
            with self.subTest(script=script):
                result = _run(script, "--repo", str(ROOT))
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn(marker, result.stdout)

    def test_production_authorization_fails_closed(self) -> None:
        def mutate(state: dict) -> None:
            state["status"]["production_authorized"] = True

        path = self._write_state(mutate)
        for script in ("validate_project_state.py", "validate_architecture_freeze.py"):
            with self.subTest(script=script):
                result = _run(script, str(path), "--repo", str(ROOT))
                combined = (result.stdout + result.stderr).lower()
                self.assertNotEqual(
                    result.returncode,
                    0,
                    f"{script} accepted production_authorized=true: {result.stdout}",
                )
                self.assertIn(
                    "production",
                    combined,
                    f"{script} rejected the state but did not identify the production boundary",
                )

    def test_runtime_thaw_fails_closed(self) -> None:
        def mutate(state: dict) -> None:
            research = state["tracks"]["long_horizon_research"]
            research["architecture_refoundation"]["runtime_expansion_frozen"] = False

        path = self._write_state(mutate)
        result = _run("validate_architecture_freeze.py", str(path), "--repo", str(ROOT))
        combined = (result.stdout + result.stderr).lower()
        self.assertNotEqual(
            result.returncode, 0, f"architecture freeze accepted a thaw: {result.stdout}"
        )
        self.assertIn(
            "freeze",
            combined,
            "architecture freeze rejected the state but did not identify the freeze boundary",
        )


class ValidatorGitBoundCheckpointTests(unittest.TestCase):
    """The git-bound checkpoint guards must actually execute somewhere.

    ``tests/test_project_state.py`` calls ``validate(..., check_git=False)``, so
    without this test no path exercises commit existence or ancestry at all.
    """

    def setUp(self) -> None:
        if _repository_is_shallow():
            self.skipTest(
                "git-bound checkpoint validation requires full history "
                "(CI checks out with fetch-depth: 0)"
            )
        state = json.loads((ROOT / "project-state.json").read_text(encoding="utf-8"))
        state["checkpoints"]["runtime_checkpoint_sha"] = ABSENT_COMMIT_SHA
        handle = tempfile.NamedTemporaryFile(
            "w", suffix=".json", delete=False, encoding="utf-8"
        )
        with handle:
            json.dump(state, handle, ensure_ascii=False, indent=2)
        self.path = Path(handle.name)
        self.addCleanup(self.path.unlink, missing_ok=True)

    def test_absent_checkpoint_commit_is_rejected_with_git(self) -> None:
        result = _run("validate_project_state.py", str(self.path), "--repo", str(ROOT))
        self.assertNotEqual(
            result.returncode,
            0,
            "a fabricated checkpoint SHA passed git-bound validation",
        )
        self.assertIn("runtime_checkpoint_sha commit does not exist", result.stderr)

    def test_absent_checkpoint_commit_is_only_caught_by_the_git_path(self) -> None:
        """Proves the previous test exercises git, not some earlier structural pin."""
        result = _run(
            "validate_project_state.py", str(self.path), "--repo", str(ROOT), "--no-git"
        )
        self.assertEqual(result.returncode, 0, result.stderr)


class BPV1StructuralStripTests(unittest.TestCase):
    """Bounded-store markers in comments/strings must not count as implementation."""

    def _subject_fixture(self, engine_text: str) -> Path:
        repo = Path(tempfile.mkdtemp(prefix="pr-a1-qualifier-"))
        subject = repo / "experiments/bpv1/BPV1-001/subject"
        (subject / "src").mkdir(parents=True)
        (subject / "Cargo.toml").write_text("[package]\nname = \"fixture\"\n", encoding="utf-8")
        (subject / "src/engine.rs").write_text(engine_text, encoding="utf-8")
        (subject / "src/main.rs").write_text(
            "fn main() { let _ = build_raw_observations; }\n", encoding="utf-8"
        )
        return repo

    def _assert_unbounded(self, engine_text: str) -> None:
        repo = self._subject_fixture(engine_text)
        try:
            _, report = QUALIFY_OBSERVATIONS.derive_structural_facts(repo)
        finally:
            shutil.rmtree(repo)
        self.assertFalse(report["crash_journal_bounded"])
        self.assertFalse(report["witness_store_bounded"])
        self.assertFalse(report["predecessor_store_bounded"])

    def test_qualifier_ignores_bounds_markers_in_line_comments(self) -> None:
        engine = """
// CRASH_JOURNAL_MAX_ENTRIES self.crash_journal.len() >= CRASH_JOURNAL_MAX_ENTRIES
// self.crash_journal.pop_front()
// LOSS_WITNESS_MAX_RECORDS fn push_loss_witness fn roll_up_witness loss_witness_rollup
// RETAINED_DETAIL_PER_SLOT while slot.detailed_predecessors.len() > RETAINED_DETAIL_PER_SLOT
// while slot.compacted_summaries.len() > RETAINED_DETAIL_PER_SLOT
"""
        self._assert_unbounded(engine)

    def test_qualifier_ignores_bounds_markers_in_block_comments(self) -> None:
        engine = """
/* CRASH_JOURNAL_MAX_ENTRIES self.crash_journal.len() >= CRASH_JOURNAL_MAX_ENTRIES
   self.crash_journal.pop_front()
   LOSS_WITNESS_MAX_RECORDS fn push_loss_witness fn roll_up_witness loss_witness_rollup
   RETAINED_DETAIL_PER_SLOT while slot.detailed_predecessors.len() > RETAINED_DETAIL_PER_SLOT
   while slot.compacted_summaries.len() > RETAINED_DETAIL_PER_SLOT */
"""
        self._assert_unbounded(engine)

    def test_qualifier_ignores_bounds_markers_in_string_literals(self) -> None:
        engine = """
fn marker_strings() {
    let _ = "CRASH_JOURNAL_MAX_ENTRIES self.crash_journal.len() >= CRASH_JOURNAL_MAX_ENTRIES self.crash_journal.pop_front()";
    let _ = "LOSS_WITNESS_MAX_RECORDS fn push_loss_witness fn roll_up_witness loss_witness_rollup";
    let _ = "RETAINED_DETAIL_PER_SLOT while slot.detailed_predecessors.len() > RETAINED_DETAIL_PER_SLOT while slot.compacted_summaries.len() > RETAINED_DETAIL_PER_SLOT";
}
"""
        self._assert_unbounded(engine)

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

    def test_genuine_subject_facts_remain_stable_after_stripped_matching(self) -> None:
        """Legitimate implementation: derived facts stay the established set."""
        facts, report = QUALIFY_OBSERVATIONS.derive_structural_facts(ROOT)
        self.assertEqual(GENUINE_STRUCTURAL_FACTS, facts)
        self.assertTrue(report["crash_journal_bounded"])
        self.assertTrue(report["witness_store_bounded"])
        self.assertTrue(report["predecessor_store_bounded"])

    def test_frozen_bpv1_plan_digest_is_unchanged(self) -> None:
        digest = hashlib.sha256(BPV1_PLAN.read_bytes()).hexdigest()
        self.assertEqual(FROZEN_BPV1_PLAN_SHA256, digest)


if __name__ == "__main__":
    unittest.main()

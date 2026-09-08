"""Executable fail-closed guards for the composed validator CLI entrypoints.

Importing ``validate()`` directly is not sufficient coverage. The historical
validator layers are composed with ``exec(compile(...))`` into shared globals
and temporarily rebind ``__name__``. If two layers reuse the same restore
variable, the outermost module ends with a non-``__main__`` name, its
``if __name__ == "__main__"`` guard never fires, and the CLI exits ``0``
without validating anything. Both ``ai-context.yml`` steps and the manual
verification commands documented in ``README.md``, ``AGENTS.md`` and
``docs/ai/README.md`` would then be silently dead.

These tests therefore drive the CLIs as subprocesses and assert that a valid
state reports and exits ``0`` while a forbidden state exits non-zero.

They assert executable mechanics only. They do not establish an independent
reviewer/reproducer, change ``A10_H11_EXECUTION_ADMISSION``, execute H11, thaw
runtime, promote Final Canon, or authorize production.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AI_CONTEXT = ROOT / "tools" / "ai_context"

#: Every layer of the composed chains, including the documented entrypoints.
#: A reintroduced ``__name__`` collision in any layer removes its ``main()``.
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

#: Checkpoint SHA that is well-formed but cannot exist as a commit.
ABSENT_COMMIT_SHA = "0" * 39 + "1"


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
                    f"{script} did not reach main(); "
                    f"a composed layer probably clobbered the restored __name__. "
                    f"stdout={result.stdout!r}",
                )

    def test_composed_layers_use_distinct_module_name_restore_variables(self) -> None:
        """Two layers sharing one restore variable is the exact prior defect."""
        seen: dict[str, str] = {}
        for script in COMPOSED_VALIDATORS:
            text = (AI_CONTEXT / script).read_text(encoding="utf-8")
            for line in text.splitlines():
                stripped = line.strip()
                if "= __name__" not in stripped and "=__name__" not in stripped:
                    continue
                if stripped.startswith("globals()"):
                    continue
                variable = stripped.split("=", 1)[0].strip()
                if not variable.startswith("_"):
                    continue
                previous = seen.get(variable)
                self.assertIsNone(
                    previous,
                    f"{script} reuses restore variable {variable!r} already used by "
                    f"{previous}; a nested layer would clobber the outer saved __name__",
                )
                seen[variable] = script


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
                self.assertNotEqual(
                    result.returncode,
                    0,
                    f"{script} accepted production_authorized=true: {result.stdout}",
                )

    def test_runtime_thaw_fails_closed(self) -> None:
        def mutate(state: dict) -> None:
            research = state["tracks"]["long_horizon_research"]
            research["architecture_refoundation"]["runtime_expansion_frozen"] = False

        path = self._write_state(mutate)
        result = _run("validate_architecture_freeze.py", str(path), "--repo", str(ROOT))
        self.assertNotEqual(
            result.returncode, 0, f"architecture freeze accepted a thaw: {result.stdout}"
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


if __name__ == "__main__":
    unittest.main()

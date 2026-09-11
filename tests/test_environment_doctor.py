"""Host-independent tests for the read-only environment doctor."""
from __future__ import annotations

import io
import os
import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.environment_doctor import (
    EnvironmentProbe,
    GitProbe,
    VALIDATED_PYTHON_MINOR_VERSIONS,
    collect_probe,
    diagnose,
    main,
    read_pinned_rust_channel,
)

ROOT = Path(__file__).resolve().parents[1]


def _probe(**overrides: object) -> EnvironmentProbe:
    values: dict[str, object] = {
        "python_version": (3, 12, 3),
        "python_executable": "/usr/bin/python3.12",
        "sqlite_version": "3.51.3",
        "git": GitProbe(
            git_available=True,
            is_repository=True,
            is_shallow=False,
            head="e6fd577b75b567d63a2d9364cf3ec10887ad901f",
        ),
        "postgres_dsn": "postgresql://postgres:postgres@127.0.0.1:5432/native_kernel_test",
        "psycopg_importable": True,
        "rustup_path": "/usr/bin/rustup",
        "cargo_path": "/usr/bin/cargo",
        "pinned_rust_channel": "1.97.1",
        "rust_channel_available": True,
        "rustc_version": "rustc 1.97.1",
        "rust_error": None,
    }
    values.update(overrides)
    return EnvironmentProbe(**values)  # type: ignore[arg-type]


class EnvironmentDoctorDiagnosisTests(unittest.TestCase):
    def test_validated_python_minors_match_ci_matrix(self) -> None:
        self.assertEqual(VALIDATED_PYTHON_MINOR_VERSIONS, ((3, 11), (3, 12)))

    def test_sqlite_below_minimum_is_optional_gap_not_core_failure(self) -> None:
        diagnosis = diagnose(_probe(sqlite_version="3.45.1"))
        self.assertTrue(diagnosis.core.ready)
        self.assertFalse(diagnosis.sqlite_integration.ready)
        self.assertIn("3.45.1", diagnosis.sqlite_integration.detail)
        self.assertFalse(diagnosis.full_suite.ready)

    def test_sqlite_at_minimum_is_integration_ready(self) -> None:
        diagnosis = diagnose(_probe(sqlite_version="3.51.3"))
        self.assertTrue(diagnosis.sqlite_integration.ready)

    def test_sqlite_above_minimum_is_integration_ready(self) -> None:
        diagnosis = diagnose(_probe(sqlite_version="3.52.0"))
        self.assertTrue(diagnosis.sqlite_integration.ready)

    def test_shallow_git_keeps_core_ready_and_marks_history_incomplete(self) -> None:
        diagnosis = diagnose(
            _probe(
                git=GitProbe(
                    git_available=True,
                    is_repository=True,
                    is_shallow=True,
                    head="abc123",
                )
            )
        )
        self.assertTrue(diagnosis.core.ready)
        self.assertFalse(diagnosis.git_history.ready)
        self.assertIn("shallow", diagnosis.git_history.detail)

    def test_full_git_history_is_complete(self) -> None:
        diagnosis = diagnose(_probe())
        self.assertTrue(diagnosis.git_history.ready)
        self.assertTrue(diagnosis.full_suite.ready)

    def test_absent_postgres_dsn_is_optional_gap(self) -> None:
        diagnosis = diagnose(_probe(postgres_dsn=None, psycopg_importable=False))
        self.assertTrue(diagnosis.core.ready)
        self.assertFalse(diagnosis.postgres_integration.ready)
        self.assertIn("absent", diagnosis.postgres_integration.detail)

    def test_absent_rust_is_optional_gap(self) -> None:
        diagnosis = diagnose(
            _probe(
                rustup_path=None,
                cargo_path=None,
                rust_channel_available=False,
                rustc_version=None,
                rust_error="missing rustup, cargo",
            )
        )
        self.assertTrue(diagnosis.core.ready)
        self.assertFalse(diagnosis.bpv1_execution.ready)

    def test_unvalidated_python_fails_core(self) -> None:
        diagnosis = diagnose(_probe(python_version=(3, 13, 0)))
        self.assertFalse(diagnosis.core.ready)
        self.assertFalse(diagnosis.full_suite.ready)


class EnvironmentDoctorCliTests(unittest.TestCase):
    def test_default_exit_zero_is_explicitly_core_only_when_sqlite_is_unsafe(self) -> None:
        diagnosis = diagnose(_probe(sqlite_version="3.45.1"))
        with patch("tools.environment_doctor.collect_probe", return_value=_probe(sqlite_version="3.45.1")):
            with patch("tools.environment_doctor.diagnose", return_value=diagnosis):
                with patch("sys.stdout", new_callable=io.StringIO) as stdout:
                    code = main(["--repo", str(ROOT)])
        output = stdout.getvalue()
        self.assertEqual(code, 0)
        self.assertIn("DEFAULT_EXIT_SCOPE: CORE_ONLY", output)
        self.assertIn("SQLITE_INTEGRATION: NOT_READY", output)
        self.assertIn("CORE READY does not authorize SQLite/WAL integration", output)

    def test_strict_exit_nonzero_when_sqlite_is_unsafe(self) -> None:
        diagnosis = diagnose(_probe(sqlite_version="3.45.1"))
        with patch("tools.environment_doctor.collect_probe", return_value=_probe(sqlite_version="3.45.1")):
            with patch("tools.environment_doctor.diagnose", return_value=diagnosis):
                with patch("sys.stdout", new_callable=io.StringIO):
                    code = main(["--repo", str(ROOT), "--strict"])
        self.assertEqual(code, 1)

    def test_core_failure_exits_nonzero(self) -> None:
        diagnosis = diagnose(_probe(python_version=(3, 10, 14)))
        with patch("tools.environment_doctor.collect_probe", return_value=_probe()):
            with patch("tools.environment_doctor.diagnose", return_value=diagnosis):
                with patch("sys.stdout", new_callable=io.StringIO):
                    code = main(["--repo", str(ROOT)])
        self.assertEqual(code, 1)


class EnvironmentDoctorDirectInvocationTests(unittest.TestCase):
    def test_documented_script_path_works_without_pythonpath(self) -> None:
        env = os.environ.copy()
        env.pop("PYTHONPATH", None)
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "tools" / "environment_doctor.py"),
                "--repo",
                str(ROOT),
            ],
            cwd=ROOT,
            env=env,
            capture_output=True,
            text=True,
        )
        combined = result.stdout + result.stderr
        self.assertNotIn("ModuleNotFoundError", combined)
        self.assertNotIn("No module named 'native_kernel'", combined)
        self.assertIn("Native Kernel environment doctor", combined)
        core_ready = "CORE: READY" in result.stdout
        if core_ready:
            self.assertEqual(result.returncode, 0)
        else:
            self.assertEqual(result.returncode, 1)


class EnvironmentDoctorCollectTests(unittest.TestCase):
    def test_empty_postgres_dsn_is_treated_as_absent(self) -> None:
        probe = collect_probe(
            ROOT,
            environ={"NK_TEST_POSTGRES_DSN": "  "},
            python_version=(3, 12, 1),
            sqlite_version="3.51.3",
            psycopg_importable=False,
            which=lambda name: None,
            run=lambda *args, **kwargs: __import__("subprocess").CompletedProcess(
                args[0], 1, stdout="", stderr=""
            ),
        )
        self.assertIsNone(probe.postgres_dsn)

    def test_pinned_rust_channel_comes_from_toolchain_file(self) -> None:
        self.assertEqual(read_pinned_rust_channel(ROOT), "1.97.1")


if __name__ == "__main__":
    unittest.main()

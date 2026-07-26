from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
GENERATE = REPO_ROOT / "tools" / "source_recovery" / "generate_manifest.py"
VERIFY = REPO_ROOT / "tools" / "source_recovery" / "verify_manifest.py"


class SourceRecoveryToolsTests(unittest.TestCase):
    def run_tool(self, script: Path, *args: object) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(script), *(str(arg) for arg in args)],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def build_candidate(self, root: Path) -> tuple[Path, Path, Path, Path]:
        source = root / "candidate"
        source.mkdir()
        (source / "kernel.py").write_text("VERSION = '0.1.2.1'\n", encoding="utf-8")
        tests = source / "tests"
        tests.mkdir()
        (tests / "test_kernel.py").write_text("def test_example():\n    assert True\n", encoding="utf-8")
        node_ids = source / "node_ids.txt"
        node_ids.write_text("tests/test_kernel.py::test_example\n", encoding="utf-8")
        archive = root / "candidate.tar"
        archive.write_bytes(b"immutable archive placeholder")
        manifest = root / "manifest.json"
        return source, node_ids, archive, manifest

    def generate(self, source: Path, node_ids: Path, archive: Path, manifest: Path) -> subprocess.CompletedProcess[str]:
        return self.run_tool(
            GENERATE,
            source,
            "--output",
            manifest,
            "--archive",
            archive,
            "--recovered-from",
            "unit-test fixture",
            "--recovered-by",
            "test runner",
            "--test-node-ids",
            node_ids,
            "--declared-test-count",
            44,
            "--original-test-command",
            "python -m pytest -q",
        )

    def test_generate_and_verify_candidate_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, node_ids, archive, manifest = self.build_candidate(root)

            generated = self.generate(source, node_ids, archive, manifest)
            self.assertEqual(generated.returncode, 0, generated.stderr)

            payload = json.loads(manifest.read_text(encoding="utf-8"))
            self.assertEqual(payload["snapshot_status"], "UNVERIFIED_CANDIDATE")
            self.assertEqual(payload["test_inventory"]["collected_count"], 1)
            self.assertEqual(len(payload["files"]), 2)

            verified = self.run_tool(
                VERIFY,
                manifest,
                source,
                "--archive",
                archive,
                "--test-node-ids",
                node_ids,
                "--json",
            )
            self.assertEqual(verified.returncode, 0, verified.stderr)
            summary = json.loads(verified.stdout)
            self.assertTrue(summary["ok"])
            self.assertFalse(summary["authenticity_proven"])
            self.assertEqual(summary["verified_files"], 2)

    def test_verifier_detects_file_drift(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, node_ids, archive, manifest = self.build_candidate(root)
            generated = self.generate(source, node_ids, archive, manifest)
            self.assertEqual(generated.returncode, 0, generated.stderr)

            (source / "kernel.py").write_text("VERSION = 'changed'\n", encoding="utf-8")
            verified = self.run_tool(
                VERIFY,
                manifest,
                source,
                "--archive",
                archive,
                "--test-node-ids",
                node_ids,
            )
            self.assertEqual(verified.returncode, 1)
            self.assertIn("SHA-256 mismatch", verified.stderr)

    def test_verifier_rejects_path_traversal(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, node_ids, archive, manifest = self.build_candidate(root)
            generated = self.generate(source, node_ids, archive, manifest)
            self.assertEqual(generated.returncode, 0, generated.stderr)

            payload = json.loads(manifest.read_text(encoding="utf-8"))
            payload["files"][0]["original_path"] = "../escape.py"
            manifest.write_text(json.dumps(payload), encoding="utf-8")

            verified = self.run_tool(
                VERIFY,
                manifest,
                source,
                "--archive",
                archive,
                "--test-node-ids",
                node_ids,
            )
            self.assertEqual(verified.returncode, 1)
            self.assertIn("unsafe manifest path", verified.stderr)

    @unittest.skipUnless(hasattr(os, "symlink"), "symlink support is required")
    def test_generator_rejects_symlink(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, node_ids, archive, manifest = self.build_candidate(root)
            target = root / "outside.py"
            target.write_text("secret = True\n", encoding="utf-8")
            link = source / "linked.py"
            try:
                link.symlink_to(target)
            except OSError as exc:
                self.skipTest(f"symlink creation unavailable: {exc}")

            generated = self.generate(source, node_ids, archive, manifest)
            self.assertEqual(generated.returncode, 2)
            self.assertIn("symlink is not allowed", generated.stderr)


if __name__ == "__main__":
    unittest.main()

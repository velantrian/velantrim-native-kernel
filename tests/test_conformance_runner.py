from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools" / "conformance"
sys.path.insert(0, str(TOOLS))

from runner import ContractError, canonical_json_bytes, content_hash  # noqa: E402


class CanonicalEncodingTests(unittest.TestCase):
    def test_key_order_is_deterministic(self) -> None:
        self.assertEqual(canonical_json_bytes({"b": 2, "a": 1}), b'{"a":1,"b":2}')

    def test_non_nfc_is_rejected(self) -> None:
        with self.assertRaises(ContractError):
            content_hash({"text": "e\u0301"})

    def test_float_is_rejected(self) -> None:
        with self.assertRaises(ContractError):
            content_hash({"value": 1.25})

    def test_null_is_rejected(self) -> None:
        with self.assertRaises(ContractError):
            content_hash({"value": None})


class FixtureRunnerTests(unittest.TestCase):
    def test_fixture_pack_passes(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(TOOLS / "runner.py"), "validate"],
            cwd=ROOT,
            check=False,
            text=True,
            capture_output=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        report = json.loads(completed.stdout)
        self.assertEqual(report["support_state"], "SUPPORTED")
        self.assertEqual(report["kernel_runtime_conformance"], "UNSUPPORTED")


if __name__ == "__main__":
    unittest.main()

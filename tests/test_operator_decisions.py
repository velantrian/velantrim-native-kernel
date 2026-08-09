from __future__ import annotations

import importlib.util
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "ai_context" / "validate_operator_decisions.py"
SPEC = importlib.util.spec_from_file_location("validate_operator_decisions", MODULE_PATH)
module = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class OperatorDecisionTests(unittest.TestCase):
    def _copy_fixture(self, directory: Path) -> None:
        for rel in (
            module.MANIFEST_PATH,
            module.LICENSE_EN,
            module.LICENSE_RU,
            module.ADR_EN,
            module.ADR_RU,
        ):
            source = ROOT / rel
            target = directory / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)

    def test_repository_packages_remain_pending(self) -> None:
        module.validate(ROOT)

    def test_license_selection_without_operator_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            self._copy_fixture(repo)
            manifest_path = repo / module.MANIFEST_PATH
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["license_publication"]["selected_option"] = "APACHE_2_0"
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            with self.assertRaisesRegex(module.OperatorDecisionError, "selected"):
                module.validate(repo)

    def test_reducer_runtime_authorization_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            self._copy_fixture(repo)
            manifest_path = repo / module.MANIFEST_PATH
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["adr_0024"]["runtime_effect"] = "REDUCER_V2_AUTHORIZED"
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            with self.assertRaisesRegex(module.OperatorDecisionError, "runtime effect"):
                module.validate(repo)

    def test_missing_license_option_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            self._copy_fixture(repo)
            package = repo / module.LICENSE_EN
            package.write_text(
                package.read_text(encoding="utf-8").replace(
                    "Business Source License 1.1",
                    "Removed Source License",
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(module.OperatorDecisionError, "missing option"):
                module.validate(repo)

    def test_missing_adr_decision_option_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            self._copy_fixture(repo)
            package = repo / module.ADR_EN
            package.write_text(
                package.read_text(encoding="utf-8").replace("### `REJECT`", "### removed"),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(module.OperatorDecisionError, "REJECT"):
                module.validate(repo)

    def test_silent_upgrade_boundary_is_required(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            self._copy_fixture(repo)
            package = repo / module.ADR_RU
            package.write_text(
                package.read_text(encoding="utf-8").replace(
                    "SILENT_V1_TO_V2_UPGRADE",
                    "REMOVED_UPGRADE_BOUNDARY",
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(module.OperatorDecisionError, "silent-upgrade"):
                module.validate(repo)


if __name__ == "__main__":
    unittest.main()

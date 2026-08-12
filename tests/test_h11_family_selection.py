from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "ai_context" / "validate_h11_family_selection.py"
SPEC = importlib.util.spec_from_file_location("validate_h11_family_selection", MODULE_PATH)
module = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class H11FamilySelectionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.selection = json.loads((ROOT / "docs" / "research" / "H11_FAMILY_SELECTION.json").read_text(encoding="utf-8"))

    def validate(self, value: dict | None = None) -> None:
        module.validate(ROOT, copy.deepcopy(self.selection) if value is None else value)

    def test_repository_selection_candidate_passes(self) -> None:
        self.validate()

    def test_other_family_cannot_replace_h11(self) -> None:
        value = copy.deepcopy(self.selection)
        value["selected_hypothesis"] = "A10-H03"
        with self.assertRaisesRegex(module.H11FamilySelectionError, "only A10-H11"):
            self.validate(value)

    def test_selection_package_cannot_self_authorize_preregistration(self) -> None:
        value = copy.deepcopy(self.selection)
        value["preregistration_authorized_by_this_package"] = True
        with self.assertRaisesRegex(module.H11FamilySelectionError, "self-authorize"):
            self.validate(value)

    def test_selection_package_cannot_authorize_implementation_or_execution(self) -> None:
        for field in ("experiment_implementation_authorized", "experiment_execution_authorized"):
            value = copy.deepcopy(self.selection)
            value[field] = True
            with self.assertRaisesRegex(module.H11FamilySelectionError, "implementation|execution"):
                self.validate(value)

    def test_h11_cannot_be_redefined_as_composition_federation(self) -> None:
        value = copy.deepcopy(self.selection)
        value["h11_boundary"]["composition_federation_is_h11"] = True
        with self.assertRaisesRegex(module.H11FamilySelectionError, "composition/federation"):
            self.validate(value)

    def test_selection_must_remain_bound_to_frozen_ravp(self) -> None:
        value = copy.deepcopy(self.selection)
        value["source_plan"]["merge_sha"] = "0" * 40
        with self.assertRaisesRegex(module.H11FamilySelectionError, "source plan merge"):
            self.validate(value)

    def test_next_gate_cannot_jump_to_execution(self) -> None:
        value = copy.deepcopy(self.selection)
        value["next_gate_if_accepted"] = "A10_H11_EXECUTION"
        with self.assertRaisesRegex(module.H11FamilySelectionError, "next gate"):
            self.validate(value)


if __name__ == "__main__":
    unittest.main()

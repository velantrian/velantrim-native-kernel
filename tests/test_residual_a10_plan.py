from __future__ import annotations

import importlib.util
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "ai_context" / "validate_residual_a10_plan.py"
SPEC = importlib.util.spec_from_file_location("validate_residual_a10_plan", MODULE_PATH)
module = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class ResidualA10PlanTests(unittest.TestCase):
    def _copy_fixture(self, repo: Path) -> Path:
        for relative in (
            module.PLAN_PATH,
            module.EN_PATH,
            module.RU_PATH,
        ):
            source = ROOT / relative
            target = repo / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
        return repo / module.PLAN_PATH

    def _mutate(self, callback) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            plan_path = self._copy_fixture(repo)
            plan = json.loads(plan_path.read_text(encoding="utf-8"))
            callback(plan)
            plan_path.write_text(
                json.dumps(plan, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            module.validate(repo)

    def test_repository_plan_passes(self) -> None:
        module.validate(ROOT)

    def test_execution_authority_is_rejected(self) -> None:
        def change(plan):
            plan["operator_decision"]["experiment_execution_authorized"] = True

        with self.assertRaisesRegex(module.ResidualA10PlanError, "execution"):
            self._mutate(change)

    def test_residual_target_drift_is_rejected(self) -> None:
        def change(plan):
            plan["residual_targets"][-1] = "A10-H12"

        with self.assertRaisesRegex(module.ResidualA10PlanError, "target"):
            self._mutate(change)

    def test_h11_cannot_be_redefined_as_federation(self) -> None:
        def change(plan):
            h11 = next(item for item in plan["families"] if item["hypothesis_id"] == "A10-H11")
            h11["hypothesis"] = "Federated nodes preserve semantic conformance."

        with self.assertRaisesRegex(module.ResidualA10PlanError, "H11"):
            self._mutate(change)

    def test_h06_requires_three_erasure_evidence_lanes(self) -> None:
        def change(plan):
            h06 = next(item for item in plan["families"] if item["hypothesis_id"] == "A10-H06")
            h06["evidence_lanes"] = h06["evidence_lanes"][:2]

        with self.assertRaisesRegex(module.ResidualA10PlanError, "H06"):
            self._mutate(change)

    def test_h08_simulation_cannot_support_h08(self) -> None:
        def change(plan):
            h08 = next(item for item in plan["families"] if item["hypothesis_id"] == "A10-H08")
            h08["qualification_tiers"]["SIMULATION_OR_EMULATION"] = "ELIGIBLE_FOR_H08"

        with self.assertRaisesRegex(module.ResidualA10PlanError, "simulation"):
            self._mutate(change)

    def test_h09_software_rehearsal_cannot_support_substrate_claim(self) -> None:
        def change(plan):
            h09 = next(item for item in plan["families"] if item["hypothesis_id"] == "A10-H09")
            h09["qualification_tiers"]["SOFTWARE_STOCHASTIC_REHEARSAL"] = "ELIGIBLE_FOR_H09"

        with self.assertRaisesRegex(module.ResidualA10PlanError, "stochastic"):
            self._mutate(change)

    def test_h10_requires_complete_two_by_two_matrix(self) -> None:
        def change(plan):
            h10 = next(item for item in plan["families"] if item["hypothesis_id"] == "A10-H10")
            h10["minimum_matrix"] = ["C1/S1", "C1/S2", "C2/S1"]

        with self.assertRaisesRegex(module.ResidualA10PlanError, "2x2"):
            self._mutate(change)

    def test_language_change_cannot_become_computation_model_change(self) -> None:
        def change(plan):
            h10 = next(item for item in plan["families"] if item["hypothesis_id"] == "A10-H10")
            h10["equivalence_predicate"] = "A language change is sufficient computation independence."

        with self.assertRaisesRegex(module.ResidualA10PlanError, "language"):
            self._mutate(change)

    def test_giant_bpv2_default_is_rejected(self) -> None:
        def change(plan):
            plan["family_strategy"]["giant_bpv2"] = "PREFERRED"

        with self.assertRaisesRegex(module.ResidualA10PlanError, "giant BPV-2"):
            self._mutate(change)

    def test_final_canon_promotion_is_rejected(self) -> None:
        def change(plan):
            plan["operator_decision"]["final_canon"] = "AUTHORIZED"

        with self.assertRaisesRegex(module.ResidualA10PlanError, "Final Canon"):
            self._mutate(change)

    def test_human_plan_must_keep_composition_separate(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            self._copy_fixture(repo)
            english = repo / module.EN_PATH
            text = english.read_text(encoding="utf-8")
            english.write_text(
                text.replace("composition/federation", "separate-capability"),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(module.ResidualA10PlanError, "composition/federation"):
                module.validate(repo)


if __name__ == "__main__":
    unittest.main()

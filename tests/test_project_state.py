from __future__ import annotations
import copy, importlib.util, json, sys, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("validate_project_state",ROOT/"tools/ai_context/validate_project_state.py")
module=importlib.util.module_from_spec(SPEC); assert SPEC.loader; sys.modules[SPEC.name]=module; SPEC.loader.exec_module(module)

class ProjectStateTests(unittest.TestCase):
    def setUp(self):
        self.state=json.loads((ROOT/"project-state.json").read_text(encoding="utf-8"))
        self.registry=json.loads((ROOT/"contracts/registry.json").read_text(encoding="utf-8"))
    def validate(self,state=None,registry=None):
        module.validate(state or copy.deepcopy(self.state),repo=ROOT,registry=registry or copy.deepcopy(self.registry),check_git=False)
    def test_repository_state_passes(self): self.validate()
    def test_production_promotion_is_rejected(self):
        state=copy.deepcopy(self.state); state["status"]["production_authorized"]=True
        with self.assertRaisesRegex(module.ProjectStateError,"maturity|production"): self.validate(state)
    def test_checkpoint_relation_is_declared(self):
        state=copy.deepcopy(self.state); state["checkpoints"]["expected_head_relationship"]="MAYBE"
        with self.assertRaisesRegex(module.ProjectStateError,"relationship"): self.validate(state)
    def test_notion_checkpoint_must_match_publication(self):
        state=copy.deepcopy(self.state); state["checkpoints"]["notion_synchronized_through_sha"]="0"*40
        with self.assertRaisesRegex(module.ProjectStateError,"Notion/publication"): self.validate(state)
    def test_historical_recovery_cannot_block_clean_lineage(self):
        state=copy.deepcopy(self.state); state["tracks"]["historical_recovery"]["blocks_clean_implementation"]=True
        with self.assertRaisesRegex(module.ProjectStateError,"must not block"): self.validate(state)
    def test_nk_epi_cannot_be_promoted_by_metadata(self):
        state=copy.deepcopy(self.state); state["nk_epi"]["supported"]=1; state["nk_epi"]["unsupported"]=7
        with self.assertRaisesRegex(module.ProjectStateError,"NK-EPI"): self.validate(state)
    def test_legacy_registry_runtime_status_is_rejected(self):
        registry=copy.deepcopy(self.registry); registry["runtime_status"]="NOT_IMPLEMENTED"
        with self.assertRaisesRegex(module.ProjectStateError,"legacy registry"): self.validate(registry=registry)
    def test_registry_runtime_summary_must_match_state(self):
        registry=copy.deepcopy(self.registry); registry["runtime_summary"]["kernel_runtime_conformance"]="C3"
        with self.assertRaisesRegex(module.ProjectStateError,"registry/state"): self.validate(registry=registry)
    def test_registry_assertion_arithmetic_must_match(self):
        registry=copy.deepcopy(self.registry); registry["assertion_evidence_summary"]["supported"]=44
        with self.assertRaisesRegex(module.ProjectStateError,"assertion summary"): self.validate(registry=registry)
    def test_accepted_family_cannot_claim_full_support(self):
        registry=copy.deepcopy(self.registry); registry["families"][0]["implementation_support"]="FULL"
        with self.assertRaisesRegex(module.ProjectStateError,"support drift"): self.validate(registry=registry)
    def test_nk_epi_registry_cannot_claim_runtime(self):
        registry=copy.deepcopy(self.registry)
        epi=next(f for f in registry["families"] if f["family_id"]=="NK-EPI"); epi["implementation_support"]="PARTIAL"
        with self.assertRaisesRegex(module.ProjectStateError,"NK-EPI support"): self.validate(registry=registry)
    def test_issue_64_must_remain_completed(self):
        state=copy.deepcopy(self.state); state["issues"]["64"]["state"]="OPEN"
        with self.assertRaisesRegex(module.ProjectStateError,"Issue #64"): self.validate(state)

if __name__=="__main__": unittest.main()

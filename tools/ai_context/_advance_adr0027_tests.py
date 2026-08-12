#!/usr/bin/env python3
from pathlib import Path
R=Path(__file__).resolve().parents[2]
old_gate='OPERATOR_CANON_RUNTIME_DECISION_REQUIRED'; new_gate='RESIDUAL_A10_VALIDATION_PLAN'
old_status='COMPLETE / OPTION_D_VALIDATION_AND_SYNC_COMPLETE / AWAITING_SEPARATE_OPERATOR_DECISION'
new_status='COMPLETE / OPTION_D_OPERATOR_DECISION_ACCEPTED / RESIDUAL_VALIDATION_PLANNING_AUTHORIZED'
for rel in ['tests/test_a9_reference_laboratory_boundary.py','tests/test_a10_open_questions_falsification.py','tests/test_integrated_a1_a10_review.py','tests/test_independent_architecture_review_protocol.py']:
 p=R/rel; t=p.read_text(); assert old_gate in t, rel
 t=t.replace(old_gate,new_gate)
 if old_status in t: t=t.replace(old_status,new_status)
 p.write_text(t)
p=R/'tests/test_project_state.py'; t=p.read_text(); old='state["notion"]["synchronization_required"] = True\n        with self.assertRaisesRegex(module.ProjectStateError, "must remain complete"):'; new='state["notion"]["synchronization_required"] = False\n        with self.assertRaisesRegex(module.ProjectStateError, "must remain pending"):'; assert old in t; p.write_text(t.replace(old,new))

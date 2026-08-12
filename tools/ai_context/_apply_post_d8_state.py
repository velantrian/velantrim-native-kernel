#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[2]
P=R/'project-state.json'
s=json.loads(P.read_text())
D='57993f39906ae7266011f6146c9a485d0587d2bf'
N='RESIDUAL_A10_VALIDATION_PLAN'
res=['A10-H03','A10-H06','A10-H08','A10-H09','A10-H10','A10-H11']
sup=['A10-H01','A10-H02','A10-H04','A10-H05','A10-H07','A10-H12']
r=s['tracks']['long_horizon_research']; a=r['architecture_refoundation']; v=r['post_blueprint_validation']; x=v['bpv1_execution_result']
assert a['next_content_slice']=='OPERATOR_CANON_RUNTIME_DECISION_REQUIRED'
assert v['d6_hypothesis_classification']['supported_for_scope']==sup
assert v['d6_hypothesis_classification']['not_tested']==res
assert v['d7_integrated_rereview']['architecture_position']=='STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL'
assert v['d8_consolidated_sync']['status']=='COMPLETE / READ_BACK_VERIFIED'
s['snapshot_id']='native-kernel/state/2026-08-12-post-d8-operator-decision'; s['observed_at']='2026-08-12T08:11:03Z'
r['status']='ACTIVE / POST-D8 RESIDUAL VALIDATION PLANNING / NO AUTOMATIC PROMOTION'
a['status']='BLUEPRINT COMPLETE / PROVISIONAL / RESIDUAL VALIDATION PLANNING AUTHORIZED'; a['next_content_slice']=N
v['status']='COMPLETE / OPTION_D_OPERATOR_DECISION_ACCEPTED / RESIDUAL_VALIDATION_PLANNING_AUTHORIZED'
v['post_d8_operator_decision']={'protocol':'nk-post-d8-operator-decision/1','decision_id':'OD-POST-D8-001','decision_status':'ACCEPTED','operator_approval':'APPROVED','decision_merge_sha':D,'source_machine_truth_sha':'ad459cd5301756936a26cab0997ba6c77c58191b','final_canon':'DEFERRED / NOT_AUTHORIZED_AT_THIS_CHECKPOINT','architecture_position':'STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL','runtime_expansion':'FROZEN','product_runtime_thaw':False,'production_authorized':False,'next_gate':N,'next_gate_scope':'RESEARCH_PLANNING_ONLY','experiment_execution_authorized':False,'residual_validation_targets':res}
x['next_gate']=N
s['issues']['88']['meaning']=f'Architecture Re-foundation A1-A10 remains provisional. ADR-0026 Option D completed through D8. ADR-0027 / OD-POST-D8-001 was ACCEPTED / OPERATOR APPROVED at {D}: Final Canon is deferred, runtime remains frozen, and the next gate is RESIDUAL_A10_VALIDATION_PLAN for A10-H03/H06/H08/H09/H10/H11 as RESEARCH_PLANNING_ONLY; experiment execution is not authorized.'
s['notion']['synchronization_required']=True
s['notion']['scope'] += f' ADR-0027 / OD-POST-D8-001 merged at {D}; operator-decision truth is pending Notion synchronization/read-back.'
for c in ['ADR-0027 retains A1-A10 as STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL; it does not promote Final Canon.','ADR-0027 authorizes RESIDUAL_A10_VALIDATION_PLAN research planning only; it does not authorize residual experiment execution.','ADR-0027 keeps product runtime expansion frozen and production unauthorized.']:
    if c not in s['non_claims']: s['non_claims'].append(c)
P.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n')

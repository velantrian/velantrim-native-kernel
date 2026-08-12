# Post-Residual A10 Current Truth

<!-- POST_RESIDUAL_A10_PLAN_CURRENT -->

This file is the **current human-orientation overlay** after completion of the planning-only Residual A10 Validation Plan. It does not replace historical D5/D6/D7/D8/ADR-0027 records and does not authorize experiment execution.

```yaml
current_truth_source_sha: edc0501d71a827462aafd1ac4497920a719a4519
current_truth_source_pr: 124
plan_protocol: nk-residual-a10-validation-plan/1
plan_id: RAVP-001-residual-a10-validation-plan-v1
plan_state: COMPLETE / MERGED / NOTION_7_OF_7_READ_BACK_VERIFIED
architecture: STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL
final_canon: DEFERRED / NOT_AUTHORIZED_AT_THIS_CHECKPOINT
runtime_expansion: FROZEN
product_runtime_thaw: false
production_authorized: false
residual_targets: [A10-H03, A10-H06, A10-H08, A10-H09, A10-H10, A10-H11]
selected_family: NONE
next_gate: SEPARATE_FAMILY_PREREGISTRATION_SELECTION
next_gate_scope: PREREGISTRATION_SELECTION_ONLY
family_preregistration_authorized: false
experiment_implementation_authorized: false
experiment_execution_authorized: false
notion_surfaces: 7
notion_read_back_verified: 7
new_notion_pages_created: 0
issue_88: OPEN
```

## Current interpretation

- PR #124 is the completed **planning artifact**, not experiment evidence.
- The six D6 outcomes remain `NOT_TESTED`: `A10-H03/H06/H08/H09/H10/H11`.
- `A10-H11` means **laboratory mechanisms can remain reproducible without becoming Architecture Canon**.
- Composition/federation is a separate D7-F08 capability class and is **not** A10-H11.
- H06 planning distinguishes logical forgetting, cryptographic erasure and physical erasure evidence lanes.
- H08 simulation/emulation is method rehearsal only and cannot establish H08 substrate support.
- H09 stochastic software rehearsal cannot establish a physical/probabilistic-substrate claim.
- H10 does not treat a different programming language as a different computation model.
- No residual family has been selected.
- `SEPARATE_FAMILY_PREREGISTRATION_SELECTION` is a selection gate only. It does not itself authorize a family preregistration, implementation or execution.

## Authority order

For current state, use:

1. live GitHub refs, PR state, Actions, reviews and Issue #88;
2. `project-state.json`;
3. this file;
4. `AGENTS.md`;
5. older current-state overlays in `README.md`, `STATUS.md`, `ROADMAP.md`, and `docs/ai/*` only as historical chronology where they conflict with items 1–4.

Older `RESIDUAL_A10_VALIDATION_PLAN NEXT`, `D6 NEXT`, `OPERATOR_CANON_RUNTIME_DECISION_REQUIRED`, or similar wording is **historical chronology**, not the current next gate.

## Immutable boundaries

```text
RAVP-001 planning ≠ experiment evidence
planning complete ≠ hypothesis supported
NOT_TESTED ≠ SUPPORTED
family selection ≠ preregistration authorization
preregistration ≠ execution admission
execution admission ≠ product runtime thaw
laboratory reproduction ≠ Architecture Canon
language difference ≠ computation-model difference
simulation/emulation ≠ H08 physical substrate evidence
stochastic software rehearsal ≠ H09 physical substrate evidence
logical forgetting ≠ cryptographic erasure ≠ physical erasure
composition/federation ≠ A10-H11
```

Still reserved to the operator:

- Issue #18 license/publication/contribution regime;
- Issue #74 / ADR-0024 reducer-v2 semantics;
- Track H recovered-source admission;
- Final Canon promotion;
- runtime thaw/product runtime integration;
- production authorization;
- any experiment execution not separately admitted.

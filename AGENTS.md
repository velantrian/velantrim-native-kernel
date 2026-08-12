# 🤖 Velantrim Native Kernel repository guidance

## Required reading order

Before searching code, creating a branch, or proposing architecture changes, read:

1. `project-state.json`
2. `docs/ai/POST_RESIDUAL_A10_STATE.md`
3. `README.md`
4. `STATUS.md`
5. `ROADMAP.md`
6. `docs/ai/README.md`
7. `docs/ai/CURRENT_STATE.md`
8. `docs/ai/KNOWN_RISKS.md`
9. `docs/ARCHITECTURE_REFOUNDATION.md`
10. `docs/A10_OPEN_QUESTIONS_AND_FALSIFICATION.md`
11. `docs/research/BPV1_D6_A10_CLASSIFICATION.md`
12. `docs/research/BPV1_D7_INTEGRATED_REREVIEW.md`
13. `docs/research/BPV1_D8_CONSOLIDATED_SYNC.md`
14. `docs/adr/0027-post-d8-residual-validation-planning.md`
15. `docs/research/RESIDUAL_A10_VALIDATION_PLAN.md`
16. affected Canon, contracts, ADRs, source, tests, workflows and evidence
17. live GitHub PRs/issues/Actions/reviews
18. corresponding existing Notion pages when synchronization is part of the task

Do not begin with random repository search. Verify live state first.

If an older current-looking overlay conflicts with `project-state.json` or `docs/ai/POST_RESIDUAL_A10_STATE.md`, preserve the old text as chronology and follow the newer current-truth layer. In particular, old `D6 NEXT`, `RESIDUAL_A10_VALIDATION_PLAN NEXT`, or `OPERATOR_CANON_RUNTIME_DECISION_REQUIRED` wording is no longer the current gate after PR #124.

## Current maturity

```text
RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
clean_runtime_support:      PARTIAL
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
production_authorized:      false

assertions: 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:    0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
runtime expansion: FROZEN
```

Current machine truth uses `project-state.json` protocol `nk-project-state/2`. Live HEAD must be resolved through Git/GitHub; committed checkpoint metadata never predicts its own future merge SHA.

## Independent tracks

```text
H — Historical Recovery
  OPEN / BLOCKED / operator-controlled source admission

C — Clean Reference Implementation
  P1–P5 + C4 + C5
  PARTIAL / BOUNDED_REFERENCE_LABORATORY

R — Architecture Re-foundation and post-blueprint research
  A1-A10 blueprint complete / provisional
  Option D complete through D8
  ADR-0027 accepted
  RAVP-001 residual planning complete
  current gate: SEPARATE_FAMILY_PREREGISTRATION_SELECTION
```

Never collapse these tracks.

```text
historical recovery ≠ clean implementation
reference laboratory ≠ Architecture Canon
planning artifact ≠ experiment evidence
NOT_TESTED ≠ SUPPORTED
family selection ≠ preregistration authorization
preregistration ≠ execution admission
```

## Current authoritative research state

PR #124 merged `RAVP-001-residual-a10-validation-plan-v1` at `edc0501d71a827462aafd1ac4497920a719a4519` after exact-head and post-merge CI. Its seven existing Native Kernel Notion surfaces were synchronized and read back `7/7 VERIFIED`; zero new pages were created.

The D6 classification remains unchanged:

```text
SUPPORTED_FOR_SCOPE:
  A10-H01 / A10-H02 / A10-H04 / A10-H05 / A10-H07 / A10-H12

NOT_TESTED:
  A10-H03 / A10-H06 / A10-H08 / A10-H09 / A10-H10 / A10-H11
```

The residual plan decomposes the six `NOT_TESTED` hypotheses into separate bounded research families:

```text
H03 — representation migration continuity
H06 — forgetting/disposal/cryptographic/physical erasure epistemics
H08 — physical non-address-based dynamical continuity
H09 — probabilistic/statistical conformance
H10 — orthogonal storage/computation variation
H11 — laboratory reproducibility without laboratory machinery becoming Architecture Canon
```

Critical correction:

```text
A10-H11 ≠ composition/federation
```

Composition/federation remains the separate D7-F08 capability class.

## Current next gate

```text
next gate: SEPARATE_FAMILY_PREREGISTRATION_SELECTION
scope: PREREGISTRATION_SELECTION_ONLY
selected family: NONE
family preregistration authorized: false
residual experiment implementation authorized: false
residual experiment execution authorized: false
architecture: STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL
Final Canon: DEFERRED / NOT AUTHORIZED
runtime expansion: FROZEN
product runtime thaw: false
production: false
```

Do **not** silently select H11 or any other family merely because the plan recommends an order. A future family selection/preregistration requires a separate authorized step. A later execution admission is another separate gate.

## Fail-closed residual rules

- subject self-PASS is forbidden;
- implementation self-report is not semantic truth;
- private implementation state is not mandatory oracle input;
- failure conditions/oracle/thresholds must be frozen before adjudication;
- post-hoc rescue under the same experiment identity is forbidden;
- `INDETERMINATE` and `NOT_TESTED` remain legitimate outcomes;
- raw facts and semantic qualification remain separate;
- H06 must not promote logical forgetting to cryptographic/physical erasure without qualifying evidence;
- H08 simulation/emulation cannot establish physical substrate support;
- H09 stochastic software rehearsal cannot establish a physical/probabilistic-substrate claim;
- H10 cannot count programming-language difference as computation-model independence;
- H11 must protect lab reproducibility without promoting profile machinery into Canon.

## Frozen BPV-1 authority

The frozen historical BPV1 plan remains:

```text
plan_id: BPV1-001-cross-lineage-bounded-accountability-v1
plan merge: a538d7f1e28858a88b9ee777ac7d6e05b85943db
plan SHA-256: 7fe8174c604678c6b79d3fdeae83d7c5ab0d2fb15bfe343d41659d05d9496ad0
```

Do not use the old erroneous digest `15c830ed...`.

Historical D5 and D5-R1 remain distinct:

```text
D5 PR #114 merge: a191e9c868c14af34a269dcdfae44406f1013bda
D5-R1 PR #115 merge: 3856740570620fb2243e2f0da76359281ec4068f
external qualification: QUALIFIED
frozen evaluator: SUPPORTED_FOR_SCOPE
mandatory fixtures: 12/12 PASS
```

Do not rewrite frozen preregistration/oracle semantics or historical evidence to fit future runs.

## Runtime freeze

Allowed while frozen:

- truth-surface/integrity/security/provenance repairs;
- evidence preservation;
- historical recovery work that does not admit operator-controlled sources;
- planning/preregistration work only when the active gate authorizes it.

Not automatically authorized:

- residual experiment implementation/execution;
- product runtime integration;
- reducer v2/new Event verbs;
- new product DB/language/hardware profile;
- executable NK-EPI/Temporal/deletion expansion;
- Final Canon or production promotion.

## Reserved operator decisions

```text
Issue #18 — license/publication/contribution regime
  PENDING_OPERATOR

Issue #74 / ADR-0024 — reducer referential semantics
  PROPOSED / PENDING_OPERATOR
  reducer-v2 NOT AUTHORIZED

Track H source admission
  OPERATOR-CONTROLLED
```

No AI agent may choose the license, accept ADR-0024, admit recovered Track H sources, thaw runtime, promote Final Canon, or authorize production without explicit operator authority.

## Required distinctions

```text
Claim ≠ truth
admission ≠ objective truth
Unknown ≠ False
Architecture Canon ≠ implementation profile
reference implementation ≠ architectural authority
operator approval ≠ independent validation
qualifying independent review ≠ architecture proof
falsification instrument ≠ product runtime
logical ERASED ≠ physical deletion
cryptographic erasure ≠ physical erasure
forgetting/loss ≠ deliberate erasure
language difference ≠ computation-model difference
simulation/emulation ≠ physical substrate evidence
local scoped conformance ≠ composition/federation conformance
planning ≠ preregistration ≠ execution admission ≠ execution
public repository ≠ open-source license
SUPPORTED_FOR_SCOPE ≠ universal proof
NOT_TESTED ≠ SUPPORTED
```

## Verification

At minimum for truth/research changes:

```bash
python tools/ai_context/validate_project_state.py --repo .
python tools/ai_context/validate_architecture_freeze.py --repo .
python tools/ai_context/validate_residual_a10_plan.py --repo .
python tools/ai_context/validate_reconciliation.py --repo .
python tools/ai_context/validate_context.py --repo .
python tools/docs/validate_bilingual_parity.py --repo .
```

Run any additional P4/P5/C4/C5/BPV1 gates triggered by the changed-file scope. A skipped test is not PASS. An unavailable environment is `NOT_EXECUTED`.

## Review discipline

Distinguish `BOT_NOTICE`, `AUTOMATED_FINDING`, `HUMAN_REVIEW`, `QUALIFYING_INDEPENDENT_ARCHITECTURE_REVIEW`, `OPERATOR_DECISION`, and `EVIDENCE`.

A Codex usage-limit notice is not review approval. Actionable findings must be reproduced and resolved or rejected with evidence; unresolved review threads block readiness where applicable.

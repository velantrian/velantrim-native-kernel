# 🤖 Velantrim Native Kernel repository guidance

## Required reading order

Before searching code, creating a branch, or proposing architecture changes, read:

1. `project-state.json`
2. `docs/ai/POST_RESIDUAL_A10_STATE.md`
3. `docs/research/H11_FAMILY_SELECTION.md`
4. `docs/research/H11_PREREGISTRATION.md`
5. `README.md`
6. `STATUS.md`
7. `ROADMAP.md`
8. `docs/ai/README.md`
9. `docs/ai/CURRENT_STATE.md`
10. `docs/ai/KNOWN_RISKS.md`
11. `docs/ARCHITECTURE_REFOUNDATION.md`
12. `docs/A10_OPEN_QUESTIONS_AND_FALSIFICATION.md`
13. `docs/research/BPV1_D6_A10_CLASSIFICATION.md`
14. `docs/research/BPV1_D7_INTEGRATED_REREVIEW.md`
15. `docs/research/BPV1_D8_CONSOLIDATED_SYNC.md`
16. `docs/adr/0027-retain-provisional-architecture-and-runtime-freeze-after-option-d.md`
17. `docs/research/RESIDUAL_A10_VALIDATION_PLAN.md`
18. affected Canon, contracts, ADRs, source, tests, workflows and evidence
19. live GitHub PRs/issues/Actions/reviews
20. corresponding existing Notion pages when synchronization is part of the task

Do not begin with random repository search. Verify live state first.

If an older current-looking overlay conflicts with `project-state.json` or `docs/ai/POST_RESIDUAL_A10_STATE.md`, preserve the old text as chronology and follow the newer current-truth layer. Old `D6 NEXT`, `RESIDUAL_A10_VALIDATION_PLAN NEXT`, `SEPARATE_FAMILY_PREREGISTRATION_SELECTION`, and `OPERATOR_CANON_RUNTIME_DECISION_REQUIRED` wording is historical after PR #127.

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
  A10-H11 selected and preregistered
  current gate: A10_H11_EXECUTION_ADMISSION
```

Never collapse these tracks.

```text
historical recovery ≠ clean implementation
reference laboratory ≠ Architecture Canon
planning artifact ≠ experiment evidence
NOT_TESTED ≠ SUPPORTED
family selection ≠ preregistration authorization
preregistration ≠ execution admission
execution admission ≠ execution
```

## Current authoritative research state

The residual research lineage is now:

```text
PR #124 — RAVP-001 planning
  merge: edc0501d71a827462aafd1ac4497920a719a4519

PR #126 — A10-H11 selection candidate
  merge: bcd3b3f6c9d898315c93e5d24b5d0e02c95508cc
  selection package self-authorized preregistration: false

PR #127 — H11-001 preregistration
  plan: H11-001-c5-lab-canon-separation-v1
  exact head: 1dca13cdd2759c70d810f44977a227fe1147d4bb
  merge: 4a75ff15542013c033030620bdff61997e365140
  exact-head CI: 6/6 SUCCESS
  post-merge CI: 6/6 SUCCESS
  Notion: 7/7 READ_BACK_VERIFIED / 0 new pages
```

The D6 classification is unchanged:

```text
SUPPORTED_FOR_SCOPE:
  A10-H01 / A10-H02 / A10-H04 / A10-H05 / A10-H07 / A10-H12

NOT_TESTED:
  A10-H03 / A10-H06 / A10-H08 / A10-H09 / A10-H10 / A10-H11
```

H11 therefore remains **`NOT_TESTED`**. Preregistration is not evidence.

## H11 frozen subject and question

Selected family:

```text
A10-H11 / RAVP-H11-LAB-CANON-SEPARATION
```

Frozen laboratory subject:

```text
native-kernel/c5/2026-08-08-adr0023
manifest: evidence/c5/2026-08-08-adr0023/manifest.json
checkpoints: 2
artifacts: 8 ZIPs
exact bundle verification: tools/evidence/verify_bundle.py
```

H11 asks whether exact laboratory reproducibility can depend on profile mechanisms without promoting those mechanisms into universal Architecture Canon.

```text
A10-H11 ≠ composition/federation
exact lab bytes ≠ Architecture Canon
profile-specific mechanism ≠ universal semantic obligation
```

`UNJUSTIFIED_CANON_DEPENDENCY` is the frozen hard-failure class. Scoped support requires `mandatory_profile_leakage_count == 0` **and** a qualifying `INDEPENDENT_SEMANTIC_ORACLE`.

## Current next gate

```text
next gate: A10_H11_EXECUTION_ADMISSION
scope: EXECUTION_ADMISSION_ONLY
selected family: A10-H11
H11 plan state: PREREGISTERED / EXECUTION_NOT_AUTHORIZED
H11 outcome: NOT_TESTED
required oracle: INDEPENDENT_SEMANTIC_ORACLE
qualifying reviewer/reproducer: NOT_ESTABLISHED / MUST_BE_VERIFIED_AT_EXECUTION_ADMISSION
no qualifying reviewer outcome: BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER
residual experiment implementation authorized: false
residual experiment execution authorized: false
architecture: STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL
Final Canon: DEFERRED / NOT AUTHORIZED
runtime expansion: FROZEN
product runtime thaw: false
production: false
```

`A10_H11_EXECUTION_ADMISSION` is an admission gate only. It may freeze an exact plan digest, machine-readable dependency graph schema, raw-observation/adjudication separation and qualifying reviewer/reproducer evidence. It may **not** silently become execution.

If no qualifying independent reviewer/reproducer exists, the correct gate state is:

`BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER`

Do not use CI, Codex code review, model/session changes, assistant self-audit, operator approval or Notion read-back as substitutes for the preregistered independent semantic reviewer/reproducer.

## Fail-closed H11 rules

- Architecture/preregistration authors may not self-certify H11;
- subject self-PASS is forbidden;
- implementation self-report is not semantic truth;
- private implementation state is not mandatory oracle input;
- profile-byte exactness for historical lab reproduction does not create Architecture authority;
- dependency-graph omissions cannot hide a profile→Canon edge;
- `UNJUSTIFIED_CANON_DEPENDENCY` remains the hard failure class;
- failure conditions/oracle/thresholds are frozen before adjudication;
- post-hoc rescue under the same experiment identity is forbidden;
- historical evidence/Architecture history cannot be rewritten to rescue H11;
- `INDETERMINATE` and `NOT_TESTED` remain legitimate outcomes;
- raw facts and semantic qualification remain separate;
- composition/federation remains D7-F08, not H11.

## Historical PR #125 compatibility markers

These exact lines preserve the immediately preceding truth checkpoint for historical validators. They are chronology, **not** current instructions.

```text
next gate: SEPARATE_FAMILY_PREREGISTRATION_SELECTION
selected family: NONE
family preregistration authorized: false
residual experiment implementation authorized: false
residual experiment execution authorized: false
A10-H11 ≠ composition/federation
```

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
- research admission/preregistration work only when the active gate authorizes it.

Not automatically authorized:

- H11 or other residual experiment implementation/execution;
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
planning ≠ selection ≠ preregistration ≠ execution admission ≠ execution
public repository ≠ open-source license
SUPPORTED_FOR_SCOPE ≠ universal proof
NOT_TESTED ≠ SUPPORTED
```

## Verification

At minimum for current truth/H11 research changes:

```bash
python tools/ai_context/validate_project_state.py --repo .
python tools/ai_context/validate_architecture_freeze.py --repo .
python tools/ai_context/validate_residual_a10_plan.py --repo .
python tools/ai_context/validate_h11_family_selection.py --repo .
python tools/ai_context/validate_h11_preregistration.py --repo .
python tools/ai_context/validate_reconciliation.py --repo .
python tools/ai_context/validate_context.py --repo .
python tools/docs/validate_bilingual_parity.py --repo .
```

Run any additional P4/P5/C4/C5/BPV1 gates triggered by changed-file scope. A skipped test is not PASS. An unavailable environment is `NOT_EXECUTED`.

## Review discipline

Distinguish `BOT_NOTICE`, `AUTOMATED_FINDING`, `HUMAN_REVIEW`, `QUALIFYING_INDEPENDENT_ARCHITECTURE_REVIEW`, `QUALIFYING_INDEPENDENT_H11_REVIEWER_REPRODUCER`, `OPERATOR_DECISION`, and `EVIDENCE`.

A Codex usage-limit notice is not review approval. Actionable findings must be reproduced and resolved or rejected with evidence; unresolved review threads block readiness where applicable.
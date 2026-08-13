<!-- H11_EXECUTION_ADMISSION_BLOCKED_CURRENT -->
> [!IMPORTANT]
> **Current authoritative overlay — 2026-08-13.** Resolve live `main` through GitHub; committed documentation must not predict its own future merge SHA. Current selected family is `A10-H11`; current repository-native gate is `A10_H11_EXECUTION_ADMISSION`; admission is `BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER`; qualifying reviewer/reproducer is `NOT_ESTABLISHED`; H11 remains `NOT_TESTED`. The open review surface is PR #131. H11 implementation, execution, dependency-graph execution, and semantic adjudication are **NOT AUTHORIZED**. Runtime expansion remains `FROZEN`; product runtime thaw is `false`; Final Canon is `DEFERRED / NOT_AUTHORIZED`; production is `false`; Issue #88 remains OPEN. PR #129 remains immutable H11 execution-admission evidence; PR #130 (`e36b7f45410d74b8a65406bff6fdd6d070fa96b0`) is the machine-truth / verified 7-of-7 Notion synchronization checkpoint. Any lower `POST_D8_OPERATOR_DECISION_CURRENT`, `D6 NEXT`, `RESIDUAL_A10_VALIDATION_PLAN NEXT`, or other older current-looking wording is preserved as **historical chronology only**, not current instruction.

<!-- POST_D8_OPERATOR_DECISION_CURRENT -->
> [!IMPORTANT]
> **Current post-D8 operator decision — 2026-08-12.** ADR-0027 / `OD-POST-D8-001` is `ACCEPTED / OPERATOR APPROVED` at `57993f39906ae7266011f6146c9a485d0587d2bf`. A1–A10 remains `STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL`; Final Canon is **deferred**, product runtime remains `FROZEN`, production remains `false`. The only current next gate is `RESIDUAL_A10_VALIDATION_PLAN` for A10-H03, A10-H06, A10-H08, A10-H09, A10-H10, A10-H11, and that gate is **RESEARCH_PLANNING_ONLY** — no residual experiment execution is authorized. Any lower `D6 NEXT`, `D8 IN_PROGRESS`, or `OPERATOR_CANON_RUNTIME_DECISION_REQUIRED` wording is historical chronology, not current truth.

# 🧬 Velantrim Native Kernel

**[English](./README.md) · [Русский](./README.ru.md)**

### Technology-neutral architecture for durable knowledge, memory, change, and explanation

> **Current state:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`  
> **Active phase:** `POST-BLUEPRINT VALIDATION / D5-R1 QUALIFIED / D6 A10 HYPOTHESIS CLASSIFICATION NEXT / RUNTIME EXPANSION FROZEN`

Velantrim Native Kernel studies what semantic meaning, identity, provenance, time, uncertainty, conflict, revision, and explanation should survive when databases, languages, models, processors, and storage media change.

It is **not** an operating-system kernel, database product, LLM memory plugin, vector store, or Python framework definition.

```text
first define problem-level meaning and candidate obligations
        ↓
preregister scope, observables, threat/grounding assumptions and failure rules
        ↓
freeze an external oracle and admission boundary
        ↓
derive a replaceable bounded realization independently
        ↓
test and falsify the architectural claims
        ↓
classify only the hypotheses actually adjudicated by the evidence
```

## Architecture boundary

```text
Problem-level Purpose and Candidate Semantic Obligations
→ Preregistered Conformance / Threat / Grounding Boundary
→ BPV1 Execution Admission
→ Independently Derived Bounded Realization
→ External Evidence Qualification
→ Frozen Oracle Evaluation
→ A10 Hypothesis Classification
→ Integrated Re-review
→ Separate Operator Canon/Runtime Decision
```

Python, Rust, JSON, SHA-256, PostgreSQL, SQLite, graphs, vectors, LLMs, conventional hardware, event sourcing, exact replay, and CI are replaceable research instruments. They are not permanent Canon.

The current Python/PostgreSQL/SQLite lineage is a **bounded reference laboratory**, not the final definition of Native Kernel. IAR-1 established that the full A3 transition/outcome machine, A6 lifecycle graph, current Event/reducer/Receipt shape, and exact reconstruction are not justified as the universal minimum Kernel form.

## Current state

```text
clean_runtime_support:      PARTIAL
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
production_authorized:      false

assertion map: 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:        0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
runtime expansion: FROZEN
P1-C5 role: BOUNDED_REFERENCE_LABORATORY
```

C5 does not promote semantic assertions and does not authorize production.

## Checkpoint model

Machine-readable truth is recorded in [`project-state.json`](project-state.json) under `nk-project-state/2`.

| Role | Checkpoint |
|---|---|
| Publication checkpoint | `10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c` |
| Runtime checkpoint | `675aa4b398a2fc0181dc71d38904a2d33a09f5f8` |
| Runtime integrity checkpoint | `a1cdc6d8f36d67f40f065641809bc6da463c10a4` |
| Evidence-producing checkpoint | `296981ae84ad5bdab5dabbec9b7b9ebb43af63d7` |
| Manifest source / Notion synchronized descendant | `70acd0da61fee19131947aa56125833adb156ced` |
| BPV-1 preregistration merge | `a538d7f1e28858a88b9ee777ac7d6e05b85943db` |
| D5 execution merge | `a191e9c868c14af34a269dcdfae44406f1013bda` |
| D5-R1 qualification merge | `3856740570620fb2243e2f0da76359281ec4068f` |

These role checkpoints remain historical identities. Live `main` is resolved from GitHub or the checked-out Git ref; committed state does not predict its own future merge SHA.

## Truth reconciliation

```text
IAR-1:                   QUALIFYING_REVIEW_COMPLETE
IAR-1-R1:                COMPLETE
BPV-1 plan:              PREREGISTERED / EXECUTION_NOT_AUTHORIZED
execution admission:     COMPLETE / BPV1-001 ONLY
D5 execution:            COMPLETE
D5-R1 qualification:     COMPLETE / QUALIFIED
qualified oracle outcome: SUPPORTED_FOR_SCOPE / 12-of-12 mandatory fixtures PASS
next gate:               D6_A10_HYPOTHESIS_CLASSIFICATION
D6:                      NOT_STARTED
```

Newer live Notion content must be read directly. The Option D plan currently defers D5/D5-R1/D6 synchronization to consolidated D8; GitHub remains authoritative for technical state until that sync/read-back.

## Current evidence

Two immutable C5 evidence identities are repository-resident:

```text
evidence/c5/2026-08-07/manifest.json
evidence/c5/2026-08-08-adr0023/manifest.json
```

The BPV1-001 D5-R1 qualification evidence is separately preserved under:

```text
experiments/bpv1/BPV1-001/results/d5-r1/
```

Historical PR #114 D5 evidence remains unchanged.

ADR-0023 sets linked SQLite `3.51.3` as the current WAL floor. Historical SQLite `3.45.1` artifacts remain unchanged and version-bound.

```text
repository-resident evidence
≠ independent custody
≠ complete authenticity
≠ live-data safety
≠ physical deletion
≠ production readiness
SUPPORTED_FOR_SCOPE
≠ universal substrate portability proof
```

## Three independent tracks

```text
H — Historical Recovery
  authentic v0.1.2.1 and original 44-test suite
  NOT_FOUND_IN_ACCESSIBLE_SOURCES / OPEN / INDEPENDENT

C — Clean Reference Implementation
  P1–P5 + C4 + C5
  PRESERVED / PARTIAL / BOUNDED REFERENCE LABORATORY

R — Post-Blueprint Validation
  A1–A10 + integrated review remain provisional
  IAR-1 QUALIFYING / IAR-1-R1 COMPLETE
  BPV1-001 D5 COMPLETE / D5-R1 QUALIFIED
  D6 A10 HYPOTHESIS CLASSIFICATION NEXT
  NO AUTOMATIC PROMOTION
```

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
historical recovery ≠ clean implementation
reference laboratory ≠ final architecture
```

## Active architecture phase — Post-Blueprint Validation

ADR-0025 established blueprint-before-runtime. ADR-0026 records the operator-approved **Option D** validation route. IAR-1 completed the qualifying independent challenge; IAR-1-R1 reconciled all ten findings; PR #110 published the preregistered BPV-1 plan; PR #112 + PR #113 completed execution admission; PR #114 executed D5; PR #115 qualified the evidence path.

```text
A1–A10 provisional blueprint
→ integrated review                         COMPLETE / PROVISIONAL
→ operator post-blueprint decision          OPTION D / ADR-0026 / APPROVED
→ INDEPENDENT_ARCHITECTURE_REVIEW           COMPLETE / IAR-1 / QUALIFYING
→ REVIEW_FINDING_RECONCILIATION             COMPLETE / IAR-1-R1
→ BPV1_PLAN_AND_PREREGISTRATION             COMPLETE / PR #110
→ BPV1_EXECUTION_ADMISSION                  COMPLETE / PR #112 + #113
→ BPV1_SUBJECT_IMPLEMENTATION_AND_EXECUTION COMPLETE / PR #114
→ D5_R1_EVIDENCE_QUALIFICATION              COMPLETE / PR #115
→ D6_A10_HYPOTHESIS_CLASSIFICATION          NEXT / NOT STARTED
→ integrated re-review
→ consolidated authoritative synchronization
→ separate later operator Canon/runtime decision
```

Current boundaries:

```text
BPV-1 plan: BPV1-001-cross-lineage-bounded-accountability-v1 / PREREGISTERED
plan merge: a538d7f1e28858a88b9ee777ac7d6e05b85943db
frozen plan digest: 7fe8174c604678c6b79d3fdeae83d7c5ab0d2fb15bfe343d41659d05d9496ad0
D5 execution merge: a191e9c868c14af34a269dcdfae44406f1013bda
D5-R1 qualification merge: 3856740570620fb2243e2f0da76359281ec4068f
external qualification: QUALIFIED
frozen-oracle outcome: SUPPORTED_FOR_SCOPE
mandatory fixtures: 12/12 PASS
next gate: D6_A10_HYPOTHESIS_CLASSIFICATION
D6: NOT_STARTED
runtime expansion: FROZEN
product runtime thaw: NO
A1-A10 Final Canon: NOT AUTHORIZED
production: false
```

D5-R1 removes the identified HR10 subject-self-report adjudication path by making the Rust subject emit raw facts and deriving oracle-facing structural facts in a separate qualifier that does not read fixture expectations. The unchanged frozen evaluator remains the adjudicator. Integrity coverage now includes evidence and epistemic position, and retained loss-witness storage is internally bounded with bounded rollup.

This still does **not** establish independent implementation team/custody or an independent computation model. BPV1-001 remains conventional-digital, single-node, non-composed scoped evidence.

D6 must classify only the A10 hypotheses actually adjudicated by this evidence. Aggregate `SUPPORTED_FOR_SCOPE` must not be copied mechanically to hypotheses marked informative or not tested.

Plan: [English](docs/ARCHITECTURE_REFOUNDATION.md) · [Русский](docs/ARCHITECTURE_REFOUNDATION.ru.md).  
BPV-1 preregistration: [English](docs/research/BPV1_PREREGISTRATION.md) · [Русский](docs/research/BPV1_PREREGISTRATION.ru.md) · [JSON](docs/research/BPV1_PREREGISTRATION.json).  
D5-R1 qualification: [English](docs/research/BPV1_D5_R1_QUALIFICATION.md) · [Русский](docs/research/BPV1_D5_R1_QUALIFICATION.ru.md).  
Tracking: [Issue #88](https://github.com/velantrian/velantrim-native-kernel/issues/88).

During the freeze, architecture research, D6/D7/D8 validation work, integrity/security/reproducibility/provenance repair, evidence preservation, truth-surface repair and historical recovery remain allowed. Product semantic/runtime expansion remains unauthorized.

## Pending decisions

```text
Issue #18 — license/publication
  PENDING_OPERATOR / selected_option: null

Issue #74 / ADR-0024 — reducer referential semantics
  PROPOSED / PENDING_OPERATOR / selected_option: null
```

Neither decision is silently decided by ADR-0026 or BPV-1. Track H source admission remains operator-controlled.

## Historical R1 gate markers

These exact strings are retained only for publication-time continuity of the R1-era documentation registry, not as current state:

```text
BPV1_PLAN_AND_PREREGISTRATION
BLOCKED_PENDING_PREREGISTERED_PLAN
```

## Human quickstart

The current laboratory requires Python 3.11 or 3.12:

```bash
python -m unittest discover -s tests -p 'test_semantic_core.py' -v
python -m unittest discover -s tests -p 'test_p1_manifest.py' -v
python tools/ai_context/validate_project_state.py --repo .
python tools/ai_context/validate_architecture_freeze.py --repo .
python tools/ai_context/validate_bpv1_preregistration.py --repo .
python tools/ai_context/validate_context.py --repo .
```

> **SQLite profile warning:** P5/C3/C4/C5 fail closed when the Python process is linked against SQLite older than `3.51.3`. Do not treat a system SQLite rejection as a semantic failure. Build/use the pinned safe SQLite library before running those profile checks.

For the pinned-library setup, PostgreSQL DSN, and full P4/P5/C3/C4/C5 commands, use [`docs/QUICKSTART.md`](docs/QUICKSTART.md).
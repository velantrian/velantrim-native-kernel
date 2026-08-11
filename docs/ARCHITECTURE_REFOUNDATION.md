# 🧬 Architecture Re-foundation — Blueprint before Runtime

**[English](./ARCHITECTURE_REFOUNDATION.md) · [Русский](./ARCHITECTURE_REFOUNDATION.ru.md)**

> **State:** `ACTIVE / POST-BLUEPRINT VALIDATION / BPV1 PREREGISTERED / EXECUTION ADMISSION NEXT / RUNTIME EXPANSION FROZEN`  
> **Blueprint decision:** [`ADR-0025`](./adr/0025-blueprint-before-runtime-expansion.md)  
> **Post-blueprint decision:** [`ADR-0026`](./adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md)  
> **Issue:** [#88](https://github.com/velantrian/velantrim-native-kernel/issues/88)

## 1. Why this phase exists

Native Kernel studies a technology-neutral architecture for meaning, memory, knowledge, provenance, uncertainty, change and accountability. The existing **Python + PostgreSQL + SQLite** lineage is retained as a bounded reference laboratory rather than promoted into Canon because it exists first.

```text
A1-A10 blueprint                                  COMPLETE / PROVISIONAL
→ integrated A1-A10 review                       COMPLETE / PROVISIONAL
→ operator post-blueprint decision               COMPLETE / OPTION D
→ independent architecture review                COMPLETE / IAR-1
→ review finding reconciliation                  COMPLETE / IAR-1-R1
→ BPV1 plan and preregistration                  COMPLETE / PR #110
→ BPV1 execution admission                       NEXT
→ bounded cross-lineage falsification            BLOCKED BY ADMISSION
```

## 2. Draft inventory

All ten required blueprint slices exist and remain `DRAFTED / PROVISIONAL`. A10 retains model identity `nk-open-questions-falsification/A10-draft-1`.

1. [A1](./A1_KERNEL_PURPOSE_AND_NON_GOALS.md) / [RU](./A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md)
2. [A2](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md) / [RU](./A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.ru.md)
3. [A3](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.md) / [RU](./A3_ABSTRACT_NATIVE_KERNEL_MACHINE.ru.md)
4. [A4](./A4_SEMANTIC_LAWS_AND_INVARIANTS.md) / [RU](./A4_SEMANTIC_LAWS_AND_INVARIANTS.ru.md)
5. [A5](./A5_IDENTITY_TIME_AND_CHANGE.md) / [RU](./A5_IDENTITY_TIME_AND_CHANGE.ru.md)
6. [A6](./A6_KNOWLEDGE_LIFECYCLE.md) / [RU](./A6_KNOWLEDGE_LIFECYCLE.ru.md)
7. [A7](./A7_CONFLICT_UNCERTAINTY_AND_REVISION.md) / [RU](./A7_CONFLICT_UNCERTAINTY_AND_REVISION.ru.md)
8. [A8](./A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md) / [RU](./A8_SUBSTRATE_INDEPENDENCE_CONTRACT.ru.md)
9. [A9](./A9_REFERENCE_LABORATORY_BOUNDARY.md) / [RU](./A9_REFERENCE_LABORATORY_BOUNDARY.ru.md)
10. [A10](./A10_OPEN_QUESTIONS_AND_FALSIFICATION.md) / [RU](./A10_OPEN_QUESTIONS_AND_FALSIFICATION.ru.md)

## 3. Integrated and independent review lineage

The first integrated review remains preserved as `nk-integrated-blueprint-review/A1-A10-review-1`, historical state `COMPLETED / PROVISIONAL / OPERATOR_DECISION_PENDING`. It reconciled seven cross-slice findings and found no known remaining blocking internal semantic contradiction in that pass; it was explicitly **not** independent validation.

Stable gate token: `INTEGRATED_A1_A10_REVIEW`.

ADR-0026 then authorized Option D. The qualifying independent challenge is preserved separately in IAR-1 result and reconciliation records:

- review process: `QUALIFYING_REVIEW_COMPLETE`;
- findings: `10 total / 7 BLOCKING / 3 MATERIAL`;
- reconciliation: `IAR-1-R1 / COMPLETE`;
- open blocking/material findings after reconciliation: `0 / 0`.

IAR-1 does not approve the blueprint. IAR-1-R1 does not prove the refined architecture; it records explicit provisional dispositions before falsification.

## 4. Reconciled minimum architecture boundary

IAR-1 found that the first blueprint remained over-shaped by the current laboratory even after literal Python/SQL/Event disclaimers. The complete A2 inventory, A3 transition/outcome catalogue, A5 identity/time inventory, A6 lifecycle graph, Receipt-shaped accountability, Event-log-shaped history, exact replay and exact reconstruction therefore remain **reference taxonomies/capabilities**, not the universal minimum Kernel shape.

The smaller current candidate minimum is problem-level:

```text
representation / Claim are not silently reality / truth
scope / Context / warrant-provenance / Authority assumptions explicit where material
Unknown / uncertainty / unsupported remain explicit
change / revision / supersession / retention / loss accountable for declared scope
equivalence / degradation / loss judged against preregistered observables and failure rules
```

A future realization may use snapshots, witnesses, bounded summaries, procedural accounts, or another state/change model if the preregistered obligations for its scope are preserved.

## 5. Reference laboratory boundary

P1–C5 remains `BOUNDED_REFERENCE_LABORATORY`. Python, PostgreSQL, SQLite, SQL, JSON, SHA-256, current Event/reducer/Receipt/sequence mechanisms, CI and evidence packaging remain profile/laboratory mechanisms unless a later architecture decision establishes otherwise.

```text
useful implementation evidence ≠ architecture requirement
PostgreSQL ↔ SQLite C3 ≠ independent-language equivalence
bounded accountability ≠ exact reconstruction
history visibility ≠ mandatory Event sourcing
local conformance ≠ composition/federation conformance
substrate-independent specification ≠ universal portability proof
```

## 6. Runtime freeze

Allowed while frozen: architecture research; execution-admission packaging derived from the frozen BPV-1 plan; integrity/security/reproducibility/provenance fixes; evidence preservation; truth/validator repair; historical recovery; and later isolated falsification execution only after separate admission.

Not authorized: subject implementation/execution before admission; reducer-v2; new semantic Event verbs; product database/language/model/integration profiles; executable NK-EPI/Temporal/full Admission; deletion execution expansion; Final Canon; maturity or production promotion.

## 7. Pending operator-controlled decisions

- Issue #18 license/publication: unchanged / operator-controlled.
- Issue #74 / ADR-0024: `PROPOSED / PENDING_OPERATOR`; reducer-v2 unauthorized.
- ADR-0003: `PROPOSED / NOT_STARTED`.
- Track H source admission: operator-controlled.

## 8. Current progress

```text
Blueprint content: A1-A10 DRAFTED / PROVISIONAL / RECONCILED BY OVERLAY
Integrated review: COMPLETED / PROVISIONAL
Operator post-blueprint decision: OPTION D / ADR-0026 / APPROVED
Independent architecture review: IAR-1 / QUALIFYING_REVIEW_COMPLETE
IAR-1 findings: 10 total / 7 BLOCKING / 3 MATERIAL
Review finding reconciliation: IAR-1-R1 / COMPLETE
Open BLOCKING findings: 0
Open MATERIAL findings: 0
BPV-1 plan: BPV1-001-cross-lineage-bounded-accountability-v1 / PREREGISTERED
Authoritative plan merge: a538d7f1e28858a88b9ee777ac7d6e05b85943db
Next bounded gate: BPV1_EXECUTION_ADMISSION
BPV-1 execution: BLOCKED_PENDING_EXECUTION_ADMISSION
Runtime expansion: FROZEN
Existing P1–C5 laboratory: PRESERVED / BOUNDED
Production authorization: false
```

## 9. BPV-1 preregistration and execution-admission gate

The authoritative plan is [BPV1_PREREGISTRATION](./research/BPV1_PREREGISTRATION.md) / [RU](./research/BPV1_PREREGISTRATION.ru.md) / [JSON](./research/BPV1_PREREGISTRATION.json). It was merged by PR #110 as `a538d7f1e28858a88b9ee777ac7d6e05b85943db`.

It freezes before execution exactly:

```text
scenario_id
purpose_scope
mandatory_obligations
applicability_rules
mandatory_observables
equivalence_predicates
allowed_declared_losses
failure_thresholds
hard_refutation_observations
grounding_mode
threat_model
oracle_authority
```

`BPV1-001` specifies a single-node, non-composed, conventional-digital, cross-language Rust falsification instrument with bounded durable semantic state and no authoritative per-operation Event log. Rust is an experimental instrument only, not Canon or a product profile. Independent team/custody and independent computation model are `NOT_ESTABLISHED`.

Post-execution changes to normative fields invalidate the run and require a new scenario identity.

The next gate, `BPV1_EXECUTION_ADMISSION`, must bind the frozen plan/digest, machine-readable fixtures, standalone evaluator tests, pinned Rust toolchain/source boundary, and static no-product-integration audit **before** any subject execution.

## 10. Required threat and grounding boundary

The preregistered plan declares protected meanings, trust assumptions and adversarial cases including forgery, truncation, rollback, equivocation, withheld counterevidence and unavailable/forged Authority where applicable.

Context/Provenance/Authority evaluation uses an explicit finite grounding mode rather than infinite recursive metadata. Physical/cryptographic erasure is outside BPV1-001 scope because independent physical substrate observability is absent; no stronger erasure claim may be inferred.

## 11. Current sequence and hard stop

```text
IAR-1 qualifying review                       COMPLETE
IAR-1-R1 reconciliation                       COMPLETE
BPV1_PLAN_AND_PREREGISTRATION                 COMPLETE / PR #110
BPV1_EXECUTION_ADMISSION                      NEXT
BPV-1 bounded cross-lineage falsification     BLOCKED_PENDING_EXECUTION_ADMISSION
A10 outcome classification                    BLOCKED BY BPV-1
integrated re-review                           BLOCKED BY OUTCOMES
separate operator Canon/runtime decision      BLOCKED BY RE-REVIEW
```

`BPV1_EXECUTION_ADMISSION` may admit only the bounded preregistered falsification instrument. It is not A11, not product runtime thaw, not Final Canon and not production authorization.

### Historical IAR-1-R1 publication-time markers

The following strings are retained only as historical R1 publication-time state and **do not describe the current gate**:

```text
Next bounded gate: BPV1_PLAN_AND_PREREGISTRATION
BPV-1 execution: BLOCKED_PENDING_PREREGISTERED_PLAN
```

# 🧬 Architecture Re-foundation — Blueprint before Runtime

**[English](./ARCHITECTURE_REFOUNDATION.md) · [Русский](./ARCHITECTURE_REFOUNDATION.ru.md)**

> **State:** `ACTIVE / POST-BLUEPRINT VALIDATION / IAR-1 RECONCILED / BPV1 PLAN NEXT / RUNTIME EXPANSION FROZEN`  
> **Blueprint decision:** [`ADR-0025`](./adr/0025-blueprint-before-runtime-expansion.md)  
> **Post-blueprint decision:** [`ADR-0026`](./adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md)  
> **Issue:** [#88](https://github.com/velantrian/velantrim-native-kernel/issues/88)

## 1. Why this phase exists

Native Kernel studies a technology-neutral architecture for meaning, memory, knowledge, provenance, uncertainty, change and accountability. The existing **Python + PostgreSQL + SQLite** lineage is retained as a bounded reference laboratory rather than promoted into Canon because it exists first.

```text
A1 purpose / non-goals
→ A2 ontology
→ A3 abstract machine
→ A4 semantic laws
→ A5 identity / time / change
→ A6 lifecycle
→ A7 conflict / uncertainty / revision
→ A8 substrate-independence
→ A9 reference-laboratory boundary
→ A10 open questions / falsification
→ integrated A1-A10 review
→ operator post-blueprint decision
→ independent architecture review             COMPLETE / IAR-1
→ review finding reconciliation               COMPLETE / IAR-1-R1
→ BPV1 plan and preregistration               NEXT
→ bounded cross-lineage falsification         BLOCKED UNTIL PLAN IS AUTHORITATIVE
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

The first integrated review remains preserved as:

- [Integrated A1–A10 Review](./INTEGRATED_A1_A10_REVIEW.md)
- [Russian review](./INTEGRATED_A1_A10_REVIEW.ru.md)
- identity: `nk-integrated-blueprint-review/A1-A10-review-1`
- historical state: `COMPLETED / PROVISIONAL / OPERATOR_DECISION_PENDING`

The integrated review reconciled seven cross-slice findings and found no known remaining blocking internal semantic contradiction in that pass. It was explicitly **not** independent validation.

ADR-0026 then authorized Option D. The qualifying independent challenge is now preserved separately as:

- [IAR-1 result](./reviews/IAR-1_RESULT.md) / [RU](./reviews/IAR-1_RESULT.ru.md) / [JSON](./reviews/IAR-1_RESULT.json)
- [IAR-1 reconciliation](./reviews/IAR-1_RECONCILIATION.md) / [RU](./reviews/IAR-1_RECONCILIATION.ru.md) / [JSON](./reviews/IAR-1_RECONCILIATION.json)
- review process outcome: `QUALIFYING_REVIEW_COMPLETE`
- findings: `10 total / 7 BLOCKING / 3 MATERIAL`
- reconciliation identity: `IAR-1-R1`
- reconciliation state: `COMPLETE`

IAR-1 does not approve the blueprint. It attacks it. IAR-1-R1 does not prove the refined architecture; it records explicit provisional dispositions needed before falsification planning.

## 4. Reconciled minimum architecture boundary

IAR-1 found that the first blueprint remained over-shaped by the current laboratory even after literal Python/SQL/Event disclaimers. Therefore the following remain **reference taxonomies**, not the universal minimum Kernel shape:

- the complete A2 inventory;
- A3 `K → K′`, fixed transition-family catalogue and common outcome vocabulary;
- A5's full seven-identity/eight-time inventory as a mandatory whole;
- A6's nine lifecycle positions;
- Receipt-shaped accountability;
- Event-log-shaped history;
- exact replay or exact reconstruction.

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

Allowed while frozen: architecture research; BPV-1 plan/preregistration; integrity/security/reproducibility/provenance fixes; evidence preservation; truth/validator repair; historical recovery; and later isolated falsification execution only after its preregistered plan becomes authoritative.

Not authorized automatically: BPV-1 execution before that plan; reducer-v2; new semantic Event verbs; product database/language/model/integration profiles; executable NK-EPI/Temporal/full Admission; deletion execution expansion; Final Canon; maturity or production promotion.

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
Next bounded gate: BPV1_PLAN_AND_PREREGISTRATION
BPV-1 execution: BLOCKED_PENDING_PREREGISTERED_PLAN
Runtime expansion: FROZEN
Existing P1–C5 laboratory: PRESERVED / BOUNDED
Production authorization: false
```

## 9. BPV-1 preregistration gate

The original independent-review protocol is preserved as the normative review method:

- [Independent Architecture Review Protocol](./INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md)
- [Russian protocol](./INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.ru.md)
- identity: `nk-independent-architecture-review/1`

Its header describes the protocol's publication-time state and is historical with respect to the completed IAR-1. Current live review outcome is recorded in IAR-1 result/reconciliation records and `project-state.json`.

Before BPV-1 implementation/execution, an authoritative plan must preregister:

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

The implementation under test may not decide its own normative oracle after execution. Post-execution changes to mandatory obligations, applicability, equivalence predicates or failure thresholds invalidate the run for the claimed scope and require a new experiment identity.

## 10. Required threat and grounding boundary

Where materially relevant, BPV-1 planning must declare protected meanings, trust roots/assumptions and adversarial cases including forgery, fork, truncation, rollback, equivocation, withheld counterevidence, unavailable/colluding witnesses and compromised certifier.

Context/Provenance/Authority chains must terminate through an explicit finite grounding mode:

```text
EXTERNALLY_ATTESTED_ROOT
EXPLICIT_ASSUMED_ROOT
BOUNDED_RECURSIVE_CLOSURE
DECLARED_CYCLE
TERMINAL_UNKNOWN_OR_GAP
```

Physical/cryptographic erasure cannot be promoted from unverified self-assertion; absent sufficient threat-scoped evidence the correct outcome remains `INDETERMINATE`.

## 11. Current sequence and hard stop

```text
IAR-1 qualifying review                       COMPLETE
IAR-1-R1 reconciliation                       COMPLETE
BPV1_PLAN_AND_PREREGISTRATION                 NEXT
BPV-1 bounded cross-lineage falsification     BLOCKED_PENDING_PREREGISTERED_PLAN
A10 outcome classification                    BLOCKED BY BPV-1
integrated re-review                           BLOCKED BY OUTCOMES
separate operator Canon/runtime decision      BLOCKED BY RE-REVIEW
```

`BPV1_PLAN_AND_PREREGISTRATION` authorizes design/preregistration only. It is not A11, not experiment execution, not runtime thaw, not Final Canon, and not production authorization.
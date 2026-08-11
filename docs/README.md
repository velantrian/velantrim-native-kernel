# 📚 Native Kernel Documentation

**[English](./README.md) · [Русский](./README.ru.md)**

> **Current boundary:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`  
> **Active phase:** `POST-BLUEPRINT VALIDATION / BPV1 PREREGISTERED / EXECUTION ADMISSION NEXT / RUNTIME EXPANSION FROZEN`

## Start here

| Document | Role |
|---|---|
| [`../STATUS.md`](../STATUS.md) | authoritative human current state |
| [`../project-state.json`](../project-state.json) | committed machine state (`nk-project-state/2`) |
| [`../ROADMAP.md`](../ROADMAP.md) | active sequence and authorization boundaries |
| [`ARCHITECTURE_REFOUNDATION.md`](./ARCHITECTURE_REFOUNDATION.md) | blueprint/refoundation history and current validation gate |
| [`INTEGRATED_A1_A10_REVIEW.md`](./INTEGRATED_A1_A10_REVIEW.md) | historical integrated review / provisional reconciliation |
| [`INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md`](./INDEPENDENT_ARCHITECTURE_REVIEW_PROTOCOL.md) | normative independent-review protocol; publication-time status is historical |
| [`reviews/IAR-1_RESULT.md`](./reviews/IAR-1_RESULT.md) / [`RU`](./reviews/IAR-1_RESULT.ru.md) / [`JSON`](./reviews/IAR-1_RESULT.json) | qualifying independent review result |
| [`reviews/IAR-1_RECONCILIATION.md`](./reviews/IAR-1_RECONCILIATION.md) / [`RU`](./reviews/IAR-1_RECONCILIATION.ru.md) / [`JSON`](./reviews/IAR-1_RECONCILIATION.json) | provisional architecture reconciliation |
| [`research/BPV1_PREREGISTRATION.md`](./research/BPV1_PREREGISTRATION.md) / [`RU`](./research/BPV1_PREREGISTRATION.ru.md) / [`JSON`](./research/BPV1_PREREGISTRATION.json) | authoritative BPV-1 preregistration; execution not authorized |
| [`adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md`](./adr/0026-independent-challenge-before-bounded-cross-lineage-falsification.md) | operator-approved Option D decision |
| [`ai/CURRENT_STATE.md`](./ai/CURRENT_STATE.md) | compact AI current state |
| [`../AGENTS.md`](../AGENTS.md) | mandatory repository instructions |

A1–A10 first-draft documents remain preserved and `DRAFTED / PROVISIONAL / RECONCILED BY OVERLAY`.

## Reading order

```text
STATUS + project-state
→ ROADMAP
→ Architecture Re-foundation
→ A1–A10 first drafts
→ Integrated A1–A10 Review
→ ADR-0026 Option D
→ Independent Architecture Review Protocol
→ IAR-1 result
→ IAR-1-R1 reconciliation
→ BPV-1 preregistration
→ relevant accepted contracts/ADRs
→ reference runtime/tests/evidence
```

## Current map

```text
H historical recovery: OPEN / BLOCKED / independent
C clean implementation: PRESERVED / PARTIAL / BOUNDED REFERENCE LABORATORY
R post-blueprint validation: ACTIVE / BPV1-PREREGISTERED / EXECUTION-ADMISSION-NEXT
blueprint content: A1-A10 DRAFTED / PROVISIONAL / RECONCILED BY OVERLAY
integrated review: COMPLETED / PROVISIONAL
operator post-blueprint choice: OPTION D / ADR-0026 / APPROVED
independent architecture review: IAR-1 / QUALIFYING_REVIEW_COMPLETE
IAR-1 findings: 10 total / 7 BLOCKING / 3 MATERIAL
IAR-1-R1: COMPLETE / open blockers 0 / open material 0
BPV-1 plan: BPV1-001-cross-lineage-bounded-accountability-v1 / PREREGISTERED / EXECUTION_NOT_AUTHORIZED
plan merge: a538d7f1e28858a88b9ee777ac7d6e05b85943db
next gate: BPV1_EXECUTION_ADMISSION
BPV-1 execution: BLOCKED_PENDING_EXECUTION_ADMISSION
kernel runtime: C4
operational validation: C5_BOUNDED_REHEARSAL
assertions: 45 / 10 / 17 / 0
NK-EPI: 0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
production: NOT AUTHORIZED
runtime expansion: FROZEN
```

Integrated review identity: `nk-integrated-blueprint-review/A1-A10-review-1`. Independent-review protocol identity: `nk-independent-architecture-review/1`. Reconciliation identity: `IAR-1-R1`. BPV-1 plan identity: `BPV1-001-cross-lineage-bounded-accountability-v1`.

## Current reconciled distinctions

```text
PHYSICALLY_ERASED ≠ CRYPTOGRAPHICALLY_ERASED
physical/crypto erasure assertion ≠ independently verified substrate condition
FORGOTTEN_OR_LOST ≠ deliberate erasure claim
Uncertainty ≠ one universal confidence scalar
Conflict ≠ necessarily Contradiction
A3 transition catalogue ≠ mandatory Kernel shape
A6 lifecycle positions ≠ mandatory Kernel shape
bounded accountability ≠ exact reconstruction
history visibility ≠ mandatory Event sourcing
local scoped conformance ≠ composition/federation conformance
A10 outcome protocol = SUPPORTED_FOR_SCOPE / WEAKENED / REFUTED / INDETERMINATE / NOT_TESTED
NOT_TESTED ≠ SUPPORTED
reference laboratory ≠ final architecture
existing mechanism ≠ architecture requirement
substrate-independent specification ≠ universal portability proof
qualifying independent review ≠ architecture proof
review reconciliation ≠ BPV-1 execution authorization
preregistered plan ≠ BPV-1 execution authorization
falsification instrument ≠ product runtime
```

## Hard stop

`BPV1_EXECUTION_ADMISSION` is the next gate. BPV-1 subject implementation/execution cannot begin until the admission checkpoint binds the frozen plan/digest, machine-readable fixture/oracle package, standalone evaluator tests, pinned Rust toolchain/source boundary and static no-product-integration audit. Runtime remains `FROZEN`; A1–A10 remain provisional. Issue #18, Issue #74 / ADR-0024, ADR-0003 and Track H remain unchanged/operator-controlled.

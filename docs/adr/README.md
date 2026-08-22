<!-- H11_EXECUTION_ADMISSION_BLOCKED_CURRENT -->
> [!IMPORTANT]
> **Current research boundary — 2026-08-22.** Architecture remains provisional and interpreted through Integrated Review / IAR-1 / IAR-1-R1. Final Canon is deferred. The selected residual family is `A10-H11`; current gate `A10_H11_EXECUTION_ADMISSION` is `BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER`; reviewer/reproducer `NOT_ESTABLISHED`; H11 `NOT_TESTED`; runtime `FROZEN`; production `false`. ADR-0024 is accepted for its bounded abstract-contract scope but does not authorize reducer-v2 runtime.

# 📝 Architecture Decision Records

[← Project README](../../README.md) · [Русский README](../../README.ru.md) · [Decision process](../DECISION_PROCESS.md) · [Research RFCs](../rfc/README.md)

ADRs preserve why durable architectural, profile, evidence, and research-priority boundaries exist. Acceptance is not empirical proof.

## Independent dimensions

```text
Decision status
≠ Evidence level
≠ Implementation status
≠ Operator approval
```

## Index

| ADR | Title | Decision | Evidence | Implementation | Approval |
|---|---|---|---|---|---|
| [`0001`](./0001-architecture-canon-vs-implementation-profiles.md) | Canon vs Implementation Profiles | `ACCEPTED` | C3/C4 bounded evidence | partial profiles | `APPROVED` |
| [`0002`](./0002-state-checkpoints-are-disposable.md) | State checkpoints are disposable | `PROPOSED` | P3–C5 mechanisms reproduced | bounded mechanism | `NOT_REQUESTED` |
| [`0003`](./0003-semantic-conflicts-require-explicit-resolution.md) | Semantic conflicts require explicit resolution | `PROPOSED` | `DOCUMENTED` | mostly unsupported | `NOT_REQUESTED` |
| [`0004`](./0004-rebuild-from-authoritative-history.md) | Rebuild is the first conformance experiment | `PROPOSED` | P3–C5 mechanisms reproduced | bounded mechanism | `NOT_REQUESTED` |
| [`0005`](./0005-curiosity-core-is-optional-and-non-authoritative.md) | Curiosity Core is optional | `PROPOSED` | `DOCUMENTED` | `NOT_STARTED` | `NOT_REQUESTED` |
| [`0006`](./0006-causal-links-are-relations.md) | Causal links are relations | `ACCEPTED` | `DOCUMENTED` | selected relation path exists | `APPROVED` |
| [`0007`](./0007-operator-approval-is-not-evidence.md) | Operator approval is not evidence | `ACCEPTED` | `DOCUMENTED` | governance implemented | `APPROVED` |
| [`0008`](./0008-epistemic-boundaries-are-representation-disciplines.md) | Epistemic boundaries are representation disciplines | `PROPOSED` | fixtures described; runtime unsupported | `NOT_STARTED` | `PENDING` |
| [`0009`](./0009-postgresql-primary-sqlite-optional-profile.md) | PostgreSQL primary; SQLite optional | `ACCEPTED` | PostgreSQL/SQLite C2, C3, C4, C5 | both profiles partial | `APPROVED` |
| [`0010`](./0010-foundational-contract-families.md) | Foundational contract families | `ACCEPTED` | assertion maps through C5 | partial | `APPROVED` |
| [`0011`](./0011-canonical-identity-contract-v1.md) | Canonical identity contract v1 | `ACCEPTED` | C2/C3/C4/C5 checks | selected assertions supported/partial | `APPROVED` |
| [`0012`](./0012-single-writer-append-and-replay-contract-v1.md) | Append and replay contract v1 | `ACCEPTED` | P2–C5 repository evidence | bounded paths partial | `APPROVED` |
| [`0013`](./0013-deletion-restriction-retention-contract-v1.md) | Deletion/restriction/retention v1 | `ACCEPTED` | semantic and C5 checks | physical execution absent | `APPROVED` |
| [`0014`](./0014-executable-conformance-fixture-protocol-v1.md) | Executable fixture/evidence protocol v1 | `ACCEPTED` | P4–C5 reports/artifacts | two profiles + evaluators | `APPROVED` |
| [`0015`](./0015-accept-clean-profile-and-authorize-p1-semantic-core.md) | Accept clean lineage and authorize P1 | `ACCEPTED` | P1 and later regressions | `PARTIAL — P1` | `APPROVED` |
| [`0016`](./0016-authorize-p2-postgresql-append-profile.md) | Authorize P2 PostgreSQL append | `ACCEPTED` | repository reproduced | `PARTIAL — P2` | `APPROVED` |
| [`0017`](./0017-authorize-p3-replay-projection-receipts.md) | Authorize P3 replay/projections/Receipts | `ACCEPTED` | repository reproduced | `PARTIAL — P3` | `APPROVED` |
| [`0018`](./0018-authorize-p4-assertion-scoped-conformance.md) | Authorize P4 assertion-scoped conformance | `ACCEPTED` | C2 | `PARTIAL — P4` | `APPROVED` |
| [`0019`](./0019-authorize-p5-sqlite-and-c3-equivalence.md) | Authorize P5 SQLite and C3 equivalence | `ACCEPTED` | C2/C3 | `PARTIAL — P5` | `APPROVED` |
| [`0020`](./0020-authorize-c4-offline-shadow-evaluation.md) | Authorize C4 offline shadow evaluation | `ACCEPTED` | approved dataset + C3 + reports | `PARTIAL — C4` | `APPROVED` |
| [`0021`](./0021-authorize-c5-bounded-operational-rehearsal.md) | Authorize C5 bounded operational rehearsal | `ACCEPTED` | two passing checkpoints + retained ZIPs | `PARTIAL — C5` | `APPROVED` |
| [`0022`](./0022-preserve-c5-evidence-and-declare-project-state.md) | Preserve C5 evidence and declare project state | `ACCEPTED` | repository and post-merge validation passed | implemented; current state uses `nk-project-state/2` | `APPROVED` |
| [`0023`](./0023-harden-sqlite-wal-and-event-integrity.md) | Harden SQLite WAL and stored Event integrity | `ACCEPTED` | repository-reproduced; additive evidence captured | merged via PR #69 + follow-up PR #72 | `APPROVED` |
| [`0024`](./0024-version-reducer-referential-semantics.md) | Version reducer referential semantics without rewriting history | `ACCEPTED` | `DOCUMENTED`; reducer-v1 lineage trace retained | `NOT_STARTED` | `APPROVED — ACCEPT_WITH_CHANGES` |
| [`0025`](./0025-blueprint-before-runtime-expansion.md) | Complete the architecture blueprint before further runtime expansion | `ACCEPTED` | `DOCUMENTED` | blueprint drafted/reviewed provisionally; runtime freeze active | `APPROVED` |
| [`0026`](./0026-independent-challenge-before-bounded-cross-lineage-falsification.md) | Independent challenge before bounded cross-lineage falsification | `ACCEPTED` | IAR-1 + IAR-1-R1 + BPV-1 / residual-A10 evidence | `GOVERNANCE_PARTIAL` / H11 admission blocked | `APPROVED` |
| [`0027`](./0027-retain-provisional-architecture-and-runtime-freeze-after-option-d.md) | Retain provisional architecture and runtime freeze after Option D | `ACCEPTED` | `REPOSITORY_REPRODUCED` | governance complete; residual validation active | `APPROVED` |

> **ADR-0024 navigation note:** [`0024-operator-decision-package.md`](./0024-operator-decision-package.md) is the supporting operator-decision package and provenance for the accepted `ACCEPT_WITH_CHANGES` decision, not a second ADR. The normative accepted contract is [`0024-version-reducer-referential-semantics.md`](./0024-version-reducer-referential-semantics.md).

## Current boundary

```text
H historical recovery: OPEN / BLOCKED / operator-controlled source admission
C clean implementation: P1–P5 + C4 + C5 / BOUNDED_REFERENCE_LABORATORY
R post-blueprint validation: ACTIVE / H11 EXECUTION ADMISSION BLOCKED
selected family: A10-H11
current gate: A10_H11_EXECUTION_ADMISSION
admission: BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER
reviewer/reproducer: NOT_ESTABLISHED
H11: NOT_TESTED
kernel_runtime_conformance: C4
operational_validation: C5_BOUNDED_REHEARSAL
assertion map: 45 / 10 / 17 / 0
NK-EPI: 0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
Final Canon: DEFERRED / NOT AUTHORIZED
production: NOT AUTHORIZED
runtime expansion: FROZEN
```

## Active architecture / research gate

```text
ADR-0024 — Version reducer referential semantics
  ACCEPTED / OPERATOR APPROVED / ACCEPT_WITH_CHANGES
  implementation: NOT_STARTED
  reducer-v2 runtime: NOT AUTHORIZED
  reducer-v1 historical semantics: IMMUTABLE

ADR-0025 — Blueprint before Runtime
  ACCEPTED / OPERATOR APPROVED
  A1-A10 first drafts + integrated review complete/provisional

ADR-0026 — Post-Blueprint Validation / Option D
  ACCEPTED / OPERATOR APPROVED
  independent architecture review: IAR-1 / QUALIFYING_REVIEW_COMPLETE
  reconciliation: IAR-1-R1 / COMPLETE
  BPV-1 + D6/D7/D8: COMPLETE for their recorded scope
  residual A10 plan: RAVP-001 / COMPLETE
  selected residual family: A10-H11
  H11 preregistration: COMPLETE / EXECUTION_NOT_AUTHORIZED
  H11 execution admission: BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER
  H11 outcome: NOT_TESTED
  product runtime thaw: NO

Issue #18 — license/publication terms
  PENDING_OPERATOR
```

Residual validation order remains planning guidance only. H11 cannot execute until qualifying reviewer/reproducer evidence exists and execution admission is separately reassessed.

## Operational rules

1. Multi-model agreement is input, not approval.
2. Proposed decisions must not be summarized as implemented behavior.
3. `ACCEPTED` does not mean complete runtime or empirical proof.
4. Evidence must link exact checks, bytes, digests, reports, commits, runs, or artifacts.
5. Approval and evidence remain separate.
6. Reproducible evidence does not silently promote proposals.
7. Historical reasoning remains after supersession.
8. Issue #1 remains separate from clean implementation.
9. Translation preserves decision/evidence/implementation/approval meaning.
10. A Receipt/report/archive is bounded evidence, not truth, authenticity, or physical-erasure proof.
11. C2/C3/C4/C5 labels include assertion counts and support state.
12. C3 semantic equivalence is not operational equivalence or independent implementation.
13. C5 operational evidence cannot promote NK-EPI.
14. Research notes cannot authorize runtime or Canon changes.
15. Dataset, plan, or bundle changes require new identity/digest and evidence.
16. Reducer semantics may not change for an existing history through a process-local default or silent version upgrade.
17. Portable semantic commitments and operational/profile receipts must not be collapsed without an accepted contract.
18. A public repository does not imply an open-source license.
19. Existing implementation profiles cannot define Canon merely by being implemented first.
20. ADR-0025 permits maintenance and falsification instruments, not automatic semantic/runtime expansion.
21. ADR-0026 permits independent challenge and bounded falsification only under explicit review/reconciliation/preregistration/admission gates; it does not thaw product runtime.
22. A qualifying independent review may not be self-certified by the same authorship lineage.
23. Frozen normative fields cannot be post-hoc respecified to rescue an experiment.
24. Preregistration ≠ execution authorization; execution admission is separate.
25. Bounded results may weaken/refute architecture claims; they never promote Canon or runtime automatically.
26. ADR-0024 acceptance authorizes its abstract contract only; reducer-v2 implementation requires a separate explicit authorization gate.

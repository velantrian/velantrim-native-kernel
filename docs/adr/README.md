# 📝 Architecture Decision Records

[← Project README](../../README.md) · [Русский README](../../README.ru.md) · [Decision process](../DECISION_PROCESS.md) · [Research RFCs](../rfc/README.md)

ADRs preserve why durable architectural, profile and evidence boundaries exist. Acceptance is not empirical proof.

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
| [`0022`](./0022-preserve-c5-evidence-and-declare-project-state.md) | Preserve C5 evidence and declare project state | `ACCEPTED` | local bundle/state validation; CI pending | implemented in change | `APPROVED` |
| [`0023`](./0023-harden-sqlite-wal-and-event-integrity.md) | Harden SQLite WAL and stored Event integrity | `ACCEPTED` | local tests; repository reproduction pending | implemented in candidate | `APPROVED` |

## Current boundary

```text
H historical recovery: OPEN / BLOCKED / independent
C clean implementation: P1–P5 + C4 + C5 / ACTIVE / PARTIAL
R long-horizon research: PROPOSED / BOUNDED
kernel_runtime_conformance: C4
operational_validation: C5_BOUNDED_REHEARSAL
assertion map: 45 / 10 / 17 / 0
NK-EPI: 0 / 8 SUPPORTED
production: NOT AUTHORIZED
```

## Operational rules

1. Multi-model agreement is input, not approval.
2. Proposed decisions must not be summarized as implemented behavior.
3. `ACCEPTED` does not mean complete runtime.
4. Evidence must link exact checks, bytes, digests, reports, commits, runs or artifacts.
5. Approval and evidence remain separate.
6. Reproducible evidence does not silently promote proposals.
7. Historical reasoning remains after supersession.
8. Issue #1 remains separate from clean implementation.
9. Translation preserves decision/evidence/implementation/approval meaning.
10. A Receipt/report/archive is bounded evidence, not truth, authenticity or physical-erasure proof.
11. C2/C3/C4/C5 labels include assertion counts and support state.
12. C3 semantic equivalence is not operational equivalence.
13. C5 operational evidence cannot promote NK-EPI.
14. Research notes cannot authorize runtime or Canon changes.
15. Dataset, plan or bundle changes require new identity/digest and evidence.

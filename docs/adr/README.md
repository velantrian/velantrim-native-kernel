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
| [`0001`](./0001-architecture-canon-vs-implementation-profiles.md) | Canon vs Implementation Profiles | `ACCEPTED` | `DOCUMENTED` | documentation complete; portability bounded by C3/C4 evidence | `APPROVED` |
| [`0002`](./0002-state-checkpoints-are-disposable.md) | State checkpoints are disposable | `PROPOSED` | P3–C4 mechanisms reproduced; ADR not promoted | bounded mechanism exists | `NOT_REQUESTED` |
| [`0003`](./0003-semantic-conflicts-require-explicit-resolution.md) | Semantic conflicts require explicit resolution | `PROPOSED` | `DOCUMENTED` | mostly unsupported | `NOT_REQUESTED` |
| [`0004`](./0004-rebuild-from-authoritative-history.md) | Rebuild is the first conformance experiment | `PROPOSED` | P3–C4 mechanisms reproduced; ADR not promoted | bounded mechanism exists | `NOT_REQUESTED` |
| [`0005`](./0005-curiosity-core-is-optional-and-non-authoritative.md) | Curiosity Core is optional | `PROPOSED` | `DOCUMENTED` | `NOT_STARTED` | `NOT_REQUESTED` |
| [`0006`](./0006-causal-links-are-relations.md) | Causal links are relations | `ACCEPTED` | `DOCUMENTED` | selected semantic relation path exists | `APPROVED` |
| [`0007`](./0007-operator-approval-is-not-evidence.md) | Operator approval is not evidence | `ACCEPTED` | `DOCUMENTED` | governance implemented | `APPROVED` |
| [`0008`](./0008-epistemic-boundaries-are-representation-disciplines.md) | Epistemic boundaries are representation disciplines | `PROPOSED` | fixtures exist; C4 reports unsupported | `NOT_STARTED` | `PENDING` |
| [`0009`](./0009-postgresql-primary-sqlite-optional-profile.md) | PostgreSQL primary; SQLite optional | `ACCEPTED` | PostgreSQL/SQLite C2, C3 and bounded C4 evidence | both profiles partial | `APPROVED` |
| [`0010`](./0010-foundational-contract-families.md) | Foundational contract families | `ACCEPTED` | assertion maps through C4 | profile support remains partial | `APPROVED` |
| [`0011`](./0011-canonical-identity-contract-v1.md) | Canonical identity contract v1 | `ACCEPTED` | C2/C3/C4 identity checks | selected identity assertions supported/partial | `APPROVED` |
| [`0012`](./0012-single-writer-append-and-replay-contract-v1.md) | Append and replay contract v1 | `ACCEPTED` | P2–C4 repository evidence | bounded append/replay paths partial | `APPROVED` |
| [`0013`](./0013-deletion-restriction-retention-contract-v1.md) | Deletion/restriction/retention v1 | `ACCEPTED` | semantic fixtures/checks | physical execution absent | `APPROVED` |
| [`0014`](./0014-executable-conformance-fixture-protocol-v1.md) | Executable fixture/evidence protocol v1 | `ACCEPTED` | P4/P5/C4 reports and artifacts | implemented for two profiles plus offline evaluator | `APPROVED` |
| [`0015`](./0015-accept-clean-profile-and-authorize-p1-semantic-core.md) | Accept clean lineage and authorize P1 | `ACCEPTED` | P1 and later regressions | `PARTIAL — P1` | `APPROVED` |
| [`0016`](./0016-authorize-p2-postgresql-append-profile.md) | Authorize P2 PostgreSQL append | `ACCEPTED` | `REPOSITORY_REPRODUCED` | `PARTIAL — P2` | `APPROVED` |
| [`0017`](./0017-authorize-p3-replay-projection-receipts.md) | Authorize P3 replay/projections/Receipts | `ACCEPTED` | `REPOSITORY_REPRODUCED` | `PARTIAL — P3` | `APPROVED` |
| [`0018`](./0018-authorize-p4-assertion-scoped-conformance.md) | Authorize P4 assertion-scoped conformance | `ACCEPTED` | C2 with retained artifacts | `PARTIAL — P4`; 41/13/18 | `APPROVED` |
| [`0019`](./0019-authorize-p5-sqlite-and-c3-equivalence.md) | Authorize P5 SQLite and C3 equivalence | `ACCEPTED` | C2/C3 with retained 4×3 reports | `PARTIAL — P5`; C3 45/10/17 | `APPROVED` |
| [`0020`](./0020-authorize-c4-offline-shadow-evaluation.md) | Authorize C4 offline shadow evaluation | `ACCEPTED` | approved dataset + C3 prerequisite + retained 4×4 reports | `PARTIAL — C4`; 15 cases, 45/10/17 | `APPROVED` |

## Current boundary

```text
P1–P5 clean implementation
C4 authority-free offline shadow evidence
support_state: PARTIAL
Single-profile C2: 41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED
Cross-profile C3: 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
Offline C4 scope: 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
C4 applies only to the approved immutable 15-case dataset
C4 ≠ live shadowing / authority promotion / operational equivalence
C5 ≠ authorized
```

C4 does not automatically promote ADR-0002, ADR-0003, ADR-0004, ADR-0008 or `NK-EPI`.

## Operational rules

1. Multi-model agreement is input, not approval.
2. Proposed decisions must not be summarized as implemented behavior.
3. `ACCEPTED` does not mean complete runtime.
4. Evidence must link to exact checks, dataset bytes/digest, reports, PRs, commits, runs or artifacts.
5. Approval and evidence remain separate.
6. Reproducible evidence does not silently promote proposals.
7. Historical reasoning remains after supersession.
8. Issue #1 recovery remains separate from clean implementation/evidence.
9. Translation must preserve decision/evidence/implementation/approval meaning.
10. A Receipt/report is bounded evidence, not truth, authenticity or physical-erasure proof.
11. A top-level C2/C3/C4 label must include assertion counts and `support_state`.
12. C3 requires materially independent profiles and explicit comparison evidence.
13. C3 semantic equivalence must not be described as operational equivalence.
14. C4 requires an approved immutable dataset, exact prerequisite report, no-promotion authority boundary and retained artifact.
15. Offline shadow agreement must not be described as live traffic, candidate approval or production safety.
16. Dataset/threshold changes require a new version/digest and evidence cycle.

## When an ADR is required

Create or update an ADR for changes to Canon, cross-technology contracts, identity, event/replay semantics, authority, conflict, deletion, evidence/conformance, dataset governance, promotion authority, integration boundaries, portability or major profile commitments.

Use the next available four-digit number and never reuse one. Start from [`0000-template.md`](./0000-template.md).

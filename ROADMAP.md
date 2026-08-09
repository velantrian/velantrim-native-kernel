# Roadmap

```yaml
document_role: ACTIVE_ROADMAP
status_as_of: 2026-08-09
authoritative_machine_source: project-state.json
repository_status: RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
publication_checkpoint: 10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c
```

Velantrim Native Kernel maintains three independent tracks:

```text
H — Historical Recovery
C — Clean Implementation
R — Long-Horizon Research
```

Their status, evidence and authority must never be collapsed.

## Governing sequence

```text
Architecture Canon
→ versioned abstract contract
→ failure and threat model
→ explicit decision
→ runtime implementation
→ positive and negative fixtures
→ cross-profile comparison
→ exact evidence
→ status update
→ Notion synchronization
```

Runtime must not define new semantics before the contract. Evidence must not be relabelled after the fact. Maturity does not rise automatically because more tests passed.

## Track H — Historical Recovery

**Status:** `BLOCKED / ACTIVE EVIDENCE-RECOVERY / INDEPENDENT`.

Purpose: recover authentic `v0.1.2.1` source and the original 44-test suite from permitted sources.

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
clean reconstruction ≠ authentic historical recovery
```

A candidate must be preserved read-only, hashed before extraction, inspected in isolation, recorded as `UNVERIFIED_CANDIDATE`, reviewed for provenance and accepted only by an explicit operator decision. Track H does not block Track C.

## Track C — Clean Implementation

**Status:** `ACTIVE / PARTIAL / NOT PRODUCTION-READY`.

```text
P1 semantic core                         MERGED / REPOSITORY-TESTED
P2 PostgreSQL append                     MERGED / REPOSITORY-INTEGRATION-TESTED
P3 replay / projections / Receipts       MERGED / REPOSITORY-INTEGRATION-TESTED
P4 PostgreSQL assertion conformance      MERGED / PARTIAL / C2
P5 SQLite + cross-profile comparison     MERGED / PARTIAL / C2 + C3
C4 offline shadow evaluation             MERGED / PARTIAL
C5 bounded operational rehearsal         MERGED / PARTIAL / SYNTHETIC

kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
assertion map:              45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:                     0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
production_authorized:      false
```

## Phase 0 — Truth-Surface Reconciliation

```text
0A machine-readable truth  COMPLETE / PR #80
0B human-readable truth    COMPLETE / PR #81
0C Issues and Notion       COMPLETE / PR #82 RECORD / PR #83 SYNC VERIFIED
```

PR #83 publication checkpoint is `10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c`. It published operator decision packages and preserved all maturity, evidence and authorization boundaries.

## Phase 0.5 — License and Publication Decision

**State:** `PACKAGE PREPARED / ISSUE #18 / PENDING_OPERATOR / selected_option: null`.

Until explicit selection:

```text
license change: NO
external contributions: NOT ACCEPTED
package publication: NOT AUTHORIZED
```

The operator must decide the regime for code, documentation, diagrams/media, fixtures/datasets, external contributions, patent terms, trademarks, AI-assisted contributions, recovered historical source and package publication.

## Phase 1 — ADR-0024 Final Decision

**State:** `PACKAGE PREPARED / PROPOSED / PENDING_OPERATOR / RUNTIME NOT AUTHORIZED`.

Available outcomes:

```text
ACCEPT
ACCEPT_WITH_CHANGES
REVISE
REJECT
```

The technical recommendation `ACCEPT_WITH_CHANGES` is not approval. Reducer v1 remains immutable and authoritative for existing histories and evidence. Any stricter referential behavior belongs to reducer v2 with stable failure codes and explicit migration boundaries.

## Phase 1.25 — NK-SAM and Named Equivalence

**State:** `PROPOSED / BLOCKED BY OPERATOR DECISIONS`.

Define `Apply`, `Observe`, `Equivalent`, `AssessMigration` and `Migrate`, plus named byte, structural, state, observational, trace, epistemic, authority, Receipt and probabilistic equivalence profiles. Separate semantic identity from reference encoding.

## Phase 1.5 — Event and History Commitment

**State:** `PROPOSED / REQUIRED BEFORE REDUCER-V2 HISTORIES`.

Separate portable semantic history commitment from operational/profile receipts. Classify every field as semantically committed, operationally committed, derived or uncommitted metadata. Define history-head, mutation, reorder, truncation, fork, rollback and version-substitution fixtures before signatures or witnesses.

## Phase 2 — Reducer v2

**State:** `BLOCKED BY PHASES 0.5, 1, 1.25 AND 1.5`.

Required order:

1. reducer registry and immutable v1 reader;
2. reducer v2 semantic core;
3. stable failure codes and negative fixtures;
4. instance/history version binding;
5. migration assessment without silent rewrite;
6. PostgreSQL and SQLite integration;
7. new evidence identity.

No in-place reinterpretation of reducer-v1 histories is allowed.

## Later phases

| Phase | State | Boundary |
|---|---|---|
| Independent conformance foundation | `PROPOSED` | Rust or Go requires a separate decision; Python may not be a hidden oracle. |
| Executable NK-EPI-004 | `PROPOSED / 0 OF 8 SUPPORTED` | First slice is `Unknown ≠ False`. |
| Temporal v0.1 | `PROPOSED` | Valid time, recorded time, write order, intervals and identity impact. |
| Admission v0.1 | `PROPOSED` | Admission for role/scope is not objective truth. |
| Operational deletion | `PROPOSED / NOT ESTABLISHED` | Inventory actual locations, execution, verification, retries, retention and restore. |
| Performance evidence | `PROPOSED` | Reproducible correctness before optimization. |
| Deployment-specific governance | `UNDEFINED / NOT AUTHORIZED` | No invented C6–C8 ladder; maturity is deployment-specific. |

## Current authorized work

```text
obtain explicit license/publication operator selection
→ obtain explicit ADR-0024 operator selection
→ define NK-SAM and named equivalence profiles
→ define Event/history commitment
```

Not authorized yet:

- reducer-v2 runtime;
- executable NK-EPI;
- Temporal runtime;
- full Admission;
- operational deletion;
- full Rust/Go implementation;
- Titan, Crystal or Mentaury integration;
- distributed multi-writer architecture;
- production promotion.

## Promotion rule

```text
research hypothesis
→ explicit versioned contract
→ failure and threat model
→ reproducible implementation and tests
→ negative fixtures
→ exact evidence
→ decision record
→ operator approval
```

The pre-reconciliation roadmap remains available at [publication checkpoint `626f34e…`](https://github.com/velantrian/velantrim-native-kernel/blob/626f34e6328b455258f2dd5fcf2145ec4db64a60/ROADMAP.md). It is historical context, not the active sequence.

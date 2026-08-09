# Roadmap

```yaml
document_role: ACTIVE_ROADMAP
status_as_of: 2026-08-09
authoritative_machine_source: project-state.json
repository_status: RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
```

Velantrim Native Kernel maintains three independent tracks. Their statuses, evidence and authority must never be collapsed.

```text
H — Historical Recovery
C — Clean Implementation
R — Long-Horizon Research
```

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

**Status:** `BLOCKED / ACTIVE EVIDENCE-RECOVERY / INDEPENDENT`

Purpose: recover the authentic `v0.1.2.1` source and original 44-test suite from permitted sources.

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
clean reconstruction ≠ authentic historical recovery
```

If a candidate appears:

```text
preserve original container
→ hash before extraction
→ isolated inspection
→ UNVERIFIED_CANDIDATE manifest
→ byte verification
→ provenance review
→ operator decision
```

Track H does not block Track C. No reconstructed runtime may be called authentic `v0.1.2.1` without provenance evidence.

## Track C — Clean Implementation

**Status:** `ACTIVE / PARTIAL / NOT PRODUCTION-READY`

```text
P1 semantic core                         MERGED / REPOSITORY-TESTED
P2 PostgreSQL append                     MERGED / REPOSITORY-INTEGRATION-TESTED
P3 replay / projections / Receipts       MERGED / REPOSITORY-INTEGRATION-TESTED
P4 PostgreSQL assertion conformance      MERGED / PARTIAL / C2
P5 SQLite + cross-profile comparison     MERGED / PARTIAL / C2 + C3
C4 offline shadow evaluation             MERGED / PARTIAL
C5 bounded operational rehearsal         MERGED / PARTIAL / SYNTHETIC
```

```text
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
assertion map:              45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:                     0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
production_authorized:      false
```

## Active phase sequence

### Phase 0 — Truth-Surface Reconciliation

#### 0A — Machine-readable truth

**State:** `MERGED AS PR #80 / POST-MERGE VALIDATION REQUIRED`.

Delivered:

- `nk-project-state/2`;
- non-self-referential checkpoint roles;
- registry↔project-state consistency;
- per-family implementation, fixture and evidence status;
- preserved fail-closed evidence and SQLite integrity guards.

#### 0B — Human-readable truth

**State:** `IN PROGRESS`.

Scope:

- separate current state, history, proposal, known gap and next authorized gate;
- remove stale PR/CI wording;
- replace ambiguous `0 / 8 SUPPORTED` notation with exact NK-EPI counts;
- correct profile and roadmap drift;
- preserve historical snapshots through immutable links and Git history.

#### 0C — Issues and Notion

**State:** `PENDING AFTER 0B MERGE`.

Scope:

- reconcile Issues #14–#17 without automatic closure;
- record completed scope, evidence, remaining work, next gate and non-goals;
- create a compact Notion current-state dashboard;
- separate current pages from historical reports and proposals;
- record exact GitHub publication and synchronization checkpoints.

## Phase 0.5 — License and Publication Decision

**State:** `OPEN / ISSUE #18 / OPERATOR DECISION REQUIRED`.

The operator must choose the rights regime for code, documentation, diagrams, datasets, contributions, patents, trademarks, recovered historical source and package publication.

AI agents may prepare options but must not choose or imply a license.

## Phase 1 — ADR-0024 Final Decision

**State:** `PROPOSED / APPROVAL PENDING / RUNTIME NOT STARTED`.

The operator must decide:

```text
ACCEPT
ACCEPT_WITH_CHANGES
REVISE
REJECT
```

Reducer v1 remains immutable and authoritative for existing histories and evidence. Any stricter referential behavior belongs to reducer v2 with stable failure codes and explicit migration boundaries.

## Phase 1.25 — Semantic Abstract Machine and Equivalence

**State:** `PROPOSED`.

Define the Native Kernel Semantic Abstract Machine (`NK-SAM`) and named equivalence profiles:

- byte;
- structural;
- state;
- observational;
- trace;
- epistemic;
- authority;
- Receipt;
- probabilistic.

Separate semantic identity from the reference encoding profile. No implementation may claim generic “equivalence” without naming the profile and allowed differences.

## Phase 1.5 — Event and History Commitment

**State:** `PROPOSED / REQUIRED BEFORE REDUCER-V2 HISTORIES`.

Separate:

```text
portable semantic history commitment
≠ operational/profile receipt
```

Classify every Event field as semantically committed, operationally committed, derived or uncommitted metadata. Define history-head, mutation, reorder, truncation, fork, rollback and version-substitution fixtures before considering signatures or external witnesses.

## Phase 2 — Reducer v2

**State:** `BLOCKED BY PHASES 0.5, 1, 1.25 AND 1.5`.

Bounded sequence:

1. reducer registry and immutable v1 reader;
2. reducer v2 semantic core;
3. stable failure codes and negative fixtures;
4. instance/history-level version binding;
5. migration assessment without silent rewrite;
6. PostgreSQL and SQLite integration;
7. new evidence identity.

No in-place reinterpretation of reducer-v1 histories is allowed.

## Phase 3 — Independent Conformance Foundation

**State:** `PROPOSED`.

Choose Rust or Go through an operator/engineering decision. The first independent scope should own:

- canonical identity vectors;
- Event parsing and commitment verification;
- reducer-v1 reader;
- reducer v2;
- semantic state comparison.

It must not invoke Python as a hidden oracle.

## Phase 4 — Executable NK-EPI-004

**State:** `PROPOSED / 0 OF 8 NK-EPI ASSERTIONS SUPPORTED`.

First vertical slice:

```text
Unknown ≠ False
```

Required path:

```text
representation
→ admission boundary
→ Event
→ reducer
→ state
→ projection
→ retrieval
→ query result
→ Receipt
```

Negative fixtures must reject silent conversion of missing, unanswered, unavailable, unresolved or unevaluated states into `FALSE`.

## Phase 5 — Temporal v0.1

**State:** `PROPOSED`.

Initial scope:

- valid time;
- recorded time;
- write order;
- explicit interval encoding;
- identity-impact decision;
- bounded as-of queries.

Do not silently interpret “valid at T” as objectively true at T.

## Phase 6 — Admission v0.1

**State:** `PROPOSED`.

Admission must be a replayable decision with explicit policy, authority, actor, scope, evidence references, reason codes and known limits.

```text
admitted for a role and scope ≠ objectively true
```

## Phase 7 — Independent Implementation Extension

**State:** `PROPOSED`.

Extend independent support to NK-EPI, Temporal, Admission verification and cross-language evidence. Two storage profiles sharing one semantic implementation are not full substrate-neutrality proof.

## Phase 8 — Operational Deletion

**State:** `PROPOSED / PHYSICAL DELETION NOT ESTABLISHED`.

Inventory actual locations, execution methods, verification, retries, retention and restore behavior. Resolve the conflict between immutable audit evidence and privacy/deletion obligations before making stronger claims.

## Phase 9 — Performance Evidence

**State:** `PROPOSED`.

Establish reproducible correctness, nightly and controlled-scale workloads before optimization. Every optimization must preserve semantic state, state digest, failure codes, Receipt semantics and the declared equivalence profile.

## Phase 10 — Deployment-Specific Governance and Maturity

**State:** `UNDEFINED / NOT AUTHORIZED`.

No normative C6–C8 ladder is accepted. Production readiness must be defined per deployment profile, data class, users, exposure, threat model, operations, recovery, deletion, privacy and independent review.

## Current authorized work

```text
complete Phase 0B
→ complete Phase 0C
→ prepare Phase 0.5 options
→ prepare Phase 1 decision package
→ define Phase 1.25
→ define Phase 1.5
```

Not authorized inside the current slice:

- reducer-v2 runtime;
- executable NK-EPI;
- Temporal runtime;
- full Admission;
- operational deletion;
- full Rust/Go implementation;
- Titan, Crystal or Mentaury integration;
- distributed multi-writer architecture;
- C6 or production promotion.

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

## Historical roadmap

The pre-reconciliation roadmap remains available at [publication checkpoint `626f34e…`](https://github.com/velantrian/velantrim-native-kernel/blob/626f34e6328b455258f2dd5fcf2145ec4db64a60/ROADMAP.md). It is historical context, not the active sequence.
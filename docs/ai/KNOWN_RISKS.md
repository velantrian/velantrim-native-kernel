# ⚠️ Native Kernel Known Risks and Required Proof

```yaml
document_role: ACTIVE_RISKS
status_as_of: 2026-08-09
authoritative_machine_source: ../../project-state.json
repository_status: RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
active_architecture_decision: ADR-0025
```

This page lists current risks and explicitly closed historical findings. A closed code defect may still leave version-bound historical evidence or a broader unresolved threat model.

## Risk-state vocabulary

```text
OPEN                 unresolved technical, governance or evidence risk
MITIGATED            bounded control exists; residual risk remains
CLOSED               exact finding corrected and repository-verified
HISTORICAL_BOUNDARY  retained evidence remains valid only for its original version/scope
PROPOSED             research or decision work, not runtime protection
```

## P0 — Production overclaim

```text
ephemeral CI + synthetic data + 18 scenarios
≠ production deployment
≠ live user traffic
≠ sustained operations
```

**State:** `OPEN / PRIMARY COMMUNICATION AND GOVERNANCE RISK`.

C5 establishes a bounded synthetic operational rehearsal only. Production authorization remains `false`.

## P0 — Semantic assertion overclaim

```text
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
assertion map:              45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:                     0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
```

**State:** `OPEN`.

Operational success cannot promote unsupported or partial semantic assertions. In particular, `NK-EPI-004 — Unknown ≠ False` is not executable support yet.

## P0 — Reference implementation may capture the Canon

```text
available Python / PostgreSQL / SQLite mechanisms
≠ ontology
≠ abstract Kernel machine
≠ permanent architecture
```

**State:** `MITIGATED BY ADR-0025 / RESIDUAL RISK OPEN`.

The current P1–C5 lineage was implemented before the full knowledge ontology, abstract machine, semantic laws and substrate-independence contract were complete. Without an explicit boundary, current source structures and event-sourcing assumptions could become de facto Canon through inertia.

Controls:

- ADR-0025 establishes `Blueprint before Runtime`;
- P1–C5 is classified as a `BOUNDED REFERENCE LABORATORY`;
- new semantic/runtime expansion is frozen until integrated blueprint review and a separate operator decision;
- machine/current-state surfaces and fail-closed AI-context guards record the phase;
- isolated experiments are permitted only as falsification instruments without automatic promotion.

Residual risk:

- the blueprint A1–A10 is incomplete;
- existing accepted contracts may still contain assumptions inherited from current event-sourcing and serialization practice;
- future contributors or agents may attempt to hide semantic expansion inside maintenance, optimization or portability work;
- a detailed blueprint may itself be mistaken for implementation or portability evidence.

Detection rule:

```text
new semantic behaviour
without ontology / abstract-machine / law / contract / decision lineage
→ governance failure
```

## P0 — Historical and clean lineages may be collapsed

```text
clean P1–P5 + C4 + C5
≠ recovered v0.1.2.1
≠ original 44-test evidence
```

**State:** `OPEN / GOVERNANCE BOUNDARY`.

Issue #1 remains independent. `NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST`.

## P0 — Reducer referential semantics are incomplete

Reducer v1 permits histories whose LINK, UTILIZED, SUPERSEDED or ERASED references do not satisfy the proposed stricter rules in Issue #74 / ADR-0024.

**State:** `OPEN / CONTRACT DECISION REQUIRED / RUNTIME FROZEN`.

Reducer v1 must not be changed in place. Any stricter behavior requires a separately versioned reducer, fixtures, migration assessment and evidence after the blueprint gate is reviewed and runtime work is separately reopened.

## P0 — Event/history commitment is not complete authenticity

The current hash chain and exact Event verification are integrity signals. The portable semantic commitment boundary, history-head model, fork/truncation/rollback model, external witness model and authenticity claims remain incomplete.

**State:** `OPEN`.

```text
hash chain ≠ complete authenticity
signature over incomplete commitment ≠ complete integrity
```

## P0 — Physical deletion remains absent

No complete physical or cryptographic deletion is executed and verified across databases, backups, replicas, logs, exports, caches, evidence artifacts, external providers or keys.

**State:** `OPEN`.

Logical `ERASED`, restriction and a bounded Receipt must not be represented as global physical deletion.

## P0 — License and contribution rights are unresolved

The repository is public but has no operator-approved open-source or source-available regime.

**State:** `OPEN / ISSUE #18 / OPERATOR DECISION REQUIRED`.

```text
publicly readable source ≠ permission to copy, modify or redistribute
```

External collaboration, package publication, CLA/DCO policy, patent terms and contribution acceptance remain blocked pending a decision.

## P0 — Research may be mistaken for authorization

The Architecture Re-foundation plan and post-C5 backlog include ontology, an abstract Kernel machine, semantic laws, NK-EPI, Temporal, Admission, independent profiles, signed Receipts, deletion, ecosystem adapters and future substrates.

**State:** `OPEN / GOVERNANCE BOUNDARY`.

Research prose does not create Canon, accepted contracts, runtime behavior, evidence or production authority. ADR-0025 authorizes the research phase and runtime freeze; it does not pre-accept the contents of future blueprint deliverables.

## P1 — Operational equivalence remains absent

PostgreSQL and SQLite pass the same bounded semantic scenarios, but concurrency, durability, replication, failover, administration, filesystem and managed-provider behavior differ.

**State:** `OPEN`.

C3 is bounded semantic/behavioural comparison, not full operational equivalence.

## P1 — Independent implementation evidence remains absent

Current PostgreSQL and SQLite profiles share a Python semantic lineage. This is stronger than a single storage profile but weaker than a fully independent language/runtime implementation.

**State:** `OPEN`.

A future independent implementation must own its encoder, Event parser/verifier, reducer, state codec and fixture runner and pass declared equivalence profiles without using Python as a hidden oracle. ADR-0025 does not authorize starting that implementation before blueprint review.

## P1 — Durable evidence lacks independent custody

Sixteen exact ZIPs across the historical and ADR-0023 identities are repository-resident and hash-verified.

**State:** `MITIGATED / RESIDUAL RISK OPEN`.

Still absent:

- independent third-party custody;
- signed timestamping;
- append-only external archive;
- reviewer quorum;
- disaster recovery for the Git repository itself.

## P1 — Synthetic privacy checks are not privacy compliance

Canaries were absent from inspected synthetic artifacts.

**State:** `OPEN`.

This does not prove real personal-data handling, data-subject rights, retention, provider logs, breach response or jurisdictional compliance.

## P1 — Logical export is not disaster recovery

The bounded export/import path preserves exact synthetic Event bytes and quarantined replay for one instance.

**State:** `OPEN`.

It is not physical PostgreSQL backup, WAL recovery, provider snapshot, point-in-time recovery, cross-region restore or restore-under-load proof.

## P1 — Scale and environment scope are narrow

Current operational workloads are small, and preserved evidence covers Ubuntu 24.04, Python 3.11/3.12, PostgreSQL 16/18 and the declared SQLite versions.

**State:** `OPEN`.

Passing current thresholds is not a capacity, SLO, cost, architecture or broad portability claim.

## P1 — Current-state surfaces can drift

GitHub refs, issue states, Actions and Notion can change after a committed snapshot.

**State:** `MITIGATED BY PR #80, PR #86 AND PR #87 / RESIDUAL LIVE-STATE RISK OPEN`.

`nk-project-state/2` separates checkpoint roles and declares the expected relation to HEAD. It does not make committed metadata self-updating. Live state still requires GitHub verification, and Notion requires a separate post-merge sync and read-back record.

## Closed historical findings

### Exact Event type comparison gap

Python boolean/integer equality could previously allow a re-hashed envelope with `true` where canonical payload stored `1`.

**State:** `CLOSED BY PR #72 / EXACT PR AND MAIN CI PASS / HISTORICAL EVIDENCE VERSION-BOUND`.

The correction compares committed Event fields by canonical JSON bytes in both PostgreSQL and SQLite. Earlier artifacts remain evidence only of their producing versions.

### Evidence schema and associated-run identity drift

ADR-0023 evidence fields were not fully represented in the v1 schema, and associated P5/C3/C4 run identities were insufficiently constrained.

**State:** `CLOSED BY PR #72 / EXACT PR AND MAIN CI PASS`.

This establishes repository-declared identity binding, not external signatures or independent custody.

### SQLite builder workflow trigger gap

A change limited to `tools/sqlite/build_safe_sqlite.sh` did not trigger every dependent profile workflow.

**State:** `CLOSED BY PR #72 / EXACT PR AND MAIN CI PASS`.

### Historical SQLite WAL-reset exposure

Historical C5 evidence used SQLite `3.45.1`, which lies below the current safe WAL floor.

**State:** `MITIGATED IN CURRENT PROFILE / HISTORICAL EVIDENCE VERSION-BOUND`.

The current profile fails closed below linked SQLite `3.51.3`; safe-version evidence has its own immutable identity. Historical bytes are not rewritten.

## Update rule

For every risk transition record:

- exact contract or decision;
- exact SHA and workflow runs;
- affected evidence identity;
- residual risk;
- proof boundary;
- whether operator approval is required.

Never convert a bounded PASS, retained archive, closed bug, accepted research priority or blueprint proposal into production, truth, compliance, deletion, full neutrality, future-substrate support or ecosystem-authority claims.

## Historical snapshot

The pre-reconciliation risk chronology remains available at [publication checkpoint `626f34e…`](https://github.com/velantrian/velantrim-native-kernel/blob/626f34e6328b455258f2dd5fcf2145ec4db64a60/docs/ai/KNOWN_RISKS.md).

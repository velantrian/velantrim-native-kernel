# ⚠️ Native Kernel Known Risks and Required Proof

```yaml
document_role: ACTIVE_RISKS
status_as_of: 2026-08-11
authoritative_machine_source: ../../project-state.json
repository_status: RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
blueprint_decision: ADR-0025
post_blueprint_decision: ADR-0026
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

**State:** `MITIGATED BY ADR-0025 + ADR-0026 / RESIDUAL RISK OPEN`.

The current P1–C5 lineage was implemented before the complete A1–A10 blueprint. Current source structures and event-sourcing assumptions can therefore become de facto Canon through inertia unless challenged independently.

Controls:

- ADR-0025 established `Blueprint before Runtime`;
- P1–C5 is `BOUNDED_REFERENCE_LABORATORY`;
- A1–A10 and the integrated review remain provisional;
- ADR-0026 selected independent challenge before a bounded cross-lineage falsification instrument;
- runtime remains frozen;
- BPV-1 is blocked until qualifying independent review and finding reconciliation;
- fail-closed machine/current-state guards preserve these boundaries.

Residual risk:

- independent architectural validation is still `NOT ESTABLISHED`;
- accepted contracts may retain assumptions inherited from event sourcing and current serialization practice;
- a future BPV-1 could become a port of the current model instead of a cross-lineage falsification if its independence boundary is weak;
- future agents/contributors may hide semantic expansion inside maintenance, optimization or portability work;
- a detailed blueprint may be mistaken for implementation or portability evidence.

Detection rule:

```text
new semantic behaviour
without ontology / abstract-machine / law / contract / decision lineage
→ governance failure
```

## P0 — False independence / self-confirming review

**State:** `OPEN / ADR-0026 GATE`.

A different model name, fresh session, different prompt, or review label does not automatically create meaningful independence. The same authorship/reasoning lineage could unintentionally certify its own assumptions.

Required control:

```text
qualifying reviewer identity
+ explicit independence basis
+ no authorship of A1-A10/integrated review
+ adversarial falsification mandate
≠ simple second opinion
```

If a qualifying reviewer cannot be established, the correct state is `BLOCKED_NO_QUALIFYING_REVIEWER`, not silent progression to BPV-1.

## P0 — BPV-1 may become self-confirming

**State:** `OPEN / BLOCKED BEFORE EXPERIMENT DESIGN`.

If experiment success criteria are chosen after implementation, or if Python/reducer/Event-envelope/current SQL schema/ID layout becomes the hidden oracle, BPV-1 would not provide meaningful cross-lineage evidence.

Controls required before BPV-1:

- qualifying independent review complete;
- blocking/material findings reconciled or explicitly carried as experiment dependencies;
- hypotheses and falsification conditions written before implementation;
- no automatic product-profile admission;
- A10 outcome vocabulary used exactly;
- failed outcomes retained rather than redesigned away.

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

Reducer v1 must not be changed in place. ADR-0026 does not accept ADR-0024 and does not authorize reducer v2.

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

**State:** `OPEN / GOVERNANCE BOUNDARY`.

Research prose, independent-review findings and BPV-1 results do not automatically create Canon, runtime behavior, production authority, or broad substrate claims. ADR-0026 authorizes validation only.

## P1 — Operational equivalence remains absent

PostgreSQL and SQLite pass the same bounded semantic scenarios, but concurrency, durability, replication, failover, administration, filesystem and managed-provider behavior differ.

**State:** `OPEN`.

C3 is bounded semantic/behavioural comparison, not full operational equivalence.

## P1 — Independent implementation evidence remains absent

Current PostgreSQL and SQLite profiles share a Python semantic lineage.

**State:** `OPEN / TARGETED BY FUTURE BPV-1 BUT NOT YET TESTED`.

Still absent:

- independent-language evidence;
- non-event-sourced cross-lineage realization;
- bounded-memory realization;
- independent implementation team/custody;
- probabilistic/neuromorphic/analog/non-classical implementation evidence.

A different language alone is insufficient if it simply ports the same semantics and representations.

## P1 — Durable evidence lacks independent custody

Sixteen exact ZIPs across the historical and ADR-0023 identities are repository-resident and hash-verified.

**State:** `MITIGATED / RESIDUAL RISK OPEN`.

Still absent: independent third-party custody, signed timestamping, append-only external archive, reviewer quorum and disaster recovery for the Git repository itself.

## P1 — Synthetic privacy checks are not privacy compliance

Canaries were absent from inspected synthetic artifacts.

**State:** `OPEN`.

This does not prove real personal-data handling, data-subject rights, retention, provider logs, breach response or jurisdictional compliance.

## P1 — Logical export is not disaster recovery

The bounded export/import path preserves exact synthetic Event bytes and quarantined replay for one instance.

**State:** `OPEN`.

It is not physical PostgreSQL backup, WAL recovery, provider snapshot, point-in-time recovery, cross-region restore or restore-under-load proof.

## P1 — Scale and environment scope are narrow

Current operational workloads are small, and preserved evidence covers Ubuntu 24.04, Python 3.11/3.12, PostgreSQL 16/18 and declared SQLite versions.

**State:** `OPEN`.

Passing current thresholds is not a capacity, SLO, cost, architecture or broad portability claim.

## P1 — Current-state surfaces can drift

GitHub refs, issue states, Actions and Notion can change after a committed snapshot.

**State:** `MITIGATED / RESIDUAL LIVE-STATE RISK OPEN`.

`nk-project-state/2` separates checkpoint roles and declares the expected relation to HEAD. It does not make committed metadata self-updating. Live state still requires GitHub verification, and Notion requires separate post-merge synchronization/read-back.

## Closed historical findings

### Exact Event type comparison gap

**State:** `CLOSED BY PR #72 / EXACT PR AND MAIN CI PASS / HISTORICAL EVIDENCE VERSION-BOUND`.

The correction compares committed Event fields by canonical JSON bytes in both PostgreSQL and SQLite. Earlier artifacts remain evidence only of their producing versions.

### Evidence schema and associated-run identity drift

**State:** `CLOSED BY PR #72 / EXACT PR AND MAIN CI PASS`.

This establishes repository-declared identity binding, not external signatures or independent custody.

### SQLite builder workflow trigger gap

**State:** `CLOSED BY PR #72 / EXACT PR AND MAIN CI PASS`.

### Historical SQLite WAL-reset exposure

**State:** `MITIGATED IN CURRENT PROFILE / HISTORICAL EVIDENCE VERSION-BOUND`.

The current profile fails closed below linked SQLite `3.51.3`; safe-version evidence has its own immutable identity. Historical bytes are not rewritten.

## Update rule

For every risk transition record exact contract/decision, exact SHA/workflow runs, affected evidence identity, residual risk, proof boundary, and whether operator approval is required.

Never convert a bounded PASS, retained archive, closed bug, accepted research priority, operator approval, independent-review protocol or future BPV-1 result into production, truth, compliance, deletion, Final Canon, universal neutrality, future-substrate support or ecosystem-authority claims.

## Historical snapshot

The pre-reconciliation risk chronology remains available at [publication checkpoint `626f34e…`](https://github.com/velantrian/velantrim-native-kernel/blob/626f34e6328b455258f2dd5fcf2145ec4db64a60/docs/ai/KNOWN_RISKS.md).
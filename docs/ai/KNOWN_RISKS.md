# ⚠️ Native Kernel Known Risks and Required Proof

```yaml
document_role: ACTIVE_RISKS
status_as_of: 2026-08-11
authoritative_machine_source: ../../project-state.json
repository_status: RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
blueprint_decision: ADR-0025
post_blueprint_decision: ADR-0026
independent_review: IAR-1 / QUALIFYING_REVIEW_COMPLETE
review_reconciliation: IAR-1-R1 / COMPLETE
next_gate: BPV1_PLAN_AND_PREREGISTRATION
```

This page lists current risks and explicitly closed historical findings. A closed code defect or reconciled architecture finding may still leave version-bound historical evidence or a broader unresolved threat model.

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
≠ minimum Kernel obligations
≠ permanent architecture
```

**State:** `MITIGATED BY ADR-0025 + ADR-0026 + IAR-1-R1 / RESIDUAL RISK OPEN`.

The current P1–C5 lineage was implemented before the complete A1–A10 blueprint. IAR-1 confirmed that capture risk existed not only in literal Python/SQL/Event choices, but also in higher-level A3 transition/outcome, A6 lifecycle and Receipt/reconstruction structures.

Controls now established:

- ADR-0025 established `Blueprint before Runtime`;
- P1–C5 remains `BOUNDED_REFERENCE_LABORATORY`;
- A1–A10 remain provisional;
- ADR-0026 selected independent challenge before cross-lineage falsification;
- IAR-1 completed as a qualifying adversarial review with 10 findings;
- IAR-1-R1 demotes the complete A3/A6/current-laboratory shape from universal minimum to reference taxonomy;
- a later BPV-1 must independently derive its state/change/history model from problem-level obligations;
- runtime remains frozen;
- fail-closed machine/current-state guards preserve these boundaries.

Residual risk:

- the reconciled minimum is still provisional and untested by BPV-1;
- accepted contracts may retain assumptions inherited from event sourcing and serialization within their scoped laboratory role;
- a future BPV-1 could still become a semantic port if its design copies A3/A6/Event/reducer/Receipt structures despite different syntax/language;
- future contributors may hide semantic expansion inside maintenance, optimization or portability work;
- a detailed blueprint/reconciliation may still be mistaken for portability evidence.

Detection rule:

```text
future BPV-1 realization reproduces current implementation/taxonomy by inertia
without independent derivation from preregistered problem-level obligations
→ implementation-capture failure
```

## P0 — False independence / self-confirming review

**State:** `MITIGATED BY IAR-1 / RESIDUAL GOVERNANCE RISK OPEN`.

IAR-1 recorded a concrete reviewer identity and independence basis, reviewed immutable `main@2dd51723e30d5f3c5e86268365bf4cf7639b5e9a`, answered Q1–Q12 and produced a ten-finding adversarial register. This satisfies the review-process gate under `nk-independent-architecture-review/1`; it does not prove the architecture correct.

Residual risk remains for later validation stages: a new model/session/label or the same implementation authorship lineage must not be treated as independent merely by name. Future independent gates still require their own concrete separation and evidence trail.

## P0 — BPV-1 preregistration may become self-confirming

**State:** `OPEN / NEXT ACTIVE GATE / EXECUTION BLOCKED`.

The largest immediate architecture risk is no longer absence of review; it is an experiment whose oracle can change after results are observed.

Required before BPV-1 execution:

- authoritative `scenario_id` and purpose scope;
- mandatory obligations and preregistered applicability rules;
- mandatory observables;
- equivalence predicates;
- allowed declared losses;
- failure thresholds;
- hard refutation observations;
- finite grounding mode;
- architecture-level threat model;
- oracle Authority separate from the implementation under test.

`IAR-1-R1` requires that post-execution changes to mandatory obligations, applicability, equivalence predicates or failure thresholds **invalidate the run for the claimed scope**. A redesigned experiment must receive a new identity; the prior result cannot be rewritten away.

## P0 — Bounded accountability boundary is untested

**State:** `OPEN / RECONCILED CONCEPT / NOT YET FALSIFIED`.

IAR-1-R1 separates current accountability from exact reconstruction/replay. Candidate required classes are current accountability, declared retention scope and explicit loss witness. Exact reconstruction, permanent predecessor visibility and unbounded reopening are optional capabilities unless a scenario preregisters them.

Risk: BPV-1 may show that the proposed loss-witness boundary is too weak to prevent silent overwrite or too strong for genuinely bounded realizations. Such a result must weaken/refute the architecture claim rather than force an Event-log equivalent by definition.

## P0 — Threat/authenticity boundary is provisional

**State:** `OPEN / RECONCILED CONCEPT / NEGATIVE TESTS REQUIRED`.

IAR-F08 found that honest-path semantic evidence was insufficient without explicit adversarial behavior. IAR-1-R1 now requires declared protected meanings, trust assumptions and relevant cases such as forgery, fork, truncation, rollback, equivocation, withheld counterevidence, unavailable/colluding witnesses and compromised certifier.

Risk: no single current mechanism proves authenticity across arbitrary profiles. Architecture must preserve explicit trust/failure/uncertainty semantics without turning one cryptographic mechanism into Canon.

## P0 — Context/Provenance/Authority grounding can hide assumptions

**State:** `OPEN / FINITE GROUNDING MODEL RECONCILED / NOT YET TESTED`.

IAR-F09 identified infinite regress or undeclared trusted-root risk. IAR-1-R1 requires one declared grounding mode: externally attested root, explicit assumed root, bounded recursive closure, declared cycle, or terminal Unknown/gap.

Risk: two profiles can reach identical outputs using materially different hidden roots. BPV-1 conformance must therefore compare grounding assumptions where they matter rather than treating metadata presence as sufficient.

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

Reducer v1 must not be changed in place. ADR-0026 and IAR-1-R1 do not accept ADR-0024 and do not authorize reducer v2.

## P0 — Event/history commitment is not complete authenticity

The current hash chain and exact Event verification are integrity signals. The portable semantic commitment boundary, history-head model, fork/truncation/rollback model, external witness model and authenticity claims remain incomplete.

**State:** `OPEN`.

```text
hash chain ≠ complete authenticity
signature over incomplete commitment ≠ complete integrity
```

IAR-1-R1 explicitly prevents this risk from being “solved” by declaring the current Event/hash-chain mechanism universal architecture.

## P0 — Physical deletion remains absent

No complete physical or cryptographic deletion is executed and verified across databases, backups, replicas, logs, exports, caches, evidence artifacts, external providers or keys.

**State:** `OPEN`.

Logical `ERASED`, restriction and a bounded Receipt must not be represented as global physical deletion. IAR-1-R1 further requires threat-scoped evidence outside unverified self-attestation before a physical/cryptographic erasure condition may be claimed; otherwise the appropriate result is `INDETERMINATE`.

## P0 — License and contribution rights are unresolved

The repository is public but has no operator-approved open-source or source-available regime.

**State:** `OPEN / ISSUE #18 / OPERATOR DECISION REQUIRED`.

```text
publicly readable source ≠ permission to copy, modify or redistribute
```

External collaboration, package publication, CLA/DCO policy, patent terms and contribution acceptance remain blocked pending a decision.

## P0 — Research may be mistaken for authorization

**State:** `OPEN / GOVERNANCE BOUNDARY`.

Research prose, qualifying review completion, reconciliation and future BPV-1 results do not automatically create Canon, runtime behavior, production authority, or broad substrate claims. ADR-0026 authorizes validation only.

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

A different language alone is insufficient if it simply ports the same semantics, A3/A6 taxonomies, Event/reducer/Receipt shape or current expected outputs.

## P1 — Composition/federation semantics remain outside base conformance

**State:** `OPEN / SEPARATE CAPABILITY CLASS`.

IAR-F10 showed that local scoped conformance did not define how independently evolving Kernels compose. IAR-1-R1 narrows base substrate-independence to scoped non-composed realizations. Therefore:

```text
local conformance ≠ federation/composition conformance
```

A future composition experiment must separately define Context overlap, identity disagreement, provenance union/loss, Authority conflict, concurrency and partial failure. BPV-1 must not silently introduce a centralized coordinator and then generalize from it.

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

Never convert a bounded PASS, retained archive, closed bug, accepted research priority, operator approval, qualifying independent review, review reconciliation or future BPV-1 result into production, truth, compliance, deletion, Final Canon, universal neutrality, future-substrate support or ecosystem-authority claims.

## Historical snapshot

The pre-reconciliation risk chronology remains available at [publication checkpoint `626f34e…`](https://github.com/velantrian/velantrim-native-kernel/blob/626f34e6328b455258f2dd5fcf2145ec4db64a60/docs/ai/KNOWN_RISKS.md).
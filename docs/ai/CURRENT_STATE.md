# 📍 Native Kernel Current State Checkpoint

**Verified:** 2026-08-06  
**Last verified public `main`:** `c7610bc42fbc879c24e1a3a1408ebfaae1ac7340`  
**Latest merged governance checkpoint:** PR #29 — ADR-0010 merge record finalized  
**Active proposal branch:** `agent/contracts-14-17` — exact contracts and executable fixture integrity for Issues #14–#17  
**Repository status:** `RESEARCH / DOCUMENTED_ONLY / NOT PRODUCTION-READY`  
**Primary executable Kernel gate:** Issue #1 / Stage 0.5 authentic source recovery

> This file is a last-verified checkpoint, not an automatically updated database. Compare its SHA with the actual branch or PR under review before relying on it.

```text
DOCUMENTED ≠ IMPLEMENTED
PROPOSED ≠ ACCEPTED
ACCEPTED ≠ IMPLEMENTED
IMPLEMENTED ≠ TESTED
FIXTURE TOOLING PASS ≠ KERNEL RUNTIME PASS
LOCALLY_TESTED ≠ REPOSITORY_REPRODUCED
C2 ≠ C3
Operator approval ≠ empirical evidence
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
Cross-project link ≠ runtime integration
```

## Current public reality

Public `main` contains:

- Architecture Canon, invariants and foundational intent;
- the accepted six-family foundational skeleton under ADR-0010;
- governance, ADR/RFC, source-recovery and AI-continuity documentation;
- isolated source-recovery and AI-context support tooling with their declared tests/CI;
- accepted documentation-only PostgreSQL/SQLite profile direction;
- no public Native Kernel runtime;
- no authentic `v0.1.2.1` source snapshot or original 44-test suite.

## Accepted foundational contract skeleton

**Decision:** ADR-0010 `ACCEPTED`  
**Evidence:** `DOCUMENTED`  
**Implementation:** `NOT_STARTED`  
**Operator approval:** `APPROVED`  
**Contract version:** `foundational-skeleton/1.0`  
**Merge evidence:** PR #28 → `2d42a1517ba87b39d2395aa5c22b966328615305`

```text
NK-SEM — semantic roles
NK-ID  — identity and canonical encoding
NK-EVT — event, observation and recorded change
NK-AUT — authority and admission
NK-CFL — conflict and explicit unknowns
NK-EQV — conformance and semantic equivalence
```

## Active Issues #14–#17 proposal track

The branch `agent/contracts-14-17` adds a bounded proposal package:

- ADR-0011 — canonical identity contract v1;
- ADR-0012 — single-writer append and deterministic replay v1;
- ADR-0013 — deletion, restriction and retention v1;
- ADR-0014 — executable conformance fixture protocol v1;
- bilingual normative contract documents;
- machine-readable assertion registry, neutral schema bundle and fixture pack;
- a Python standard-library fixture-integrity runner;
- five focused unit tests;
- a Python 3.11/3.12 GitHub Actions workflow proposal.

### Current proposal status

```text
ADR-0011…0014:               PROPOSED
Operator approval:           PENDING
Reference fixture tooling:   IMPLEMENTED IN BRANCH
Local tests:                 5 PASS
Local fixture validation:    PASS
Kernel runtime:              NOT IMPLEMENTED
Kernel runtime conformance:  UNSUPPORTED
C2 repository reproduction:  NOT YET ESTABLISHED
C3 cross-profile evidence:   NOT ESTABLISHED
Issue #1 impact:             NONE
```

Local validation recorded during authoring:

- 72 unique assertion IDs;
- two identity golden vectors matched;
- four invalid identity vectors rejected;
- two event-chain scenarios validated;
- two deletion state-machine scenarios validated;
- positive and negative fixtures exist for each `NK-EPI-001…008`.

This narrows architecture ambiguity and makes review executable. It does not implement event storage, reducers, deletion machinery, PostgreSQL/SQLite adapters or a live Kernel.

## Issue #1 / Stage 0.5

```text
accessible connected-source sweep
→ no authentic candidate bytes found
→ NOT_FOUND_IN_ACCESSIBLE_SOURCES
→ operator-controlled local recovery still required
```

The Issues #14–#17 proposal is a new architecture/fixture lineage. It must not be represented as recovered `v0.1.2.1` code, tests or design evidence.

## Current accepted decisions with no implied runtime

- Architecture Canon is separate from Implementation Profiles.
- Causality belongs on typed directed relations rather than `knowledge_type` or lineage.
- Operator approval is not an evidence level.
- PostgreSQL is the preferred contemporary full profile; SQLite remains optional.
- Foundational responsibilities are separated into the six ADR-0010 families.

ADR-0011–0014 remain proposals until an explicit operator decision. Local fixture evidence does not accept them automatically.

## Recent checkpoints

| Change | Evidence | Scope |
|---|---|---|
| AI context integrity guard | PR #26 → `099ae235ff935948348f2101804eb53ac9eeae1a` | support tooling and CI |
| AI guard checkpoint | PR #27 → `2a03c871e5f7250c917c060cc112a9ea1497e9c4` | continuity record |
| Foundational contract skeleton | PR #28 → `2d42a1517ba87b39d2395aa5c22b966328615305` | accepted architecture; no runtime |
| Foundational merge record | PR #29 → `c7610bc42fbc879c24e1a3a1408ebfaae1ac7340` | continuity record |
| Exact contracts and fixture protocol | branch `agent/contracts-14-17` | proposal under review; not merged reality |

## Runtime and evidence boundary

May claim on the proposal branch:

- proposed exact contracts for identity, append/replay, deletion and fixture protocol;
- committed machine-readable registry, schemas and fixtures;
- implemented fixture-integrity support tooling and focused tests;
- local authoring evidence listed above;
- explicit `UNSUPPORTED` Kernel runtime conformance.

Must not claim:

- accepted ADR-0011–0014 before operator approval;
- repository-reproduced CI before an exact workflow result exists;
- runnable public Kernel;
- implemented durable append, replay, projection rebuild or deletion;
- C2 or C3 Kernel conformance;
- production privacy, security, erasure or portability;
- authentic recovery of `v0.1.2.1`;
- active Titan, Mentaury or Crystal integration.

## Immediate next gates

1. Review ADR-0011–0014 and the normative contract language.
2. Verify exact branch tests and fixture-integrity CI.
3. Record operator decisions separately for each proposal or for the bounded package.
4. Merge only with GitHub and Notion reality synchronized.
5. Keep cross-language/profile C3 evidence open until two materially independent profiles exist.
6. Keep the executable Kernel gate separate under Issue #1 or a future explicitly new implementation lineage.

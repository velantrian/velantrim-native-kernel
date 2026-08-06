# 📍 Native Kernel Current State Checkpoint

**Verified:** 2026-08-06  
**Last verified public `main`:** `2a03c871e5f7250c917c060cc112a9ea1497e9c4`  
**Latest governance checkpoint:** PR #28 — foundational contract skeleton accepted; merge pending  
**Repository status:** `RESEARCH / DOCUMENTED_ONLY / NOT PRODUCTION-READY`  
**Primary executable gate:** Issue #1 / Stage 0.5 authentic source recovery

> This file is a last-verified checkpoint, not an automatically updated database. Compare its SHA with the actual branch or PR under review before relying on it.

```text
DOCUMENTED ≠ IMPLEMENTED
PROPOSED ≠ ACCEPTED
ACCEPTED ≠ IMPLEMENTED
IMPLEMENTED ≠ TESTED
TESTED ≠ WIRED
WIRED ≠ ENABLED
ENABLED ≠ OBSERVED

Operator approval ≠ empirical evidence
Source-recovery utility PASS ≠ Kernel runtime PASS
AI-context guard PASS ≠ semantic freshness
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
Cross-project link ≠ runtime integration
Context checkpoint ≠ automatically current main
```

## Current public reality

The repository contains:

- Architecture Canon, invariants and foundational intent;
- abstract contract and conformance documentation;
- an accepted six-family foundational contract skeleton under ADR-0010;
- status, roadmap, decision process, ADR and RFC governance;
- source-recovery specifications, manifest/verification tooling and isolated utility tests;
- accepted documentation-only PostgreSQL/SQLite profile direction;
- ecosystem and integration-boundary documentation for Titan, Mentaury and Crystal;
- mandatory root `AGENTS.md` guidance for AI agents, auditors and reviewers;
- a `docs/ai/` context pack with current checkpoint, component map, risk register, audit playbook, work log and GitHub↔Notion protocol;
- a PR template requiring exact evidence and documentation-impact classification;
- a standard-library AI-context validator with isolated tests;
- read-only AI-context CI on Python 3.11 and 3.12 for selected governance paths;
- no public Native Kernel runtime;
- no original `v0.1.2.1` source snapshot or 44-test suite in `main`.

## Accepted foundational contract skeleton

**Decision:** ADR-0010 `ACCEPTED`  
**Evidence:** `DOCUMENTED`  
**Implementation:** `NOT_STARTED`  
**Operator approval:** `APPROVED`  
**Contract version:** `foundational-skeleton/1.0`

The accepted architecture separates:

```text
NK-SEM — semantic roles
NK-ID  — identity and canonical encoding
NK-EVT — event, observation and recorded change
NK-AUT — authority and admission
NK-CFL — conflict and explicit unknowns
NK-EQV — conformance and semantic equivalence
```

This establishes ownership and stable assertion namespaces. It does not establish executable schemas, runtime behaviour, C1–C5 conformance, production readiness or demonstrated portability.

Detailed contract work remains open:

- Issue #14 — canonical Claim encoding and identity vectors;
- Issue #15 — append, idempotency, ordering, crash recovery and replay;
- Issue #16 — deletion, restriction, retention and crypto-erasure;
- Issue #17 — executable fixtures and cross-profile runner.

## Issue #1 / Stage 0.5

Current result:

```text
accessible connected-source sweep
→ no authentic candidate bytes found
→ NOT_FOUND_IN_ACCESSIBLE_SOURCES
→ operator-controlled local recovery still required
```

Allowed work includes evidence recovery, read-only candidate preservation, provenance manifests and support tooling.
Prohibited work includes reconstructing an approximation and calling it `v0.1.2.1`, replacing the original suite, or mixing controlled import with redesign.

## Current accepted decisions with no implied runtime

- Architecture Canon is separate from Implementation Profiles.
- Causality belongs on typed directed relations rather than `knowledge_type` or lineage.
- Operator approval is not an evidence level.
- PostgreSQL is the preferred contemporary full storage profile; SQLite remains optional for embedded, portable, test, recovery and constrained use.
- Foundational responsibilities are separated into `NK-SEM`, `NK-ID`, `NK-EVT`, `NK-AUT`, `NK-CFL` and `NK-EQV`.

Each decision retains its own evidence and implementation status. ADR-0009 and ADR-0010 remain `IMPLEMENTATION_STATUS: NOT_STARTED`.

## Recent documentation and governance checkpoints

| Change | Merge evidence | Scope |
|---|---|---|
| Storage profile decision and guidance | PR #21; baseline preceding PR #22: `91dc4c6d177cad80d6827e1a9b158b733ea016bc` | documentation-only profile direction |
| Visual storage-profile maps | PR #22 → `fa8b2d9356486d6d78074e8bd6eb3b14ebfd2249` | bilingual visual documentation |
| Ecosystem role clarification | PR #23 → `18ee09c870f7416932de29a2b2f5de53202fcb2e` | bilingual README role/navigation map |
| AI context and documentation continuity | PR #24 → `d5989742f987b610b5a81bb59a14c0a11518aeea` | mandatory AI entry point, context pack, audit/risk/work records, PR and Notion sync protocol |
| Context synchronization checkpoint | PR #25 → `5db894781ac34dd44c1c66b68a00f4c7fe579d32` | finalized current-state/work-log evidence |
| AI context integrity guard | PR #26 → `099ae235ff935948348f2101804eb53ac9eeae1a` | support tooling, six tests, exact-head and main-push CI |
| AI guard documentation checkpoint | PR #27 → `2a03c871e5f7250c917c060cc112a9ea1497e9c4` | current-state/risk/work-log synchronization |
| Foundational contract skeleton | PR #28 → merge pending | accepted architecture; no runtime |

## AI continuity status

```text
Mandatory AI first-read route: IMPLEMENTED
GitHub completeness rule:      DOCUMENTED AND REQUIRED
PR documentation gate:         IMPLEMENTED
Structural context validator:  IMPLEMENTED AND TESTED
Selected-path CI:               ENABLED ON PR AND MAIN PUSH
Notion acceptance record:      SYNCED FOR PR #28
Semantic auto-freshness:       NOT IMPLEMENTED
```

The validator checks mandatory files, selected repository-relative Markdown links, repository-escape attempts, checkpoint syntax, commit existence, checkpoint ancestry and required status-boundary markers.

It deliberately permits an ancestor checkpoint. It cannot decide whether every later change materially altered project meaning, and it does not prove that Notion is synchronized.

## Runtime and evidence boundary

May claim:

- documented architecture and decisions;
- accepted six-family foundational contract organization;
- isolated source-recovery tooling and its declared utility CI;
- explicit source-recovery and provenance gate;
- documented profile and ecosystem boundaries;
- implemented documentation/governance continuity mechanism for AI and human reviewers;
- repository-reproduced structural validation of the selected AI context surface on Python 3.11 and 3.12 where exact run evidence exists.

Must not claim:

- runnable public Kernel;
- repository reproduction of the external 44 tests;
- authentic recovery of `v0.1.2.1`;
- production event integrity, replay, privacy, security or migration;
- implemented PostgreSQL or SQLite Kernel profiles;
- executable implementation of ADR-0010 families;
- implemented Curiosity Core or causal runtime;
- active Titan, Mentaury or Crystal integration;
- proven technology neutrality or future-hardware portability;
- that AI-context validation proves semantic freshness, Notion synchronization, Architecture Canon correctness or runtime correctness.

## Immediate next gates

The next executable Kernel gate remains operator-controlled local source recovery.
The architecture track may continue independently through Issues #14–#17, provided every artifact remains clearly separated from the controlled historical import.

If authentic recovery succeeds, perform exact controlled import under the existing specifications.
If the declared search is completed without recovery, only an explicit operator decision may mark the checkpoint `LOST / NON-REPRODUCIBLE` and authorize a clean implementation under a new version and evidence lineage.

# 📍 Native Kernel Current State Checkpoint

**Verified:** 2026-08-06  
**Last verified public `main`:** `d5989742f987b610b5a81bb59a14c0a11518aeea`  
**Latest governance checkpoint:** PR #24 — AI context and documentation-continuity system  
**Repository status:** `RESEARCH / DOCUMENTED_ONLY / NOT PRODUCTION-READY`  
**Primary active gate:** Issue #1 / Stage 0.5 authentic source recovery

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
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
Cross-project link ≠ runtime integration
Context checkpoint ≠ automatically current main
```

## Current public reality

The repository contains:

- Architecture Canon, invariants and foundational intent;
- abstract contract and conformance documentation;
- status, roadmap, decision process, ADR and RFC governance;
- source-recovery specifications, manifest/verification tooling and isolated utility tests;
- accepted documentation-only PostgreSQL/SQLite profile direction;
- ecosystem and integration-boundary documentation for Titan, Mentaury and Crystal;
- mandatory root `AGENTS.md` guidance for AI agents, auditors and reviewers;
- a `docs/ai/` context pack with current checkpoint, component map, risk register, audit playbook, work log and GitHub↔Notion protocol;
- a PR template requiring exact evidence and documentation-impact classification;
- no public Native Kernel runtime;
- no original `v0.1.2.1` source snapshot or 44-test suite in `main`.

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
- World/epistemic boundaries are representation disciplines.
- PostgreSQL is the preferred contemporary full storage profile; SQLite remains optional for embedded, portable, test, recovery and constrained use.

Each decision retains its own evidence and implementation status. ADR-0009 remains `IMPLEMENTATION_STATUS: NOT_STARTED`.

## Recent documentation and governance checkpoints

| Change | Merge evidence | Scope |
|---|---|---|
| Storage profile decision and guidance | PR #21; baseline preceding PR #22: `91dc4c6d177cad80d6827e1a9b158b733ea016bc` | documentation-only profile direction |
| Visual storage-profile maps | PR #22 → `fa8b2d9356486d6d78074e8bd6eb3b14ebfd2249` | bilingual visual documentation |
| Ecosystem role clarification | PR #23 → `18ee09c870f7416932de29a2b2f5de53202fcb2e` | bilingual README role/navigation map |
| AI context and documentation continuity | PR #24 → `d5989742f987b610b5a81bb59a14c0a11518aeea` | mandatory AI entry point, context pack, audit/risk/work records, PR and Notion sync protocol |

## AI continuity status

```text
Mandatory AI first-read route: IMPLEMENTED
GitHub completeness rule:      DOCUMENTED AND REQUIRED
PR documentation gate:         IMPLEMENTED
Notion synchronization record: SYNCED FOR PR #24
Automated freshness checker:   NOT IMPLEMENTED
```

The context pack reduces blind scans and lost decisions, but it does not replace exact-SHA verification. A stale checkpoint must be corrected rather than silently treated as present reality.

## Runtime and evidence boundary

May claim:

- documented architecture and decisions;
- isolated source-recovery tooling and its declared utility CI;
- explicit source-recovery and provenance gate;
- documented profile and ecosystem boundaries;
- implemented documentation/governance continuity mechanism for AI and human reviewers.

Must not claim:

- runnable public Kernel;
- repository reproduction of the external 44 tests;
- authentic recovery of `v0.1.2.1`;
- production event integrity, replay, privacy, security or migration;
- implemented PostgreSQL or SQLite Kernel profiles;
- implemented Curiosity Core or causal runtime;
- active Titan, Mentaury or Crystal integration;
- proven technology neutrality or future-hardware portability;
- that AI context documentation itself proves runtime correctness.

## Immediate next gate

The next executable gate remains operator-controlled local source recovery.
If authentic recovery succeeds, perform exact controlled import under the existing specifications.
If the declared search is completed without recovery, only an explicit operator decision may mark the checkpoint `LOST / NON-REPRODUCIBLE` and authorize a clean implementation under a new version and evidence lineage.

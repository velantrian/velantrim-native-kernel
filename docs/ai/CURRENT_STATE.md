# 📍 Native Kernel Current State Checkpoint

**Verified:** 2026-08-06  
**Last verified public `main`:** `9ccbb535e22438092393e2686eb76eb362adb29d`  
**Active branch:** `agent/p1-semantic-core` — re-check exact PR head  
**Active issue:** #43 — P1 profile-independent semantic core  
**Repository status:** `RESEARCH / P1 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY`

> Context checkpoint ≠ automatically current main. Re-check the branch, PR, final merge SHA and exact workflow evidence.

Source-recovery result remains:

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
```

```text
ACCEPTED PROFILE PLAN ≠ COMPLETE PROFILE
P1 LOCAL PASS ≠ DURABLE KERNEL
LOGICAL REDUCER ≠ AUTHORITATIVE HISTORY
IMPLEMENTED CODE PATH ≠ ASSERTION-LEVEL CONFORMANCE
C1 ≠ C2 ≠ C3
```

## Operator decision

The operator accepted RFC-0002 and clean lineage, then separately authorized P1 only:

```text
RFC-0002:                 ACCEPTED / APPROVED
clean lineage:            clean/postgresql-reference/0.1
P1 semantic core:         GO
P2–P5:                    REQUIRE SEPARATE GO
Issue #1:                 ACTIVE / INDEPENDENT
```

Decision evidence is recorded in Issue #40 and ADR-0015.

## Active P1 implementation

Package:

```text
native_kernel.semantic_core
Python >=3.11,<3.13
standard library only
```

Implemented components:

1. `canonical.py` — canonical JSON, `nkh1`, `nkc1`, `nkl1`, provisional `nkd0`/`nks0`;
2. `models.py` — immutable semantic content, Claim identity, command and logical Event objects;
3. `authority.py` — explicit deterministic deny-by-default authority policy;
4. `reducer.py` — version-bound deterministic in-memory reducer;
5. `deletion.py` — accepted deletion/restriction transition graph and Receipt limits;
6. `receipt.py` — admission Receipt proof-boundary enforcement;
7. `errors.py` — explicit contract, authority, sequence, version, transition and overclaim failures.

## Local evidence

Recorded before publication:

```text
20 semantic-core unit tests PASS
4 P1-manifest guard tests PASS
7 AI-context validator tests PASS
Python compileall PASS
no PostgreSQL/SQLite/network dependency imports
```

Tests cover identity vectors, invalid canonical inputs, command determinism, explicit authority, reducer sequence/version failures, deletion fixture paths, Receipt overclaims and rejection of the superseded `DOCUMENTED_ONLY` context marker.

## Implementation limits

P1 does not contain:

- PostgreSQL or SQLite adapter;
- SQL schema, driver or migration framework;
- durable append/idempotency;
- writer lease persistence;
- authoritative replay or crash recovery;
- projection storage/rebuild;
- network API;
- conformance adapter;
- Titan, Mentaury or Crystal wiring.

The P1 reducer processes logical in-memory Events only.

## Profile and evidence manifests

```text
profile-manifest.json → historical P0 planning snapshot
p1-manifest.json      → accepted P1 implementation/evidence state
```

The P1 validator rejects false C1/C2/C3 promotion, external dependency policy, historical `v0.1.2.1` lineage, recovery claims and removal of explicit PostgreSQL/conformance prohibitions.

All 72 contract assertions remain runtime `UNSUPPORTED` until a P4 conformance adapter reports every assertion exactly once.

## Workflow state

`.github/workflows/p1-semantic-core.yml` declares PR, push-to-main and manual entry points on Python 3.11/3.12, runs the P1 tests, compiles the package and emits a machine-readable P1 manifest artifact.

`.github/workflows/ai-context.yml` validates the updated P1 maturity markers and checkpoint ancestry.

No exact GitHub Actions run is yet recorded for the active branch.

```text
workflow definitions: ACTIVE ON BRANCH
local evidence:       LOCALLY_TESTED
repository runs:      NOT_RECORDED
```

## Issue #1 separation

```text
P1 clean implementation
≠ recovered v0.1.2.1
≠ original 44 tests
≠ closure of source-recovery gate
```

## Next gates

1. verify complete branch diff and exact test evidence;
2. open/review/merge P1 PR with status boundaries intact;
3. record exact merge SHA and any Actions evidence;
4. synchronize Notion and Issue #43;
5. keep P2 blocked until a separate operator GO;
6. leave assertion-level conformance `UNSUPPORTED` until P4.

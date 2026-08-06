# 📍 Native Kernel Current State Checkpoint

**Verified:** 2026-08-06  
**Last verified public `main`:** `9fd608f3f1d2915b961644015eb6b5e1a93e84d3`  
**Latest implementation:** PR #44 — P1 profile-independent semantic core  
**Repository status:** `RESEARCH / P1 PARTIAL IMPLEMENTATION / NOT PRODUCTION-READY`

> Context checkpoint ≠ automatically current main. Re-check the repository ref, exact workflow evidence and later PRs before relying on this file.

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

```text
RFC-0002:                 ACCEPTED / APPROVED
clean lineage:            clean/postgresql-reference/0.1
P1 semantic core:         AUTHORIZED / MERGED
P2–P5:                    REQUIRE SEPARATE GO
Issue #1:                 ACTIVE / INDEPENDENT
```

Decision evidence is recorded in Issue #40 and ADR-0015.

## Exact P1 publication

```text
PR:             #44
Base main:      9ccbb535e22438092393e2686eb76eb362adb29d
Final PR head:  273d9369e624d8e4c4033dc7842ebbcc46642668
Merge SHA:      9fd608f3f1d2915b961644015eb6b5e1a93e84d3
Changed files:  30
Review threads: 0 unresolved
Submitted reviews: 0
Codex review:   unavailable due external usage limit
```

## Merged P1 package

```text
native_kernel.semantic_core
Python profile: >=3.11,<3.13
Dependencies: standard library only
```

Implemented components:

1. `canonical.py` — canonical JSON, `nkh1`, `nkc1`, `nkl1`, provisional `nkd0`/`nks0`;
2. `models.py` — immutable semantic content, Claim identity, command and logical Event objects;
3. `authority.py` — explicit deterministic deny-by-default authority policy;
4. `reducer.py` — version-bound deterministic in-memory reducer;
5. `deletion.py` — deletion/restriction transition graph and Receipt limits;
6. `receipt.py` — admission Receipt proof-boundary enforcement;
7. `errors.py` — explicit contract, authority, sequence, version, transition and overclaim failures.

Manual hardening corrected exact authority scope and rejects malformed enums, calendar timestamps, boolean sequences, authority grants, Receipt identifiers/limits and deletion evidence.

## Evidence

Exact final content was run in the available local Python 3.13.5 environment:

```text
20 semantic-core tests PASS
4 P1-manifest guard tests PASS
7 AI-context validator tests PASS
Python compileall PASS
P1 manifest validator PASS
no PostgreSQL/SQLite/network dependency imports
```

The declared runtime range is Python 3.11/3.12. No workflow run was created for PR head `273d9369…` or merge `9fd608f3…`.

```text
local final-content evidence: LOCALLY_TESTED
repository workflow evidence: NOT_RECORDED
Kernel runtime conformance:   UNSUPPORTED
C1/C2/C3:                     NOT_ESTABLISHED
```

## Implementation limits

P1 contains no PostgreSQL/SQLite adapter, SQL schema, driver, migration framework, durable append/idempotency, writer-lease persistence, authoritative replay, crash recovery, projection storage/rebuild, network API, conformance adapter or ecosystem wiring.

The reducer processes logical in-memory Events only.

## Manifests

```text
profile-manifest.json → historical P0 planning snapshot
p1-manifest.json      → accepted P1 implementation/evidence state
```

All 72 contract assertions remain runtime `UNSUPPORTED` until a future P4 conformance adapter reports every assertion exactly once.

## Issue #1 and ecosystem separation

```text
P1 clean implementation
≠ recovered v0.1.2.1
≠ original 44 tests
≠ closure of source-recovery gate
```

No Titan, Mentaury or Crystal runtime integration is authorized.

## Next gates

1. finalize this post-merge checkpoint and Notion sync;
2. close Issue #43 as completed P1 scope;
3. keep P2 blocked until a separate operator GO;
4. keep runtime assertions `UNSUPPORTED` until P4;
5. obtain exact Python 3.11/3.12 repository workflow evidence when available;
6. preserve Issue #1 and Issue #18 as independent gates.

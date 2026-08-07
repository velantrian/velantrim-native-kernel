# 🧬 P3 Replay, Projection and Receipt Implementation Record

**Recorded:** 2026-08-07  
**Base public `main`:** `4e6be77196c633c25dd3896660335c1448b2baf5`  
**Final public merge:** `4af642930e18752f8f8b0bce75df355f76100d6f`  
**Canonical issue:** #49  
**Pull request:** #50 — merged  
**Evidence lineage:** `clean/postgresql-reference/0.1`  
**Profile:** `native-kernel/postgresql-reference@0.3-p3`

## Decision and maturity

```text
ADR-0017:                  ACCEPTED / APPROVED
P1 semantic core:          MERGED
P2 PostgreSQL append:      MERGED / REPOSITORY-INTEGRATION-TESTED
P3 replay/projections:     MERGED / REPOSITORY-INTEGRATION-TESTED / PARTIAL PROFILE
P4–P5:                     NOT AUTHORIZED
Kernel conformance:        UNSUPPORTED
C1/C2/C3:                  NOT ESTABLISHED
```

P3 implements a bounded profile mechanism. It does not establish a complete Kernel runtime, production readiness, assertion-level conformance or cross-profile equivalence.

## Executable path

```text
authoritative PostgreSQL Events
→ REPEATABLE READ selected-instance snapshot
→ Event count/max/head consistency checks
→ canonical payload and envelope verification
→ global hash-chain verification
→ explicit deterministic upcaster registry
→ P1 reducer from empty SemanticState
→ bounded persisted Replay Receipt
→ locked authoritative-head comparison
→ transactional disposable projection rebuild
→ bounded persisted Projection Rebuild Receipt
→ projection-to-Receipt linkage verification on load
```

## Implemented components

- `native_kernel.semantic_core.upcasting` — explicit deterministic one-successor upcaster paths;
- `native_kernel.semantic_core.state_codec` — canonical SemanticState decode/round trip;
- `native_kernel.postgresql_profile.history` — persisted Event snapshot and chain verification;
- `native_kernel.postgresql_profile.replay` — replay, projection persistence, destroy/rebuild, stale-head guard and linked rebuild-Receipt verification;
- `native_kernel.postgresql_profile.receipt_store` — canonical persisted bounded Receipts;
- `native_kernel.postgresql_profile.replay_models` — snapshot, projection and Receipt contracts;
- SQL migration `0002_p3_replay_projection_receipts.sql`;
- P3 manifest/validator and PostgreSQL matrix workflow.

There is no `verified_replay.py` module. Receipt-link verification is part of `replay.py` and is covered by the canonical P3 PostgreSQL integration suite.

## Final repository evidence

Final PR head:

```text
7e615bc633cbf966211d3b2815f51b8ff9eb9716
```

Workflow results:

```text
P3 replay/projection run 31173133661 — PASS
P2 regression run         31173133709 — PASS
P1 semantic core run      31173133657 — PASS
Fixture integrity run     31173133713 — PASS
AI context run            31173133635 — PASS
```

P3 matrix:

```text
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
```

Every P3 matrix job passed:

- 5 semantic/upcaster/Receipt tests;
- 5 P3 manifest and anti-overclaim tests;
- 8 PostgreSQL integration tests, including valid-but-mismatched projection Receipt linkage rejection;
- 9 P2 unit tests;
- 5 P2 PostgreSQL integration tests;
- Python compileall.

Squash merge:

```text
4af642930e18752f8f8b0bce75df355f76100d6f
```

No push-to-main workflow run was recorded for the merge SHA; this is `NOT_RECORDED`, not PASS. Runtime evidence applies to the exact final PR head and runs above.

## Defects found and corrected during review

1. AI-context regression tests still expected the P2 maturity marker after the validator moved to P3.
2. A projection row verified its own canonical state but did not prove that its referenced Receipt described the same projection rebuild.
3. The manifest validator treated only literal `PASS` as repository evidence, allowing an unrecognized PASS-like status to avoid the integration-evidence invariant.
4. A stale duplicate test expected different linkage-error wording even though the correct `ProjectionCorrupt` failure occurred; the duplicate was removed and the stable diagnostic includes `linked rebuild Receipt`.
5. A duplicate tracker Issue #51 was created while resuming context; it was closed as a duplicate of canonical Issue #49.
6. An early documentation record referenced a nonexistent `verified_replay.py`; the ownership map now points to `replay.py`.
7. Manifest and documentation inventory were aligned to the final deduplicated 8-scenario integration suite.

## Receipt evidence boundary

P3 Receipts report the selected instance, source range/head, reducer and target schema versions, state digest, projection identity/generation and explicit limitations.

They do **not** establish:

- truth of recorded Claims;
- external authenticity or signatures;
- absence of every privileged rewrite before the snapshot;
- complete Event Integrity under every threat model;
- physical or cryptographic erasure;
- production durability, security, privacy or compliance;
- C1, C2 or C3.

## Remaining risks and gates

- replay currently reads one Event per sequence and has no performance benchmark;
- only schema version `1` and explicitly registered upcast paths are supported;
- projections are disposable but operational monitoring/repair policy is absent;
- deletion execution remains absent;
- all 72 runtime assertions remain `UNSUPPORTED` until P4;
- P4 conformance adapter and P5 independent SQLite profile require separate operator GO;
- Issue #1 source recovery and Issue #18 licensing remain independent.

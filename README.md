# 🧬 Velantrim Native Kernel

### Technology-neutral semantic memory contracts with replaceable profiles and bounded evidence

> **Current state:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`

Native Kernel studies how semantic identity, Event history, deterministic replay and bounded evidence can preserve meaning across changing databases, languages, models and compute substrates.

It is **not** an operating-system kernel, Linux replacement, unikernel or device-driver framework.

```text
Architecture Canon
→ abstract contracts
→ replaceable PostgreSQL / SQLite profiles
→ C2 profile evidence
→ C3 cross-profile comparison
→ C4 offline shadow evaluation
→ C5 bounded synthetic operational rehearsal
```

PostgreSQL, SQLite, Python, JSON, CI, LLMs, vectors and hardware are replaceable instruments, not Canon.

## Current evidence

> **Integrity revalidation:** the preserved P5/C3/C4/C5 runs used SQLite 3.45.1. The current remediation candidate requires linked SQLite 3.51.3+, verifies the exact Event Envelope, and is awaiting repository reproduction. Historical artifacts remain unchanged; assertion counts are not promoted or silently rewritten.

```text
Single-profile C2: 41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED
Cross-profile C3:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
Offline C4 scope:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
C5 assertion map:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED
support_state:     PARTIAL
NK-EPI:            0 / 8 SUPPORTED
```

```text
kernel_runtime_conformance: C4
operational_validation: C5_BOUNDED_REHEARSAL
production_authorized: false
```

## Three independent tracks

```text
H — historical recovery
v0.1.2.1 and original 44-test suite
NOT_FOUND_IN_ACCESSIBLE_SOURCES / still open

C — clean implementation
P1–P5 + C4 + C5
ACTIVE / PARTIAL

R — long-horizon research
PROPOSED / BOUNDED / no automatic promotion
```

Clean implementation does not claim recovery of `v0.1.2.1`. Historical recovery does not block the clean lineage.

## C5 bounded operational rehearsal

```text
plan:       native-kernel/c5-bounded-rehearsal-v1
protocol:   nk-operational-plan/1
sha256:     4ed680ff4e83ac9d1aca6c1ab8a435ecb19af4a5badf1be8202bc842f964b098
scenarios:  18
deployment: CI_EPHEMERAL_SYNTHETIC
```

Final verified checkpoint:

```text
head 3d56912260ea41b5b501b65477bff1642dfc2d58
run  31205512911 — PASS
Python 3.11/3.12 × PostgreSQL 16/18 × SQLite 3.45.1
```

This matrix is historical evidence of those exact runs, not the current SQLite minimum. See [ADR-0023](docs/adr/0023-harden-sqlite-wal-and-event-integrity.md).

```text
18/18 scenarios PASS in every matrix job
18 Receipts per job
0 canary leaks
0 recovery failures
0 uncontained incidents
```

The exact ZIP bytes from both the implementation-main and final-main C5 runs are preserved under [`evidence/c5/`](evidence/c5/README.md) with archive- and file-level hashes.

## Explicit boundary

```text
C5 bounded rehearsal
≠ production readiness
≠ live user traffic
≠ cloud IAM / multi-region HA
≠ compliance certification
≠ physical backup or deletion
≠ operational equivalence
≠ authority promotion
≠ ecosystem wiring
≠ NK-EPI promotion
```

## Read next

- [`project-state.json`](project-state.json)
- [`STATUS.md`](STATUS.md)
- [`AGENTS.md`](AGENTS.md)
- [`evidence/c5/README.md`](evidence/c5/README.md)
- [`docs/ai/C5_IMPLEMENTATION_RECORD.md`](docs/ai/C5_IMPLEMENTATION_RECORD.md)
- [`docs/research/POST_C5_RESEARCH_BACKLOG.md`](docs/research/POST_C5_RESEARCH_BACKLOG.md)
- [`docs/CONFORMANCE_MODEL.md`](docs/CONFORMANCE_MODEL.md)

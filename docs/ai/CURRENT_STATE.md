# 📍 Native Kernel Current State Checkpoint

**Verified:** 2026-08-07  
**Last verified public `main`:** `296981ae84ad5bdab5dabbec9b7b9ebb43af63d7`  
**Active issue / PR / ADR:** #64 / #65 merged / ADR-0021  
**Repository status:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`

> Context checkpoint ≠ automatically current main. Re-check the actual branch ref, plan digest, workflows, reports and retained artifact bytes.

```text
NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST
C2 ≠ C3 ≠ C4 ≠ C5
C5 BOUNDED REHEARSAL ≠ PRODUCTION READINESS
C5 SYNTHETIC DATA ≠ LIVE USER TRAFFIC
C5 OPERATIONAL VALIDATION ≠ ASSERTION PROMOTION
C5 LOGICAL BACKUP ≠ PHYSICAL DISASTER RECOVERY
ASSERTION EVIDENCE ≠ TRUTH / AUTHENTICITY / PHYSICAL ERASURE
```

## Current gate

```text
P1–P5:                 MERGED
C4 offline shadow:     MERGED / PARTIAL / REPOSITORY-REPRODUCED
C5 operational:        MERGED / PARTIAL / REPOSITORY-REPRODUCED
Production/live data:  NOT AUTHORIZED / NOT ESTABLISHED
Issue #1 / #18:        ACTIVE / INDEPENDENT
```

## Publication lineage

```text
Base main:       d1dd4986a8496cd9ca3e353d33ca422038c65d40
PR #65 head:     1c4dcc4b9d9b86d5737388ce1469a0bc2420f0e6
PR #65 merge:    296981ae84ad5bdab5dabbec9b7b9ebb43af63d7
```

## Distinct evidence dimensions

```text
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
support_state:              PARTIAL
assertion map:              45 / 10 / 17 / 0
```

C5 adds bounded operational evidence without promoting the 10 partial or 17 unsupported assertions.

## Immutable plan

```text
native-kernel/c5-bounded-rehearsal-v1
nk-operational-plan/1
sha256 4ed680ff4e83ac9d1aca6c1ab8a435ecb19af4a5badf1be8202bc842f964b098
18 scenarios
CI_EPHEMERAL_SYNTHETIC
```

## Exact implementation-main evidence

```text
Main:       296981ae84ad5bdab5dabbec9b7b9ebb43af63d7
C5:         31204861404 — PASS
C4:         31204861534 — PASS
P5/C3:      31204861602 — PASS
P4:         31204861564 — PASS
AI context: 31204861416 — PASS
```

```text
Python 3.11 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.11 / PostgreSQL 18 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 18 / SQLite 3.45.1 — PASS
```

Main-bound artifact digests:

```text
py3.11/pg16 sha256:25e019cf8428d4697bf3f1f777a3fa8ff0f5e2aac6053e006e2549ecff55f0c0
py3.11/pg18 sha256:e7a717ff3e7671c82a4544d68d9d16303fccf1fe52fb713d9ad9b286e4e570dd
py3.12/pg16 sha256:006c56d8cbe8e75b18a28695ca82228b9c55b5d3eab5b31079c1dcfb5b46c331
py3.12/pg18 sha256:029d2df8d1b32631d6b8a5939b661df0e1a1d2272218766e8371b8c84adb0d82
```

Inspected main-bound artifact:

```text
18/18 scenarios PASS
18 Receipts
0 canary leaks
0 recovery failures
0 uncontained incidents
p95 append 11.055 ms
total 960.806 ms
4-event logical backup validated and imported in quarantine
```

Every Receipt recorded `REHEARSAL_OBSERVATION_ONLY` and denied authority promotion, external side effects, live user data, production approval, physical deletion proof and compliance certification.

## Operational proof boundary

The rehearsal proves only the named synthetic scenarios in one ephemeral CI environment. It does not establish production security, live privacy, provider IAM, multi-region availability, regulatory compliance, physical backup/restore, physical deletion or ecosystem authority.

## Next action

Merge the documentation-only checkpoint, reproduce bounded C5 and AI gates on the resulting `main`, synchronize Notion and close Issue #64.

# 🛡️ C5 Bounded Operational Rehearsal — implementation and preservation record

**Date:** 2026-08-07
**Issue / PR / ADR:** #64 `CLOSED / COMPLETED` / #65 merged / ADR-0021 accepted
**Implementation merge/main:** `296981ae84ad5bdab5dabbec9b7b9ebb43af63d7`
**Final documentation checkpoint:** `3d56912260ea41b5b501b65477bff1642dfc2d58`
**State:** `MERGED / C5 PARTIAL / BOUNDED SYNTHETIC OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`

## Authorized boundary

```text
CONTROLLED_EPHEMERAL_SYNTHETIC_ONLY
NO LIVE USER DATA
NO PRODUCTION TRAFFIC
NO NETWORK API
NO AUTHORITY PROMOTION
NO EXTERNAL SIDE EFFECTS
NO ECOSYSTEM WIRING
NO PHYSICAL DELETION CLAIM
NO COMPLIANCE CERTIFICATION
```

## Plan and protocols

```text
plan_id:   native-kernel/c5-bounded-rehearsal-v1
sha256:    4ed680ff4e83ac9d1aca6c1ab8a435ecb19af4a5badf1be8202bc842f964b098
scenarios: 18

nk-operational-plan/1
nk-operational-report/1
nk-operational-receipt/1
nk-operational-backup/1
```

## Scenario inventory

```text
2 authority-denial
2 stale-writer fencing
2 idempotent retry
2 injected-fault rollback
2 replay/projection recovery
1 quarantined exact-history import
2 corruption detection
1 incident timeline
2 privacy/synthetic-data
2 bounded-load latency
```

## Semantic boundary

```text
operational_validation:     C5_BOUNDED_REHEARSAL
kernel_runtime_conformance: C4
support_state:              PARTIAL
assertions:                 45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
NK-EPI:                     0 SUPPORTED / 0 PARTIAL / 8 UNSUPPORTED / 0 FAILED
```

## Exact implementation-main evidence

```text
Main:       296981ae84ad5bdab5dabbec9b7b9ebb43af63d7
C5:        31204861404 — PASS
C4:        31204861534 — PASS
P5/C3:     31204861602 — PASS
P4:        31204861564 — PASS
AI context:31204861416 — PASS
```

Artifact digests:

```text
py3.11/pg16 sha256:25e019cf8428d4697bf3f1f777a3fa8ff0f5e2aac6053e006e2549ecff55f0c0
py3.11/pg18 sha256:e7a717ff3e7671c82a4544d68d9d16303fccf1fe52fb713d9ad9b286e4e570dd
py3.12/pg16 sha256:006c56d8cbe8e75b18a28695ca82228b9c55b5d3eab5b31079c1dcfb5b46c331
py3.12/pg18 sha256:029d2df8d1b32631d6b8a5939b661df0e1a1d2272218766e8371b8c84adb0d82
```

Inspected result:

```text
18/18 scenarios PASS
18 operational Receipts
0 privacy canary leaks
0 recovery failures
0 uncontained incidents
p95 append latency 11.055 ms
total duration 960.806 ms
```

## Exact final-main evidence

```text
Main:       3d56912260ea41b5b501b65477bff1642dfc2d58
C5:        31205512911 — PASS
C4:        31205512919 — PASS
P5/C3:     31205512874 — PASS
P4:        31205512957 — PASS
AI context:31205512966 — PASS
```

Artifact digests:

```text
py3.11/pg16 sha256:7a17248c3cbd612df93b85956299160a99c5e4ca4b97d27da492958731a6b8a5
py3.11/pg18 sha256:b285a118c562f58df0bbe1411f1ef3cec9c9767c68f8ce3b9cee2054b4bc407a
py3.12/pg16 sha256:714e18a6b0974ebbfc708b6ae4de129ca1d4c8666337ac3a53e99e10d86f2e92
py3.12/pg18 sha256:4a68f36a17e958c1def3923d3181ebcd974e8a3adba94fb4892ec02505720f4c
```

All four jobs passed 18/18 scenarios with 18 Receipts and zero canary/recovery/incident failures. Exact per-environment metrics remain in the retained reports.

## Durable preservation

Eight exact original ZIP archives are committed under:

```text
evidence/c5/2026-08-07/original/
```

Their archive hashes, internal file inventories and file hashes are bound by:

```text
evidence/c5/2026-08-07/manifest.json
```

Verifier:

```bash
python tools/evidence/verify_bundle.py evidence/c5/2026-08-07/manifest.json
```

The source GitHub artifacts expire on 2026-09-06; the repository-resident bytes do not.

## Logical backup boundary

Each artifact contains a four-Event application-level logical backup with validated digest and quarantined exact-history import. This is not a physical PostgreSQL backup, WAL recovery, point-in-time recovery or provider DR proof.

## Non-claims

```text
bounded C5 rehearsal
≠ production readiness
≠ live-traffic evidence
≠ cloud IAM / multi-region HA
≠ exhaustive DR
≠ physical backup
≠ physical deletion
≠ compliance certification
≠ operational equivalence
≠ NK-EPI promotion
```

## Completion

Issue #64 is closed as completed. Remaining work is independent: project-state governance, documentation/Notion synchronization, operational hardening and separately authorized epistemic work.

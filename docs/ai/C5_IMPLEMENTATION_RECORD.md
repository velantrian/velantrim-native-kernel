# 🛡️ C5 Bounded Operational Rehearsal — implementation record

**Date:** 2026-08-07  
**Issue / PR / ADR:** #64 / #65 / ADR-0021  
**Base main:** `d1dd4986a8496cd9ca3e353d33ca422038c65d40`  
**Implementation merge/main:** `296981ae84ad5bdab5dabbec9b7b9ebb43af63d7`  
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
```

```text
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
```

## Publication lineage

```text
PR #65 final head: 1c4dcc4b9d9b86d5737388ce1469a0bc2420f0e6
PR #65 merge/main: 296981ae84ad5bdab5dabbec9b7b9ebb43af63d7
```

## Source and documentation delivery evidence

```text
source bootstrap run: 31202306008 — PASS
source archive sha256:76730d288440ebf4c25d5fc35a2e1e4e2e414d6ad5e65999a4060d400735a0dc
docs archive sha256:  056eb51ae1a825c462b691919e9878742d3eb6c4c637c8244afca3030f981d59
docs publication run: 31204169007 — PASS
```

Rejected transport/publication attempts were not counted as implementation evidence. The first genuine matrix exposed only a CLI import-path defect; `PYTHONPATH=.` fixed the environment without changing scenarios, thresholds or proof boundaries. Temporary source/docs transport files and workflows were removed before review.

## Exact final-PR-head evidence

```text
Head:       1c4dcc4b9d9b86d5737388ce1469a0bc2420f0e6
C5:        31204406663 — PASS
C4:        31204406695 — PASS
P5/C3:     31204406946 — PASS
P4:        31204406606 — PASS
P1:        31204407186 — PASS
Fixtures:  31204409411 — PASS
AI context:31204409408 — PASS
```

Final-head artifact digests:

```text
py3.11/pg16 sha256:13926afbd797cc8462b264bea948347f6ba739cc88177ee83610782fe4b32e5b
py3.11/pg18 sha256:06e9bd2ca78f584065cd5bea3d77dfea96c5bb4564e92a5b1d2c1b21de58a0f5
py3.12/pg16 sha256:60c53b2cc5c01576e601f8a644416c1fb68c2ed0e66cb6113487ea6b2de33ce4
py3.12/pg18 sha256:ea05544497fbf04750993c66710b4dd3860ca3cbac8556793bfb72680495412b
```

Inspected final-head result:

```text
18/18 scenarios PASS
18 operational Receipts
0 privacy canary leaks
0 recovery failures
0 uncontained incidents
p95 append latency 12.421 ms
total duration 1011.689 ms
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

Main-bound artifact digests:

```text
py3.11/pg16 sha256:25e019cf8428d4697bf3f1f777a3fa8ff0f5e2aac6053e006e2549ecff55f0c0
py3.11/pg18 sha256:e7a717ff3e7671c82a4544d68d9d16303fccf1fe52fb713d9ad9b286e4e570dd
py3.12/pg16 sha256:006c56d8cbe8e75b18a28695ca82228b9c55b5d3eab5b31079c1dcfb5b46c331
py3.12/pg18 sha256:029d2df8d1b32631d6b8a5939b661df0e1a1d2272218766e8371b8c84adb0d82
```

Inspected main-bound result:

```text
18/18 scenarios PASS
18 operational Receipts
0 privacy canary leaks
0 recovery failures
0 uncontained incidents
p95 append latency 11.055 ms
total duration 960.806 ms
```

Logical backup:

```text
protocol: nk-operational-backup/1
events: 4
digest validated
quarantined exact-history import: PASS
canary tokens in report/backup: 0
```

All Receipts used `REHEARSAL_OBSERVATION_ONLY` and explicitly denied authority promotion, external side effects, live user data, production approval, physical deletion proof and compliance certification.

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
```

## Remaining publication gate

Merge the documentation-only checkpoint, repeat bounded C5/AI evidence on the resulting `main`, synchronize Notion and close Issue #64.

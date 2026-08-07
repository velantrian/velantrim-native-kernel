# Current Status

> **Verified:** 2026-08-07  
> **Last verified public `main`:** `296981ae84ad5bdab5dabbec9b7b9ebb43af63d7`  
> **Implementation publication:** Issue #64 / PR #65 merged / ADR-0021  
> **Repository status:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`

## Current phase

```text
P1: MERGED / REPOSITORY-TESTED
P2: MERGED / REPOSITORY-INTEGRATION-TESTED
P3: MERGED / REPOSITORY-INTEGRATION-TESTED
P4: MERGED / PARTIAL / POSTGRESQL C2
P5: MERGED / PARTIAL / SQLITE C2 + CROSS-PROFILE C3
C4: MERGED / PARTIAL / OFFLINE SHADOW EVIDENCE
C5: MERGED / PARTIAL / BOUNDED SYNTHETIC OPERATIONAL REHEARSAL
Production: NOT AUTHORIZED / NOT ESTABLISHED
```

C5 is a bounded operational evidence layer. It is not a new storage profile, production deployment, public service, compliance certification or ecosystem authority.

## Publication lineage

```text
C5 base main:      d1dd4986a8496cd9ca3e353d33ca422038c65d40
PR #65 final head: 1c4dcc4b9d9b86d5737388ce1469a0bc2420f0e6
PR #65 merge/main: 296981ae84ad5bdab5dabbec9b7b9ebb43af63d7
```

## Semantic and operational levels

```text
kernel_runtime_conformance: C4
operational_validation:     C5_BOUNDED_REHEARSAL
support_state:              PARTIAL
```

```text
Single-profile C2: 41 SUPPORTED / 13 PARTIAL / 18 UNSUPPORTED / 0 FAILED
Cross-profile C3:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
Offline C4 scope:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
C5 assertion map:  45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
```

C5 does not promote semantic assertions. All `NK-EPI-001…008` remain `UNSUPPORTED / PROPOSED`.

## Operational plan

```text
plan_id:       native-kernel/c5-bounded-rehearsal-v1
protocol:      nk-operational-plan/1
sha256:        4ed680ff4e83ac9d1aca6c1ab8a435ecb19af4a5badf1be8202bc842f964b098
scenarios:     18
deployment:    CI_EPHEMERAL_SYNTHETIC
```

Categories: `SECURITY · PRIVACY · RECOVERY · ROLLBACK · INCIDENT · RELIABILITY · RESILIENCE`.

## Mandatory deployment boundary

```text
live_user_data: false
synthetic_data_only: true
production_traffic: false
network_api_exposed: false
authority_promotion: false
authoritative_external_side_effects: false
ecosystem_wiring: false
physical_deletion_claimed: false
compliance_certification_claimed: false
```

## Exact final-PR-head evidence

```text
Final head:  1c4dcc4b9d9b86d5737388ce1469a0bc2420f0e6
C5:         31204406663 — PASS
C4:         31204406695 — PASS
P5/C3:      31204406946 — PASS
P4:         31204406606 — PASS
P1:         31204407186 — PASS
Fixtures:   31204409411 — PASS
AI context: 31204409408 — PASS
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

C5 matrix:

```text
Python 3.11 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.11 / PostgreSQL 18 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 18 / SQLite 3.45.1 — PASS
```

Every job passed C5 guards, exact P4/P5/C3/C4 prerequisites, all 18 scenarios, P1–C4 regressions, compileall and six-report artifact upload.

## Main-bound artifacts

```text
py3.11/pg16 sha256:25e019cf8428d4697bf3f1f777a3fa8ff0f5e2aac6053e006e2549ecff55f0c0
py3.11/pg18 sha256:e7a717ff3e7671c82a4544d68d9d16303fccf1fe52fb713d9ad9b286e4e570dd
py3.12/pg16 sha256:006c56d8cbe8e75b18a28695ca82228b9c55b5d3eab5b31079c1dcfb5b46c331
py3.12/pg18 sha256:029d2df8d1b32631d6b8a5939b661df0e1a1d2272218766e8371b8c84adb0d82
```

Artifacts are retained until 2026-09-06. Each contains P4, P5, C3, C4, C5 and logical-backup reports.

## Inspected main-bound result

```text
18 / 18 scenarios PASS
18 operational Receipts
0 privacy canary leaks
0 recovery failures
0 uncontained incidents
p95 append latency: 11.055 ms
total rehearsal duration: 960.806 ms
assertion map: 45 / 10 / 17 / 0
```

The logical backup contained four exact synthetic PostgreSQL Events, a validated digest and successful quarantined SQLite exact-history import. Both privacy canaries were absent from report and backup bytes. All Receipts denied live data, authority promotion, external side effects, production approval, physical deletion proof and compliance certification.

## Explicit non-claims

```text
C5 bounded rehearsal PASS
≠ production readiness
≠ live user traffic validation
≠ cloud IAM or multi-region HA proof
≠ exhaustive disaster recovery
≠ physical PostgreSQL backup
≠ physical or cryptographic deletion
≠ compliance certification
≠ operational equivalence
≠ authority promotion
≠ ecosystem wiring
```

## Next gate

Merge this documentation-only checkpoint, reproduce its bounded C5/AI evidence on the resulting `main`, synchronize Notion and close Issue #64. Any production, live-traffic, cloud deployment, physical deletion or ecosystem-authority work requires separate explicit operator approval.

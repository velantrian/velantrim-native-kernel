# Current Status

> **Verified:** 2026-08-07  
> **Last verified public `main`:** `d1dd4986a8496cd9ca3e353d33ca422038c65d40`  
> **Current publication candidate:** Issue #64 / PR #65 / ADR-0021  
> **Repository status:** `RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`

## Current phase

```text
P1: MERGED / REPOSITORY-TESTED
P2: MERGED / REPOSITORY-INTEGRATION-TESTED
P3: MERGED / REPOSITORY-INTEGRATION-TESTED
P4: MERGED / PARTIAL / POSTGRESQL C2
P5: MERGED / PARTIAL / SQLITE C2 + CROSS-PROFILE C3
C4: MERGED / PARTIAL / OFFLINE SHADOW EVIDENCE
C5: PR #65 OPEN / PARTIAL / BOUNDED SYNTHETIC OPERATIONAL REHEARSAL
Production: NOT AUTHORIZED / NOT ESTABLISHED
```

C5 is a bounded operational evidence layer. It is not a new storage profile, a production deployment, a public service, a compliance certification, or ecosystem authority.

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

Categories:

```text
SECURITY · PRIVACY · RECOVERY · ROLLBACK · INCIDENT · RELIABILITY · RESILIENCE
```

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

## First repository C5 evidence

```text
Evidence head: 260922de9f2a62b28697db3237b5ebfc7558edec
C5 run:       31202900408 — PASS
```

Matrix:

```text
Python 3.11 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.11 / PostgreSQL 18 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 16 / SQLite 3.45.1 — PASS
Python 3.12 / PostgreSQL 18 / SQLite 3.45.1 — PASS
```

Every job passed:
- C5 unit/report/manifest guards;
- exact P4, P5, C3 and C4 prerequisite reports;
- 18 operational scenarios;
- P1–C4 regressions;
- compileall;
- six-report artifact upload.

## Inspected artifact result

```text
18 / 18 scenarios PASS
18 operational Receipts
0 privacy canary leaks
0 recovery failures
0 uncontained incidents
p95 append latency: 11.484 ms
total rehearsal duration: 975.163 ms
assertion map: 45 / 10 / 17 / 0
```

The inspected logical backup contained four exact synthetic Events and passed digest validation and quarantined import/replay. Both configured canaries were absent from report and backup bytes.

All inspected Receipts recorded:

```text
decision: REHEARSAL_OBSERVATION_ONLY
live_user_data_used: false
authority_promoted: false
authoritative_external_side_effects: false
production_approved: false
physical_deletion_proved: false
compliance_certified: false
```

## First artifact digests

```text
py3.11/pg16 sha256:4fd218d6a3d6869cd7e5ede6269a4ee02b6c74bc4d4bb6b8a979d6f69932373e
py3.11/pg18 sha256:5e94f927ae5353eb356f012f1a3e667fb5e78407ceb357b908af98b784bdecb9
py3.12/pg16 sha256:b74611b99ad2e1c07862466278d03c8c60d91469eb8f5e922f1fd1565b3048a4
py3.12/pg18 sha256:ef28de467b35d934ed56c751cd648d7d879b16f69d8ad7709ae504bb29d3a8c6
```

Artifacts are retained until 2026-09-06.

## What C5 establishes

Within the exact synthetic ephemeral CI plan, repository evidence exists for:

- deny-by-default authority;
- stale-writer fencing;
- idempotent retry;
- rollback after injected precommit faults;
- deterministic replay and projection rebuild;
- application-level logical Event export;
- quarantined exact-history import and replay;
- corruption detection and containment;
- incident-stage recording;
- privacy canary redaction;
- bounded append workload and latency measurement.

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

Finish exact final-head evidence, review and merge PR #65, reproduce C5 on `main`, publish a documentation checkpoint and synchronize Notion. Any production, live-traffic, cloud deployment, physical deletion or ecosystem authority work requires separate explicit operator approval.

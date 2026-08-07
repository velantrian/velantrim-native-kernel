# 🛡️ C5 Bounded Operational Rehearsal — implementation record

**Date:** 2026-08-07  
**Issue / PR / ADR:** #64 / #65 / ADR-0021  
**Base main:** `d1dd4986a8496cd9ca3e353d33ca422038c65d40`  
**State:** `C5 PARTIAL / BOUNDED SYNTHETIC OPERATIONAL REHEARSAL / NOT PRODUCTION-READY`

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
plan_id:  native-kernel/c5-bounded-rehearsal-v1
sha256:   4ed680ff4e83ac9d1aca6c1ab8a435ecb19af4a5badf1be8202bc842f964b098
scenarios:18
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

## Source delivery evidence

The source payload was verified by six part digests and a final archive digest:

```text
bootstrap run: 31202306008 — PASS
archive sha256:76730d288440ebf4c25d5fc35a2e1e4e2e414d6ad5e65999a4060d400735a0dc
```

The first source publisher validation passed but its publication step attempted to modify workflow files with `GITHUB_TOKEN`; that publication was rejected and not counted as source evidence. The publisher was separated from workflow creation/cleanup, then completed successfully. Temporary source transport files were removed before the PR.

## First genuine matrix defect

The first genuine matrix failed before scenario execution because direct CLI execution could not import the repository package. `PYTHONPATH=.` was added to the workflow without changing scenarios, thresholds or proof boundaries.

## First complete repository evidence

```text
Head:    260922de9f2a62b28697db3237b5ebfc7558edec
Run:     31202900408 — PASS
Matrix:  Python 3.11/3.12 × PostgreSQL 16/18 × SQLite 3.45.1
```

Every job created six retained reports and passed P1–C4 regressions.

Artifact digests:

```text
py3.11/pg16 sha256:4fd218d6a3d6869cd7e5ede6269a4ee02b6c74bc4d4bb6b8a979d6f69932373e
py3.11/pg18 sha256:5e94f927ae5353eb356f012f1a3e667fb5e78407ceb357b908af98b784bdecb9
py3.12/pg16 sha256:b74611b99ad2e1c07862466278d03c8c60d91469eb8f5e922f1fd1565b3048a4
py3.12/pg18 sha256:ef28de467b35d934ed56c751cd648d7d879b16f69d8ad7709ae504bb29d3a8c6
```

Inspected `py3.11/pg16` result:

```text
18/18 scenarios PASS
18 operational Receipts
0 privacy canary leaks
0 recovery failures
0 uncontained incidents
p95 append latency 11.484 ms
total duration 975.163 ms
```

Logical backup:

```text
protocol: nk-operational-backup/1
events: 4
digest validated
quarantined exact-history import: PASS
canary tokens in report/backup: 0
```

## Documentation publication evidence

The C5 continuity archive contained 14 public/AI/governance files:

```text
archive sha256:056eb51ae1a825c462b691919e9878742d3eb6c4c637c8244afca3030f981d59
base64 bytes: 17196
```

Publication history:

1. Run `31203785312` failed before extraction because one character was missing from `part-00`; no documentation was published.
2. The exact byte was restored. Run `31204012871` verified all five part digests and the final archive SHA, then exposed a stale negative manifest test that still assumed `PRE_CI`.
3. The negative test was updated to erase exact SHA/run/matrix/artifact fields from a `PASS` manifest and continued to require fail-closed rejection.
4. Run `31204169007` passed archive verification, eight AI-context tests, the repository AI-context guard, all C5 unit/report/manifest tests, the manifest validator and compileall, then published the documentation commit.
5. Temporary documentation transport files and workflow were removed atomically before the final PR head.

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

Repeat C5 and all prerequisite workflows on the exact final PR head, inspect a final six-report artifact, review and merge PR #65, reproduce on `main`, publish a docs checkpoint and synchronize Notion.

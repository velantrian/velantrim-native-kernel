# ⚠️ Native Kernel Known Risks and Required Proof

**Snapshot:** 2026-08-07  
**Last verified public `main`:** `d1dd4986a8496cd9ca3e353d33ca422038c65d40`  
**Latest candidate:** C5 bounded synthetic operational rehearsal / PR #65

C5 closes none of the production, live-data, compliance, physical-deletion, provider-IAM, multi-region, source-recovery or ecosystem-authority risks.

## P0 — Bounded rehearsal may be mistaken for production readiness

```text
ephemeral CI + synthetic data + 18 scenarios
≠ production deployment
≠ live user traffic
≠ sustained operations
```

**State:** `OPEN / PRIMARY C5 COMMUNICATION RISK`.

## P0 — C5 may be mistaken for assertion promotion

```text
kernel_runtime_conformance: C4
operational_validation: C5_BOUNDED_REHEARSAL
assertion map: 45 / 10 / 17 / 0
```

**State:** `OPEN`, machine-guarded. Operational evidence does not turn partial or unsupported semantic assertions into supported ones.

## P0 — Synthetic privacy checks may be mistaken for privacy compliance

Two canaries were redacted and absent from inspected artifacts. This does not prove handling of real personal data, data subject rights, jurisdictional compliance, retention, breach response, or provider logs.

## P0 — Application-level logical export may be mistaken for disaster recovery

The backup contains exact synthetic Event bytes for one instance and supports quarantined import/replay. It is not a physical PostgreSQL backup, WAL restore, managed-provider snapshot, point-in-time recovery, cross-region restore, or restore-under-load proof.

## P0 — Application fencing may be mistaken for cloud IAM/security certification

Authority denial and stale-writer fencing passed. Cloud IAM, secret rotation, network policy, tenant isolation, host hardening, supply-chain security, vulnerability response and penetration testing remain unproven.

## P0 — Incident script may be mistaken for operational incident readiness

The timeline records `DETECTED → CONTAINED → EVIDENCE_CAPTURED → RECOVERY_VALIDATED`. It does not prove human on-call response, escalation, communications, forensics, legal obligations, or recovery under a real outage.

## P0 — Physical deletion remains absent

No physical or cryptographic deletion is executed across databases, backups, logs, artifacts, providers or keys. All Receipts explicitly deny this proof.

## P0 — Operational equivalence remains absent

PostgreSQL and SQLite pass the same bounded scenarios, but concurrency, durability, replication, failover, administration, filesystem and managed-provider behaviour remain different.

## P0 — Source recovery remains unresolved

```text
clean P1–P5 + C4 + C5
≠ recovered v0.1.2.1
≠ original 44-test evidence
```

Issue #1 remains independent. `NOT_FOUND_IN_ACCESSIBLE_SOURCES ≠ GLOBALLY_LOST`.

## P1 — Threshold representativeness

The current p95 limit is 5000 ms and workload is 24 Events per profile. Passing this bounded threshold is not a capacity, scale, SLO or cost claim.

## P1 — Artifact retention

First C5 artifacts expire 2026-09-06. Digests without retained bytes are not independent reproduction evidence.

## P1 — Plan governance

The plan is repository-local and approved by ADR-0021. There is no signed plan registry, independent reviewer quorum, revocation system or external audit.

## P1 — Environment scope

Current evidence is Ubuntu 24.04, Python 3.11/3.12, PostgreSQL 16/18 and runner SQLite 3.45.1. Other OS, architecture, provider, filesystem and runtime combinations are untested.

## P1 — Final-head evidence drift

First complete evidence passed on `260922de…`. Documentation and manifest commits changed the branch. Final-head C5 evidence must be repeated before merge, and main-bound evidence must be repeated after merge.

## Update rule

Always record exact plan ID/digest, scenario inventory, thresholds, SHA, run, artifact bytes, limitations and next gate. Never convert one bounded PASS into production, compliance, live-data, physical-deletion or ecosystem-authority claims.

# C5 bounded operational rehearsal

> **State:** implementation candidate / controlled ephemeral synthetic evidence only

## Architecture

```text
exact C4 report + approved immutable C5 plan
        ↓
18 profile/shared operational scenarios
        ↓
security · privacy · reliability · rollback · recovery · incident · resilience
        ↓
one bounded operational Receipt per scenario
        ↓
fail-closed nk-operational-report/1
```

The rehearsal is an evidence harness. It does not become Architecture Canon, a new storage profile, a command authority or a production deployment controller.

## Plan identity

```text
plan_id: native-kernel/c5-bounded-rehearsal-v1
protocol: nk-operational-plan/1
SHA-256: derived from exact committed bytes
scenarios: 18
```

## Scenario inventory

```text
SECURITY    4  authority denial + stale-writer fencing
RELIABILITY 2  idempotent retry
ROLLBACK    2  injected precommit fault rollback
RECOVERY    3  replay/projection + quarantined exact-history import
INCIDENT    3  corruption detection + ordered containment timeline
PRIVACY     2  synthetic-only boundary + canary redaction
RESILIENCE  2  bounded 24-event append workload and p95 latency
```

## Backup/restore boundary

The recovery artifact is `nk-operational-backup/1`: an application-level logical export of exact Event canonical bytes and commitments for one synthetic instance. It is restored into an empty quarantined SQLite instance and replayed before visibility.

It is not a physical PostgreSQL backup, WAL archive, managed-provider snapshot, multi-region restore or complete disaster-recovery proof.

## Privacy boundary

Two explicit canaries are inserted only into the redaction scenario. The report and backup validators reject any emitted canary. No real personal data or credentials are permitted.

## Incident boundary

Corruption is injected into one synthetic instance per profile. Replay must fail closed. Incident evidence records ordered `DETECTED → CONTAINED → EVIDENCE_CAPTURED → RECOVERY_VALIDATED` stages. This is a rehearsal timeline, not an external incident-response certification.

## Thresholds

```text
18 required scenarios
0 failed scenarios
0 canary leaks
0 recovery failures
0 uncontained incidents
p95 append <= 5000 ms
total rehearsal <= 240 s
<= 64 events per profile workload
```

## Report semantics

```text
operational_validation: C5_BOUNDED_REHEARSAL
kernel_runtime_conformance: C4
support_state: PARTIAL
```

C5 operational evidence must never promote `PARTIAL`, `UNSUPPORTED` or proposed `NK-EPI` assertions.

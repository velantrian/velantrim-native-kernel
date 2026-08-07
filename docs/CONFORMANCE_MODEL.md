# 🧪 Conformance and Operational Evidence Model

## Levels

| Level | Meaning |
|---|---|
| C0 | described mapping |
| C1 | local execution evidence |
| C2 | repository-reproduced single-profile assertion evidence |
| C3 | declared cross-profile semantic equivalence |
| C4 | approved offline recorded-workload shadow evaluation |
| C5 | bounded operational validation rehearsal |

Levels are assertion- and scope-specific.

```text
kernel_runtime_conformance: C4
operational_validation: C5_BOUNDED_REHEARSAL
support_state: PARTIAL
```

A C5 operational result does not promote semantic assertions.

## Current maps

```text
PostgreSQL C2: 41 / 13 / 18 / 0
SQLite C2:     41 / 13 / 18 / 0
C3:            45 / 10 / 17 / 0
C4:            45 / 10 / 17 / 0
C5 inherited:  45 / 10 / 17 / 0
```

## C5 requirements

C5 requires:
- exact immutable operational plan;
- synthetic ephemeral deployment boundary;
- exact C4 prerequisite;
- security/privacy/recovery/rollback/incident/reliability/resilience scenarios;
- one bounded operational Receipt per scenario;
- strict thresholds and fail-closed status;
- exact environment/run/artifact traceability;
- explicit unresolved production risks.

Current plan:

```text
native-kernel/c5-bounded-rehearsal-v1
sha256 4ed680ff4e83ac9d1aca6c1ab8a435ecb19af4a5badf1be8202bc842f964b098
18 scenarios
```

## C5 report protocols

```text
nk-operational-plan/1
nk-operational-report/1
nk-operational-receipt/1
nk-operational-backup/1
```

## Current evidence

```text
head 260922de9f2a62b28697db3237b5ebfc7558edec
run 31202900408 PASS
4 environments
18/18 scenarios
18 Receipts
0 canary/recovery/incident failures
```

## Non-conformance examples

```text
❌ Describing synthetic CI as live production.
❌ Describing C5 as support for all 72 assertions.
❌ Describing application-level Event export as physical DR.
❌ Describing authority fencing as cloud IAM certification.
❌ Describing canary redaction as privacy compliance.
❌ Describing bounded load as a scale/SLO guarantee.
❌ Describing Receipts as truth, deletion or safety certificates.
```

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
NK-EPI:         0 /  0 /  8 / 0
```

## Evidence dimensions

```text
decision status
≠ contract status
≠ implementation status
≠ conformance evidence
≠ operational evidence
≠ production authorization
```

## C5 requirements

C5 requires:

- exact immutable operational plan;
- synthetic ephemeral deployment boundary;
- exact C4 prerequisite;
- named security/privacy/recovery/rollback/incident/reliability/resilience scenarios;
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

## Durable evidence

The exact ZIP bytes for two accepted C5 checkpoints are preserved under:

```text
evidence/c5/2026-08-07/manifest.json
```

Retention proves only preservation of the producing runs' bytes and declared bounded results. It does not expand the proof boundary.

## NK-EPI boundary

`NK-EPI-001…008` remain `PROPOSED / UNSUPPORTED`. Fixture descriptions are not runtime conformance.

The first research candidate is:

```text
NK-EPI-004
unknown or unanswered is not silently treated as false
```

Promotion requires a separate decision, normative contract, positive/negative/invalid fixtures, implementation, profile execution, replay/projection checks, Receipt validation and exact evidence.

## Non-conformance examples

```text
❌ Describing synthetic CI as live production.
❌ Describing C5 as support for all 72 assertions.
❌ Describing retained ZIPs as independent production proof.
❌ Describing application Event export as physical DR.
❌ Describing authority fencing as cloud IAM certification.
❌ Describing canary redaction as privacy compliance.
❌ Describing bounded load as a scale/SLO guarantee.
❌ Describing Receipts as truth, deletion or safety certificates.
❌ Describing a research proposal as supported runtime behavior.
```

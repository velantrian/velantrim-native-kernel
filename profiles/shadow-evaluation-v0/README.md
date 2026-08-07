# C4 Offline Shadow Profile

`native-kernel/c4-offline-shadow-v1` is the bounded C4 evaluation profile authorized by ADR-0020 and Issue #61.

## Inputs

- `contracts/shadow-workload-v1.json` — approved recorded reference/candidate observations;
- an exact `nk-equivalence-report/1` C3 prerequisite report.

## Outputs

- `nk-shadow-report/1` aggregate report;
- 15 `nk-shadow-receipt/1` case Receipts;
- all 72 assertion IDs, with C4 only for the existing 45 C3-supported results.

## Hard boundary

```text
OFFLINE_RECORDED_WORKLOAD
SHADOW_ONLY
AUTHORITY_PROMOTION = FORBIDDEN
AUTHORITATIVE_WRITES = FORBIDDEN
SIDE_EFFECTS = FORBIDDEN
PROMOTION_DECISION = NOT_AUTHORIZED
```

This profile is not live traffic shadowing, C5, production readiness, operational equivalence, truth/authenticity evidence or physical deletion evidence.

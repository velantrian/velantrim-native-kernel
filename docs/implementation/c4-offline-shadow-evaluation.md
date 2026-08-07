# C4 Offline Shadow Evaluation — Implementation Record

## Scope

This record implements ADR-0020 and Issue #61 using a standard-library-only evaluator.

## Dataset

`contracts/shadow-workload-v1.json` contains 15 approved recorded cases across BYTE, STRUCTURAL, SEMANTIC and BEHAVIOURAL classes. The manifest binds the exact dataset bytes by SHA-256.

The cases cover every one of the 45 assertions already supported at C3 exactly once. They contain explicit reference/candidate observations, comparison fields, allowed operational-difference fields and hard proof boundaries.

## Fail-closed gates

- zero critical divergences;
- zero semantic divergence rate;
- zero missing Receipts;
- 100% coverage of C3-supported assertions;
- latency ratios within the declared informational threshold;
- authority promotion, writes and side effects forbidden.

## Receipts

Each case emits an `nk-shadow-receipt/1` record bound to the dataset digest, case ID and comparison digest. A Receipt proves only that the recorded case was compared. It explicitly does not prove truth, external authenticity, physical deletion, production safety or authority.

## Evidence protocol

`nk-shadow-report/1` records:

- exact dataset and C3 prerequisite digests;
- environment and repository metadata;
- thresholds and aggregate metrics;
- all case results and divergences;
- one Receipt per case;
- all 72 assertion IDs;
- C4 only for the 45 inherited supported assertions;
- explicit limitations and no-promotion decision.

## Boundary

```text
repository-reproduced offline shadow
≠ captured production traffic
≠ live shadow deployment
≠ authority promotion
≠ C5
≠ production readiness
```

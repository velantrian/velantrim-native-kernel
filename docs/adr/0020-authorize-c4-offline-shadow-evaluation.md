# ADR-0020 — Authorize C4 Offline Shadow Evaluation

- **Status:** ACCEPTED
- **Operator approval:** APPROVED
- **Date:** 2026-08-07
- **Issue:** #61
- **Base:** `main@b10be105743355a04e58611639a9d28faf7ea514`

## Decision

Authorize C4 only as an offline, authority-free evaluation of approved immutable recorded workloads.

The implementation may compare exact reference and candidate observations, calculate metrics and divergences, and emit bounded Shadow Receipts. It may not append authoritative Events, mutate history, execute side effects, authorize promotion, consume live production traffic or claim C5.

## Required protocol

```text
approved nk-shadow-workload/1 dataset
+ exact nk-equivalence-report/1 C3 prerequisite
→ offline comparison
→ fail-closed gates
→ nk-shadow-receipt/1 per case
→ nk-shadow-report/1
```

## Assertion boundary

C4 applies only to the 45 assertions already `SUPPORTED` at C3. The inherited map remains:

```text
45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED / 0 FAILED
```

No assertion status is promoted by the C4 label itself.

## Non-claims

C4 is not live production shadowing, authority promotion, automatic action approval, operational equivalence, C5, production readiness, truth/authenticity proof, physical deletion evidence, ecosystem integration or historical recovery.

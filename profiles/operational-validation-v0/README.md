# C5 operational validation profile

This directory records the machine-readable C5 rehearsal manifest.

```text
plan: native-kernel/c5-bounded-rehearsal-v1
protocols: nk-operational-plan/1, nk-operational-report/1, nk-operational-receipt/1
runtime conformance inherited: C4
operational evidence target: C5_BOUNDED_REHEARSAL
```

`c5-manifest.json` begins as `PRE_CI`. It may become `PASS` only after exact repository SHA/run/matrix/artifact evidence exists.

The manifest cannot claim production readiness, live data, cloud IAM, physical deletion, compliance certification, operational equivalence, historical recovery or `NK-EPI` acceptance.

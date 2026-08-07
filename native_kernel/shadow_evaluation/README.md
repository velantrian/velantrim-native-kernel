# C4 Offline Shadow Evaluation

This package evaluates an approved immutable recorded-workload dataset without authority promotion, authoritative writes or side effects.

```text
approved recorded observations
+ exact C3 prerequisite report
→ declared field comparison
→ metrics + divergences
→ one bounded Shadow Receipt per case
→ nk-shadow-report/1
```

The evaluator is technology-neutral and standard-library only. It does not call PostgreSQL or SQLite adapters, append Events, mutate authoritative history, execute actions or approve promotion. Profile observations are inputs, not authority.

A passing report keeps the assertion map at `45 SUPPORTED / 10 PARTIAL / 17 UNSUPPORTED`; C4 is attached only to the 45 assertions already supported at C3.

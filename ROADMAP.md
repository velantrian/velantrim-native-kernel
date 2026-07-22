# Roadmap

## Stage 0 — Repository bootstrap

Status: current pull request

- publish explicit research boundary;
- establish Canon / Experimental / Anti-Canon separation;
- document benchmark and integration rules;
- keep the existing prototype outside `main` until exact code and tests are imported reviewably;
- keep license unset until publication terms are decided.

## Stage 1 — Controlled prototype import

Primary goal: import the exact locally tested `v0.1.2.1` snapshot without semantic redesign.

Required artifacts:

1. `kernel.py` or an equivalent package layout;
2. the complete 44-test regression suite;
3. reproducible Python environment metadata;
4. CI for supported Python versions;
5. exact commands and expected results;
6. benchmark script with selective and broad-query workloads;
7. parity review against the architecture and status documents.

Exit gate:

- repository CI reproduces the deterministic test baseline;
- no code is silently rewritten during import;
- any version-label inconsistencies are corrected explicitly;
- status changes to `RUNNABLE RESEARCH PROTOTYPE` only after review.

## v0.1.2.2 — Read-Path Completion

Primary goal: finish the remaining structural performance work without changing the semantic contract.

Planned work:

1. build incoming and outgoing adjacency indexes;
2. eliminate repeated canonical-neighbour event scans;
3. optimize, bound, or redesign greedy ablation;
4. add broad-query benchmark cases activating 80–100% of claims;
5. add performance regression checks that avoid unstable microsecond promises;
6. replace direct SQL test manipulation with controlled clock or test APIs;
7. define candidate-conflict directionality;
8. clarify or implement write-level idempotency.

Exit gate:

- semantic parity with `v0.1.2.1`;
- all existing tests pass;
- broad-query tests and benchmarks are reproducible;
- no claim of universal linear complexity unless demonstrated.

## Offline Shadow

Primary goal: evaluate value without allowing the kernel to affect live Titan or Crystal state.

Design:

- replay approximately 100 recorded Titan queries;
- compare selected context, conflicts, omissions, latency, and receipt quality;
- use a static snapshot;
- prohibit writes into Titan or Crystal truth stores;
- record failure cases and operator judgments.

Offline Shadow does not require compare-and-swap because it has no concurrent live writers.

Exit gate:

- measurable improvement on defined tasks;
- no unacceptable regression in omission, conflict visibility, or latency;
- documented cases where the kernel should not be used.

## v0.1.3 — Event Integrity

Primary goal: make replay and write semantics durable enough for controlled integration experiments.

Planned work:

- full event envelope;
- durable command or idempotency keys;
- actor and schema-version binding;
- complete payload commitment;
- ordering and crash-consistency rules;
- replay verification;
- tamper and truncation tests;
- explicit threat model.

Exit gate:

- deterministic replay from an empty projection store;
- duplicate commands produce defined no-op or replay behaviour;
- corruption and truncation are detected within the stated threat model.

## Live Shadow / dual-write research

This stage is blocked until Event Integrity is complete.

Requirements:

- no authority over production Canon;
- durable ordering;
- write idempotency;
- rollback and divergence detection;
- privacy and deletion semantics;
- operator-visible receipts;
- compare-and-swap only where concurrent writers require it.

## Later research

- full bi-temporal queries;
- directed link contracts;
- conflict lifecycle and human resolution;
- validation-policy plugins;
- evidence integrity and source verification;
- real task-sufficiency evaluation;
- alternative projection adapters;
- storage migration tests;
- multi-writer replication models.

## Promotion rule

```text
research hypothesis
→ reproducible code and tests
→ Offline Shadow evidence
→ explicit decision record
→ bounded integration proposal
→ threat model and rollback
→ separate implementation PR
→ operator approval
```
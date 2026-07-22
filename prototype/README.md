# Prototype Import Plan

> **Status:** `PENDING CONTROLLED IMPORT`  
> **Target snapshot:** `v0.1.2.1`

The existing Python research prototype and its deterministic test suite were verified outside this repository. They must be imported through a dedicated pull request without silent refactoring.

## Required source artifacts

```text
kernel.py
complete test suite (44 tests)
benchmark harness
Python environment metadata
CI workflow
```

## Import invariants

1. Preserve the exact semantic behaviour of the verified snapshot.
2. Do not combine import with read-path redesign.
3. Do not combine import with packaging cleanup beyond what is necessary to run tests.
4. Keep the engine version consistent in code, receipts, tests, and documentation.
5. Record the exact command and environment used to reproduce the test baseline.
6. Mark external benchmark numbers as external until reproduced from the committed code.
7. Keep Native Kernel separate from Titan and Crystal runtime.

## Acceptance checklist

- [ ] Exact source snapshot imported.
- [ ] Exact regression tests imported.
- [ ] `python -m pytest` passes in repository CI.
- [ ] Python 3.11 and 3.12 behaviour is checked.
- [ ] Selective and broad-query benchmark cases are reproducible.
- [ ] `STATUS.md` is updated from `DOCUMENTATION-FIRST` to `RUNNABLE RESEARCH PROTOTYPE` only after evidence exists.
- [ ] No production-ready claim is introduced.

## Deliberately deferred

The import PR must not attempt to solve:

- remaining broad-query superlinearity;
- full write idempotency;
- complete event-envelope integrity;
- multi-writer concurrency;
- full bi-temporal semantics;
- genuine task-sufficiency evaluation.

Those belong to later roadmap stages after the baseline is preserved and reproducible.
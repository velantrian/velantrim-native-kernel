# Prototype Import Plan

> **Status:** `BLOCKED / AUTHENTIC SOURCE NOT LOCATED`  
> **Target snapshot:** reported external `v0.1.2.1`  
> **Repository runtime:** `ABSENT`

The reported Python research prototype and its deterministic 44-test suite were verified outside this repository. The authentic source files and original test suite have not been located in the repository, linked project documentation, or the currently accessible archive sweep.

Do not reconstruct, regenerate, refactor, or approximate an implementation and label it as the validated `v0.1.2.1` snapshot.

See:

- [`docs/ISSUE_1_IMPORT_SPEC.md`](../docs/ISSUE_1_IMPORT_SPEC.md);
- [`docs/ISSUE_1_IMPORT_SPEC.ru.md`](../docs/ISSUE_1_IMPORT_SPEC.ru.md);
- [Issue #1](https://github.com/velantrian/velantrim-native-kernel/issues/1).

## Stage 0.5 — Authentic Source Recovery

The controlled import is blocked until the original source location or immutable archive is identified and its lineage can be recorded.

Allowed work while blocked:

- search known archives, backups, previous environments, old branches, and exports;
- record every searched location and result;
- preserve candidate artifacts read-only;
- prepare manifest, CI, benchmark, and traceability templates without runtime claims.

Prohibited work while blocked:

- rebuilding the implementation from documentation and calling it `v0.1.2.1`;
- replacing the original suite with 44 newly written tests;
- changing repository status to runnable;
- upgrading external benchmark evidence;
- mixing import work with read-path redesign, Event Integrity, Curiosity Core, causality, Titan, or Crystal.

## Required recovered artifacts

```text
authentic source archive or original source location
complete original test suite (reported as 44 tests)
benchmark harness, if present in the original checkpoint
original environment metadata
original commands and expected results
```

## Sealed import layout

Prefer preserving the recovered source separately from repository adapters:

```text
prototype/
├── recovered/
│   └── v0.1.2.1/          # immutable recovered files
├── import_wrapper/         # minimum adapter required to execute
├── manifests/
│   └── v0.1.2.1.json
├── benchmarks/
└── tests/
```

File relocation, line-ending normalization, wrapper code, and every other transformation must be declared in the manifest. Semantic transformations are outside the controlled import.

## Import invariants

1. Preserve the exact semantic behaviour of the authentic snapshot.
2. Keep the recovered source sealed and distinguish it from repository wrappers.
3. Do not combine import with read-path redesign.
4. Do not combine import with packaging cleanup beyond what is necessary to execute the sealed source.
5. Keep the engine version consistent in code, Receipts, tests, and documentation.
6. Record the exact command and environment used to reproduce the historical baseline.
7. Mark external benchmark numbers as external until the relevant workload and timing evidence are reproduced separately.
8. Keep Native Kernel separate from Titan and Crystal runtime.
9. Record source archive hash, per-file source and repository hashes, and every transformation.
10. Preserve and hash the collected test node-ID inventory; numeric test count alone is insufficient.

## Acceptance checklist

### Source recovery

- [ ] Authentic source archive or original location identified.
- [ ] Source lineage documented.
- [ ] Archive preserved read-only and hashed.
- [ ] Original test inventory present.
- [ ] Operator GO recorded.

### Controlled import

- [ ] Sealed exact source snapshot imported.
- [ ] Exact original regression tests imported.
- [ ] Source and repository hashes recorded.
- [ ] Every transformation declared.
- [ ] Test node-ID inventory preserved and hashed.
- [ ] Historical environment reproduced as closely as evidence allows.
- [ ] Exact test command passes.
- [ ] Compatibility behaviour on Python 3.11 and 3.12 is checked separately.
- [ ] Selective and broad-query benchmark workloads are reproducible.
- [ ] Workload evidence and historical timing evidence are reported separately.
- [ ] Contract-to-test traceability matrix is reviewed.
- [ ] `STATUS.md` changes from `DOCUMENTED_ONLY` to `RUNNABLE RESEARCH PROTOTYPE` only after evidence and operator approval.
- [ ] No production-ready claim is introduced.

## Deliberately deferred

The import PR must not attempt to solve:

- remaining broad-query superlinearity;
- full write idempotency;
- complete event-envelope integrity;
- multi-writer concurrency;
- full bi-temporal semantics;
- conflict-resolution lifecycle;
- State Checkpoints;
- Curiosity Core;
- causal relation runtime;
- genuine task-sufficiency evaluation;
- Titan or Crystal runtime integration.

Those belong to later roadmap stages after the authentic baseline is preserved and reproducible.

If authentic recovery ultimately fails, the checkpoint must be recorded as `LOST / NON-REPRODUCIBLE EXTERNAL CHECKPOINT`. Any clean implementation must start under a new version and new evidence lineage.
# Prototype Import Plan

> **Status:** `BLOCKED / AUTHENTIC SOURCE NOT LOCATED`  
> **Target snapshot:** reported external `v0.1.2.1`  
> **Repository Kernel runtime:** `ABSENT`  
> **Accessible-source sweep:** `COMPLETE / NO CANDIDATE BYTES FOUND`

The reported Python research prototype and its deterministic 44-test suite were verified outside this repository. The authentic source files and original test suite have not been located in the repository, connected GitHub repositories, linked Notion records, ChatGPT Library, or current conversation files.

This means `NOT_FOUND_IN_ACCESSIBLE_SOURCES`; it does not yet mean `GLOBALLY LOST`, because operator-controlled local filesystems, backups, IDE history, Git reflogs/stashes, removable media, private repositories, email attachments, and disconnected cloud folders remain outside the connected search scope.

Do not reconstruct, regenerate, refactor, or approximate an implementation and label it as the validated `v0.1.2.1` snapshot.

See:

- [`docs/ISSUE_1_IMPORT_SPEC.md`](../docs/ISSUE_1_IMPORT_SPEC.md);
- [`docs/ISSUE_1_IMPORT_SPEC.ru.md`](../docs/ISSUE_1_IMPORT_SPEC.ru.md);
- [`docs/source-recovery/README.md`](../docs/source-recovery/README.md);
- [`docs/source-recovery/2026-07-26-accessible-sources-sweep.md`](../docs/source-recovery/2026-07-26-accessible-sources-sweep.md);
- [`tools/source_recovery/README.md`](../tools/source_recovery/README.md);
- [Issue #1](https://github.com/velantrian/velantrim-native-kernel/issues/1).

## Stage 0.5 — Authentic Source Recovery

The controlled import is blocked until the original source location or immutable archive is identified and its lineage can be recorded.

Allowed work while blocked:

- search known archives, backups, previous environments, old branches, and exports;
- record every searched location and result;
- preserve candidate artifacts read-only;
- generate and verify an `UNVERIFIED_CANDIDATE` byte manifest;
- prepare CI, benchmark, and traceability templates without Kernel runtime claims.

Prohibited work while blocked:

- rebuilding the implementation from documentation and calling it `v0.1.2.1`;
- replacing the original suite with 44 newly written tests;
- changing repository status to runnable;
- treating source-recovery utility tests as the original Kernel tests;
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

## Candidate handling

When a possible archive is found:

1. preserve the original container read-only;
2. record filename, size, source location, and SHA-256 before extraction;
3. inspect and extract in an isolated environment;
4. reject traversal, symlinks, device files, and unexpected installers;
5. generate an `UNVERIFIED_CANDIDATE` manifest with `tools/source_recovery/generate_manifest.py`;
6. verify byte consistency with `tools/source_recovery/verify_manifest.py`;
7. compare test node IDs, fixtures, version labels, environment, timestamps, and historical references;
8. require an explicit operator provenance decision before `AUTHENTIC_RECOVERED`.

Successful hash verification proves only:

```text
candidate bytes match the recorded candidate manifest
```

It does not prove:

```text
candidate is the historical v0.1.2.1 snapshot
```

## Sealed import layout

Prefer preserving the recovered source separately from repository adapters:

```text
prototype/
├── recovered/
│   └── v0.1.2.1/          # immutable recovered files
├── import_wrapper/         # minimum adapter required to execute
├── manifests/
│   ├── v0.1.2.1.template.json
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
11. Keep source-recovery tooling, Kernel runtime, Kernel regression evidence, and operator authenticity approval as separate scopes.

## Acceptance checklist

### Source recovery

- [x] Connected GitHub, Notion, ChatGPT Library, and current conversation sweep recorded.
- [ ] Operator-controlled local filesystems and backups checked.
- [ ] Authentic source archive or original location identified.
- [ ] Source lineage documented.
- [ ] Original container preserved read-only and hashed.
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

Tracked follow-up contracts:

- [Issue #14 — canonical Claim encoding and identity](https://github.com/velantrian/velantrim-native-kernel/issues/14);
- [Issue #15 — atomic append, idempotency, ordering, and replay](https://github.com/velantrian/velantrim-native-kernel/issues/15);
- [Issue #16 — deletion, restriction, retention, and crypto-erasure](https://github.com/velantrian/velantrim-native-kernel/issues/16);
- [Issue #17 — executable conformance fixture pack](https://github.com/velantrian/velantrim-native-kernel/issues/17);
- [Issue #18 — publication and contribution license terms](https://github.com/velantrian/velantrim-native-kernel/issues/18).

Those belong to later roadmap stages or separate governance decisions after the authentic baseline is preserved and reproducible, or under a clearly new implementation lineage.

If authentic recovery ultimately fails after the declared local and connected-source process, the checkpoint must be recorded through an explicit operator decision as `LOST / NON-REPRODUCIBLE EXTERNAL CHECKPOINT`. Any clean implementation must start under a new version and new evidence lineage.

# Issue #1 Controlled Import Specification

> **Document status:** `PROPOSED / DOCUMENTED`  
> **Decision authority:** operator/maintainer  
> **Target snapshot:** reported external `v0.1.2.1`  
> **Repository state:** `DOCUMENTED_ONLY / NO PUBLIC RUNTIME`  
> **Current execution state:** `BLOCKED BY AUTHENTIC SOURCE RECOVERY`

## 1. Purpose

This document consolidates the executable gate for Issue #1 without changing Native Kernel Architecture Canon.

It distinguishes two stages that must not be collapsed:

```text
Stage 0.5 — authentic source recovery
        ↓ only if provenance is established
Stage 1 — exact controlled import
```

The reported `v0.1.2.1` implementation and original 44-test suite are external evidence. They are not present in `main`, and the currently accessible project sources have not yielded an authentic source archive.

No approximation, clean-room reconstruction, regenerated test suite, refactor, or semantic redesign may be labelled as the validated `v0.1.2.1` snapshot.

## 2. Stage 0.5 — Authentic Source Recovery

### 2.1 Goal

Identify the original source location or immutable archive for the externally reported `v0.1.2.1` checkpoint and its original 44-test suite.

### 2.2 Allowed work while blocked

- search known local archives, backups, exported workspaces, old branches, removable media, and prior development environments;
- record every searched location and result;
- prepare manifest, CI, and validation templates without making runtime claims;
- inventory documentation-derived expectations as expectations, not recovered source;
- preserve all candidate artifacts read-only until provenance review.

### 2.3 Prohibited work while blocked

- reconstructing an implementation from documentation and naming it `v0.1.2.1`;
- creating 44 replacement tests and presenting them as the original suite;
- upgrading any external evidence to repository evidence;
- changing `STATUS.md` to `RUNNABLE RESEARCH PROTOTYPE`;
- treating matching behaviour as proof of source authenticity;
- mixing source recovery with Curiosity Core, causality, Event Integrity, Titan, Crystal, or read-path redesign.

### 2.4 Recovery record

Every search pass should record:

```yaml
search_id: NK-SRC-RECOVERY-YYYYMMDD-NNN
performed_at: YYYY-MM-DDTHH:MM:SSZ
performed_by: operator-or-reviewer
locations_checked:
  - location: description
    access_mode: read-only
    result: found | not_found | inaccessible
candidate_artifacts:
  - path_or_reference: value
    size_bytes: 0
    sha256: value
    status: unverified_candidate
notes: free text
```

### 2.5 Stage 0.5 exit gate

Stage 1 may begin only when all conditions are met:

- [ ] an authentic source archive or original source location is identified;
- [ ] the source lineage is documented;
- [ ] the archive is preserved read-only;
- [ ] an archive-level SHA-256 is recorded;
- [ ] the original test inventory is present and inspectable;
- [ ] the operator explicitly authorizes controlled import.

If the source cannot be recovered after the declared recovery process, the project must record `v0.1.2.1` as `LOST / NON-REPRODUCIBLE EXTERNAL CHECKPOINT` and start a separately versioned clean implementation. That implementation must not inherit the old evidence state.

## 3. Stage 1 — Exact Controlled Import

### 3.1 Scope

The import PR must contain:

1. the sealed authentic source snapshot;
2. the complete original test suite;
3. the original or faithfully reconstructed execution environment metadata;
4. a cryptographic provenance manifest;
5. a minimal repository wrapper required to run the sealed source;
6. CI compatibility checks;
7. a benchmark workload harness with stable benchmark IDs;
8. a contract-to-test traceability review.

### 3.2 Deliberately deferred

The import PR must not implement or redesign:

- broad-query optimization;
- full write idempotency;
- Event Integrity;
- multi-writer concurrency;
- full bi-temporal semantics;
- conflict-resolution lifecycle;
- State Checkpoints;
- Curiosity Core;
- causal relation runtime;
- Titan or Crystal runtime integration;
- production security, privacy, or availability claims.

## 4. Repository layout

The exact source should remain sealed and distinguishable from repository adapters:

```text
prototype/
├── recovered/
│   └── v0.1.2.1/          # immutable recovered files
├── import_wrapper/         # minimal adapter; no semantic redesign
├── manifests/
│   └── v0.1.2.1.json
├── benchmarks/
└── tests/                  # original tests or an exact preserved layout
```

Moving or renaming files is not automatically harmless. Every transformation must be declared. Prefer preserving original paths inside `prototype/recovered/v0.1.2.1/` and adapting around them.

## 5. Provenance manifest

A hash of repository files alone does not prove source authenticity. The manifest must bind the recovered archive, source files, repository files, transformations, test inventory, environment, and import commit.

Minimum schema:

```json
{
  "manifest_version": "1.1",
  "snapshot_id": "v0.1.2.1",
  "snapshot_status": "AUTHENTIC_RECOVERED",
  "source_archive": {
    "filename": "<archive-name>",
    "sha256": "<archive-sha256>",
    "size_bytes": 0,
    "recovered_from": "<location-description>",
    "recovered_at": "YYYY-MM-DDTHH:MM:SSZ",
    "recovered_by": "<operator-or-reviewer>"
  },
  "files": [
    {
      "original_path": "kernel.py",
      "repository_path": "prototype/recovered/v0.1.2.1/kernel.py",
      "source_sha256": "<sha256>",
      "repository_sha256": "<sha256>",
      "size_bytes": 0,
      "role": "runtime",
      "transformation": "NONE"
    }
  ],
  "test_inventory": {
    "declared_count": 44,
    "collected_count": 44,
    "node_ids_sha256": "<sha256-of-normalized-test-node-id-list>"
  },
  "environment": {
    "original_python": "<version>",
    "dependency_lock_sha256": "<sha256>",
    "original_test_command": "<command>"
  },
  "repository": {
    "import_pr": "<number>",
    "import_commit": "<sha>"
  }
}
```

Allowed transformation values must be explicit and narrow, for example:

```text
NONE
LINE_ENDING_NORMALIZATION
PATH_RELOCATION_ONLY
REPOSITORY_WRAPPER_ONLY
```

Any transformation that changes imports, data representation, ordering, defaults, event meaning, identity, reduction, or output is not a pure import and requires separate review.

## 6. Test fidelity

`declared_test_count: 44` is insufficient by itself.

The import must preserve:

- the original test files;
- collected test node IDs;
- parameterization identity;
- fixtures and data files;
- expected failures and skips;
- original test command and environment assumptions.

The normalized output of `pytest --collect-only -q` or the equivalent original runner must be stored or hashed. A new suite with the same numeric count is not equivalent to the original suite.

## 7. CI and reproducibility

Use two distinct layers.

### 7.1 Historical reproduction environment

Reproduce the authentic snapshot in the closest recoverable original environment. Pin:

- exact Python patch version where known;
- dependency lock or hashes;
- OS/container identity;
- locale, timezone, and relevant environment variables;
- deterministic seeds;
- exact command.

### 7.2 Compatibility CI

After historical reproduction succeeds, test compatibility on Python 3.11 and 3.12.

Prefer a fixed runner such as `ubuntu-24.04` over a floating `ubuntu-latest`. For stronger reproducibility, use a container image pinned by digest.

Compatibility failure does not invalidate the historical checkpoint. It creates a separately reviewed compatibility task.

## 8. Benchmark evidence

Benchmark evidence has separate dimensions:

```text
workload reproduced
≠ historical number reproduced
≠ scaling shape observed
≠ production capacity validated
```

Recommended fields:

```yaml
benchmark_id: NK-BM-V0121-SELECTIVE-001
workload_evidence: REPOSITORY_REPRODUCED
historical_timing_evidence: EXTERNALLY_OBSERVED
scaling_shape_evidence: REPOSITORY_OBSERVED
production_capacity: NOT_EVALUATED
```

A GitHub-hosted runner may reproduce workload semantics and reveal regressions, but it does not automatically reproduce historical absolute timings because CPU allocation and contention are not stable.

Every result must record:

- benchmark ID;
- source snapshot hash;
- repository commit;
- Python and dependency identity;
- OS and CPU metadata;
- seed;
- corpus parameters;
- warm-up policy;
- repetitions;
- median and p95;
- separate construction and query timings;
- timestamp.

## 9. Contract-to-test traceability

A prose-only or line-by-line architecture review is insufficient. The import PR must include a traceability matrix:

| Contract assertion | Test ID | Runtime symbol/path | Result | Known limit |
|---|---|---|---|---|
| Claims are immutable semantic records | `<test-id>` | `<symbol>` | pass/fail | `<limit>` |
| Replay reconstructs declared state | `<test-id>` | `<symbol>` | pass/fail | `<limit>` |
| Candidate conflict is not canonical conflict | `<test-id>` | `<symbol>` | pass/fail | `<limit>` |
| Selection relevance is not truth evidence | `<test-id>` | `<symbol>` | pass/fail | `<limit>` |

The matrix documents what the imported snapshot actually demonstrates. Missing rows remain explicit gaps.

## 10. Conformance and status gate

A successful import may support **C2 — Repository reproduced** only for explicitly tested contract assertions. It does not establish:

- cross-profile equivalence;
- Shadow task value;
- operational security;
- production readiness;
- universal technology independence.

`STATUS.md` may change to `RUNNABLE RESEARCH PROTOTYPE` only after:

- authentic provenance is accepted;
- the original tests are reproduced;
- CI and traceability review pass;
- benchmark claims are correctly scoped;
- an independent review is completed;
- the operator records approval.

## 11. Contract-hardening backlog outside Issue #1

The following gaps are important but remain separate from the controlled import:

1. canonical Claim encoding, Unicode normalization, hash domain/version, and identity migration rules;
2. command validation, durable idempotency, atomic append, ordering, crash recovery, schema upcasting, and deterministic replay;
3. deletion and restriction semantics for payloads, projections, embeddings, exports, Receipts, and backups;
4. executable schemas, golden vectors, invalid-event corpora, expected reducer outputs, and cross-profile conformance runners;
5. clear separation of decision status, empirical evidence, implementation status, and operator approval.

These items should be addressed through separately scoped contracts, ADRs, tests, and PRs. They must not be silently implemented during source import.

## 12. Definition of Done

### Source recovery

- [ ] authentic source archive identified;
- [ ] source lineage recorded;
- [ ] archive SHA-256 recorded;
- [ ] original test inventory identified;
- [ ] operator GO recorded.

### Source fidelity

- [ ] sealed snapshot imported without semantic rewrite;
- [ ] transformations explicitly declared;
- [ ] source and repository file hashes recorded;
- [ ] original test inventory preserved and hashed;
- [ ] version labels agree across source, tests, Receipts, and docs.

### Reproducibility

- [ ] original environment reconstructed as closely as evidence allows;
- [ ] exact test command succeeds;
- [ ] compatibility CI covers Python 3.11 and 3.12;
- [ ] environment and dependency identities are recorded.

### Benchmarks

- [ ] stable benchmark IDs are emitted;
- [ ] selective and broad workloads remain separate;
- [ ] workload evidence and timing evidence are reported separately;
- [ ] complete metadata, median, and p95 are recorded.

### Governance

- [ ] no production claim is introduced;
- [ ] no Titan or Crystal dependency is introduced;
- [ ] no post-baseline redesign is mixed into the import;
- [ ] contract-to-test traceability is reviewed;
- [ ] `STATUS.md` changes only after evidence and operator approval.

## 13. ADR rule

No new ADR is required for a byte-faithful import that only executes the already documented gate.

A new or updated ADR is required if the PR changes public contract meaning, event vocabulary, Claim identity, replay semantics, deletion semantics, conflict semantics, project boundaries, or a long-lived implementation-profile commitment.

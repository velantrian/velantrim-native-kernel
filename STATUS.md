# Current Status

> **Date:** 2026-07-26  
> **Reported external prototype track:** `v0.1.2.1`  
> **Repository status:** `RESEARCH / DOCUMENTED_ONLY / NOT PRODUCTION-READY`  
> **Issue #1 state:** `BLOCKED BY AUTHENTIC SOURCE RECOVERY`

## Project identity

Velantrim Native Kernel is an independent, personal, long-horizon architecture research project.

It is separate from the Crystal grant-facing product track. It may study or reuse ideas from Titan, Crystal, academic work, and external systems, but it follows its own architecture and evidence gates.

The project is architecture-first: it describes durable semantic and epistemic contracts while using modern technologies as replaceable implementation profiles and research instruments.

See [`docs/LONG_HORIZON_VISION.md`](./docs/LONG_HORIZON_VISION.md).

## Reading rule

This file is the current implementation boundary for this repository. Architectural documents may describe future mechanisms or future computational substrates, but only code and tests present in the repository count as implemented.

The following distinctions are mandatory:

```text
architecture Canon
≠ abstract contract
≠ implementation profile
≠ implemented runtime
≠ empirical evidence
≠ operator approval
≠ production evidence
```

## Current public repository state

The repository currently contains the research specification and governance boundary. No runnable Native Kernel implementation or repository test suite is present in `main`.

A local research checkpoint identified as `v0.1.2.1` was previously reported to have passed 44 deterministic tests. The authentic source files, original test suite, source archive, complete environment, and benchmark harness have not been located in the repository, linked project documentation, or the currently accessible archive sweep.

Therefore the public repository may currently claim:

- a documented Native Kernel architecture;
- an independent long-horizon research vision;
- a separation between Architecture Canon, Abstract Contracts, and Implementation Profiles;
- an explicit Canon / Experimental / Anti-Canon separation;
- a staged roadmap;
- benchmark methodology and stable record identifiers;
- Titan and Crystal integration boundaries;
- a blocked controlled-import process with an explicit source-recovery gate;
- current technologies as candidate laboratory adapters rather than permanent architecture;
- a proposed, documentation-only Curiosity Core research RFC with explicit authority and safety boundaries;
- an accepted, documentation-only decision that future causality belongs on typed directed relations rather than `knowledge_type` or lineage.

It must not yet claim:

- a runnable public kernel implementation;
- public reproduction of the 44-test result;
- authenticity or availability of the reported `v0.1.2.1` source snapshot;
- that a reconstructed implementation is the validated snapshot;
- production-ready event sourcing;
- complete write idempotency;
- full Event Integrity;
- multi-writer safety;
- universal linear-time context selection;
- genuine task sufficiency;
- production security or privacy;
- demonstrated portability across arbitrary hardware or future computational substrates;
- superiority of non-binary, neuromorphic, photonic, or other speculative execution models;
- that SQLite, graph, vector retrieval, LLMs, or conventional processors are rejected;
- an implemented Curiosity Core runtime;
- accepted curiosity event verbs;
- an implemented causal relation, causal read model, or `CausalContextBuilder`;
- autonomous self-modification, autonomous truth promotion, or live Titan/Crystal curiosity integration.

## Issue #1 source-recovery blocker

The controlled `v0.1.2.1` import is blocked.

Do not reconstruct, regenerate, refactor, or approximate an implementation and label it as the validated snapshot. Matching behaviour, matching terminology, or a replacement suite with 44 tests does not prove source authenticity.

The import may begin only after:

1. an authentic source archive or original source location is identified;
2. source lineage is documented;
3. the archive is preserved read-only and hashed;
4. the original test inventory is present;
5. the operator records explicit GO.

See:

- [`docs/ISSUE_1_IMPORT_SPEC.md`](./docs/ISSUE_1_IMPORT_SPEC.md);
- [`docs/ISSUE_1_IMPORT_SPEC.ru.md`](./docs/ISSUE_1_IMPORT_SPEC.ru.md);
- [`prototype/README.md`](./prototype/README.md);
- [Issue #1](https://github.com/velantrian/velantrim-native-kernel/issues/1).

If authentic recovery ultimately fails, `v0.1.2.1` must be recorded as `LOST / NON-REPRODUCIBLE EXTERNAL CHECKPOINT`. A clean implementation must use a new version and evidence lineage.

## Curiosity Core research track

**Status:** `PROPOSED / DOCUMENTED_ONLY / NOT IMPLEMENTED / OUTSIDE ISSUE #1`

Curiosity Core is documented as an optional, non-authoritative active-investigation module. It may detect meaningful unknowns, prioritize bounded investigation, form questions and competing hypotheses, and create falsifiable System Insights.

Mandatory current boundaries:

- no direct Canon or Epistemic State mutation;
- no new curiosity event verbs in the controlled import;
- operational Event Admission, external Action Gate, and epistemic TruthGate remain distinct;
- attention, novelty, utility, and repeated use are not truth evidence;
- temporal decay may affect attention or dormancy, not evidence-derived truth confidence;
- adaptive policies remain Shadow-only until explicit operator approval;
- Titan is a possible future evaluation host, not a parent runtime or current dependency;
- Crystal may only consider a separate restricted Audit Curiosity profile;
- no runtime, benchmark, safety, or production claim is made.

See:

- [`docs/rfc/0001-curiosity-core-architecture.md`](./docs/rfc/0001-curiosity-core-architecture.md);
- [`docs/rfc/0001-curiosity-core-architecture.ru.md`](./docs/rfc/0001-curiosity-core-architecture.ru.md);
- [`docs/adr/0005-curiosity-core-is-optional-and-non-authoritative.md`](./docs/adr/0005-curiosity-core-is-optional-and-non-authoritative.md).

## Existing external prototype checkpoint

The reported external checkpoint remains:

```text
v0.1.2.1
44 deterministic tests
source and original suite not currently located
```

This is historical external evidence only. It cannot become repository evidence until authentic provenance, exact code, exact tests, environment, commands, and reviewable artifacts exist.

## Current implementation profile

The intended near-term laboratory profile may use:

- Python;
- SQLite or append-only files;
- FTS or lexical retrieval;
- graph adapters;
- vector or hybrid retrieval adapters;
- local or remote model adapters;
- conventional CPU/GPU execution.

These choices are implementation candidates. They do not redefine the Architecture Canon.

## Known architectural limitations

### Claim identity and canonical encoding

Stable semantic identity is an architectural requirement, but the repository does not yet define normative canonical bytes, Unicode normalization, hash domain/version separation, collision handling, or identity migration rules. These belong to a separate contract and test suite, not the controlled import.

### Broad-query scaling

The reported external checkpoint described event indexing and charge caching improvements, but broad queries remained superlinear because neighbour discovery and greedy ablation contained repeated work. This remains external, unreproduced evidence.

### Write idempotency

Read-time deduplication is not equivalent to durable command idempotency. Duplicate writes require an explicit command and event-level contract.

### Evidence integrity

A non-empty evidence string is only a hygiene condition. It is not source verification, cryptographic evidence, or proof of truth.

### Event-envelope and append integrity

A future event envelope must bind ordering, actor, timestamp, schema version, idempotency key, payload commitment, and previous hash under an explicit threat model.

The full command path remains undefined and unimplemented:

```text
command validation
→ durable idempotency
→ atomic append
→ ordering
→ crash recovery
→ schema upcast
→ deterministic replay
```

### Conflict semantics

Candidate and canonical conflicts are separated conceptually, but directionality, admission, resolution, and lifecycle policy remain research work.

### Context selection

The reported prototype used lexical proxy ablation. It must not be described as proven sufficient or globally minimal evidence selection.

### Legal erasure and restriction

The `ERASED` event concept does not by itself define deletion or restriction for source payloads, projections, vector indexes, exports, Receipts, Shadow datasets, or backups. A separate deletion/crypto-erasure contract and threat model are required.

### Executable conformance

The C0–C5 model is a documentation contract. Executable schemas, golden vectors, invalid-event corpora, expected reducer outputs, and cross-profile runners are not yet present.

### Curiosity evaluation

No trigger, scoring adapter, Attention Allocator, Investigation Runtime, Hypothesis Set, SystemInsight, calibration loop, or Safety and Resource Guard has been implemented or evaluated. Proposed formulas and event vocabulary remain research inputs only.

### Causal semantics

ADR-0006 accepts causal relations as the future abstract placement for causality. No public runtime, directed-link contract, causal event vocabulary, query implementation, or repository test exists yet. The reported external `CAUSES` link remains external evidence until authentic source is recovered and reproduced.

### Technology portability

Technology independence is currently an architectural target. It has not yet been demonstrated across multiple storage engines, runtimes, processors, or future computational substrates.

## Next repository gate

The immediate gate is **Stage 0.5 — Authentic Source Recovery**, not implementation work.

Only after Stage 0.5 succeeds may a dedicated import PR establish:

1. a sealed authentic source snapshot;
2. archive-level and per-file provenance hashes;
3. preserved and hashed original test inventory;
4. historical reproduction environment;
5. exact test command;
6. compatibility CI on Python 3.11 and 3.12;
7. benchmark workload reproduction with separate timing evidence;
8. contract-to-test traceability;
9. no unsupported production claims.

The long-horizon architecture track may continue only as bounded, clearly labelled documentation. It must not alter or simulate the missing import baseline.

Only after authentic import, independent review, evidence, and operator approval may this status change from `DOCUMENTED_ONLY` to `RUNNABLE RESEARCH PROTOTYPE`.
# Roadmap

Velantrim Native Kernel has two parallel research tracks:

```text
Track A — executable validation
source recovery → exact import → tests → read path → Offline Shadow → Event Integrity

Track B — long-horizon architecture
Canon → abstract contracts → implementation profiles → executable conformance → portability evidence
```

Track B is independent of the Crystal grant roadmap. It may continue as bounded documentation and isolated experiments while Track A preserves strict implementation evidence.

Architecture research and executable implementation may progress at different speeds, but their statuses must never be collapsed.

## Stage 0 — Repository bootstrap

**Status:** `COMPLETE IN MAIN / DOCUMENTATION CONTINUES`

- publish explicit research boundary;
- establish Canon / Experimental / Anti-Canon separation;
- document benchmark and integration rules;
- keep unverified runtime artifacts outside `main`;
- keep license unset until publication terms are decided;
- establish Native Kernel as an independent, personal, long-horizon research project.

## Stage 0.5 — Authentic Source Recovery

**Status:** `BLOCKED / ACTIVE EVIDENCE-RECOVERY GATE`

Primary goal: identify the authentic source archive or original location for the reported external `v0.1.2.1` checkpoint and original 44-test suite.

Current facts:

- no runnable kernel implementation exists in `main`;
- the authentic source and original test suite have not been located in the currently accessible GitHub, Notion, or project archive sweep;
- documentation-derived reconstruction is not source recovery;
- matching behaviour or matching test count is not provenance.

Allowed work:

1. search known archives, backups, previous environments, old branches, and exports;
2. record every location checked and its result;
3. preserve candidate artifacts read-only;
4. prepare provenance-manifest, CI, benchmark, and traceability templates without runtime claims.

Prohibited work:

1. reconstruct an approximation and label it `v0.1.2.1`;
2. replace the original suite with newly written tests;
3. upgrade external evidence to repository evidence;
4. change status to `RUNNABLE RESEARCH PROTOTYPE`;
5. mix source recovery with architecture redesign or Titan/Crystal integration.

Exit gate:

- authentic source archive or original location identified;
- lineage documented;
- archive preserved and hashed;
- original test inventory present;
- operator GO recorded.

Failure branch:

```text
authentic source recovered
→ Stage 1 exact controlled import

authentic source not recoverable after declared search
→ record v0.1.2.1 as LOST / NON-REPRODUCIBLE EXTERNAL CHECKPOINT
→ begin a new clean implementation under a new version and evidence lineage
```

See [`docs/ISSUE_1_IMPORT_SPEC.md`](./docs/ISSUE_1_IMPORT_SPEC.md) and [`docs/ISSUE_1_IMPORT_SPEC.ru.md`](./docs/ISSUE_1_IMPORT_SPEC.ru.md).

## Stage 1 — Controlled prototype import

**Status:** `BLOCKED BY STAGE 0.5`

Primary goal: import the exact authentic `v0.1.2.1` snapshot without semantic redesign.

Required artifacts:

1. sealed recovered source snapshot;
2. complete original 44-test regression suite;
3. archive-level and per-file provenance manifest;
4. preserved and hashed test node-ID inventory;
5. historical reproduction environment metadata;
6. exact commands and expected results;
7. minimal repository wrapper, declared separately from recovered source;
8. compatibility CI for Python 3.11 and 3.12;
9. benchmark harness with stable IDs and separate workload/timing evidence;
10. contract-to-test traceability matrix.

Import invariants:

- no silent semantic rewrite;
- no read-path redesign;
- no packaging cleanup beyond a declared minimal wrapper;
- every transformation recorded;
- source and repository hashes both recorded;
- no Titan or Crystal runtime dependency;
- no Curiosity Core, causality, Event Integrity, checkpoint, conflict-lifecycle, or other post-baseline redesign;
- no production claim.

Exit gate:

- authentic provenance accepted;
- original test inventory reproduced;
- exact historical command succeeds in the closest recoverable environment;
- Python 3.11 and 3.12 compatibility is checked separately;
- benchmark workloads are reproducible and claims remain correctly scoped;
- traceability review is complete;
- independent review is complete;
- operator approval is recorded;
- status changes to `RUNNABLE RESEARCH PROTOTYPE` only after all evidence exists.

Long-horizon documentation may evolve during this stage, but it must not alter the imported semantic baseline.

## v0.1.2.2 — Read-Path Completion

**Blocked by:** successful Stage 1 import.

Primary goal: finish remaining structural performance work without changing the semantic contract.

Planned work:

1. build incoming and outgoing adjacency indexes;
2. eliminate repeated canonical-neighbour event scans;
3. optimize, bound, or redesign greedy ablation;
4. add broad-query cases activating 80–100% of Claims;
5. add performance regression checks without unstable microsecond promises;
6. replace direct SQL test manipulation with controlled clock or test APIs;
7. define candidate-conflict directionality;
8. clarify or implement durable write-level idempotency.

Exit gate:

- semantic parity with the imported baseline;
- all baseline tests pass;
- broad-query tests and benchmarks are reproducible;
- workload evidence, timing evidence, and scaling claims remain separate;
- no universal linear-complexity claim unless demonstrated.

## Offline Shadow

**Blocked by:** v0.1.2.2 Read-Path Completion.

Primary goal: evaluate value without allowing the Kernel to affect live Titan or Crystal state.

Design:

- replay approximately 100 recorded Titan queries;
- compare selected context, conflicts, omissions, latency, and Receipt quality;
- use a static, privacy-reviewed snapshot;
- prohibit writes into Titan or Crystal truth stores;
- record failure cases and operator judgments;
- define deletion and retention rules for the Shadow dataset.

Offline Shadow does not require compare-and-swap because it has no concurrent live writers.

Exit gate:

- measurable improvement on defined tasks;
- no unacceptable regression in omission, conflict visibility, privacy, or latency;
- documented cases where the Kernel should not be used;
- reproducible Receipts and evaluation artifacts.

## v0.1.3 — Event Integrity

**Blocked by:** Offline Shadow evidence and separately approved contract work.

Primary goal: make replay and write semantics durable enough for controlled integration experiments.

Required command path:

```text
command validation
→ durable idempotency
→ atomic append
→ deterministic ordering
→ crash recovery
→ schema upcast
→ deterministic replay
```

Planned work:

- complete event envelope;
- durable command/idempotency keys;
- actor and schema-version binding;
- complete payload commitment;
- ordering and crash-consistency rules;
- replay verification;
- tamper and truncation tests;
- explicit threat model;
- declared multi-writer model or explicit single-writer boundary.

Exit gate:

- deterministic replay from an empty projection store;
- duplicate commands produce defined no-op or replay behaviour;
- corruption and truncation are detected within the stated threat model;
- crash boundaries and ordering semantics are tested.

## Live Shadow / dual-write research

**Status:** `BLOCKED UNTIL EVENT INTEGRITY`

Requirements:

- no authority over production Canon;
- durable ordering;
- write idempotency;
- rollback and divergence detection;
- privacy and deletion semantics;
- operator-visible Receipts;
- compare-and-swap only where concurrent writers require it;
- explicit disablement and incident procedure.

## Long-horizon architecture track

This track develops a technology-independent blueprint rather than a commitment to a specific 2026 stack.

### A. Abstract contract map

Define explicit contracts for:

- semantic identity and canonical encoding;
- authoritative storage and history;
- command admission and atomic append;
- deterministic reduction and schema evolution;
- disposable projection and rebuild;
- retrieval and activation;
- conflict visibility and resolution boundaries;
- audit and Receipt;
- deletion, restriction, retention, and migration;
- neutral interchange and portability.

### B. Implementation profiles

Document profiles rather than hard-code one permanent stack.

Current laboratory candidates include Python, SQLite or append-only files, lexical/FTS retrieval, graph adapters, vector or hybrid adapters, model adapters, and conventional CPU/GPU execution.

Future profiles may explore different runtimes, memory media, representations, or computational substrates. No profile becomes Canon by implementation convenience.

### C. Executable conformance

Turn the C0–C5 documentation model into reviewable artifacts:

- normative schemas;
- canonical encoding vectors where byte identity is required;
- golden event histories;
- invalid-event corpora;
- expected reducer outputs;
- projection deletion/rebuild vectors;
- conflict and temporal fixtures;
- cross-profile comparison runner;
- machine-readable evidence records.

### D. Portability evaluation

Candidate evidence:

- replay the same authoritative history through multiple storage adapters;
- rebuild projections from zero;
- compare identity, lineage, temporal meaning, conflicts, policy results, and Receipts;
- verify that adapter replacement does not require Canon redesign;
- document semantic differences rather than hiding them;
- define neutral export and import forms.

### E. Future substrate research

Possible directions include neuromorphic, photonic, analog, probabilistic, non-binary, or other future systems.

These remain research possibilities. No roadmap item may claim availability, superiority, or compatibility without implementation evidence.

### F. Contract-hardening backlog

The following are P1 architecture contracts but remain outside Issue #1:

1. canonical Claim bytes, Unicode normalization, hash domain/version, collision handling, and identity migration;
2. complete command-to-replay integrity contract;
3. legal erasure, crypto-erasure, restriction, retention, and backup semantics;
4. executable conformance fixtures and runners;
5. four independent governance dimensions: decision, evidence, implementation, and operator approval.

Each requires separately scoped contracts, ADRs where applicable, tests, and PRs.

### G. Optional bio-inspired / Kitara research

**Status:** `PROPOSED / EXPERIMENTAL / NOT IMPLEMENTED / OUTSIDE ISSUE #1 / SCOPE-FROZEN`

Candidate patterns include peripheral event processing, adaptive gain, procedural memory, sensorimotor loops, distributed adaptation, Physarum-like routing, and multimodal sensor fusion.

Hard boundaries:

- routing, salience, gain, and repeated use do not determine truth;
- biological metaphors do not become architectural evidence;
- physical sensors and actuators remain outside Native Kernel Canon;
- Kitara remains a possible separate future research system;
- no mechanism enters runtime through documentation alone;
- no implementation work begins before Stage 1 evidence exists.

See `docs/research/BIO_INSPIRED_COMPUTATION_AND_KITARA.md` and `docs/research/PHYSARUM_ROUTING_EXPERIMENT.md`.

### H. Optional Curiosity Core research

**Status:** `PROPOSED / DOCUMENTED_ONLY / NOT IMPLEMENTED / OUTSIDE ISSUE #1 / SCOPE-FROZEN`

Curiosity Core studies a bounded active-investigation layer above Native Kernel contracts. It is not a truth authority and is not required for Kernel replay or integrity.

```text
Native Kernel
→ preserves Claims, history, state, and Receipts

Curiosity Core
→ decides which unknown deserves bounded investigation

Action Gate
→ controls tools and external actions

TruthGate
→ controls epistemic promotion
```

Hard boundaries:

- no direct Canon or Epistemic State mutation;
- operational Event Admission, Action Gate, and TruthGate remain distinct;
- attention, novelty, utility, and repeated use are not evidence;
- temporal decay affects attention or dormancy, not truth confidence;
- System Insights do not modify code, policies, or architecture automatically;
- every investigation requires budget, stopping, suspension, and reopen conditions;
- adaptive policies begin in Shadow and require operator approval;
- Titan is only a possible future evaluation host;
- Crystal may only consider a separate restricted Audit Curiosity profile;
- no proposed event verb enters the controlled import;
- no implementation work begins before Stage 1 evidence exists.

See `docs/rfc/0001-curiosity-core-architecture.md`, its Russian translation, and ADR-0005.

## Later research

- full bi-temporal queries;
- directed-link contracts;
- typed causal relations after directed-link and temporal prerequisites;
- causal read models and bounded `CausalContextBuilder` profiles;
- conflict lifecycle and human resolution;
- validation-policy plugins;
- evidence integrity and source verification;
- real task-sufficiency evaluation;
- alternative projection adapters;
- storage migration tests;
- multi-writer replication models;
- snapshot policy if replay cost justifies it;
- bounded bio-inspired routing experiments;
- passive Curiosity Core Shadow evaluation after controlled import;
- restricted Crystal Audit Curiosity only through a separate Crystal RFC.

Causal research ordering is explicit:

```text
directed-link contract
→ temporal semantics required by causal payload
→ typed CAUSES relation contract tests
→ rebuildable causal read model
→ bounded Titan profile, if separately approved
```

ADR-0006 accepts where causality belongs. It does not claim the relation, event vocabulary, query runtime, or Titan integration is implemented.

## Promotion rule

```text
research hypothesis
→ explicit contract
→ reproducible code and tests
→ failure cases
→ Offline Shadow evidence where applicable
→ explicit decision record
→ bounded integration proposal
→ threat model, deletion, and rollback
→ separate implementation PR
→ operator approval
```

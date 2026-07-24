# Roadmap

Velantrim Native Kernel has two parallel research tracks:

```text
Track A — executable validation
exact import → tests → read path → Shadow → Event Integrity

Track B — long-horizon architecture
Canon → abstract contracts → implementation profiles → portability evidence
```

Track B is independent of the Crystal grant roadmap. It may continue as documentation and bounded experiments while Track A preserves strict implementation evidence.

## Stage 0 — Repository bootstrap

Status: complete in `main`; documentation refinement continues.

- publish explicit research boundary;
- establish Canon / Experimental / Anti-Canon separation;
- document benchmark and integration rules;
- keep the existing prototype outside `main` until exact code and tests are imported reviewably;
- keep license unset until publication terms are decided;
- establish Native Kernel as an independent, personal, long-horizon research project.

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

Long-horizon documentation may evolve during this stage, but it must not alter the imported semantic baseline.

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

## Long-horizon architecture track

This track develops the architecture as a technology-independent blueprint rather than a commitment to a specific 2026 implementation stack.

### A. Abstract contract map

Define explicit contracts for:

- storage and authoritative history;
- projection and rebuild;
- retrieval and activation;
- compute and reduction;
- admission and policy;
- audit and Receipt;
- migration and interchange.

### B. Implementation profiles

Document profiles rather than hard-code one permanent stack.

Initial profile candidates:

```text
Python
SQLite / append-only files
FTS / lexical retrieval
Graph adapters
Vector / hybrid retrieval
LLM adapters
Conventional CPU / GPU
```

Future profiles may explore different runtimes, memory media, representations, or computational substrates.

### C. Portability evaluation

Candidate evidence:

- replay the same authoritative history through multiple storage adapters;
- rebuild projections from zero;
- compare semantic state, lineage, temporal meaning, conflicts, and Receipts;
- verify that adapter replacement does not require Canon redesign;
- document semantic differences rather than hiding them;
- define neutral export and import forms.

### D. Future substrate research

Possible research directions include neuromorphic, photonic, analog, probabilistic, non-binary, or other future systems.

These remain research possibilities. No roadmap item may claim that a future substrate is available, superior, or compatible without implementation evidence.

### E. Architecture promotion gate

```text
research hypothesis
→ abstract contract
→ bounded implementation profile
→ tests and failure cases
→ cross-profile comparison
→ explicit decision record
→ operator approval
```

### F. Optional bio-inspired / Kitara research

**Status:** `PROPOSED / EXPERIMENTAL / NOT IMPLEMENTED / OUTSIDE ISSUE #1`

This optional branch records patterns extracted from an external Grok audit and design discussion. It does not change Native Kernel Canon and does not claim scientific proof or runtime support.

Candidate patterns:

```text
peripheral event processing
adaptive gain
procedural / motor memory
sensorimotor loops
distributed network adaptation
Physarum-like routing
multimodal sensor fusion
```

Hard boundaries:

- routing, salience, gain, and repeated use do not determine truth;
- biological metaphors do not become architectural evidence;
- physical sensors and actuators remain outside Native Kernel Canon;
- Kitara remains a possible separate future research system;
- no mechanism enters runtime through documentation alone;
- the controlled prototype import remains unchanged.

Initial experiment order:

1. Physarum-like routing on a seeded synthetic Claim graph;
2. adaptive gain versus fixed ranking;
3. peripheral filtering on recorded sensor data;
4. procedural-memory representation;
5. multimodal fusion;
6. embodied sensorimotor loops only after safety and authorization design.

See:

- `docs/research/BIO_INSPIRED_COMPUTATION_AND_KITARA.md`;
- `docs/research/PHYSARUM_ROUTING_EXPERIMENT.md`.

## Later research

- full bi-temporal queries;
- directed link contracts;
- conflict lifecycle and human resolution;
- validation-policy plugins;
- evidence integrity and source verification;
- real task-sufficiency evaluation;
- alternative projection adapters;
- storage migration tests;
- multi-writer replication models;
- snapshot policy as a separate RFC if replay cost justifies it;
- architecture decision records for major Canon and adapter choices;
- bounded bio-inspired routing and gain experiments under separate research status.

## Promotion rule

```text
research hypothesis
→ reproducible code and tests
→ Offline Shadow evidence where applicable
→ explicit decision record
→ bounded integration proposal
→ threat model and rollback
→ separate implementation PR
→ operator approval
```

Architecture research and executable implementation may progress at different speeds, but their statuses must never be collapsed.

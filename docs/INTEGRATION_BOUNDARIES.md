# Integration Boundaries

## Native Kernel project identity

Velantrim Native Kernel is an independent, personal, long-horizon architecture research project.

It is not the Crystal grant deliverable, not a hidden Crystal runtime, and not constrained by Crystal product milestones.

The project may study or reuse ideas from Titan, Crystal, academic work, and external systems. Any adoption must preserve Native Kernel's own architecture, status discipline, and evidence gates.

Modern technologies such as Python, SQLite, graph engines, FTS, vectors, retrieval pipelines, LLMs, and conventional CPU/GPU systems are treated as replaceable implementation profiles and research instruments.

They are not the permanent definition of the architecture.

## Native Kernel and Titan

Titan / Full Exo-Cortex is the primary research environment for future evaluation. Native Kernel may be tested through:

- recorded-query replay;
- Offline Shadow;
- isolated adapters;
- receipt comparison;
- conflict and omission analysis.

Until later gates are met, Native Kernel must not become Titan's sole production source of truth.

Titan is broader than a collection of Native Kernel projections. It remains an independent cognitive research environment.

## Native Kernel and Crystal

Crystal is an independent, grant-facing verifiable-memory product. This repository is not part of Crystal runtime or grant delivery scope.

Mandatory boundaries:

- Crystal works without Native Kernel.
- Native Kernel is not a second Crystal truth authority.
- No direct Native Event Log → Crystal Canon path.
- No live dual-write under the current research status.
- No claim that Crystal already uses this kernel.
- No prototype benchmark may be presented as Crystal production scalability.
- Native Kernel research is free to continue beyond Crystal product or grant priorities.

Potential future transfer is limited to narrowly scoped mechanisms such as:

- claim lineage;
- deterministic projection rebuild;
- temporal validity semantics;
- conflict lifecycle;
- stronger receipts;
- event-envelope integrity.

Each mechanism requires a separate Crystal RFC, threat model, tests, security and privacy review, rollback plan, pull request, and implementation-status update.

## Architecture and technology boundaries

Safe relationship:

```text
Architecture Canon
→ Abstract Contract
→ Replaceable Implementation Profile
```

Examples:

```text
Claim identity
→ storage contract
→ SQLite row today / another substrate later

Typed relation
→ projection contract
→ adjacency table today / graph engine later

Context retrieval
→ retrieval contract
→ FTS, vector, hybrid, or future activation policy
```

Unsafe relationship:

```text
SQLite schema = memory architecture
Graph database = truth
Embedding space = semantic identity
Python runtime = permanent Canon
Binary processor assumptions = ontology of knowledge
```

Future computational substrates may be studied, but speculative hardware must not be represented as implemented, superior, or compatible without evidence.

## Shared terminology

Safe wording:

```text
Velantrim Native Kernel is a separate, independent long-horizon research project
exploring a model-, storage-, runtime-, and hardware-independent semantic memory
architecture. Current technologies are used as replaceable implementation profiles.
Titan may evaluate it in Offline Shadow. Crystal remains independent and may only
adopt separately validated primitives through its own review process.
```

Unsafe wording:

```text
Crystal runs on Native Kernel.
Native Kernel is the production source of truth for Velantrim.
Titan is only a Native Kernel projection layer.
The kernel proves consciousness or autonomous truth.
The current prototype guarantees sufficient context selection.
The architecture has already been proven on future or non-binary hardware.
Modern databases, retrieval systems, or binary processors are rejected.
```

## Promotion sequence

```text
Native Kernel research
→ abstract contract
→ reproducible prototype and tests
→ cross-profile or Offline Shadow evidence
→ bounded Titan or Crystal RFC where applicable
→ threat model and rollback
→ separate integration PR
→ operator approval
```

No package transfer of the complete research kernel into Crystal is implied or approved by this document.

# Integration Boundaries

## Native Kernel and Titan

Titan / Full Exo-Cortex is the primary research environment for future evaluation. Native Kernel may be tested through:

- recorded-query replay;
- Offline Shadow;
- isolated adapters;
- receipt comparison;
- conflict and omission analysis.

Until later gates are met, Native Kernel must not become Titan's sole production source of truth.

## Native Kernel and Crystal

Crystal is an independent, grant-facing verifiable-memory product. This repository is not part of Crystal runtime.

Mandatory boundaries:

- Crystal works without Native Kernel.
- Native Kernel is not a second Crystal truth authority.
- No direct Native Event Log → Crystal Canon path.
- No live dual-write under the current research status.
- No claim that Crystal already uses this kernel.
- No prototype benchmark may be presented as Crystal production scalability.

Potential future transfer is limited to narrowly scoped mechanisms such as:

- claim lineage;
- deterministic projection rebuild;
- temporal validity semantics;
- conflict lifecycle;
- stronger receipts;
- event-envelope integrity.

Each mechanism requires a separate Crystal RFC, threat model, tests, security and privacy review, rollback plan, pull request, and implementation-status update.

## Shared terminology

Safe wording:

```text
Velantrim Native Kernel is a separate research project exploring a model- and
storage-independent event-sourced memory substrate. Titan may evaluate it in
Offline Shadow. Crystal remains independent and may only adopt separately
validated primitives through its own review process.
```

Unsafe wording:

```text
Crystal runs on Native Kernel.
Native Kernel is the production source of truth for Velantrim.
The kernel proves consciousness or autonomous truth.
The current prototype guarantees sufficient context selection.
```

## Promotion sequence

```text
Native Kernel research
→ reproducible prototype and tests
→ Offline Shadow evidence
→ bounded Titan or Crystal RFC
→ threat model and rollback
→ separate integration PR
→ operator approval
```

No package transfer of the complete research kernel into Crystal is implied or approved by this document.
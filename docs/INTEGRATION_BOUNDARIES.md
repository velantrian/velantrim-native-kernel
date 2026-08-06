# Integration Boundaries

> See the bilingual cross-project navigation map: [`VELANTRIM_ECOSYSTEM.md`](./VELANTRIM_ECOSYSTEM.md).

## Native Kernel project identity

Velantrim Native Kernel is an independent, personal, long-horizon architecture research project.

It is not the Crystal grant deliverable, not a hidden Crystal runtime, not Titan's mandatory storage layer, and not Mentaury's identity authority.

The project may study or reuse ideas from Titan, Crystal, Mentaury, academic work, and external systems. Any adoption must preserve Native Kernel's own architecture, status discipline, and evidence gates.

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

## Native Kernel and Mentaury Soul

> See [`ADR-0010`](./adr/0010-mentaury-soul-implementations-as-external-research-input.md) for the proposed, citation-only research-input practice covering Mentaury Soul's P0-010/P0-013/P0-015.

Mentaury Soul is an independent research track for digital individuality, identity continuity, relationships, commitments and governed development.

Native Kernel may eventually contribute bounded substrate primitives such as append-only events, deterministic replay, lineage, redaction-aware history or auditable Receipts. Those primitives do not define personal identity by themselves.

Mandatory boundaries:

- Native event identity is not personal identity.
- Replay consistency is not continuity proof.
- A valid hash chain is not consent, relationship continuity or capability authority.
- Kernel projections do not become Mentaury M2 beliefs or M3 identity state automatically.
- Copy, fork, restore or migration does not inherit credentials, consent, relationships or commitments from event storage alone.
- Mentaury Canon and Non-Projection review remain independent authority boundaries.
- Any future adapter requires explicit schemas, provenance, privacy review, deterministic tests, rollback, Receipts and operator approval.

Safe relationship:

```text
Native Kernel event / projection / Receipt
→ bounded evidence or infrastructure input
→ Mentaury provenance and source classification
→ uncertainty + contradiction analysis
→ Non-Projection review
→ possible M2 candidate
→ governed longitudinal promotion

Never:
Native Kernel event → direct Mentaury M3 write
```

## Native Kernel and Curiosity Core

Curiosity Core is a proposed optional active-investigation module. It is not part of Native Kernel Canon, not part of the controlled `v0.1.2.1` import, and not an implemented runtime.

Safe relationship:

```text
Native Kernel
→ exposes bounded read, admission, Receipt, and promotion contracts

Curiosity Core
→ detects meaningful unknowns and proposes bounded investigation

Event Admission
→ controls operational process records

Action Gate
→ controls tools and external or irreversible actions

TruthGate
→ controls epistemic promotion or rejection
```

Mandatory boundaries:

- Curiosity Core never mutates Canon or Epistemic State directly.
- Operational curiosity events describe process, not truth.
- Attention allocation may influence task-local context only when the influence is visible in a Receipt.
- Questions, gaps, hypotheses, and System Insights remain candidates until separately evaluated.
- Novelty, priority, repeated use, and utility are not evidence.
- System Insights cannot change code, policy, or architecture automatically.
- Temporal decay may change attention, urgency, or dormancy, but not evidence-derived truth confidence.
- External tools and sensitive or irreversible actions require Action Gate permission.
- Adaptive policies begin in Shadow and require explicit operator approval.
- Curiosity Core can be disabled without damaging Native Kernel replay or integrity.
- Proposed curiosity event verbs do not enter Issue #1 through documentation.

### Titan Curiosity profile

Titan is the primary candidate host for a future full profile because it already represents the broader cognitive research environment.

A Titan profile may eventually include:

- goal-aware gap and conflict detection;
- active questions;
- causal investigation;
- competing Hypothesis Sets;
- falsification and counterfactual checks;
- sandboxed tools through Action Gate;
- System Insights and calibration.

No live Titan integration is claimed or approved by this document.

### Crystal Audit Curiosity profile

Crystal may only consider a restricted profile focused on trust and verification:

```text
Audit Curiosity
├─ evidence gap
├─ provenance gap
├─ contradiction
├─ compliance uncertainty
├─ missing validation
├─ temporal-validity gap
├─ policy conflict
└─ recommended verification step
```

Crystal Audit Curiosity does not imply broad autonomous research, unrestricted hypothesis generation, or self-modifying policy. It requires a separate Crystal RFC, security/privacy review, tests, rollback, and operator approval.

See:

- [`rfc/0001-curiosity-core-architecture.md`](./rfc/0001-curiosity-core-architecture.md);
- [`rfc/0001-curiosity-core-architecture.ru.md`](./rfc/0001-curiosity-core-architecture.ru.md);
- [`adr/0005-curiosity-core-is-optional-and-non-authoritative.md`](./adr/0005-curiosity-core-is-optional-and-non-authoritative.md).

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
Curiosity priority = epistemic validity
SystemInsight = authority to self-modify
```

Future computational substrates may be studied, but speculative hardware must not be represented as implemented, superior, or compatible without evidence.

## Shared terminology

Safe wording:

```text
Velantrim Native Kernel is a separate, independent long-horizon research project
exploring a model-, storage-, runtime-, and hardware-independent semantic memory
architecture. Current technologies are used as replaceable implementation profiles.
Titan may evaluate it in Offline Shadow. Crystal remains independent and may only
adopt separately validated primitives through its own review process. Mentaury remains
an independent identity-continuity research track and may only consume bounded,
provenance-preserving infrastructure inputs through its own governance. Curiosity Core
is a proposed optional non-authoritative research module for bounded investigation.
```

Unsafe wording:

```text
Crystal runs on Native Kernel.
Native Kernel is the production source of truth for Velantrim.
Titan is only a Native Kernel projection layer.
Native Kernel event identity proves Mentaury personal identity.
Kernel replay automatically preserves consent, relationships or commitments.
Curiosity Core makes the Kernel conscious or alive.
Curiosity Core can write truth directly into Canon.
Curiosity priority proves importance or validity.
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
→ bounded Titan, Crystal or Mentaury RFC where applicable
→ threat model, privacy review and rollback
→ separate integration PR
→ operator approval
```

For Curiosity Core specifically:

```text
documented boundary
→ passive frozen-snapshot evaluator
→ deterministic tests and failure cases
→ resource and safety validation
→ receipted Offline Shadow
→ separate bounded integration proposal
→ operator approval
```

No package transfer of the complete research kernel into Crystal, Titan or Mentaury is implied or approved by this document.

# 🎯 A1 — Kernel Purpose and Non-goals

**[English](./A1_KERNEL_PURPOSE_AND_NON_GOALS.md) · [Русский](./A1_KERNEL_PURPOSE_AND_NON_GOALS.ru.md)**

> **Deliverable:** `A1` of the [Architecture Re-foundation](./ARCHITECTURE_REFOUNDATION.md) blueprint (`ADR-0025`, [Issue #88](https://github.com/velantrian/velantrim-native-kernel/issues/88))
> **Evidence boundary:** architecture research and definition only; no runtime, contract, evidence, assertion map, NK-EPI, maturity, or production change
> **Review status:** first drafted slice; pending independent review and integrated blueprint review with A2–A10

## 1. What this document is

This document answers the completion test set by the Architecture Re-foundation plan for `A1`:

> A reader can distinguish the architecture from a product, database, framework, cognitive system, and storage engine without referring to current source code.

It defines the problem Native Kernel studies, what the word `Kernel` means in this project, the durable qualities a Kernel implementation must preserve, what is explicitly outside the Kernel, and the boundary with Titan, Crystal, Mentaury, operating systems, databases, and model runtimes.

It does not define the ontology (`A2`), the abstract machine (`A3`), the semantic laws (`A4`), or any later deliverable. Where this document uses a term that a later deliverable will define more precisely, that term is used informally and flagged as provisional.

## 2. The problem Native Kernel studies

Software systems that store knowledge usually begin from available machinery rather than from a stated question:

```text
a relational database is available → memory becomes tables and rows
a graph engine is available        → knowledge becomes vertices and edges
a vector index is available        → meaning becomes numerical proximity
an LLM API is available            → reasoning becomes whatever that provider returns
```

Each choice can be useful. The problem is that the temporary structure of the chosen technology silently becomes the permanent definition of what a claim, a fact, a memory, an identity, or a truth *is*. When the technology changes, the system must rewrite not only its storage and execution, but its understanding of what the retained information meant.

Native Kernel exists to study a different, explicit question:

> **What must be true about the representation of a claim, its evidence, its history of change, and the confidence attached to it, so that the same meaning survives a change of storage, language, processor, or computational paradigm?**

This is a research question about representation and invariants, not a commitment to build a shipped product, a database engine, or an AI system.

## 3. What `Kernel` means in this project

Inside Native Kernel, `Kernel` denotes:

```text
a minimal, technology-neutral set of semantic obligations
that any concrete implementation of claim/knowledge management
must satisfy to be called a conforming Native Kernel implementation,
together with the abstract machine and laws that make those
obligations checkable.
```

A Kernel, in this sense, is closer to an abstract instruction set architecture for meaning than to an executable artifact. It is a contract that many different, mutually incompatible implementations can each satisfy in their own way, while remaining comparable through declared equivalence.

The Kernel is not:

- a single running program;
- a specific file format, schema, or wire protocol;
- a library, SDK, or framework that ships as source code;
- the Python/PostgreSQL/SQLite reference laboratory currently in this repository.

The reference laboratory (`P1`–`C5`) is one attempted, partial, bounded expression of hypothesized Kernel obligations. It is evidence about whether those obligations are implementable and testable. It is not the Kernel itself, and its present shape must not be read backward into the definition of the Kernel merely because it was written first. `A9` will classify each laboratory module against this boundary in detail.

## 4. Durable qualities the Kernel must preserve

The following qualities are the current, versioned, revisable candidate list of what a conforming implementation must preserve regardless of substrate. `A4` will state these as numbered semantic laws with counterexamples and failure modes; this section only names them and explains why each is a candidate.

| Quality | Why it is a candidate obligation |
|---|---|
| **Semantic identity** | A claim must not become a different claim merely because its storage row, file location, or process moved |
| **Explicit change** | Revision, supersession, restriction, and erasure must remain visible operations, not silent overwrites |
| **Provenance** | Where a claim came from and how it was transformed must remain attached to the claim, not inferred after the fact |
| **Lineage** | Related versions and derivations of a claim must remain traceable to one another |
| **Temporal meaning** | The time something was true, the time it was observed, and the time it was recorded must remain distinguishable, not collapsed into one timestamp |
| **Epistemic state** | Supported, inferred, contested, unknown, and rejected claims must remain distinguishable from one another and from truth |
| **Conflict visibility** | A contradiction must remain visible until an explicit process resolves it; it must not be silently averaged, dropped, or overwritten |
| **Reconstructability** | Disposable derived state must be reproducible from retained authoritative material under a declared equivalence rule |
| **Bounded accountability** | A selection, omission, transformation, or refusal must be explainable through a bounded record, without claiming that record proves completeness or truth |
| **Declared equivalence under substrate change** | Moving to a different storage, language, or processor must preserve a named, tested level of semantic equivalence, not an assumed one |

These are hypotheses under active research, not settled mathematics. Each remains open to revision, replacement, or rejection through an explicit architecture decision, and `A10` will track the falsification condition for each one.

## 5. What belongs outside the Kernel

The Kernel does not define, and must not be defined by:

- a specific database, file format, serialization, or wire protocol;
- a specific programming language, runtime, or processor architecture;
- a specific retrieval algorithm, ranking function, or embedding model;
- a specific LLM, prompting strategy, or agent orchestration pattern;
- application-level features such as user interfaces, notifications, or workflow automation;
- performance targets, throughput numbers, or latency budgets;
- deployment topology, multi-tenancy, or operational infrastructure;
- legal, licensing, or compliance certification;
- production-readiness, security hardening, or incident response processes.

These are legitimate concerns for an implementation profile, a deployment, or a product built on top of a conforming Kernel. They are not properties the Kernel architecture itself asserts, requires, or forbids at the Canon level.

## 6. Boundary with Titan, Crystal, and Mentaury

Native Kernel is one of several independent Velantrim research and product tracks. `docs/VELANTRIM_ECOSYSTEM.md` defines the cross-project relationship map in detail; this section restates only the part relevant to the Kernel's own definition.

```text
🧬 Native Kernel   — substrate-neutral architecture for claims, evidence, provenance,
                     time, conflict, revision, and bounded explanation
🔱 Titan           — cognition, orchestration, retrieval, tools, and agents
💎 Crystal         — verifiable memory, evidence, trust, and audit product
⭐️ Mentaury Soul   — digital individuality, identity continuity, relationships,
                     commitments, and governed development
```

- Native Kernel is not a hidden storage layer, memory backend, or truth authority for Titan, Crystal, or Mentaury.
- Titan may evaluate Kernel ideas as a workload source or through a bounded, reviewed adapter. That evaluation does not make Titan's runtime the Kernel's runtime, and does not make the Kernel's evidence Titan's evidence.
- Crystal continues to define and evolve its own Canon, evidence model, and grant-facing product independently of whether Native Kernel exists or changes.
- A Kernel claim, event, projection, or Receipt does not become a Mentaury identity, relationship, commitment, or continuity record merely by existing. Identity continuity is Mentaury's own research problem, not a Kernel export.
- No capability, credential, consent, or authority is inherited across these projects implicitly. Any future integration requires its own scoped ADR/RFC, explicit equivalence contract, tests, threat/privacy review, and separate operator approval, exactly as `VELANTRIM_ECOSYSTEM.md` already requires.

## 7. Boundary with operating systems, databases, and model runtimes

- **Operating system.** The Kernel does not manage processes, scheduling, memory allocation, device drivers, or a filesystem. An operating system may host an implementation profile; it is not itself a Kernel concern.
- **Database.** A database (relational, document, graph, key-value, or vector) may serve as the durable store for one implementation profile's authoritative history or derived projections. The Kernel does not require any particular database, does not assume SQL, and does not treat any database's transaction or consistency model as a Canon requirement rather than an implementation detail to be mapped explicitly (`A8`).
- **Model runtime.** An LLM, embedding model, or other machine-learning runtime may be used by an implementation profile to interpret, summarize, propose, or rank candidate information. The Kernel does not require a model runtime to exist, does not treat model output as admitted knowledge by default, and does not delegate epistemic classification (claim, evidence, conflict, uncertainty) to a model's confidence score. `docs/WORLD_AND_EPISTEMIC_BOUNDARIES.md` already records the specific epistemic-boundary failure modes this excludes; this section only states the architectural boundary that motivates them.
- **Knowledge graph, search index, or memory framework.** Any of these may implement one projection or access path over Kernel-conformant history. None of them is the Kernel itself, and none may silently become the authoritative source of truth in place of the retained history it was derived from.

## 8. Non-goals of this document and of the Kernel at this stage

This document does not:

- define the ontology of knowledge and memory primitives (`A2`);
- define the abstract Kernel machine's states and transitions (`A3`);
- state semantic laws with counterexamples and failure modes (`A4`);
- define identity, time, or change formally (`A5`);
- define the knowledge lifecycle (`A6`);
- define conflict, uncertainty, or revision semantics (`A7`);
- define the substrate-independence contract (`A8`);
- classify the existing reference laboratory module by module (`A9`);
- enumerate open questions and falsification criteria (`A10`);
- authorize, resume, or design any new runtime, reducer version, database profile, or ecosystem integration;
- change the assertion map, `NK-EPI` support state, `C4`/`C5` maturity, or production authorization;
- decide `Issue #18` (license/publication) or `ADR-0024` (reducer referential semantics);
- claim that the durable qualities in Section 4 have been proven, only that they are the current candidate obligations under active research.

The Kernel, at this stage of the blueprint, is a stated problem, a working definition of the term, a candidate list of durable qualities, and an explicit set of boundaries. It is not yet an abstract machine, a law set, or an implementation requirement.

## 9. Relationship to existing documents

- [`FOUNDATIONAL_INTENT.md`](./FOUNDATIONAL_INTENT.md) narrates the same motivation in essay form and remains valid background reading; this document is the versioned, blueprint-tracked deliverable that the Architecture Re-foundation plan requires under the exact name `A1_KERNEL_PURPOSE_AND_NON_GOALS`.
- [`ARCHITECTURE_REFOUNDATION.md`](./ARCHITECTURE_REFOUNDATION.md) defines the ten-deliverable sequence and the completion gate this document must satisfy for `A1`.
- [`VELANTRIM_ECOSYSTEM.md`](./VELANTRIM_ECOSYSTEM.md) defines the full cross-project integration-boundary contract referenced in Section 6.
- [`WORLD_AND_EPISTEMIC_BOUNDARIES.md`](./WORLD_AND_EPISTEMIC_BOUNDARIES.md) defines the epistemic-boundary failure modes referenced in Section 7.
- [`../ARCHITECTURE.md`](../ARCHITECTURE.md) describes the current Canon shape produced by the reference laboratory; Section 3 of this document explains why that shape is evidence, not the Kernel definition.

## 10. Open questions carried forward

The following questions are noted here because they surfaced while drafting `A1`, but they are owned by later deliverables and are not answered here:

- Which of the Section 4 qualities are truly substrate-independent obligations, and which are artifacts of event-sourcing practice? (`A4`, `A8`)
- Can "bounded accountability" be satisfied without any durable log at all? (`A6`, `A8`)
- Does the Titan/Crystal/Mentaury boundary in Section 6 need a distinct contract per project, or one shared cross-project contract? (future ecosystem RFC, outside this blueprint)

## 11. Non-claims

```text
this document ≠ the ontology, abstract machine, or semantic laws
naming a quality in Section 4 ≠ proving that quality is achievable
this document ≠ approval to resume runtime, reducer, or profile work
this document ≠ a decision on Issue #18 or ADR-0024
this document ≠ evidence that any future substrate already conforms
```

## 12. Status

```text
deliverable: A1_KERNEL_PURPOSE_AND_NON_GOALS
state: DRAFTED
review: PENDING independent review and integrated blueprint review with A2-A10
next_content_slice: A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY
runtime, evidence, assertions, NK-EPI, maturity, production: UNCHANGED
```

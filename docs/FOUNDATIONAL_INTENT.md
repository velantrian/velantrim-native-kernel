# 🔱 Foundational Intent

**[English](./FOUNDATIONAL_INTENT.md) · [Русский](./FOUNDATIONAL_INTENT.ru.md)**

> **Status:** `ARCHITECTURAL INTENT / DOCUMENTATION / NOT A RUNTIME CLAIM`  
> **Track:** independent personal research  
> **Purpose:** explain why Velantrim Native Kernel exists, what problem it studies, and what should survive technology replacement

---

## 1. The simple idea

Velantrim Native Kernel is not a tuning layer for Titan and is not a hidden part of Crystal.

It is a separate, long-horizon architectural research project that asks:

> **How should memory, knowledge, change, uncertainty, conflict, and explanation be represented so that their meaning remains understandable when the underlying technology changes?**

```text
technology changes
        ↓
implementation profile changes
        ↓
architectural meaning should remain understandable
```

> [!NOTE]
> Native Kernel is a blueprint tested with present-day tools. It is not a rejection of present-day tools.

---

## 2. The problem this project studies

Most software systems begin with available machinery:

```text
we have a relational database
→ memory becomes tables and rows

we have a graph engine
→ knowledge becomes vertices and edges

we have a vector index
→ meaning becomes numerical proximity

we have an LLM API
→ reasoning becomes whatever that provider returns
```

These technologies can be useful and effective. The problem appears when their temporary structure silently becomes the permanent definition of memory, knowledge, identity, truth, or reasoning.

When the technology later changes, the system may have to rewrite not only its storage and execution, but also its understanding of what the information means.

Native Kernel studies a different order:

```text
first define the meaning and invariants
        ↓
then define abstract behavioural contracts
        ↓
then implement those contracts with available technology
```

The project therefore does not begin with the question:

> Which database should own memory?

It begins with questions such as:

- What gives a Claim stable semantic identity?
- How should change remain explicit rather than silently overwrite the past?
- How should provenance and lineage survive migration?
- How should time, uncertainty, conflict, and revision be represented?
- How can derived state be reconstructed?
- How can the system explain what it selected, omitted, or could not establish?

---

## 3. Architecture before machinery

The project separates two categories.

### What should remain stable?

- semantic identity;
- explicit history of change;
- provenance and lineage;
- temporal meaning;
- uncertainty and epistemic status;
- conflict visibility;
- reconstructable state;
- accountable selection and Receipts;
- explicit boundaries between evidence, relevance, utility, and truth.

### What may be replaced?

- databases;
- file formats;
- graph engines;
- search algorithms;
- vector indexes;
- model providers;
- programming languages;
- operating environments;
- processor assumptions;
- storage media;
- future computational substrates.

```text
🏛️ Architecture Canon
        ↓
📐 Abstract Contracts
        ↓
🔌 Replaceable Implementation Profiles
        ↓
🧪 Reproducible Evidence
```

The architecture describes required meaning and observable behaviour. A current implementation demonstrates part of that description without becoming the permanent definition of it.

---

## 4. Present technology is a laboratory

Native Kernel does not reject Python, SQLite, files, FTS, graphs, vectors, retrieval systems, LLMs, CPUs, or GPUs.

They are useful because they allow the project to:

- execute architectural ideas;
- test invariants;
- expose contradictions;
- measure cost and failure modes;
- compare alternative profiles;
- distinguish a useful principle from an attractive metaphor.

```text
present technology
        =
research instrument
        ≠
permanent architecture definition
```

Examples:

- SQLite may store event history without becoming the meaning of that history.
- A graph may expose relations without becoming the authority for truth.
- A vector index may rank candidates without defining semantic correctness.
- An LLM may propose or interpret information without becoming the source of truth.
- A CPU/GPU runtime may execute the reference implementation without defining the only possible computational model.

> [!IMPORTANT]
> The project claims portability at the level of explicit contracts and tests. It does not claim that arbitrary future hardware is already supported.

---

## 5. The blueprint analogy

A useful analogy is a future transportation blueprint.

A design may ask what a less destructive transportation system should accomplish before the required propulsion technology exists. Present vehicles and roads can still be used for experiments, but they should not automatically define the final principle of movement.

Native Kernel applies the same discipline to information architecture:

```text
available machinery today
        ↓
reference experiments
        ↓
refined contracts and invariants
        ↓
future implementations may replace the machinery
```

The analogy is not a technical claim about levitation, quantum computing, or any particular future technology. Its purpose is to explain the separation between:

```text
what the system should preserve
        ≠
how one implementation performs it today
```

---

## 6. Why Native Kernel remains separate

```text
🧬 Native Kernel
independent architecture and reference experiments

🔱 Titan
broader cognitive research environment

💎 Crystal
independent trust-facing product and grant track
```

Native Kernel may learn from Titan, Crystal, academic systems, and external projects. Adoption is selective.

It must not inherit a dependency merely because another Velantrim project currently uses it.

> [!IMPORTANT]
> A useful mechanism may be borrowed. The architectural dependency is not borrowed automatically.

Examples:

- Titan may provide workloads for evaluating a Kernel contract without defining that contract.
- Crystal may later adopt a validated primitive without becoming the owner of Kernel semantics.
- Native Kernel may use ideas from both projects while remaining separately versioned, reviewed, and testable.
- Neither Titan nor Crystal is required for Native Kernel to exist.

This separation protects:

- architectural clarity;
- safe experimentation;
- independent failure analysis;
- the ability to reject an integration without destabilising another project;
- the ability to compare several implementations of the same contract.

---

## 7. What the architecture is trying to preserve

The project currently treats the following as candidate durable properties:

| Property | Why it matters |
|---|---|
| **Semantic identity** | A Claim should not become a different meaning merely because its backend row or file location changes |
| **Explicit change** | Revision, supersession, restriction, and erasure should not be hidden as silent overwrites |
| **Provenance** | The system should retain where information came from and how it was transformed |
| **Lineage** | Related versions and derivations should remain inspectable |
| **Temporal meaning** | Valid time, record time, and write order should not collapse into one timestamp |
| **Epistemic state** | Supported, inferred, contested, unknown, and rejected information should remain distinguishable |
| **Conflict visibility** | Contradiction should remain visible until an explicit resolution process handles it |
| **Reconstructability** | Disposable state should be reproducible from authoritative history |
| **Auditability** | The system should explain selection, omission, transformation, conflict, and uncertainty through Receipts |
| **Technology replacement** | Moving to a new profile should preserve a declared level of semantic equivalence |

These properties are versioned architectural hypotheses. They are not presented as eternal mathematical truths.

---

## 8. How the research should proceed

Native Kernel should grow through bounded experiments rather than by accumulating every interesting idea.

```text
architectural question
        ↓
explicit proposal or ADR
        ↓
small reference experiment
        ↓
failure cases and evidence
        ↓
review by maintainer/operator
        ↓
accept, revise, reject, or keep experimental
```

The project deliberately separates:

```text
interesting idea
≠ accepted architecture

working local code
≠ repository-reproduced evidence

several AI opinions
≠ operator approval

successful retrieval
≠ established truth
```

AI systems, papers, existing projects, and human reviewers may provide design inputs. They do not silently approve architecture.

---

## 9. The first proof is intentionally small

The first important experiment is not a large autonomous system and not a full Titan integration.

It is a reconstruction test:

```text
1. Create Claims and Events.
2. Derive semantic state.
3. Delete disposable projections and indexes.
4. Rebuild from authoritative history.
5. Compare the semantic result under a declared equivalence rule.
6. Produce a Receipt describing the reconstruction.
```

Required outcome:

```text
full_replay(authoritative_history)
    ≡
previous_semantic_state
```

`≡` means a documented level of semantic equivalence. It does not require every implementation to serialize identical bytes.

> [!NOTE]
> One reproducible result is more valuable than ten untested architectural claims.

---

## 10. What success would mean

The project would provide meaningful evidence for its central thesis if it can demonstrate that:

1. the same declared history can be interpreted by more than one implementation profile;
2. deleting SQLite tables, graph indexes, FTS indexes, vectors, or other disposable projections does not destroy authoritative meaning;
3. reconstructed state preserves declared identity, lineage, provenance, temporal meaning, and epistemic status;
4. technology replacement does not silently change the truth, conflict, or access semantics;
5. important decisions remain explainable through Receipts and ADRs;
6. failures and unknowns remain visible instead of being converted into confident output;
7. a third party can reproduce the claimed behaviour from the repository;
8. future implementations can demonstrate conformance without copying the same source code or storage layout.

Success does not require the current reference implementation to solve every memory or reasoning problem. It requires the project to produce clear contracts, honest boundaries, and reproducible evidence.

---

## 11. Long-horizon research questions

The long-horizon track may investigate questions such as:

- Which parts of Claim, Event, Lineage, Conflict, and Receipt are genuinely substrate-independent?
- Which concepts are only artifacts of current event-sourcing or database practice?
- What kind of equivalence is required across different implementations?
- Can a non-relational, neuromorphic, probabilistic, analog, photonic, or other future substrate preserve the same semantic contracts?
- Which invariants should survive a major architecture version, and which should be replaced?
- How should the system represent Unknown, incomplete evidence, and unresolved conflicts?
- How should computational efficiency be improved without turning an optimisation into the source of truth?

These are research directions, not implementation claims.

---

## 12. What the project is not claiming

```text
🚫 The current design is a universal mathematical truth.
🚫 Future hardware is already compatible.
🚫 Event sourcing solves every memory problem.
🚫 Documentation proves feasibility.
🚫 Titan or Crystal must migrate to Native Kernel.
🚫 The reference implementation is the final architecture.
🚫 Several AI models agreeing counts as evidence.
🚫 A reproducible Receipt proves that selected context was sufficient.
🚫 Technology independence has already been demonstrated across arbitrary substrates.
```

The project seeks durable invariants, but every invariant remains versioned, reviewable, testable, and open to revision through explicit architecture decisions.

---

## 13. Guidance for readers, contributors, and AI systems

Before proposing or accepting a change, ask:

1. Is this a durable semantic requirement or a property of today's implementation?
2. Could another technology implement the same contract?
3. What evidence supports the claim?
4. What is the declared equivalence rule?
5. Does the change preserve the boundary between Canon, contract, profile, runtime evidence, and production evidence?
6. Does it create an unintended dependency on Titan, Crystal, SQLite, a graph engine, an LLM, or a processor model?
7. Does it hide conflict, uncertainty, provenance, or failure?
8. Is an Architecture Decision Record required?
9. Is the proposal being confused with implementation or approval?

> **Central statement:** Native Kernel is an independent, future-facing architecture blueprint tested with present-day tools. The tools may change; the project exists to identify, preserve, test, and clarify the semantic meaning that should survive those changes.

---

## Related documents

- [`LONG_HORIZON_VISION.md`](./LONG_HORIZON_VISION.md) — architecture layers and future research horizon
- [`CONFORMANCE_MODEL.md`](./CONFORMANCE_MODEL.md) — how an implementation demonstrates compatibility
- [`DECISION_PROCESS.md`](./DECISION_PROCESS.md) — how architecture decisions and evidence are recorded
- [`adr/0004-rebuild-from-authoritative-history.md`](./adr/0004-rebuild-from-authoritative-history.md) — proposed first conformance experiment
- [`../ARCHITECTURE.md`](../ARCHITECTURE.md) — current Canon shape and invariants
- [`../STATUS.md`](../STATUS.md) — authoritative implementation boundary

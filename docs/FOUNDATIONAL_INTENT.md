# 🔱 Foundational Intent

> **Status:** `ARCHITECTURAL INTENT / DOCUMENTATION / NOT A RUNTIME CLAIM`  
> **Track:** independent personal research  
> **Purpose:** explain, in plain language, why Velantrim Native Kernel exists as a separate system

## 1. The simple idea

Velantrim Native Kernel is not a tuning layer for Titan and is not a hidden part of Crystal.

It is a separate architectural research project that asks:

> **How should memory, knowledge, change, uncertainty, conflict, and explanation be represented so that their meaning survives when the underlying technology changes?**

```text
technology changes
        ↓
implementation profile changes
        ↓
architectural meaning should remain understandable
```

> [!NOTE]
> This project does not reject current technology. Python, SQLite, files, graphs, FTS, vectors, retrieval systems, LLMs, CPUs, and GPUs are useful laboratory tools. They are not allowed to become the permanent definition of the architecture.

---

## 2. Architecture before machinery

The project separates two questions:

### What should remain stable?

- semantic identity;
- explicit history of change;
- provenance and lineage;
- temporal meaning;
- uncertainty and epistemic status;
- conflict visibility;
- reconstructable state;
- accountable selection and Receipts.

### What may be replaced?

- databases;
- file formats;
- graph engines;
- search algorithms;
- vector indexes;
- model providers;
- programming languages;
- processor assumptions;
- future storage and compute substrates.

```text
🏛️ Architecture Canon
        ↓
📐 Abstract Contracts
        ↓
🔌 Replaceable Implementations
```

The architecture should describe the required meaning and behaviour. A current implementation should demonstrate that description without redefining it.

---

## 3. Why Native Kernel remains separate

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

- Titan may help evaluate a Kernel contract without defining that contract.
- Crystal may later adopt a validated primitive without becoming the owner of Kernel semantics.
- SQLite may store an event history without becoming the meaning of that history.
- A graph may expose relations without becoming the authority for truth.

---

## 4. The first proof is small

The first important experiment is not a large autonomous system.

It is a reconstruction test:

```text
1. Create Claims and Events.
2. Derive semantic state.
3. Delete disposable projections and indexes.
4. Rebuild from authoritative history.
5. Compare the semantic result.
6. Produce a Receipt describing the reconstruction.
```

Required outcome:

```text
full_replay(authoritative_history)
    ≡
previous_semantic_state
```

`≡` means a documented level of semantic equivalence. It does not require every future implementation to serialize identical bytes.

> [!NOTE]
> One reproducible result is more valuable than ten untested architectural claims.

---

## 5. What the project is not claiming

```text
🚫 The current design is a universal mathematical truth.
🚫 Future hardware is already compatible.
🚫 Event sourcing solves every memory problem.
🚫 Titan or Crystal must migrate to Native Kernel.
🚫 Documentation proves feasibility.
🚫 Several AI models agreeing counts as evidence.
```

The project seeks durable invariants, but every invariant remains versioned, reviewable, testable, and open to revision through explicit architecture decisions.

---

## 6. Reader guidance

When reading or changing this repository, ask:

1. Is this a durable semantic requirement or a property of today's implementation?
2. Could another technology implement the same contract?
3. What evidence supports the claim?
4. Does the change preserve the boundary between Canon, contract, profile, and runtime evidence?
5. Is an Architecture Decision Record required?

> **Central statement:** Native Kernel is a future-facing blueprint tested with present-day tools. The tools may change; the project exists to preserve and clarify the meaning that should survive those changes.

# 🧬 Velantrim Native Kernel — Human Project Overview

**[English](./PROJECT_OVERVIEW.md) · [Русский](./PROJECT_OVERVIEW.ru.md)**

> **Audience:** people who want to understand the architecture before reading the formal contracts.  
> **Not a live-state ledger:** for current gates, authorization and evidence status use [STATUS.md](STATUS.md) and [project-state.json](project-state.json).  
> **AI agents:** start from [docs/ai/README.md](docs/ai/README.md), not from this narrative.

## 🎯 The problem

Most knowledge systems are described in terms of the technology that currently implements them:

- rows and tables;
- documents and JSON;
- graph nodes and edges;
- embeddings and vector search;
- event logs and reducers;
- model context and agent memory.

Those mechanisms are useful, but they are not automatically the *meaning* of the knowledge.

Native Kernel asks a different question:

> If the storage engine, programming language, processor, memory representation or inference model changes, **which semantic obligations must still hold for us to say that the same knowledge process survived?**

The project therefore tries to separate **architecture-level meaning** from **profile-level realization**.

## 🧠 Mental model

```text
world / source
     │
     ▼
👁 observation
     │
     ▼
💬 claim
     │
     ├───────────────┐
     ▼               ▼
🔎 evidence       🧭 provenance
     │               │
     └───────┬───────┘
             ▼
       ⚖ epistemic position
             │
      ┌──────┼────────┐
      ▼      ▼        ▼
   🌫 doubt ⚔ conflict 🔁 revision
      │      │        │
      └──────┴────────┘
             ▼
       🧾 explanation
             │
             ▼
      🕰 accountable history
```

The architecture is interested in the **relations and obligations** between these concepts. It does not require every implementation to store them in the same byte layout.

## 🏛️ Architecture layers

```text
┌──────────────────────────────────────────────────────────────┐
│ 🧠 SEMANTIC MEANING                                         │
│ identity · evidence · provenance · uncertainty · revision   │
└───────────────────────────┬──────────────────────────────────┘
                            │ obligations
┌───────────────────────────▼──────────────────────────────────┐
│ 📐 TECHNOLOGY-NEUTRAL CONTRACTS                              │
│ what a conforming realization must preserve / expose        │
└───────────────────────────┬──────────────────────────────────┘
                            │ mapping
┌───────────────────────────▼──────────────────────────────────┐
│ 🔌 PROFILES                                                  │
│ a concrete way to realize the obligations                   │
└───────────────────────────┬──────────────────────────────────┘
                            │ implementation
┌───────────────────────────▼──────────────────────────────────┐
│ 🧪 REFERENCE LABORATORY                                     │
│ executable, bounded, replaceable research machinery         │
└───────────────────────────┬──────────────────────────────────┘
                            │ observations
┌───────────────────────────▼──────────────────────────────────┐
│ 🔬 EVIDENCE / FALSIFICATION                                 │
│ what survived, failed, weakened, or remains untested        │
└───────────────────────────┬──────────────────────────────────┘
                            │ informs — never auto-promotes
┌───────────────────────────▼──────────────────────────────────┐
│ 🚦 GOVERNED DECISIONS                                       │
│ architecture / Final Canon / runtime / production           │
└──────────────────────────────────────────────────────────────┘
```

The bottom layer cannot silently rewrite the top layer. A convenient implementation choice is not allowed to become a universal law merely because the current code uses it.

## 🧩 The semantic obligations

The current architecture work separates several families of concerns.

| Concern | Question Native Kernel asks |
|---|---|
| 🧠 Knowledge | What distinguishes an observation, claim, evidence item and epistemic position? |
| 🔎 Provenance | Where did a claim/evidence item come from, and what does that provenance actually prove? |
| 🕰 Identity & time | What remains “the same thing” across revision, copying, migration and change? |
| 🌫 Uncertainty | How is not-knowing represented without silently converting it into false certainty? |
| ⚖ Conflict | How can incompatible positions coexist without forcing a fake universal winner? |
| 🔁 Revision | How is a belief changed, superseded or weakened while preserving accountability? |
| 🗑 Loss / erasure | What does logical disappearance prove — and what does it not prove about physical deletion? |
| 🧾 Explanation | Can the system explain why a current state exists and which evidence shaped it? |
| 🌍 Substrate independence | Can these obligations survive a change of representation or computational substrate? |

A major design rule follows:

```text
storage fact ≠ semantic truth
operation receipt ≠ correctness
history visibility ≠ mandatory event sourcing
graph representation ≠ mandatory graph architecture
embedding retrieval ≠ knowledge
profile conformance ≠ production authorization
```

## 🌍 What “substrate-neutral” means here

Substrate neutrality is **not** the claim that one implementation already runs unchanged on every possible machine.

It is the stronger architectural discipline that the project should be describable without making present-day mechanisms permanent by accident.

For example:

```text
Architecture obligation:
  "a revision must preserve enough lineage to distinguish
   replacement, supersession and unresolved conflict"

Possible realization A:
  PostgreSQL rows + explicit provenance records

Possible realization B:
  graph edges + temporal validity

Possible realization C:
  append-only cells + derived views

Possible realization D:
  future non-von-Neumann substrate

Question:
  do all four preserve the declared obligation?
```

If a mapping cannot preserve an obligation, the correct answer may be **LOSSY**, **PARTIAL**, **REFUTED** or **INDETERMINATE**. The architecture should expose that instead of hiding it.

## 🧪 Why the reference laboratory exists

A purely abstract architecture is easy to overclaim. The laboratory exists to attack the abstractions with executable cases.

The current laboratory lineage includes conventional software mechanisms such as Python, PostgreSQL, SQLite and independent-language experiments. Their role is deliberately bounded:

```text
laboratory
   ├── produces observations
   ├── exposes implementation assumptions
   ├── gives invariants something concrete to fail against
   └── provides reproducible evidence
        │
        └── but does NOT define permanent Canon
```

This lets the project ask questions such as:

- Does an invariant survive when storage changes?
- Does a claim depend on an event-sourced representation that the architecture never justified?
- Is “replay” actually required, or is accountable reconstruction enough?
- Does a mechanism preserve meaning, or merely preserve bytes?
- Did an experiment test the hypothesis, or only a convenient proxy?

## 🔬 Evidence before promotion

Native Kernel deliberately separates these states:

```text
IMPLEMENTED
    ↓
TESTED
    ↓
EVIDENCE QUALIFIED
    ↓
SUPPORTED FOR A DECLARED SCOPE
    ↓
ARCHITECTURE REASSESSED
    ↓
possible operator decision

None of these arrows is automatic.
```

A failed experiment is useful. An indeterminate experiment is useful. A result that weakens the architecture is useful.

The research process is not optimized to make the current design “win”; it is optimized to reveal where its claims are too strong.

## 🆚 Relationship to agent-memory and graph systems

Native Kernel overlaps with memory systems, but its unit of concern is different.

### 🧠 Letta / MemGPT

Letta describes itself as a platform for stateful agents with advanced persistent memory. That is an agent-level problem: how an agent remembers, learns and carries state across interactions/models.

Native Kernel asks a lower-level architecture question: if a memory mechanism is replaced, what semantic properties must be preserved for the resulting system to count as equivalent for a declared scope?

### 🕸 Graphiti

Graphiti is an open-source temporal context graph engine for AI agents. It tracks evolving facts, temporal validity and provenance, and supports graph-aware retrieval.

Those capabilities are highly relevant to Native Kernel, but Native Kernel does not declare a graph to be the universal representation. A graph can be one profile if it preserves the required semantics.

### 📚 RAG, event sourcing and other mechanisms

RAG can be a retrieval mechanism. Event sourcing can be a history mechanism. A relational database can be a storage mechanism. A graph can be a relation mechanism. An LLM can be an inference mechanism.

Native Kernel treats these as **candidate instruments**, not as identity-defining primitives.

| Mechanism | Native Kernel view |
|---|---|
| Vector search | useful retrieval profile, not knowledge itself |
| Knowledge graph | useful relational profile, not mandatory universal topology |
| Event log | useful history profile, not automatically the universal semantic primitive |
| LLM memory block | useful agent-memory profile, not the source of architectural truth |
| SQL schema | useful durable mapping, not Canon by itself |

Official comparison references: [Letta](https://github.com/letta-ai/letta) and [Graphiti](https://github.com/getzep/graphiti).

## 🧭 What makes the project unusual

Four choices are especially important:

1. **The implementation is intentionally demoted.**  
   The current working code is evidence-producing machinery, not the definition of the architecture.

2. **Uncertainty and conflict are first-class.**  
   The system should be able to say “unresolved”, “weakened” or “unknown” without converting those states into a forced binary answer.

3. **Evidence has bounded authority.**  
   Passing a test supports only the hypotheses and scope that the test actually adjudicated.

4. **Promotion is governed separately.**  
   Architecture, Final Canon, runtime authorization and production authorization are distinct decisions.

## 🧱 What the project is not trying to be

Native Kernel is not currently claiming to be:

- a production database;
- a universal memory server;
- a finished autonomous-agent framework;
- a replacement for every knowledge graph;
- a proof that one event model works on every substrate;
- a proof of quantum, neuromorphic or biological portability;
- a production-authorized runtime.

Those may become implementation contexts or future experiments. They are not implied by the current architecture.

## 📚 Deep reading map

```text
👤 Human understanding
README.md
  ↓
PROJECT_OVERVIEW.md
  ↓
ARCHITECTURE.md
  ↓
docs/A1...A10
  ↓
docs/research/
  ↓
evidence/

🤖 Machine / agent continuity
docs/ai/README.md
  ↓
AGENTS.md
  ↓
project-state.json
  ↓
docs/ai/CURRENT_STATE.md
  ↓
required contracts / ADRs / research artifacts

📊 Live state
STATUS.md + project-state.json
```

Useful entry points:

- [ARCHITECTURE.md](ARCHITECTURE.md) — architectural orientation.
- [docs/A1_KERNEL_PURPOSE_AND_NON_GOALS.md](docs/A1_KERNEL_PURPOSE_AND_NON_GOALS.md) — purpose and non-goals.
- [docs/A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md](docs/A2_KNOWLEDGE_AND_MEMORY_ONTOLOGY.md) — ontology.
- [docs/A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md](docs/A8_SUBSTRATE_INDEPENDENCE_CONTRACT.md) — substrate-independence contract.
- [docs/A9_REFERENCE_LABORATORY_BOUNDARY.md](docs/A9_REFERENCE_LABORATORY_BOUNDARY.md) — laboratory vs architecture.
- [docs/A10_OPEN_QUESTIONS_AND_FALSIFICATION.md](docs/A10_OPEN_QUESTIONS_AND_FALSIFICATION.md) — hypotheses and falsification.
- [STATUS.md](STATUS.md) — current human-readable status.
- [project-state.json](project-state.json) — machine-readable state.
- [docs/ai/README.md](docs/ai/README.md) — AI/agent entrypoint.

## 🚦 Authority note

This overview is intentionally **stable**. It should change when the conceptual architecture changes, not every time a PR lands.

When you need to know whether a gate is open, whether a reviewer is qualified, whether runtime is authorized, or what the current evidence checkpoint is, do not infer it from this page. Read the current-state surfaces.

> **Short version:** Native Kernel tries to make knowledge architecture survive technological replacement without pretending that preservation happened when the evidence says otherwise.

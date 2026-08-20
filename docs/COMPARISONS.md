# 🆚 Native Kernel — comparison notes

**Document role:** human-facing, non-authoritative comparison surface  
**Last source check:** 2026-08-14  
**Current-state authority:** this file does **not** define Native Kernel runtime, Canon, H11 admission, or production state.

## Why this document exists

Native Kernel overlaps with memory, retrieval, graph, and history-preservation systems, but it is not trying to replace all of them.

This comparison asks a narrower question:

> **What architectural problem is each approach primarily trying to solve, and which obligations are explicitly part of its public design target?**

It is **not a leaderboard** and must not be used to claim that Native Kernel is universally “better”.

## How to read the matrix

- ✅ — an explicit property of the cited architecture or pattern.
- 🟢 — strong support in the cited public positioning, with scope caveats.
- 🟡 — conditional, component-dependent, or adjacent to the criterion rather than a formal invariant.
- 🛡 — Native Kernel design target; **not** a claim of universal proof.
- 🎯 — explicit Native Kernel research goal / boundary.

Absence language is deliberately conservative. “Not a declared contract” does **not** mean “impossible”.

## Comparison matrix

| Criterion | 🧬 Native Kernel | 🧠 Letta / MemGPT | 🕸 Graphiti | 📚 Vector RAG | 📜 Event Sourcing |
|---|---|---|---|---|---|
| **Core entity** | ⚖ Semantic obligations, distinctions and invariants across replaceable profiles | 💭 Stateful agent + persistent / advanced memory | 🔗 Temporal entities, facts, relationships and source episodes | 📄 Retrieved passages / documents represented through a retrieval index | 📝 Domain events in an append-only event stream |
| **Main question** | 🎯 “What meaning must remain valid or explicit when the implementation changes?” | 🤔 “How does an agent preserve and use state / memory over time?” | 🕵️ “What is or was true, and how are entities related through time?” | 🔍 “Which external context is relevant to the current query?” | ⏳ “What changes happened, and how can current state be derived from them?” |
| **Changing the LLM** | 🛡 Model-independence is a design target; current evidence is bounded, not universal proof | 🟢 Letta explicitly describes itself as model-agnostic; exact behavior still depends on the selected model | 🟡 LLMs participate in extraction / reasoning; cross-model semantic equivalence is not the declared contract | 🟡 Generator can change; exact output behavior is not invariant, and retriever/index choices may also change | ✅ The pattern itself is not inherently LLM-dependent |
| **Changing storage / DB** | 🛡 Storage-independence is a design target; semantic obligations sit above a profile | 🟡 Persistent state can use different deployment modes, but storage-equivalence is not the primary public contract | 🟡 Multiple back-end / integration choices exist; equivalent semantics across all back ends are not inferred | 🟡 Index / store is replaceable, but changing embeddings or indexing often requires re-indexing | 🟢 Event-store technology can change if ordering, event meaning and migration semantics are preserved; the pattern still constrains storage design |
| **Temporal focus** | 🕰 Past + present + future lifecycle: validity, lineage, revision, obligations and loss | 🕰 Long-lived agent state across interactions | 📜 Past + present temporal validity with evolving facts | 📖 Current retrieval over an external corpus; time matters only if represented in data / metadata | 🗂 Historical event sequence → current state |
| **Restart / recovery** | 🔄 A conforming implementation should reconstruct durable semantic state and unresolved obligations; the current lab is not universal proof | ✅ Persistent agent state / memory is designed to survive sessions when its backing state persists | ✅ Persisted context graph supports incremental updates; Graphiti does not require complete graph recomputation on every restart | ✅ A persisted index survives restart; conversational / workflow state is outside plain RAG | ✅ State can be rehydrated from the event stream; projections / snapshots can avoid replaying everything from genesis every time |
| **Role in a stack** | 🏛 Semantic-contract / “constitution-like” layer | 🧩 Agent runtime + memory / context layer | 🗺 Temporal context-graph / memory layer | 📇 Retrieval / knowledge-augmentation layer | 📋 Persistence + history architecture pattern |
| **What is intended to survive implementation replacement?** | 🎯 Declared semantic obligations and distinctions — if the replacement conforms; loss must be explicit | 🟡 Agent-memory abstractions can survive model swaps, but exact behavioral equivalence is not guaranteed by the public positioning | 🟡 Stored temporal graph / provenance can persist; extraction behavior may change with components | 🟡 Source corpus can persist; embeddings / index may need regeneration when encoder or indexing semantics change | ✅ Event history can survive implementation changes if event schema / meaning is preserved; business logic is not automatically preserved |

## Why some intuitive shortcuts are intentionally avoided

Several attractive shorthand claims are too strong for a research-facing repository:

- **Letta is not “low resilience to LLM change”**: its current public README explicitly calls the platform model-agnostic. That does not imply identical behavior across models.
- **Graphiti does not generally require rebuilding the graph after restart**: its public README emphasizes incremental updates without complete graph recomputation.
- **A persisted Vector RAG index does not disappear on agent restart**: plain RAG simply does not define the broader conversational / workflow state of an agent.
- **Event sourcing does not require replay from genesis on every request**: materialized views, projections and snapshots are common mechanisms for avoiding full replay.
- **Native Kernel does not claim “everything survives”**: the architecture requires declared semantic obligations to survive a conforming replacement, or requires loss / change to be explicit. Current evidence is bounded.

These corrections make the comparison less dramatic but more defensible.

## What the comparison actually means

### 🧠 Letta / MemGPT

The current Letta repository describes Letta as a platform for **stateful agents** with advanced memory that can learn and improve over time. It also explicitly describes itself as model-agnostic.

Native Kernel can therefore overlap with Letta around long-lived state and memory, while asking a different architectural question: what semantic obligations should remain valid if the agent framework, model, storage profile, or substrate changes?

### 🕸 Graphiti

Graphiti describes itself as a framework for **temporal context graphs for AI agents**. Its public documentation explicitly discusses temporal validity, changing facts, source episodes/provenance, hybrid retrieval, and incremental updates without complete graph recomputation.

That makes Graphiti much closer to Native Kernel than a flat vector store on several dimensions. The difference is scope: Native Kernel treats provenance, uncertainty, revision, loss, authority, and substrate replacement as parts of a technology-neutral contract rather than selecting a temporal graph as the architecture itself.

### 📚 Vector RAG

The original RAG formulation combines parametric model memory with an external non-parametric memory accessed through retrieval. Its primary contribution is retrieval-augmented generation for knowledge-intensive tasks; the original implementation uses a dense vector index and neural retriever.

A vector RAG stack may be useful inside a Native Kernel-compatible system, but retrieval relevance alone does not establish the semantic identity, authority, provenance, lifecycle, or revision obligations of a claim.

### 📜 Event sourcing

The event-sourcing pattern stores the sequence of changes/events as an append-only system of record and can reconstruct/materialize current state from that history. Canonical guidance also emphasizes materialized views and projections because repeated full replay is expensive.

That is useful for auditability and historical reconstruction. Native Kernel deliberately does not equate “there is an event log” with “the knowledge semantics are preserved”: event sourcing can be an implementation/profile mechanism without becoming a universal Kernel law.

### 🧬 Native Kernel

Native Kernel’s declared focus is not a particular memory engine. It asks which semantic distinctions and obligations must survive replacement of implementations and how failure, uncertainty, revision, supersession, retention/loss, provenance, and authority remain explicit.

The current implementation is a **bounded reference laboratory**, not proof that its Python/PostgreSQL/SQLite/event-oriented mechanisms are universal Canon.

## Source ledger

Checked on **2026-08-14** against primary or canonical sources:

| Subject | Source | What it supports here |
|---|---|---|
| Letta / MemGPT | https://github.com/letta-ai/letta | Stateful-agent and advanced-memory focus; current public model-agnostic positioning; persistent/local/self-hosted deployment framing |
| Graphiti | https://github.com/getzep/graphiti | Temporal context graphs, temporal validity, source provenance, incremental updates, no complete graph recomputation requirement, agent retrieval/context focus |
| Retrieval-Augmented Generation | https://arxiv.org/abs/2005.11401 | Original RAG framing: parametric + non-parametric memory, dense vector index, neural retrieval, retrieval-augmented generation |
| Event sourcing | https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing | Append-only event/change history, system-of-record role, rehydration, materialized views/projections, migration/design trade-offs |
| Native Kernel | ../PROJECT_OVERVIEW.md and ../ARCHITECTURE.md | Native Kernel’s own declared architecture, boundaries, and non-claims |

## Maintenance rule

When this comparison changes materially:

1. re-check the external primary sources;
2. update **Last source check**;
3. prefer conditional / scoped language over unsupported “system X cannot do Y” claims;
4. keep the root README matrix compact enough to orient rather than replace this document;
5. keep detailed caveats and the source ledger here;
6. do not convert comparison language into Native Kernel authority, evidence, or current-state claims.

If an external project changes, this document should change. The stable Native Kernel architecture must not depend on a competitor remaining unchanged.

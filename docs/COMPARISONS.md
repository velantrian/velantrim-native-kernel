# 🆚 Native Kernel — comparison notes

**Document role:** human-facing, non-authoritative comparison surface  
**Last source check:** 2026-08-14  
**Current-state authority:** this file does **not** define Native Kernel runtime, Canon, H11 admission, or production state.

## Why this document exists

Native Kernel overlaps with memory, retrieval, graph, and history-preservation systems, but it is not trying to replace all of them.

This comparison asks a narrower question:

> **What architectural problem is each approach primarily trying to solve, and which obligations are explicitly part of its public design target?**

It is **not a leaderboard** and must not be used to claim that Native Kernel is universally “better”.

## Reading the symbols

- ✅ — explicitly central in the cited source or architecture.
- 🟡 — present or adjacent, but not the same architectural target.
- ◻️ — **not identified as a primary declared goal in the cited material**; this does not prove the capability is absent.
- 🔌 — usable as an optional implementation mechanism.
- 🎯 — explicit Native Kernel research goal or boundary.

## Comparison matrix

| Criterion | 🧠 Letta / MemGPT | 🕸 Graphiti | 📚 Vector RAG | 📜 Event sourcing | 🧬 Native Kernel |
|---|---|---|---|---|---|
| **Primary declared focus** | Stateful agents with advanced/persistent memory | Temporal context graphs for AI agents | Retrieval-augmented generation using external non-parametric memory | Persist an append-only sequence of changes/events and derive current state | Preserve declared semantic obligations across replaceable realizations |
| **Agent memory / retrieval** | ✅ Core | ✅ Core retrieval/context function | ✅ Core retrieval function | ◻️ Not the pattern’s primary purpose | 🔌 Optional mechanism rather than the architecture itself |
| **Temporal relations / provenance** | 🟡 Persistent agent state/history; not evaluated here as the same provenance contract | ✅ Explicit temporal validity and provenance to source episodes | 🟡 Retrieved sources can support grounding, but provenance semantics are not the architecture defined by the original RAG formulation | ✅ Historical reconstruction/auditability are central | ✅ Explicit architectural concern |
| **Replaceable implementation surface** | 🟡 Letta publicly describes model-agnostic operation; this is not treated here as proof of cross-substrate semantic equivalence | 🟡 Framework/back-end choices are implementation concerns; no semantic-equivalence claim is inferred here | 🟡 Retriever, index, generator and corpus can vary | 🟡 A reusable architectural pattern, but adoption constrains storage/state design | 🎯 Implementation/profile replacement is an explicit boundary |
| **Substrate-neutral semantic contract** | ◻️ Not identified as a primary declared goal in the cited source | ◻️ Not identified as a primary declared goal in the cited source | ◻️ Not the goal of the original RAG formulation | ◻️ Event history by itself is not presented as a substrate-neutral knowledge-semantics contract | 🎯 Core research goal |
| **Falsification-first architecture** | ◻️ Not identified as a primary declared goal in the cited source | ◻️ Not identified as a primary declared goal in the cited source | ◻️ Not the goal of the original RAG formulation | ◻️ Not the pattern’s primary purpose | 🎯 Core research method |

## What the comparison actually means

### 🧠 Letta / MemGPT

The current Letta repository describes Letta as a platform for **stateful agents** with advanced memory that can learn and improve over time. It also describes itself as model-agnostic.

Native Kernel can therefore overlap with Letta around long-lived state and memory, while asking a different architectural question: what semantic obligations should remain valid if the agent framework, model, storage profile, or substrate changes?

### 🕸 Graphiti

Graphiti describes itself as a framework for **temporal context graphs for AI agents**. Its public documentation explicitly discusses temporal validity, changing facts, source episodes/provenance, and hybrid retrieval.

That makes Graphiti much closer to Native Kernel than a flat vector store on several dimensions. The difference is scope: Native Kernel treats provenance, uncertainty, revision, loss, authority, and substrate replacement as parts of a technology-neutral contract rather than selecting a temporal graph as the architecture itself.

### 📚 Vector RAG

The original RAG formulation combines parametric model memory with an external non-parametric memory accessed through retrieval. Its primary contribution is retrieval-augmented generation for knowledge-intensive tasks.

A vector RAG stack may be useful inside a Native Kernel-compatible system, but retrieval relevance alone does not establish the semantic identity, authority, provenance, lifecycle, or revision obligations of a claim.

### 📜 Event sourcing

The event-sourcing pattern stores the sequence of changes/events as an append-only system of record and can reconstruct/materialize current state from that history.

That is useful for auditability and historical reconstruction. Native Kernel deliberately does not equate “there is an event log” with “the knowledge semantics are preserved”: event sourcing can be an implementation/profile mechanism without becoming a universal Kernel law.

### 🧬 Native Kernel

Native Kernel’s declared focus is not a particular memory engine. It asks which semantic distinctions and obligations must survive replacement of implementations and how failure, uncertainty, revision, supersession, retention/loss, provenance, and authority remain explicit.

The current implementation is a **bounded reference laboratory**, not proof that its Python/PostgreSQL/SQLite/event-oriented mechanisms are universal Canon.

## Source ledger

Checked on **2026-08-14** against primary or canonical sources:

| Subject | Source | What it supports here |
|---|---|---|
| Letta / MemGPT | https://github.com/letta-ai/letta | Stateful-agent and advanced-memory focus; current public model-agnostic positioning |
| Graphiti | https://github.com/getzep/graphiti | Temporal context graphs, temporal validity, source provenance, agent retrieval/context focus |
| Retrieval-Augmented Generation | https://arxiv.org/abs/2005.11401 | Original RAG framing: parametric + non-parametric memory and retrieval-augmented generation |
| Event sourcing | https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing | Append-only event/change history, system-of-record role, materialized state, trade-offs |
| Native Kernel | ../PROJECT_OVERVIEW.md and ../ARCHITECTURE.md | Native Kernel’s own declared architecture, boundaries, and non-claims |

## Maintenance rule

When this comparison changes materially:

1. re-check the external primary sources;
2. update **Last source check**;
3. prefer “not identified as a primary declared goal” over unsupported claims that another system “cannot” do something;
4. keep the root README summary short;
5. do not convert comparison language into Native Kernel authority, evidence, or current-state claims.

If an external project changes, this document should change. The stable Native Kernel architecture must not depend on a competitor remaining unchanged.

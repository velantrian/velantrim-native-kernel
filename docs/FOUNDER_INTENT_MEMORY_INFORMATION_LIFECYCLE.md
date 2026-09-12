# 🌱 Founder Intent — Memory and Information Lifecycle

> **Status:** `HISTORICAL ORIGIN + LONG-HORIZON RESEARCH INTENT · DOCS_ONLY · NON-CANONICAL`
> **Runtime / implementation / Final Canon authority:** `NONE`
> **Purpose:** preserve the original problem statement that motivated Native Kernel without turning one present-day mechanism into the definition of memory.

## 1. Original intent

Native Kernel was conceived as a **technology-neutral / substrate-neutral architecture for memory and work with information**.

The original idea was broader than durable storage. It covered the full memory/information lifecycle:

```text
experience / source / observation
        ↓
what should be preserved
        ↓
how it is represented with provenance, time, uncertainty and relations
        ↓
how relevant information is retrieved / reconstructed / qualified
        ↓
how the retrieved material is prepared for downstream use
        ↓
how new accepted information, revisions and relationships are written back
        ↓
how the lineage of that change remains inspectable
```

The architecture should therefore remain able to express questions such as:

- What is being remembered: fact, claim, observation, state, relation, decision, uncertainty, or history?
- Where did it come from, and how was it transformed?
- What is current, historical, superseded, unresolved, rejected, or unknown?
- How can information be retrieved without equating retrieval score with truth or authority?
- How should relevant material be related, compared, revised, or carried forward?
- How can new information be persisted without losing the path by which it became accepted, disputed, or replaced?
- Which semantic obligations should survive if the implementation technology changes completely?

## 2. Retrieval belongs to the research intent without becoming one fixed algorithm

Native Kernel does **not** canonize BM25, vector search, graph traversal, SQL queries, RAG, a cross-encoder, an LLM judge, or any other retrieval mechanism.

But this does not mean retrieval is outside the research intent.

The durable question is:

> **What must remain true about selection, reconstruction, applicability, provenance, uncertainty, omission and write-back when different retrieval mechanisms are substituted?**

A retrieval algorithm is an implementation profile. The semantic obligations around what was selected, why it was selected, what was not established, what source and scope apply, and what may be written back are architectural research questions.

```text
retrieval mechanism ≠ retrieval semantics
retrieved ≠ relevant
relevant ≠ evidence
selected ≠ true
not retrieved ≠ absent
model output ≠ state authority
```

## 3. Neutrality means the concept must outlive current machinery

Graphs, SQLite/PostgreSQL, vector databases, embeddings, event logs, files, LLMs, current CPU/GPU systems and future storage engines can all be useful profiles or laboratories.

None of them should become the permanent definition of memory.

The project should remain open to mechanisms that are not yet practical or even fully known today, including future computational substrates and different ways of representing, retrieving, relating or revising information. Unknown mechanisms may be preserved as explicit research questions; they must not be presented as implemented capabilities.

## 4. Ownership boundary after later project separation

The broader Velantrim research program later separated responsibilities:

- **🧬 Native Kernel** owns memory / epistemic-history / retrieval-and-revision semantic obligations at the technology-neutral level.
- **🌀 Mentaury Soul** owns cognition, self/identity, goals, values, feelings, deliberation, learning and the use of memory inside an evolving individuality.
- **🪁 Mentaury-Kernel** owns technology-neutral composition rules for meaning crossing domain boundaries without silent authority transfer or provenance loss.

This separation refines ownership; it does not erase the original Native Kernel intent.

## 5. Non-claims

```text
FOUNDER INTENT ≠ FINAL CANON
MEMORY LIFECYCLE ≠ EVENT-SOURCING REQUIREMENT
RETRIEVAL SEMANTICS ≠ ONE RETRIEVAL ALGORITHM
GRAPH USE ≠ GRAPH REQUIREMENT
SQLITE USE ≠ SQLITE REQUIREMENT
FUTURE SUBSTRATE HORIZON ≠ CURRENT SUPPORT CLAIM
DOCS-ONLY RECONCILIATION ≠ RUNTIME AUTHORIZATION
```

This document records origin and long-horizon research intent only. Existing architecture gates, evidence requirements, runtime freeze, and Final Canon procedures remain unchanged.

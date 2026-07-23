# ADR-0001: Separate Architecture Canon from Implementation Profiles

- **Decision status:** `ACCEPTED`
- **Evidence level:** `DOCUMENTED` + `OPERATOR_APPROVED`
- **Implementation status:** documentation `COMPLETE`; cross-profile portability `NOT_STARTED`
- **Date:** `2026-07-23`
- **Deciders:** `@velantrian`
- **Track:** `Architecture Canon`
- **Related:** `ARCHITECTURE.md`, `STATUS.md`, `ROADMAP.md`, `docs/LONG_HORIZON_VISION.md`
- **Tags:** `portability, canon, adapters, future-substrates`

## Context 🧭

Velantrim Native Kernel is intended as a long-horizon architecture blueprint rather than a permanent commitment to a particular 2026 technology stack.

Contemporary technologies are useful for implementation and testing, but database schemas, graph engines, vector indexes, model APIs, programming languages, runtimes, and processor assumptions must not silently become the semantic definition of memory.

The project must also avoid the opposite error: claiming arbitrary future-hardware portability without implementation evidence.

## Decision drivers 🎯

- preserve semantic identity across technology replacement;
- permit practical implementation using current tools;
- prevent accidental backend lock-in;
- keep architecture claims separate from runtime evidence;
- support future migration and cross-profile comparison;
- maintain explicit epistemic and integration boundaries.

## Considered options 🧪

### Option A — Define the architecture through the current Python/SQLite prototype

**Advantages**

- simple and concrete;
- directly executable with current tools.

**Disadvantages**

- backend schemas become semantic authority;
- replacing storage or runtime may require architectural redesign;
- processor and model assumptions become hidden dependencies.

### Option B — Reject contemporary technologies until a future substrate exists

**Advantages**

- avoids immediate technology coupling.

**Disadvantages**

- prevents testing;
- converts architecture into unexecutable philosophy;
- provides no evidence that contracts are coherent.

### Option C — Separate Canon, Abstract Contracts, and Implementation Profiles

**Advantages**

- current tools remain usable;
- architecture can be evaluated through multiple profiles;
- technology-specific constraints remain visible;
- future portability can be tested rather than merely asserted.

**Disadvantages**

- requires disciplined documentation;
- semantic equivalence must be explicitly defined;
- multiple profiles increase testing and migration cost.

## Decision ✅

**We will:**

Maintain three distinct layers:

```text
Architecture Canon
→ Abstract Contracts
→ Replaceable Implementation Profiles
```

Modern technologies are valid laboratory instruments. They do not become permanent Canon merely because the first prototype uses them.

A new implementation profile is acceptable only when it preserves or explicitly translates the declared contracts for identity, history, reduction, provenance, time, conflict visibility, and Receipts.

**We will not:**

- define Claim identity solely through database-generated IDs;
- define truth through graph edges, embeddings, or retrieval ranking;
- define the event model solely through one SQL schema;
- reject modern technology as unusable;
- claim arbitrary future-substrate portability without cross-profile evidence.

### One-line rationale

> To preserve memory meaning across technological change while still allowing executable research today, we separate durable semantic Canon from abstract contracts and replaceable implementation profiles, accepting additional documentation and equivalence-testing cost.

## Consequences 📌

### Positive

- the architecture can outlive one storage engine or model provider;
- current Python/SQLite/FTS/Graph/Vector tools remain usable;
- technology-specific assumptions become reviewable;
- migration and portability gain explicit evaluation targets.

### Negative / accepted trade-offs

- architecture and runtime statuses require careful separation;
- profile adapters must be tested for semantic parity;
- future substrates cannot be claimed compatible until demonstrated.

## Invariants 🔒

1. Current processor and hardware assumptions belong to an implementation profile, not the Canon.
2. Backend-generated identifiers must not become the only semantic identity of a Claim.
3. Replacing storage, retrieval, models, runtime, or hardware must not silently change epistemic meaning.
4. Technology independence remains a research hypothesis until demonstrated across multiple profiles.
5. Speculative future substrates are research possibilities, not implementation evidence.
6. Current technologies may be used fully without becoming permanent architectural dependencies.

## Architecture-layer placement

| Question | Answer |
|---|---|
| Architecture Canon changed? | `yes` |
| Abstract contract changed? | `yes` |
| Implementation profile selected? | `no permanent profile` |
| Runtime code exists? | external prototype only |
| Production evidence exists? | `no` |

## Validation and evidence 🧪

Current evidence is documentary and operator-approved.

Future evidence should include:

- replay through at least two storage adapters;
- rebuild of projections from the same authoritative history;
- comparison of identity, lineage, temporal meaning, conflict visibility, and Receipt semantics;
- documented differences and failure cases;
- migration and rollback tests.

## Rollback / supersession

This ADR may be superseded if research demonstrates that the three-layer distinction is incoherent or insufficient. The reasons and evidence must remain visible in the superseding ADR.

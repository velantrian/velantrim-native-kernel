# 📖 Native Kernel Glossary

**[English](./GLOSSARY.md) · [Русский](./GLOSSARY.ru.md)**

> This glossary is an onboarding aid. Architecture Canon, accepted ADRs and normative contracts remain authoritative when a compact definition omits detail.

## Core semantic terms

| Term | Compact definition | Important boundary |
|---|---|---|
| **Claim** | An immutable semantic content unit with a declared role, stable identity and provenance fields; roles may include proposition, observation, measurement, interpretation, hypothesis, question or explicit unknown. | A Claim is not automatically true, current, authorized, or conflict-free. |
| **Claim identity** | Deterministic identity derived under a versioned canonicalization contract. | Identity equality does not prove truth or source authenticity. |
| **Content hash** | A versioned digest of canonical semantic content. | Equal hashes mean equal canonical bytes under the declared contract, not equal real-world origin. |
| **Lineage** | A stable continuity relation used to connect revisions or related semantic history. | Lineage is not identity, ownership, personhood, or causal proof. |
| **Event** | An append-only record of an admitted state transition request, such as `ADMIT`, `LINK`, `UTILIZED`, `SUPERSEDED`, or `ERASED`. | An Event records what the system accepted as history; it is not direct reality. |
| **Event Envelope** | The versioned structure containing identity, order, actor/authority, time, payload and hash-chain commitments. | A valid envelope does not make its payload true. |
| **Reducer** | A deterministic function that reconstructs semantic state from ordered Events. | Reducer v1 is historically stable; stricter referential rules are only proposed in ADR-0024. |
| **Semantic State** | The deterministic reducer result for a declared reducer version. | The current runtime state is not yet a complete executable epistemic model. |
| **Epistemic State** | The architecture-level representation of what is supported, disputed, unknown, restricted, superseded or otherwise bounded. | `NK-EPI` remains `0/8 SUPPORTED`; do not describe the full epistemic layer as implemented. |
| **Unknown** | An explicit absence of a justified answer or resolved state. | Unknown is not false, rejected, erased, unavailable, or unsupported. |
| **Conflict Set** | A deliberately preserved group of incompatible or disputed Claims. | Conflict lifecycle is architectural/contract work; current reducer v1 does not construct a complete Conflict Set runtime. |
| **Superseded** | A recorded relation stating that one Claim has a declared successor. | Superseded is not erased, false, physically deleted, or automatically conflict-resolved. |
| **Erased** | A semantic Event/state marker within the current bounded implementation. | It does not prove physical, cryptographic, backup-wide or globally complete deletion. |
| **Relation / Link** | A typed semantic connection between Claims. | A relation label does not by itself prove causality, symmetry, transitivity or acyclicity. |

## Storage, replay and evidence

| Term | Compact definition | Important boundary |
|---|---|---|
| **Architecture Canon** | Technology-independent invariants that implementations must preserve. | Python, SQL, JSON, current processors and current databases are not Canon. |
| **Abstract Contract** | A versioned, testable obligation independent of one implementation profile. | Documentation alone is not implementation or evidence. |
| **Implementation Profile** | A concrete realization of accepted contracts, currently PostgreSQL and SQLite profiles. | A profile may add operational limits but must not redefine semantic meaning. |
| **Authoritative history** | The accepted ordered Event sequence for one Kernel instance. | One instance must not randomly alternate authoritative stores per request. |
| **Replay** | Deterministic reconstruction from authoritative Events. | Replay success does not prove source truth, complete deletion, or production safety. |
| **Projection** | A rebuildable derived view such as tables, indexes, search or graph structures. | A Projection is disposable and must not silently become truth authority. |
| **Receipt** | A bounded auditable record of inputs, decisions, inclusions, exclusions, limits and relevant evidence references. | A Receipt explains a bounded operation; it is not a certificate of ultimate truth. |
| **Provenance** | Recorded source, actor, authority, time and transformation references. | Recorded provenance can be incomplete or fraudulent unless independently verified. |
| **Canonical bytes** | The exact byte representation produced by a declared canonicalization contract. | Canonicalization provides deterministic comparison; it is not injection prevention or authenticity. |
| **Golden vector** | A fixed input with expected byte/digest/identity output for cross-implementation reproduction. | Golden vectors test declared cases, not all possible inputs or future hardware. |
| **Evidence bundle** | Repository-retained artifacts, manifests and hashes tied to exact producing runs and commits. | Retention does not broaden evidence beyond the producing checkpoint or create independent custody. |

## Governance and maturity

| Term | Compact definition | Important boundary |
|---|---|---|
| **Decision status** | Whether a proposal is `PROPOSED`, `ACCEPTED`, rejected or otherwise governed. | Acceptance is operator approval, not proof of implementation. |
| **Implementation status** | Whether code exists in a declared scope at an exact SHA. | Implemented does not automatically mean tested, wired, enabled or observed. |
| **Evidence level** | The bounded reproduction/evaluation stage such as C2, C3, C4 or C5. | A higher label does not erase explicit unsupported assertions. |
| **C3** | Cross-profile comparison within declared byte, structural, semantic and behavioural classes. | C3 is not operational equivalence or proof of arbitrary substrate neutrality. |
| **C4** | Offline shadow evaluation on a bounded recorded workload. | C4 is not live production shadowing or authority promotion. |
| **C5** | Bounded synthetic operational rehearsal under a declared plan and matrix. | C5 is not production readiness, live traffic, compliance or multi-region reliability. |
| **Track H** | Historical recovery of reported `v0.1.2.1` and its original test suite. | Clean implementation does not claim to be recovered historical source. |
| **Track C** | Clean implementation lineage for current contracts and profiles. | Track C does not resolve Track H authenticity. |
| **Track R** | Long-horizon research proposals. | Research text is not Canon, accepted decision or runtime authorization. |
| **Operator approval** | Explicit maintainer authorization for a decision or promotion. | AI agreement, review comments and passing tests do not substitute for operator authority. |

## Non-equivalences to preserve

```text
Claim              ≠ truth
Event              ≠ reality
Identity           ≠ authenticity
Lineage            ≠ personhood
Unknown            ≠ false
Superseded         ≠ erased
Projection         ≠ authority
Receipt            ≠ truth certificate
Canonicalization   ≠ security validation
Repository evidence ≠ independent custody
C3                 ≠ operational equivalence
C4                 ≠ live production shadow
C5                 ≠ production readiness
Public repository  ≠ open-source license
Research proposal  ≠ accepted contract
Accepted ADR       ≠ implemented runtime
```

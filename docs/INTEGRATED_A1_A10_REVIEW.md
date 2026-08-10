# Integrated A1–A10 Blueprint Review

**State:** `COMPLETED / PROVISIONAL / OPERATOR_DECISION_PENDING`  
**Review identity:** `nk-integrated-blueprint-review/A1-A10-review-1`  
**Architecture phase:** ADR-0025 / Issue #88  
**Reviewed inventory:** A1–A10 first-draft blueprint  
**Next gate:** `OPERATOR_POST_BLUEPRINT_DECISION`  
**Runtime expansion:** `FROZEN`

## 1. Purpose and authority boundary

This review evaluates A1–A10 as one architecture rather than as ten isolated documents. It checks terminology, dependency direction, semantic non-equivalences, contradictions, duplicate concepts, implementation capture, laboratory mapping, falsifiability, and the boundary between architecture research and operator authority.

This is a repository-integrated review pass. It is **not independent validation**: the same project/operator lineage produced the drafts and this reconciliation. It is also not operator acceptance, Canon promotion, runtime authorization, production authorization, or proof of arbitrary-substrate portability.

The first-draft A1–A10 files remain preserved as historical drafted slices. Where this review identifies a conflict, the explicit reconciliation decisions in §4 are the current provisional interpretation for the integrated blueprint. This avoids silently rewriting historical draft wording.

## 2. Dependency-chain assessment

The intended chain is coherent:

```text
A1 purpose / non-goals
→ A2 meaning-level ontology
→ A3 obligation-and-transition machine
→ A4 semantic laws / non-collapse invariants
→ A5 identity / time / change
→ A6 lifecycle positions / accountable transitions
→ A7 conflict / uncertainty / revision
→ A8 substrate mapping / conformance
→ A9 reference-laboratory classification
→ A10 open hypotheses / falsification
→ this integrated review
```

No reviewed later slice requires Python, PostgreSQL, SQLite, SQL, JSON, SHA-256, Event sourcing, reducer replay, global integer sequence, LLMs, embeddings, or one processor model as universal Canon. Current P1–C5 mechanisms remain bounded laboratory realizations and evidence instruments.

## 3. Cross-slice consistency results

### 3.1 Representation and epistemic boundaries — coherent

A1’s technology-neutral purpose, A2’s Observation/Claim/Evidence/Source distinctions, A4-L01…L10, A7 uncertainty rules and A8 mapping states consistently reject representation-as-reality and unknown-as-false collapse.

### 3.2 Identity, time and ordering — coherent

A4-L11…L19, A5 typed identity relations and temporal dimensions, A6 lifecycle order, and A8 portability rules consistently preserve:

```text
semantic identity ≠ storage identity
write order ≠ occurrence order ≠ causal order
Revision ≠ overwrite
Supersession ≠ deletion or falsity
```

### 3.3 Conflict, uncertainty and revision — coherent after terminology reconciliation

A2/A4/A7/A8/A10 consistently preserve unresolved plurality, scoped Authority, detection ≠ resolution, and uncertainty ≠ one universal confidence scalar. IR-F03 and IR-F04 below remove wording/protocol ambiguity at the integrated layer.

### 3.4 Substrate independence — coherent but unproved

A1/A3/A8/A9/A10 consistently define substrate independence as a specification and conformance discipline, not a claim that every substrate can implement the Kernel. PostgreSQL↔SQLite C3 remains narrow same-language storage-profile evidence.

### 3.5 Laboratory boundary — coherent

A9 correctly prevents implementation capture while preserving reproducibility and evidence lineage. No reviewed laboratory mechanism becomes universal Canon merely because it exists or passes CI.

## 4. Integrated findings and explicit reconciliation decisions

### `IR-F01` — Physical deletion and cryptographic erasure were collapsed in A6

**Severity:** material semantic inconsistency.  
**Source:** A5 explicitly states `physical deletion ≠ cryptographic erasure`; A6 first draft combines them as `PHYSICALLY_OR_CRYPTOGRAPHICALLY_ERASED`.

**Integrated correction:** the current provisional blueprint uses **four** closure meanings:

```text
LOGICALLY_ERASED
PHYSICALLY_ERASED
CRYPTOGRAPHICALLY_ERASED
FORGOTTEN_OR_LOST
```

- `LOGICALLY_ERASED` — ordinary semantic/operational availability is withdrawn under declared scope; physical residue may still exist.
- `PHYSICALLY_ERASED` — the relevant physical carrier/state is destroyed, overwritten, or altered beyond the declared recovery boundary under a named physical method and observation scope. If residue cannot be inspected adequately, the stronger claim remains `INDETERMINATE`.
- `CRYPTOGRAPHICALLY_ERASED` — required cryptographic secret/key material is destroyed under a named method and declared cryptographic assumptions so protected content is computationally inaccessible for the stated threat/scope. This does **not** assert that physical ciphertext/residue was removed.
- `FORGOTTEN_OR_LOST` — material is not reconstructible from the declared accessible-source boundary, without implying deliberate erasure, universal loss, or non-existence.

The original combined A6 token is retained only as historical first-draft wording and must not be used as the current integrated closure taxonomy.

### `IR-F02` — A6 required a named erasure method for every closure kind

**Severity:** internal contradiction.  
**Source:** A6 allows `FORGOTTEN_OR_LOST` without a recorded deliberate erasure method, but later says a closure kind without a named method is invalid.

**Integrated correction:** every closure claim needs a named **basis/assessment/observation method and scope**. Only deliberate `PHYSICALLY_ERASED` and `CRYPTOGRAPHICALLY_ERASED` claims additionally require a named erasure method. `FORGOTTEN_OR_LOST` may result from accidental or unexplained loss and therefore does not require a deliberate erasure method.

### `IR-F03` — A1 foundational question used “confidence attached” too broadly

**Severity:** terminology drift, non-blocking once reconciled.  
**Source:** A1 asks about “the confidence attached” to a Claim, while A7 establishes `uncertainty ≠ one universal confidence scalar` and model confidence ≠ Evidence.

**Integrated correction:** read the A1 research question as referring to the **uncertainty and epistemic position associated with the Claim**, not to a mandatory confidence scalar or field. Any profile-specific confidence value is only one possible input/representation and has no automatic epistemic authority.

### `IR-F04` — A10 hypothesis table used labels outside its five-outcome protocol

**Severity:** protocol vocabulary inconsistency.  
**Source:** A10 defines exactly `SUPPORTED_FOR_SCOPE / WEAKENED / REFUTED / INDETERMINATE / NOT_TESTED`, but first-draft table cells also use `PARTIALLY_SUPPORTED` and `OPEN / INDETERMINATE`.

**Integrated correction:** A10’s machine/review outcome vocabulary is exactly the five declared outcomes. Contextual evidence notes do not create new states.

Normalized current interpretations:

- `A10-H03`: `NOT_TESTED` across independent representation/substrate migrations; current same-lineage mappings are contextual prior evidence only.
- `A10-H06`: `INDETERMINATE`; the problem remains open.
- `A10-H10`: `NOT_TESTED` for independently varying storage and computation axes; P5 provides storage-only contextual evidence.
- `A10-H11`: `SUPPORTED_FOR_SCOPE` only for the governance discipline that reproducible laboratory mechanisms can remain non-Canon; it is not substrate evidence.

### `IR-F05` — Erasure observability needed explicit physical/cryptographic separation

**Severity:** clarification needed for A8/A10 consistency.

**Integrated correction:** physical and cryptographic erasure are separate claims with separate observables. Lack of physical-residue visibility keeps physical-erasure claims `INDETERMINATE`; cryptographic erasure requires evidence about key/secret destruction plus stated cryptographic assumptions and threat boundary, and never implies physical deletion.

### `IR-F06` — “Conflict visibility” must not imply every tension is a Contradiction

**Severity:** terminology clarification.

**Integrated correction:** A1’s durable-quality statement about contradiction is interpreted more generally as **material tension/conflict visibility**, with `Contradiction` only one A7 tension kind after alignment. A conflict may remain unresolved, dissolve after scope/time alignment, or be handled for scope without either side becoming false.

### `IR-F07` — Lifecycle wording must remain non-linear and non-mandatory

**Severity:** wording clarification.

**Integrated correction:** A6 phases are recurring positions that an item **may occupy**, possibly concurrently under different identity relations. They are not mandatory stages that every item “passes through,” and no requirement exists for eventual progression or closure.

## 5. Duplicate-concept assessment

The review found deliberate overlap but no remaining known duplicate that requires a second competing ontology:

- A2 defines concepts; A4 constrains silent collapse of those concepts.
- A3 defines transition families; A6 defines lifecycle positions/relations over them.
- A5 defines identity/time/change; A7 uses those relations for conflict/revision.
- A8 defines preservation/conformance; A9 classifies current mechanisms against it.
- A10 defines falsification/open questions; it does not replace P4 assertion states or A8 conformance states.

The integrated review therefore does not merge these layers into one document or one universal state machine.

## 6. Implementation-capture audit

The following remain profile/laboratory mechanisms, not architecture requirements:

- Python classes/runtime;
- PostgreSQL/SQLite/SQL;
- current Event verbs/envelope;
- reducer v1 and replay shape;
- SHA-256 and current ID/hash prefixes;
- global/stream integer sequences;
- current Receipt encoding;
- GitHub Actions and evidence ZIP packaging.

Architecture-level obligations are the preserved meaning, identity/lineage, scope/provenance/Authority, explicit uncertainty/loss, accountable change, and scoped conformance behavior described across A1–A10.

## 7. Falsification coverage assessment

A10 provides at least one weakening/refutation condition for each major hypothesis and explicit stop conditions. The important unresolved hypotheses remain genuinely unresolved:

- independent computation-model preservation;
- non-event-sourced minimum history/accountability;
- lossy/bounded-memory accountability;
- analog/neuromorphic persistence and lineage;
- probabilistic conformance;
- independent-language/team/custody evidence thresholds;
- physical/cryptographic erasure observability;
- decentralized Authority;
- non-classical/quantum mapping;
- self-modifying realization continuity.

No absence of evidence is promoted to support.

## 8. Current contracts and reference laboratory

Accepted/versioned contracts and P1–C5 evidence remain historically valid within their declared scope. This review does not retroactively rewrite them. Where an accepted contract mixes architecture-level meaning with profile mechanism, later work may split or map layers explicitly, but only through a separate decision and without relabelling historical evidence.

Issue #14/#15/#16/#17 retain their existing scopes. Issue #18 and Issue #74/ADR-0024 remain operator-controlled. ADR-0003 remains proposed/not started. Track H source admission remains operator-controlled.

## 9. Review conclusion

After the explicit reconciliation decisions in §4:

- **no known blocking internal semantic contradiction remains across A1–A10** in this review pass;
- terminology/dependency direction is coherent enough to present the blueprint to the operator;
- unresolved research remains explicit rather than “closed” by documentation;
- the reference laboratory remains bounded and does not capture Canon;
- substrate independence remains a falsifiable architecture hypothesis, not universal portability proof.

This conclusion is provisional and not independent validation. A later independent reviewer may weaken, reject, split, or reopen any finding or draft assumption.

## 10. Next gate and hard stop

```text
A1–A10 drafting: COMPLETE / PROVISIONAL
integrated A1–A10 review: COMPLETE / PROVISIONAL
independent architectural validation: NOT ESTABLISHED
next gate: OPERATOR_POST_BLUEPRINT_DECISION
runtime expansion: FROZEN
reference laboratory: BOUNDED_REFERENCE_LABORATORY
production authorization: false
```

The operator must separately decide what, if anything, follows. This review does not choose among possible next phases and does not authorize runtime thaw, contract promotion, new implementation profiles, licensing, reducer-v2, or production work.

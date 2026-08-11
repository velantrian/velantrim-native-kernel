# BPV-1 — Cross-Lineage Bounded-Accountability Preregistration

**[English](./BPV1_PREREGISTRATION.md) · [Русский](./BPV1_PREREGISTRATION.ru.md)**

> **Protocol:** `nk-bpv1-preregistration/1`  
> **Scenario:** `BPV1-001-cross-lineage-bounded-accountability-v1`  
> **Status after authoritative merge:** `PREREGISTERED / EXECUTION_NOT_AUTHORIZED`  
> **Role:** `FALSIFICATION_INSTRUMENT_ONLY`  
> **Architecture checkpoint:** `c5d76fe281606edc0053bd7fc65167ebdfa50992`  
> **Runtime expansion:** `FROZEN`

## 1. Purpose

BPV-1 is not another Native Kernel runtime. It is a bounded attempt to make the provisional architecture fail.

This scenario asks a deliberately narrow question:

> Can the reconciled minimum Native Kernel obligations survive a materially different, single-node realization that is written in a non-Python language, does **not** use Event sourcing as its authoritative history model, and keeps retained durable experimental state bounded while preserving declared accountability and loss semantics?

A successful run would provide stronger evidence than PostgreSQL↔SQLite inside one Python lineage, but it would **not** prove universal substrate independence, independent team/custody, future hardware support, Final Canon, production readiness, or product-runtime suitability.

The primary A10 targets are `A10-H02` and `A10-H05`; secondary targets are `A10-H01`, `A10-H04`, `A10-H07`, and `A10-H12`. The scenario is also intended to produce concrete evidence for `A10-Q01`, `Q02`, `Q04`, `Q10`, `Q13`, `Q14`, and `Q18`.

## 2. Experimental lineage boundary

The planned subject realization is an **experimental Rust instrument**.

Rust is selected only to create a materially different implementation-language lineage. It is not a Canon requirement and does not become a product profile by being used here.

The realization must independently derive its state/change/history representation from the problem-level obligations in this preregistration. It may **not**:

- depend on `native_kernel/**` as runtime code;
- translate the current Python domain classes mechanically;
- reuse the current Event envelope as its native history representation;
- reuse the current reducer as its semantic engine;
- use the current SQL schema as its native state shape;
- treat the current Receipt shape as the conformance oracle;
- require exact replay or a global total order merely because the laboratory does.

The intended state model is a bounded current-state representation plus lineage summaries and explicit loss witnesses. An authoritative per-operation append-only Event log is prohibited. A small bounded crash journal is allowed only as a recovery mechanism, capped at eight entries, and may not define semantic history.

The implementation remains conventional digital computation and remains in the same repository custody. Independent team/custody and an independent computation model are **not established** by BPV1-001.

## 3. Frozen workload

The bounded-memory workload is fixed before implementation:

```text
active claim slots: 32
revision cycles: 16
scripted mutations: 512
measurement checkpoints: 128 / 256 / 512 mutations
compaction: after every revision cycle
durable experimental-state cap: 262,144 bytes
retained detailed predecessors: <= 64
loss witnesses: <= 32
authoritative per-operation append log: forbidden
bounded crash journal: <= 8 entries; not semantic Authority
```

“Bounded memory” in this scenario means **bounded retained durable experimental semantic state**, not process RSS or allocator behavior.

At the final checkpoint:

```text
durable_bytes_at_512 <= durable_bytes_at_256 * 1.25 + 4096
```

This is a scenario threshold, not a universal Native Kernel law.

## 4. Exact preregistration fields

The following twelve fields are normative. They correspond exactly to the IAR-1-R1 preregistration inventory. Any post-execution change to a normative field invalidates the run for the claimed scope and requires a new scenario identity.

### 4.1 `scenario_id`

`BPV1-001-cross-lineage-bounded-accountability-v1`

### 4.2 `purpose_scope`

Single-node, non-composed, conventional-digital falsification scenario. It tests cross-language + different history/state-model preservation only.

Explicit non-claims:

- no production-readiness claim;
- no universal substrate-portability claim;
- no independent-team/custody claim;
- no analog/neuromorphic/probabilistic claim;
- no composition/federation claim;
- no physical/cryptographic-erasure proof;
- no performance-superiority claim;
- no product-runtime suitability claim.

### 4.3 `mandatory_obligations`

The realization must preserve all of the following for the declared scope:

1. Representation or Claim is not silently reality/objective truth.
2. Material Context, warrant/provenance, and scoped Authority assumptions remain inspectable without requiring the current Python field layout.
3. Unknown, uncertainty, and unsupported remain representable without coercion to False or fabricated certainty.
4. Revision, supersession, retention, and loss remain accountable for the declared retained scope without silent overwrite.
5. Equivalence, degradation, and loss are classified by the preregistered oracle, not implementation self-report.
6. `CURRENT_ACCOUNTABILITY` remains available for every retained active claim slot.
7. `DECLARED_RETENTION_SCOPE` is explicit and machine-observable.
8. `LOSS_WITNESS` exists whenever detail is compacted outside retained scope.
9. Unresolved plurality remains representable when no preregistered Authority rule selects a winner.
10. These obligations must be met without a canonical per-operation Event log or exact replay as authoritative history.

### 4.4 `applicability_rules`

Applicable:

- single-node / non-composed;
- bounded durable semantic state;
- non-event-sourced authoritative history;
- independent implementation language: Rust.

Declared limitations:

- same repository custody;
- independent team not established;
- independent computation model not established;
- only identity/time dimensions named by a fixture are mandatory.

`NOT_APPLICABLE` with preregistered rationale:

- physical erasure — no independently observable physical-erasure channel;
- cryptographic erasure — no key-destruction substrate claim;
- composition/federation — separate capability class;
- exact replay and global total order — not universal requirements in this scenario.

Changing applicability after execution begins invalidates the run for the claimed scope.

### 4.5 `mandatory_observables`

The external evaluator must be able to observe, without implementation-private semantic authority:

- current claim/proposition state and epistemic position;
- material Source/Evidence/Provenance/Authority distinctions where a fixture requires them;
- Context binding;
- retained revision/supersession relation;
- declared retention scope;
- bounded loss witness after compaction;
- unresolved plurality where no winner is authorized;
- explicit `LOSSY`, `UNSUPPORTED`, and `INDETERMINATE` outcomes;
- durable state size and retained detail/witness counts at 128/256/512 mutations;
- whether an authoritative per-operation append log exists;
- rollback/truncation and forged-Authority failure semantics;
- evaluator-owned conformance result.

### 4.6 `equivalence_predicates`

The machine-readable plan freezes predicates `EQ01`–`EQ10`.

Key rule: semantic equivalence is scoped and meaning-level. Matching bytes, IDs, storage layout, write sequence, Event envelope, reducer state, Receipt bytes, or SQL schema are neither required nor sufficient.

Full conformance is forbidden when visible final values match but material provenance, Authority, Context, uncertainty, or declared-loss semantics differ.

### 4.7 `allowed_declared_losses`

The scenario permits explicit loss of:

- exact bytes/storage addresses of superseded detail outside retained scope;
- per-operation write chronology outside retained accountability scope;
- exact replay;
- native A3 transition and A6 lifecycle representations;
- current Event/reducer/Receipt/SQL/ID/hash forms;
- A5 identity/time dimensions not named by a fixture;
- superseded detail after compaction, **only** with a valid bounded `LOSS_WITNESS`;
- bounded crash-journal entries after recovery, provided they are not semantic history.

No loss inside the declared retained accountability scope may be silent.

### 4.8 `failure_thresholds`

There is no score averaging for semantic failures.

```text
semantic hard failures allowed: 0
mandatory fixture failures allowed: 0
Unknown→False coercions allowed: 0
silent retained-scope losses allowed: 0
unauthorized conflict-winner selections allowed: 0
material role collapses allowed: 0
authoritative per-operation append log: forbidden
durable state cap: 262,144 bytes
retained detailed predecessors: <= 64
loss witnesses: <= 32
required mutations: 512
required measurement checkpoints: 3
```

If a mandatory observable cannot be evaluated independently, the relevant predicate is `INDETERMINATE`, not PASS.

### 4.9 `hard_refutation_observations`

The plan freezes `HR01`–`HR10`. Among them:

- needing an authoritative unbounded/per-operation Event log to preserve required accountability weakens/refutes `A10-H02` for this scope;
- inability to compact while preserving current accountability, retention scope, and truthful loss witness weakens/refutes `A10-H05`;
- forcing Unknown→False or unresolved plurality→winner refutes `A10-H04` for this scope;
- requiring current A3/A6/Event/reducer/Receipt shape to express the minimum weakens `A10-H01` and invalidates any claim that those structures were independently rediscovered;
- matching final values with materially divergent provenance/Authority/uncertainty/loss semantics refutes full semantic equivalence for that fixture;
- copying the current Python conceptual/runtime structures invalidates the intended `A10-H07` evidence class;
- silent retained-scope loss refutes bounded-accountability conformance;
- silently accepting rollback/truncation/forged Authority refutes the protected meaning involved;
- changing normative rules after execution invalidates the run;
- an oracle that depends on implementation-private self-report makes the run non-qualifying.

### 4.10 `grounding_mode`

`EXPLICIT_ASSUMED_ROOT`.

The BPV1 fixture/oracle package is an explicit experimental root, not objective world truth. Provenance/Authority chains terminate at that root or at `TERMINAL_UNKNOWN_OR_GAP`; hidden infinite grounding is not permitted.

### 4.11 `threat_model`

Protected meanings:

- declared provenance and scoped Authority basis;
- current accountability within retained scope;
- revision/supersession relation;
- declared retention/loss boundary;
- conformance observations/evidence.

Mandatory adversarial cases include forgery, truncation, rollback, equivocation, withheld counterevidence, unavailable witness, and forged Authority/provenance.

Colluding-witness, compromised external certifier, and physical-residue cases are `NOT_APPLICABLE` for BPV1-001 with explicit rationale in the machine plan.

### 4.12 `oracle_authority`

`BPV1-ORACLE-001`.

After merge, `docs/research/BPV1_PREREGISTRATION.json` is the normative experiment-oracle source for BPV1-001. It is authority **only for this experimental conformance scope**.

The implementation under test may not modify the oracle or define expected results.

Before execution, a separate `BPV1_EXECUTION_ADMISSION` checkpoint must bind:

- this authoritative preregistration;
- its frozen digest;
- a machine-readable fixture/oracle package derived only from this plan;
- standalone evaluator tests passing before subject execution;
- a pinned Rust toolchain and source boundary;
- static proof that the instrument is not integrated into product runtime/profile paths.

## 5. Fixture families

Twelve mandatory fixture families are preregistered:

```text
BPV1-FX01  Unknown ≠ False
BPV1-FX02  role non-conflation
BPV1-FX03  Context binding
BPV1-FX04  revision / supersession
BPV1-FX05  unresolved plurality
BPV1-FX06  bounded compaction + LOSS_WITNESS
BPV1-FX07  truncation / rollback
BPV1-FX08  forged Authority
BPV1-FX09  withheld counterevidence
BPV1-FX10  declared loss / unsupported / indeterminate
BPV1-FX11  non-Event accountability
BPV1-FX12  hidden semantic divergence despite matching final values
```

The execution-admission package may make these fixtures machine-executable, but it may not change their semantic purpose or normative predicates under the same scenario identity.

## 6. A10 outcome discipline

Only these result values are allowed:

```text
SUPPORTED_FOR_SCOPE
WEAKENED
REFUTED
INDETERMINATE
NOT_TESTED
```

`NOT_TESTED ≠ SUPPORTED`.

A positive BPV1 result would strengthen only the tested scope. It would not prove future substrates, universal portability, Final Canon, or production readiness.

## 7. Execution hard stop

Merging this preregistration does **not** authorize D5 execution.

After this plan becomes authoritative, the state must move to:

```text
BPV-1 plan: PREREGISTERED / AUTHORITATIVE
next gate: BPV1_EXECUTION_ADMISSION
BPV-1 execution: BLOCKED_PENDING_EXECUTION_ADMISSION
runtime expansion: FROZEN
product runtime thaw: NO
production: false
```

D5 begins only after a separate admission checkpoint. Any attempt to implement or execute BPV1-001 before that gate is a process failure, not experimental evidence.

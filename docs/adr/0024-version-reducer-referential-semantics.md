# ADR-0024: Version reducer referential semantics without rewriting history

- **Decision status:** `ACCEPTED`
- **Evidence level:** `DOCUMENTED`
- **Implementation status:** `NOT_STARTED`
- **Operator approval:** `APPROVED`
- **Date:** `2026-08-08`
- **Accepted:** `2026-08-22`
- **Deciders:** `@velantrian`
- **Operator decision:** `ACCEPT_WITH_CHANGES`
- **Track:** `Abstract Contract / Clean Implementation`
- **Related:** Issue #74, ADR-0003, ADR-0006, ADR-0012, ADR-0015, PR #72, PR #73
- **Tags:** `reducer, referential-integrity, replay, compatibility, supersession, links`

> [!IMPORTANT]
> ADR-0024 is accepted as an abstract versioning and referential-semantics contract only. Acceptance does **not** authorize reducer-v2 implementation or runtime expansion. `nk-p1-reducer/1` remains immutable in meaning and remains the interpretation contract for published P1-C5 evidence.

## Decision

Select the versioned strict-reducer direction with the operator-selected `ACCEPT_WITH_CHANGES` clarifications below.

```text
published reducer-v1 history
!= silently upgraded reducer-v2 history
```

A future strict reducer uses a distinct contract/version (`nk-p1-reducer/2` is the reserved candidate identifier) and is bound explicitly to a Kernel instance/history. Selection must never be inferred from date, deployment version, database profile, process-global default, or replay under newer software.

Existing histories, projections, Receipts, reports, archives and evidence remain interpreted under reducer v1. A v1 history may be valid under v1 while non-migratable to v2. Existing P1-C5 evidence is not relabelled as reducer-v2 evidence.

## Accepted compatibility boundary

1. `nk-p1-reducer/1` remains readable, replayable and immutable in meaning.
2. Reducer semantics are selected explicitly per Kernel instance/history or equivalent authoritative history boundary.
3. A committed history cannot silently change reducer interpretation.
4. Mixed reducer semantics inside one history are forbidden unless a separately accepted migration contract defines the boundary and replay algorithm.
5. A final projection that resembles a v2 state does not make a v1 history v2-conformant.
6. Reducer-v2 implementation requires a separate authorization after the dependencies and contract surfaces below are complete.

## Accepted reducer-v2 first scope

Reducer v2 is limited to referential semantics for already-authorized Event roles. It does not add or execute a full Admission workflow, truth evaluation, Temporal semantics, typed relation ontology, causal reasoning, operational deletion, distributed multi-writer behavior, or ecosystem authority.

### `ADMIT`

- first valid admission creates the admitted Claim state;
- duplicate identical admission is deterministic and idempotent;
- conflicting admission fails;
- admission of an erased or restricted Claim fails unless a future explicit restoration contract permits it;
- reducer v2 may validate an existing admission decision/reference but does not own the full Admission lifecycle.

### `LINK`

- source and target must already exist and be admitted;
- erased references fail;
- restricted references fail by default unless an accepted contract explicitly authorizes the reference scope;
- identical repeated edges are deterministic no-ops;
- generic self-links and generic graph cycles remain allowed by the base reducer;
- relation-specific topology belongs to a separate typed-relation contract.

### `UTILIZED`

- unknown or erased Claim utilization fails;
- restricted Claim utilization fails by default unless an accepted compatible scope exists;
- historical reporting of prior utilization is a separate role, not current `UTILIZED`;
- utilization is operational history, not epistemic promotion.

### `SUPERSEDED`

- predecessor and successor must exist, be admitted and be referenceable;
- predecessor and successor must differ;
- repeated identical predecessor-to-successor is deterministic and idempotent;
- a different second successor fails; no last-write overwrite;
- self-supersession fails;
- two-node and longer successor cycles fail;
- successor chains such as `A -> B -> C` remain valid;
- supersession does not establish truth.

### `ERASED`

- unknown Claim erasure fails;
- first valid erase moves the Claim to logical-erasure state;
- repeated identical logical erase is deterministic and idempotent while the Event remains in history;
- restriction/retention-held cases follow the accepted deletion-state contract;
- reducer v2 never claims physical or cryptographic deletion.

## Stable failure contract

The following machine-readable failure-code families are accepted for reducer v2 contract finalization:

```text
NK-RED-UNKNOWN-SOURCE
NK-RED-UNKNOWN-TARGET
NK-RED-UNKNOWN-CLAIM
NK-RED-ERASED-REFERENCE
NK-RED-RESTRICTED-REFERENCE
NK-RED-ADMISSION-CONFLICT
NK-RED-SELF-SUPERSESSION
NK-RED-SUCCESSOR-CONFLICT
NK-RED-SUPERSESSION-CYCLE
NK-RED-UNKNOWN-ERASE
NK-RED-REDUCER-VERSION-MISMATCH
NK-RED-ENCODING-PROFILE-MISMATCH
```

Within reducer-v2, rejected histories must expose a stable machine failure surface containing:

```text
failure_code
failure_location
Event index
global_seq, when committed
reducer contract/version
state-before-failure digest
proof boundary
```

Human-readable message text may evolve without changing the stable machine meaning.

## Version/history binding

Minimum declared binding for a reducer-v2 history:

```text
instance_id
reducer_contract
reducer_version
Event contract/version
identity contract
encoding profile
```

The binding must be part of the authoritative history/instance interpretation context rather than a process-local default.

## Migration boundary

The accepted first migration scope is only:

```text
CONTINUE_V1
START_NEW_V2_INSTANCE
ASSESS_V1_MIGRATABILITY
```

Explicitly forbidden in the first scope:

```text
SILENT_V1_TO_V2_UPGRADE
AUTOMATIC_HISTORY_REWRITE
AUTOMATIC_EVENT_TRANSFORMATION
```

Migration assessment may return:

```text
VALID_UNDER_V1_AND_MIGRATABLE
VALID_UNDER_V1_WITH_DECLARED_V2_FAILURES
VALID_UNDER_V1_NON_MIGRATABLE_TO_V2
INVALID_UNDER_DECLARED_V1_CONTRACT
UNDETERMINED
```

`NON_MIGRATABLE_TO_V2` does not invalidate a history that is valid under reducer v1.

## Dependencies before reducer-v2 runtime authorization

Acceptance of this ADR is not implementation authorization. Reducer-v2 runtime remains blocked until a separately reviewable contract-finalization/authorization path establishes:

1. NK-SAM and named equivalence profiles sufficient for the intended cross-profile claim;
2. portable Event/history commitment separated from operational/profile Receipts;
3. reducer, identity, encoding and schema versions inside the declared commitment boundary;
4. stable failure-location semantics;
5. exact positive/negative conformance fixtures and new evidence identity;
6. explicit rollback/migration behavior that cannot reinterpret historical v1 evidence.

These dependencies are gates for reducer-v2 runtime authorization, not authorization to broaden NK-SAM, Event vocabulary, H11, Final Canon or production scope in this ADR.

## Required fixture matrix before runtime authorization

Positive fixtures include first/duplicate admission, valid/duplicate LINK, valid utilization, valid/repeated supersession, valid/repeated logical erase.

Negative fixtures include conflicting admission; missing, erased or restricted LINK references; unknown/erased/restricted utilization; unknown supersession endpoints; self-supersession; successor overwrite; successor cycles; unknown erase; reducer-version substitution; encoding-profile substitution; and cross-profile failure-location disagreement.

PostgreSQL, SQLite and any future independent implementation must preserve equivalent successful state and equivalent rejected-history failure meaning under named profiles. Shared Python code can support profile comparison but does not establish independent implementation neutrality.

## Evidence-lineage boundary

A bounded read-only trace recorded after the original proposal found that current C3 support evidence is materially produced under reducer-v1 permissive referential semantics. This does not show that current supported assertions are false and does not change the existing assertion arithmetic. It means current C3/C4/C5 support is historical reducer-v1-bounded evidence and cannot be silently reused as proof of reducer-v2 semantics. Issue #74 and `docs/ai/KNOWN_RISKS.md` retain the detailed trace.

## Consequences

### Positive

- historical replay/evidence identity remains honest;
- strict future histories cannot silently accumulate the accepted classes of dangling current references;
- supersession gains deterministic conflict/cycle rules;
- generic relation topology remains extensible;
- append/replay can share an explicit versioned contract;
- migration becomes explicit and auditable.

### Costs

- v1 and a future v2 must coexist;
- profiles need explicit reducer-version binding and dispatch;
- some valid v1 histories may be non-migratable;
- relation-specific validity remains outside this reducer contract.

## Invariants

1. Published reducer-v1 history is never replayed under v2 semantics without a separately accepted migration path.
2. Reducer version is authoritative interpretation context, not a process-local default.
3. Strict validation applies during replay as well as append/admission.
4. Referential failure means invalid under the declared reducer contract; it does not prove the represented statement false.
5. Profile technology does not change semantic result.
6. Generic relation topology is not globally declared acyclic by the base reducer.
7. Logical erasure does not rewrite history or claim physical deletion.
8. Existing reducer-v1 evidence remains reducer-v1-bounded evidence.
9. Acceptance does not authorize implementation.
10. H11, Final Canon, runtime thaw and production remain governed by their existing independent gates.

## Architecture-layer placement

| Question | Answer |
|---|---|
| Architecture Canon changed? | `no` |
| Abstract contract changed? | `accepted for ADR-0024 scope` |
| Implementation profile selected? | `no` |
| Runtime code exists? | `no strict reducer` |
| Reducer-v2 runtime authorized? | `no` |
| Production evidence exists? | `no` |

## Operator decision record

```yaml
operator_decision: ACCEPT_WITH_CHANGES
operator: '@velantrian'
decision_date: 2026-08-22
v1_immutability: REQUIRED
v2_instance_history_binding: REQUIRED
duplicate_admit_policy: IDEMPOTENT_NO_STATE_CHANGE
restricted_reference_policy: FAILURE_BY_DEFAULT
same_successor_repetition: IDEMPOTENT_NO_STATE_CHANGE
different_successor_overwrite: FAILURE
repeated_erase_policy: IDEMPOTENT_NO_STATE_CHANGE
stable_failure_codes: REQUIRED
migration_scope:
  - CONTINUE_V1
  - START_NEW_V2_INSTANCE
  - ASSESS_V1_MIGRATABILITY
nk_sam_dependency: REQUIRED_BEFORE_RUNTIME_AUTHORIZATION
event_commitment_dependency: REQUIRED_BEFORE_RUNTIME_AUTHORIZATION
runtime_authorized_after_decision: false
```

## Non-authorizations

This acceptance does **not** authorize reducer-v2 code, PostgreSQL/SQLite schema changes, automatic migration, Event-vocabulary expansion, Admission runtime ownership, H11 execution, Final Canon, runtime thaw, production, or changes to historical evidence/assertion status.

## References

- [Issue #74](https://github.com/velantrian/velantrim-native-kernel/issues/74)
- [`0024-operator-decision-package.md`](./0024-operator-decision-package.md)
- [`ADR-0003`](./0003-semantic-conflicts-require-explicit-resolution.md)
- [`ADR-0006`](./0006-causal-links-are-relations.md)
- [`ADR-0012`](./0012-single-writer-append-and-replay-contract-v1.md)
- [`ADR-0015`](./0015-accept-clean-profile-and-authorize-p1-semantic-core.md)
- [`DECISION_PROCESS.md`](../DECISION_PROCESS.md)

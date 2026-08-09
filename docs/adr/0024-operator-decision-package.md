# ⚖️ ADR-0024 Operator Decision Package

**[English](./0024-operator-decision-package.md) · [Русский](./0024-operator-decision-package.ru.md)**

```yaml
document_role: OPERATOR_DECISION_PACKAGE
issue: 74
adr: ADR-0024
status_as_of: 2026-08-09
decision_state: PENDING_OPERATOR
selected_option: null
runtime_effect: REDUCER_V2_NOT_AUTHORIZED
```

> This package prepares the final decision on versioned reducer referential semantics. It does not accept ADR-0024 or authorize reducer-v2 runtime work.

## 1. Verified problem

Reducer v1 remains internally deterministic for its accepted event sequence, but it does not enforce the stricter referential rules proposed for future histories.

Current gaps include:

- `LINK` may reference Claims that were never admitted;
- `UTILIZED` may reference unknown or erased Claims;
- `SUPERSEDED` may reference an unknown successor, overwrite a previous successor, self-supersede or create cycles;
- `ERASED` may reference an unknown Claim;
- process-global reducer selection would be unsafe if different histories require different semantics.

This is a real semantic-contract gap, not evidence that existing reducer-v1 histories are invalid under reducer v1.

## 2. Non-negotiable historical boundary

```text
reducer v1 history
≠ silently upgraded reducer v2 history
```

Existing reducer-v1 histories, fixtures, state digests, Receipts and P1–C5 evidence remain interpreted under their published contract.

Any stricter semantics require:

- a new reducer contract/version;
- explicit history/instance binding;
- stable failure codes and locations;
- new positive and negative fixtures;
- a migration-assessment boundary;
- new evidence identity;
- no rewrite of historical evidence.

## 3. Available operator decisions

### `ACCEPT`

Accept ADR-0024 exactly as currently written.

**Effect:** authorizes contract-finalization work under the existing proposal, but does not by itself authorize runtime implementation until the history commitment and version-binding details are complete.

**Risk:** the current ADR leaves several operational details implicit, including exact failure-code names, failure locations, duplicate `ADMIT`, repeated `ERASED`, restricted references and the commitment dependency.

### `ACCEPT_WITH_CHANGES`

Accept the architectural direction while requiring the clarifications in this package before runtime work.

**Effect:** preserves immutable v1 and authorizes a revised final ADR that defines reducer v2, stable failures, per-history binding, bounded migration assessment and dependencies on NK-SAM/Event commitment.

**Technical assessment:** this is the strongest current engineering candidate because it closes ambiguities without rejecting the versioned-reducer direction.

### `REVISE`

Return ADR-0024 for a broader redesign before acceptance.

**Effect:** no reducer-v2 runtime work; the proposal is rewritten, potentially changing event roles, relation semantics or migration architecture.

**Best fit when:** the operator disagrees with referential enforcement in the reducer or wants Admission/typed relations designed first.

### `REJECT`

Reject versioned stricter referential semantics.

**Effect:** reducer v1 remains the only accepted reducer; Issue #74 must be closed as rejected or replaced by a different proposal.

**Risk:** unknown, erased and cyclic references remain permitted by the accepted reducer unless another contract layer rejects them.

## 4. Technical recommendation — not a decision

```text
recommended engineering option: ACCEPT_WITH_CHANGES
operator selection:             UNSET
```

Reasoning:

- immutable reducer v1 protects historical evidence;
- reducer v2 is the smallest explicit way to add stricter semantics without reinterpretation;
- per-history binding avoids process-global semantic drift;
- migration assessment can classify old histories without rewriting them;
- stable failure codes make PostgreSQL, SQLite and future independent implementations comparable;
- required changes can keep Admission, Temporal and typed-relation work out of the first v2 slice.

## 5. Required changes before `ACCEPT_WITH_CHANGES`

### 5.1. Dependency order

Reducer-v2 runtime must remain blocked until:

1. NK-SAM and named equivalence profiles are defined;
2. portable Event/history commitment is separated from operational/profile Receipts;
3. reducer, identity, encoding and schema versions are included in the declared commitment boundary;
4. stable failure-location semantics are defined.

### 5.2. Version binding

Reducer selection must be bound to a Kernel instance/history, not a Python process default.

Minimum binding:

```text
instance_id
reducer_contract
reducer_version
Event contract/version
identity contract
encoding profile
```

A history must not change reducer interpretation after its first committed Event without an accepted migration contract.

### 5.3. Reducer v1

`nk-p1-reducer/1` remains:

- readable;
- executable for historical replay;
- immutable in meaning;
- compatible with existing fixtures and evidence;
- permitted to contain histories that are non-migratable to v2.

### 5.4. Reducer v2 first scope

`nk-p1-reducer/2` enforces only referential semantics for already-authorized event roles.

It does **not** implement:

- full Admission workflow;
- truth evaluation;
- Temporal semantics;
- typed relation ontology;
- causal reasoning;
- operational deletion;
- distributed multi-writer behavior.

## 6. Proposed event-role decisions

The following defaults are technical recommendations and require operator acceptance.

### `ADMIT`

Recommended rules:

- first valid admission creates the admitted Claim state;
- an exactly duplicate admission under the same admitted Claim identity is deterministic and idempotent;
- a conflicting admission payload or incompatible admission reference fails;
- admitting an already erased/restricted Claim fails unless a future explicit restoration contract permits it;
- reducer v2 verifies an existing admission decision/reference but does not execute the complete Admission lifecycle.

Open decision:

```yaml
duplicate_identical_admit: IDEMPOTENT_NO_STATE_CHANGE
conflicting_admit: FAILURE
admit_erased_claim: FAILURE
admit_restricted_claim: FAILURE
```

### `LINK`

Recommended rules:

- source must exist and be admitted;
- target must exist and be admitted;
- erased or restricted references fail unless the event contract explicitly defines a historical-reporting role;
- generic self-links are not globally forbidden;
- generic graph cycles are not globally forbidden;
- relation-specific self-link/cycle restrictions belong to future typed-relation contracts.

Open decision:

```yaml
generic_self_link: ALLOWED
generic_cycle: ALLOWED
erased_reference: FAILURE
restricted_reference: FAILURE_BY_DEFAULT
```

### `UTILIZED`

Recommended rules:

- unknown Claim fails;
- erased Claim fails for current utilization;
- restricted Claim fails unless the event carries an explicitly authorized scope compatible with the restriction contract;
- historical reporting of prior use is a separate query/event role, not current `UTILIZED`.

Open decision:

```yaml
unknown_claim: FAILURE
erased_claim: FAILURE
restricted_claim: FAILURE_BY_DEFAULT
historical_use_reporting: SEPARATE_ROLE
```

### `SUPERSEDED`

Recommended rules:

- predecessor and successor must exist and be admitted;
- neither may be erased or prohibited from reference;
- predecessor and successor must differ;
- a predecessor may have only one active successor in v2;
- replaying the same predecessor→successor pair is deterministic and idempotent;
- replacing an existing successor with a different successor fails;
- self-supersession fails;
- two-node and longer supersession cycles fail;
- write order is not semantic truth.

Open decision:

```yaml
same_successor_repetition: IDEMPOTENT_NO_STATE_CHANGE
different_successor_overwrite: FAILURE
self_supersession: FAILURE
supersession_cycle: FAILURE
```

### `ERASED`

Recommended rules:

- unknown Claim fails;
- first valid erase moves the Claim to the existing logical-erasure state;
- repeated identical logical erase is deterministic and idempotent, while the Event remains visible in history;
- restricted/retention-held cases follow the accepted deletion-state contract and may result in restriction, pending or failure rather than a false physical-deletion claim;
- reducer v2 never claims physical or cryptographic deletion.

Open decision:

```yaml
unknown_claim: FAILURE
repeated_logical_erase: IDEMPOTENT_NO_STATE_CHANGE
physical_deletion_claim: FORBIDDEN
```

## 7. Proposed stable failure-code families

Final names must be frozen in the accepted contract.

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

Required stable failure output:

```text
failure_code
failure_location
Event index
global_seq, when committed
reducer contract/version
state-before-failure digest
proof boundary
```

Message text may evolve; machine code and location semantics must remain stable within the contract version.

## 8. Migration decision

Recommended first migration scope:

```text
CONTINUE_V1
START_NEW_V2_INSTANCE
ASSESS_V1_MIGRATABILITY
```

Not authorized in the first slice:

```text
SILENT_V1_TO_V2_UPGRADE
AUTOMATIC_HISTORY_REWRITE
AUTOMATIC_EVENT_TRANSFORMATION
```

Valid assessment outcomes:

```text
VALID_UNDER_V1_AND_MIGRATABLE
VALID_UNDER_V1_WITH_DECLARED_V2_FAILURES
VALID_UNDER_V1_NON_MIGRATABLE_TO_V2
INVALID_UNDER_DECLARED_V1_CONTRACT
UNDETERMINED
```

`NON_MIGRATABLE_TO_V2` does not invalidate a valid v1 history.

## 9. Required fixture set

Positive:

- first admission;
- duplicate identical admission;
- valid LINK;
- valid utilization;
- valid supersession;
- repeated identical supersession;
- valid erase;
- repeated logical erase.

Negative:

- conflicting admission;
- LINK missing source/target;
- LINK erased/restricted source/target;
- UTILIZED unknown/erased/restricted;
- SUPERSEDED unknown predecessor/successor;
- self-supersession;
- successor overwrite;
- two-node and long cycles;
- ERASED unknown;
- reducer-version substitution;
- encoding-profile substitution;
- failure-location disagreement between profiles.

## 10. Cross-profile acceptance

PostgreSQL, SQLite and future independent implementations must emit equivalent results under named profiles:

- state equivalence for successful histories;
- trace/failure equivalence for rejected histories;
- Receipt equivalence for bounded proof output.

They must agree on:

```text
failure code
failure location
Event index
global sequence, when applicable
reducer version
state-before-failure digest
```

Shared Python code may support PostgreSQL/SQLite comparison but does not establish independent implementation neutrality.

## 11. Operator selections

```yaml
adr_0024_decision: UNSELECTED
v1_immutability: REQUIRED
v2_instance_history_binding: UNSELECTED
duplicate_admit_policy: UNSELECTED
restricted_reference_policy: UNSELECTED
same_successor_repetition: UNSELECTED
different_successor_overwrite: UNSELECTED
repeated_erase_policy: UNSELECTED
stable_failure_codes: UNSELECTED
migration_scope: UNSELECTED
nk_sam_dependency: UNSELECTED
event_commitment_dependency: UNSELECTED
runtime_authorized_after_decision: false
```

## 12. Acceptance gates after operator decision

If accepted or accepted with changes:

1. revise ADR-0024 to final accepted wording;
2. freeze failure codes and event-role rules;
3. define NK-SAM/equivalence dependency;
4. define Event/history commitment dependency;
5. update registry and schemas without assertion promotion;
6. create a reducer-v2 semantic-core PR;
7. create a separate PostgreSQL/SQLite integration PR;
8. produce new fixtures and evidence identity;
9. preserve reducer-v1 reader and historical evidence;
10. synchronize GitHub and Notion after merge.

## 13. What this package proves

It proves only that the technical choices, dependencies, recommended defaults and unresolved operator selections are explicit.

## 14. What this package does not prove

It does not accept ADR-0024, authorize reducer v2, alter reducer v1, establish Admission/Temporal semantics, promote assertions or create evidence.
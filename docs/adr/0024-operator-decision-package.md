# ⚖️ ADR-0024 Operator Decision Package

**[English](./0024-operator-decision-package.md) · [Русский](./0024-operator-decision-package.ru.md)**

```yaml
document_role: OPERATOR_DECISION_PACKAGE
document_state: DECIDED
issue: 74
adr: ADR-0024
status_as_of: 2026-08-22
decision_state: OPERATOR_APPROVED
selected_option: ACCEPT_WITH_CHANGES
operator: '@velantrian'
decision_date: 2026-08-22
operator_decision_comment_id: 5379224144
operator_decision_url: https://github.com/velantrian/velantrim-native-kernel/issues/74#issuecomment-5379224144
operator_decision_block_sha256: c1fc11af41d3bed1088040bfbfbb31e1d840e4c860d36972b865e4ec86c3394c
runtime_effect: REDUCER_V2_NOT_AUTHORIZED
```

> This package is now decision provenance for ADR-0024. The normative accepted contract is `0024-version-reducer-referential-semantics.md`. Acceptance does not authorize reducer-v2 implementation.

## Decision

```text
ACCEPT_WITH_CHANGES
```

The operator accepted the versioned-reducer direction with the bounded clarifications prepared by this package.

## Accepted selections

```yaml
v1_immutability: REQUIRED
v2_instance_history_binding: REQUIRED
duplicate_admit_policy: IDEMPOTENT_NO_STATE_CHANGE
restricted_reference_policy: FAILURE_BY_DEFAULT
same_successor_repetition: IDEMPOTENT_NO_STATE_CHANGE
different_successor_overwrite: FAILURE
self_supersession: FAILURE
supersession_cycle: FAILURE
repeated_erase_policy: IDEMPOTENT_NO_STATE_CHANGE
physical_deletion_claim: FORBIDDEN
stable_failure_codes: REQUIRED
migration_scope:
  - CONTINUE_V1
  - START_NEW_V2_INSTANCE
  - ASSESS_V1_MIGRATABILITY
nk_sam_dependency: REQUIRED_BEFORE_RUNTIME_AUTHORIZATION
event_commitment_dependency: REQUIRED_BEFORE_RUNTIME_AUTHORIZATION
runtime_authorized_after_decision: false
```

## Historical boundary

`nk-p1-reducer/1` remains readable, replayable and immutable in meaning. Existing P1-C5 evidence remains reducer-v1-bounded evidence. A v1 history is not silently promoted, rewritten or reinterpreted as v2.

## Accepted first v2 contract scope

The future v2 contract is limited to referential semantics for already-authorized Event roles. It does not own full Admission, truth evaluation, Temporal semantics, typed relation ontology, causal reasoning, physical deletion, distributed multi-writer behavior or ecosystem authority.

Generic LINK self-reference and generic graph cycles remain allowed by the base reducer; relation-specific restrictions remain outside this contract. Unknown/erased references fail under the accepted strict rules; restricted references fail by default unless an accepted compatible scope exists. Supersession self-reference, successor overwrite and successor cycles fail.

## Stable failure families

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

Stable rejected-history output must bind failure code/location, Event index, global sequence when committed, reducer contract/version, state-before-failure digest and proof boundary.

## Migration boundary

Allowed first-scope operations:

```text
CONTINUE_V1
START_NEW_V2_INSTANCE
ASSESS_V1_MIGRATABILITY
```

Not authorized:

```text
SILENT_V1_TO_V2_UPGRADE
AUTOMATIC_HISTORY_REWRITE
AUTOMATIC_EVENT_TRANSFORMATION
```

## Runtime authorization remains closed

Before reducer-v2 runtime can be separately authorized, the repository must establish the required NK-SAM/named-equivalence dependency, portable Event/history commitment boundary, version binding, stable failure-location semantics, exact fixtures/evidence identity and rollback/migration behavior.

This decision does not authorize implementation, schema changes, H11 execution, Final Canon, runtime thaw, production, assertion promotion or reinterpretation of historical evidence.

## Decision closure

The earlier recommendation and unresolved selections in this package are superseded by the operator decision above. The normative details are frozen in the accepted ADR-0024. Any material expansion requires a new explicit architecture/operator decision rather than reinterpretation of this package.

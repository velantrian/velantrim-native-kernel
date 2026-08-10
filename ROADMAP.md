# Roadmap

```yaml
document_role: ACTIVE_ROADMAP
status_as_of: 2026-08-10
authoritative_machine_source: project-state.json
repository_status: RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
publication_checkpoint: 10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c
active_architecture_decision: ADR-0025
active_architecture_issue: 88
```

Native Kernel keeps three independent tracks:

```text
H — Historical Recovery
C — Clean Reference Implementation
R — Architecture Re-foundation and Long-Horizon Research
```

## Governing sequence

```text
A1 purpose
→ A2 ontology
→ A3 abstract machine
→ A4 semantic laws
→ A5 identity / time / change
→ A6 lifecycle
→ A7 conflict / uncertainty / revision
→ A8 substrate-independence contract
→ A9 reference-laboratory boundary
→ A10 open questions / falsification
→ integrated A1-A10 review                 COMPLETE / PROVISIONAL
→ OPERATOR_POST_BLUEPRINT_DECISION          NEXT GATE
→ only then any separately authorized next phase
```

## Current architecture checkpoint

- A1–A10: `DRAFTED / PROVISIONAL`;
- integrated review: [EN](docs/INTEGRATED_A1_A10_REVIEW.md) / [RU](docs/INTEGRATED_A1_A10_REVIEW.ru.md);
- review identity: `nk-integrated-blueprint-review/A1-A10-review-1`;
- integrated review state: `COMPLETED / PROVISIONAL / OPERATOR_DECISION_PENDING`;
- next gate: `OPERATOR_POST_BLUEPRINT_DECISION`;
- runtime expansion: `FROZEN`;
- P1–C5: `BOUNDED_REFERENCE_LABORATORY`;
- production: `false`.

The integrated review explicitly reconciles seven findings. Material corrections include separating physical and cryptographic erasure, resolving the A6 closure-method contradiction, interpreting A1 confidence wording through A7 uncertainty semantics, normalizing A10 to its five declared outcomes, and preserving non-linear lifecycle/conflict semantics.

This review pass found **no known blocking internal semantic contradiction remaining after those explicit reconciliation decisions**. That is not independent validation and not operator acceptance.

## Runtime freeze

Allowed: architecture research, integrity/security/reproducibility/provenance repair, evidence preservation, truth/validator repair, historical recovery, isolated falsification experiments without runtime promotion.

Not authorized without a new explicit operator decision: reducer-v2, new semantic/conflict Event verbs, new databases/language profiles/model adapters/integrations, executable NK-EPI/Temporal/full Admission, operational deletion expansion, maturity promotion, production authorization, or other semantic/runtime expansion.

## Independent pending decisions

- **Issue #18** — license/publication: `PENDING_OPERATOR`; selected option remains null.
- **Issue #74 / ADR-0024** — `PROPOSED / PENDING_OPERATOR`; reducer-v2 remains unauthorized.
- **ADR-0003** — `PROPOSED / NOT_STARTED`.
- **Track H source admission** — operator-controlled.

## Contract and laboratory boundary

Accepted/versioned current contracts remain usable and historically valid within their scope. The integrated review does not silently promote Python, PostgreSQL, SQLite, Event sourcing, reducer v1, SHA-256, sequence integers, Receipt encoding, CI, or evidence packaging into universal Architecture Canon.

```text
accepted current mechanism
→ retain scope and evidence identity
→ map against integrated blueprint when needed
≠ automatic architecture requirement
≠ retroactive evidence rewrite
```

## Hard stop

`OPERATOR_POST_BLUEPRINT_DECISION` is a decision gate, not an A11 deliverable. No automatic sequencing follows from integrated-review completion.

```text
A1-A10 drafted ≠ independent approval
integrated review complete ≠ operator acceptance
Integrated review complete ≠ runtime thaw
integrated review complete ≠ arbitrary-substrate proof
C5 PASS ≠ production readiness
public repository ≠ open-source license
```

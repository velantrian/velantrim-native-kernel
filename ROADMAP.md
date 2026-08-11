# Roadmap

```yaml
document_role: ACTIVE_ROADMAP
status_as_of: 2026-08-11
authoritative_machine_source: project-state.json
repository_status: RESEARCH / C5 BOUNDED OPERATIONAL REHEARSAL / NOT PRODUCTION-READY
publication_checkpoint: 10ffd6f9d8e7e588a07d7815205f7c3d50b3cb5c
blueprint_decision: ADR-0025
post_blueprint_decision: ADR-0026
active_architecture_issue: 88
```

Native Kernel keeps three independent tracks:

```text
H — Historical Recovery
C — Clean Reference Implementation
R — Architecture Re-foundation and Post-Blueprint Validation
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
→ OPERATOR_POST_BLUEPRINT_DECISION         COMPLETE / OPTION D / ADR-0026
→ INDEPENDENT_ARCHITECTURE_REVIEW          NEXT GATE
→ REVIEW_FINDING_RECONCILIATION            BLOCKED BY REVIEW
→ BPV-1 CROSS-LINEAGE FALSIFICATION        BLOCKED BY REVIEW + RECONCILIATION
→ A10 OUTCOME CLASSIFICATION               BLOCKED BY BPV-1
→ INTEGRATED RE-REVIEW                     BLOCKED BY OUTCOMES
→ separate operator Canon/runtime decision BLOCKED BY RE-REVIEW
```

## Current architecture checkpoint

- A1–A10: `DRAFTED / PROVISIONAL`;
- integrated review: [EN](docs/INTEGRATED_A1_A10_REVIEW.md) / [RU](docs/INTEGRATED_A1_A10_REVIEW.ru.md);
- review identity: `nk-integrated-blueprint-review/A1-A10-review-1`;
- operator post-blueprint choice: `OPTION D / ADR-0026 / APPROVED`;
- independent review protocol: `nk-independent-architecture-review/1`;
- independent architectural validation: `NOT ESTABLISHED`;
- next gate: `INDEPENDENT_ARCHITECTURE_REVIEW`;
- BPV-1: `BLOCKED_PENDING_INDEPENDENT_REVIEW_AND_RECONCILIATION`;
- runtime expansion: `FROZEN`;
- P1–C5: `BOUNDED_REFERENCE_LABORATORY`;
- production: `false`.

## Option D validation sequence

ADR-0026 deliberately separates two kinds of attack on the architecture:

1. **independent conceptual challenge** — search for hidden assumptions, unnecessary obligations, circularity, non-falsifiability and implementation capture before the experiment is designed;
2. **bounded cross-lineage falsification** — after review reconciliation, attempt one deliberately different realization to test named architecture hypotheses without admitting it as product runtime.

The independent review is not complete merely because the protocol exists. The review must have a declared qualifying reviewer and independence basis.

The later BPV-1 plan must define success/failure conditions before implementation. A failed experiment may weaken or refute an architecture claim and is not a project failure.

## Runtime freeze

Allowed: architecture research, independent review, review reconciliation, integrity/security/reproducibility/provenance repair, evidence preservation, truth/validator repair, historical recovery, and later isolated falsification experiments that satisfy ADR-0026 without runtime promotion.

Not authorized without a later explicit operator decision: reducer-v2, new semantic/conflict Event verbs, product database/language/model/integration profiles, executable NK-EPI/Temporal/full Admission, operational deletion expansion, maturity promotion, production authorization, or other product semantic/runtime expansion.

## Independent pending decisions

- **Issue #18** — license/publication: `PENDING_OPERATOR`; selected option remains null.
- **Issue #74 / ADR-0024** — `PROPOSED / PENDING_OPERATOR`; reducer-v2 remains unauthorized.
- **ADR-0003** — `PROPOSED / NOT_STARTED`.
- **Track H source admission** — operator-controlled.

## Contract and laboratory boundary

Accepted/versioned current contracts remain usable and historically valid within their scope. ADR-0026 does not silently promote Python, PostgreSQL, SQLite, Event sourcing, reducer v1, SHA-256, sequence integers, Receipt encoding, CI, or evidence packaging into universal Architecture Canon.

```text
accepted current mechanism
→ retain scope and evidence identity
→ challenge against A1-A10 obligations
→ later map as PRESERVED / PARTIAL / LOSSY / UNSUPPORTED / INDETERMINATE
≠ automatic architecture requirement
≠ retroactive evidence rewrite
```

## Hard stop

```text
Option D approved ≠ independent validation
independent review protocol ≠ completed review
completed review ≠ BPV-1 success
BPV-1 ≠ product runtime
BPV-1 outcome ≠ automatic Canon promotion
A1-A10 drafted ≠ Final Canon
C5 PASS ≠ production readiness
public repository ≠ open-source license
```

The only current next gate is `INDEPENDENT_ARCHITECTURE_REVIEW`.
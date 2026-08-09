# ⚖️ Governance and Operator Decisions

**[English](./README.md) · [Русский](./README.ru.md)**

This directory contains decision packages and machine-readable pending-decision state. It does not contain automatic authorization.

## Current packages

| Decision | Issue | State | Package |
|---|---:|---|---|
| License and publication terms | #18 | `PENDING_OPERATOR` | [`LICENSE_PUBLICATION_DECISION_OPTIONS.md`](./LICENSE_PUBLICATION_DECISION_OPTIONS.md) |
| ADR-0024 reducer referential semantics | #74 | `PENDING_OPERATOR` | [`../adr/0024-operator-decision-package.md`](../adr/0024-operator-decision-package.md) |

Machine-readable state:

- [`operator-decisions-v1.json`](./operator-decisions-v1.json)

## Current effect

```text
license selected:             NO
external contributions open: NO
package publication allowed: NO
ADR-0024 accepted:            NO
reducer-v2 runtime allowed:   NO
production authorized:        NO
```

## Decision rule

Only an explicit operator decision may replace `PENDING_OPERATOR`. The resulting decision must identify its exact scope, rationale, effective checkpoint and required follow-up PRs.

```text
decision package
≠ operator decision
≠ runtime implementation
≠ evidence
≠ production authorization
```

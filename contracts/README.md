# Native Kernel contract registry and fixture pack

This directory is a machine-readable review surface for the architecture track. It is not a Kernel runtime.

## Decision status

ADR-0011 through ADR-0014 are now `ACCEPTED / OPERATOR_APPROVAL_APPROVED`.

```text
accepted contract
≠ runtime implementation
≠ repository-reproduced CI
≠ C2/C3 Kernel conformance
≠ production proof
```

Accepted exact contracts:

```text
nk-id/1.0       — canonical identity
nk-event/1.0    — single-writer append/idempotency/order/replay boundary
nk-deletion/1.0 — deletion/restriction/retention semantics
nk-fixtures/1.0 — executable fixture/evidence protocol
```

`NK-EPI-001…008` and ADR-0008 remain `PROPOSED`.

## Registry semantics

`registry.json` records accepted family ownership and assertion-level status. The exact assertions governed by ADR-0011 through ADR-0014 are `ACCEPTED`; the epistemic fixture assertions remain `PROPOSED`.

`runtime_status: NOT_IMPLEMENTED` remains authoritative for this package. Assertion acceptance states what future profiles must preserve; it does not state that the built-in reader implements those assertions as Kernel behaviour.

## Files

- `registry.json` — stable family/assertion registry;
- `schema-bundle.json` — neutral JSON Schema bundle for review and adapters;
- `evidence-report-v1.schema.json` — standalone evidence-report schema;
- `fixture-pack.json` — identity, event, deletion and epistemic scenarios;
- `idempotency-scenarios.json` — retry, conflicting reuse and concurrent-attempt cases.

## Validation

```bash
python tools/conformance/runner.py validate
python -m unittest discover -s tests -p 'test_conformance_runner.py'
```

Local authoring result recorded for the accepted package:

```text
8 unit tests PASS
72 assertion IDs covered exactly once in the evidence report
2 identity golden vectors matched
4 invalid identity vectors rejected
2 event-chain scenarios validated
2 idempotency scenarios validated
2 deletion scenarios validated
NK-EPI-001…008 each have positive and negative fixtures
```

The runner directly verifies stored `payload_hash`, event-chain continuity, idempotency fixture semantics and complete adapter assertion coverage. Missing, duplicated or silently skipped assertion results are rejected.

A passing built-in report deliberately states:

```text
support_state: SUPPORTED
kernel_runtime_conformance: UNSUPPORTED
assertion_results: 72 × UNSUPPORTED
```

The support state describes the fixture-integrity reader only. It does not claim that a Kernel runtime supports the assertions.

## Workflow

The repository workflow supports:

```text
pull_request path trigger
push-to-main path trigger
manual workflow_dispatch
```

An active workflow definition is not an executed result. Until an exact run is recorded, evidence remains `LOCALLY_TESTED` rather than `REPOSITORY_REPRODUCED`.

## Evidence boundary

```text
fixture integrity
≠ runtime implementation
≠ operator evidence substitution
≠ C2 for a Kernel profile
≠ C3 without two materially independent profiles
```

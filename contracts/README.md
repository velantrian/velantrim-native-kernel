# Native Kernel contract, evidence and fixture registry

This directory is a machine-readable review surface for the architecture and bounded-evidence tracks. It is not a Kernel runtime, deployment or authority source.

## Decision status

ADR-0011 through ADR-0014 are `ACCEPTED / OPERATOR_APPROVAL_APPROVED`. ADR-0019 authorizes the independent SQLite/C3 profile work. ADR-0020 authorizes C4 only as authority-free offline evaluation of an approved recorded workload.

```text
accepted contract or evidence protocol
≠ runtime implementation
≠ repository-reproduced CI
≠ authority promotion
≠ production proof
```

Accepted exact contract protocols:

```text
nk-id/1.0       — canonical identity
nk-event/1.0    — single-writer append/idempotency/order/replay boundary
nk-deletion/1.0 — deletion/restriction/retention semantics
nk-fixtures/1.0 — executable fixture/evidence protocol
```

Bounded evidence protocols:

```text
nk-evidence-report/1 — single-profile assertion report
nk-equivalence-report/1 — declared cross-profile C3 comparison
nk-shadow-workload/1 — approved immutable recorded observations
nk-shadow-report/1 — complete C4 evaluation report
nk-shadow-receipt/1 — bounded per-case observation receipt
```

Evidence protocols do not make one current JSON layout or evaluator implementation Architecture Canon.

`NK-EPI-001…008` and ADR-0008 remain `PROPOSED`.

## Registry semantics

`registry.json` records accepted family ownership and assertion-level status. The exact assertions governed by ADR-0011 through ADR-0014 are `ACCEPTED`; epistemic assertions remain `PROPOSED`.

Assertion acceptance states what profiles must preserve. It does not by itself establish implementation, C2, C3, C4, truth, deletion or production behaviour.

## Files

- `registry.json` — stable family/assertion registry;
- `schema-bundle.json` — neutral JSON Schema bundle for review and adapters;
- `evidence-report-v1.schema.json` — single-profile evidence-report schema;
- `fixture-pack.json` — identity, event, deletion and epistemic scenarios;
- `idempotency-scenarios.json` — retry, conflicting reuse and concurrent-attempt cases;
- `shadow-workload-v1.json` — approved C4 recorded observations and thresholds;
- `shadow-report-v1.schema.json` — C4 report shape and required evidence fields.

## Approved C4 workload

```text
dataset_id:      native-kernel/c4-offline-shadow-v1
protocol:        nk-shadow-workload/1
sha256:          15fb81d8858dcc4e349ffe87c257b25450db026473614582faa7817f90249da3
cases:           15
assertion scope: 45 / 45 C3-supported assertions
approval:        ADR-0020 / Issue #61 / OFFLINE_RECORDED_WORKLOAD_ONLY
```

The workload contains synthetic recorded repository observations. It is not captured production traffic.

Its authority policy is mandatory:

```text
mode:                  SHADOW_ONLY
authority promotion:   FORBIDDEN
authoritative writes:  FORBIDDEN
side effects:           FORBIDDEN
promotion decision:    NOT_AUTHORIZED
```

Changing dataset observations, fields or thresholds requires a new immutable dataset version, digest, decision/manifest update and repository evidence cycle. Reusing the old identity after a material edit is invalid.

## Fixture validation

```bash
python tools/conformance/runner.py validate
python -m unittest discover -s tests -p 'test_conformance_runner.py'
```

The fixture reader verifies stored `payload_hash`, Event-chain continuity, idempotency fixture semantics and complete adapter assertion coverage. Missing, duplicated or silently skipped assertion results are rejected.

A passing built-in fixture-integrity report may still state:

```text
kernel_runtime_conformance: UNSUPPORTED
assertion_results: 72 × UNSUPPORTED
```

Fixture integrity is not profile support.

## C4 validation

```bash
python -m unittest discover -s tests -p 'test_c4_shadow_evaluation.py' -v
python -m unittest discover -s tests -p 'test_c4_report_validator.py' -v
python tools/conformance/validate_c4_report.py report.json --require-repository
```

The C4 evaluator and validator require:

- exact dataset protocol/ID/digest;
- exact validated C3 prerequisite;
- all 15 cases and one Receipt per case;
- exact 45-supported assertion scope and complete 72-ID result set;
- zero semantic/critical divergences and zero missing Receipts for PASS;
- explicit allowed operational differences;
- repository SHA/run/environment metadata;
- required offline/live, authority, truth, deletion, C5 and production limitations.

## Evidence boundary

```text
fixture integrity
≠ runtime implementation

C2 single-profile reproduction
≠ C3 cross-profile comparison

C3 comparison
≠ C4 offline shadow observation

C4 offline observation
≠ live traffic
≠ authority promotion
≠ candidate approval
≠ truth/authenticity
≠ physical deletion
≠ C5 / production readiness
```

# Native Kernel contract registry and fixture pack

This directory is a machine-readable review surface for the architecture track. It is not a Kernel runtime.

## Publication status

The package was published to `main` through PR #35 at merge SHA `0552ae284d56148972e9bcc8de5f80a7f462c0f3`.

```text
published in main
≠ ADR-0011…0014 accepted
≠ operator approval
≠ Kernel runtime implemented
≠ C2/C3 Kernel conformance
```

ADR-0011 through ADR-0014 remain `PROPOSED / OPERATOR_APPROVAL_PENDING`. This checkpoint update intentionally touches `contracts/**` so the now-active fixture-integrity workflow can run on a subsequent `main` push.

## Status semantics

`registry.json` contains two layers:

1. assertion IDs inherited from the accepted ADR-0010 family skeleton;
2. additional exact-contract assertions proposed by ADR-0011 through ADR-0014.

The family-level `decision_status` records the status of the **family ownership boundary**, not automatic acceptance of every assertion or the named exact contract version. The authoritative status of each row is its own `status` field plus the owning ADR.

```text
family decision_status: ACCEPTED
+ assertion status: PROPOSED
= accepted ownership namespace with a proposed exact rule
```

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

Local authoring result recorded for PR #35:

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

## Evidence boundary

```text
fixture integrity
≠ runtime implementation
≠ operator acceptance
≠ C2 until exact repository CI exists
≠ C3 without two materially independent profiles
```

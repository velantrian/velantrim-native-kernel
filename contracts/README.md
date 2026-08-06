# Native Kernel contract registry and fixture pack

This directory is a machine-readable review surface for the architecture track. It is not a Kernel runtime.

## Status semantics

`registry.json` contains two layers:

1. assertion IDs inherited from the accepted ADR-0010 family skeleton;
2. additional exact-contract assertions proposed by ADR-0011 through ADR-0014.

The family-level `decision_status` records the status of the **family ownership boundary**, not automatic acceptance of every assertion or the named exact contract version. The authoritative status of each row is its own `status` field plus the owning ADR.

Therefore:

```text
family decision_status: ACCEPTED
+ assertion status: PROPOSED
= accepted ownership namespace with a proposed exact rule
```

ADR-0011 through ADR-0014 remain `PROPOSED / OPERATOR_APPROVAL_PENDING` until an explicit operator decision is recorded.

## Files

- `registry.json` — stable family/assertion registry;
- `schema-bundle.json` — neutral JSON Schema bundle for review and adapters;
- `fixture-pack.json` — identity, event, deletion and epistemic scenarios.

## Validation

```bash
python tools/conformance/runner.py validate
python -m unittest discover -s tests -p 'test_conformance_runner.py'
```

A passing report deliberately states `kernel_runtime_conformance: UNSUPPORTED`.

## Evidence boundary

```text
fixture integrity
≠ runtime implementation
≠ operator acceptance
≠ C2 until exact repository CI exists
≠ C3 without two materially independent profiles
```

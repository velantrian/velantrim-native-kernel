# Conformance fixture tooling

Standard-library support tooling for Issues #14–#17.

```bash
python tools/conformance/runner.py validate
python -m unittest discover -s tests -p 'test_conformance_runner.py'
```

The validator checks:

- unique assertion IDs;
- identity golden and invalid vectors;
- event sequence, payload commitments and hash-chain continuity;
- idempotent retries, conflicting key reuse and concurrent attempts;
- deletion state-machine transitions and Receipt limits;
- positive/negative coverage for `NK-EPI-001…008`;
- exact assertion coverage in external adapter evidence reports.

Current local suite: `8 PASS`.

The built-in output deliberately states `kernel_runtime_conformance: UNSUPPORTED` and emits one `UNSUPPORTED` result for every registered assertion. `support_state: SUPPORTED` refers only to the fixture-integrity reader.

This tooling validates fixture integrity and reference algorithms; it is not Native Kernel runtime code.

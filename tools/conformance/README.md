# Conformance fixture tooling

Standard-library support tooling for Issues #14–#17.

```bash
python tools/conformance/runner.py validate
python -m unittest discover -s tests -p 'test_conformance_runner.py'
```

The output deliberately states `kernel_runtime_conformance: UNSUPPORTED`. This tooling validates fixture integrity and reference algorithms; it is not Native Kernel runtime code.

# P1 Semantic Core

**Status:** `IMPLEMENTED / LOCALLY_TESTED / PROFILE-INCOMPLETE`

This directory is the first bounded runtime slice of the clean lineage:

```text
profile:  native-kernel/postgresql-reference
evidence: clean/postgresql-reference/0.1
phase:    P1 semantic core
```

It is profile-independent and uses Python 3.11+ standard library only.

## Implemented scope

- `nk-id/1.0` canonical JSON subset and domain-separated identity helpers;
- immutable semantic content, Claim identity, command and logical Event models;
- provisional P1 command/state digests (`nkd0`, `nks0`), explicitly not Canon;
- explicit deny-by-default authority policy;
- deterministic version-bound in-memory reducer;
- deletion/restriction state-machine transitions;
- admission and deletion Receipt overclaim rejection;
- focused tests against committed identity/deletion fixtures.

## Explicitly absent

```text
PostgreSQL / SQLite adapter
SQL schema or migration
append store or durable idempotency
writer lease / epoch persistence
projection persistence
network API
P2–P5 implementation
C1 / C2 / C3 profile conformance
Titan / Mentaury / Crystal integration
recovered v0.1.2.1 lineage
```

The reducer processes logical in-memory Events for deterministic P1 evidence. It is not an authoritative event store and does not establish replay durability.

## Validation

```bash
python -m unittest discover -s tests -p 'test_semantic_core.py' -v
python -m compileall -q native_kernel
```

Recorded branch evidence must name the exact head SHA. Local PASS is not repository CI evidence.

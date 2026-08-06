# 🧬 Identity and Canonical Encoding Contract v1

- **Contract:** `nk-id/1.0`
- **Decision:** `ACCEPTED`
- **Operator approval:** `APPROVED`
- **Evidence:** `LOCALLY_TESTED` for the reference canonicalizer and vectors only
- **Runtime:** `NOT_IMPLEMENTED`
- **Issue:** #14
- **ADR:** ADR-0011

## Purpose

Define identity that survives replacement of databases, languages and object layouts.

```text
content identity ≠ Claim identity ≠ lineage identity ≠ Event identity ≠ storage identity
```

## Canonical subset

Identity-bearing objects use UTF-8 JSON with these rules:

1. every string and key is already Unicode NFC;
2. object keys are sorted lexicographically;
3. no insignificant whitespace is emitted;
4. integers and booleans are allowed;
5. binary floating-point values are forbidden;
6. decimal quantities are strings under a field-specific grammar;
7. explicit `null` is forbidden; omit an optional field;
8. timestamps participating in identity use `YYYY-MM-DDTHH:MM:SSZ`;
9. unknown identity-bearing fields require a new contract version.

Reference encoding:

```text
json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
```

This line is explanatory; the normative behaviour is the rules plus golden and invalid vectors.

## Domains and identifiers

| Identity | Domain prefix before canonical bytes | External form |
|---|---|---|
| Content | `nk-id-content-v1\0` | `nkh1:<sha256>` |
| Claim | `nk-id-claim-v1\0` | `nkc1:<sha256>` |
| Lineage | `nk-id-lineage-v1\0` | `nkl1:<sha256>` |

`content_hash` identifies declared semantic content. `claim_id` identifies a source-bound durable assertion using `content_hash`, `source_ref`, `source_record_id` and `asserted_at`. `lineage_id` is independently derived from an explicit lineage namespace and seed. Backend row IDs never substitute for these values.

## Collision and migration

- a matching identifier with different canonical bytes is a hard collision incident;
- records must not be merged or overwritten;
- migration creates aliases from the old contract/version to the new identifier;
- original identifiers and bytes remain inspectable where retention policy permits;
- hash replacement requires a new prefix and domain.

## Proof boundary

The Python canonicalizer and fixtures prove deterministic behaviour for the declared vectors. They do not prove cross-language equivalence, storage portability, runtime adoption or historical use by `v0.1.2.1`. C3 requires two materially independent implementations.

---

# 📜 Atomic Append, Ordering and Replay Contract v1

- **Contract:** `nk-event/1.0`
- **Decision:** `ACCEPTED`
- **Operator approval:** `APPROVED`
- **Evidence:** `LOCALLY_TESTED` fixture integrity only
- **Runtime:** `NOT_IMPLEMENTED`
- **Issue:** #15
- **ADR:** ADR-0012

## Baseline writer model

Version 1 defines a **single authoritative writer**. Multi-writer behaviour is outside this version and cannot be inferred from a hash chain.

```text
command intent
→ schema validation
→ authority check
→ idempotency decision
→ atomic history append
→ durability acknowledgement
→ asynchronous/disposable projections
→ replay Receipt
```

## Idempotency

An idempotency key is scoped to the authoritative writer and command contract version.

- first valid command: append exactly one Event;
- retry with the same canonical command digest: return the original append result;
- reuse with a different digest: reject as `IDEMPOTENCY_CONFLICT`;
- read-time deduplication is not durable idempotency.

## Ordering

- `global_seq` starts at 1 and is contiguous for the writer history;
- `stream_seq` is contiguous inside each declared stream;
- timestamps do not replace sequence ordering;
- valid time, observation time and record time remain separate fields when applicable.

## Event envelope

The v1 envelope binds command identity, idempotency key, stream, sequence, actor, authority, record time, event type, schema version, payload commitment and previous global hash. The accepted event vocabulary remains:

```text
ADMIT · LINK · UTILIZED · SUPERSEDED · ERASED
```

No additional verb is accepted by this contract.

## Atomicity and projections

The authoritative append and durable idempotency record form one atomic boundary. Projection updates occur after append. Projection failure must be visible and recoverable by destroy/rebuild; it cannot rewrite or roll back committed history.

## Integrity and threat boundary

A domain-separated SHA-256 chain detects many accidental or unsanctioned byte changes in the inspected sequence. It does not prove source authenticity, prevent a privileged history rewrite, solve distributed consensus or prove external timestamp accuracy.

## Replay

Replay starts from empty derived state, consumes events in `global_seq`, applies declared schema upcasters and reducer version, and emits an evidence record. Unsupported event or reducer versions fail explicitly.

## Proof boundary

The fixture reader validates commitments, ordering, idempotency scenarios and replay boundaries only. It is not a durable event store, reducer, crash-recovery mechanism or Kernel runtime.

---

# 🔒 Deletion, Restriction and Retention Contract v1

- **Contract:** `nk-deletion/1.0`
- **Decision:** `ACCEPTED`
- **Operator approval:** `APPROVED`
- **Evidence:** `LOCALLY_TESTED` state-machine fixtures only
- **Runtime:** `NOT_IMPLEMENTED`
- **Issue:** #16
- **ADR:** ADR-0013

## Core distinction

```text
logical ERASED event
≠ access restriction
≠ physical deletion
≠ cryptographic erasure
≠ proof of global erasure
```

Append-only architecture does not override legal or contractual deletion obligations.

## Data-location inventory

Every adopting profile must inventory authoritative payloads, projections, caches, FTS/graph/vector indexes, external model requests, exports, Receipts, Shadow datasets, backups, replicas, migration artifacts, logs, dumps and dead-letter stores. Unsupported or unknown locations remain explicit.

## State machine

```text
ACTIVE ↔ RESTRICTED
ACTIVE/RESTRICTED → ERASE_REQUESTED → ERASURE_IN_PROGRESS
ERASURE_IN_PROGRESS → PARTIALLY_ERASED → retry
ERASURE_IN_PROGRESS → CRYPTO_ERASED | PHYSICALLY_ERASED
any permitted stage → RETENTION_HOLD or FAILED_RETRYABLE
```

A hold blocks destructive completion but does not authorize broader access.

## Restore rule

A restored backup remains quarantined until restriction and erasure records are replayed. Data must not become queryable before the latest applicable deletion state is applied.

## Crypto-erasure

Crypto-erasure requires subject- or scope-specific key separation, documented key hierarchy, destruction evidence and a statement of residual metadata. Destroying a shared key that also destroys unrelated records is not an acceptable implicit implementation.

## Receipt boundary

A deletion Receipt lists verified locations, pending/unverified locations, policy and authority, attempts, provider acknowledgements and known limits. It must not assert complete global erasure.

## Proof boundary

The accepted contract defines meaning, lifecycle and proof limits. It does not establish legal compliance, physical media deletion, provider behaviour, backup completion or an implemented key-management/runtime mechanism.

---

# 🧪 Executable Conformance Fixture Protocol v1

- **Contract:** `nk-fixtures/1.0`
- **Decision:** `ACCEPTED`
- **Operator approval:** `APPROVED`
- **Tooling:** `IMPLEMENTED / LOCALLY_TESTED`
- **Kernel runtime conformance:** `UNSUPPORTED`
- **Issue:** #17
- **ADR:** ADR-0014

## Artifact structure

```text
contracts/
├── registry.json
├── schema-bundle.json
├── evidence-report-v1.schema.json
├── fixture-pack.json
└── idempotency-scenarios.json

tools/conformance/
├── runner.py
└── README.md

tests/test_conformance_runner.py
```

Every assertion has a stable ID and status. A fixture states family, version, expected result and equivalence class. Unsupported assertions are reported rather than skipped.

## Equivalence classes

- **byte** — identical canonical bytes or domain-separated identifier;
- **structural** — equivalent required fields and relationships;
- **semantic** — preserved identity, scope, authority, time, conflict and unknown meaning;
- **behavioural** — equivalent accepted/rejected commands and observable outcomes in a bounded workload.

## Runner protocol

```bash
python tools/conformance/runner.py validate
python -m unittest discover -s tests -p 'test_conformance_runner.py'
```

The built-in reader checks registry uniqueness, identity vectors, event commitments/chains, idempotency scenarios, deletion transitions and positive/negative `NK-EPI-001..008` coverage.

An external adapter may be invoked through:

```bash
python tools/conformance/runner.py adapter --output report.json -- <adapter-command>
```

The runner appends the fixture-pack path. The adapter writes one JSON evidence report to stdout. Non-zero exit, malformed JSON, missing or duplicated assertion status, and silent skip are failures.

## Evidence boundary

The built-in Python profile is a fixture-integrity reader, not a Kernel implementation. A passing report supports only the fixture protocol in its recorded environment. Repository reproduction requires an exact committed workflow result. C3 requires two materially independent implementation profiles.

## Governance boundary

Acceptance makes these four contracts the current normative architecture for future profiles. It does not:

- implement Native Kernel runtime behaviour;
- establish C2 or C3;
- accept `NK-EPI` as an architecture family beyond its existing proposed status;
- change Issue #1 or reconstruct `v0.1.2.1`;
- authorize Titan, Mentaury or Crystal runtime integration.

# 🧪 Conformance Model

> **Status:** `ACCEPTED ABSTRACT CONTRACT / P4 ASSERTION ADAPTER IMPLEMENTED / NOT A CERTIFICATION PROGRAM`  
> **Purpose:** define how a present or future implementation demonstrates bounded Native Kernel contract support

## 1. Why conformance matters

Technology independence must be tested, not merely declared. A system is not a Native Kernel implementation because it uses the same terminology or database.

```text
same architectural contract
        ↓
implementation profile A
implementation profile B
        ↓
comparable declared semantic behaviour
```

Conformance concerns meaning and observable behaviour. Identical code, storage layout or bytes are required only when a specific assertion declares byte equality.

## 2. Conformance levels

| Level | Meaning | Required evidence |
|---|---|---|
| **C0 — Described** | A profile maps itself to a contract | architecture mapping only |
| **C1 — Locally exercised** | Behaviour runs in a recorded local environment | commands, local tests and failure cases |
| **C2 — Repository reproduced** | A third party can reproduce the assertion from the repository | committed implementation, tests, environment, CI and traceability |
| **C3 — Cross-profile equivalent** | Two materially different profiles preserve a declared equivalence | shared fixtures, profile mappings and comparison evidence |
| **C4 — Shadow evaluated** | Behaviour is compared on approved recorded workloads without authority promotion | dataset, metrics, Receipts, failures and report |
| **C5 — Operationally validated** | A bounded deployment has security, rollback, privacy and incident evidence | explicit operational review and evidence |

Levels are **assertion-scoped**. They do not replace decision status, implementation status, evidence level, support state, maturity or operator approval.

A profile can therefore truthfully report:

```text
support_state: PARTIAL
kernel_runtime_conformance: C2
```

when C2 applies only to the assertion results marked `SUPPORTED`, while other assertions remain `PARTIAL` or `UNSUPPORTED`.

## 3. Contract families and exact contracts

ADR-0010 accepts the family map:

```text
NK-SEM — semantic roles
NK-ID  — identity and canonical encoding
NK-EVT — event, observation and recorded change
NK-AUT — authority and admission
NK-CFL — conflict and explicit unknowns
NK-EQV — conformance and semantic equivalence
```

ADR-0011 through ADR-0014 accept:

```text
nk-id/1.0       — canonical semantic identity
nk-event/1.0    — append, idempotency, order and replay boundary
nk-deletion/1.0 — restriction, deletion, retention and erasure meaning
nk-fixtures/1.0 — machine-readable fixture/evidence protocol
```

`NK-EPI-001…008` remains a proposed family associated with ADR-0008. Fixture presence and test execution do not accept that family.

Normative sources:

- [`docs/contracts/NORMATIVE_CONTRACTS_V1.md`](./contracts/NORMATIVE_CONTRACTS_V1.md);
- [`docs/contracts/NORMATIVE_CONTRACTS_V1.ru.md`](./contracts/NORMATIVE_CONTRACTS_V1.ru.md);
- ADR-0011 through ADR-0014;
- machine-readable [`../contracts/registry.json`](../contracts/registry.json).

## 4. Assertion result states

Every registered assertion must appear exactly once in an evidence report as:

| State | Meaning |
|---|---|
| `SUPPORTED` | the declared bounded behavior was directly reproduced |
| `PARTIAL` | meaningful behavior was reproduced, but an explicit gap remains |
| `UNSUPPORTED` | sufficient executable support is absent or the assertion is not accepted |
| `FAILED` | a required declared check was executed and failed |

Unsupported assertions remain visible. A profile cannot obtain a higher level by omitting them.

`FAILED` must not be silently converted to `UNSUPPORTED`. Adapter failure aborts report generation when a required check fails.

## 5. Evidence report protocol

The report protocol is `nk-evidence-report/1`.

A report must contain:

- profile ID;
- support state;
- assertion-scoped conformance level;
- evidence level;
- all 72 assertion results;
- executed checks;
- report-wide limitations.

Every `SUPPORTED` or `PARTIAL` result must:

1. reference at least one check ID;
2. reference only checks present in the same report;
3. reference only checks that passed;
4. contain explicit limitations.

Every result, including `UNSUPPORTED`, must contain a reason or limitation.

## 6. External adapter protocol

The support runner invokes an external profile adapter:

```bash
python tools/conformance/runner.py adapter \
  --output report.json \
  -- <adapter-command>
```

The fixture-pack path is appended to the command. The adapter must emit one JSON report.

The runner rejects:

- non-zero process exit;
- malformed JSON;
- missing required fields;
- duplicate assertion results;
- missing registered assertions;
- unknown extra IDs;
- invalid result statuses.

The P4 strict validator additionally rejects:

- wrong profile/support state;
- wrong support counts;
- unknown or failed referenced checks;
- `SUPPORTED`/`PARTIAL` without evidence;
- missing limitations;
- proposed `NK-EPI` promotion;
- C2 with local placeholder metadata;
- missing truth/C3/deletion boundaries.

## 7. Current PostgreSQL P4 adapter

Profile:

```text
native-kernel/postgresql-reference@0.4-p4
```

Current guarded result map:

```text
SUPPORTED:   41
PARTIAL:     13
UNSUPPORTED: 18
FAILED:       0
TOTAL:       72
```

The 18 unsupported results include all eight proposed `NK-EPI` assertions and accepted gaps such as independent profile translation, identity aliasing, cross-project authority, restore enforcement and most dedicated conflict behavior.

### 7.1 Profile-neutral checks

- registry version, assertion coverage and decision statuses;
- accepted identity golden vectors;
- invalid canonical identity inputs;
- semantic roles, explicit scope and source-bound Claim identity;
- explicit deny-by-default authority;
- Admission and Deletion Receipt overclaim rejection;
- deterministic reduction;
- explicit sequence/schema failures;
- semantic deletion/restriction transitions.

### 7.2 PostgreSQL checks

- migration idempotency;
- writer lease/epoch fencing;
- append, same-digest retry and idempotency conflict;
- rollback-safe contiguous sequence allocation;
- persisted replay equal to direct reduction;
- bounded Replay Receipt;
- projection load/destroy/rebuild;
- monotonic projection generation;
- stale-head rejection;
- stored canonical corruption detection.

### 7.3 Evidence checks

- exact profile/commit/run/Python/PostgreSQL metadata;
- complete assertion-to-check traceability.

## 8. Current P4 repository evidence

Initial successful C2 head:

```text
93710131fffdea7d9a586cc05e7f258c07fae707
```

```text
P4 run 31175767586 — PASS
Python 3.11 / PostgreSQL 16 — PASS
Python 3.11 / PostgreSQL 18 — PASS
Python 3.12 / PostgreSQL 16 — PASS
Python 3.12 / PostgreSQL 18 — PASS
P1/P2/P3 regressions — PASS
4 JSON artifacts retained for 30 days
```

Each artifact is bound to the run/head and contains one strict report.

The first P4 run `31175593261` failed at standalone adapter import after all unit/manifest/C1 integration checks passed. That failure remains useful negative evidence. The CLI path was fixed; report requirements were not weakened.

A later documentation head must repeat affected checks before merge. Earlier evidence remains valid only for its named SHA/run.

## 9. Meaning of P4 C2

```text
C2 applies to 41 SUPPORTED assertion results
PARTIAL assertions remain partial
UNSUPPORTED assertions remain unsupported
support_state remains PARTIAL
```

P4 C2 does not establish:

- support for all 72 assertions;
- storage neutrality;
- C3 cross-profile equivalence;
- accepted `NK-EPI`;
- truth or external authenticity;
- physical deletion;
- C4/C5;
- production readiness.

## 10. Fixture families

### Identity

`nk-id/1.0` vectors cover deterministic key ordering, NFC enforcement, rejection of floats/null, domain-separated IDs and golden/invalid cases.

### Event, idempotency and replay

`nk-event/1.0` covers contiguous ordering, payload/Event commitments, previous-hash continuity, idempotency retry/conflict and projection-failure boundaries.

P4 adds execution against a real PostgreSQL service, but does not cover every crash, fork, threat model or provider behavior.

### Deletion and restriction

`nk-deletion/1.0` covers semantic state transitions and Receipt proof limits. It does not prove provider, backup, media or key deletion.

### Epistemic boundaries

Fixtures exist for `NK-EPI-001…008`, but P4 retains all eight as `UNSUPPORTED` because the family remains proposed.

## 11. Equivalence classes

| Class | Required comparison |
|---|---|
| **Byte** | identical canonical bytes or identifiers under one declared contract/version |
| **Structural** | equivalent required fields/entities/relations with allowed non-semantic differences |
| **Semantic** | preserved identity, lineage, time, scope, authority, conflict and unknown meaning |
| **Behavioural** | equivalent accepted/rejected commands and observable outcomes in a bounded workload |

Every C3 claim must list allowed and forbidden differences. “Equivalent” without a definition is non-conforming language.

## 12. Why the matrix is not C3

Python 3.11/3.12 and PostgreSQL 16/18 exercise environment compatibility for one profile.

```text
4 matrix jobs
≠ 4 independent implementations
≠ profile diversity
≠ C3
```

P5 requires a materially independent SQLite profile and explicit comparison evidence.

## 13. Artifact boundary

Artifacts improve reproducibility but have finite retention. An artifact digest without retained bytes is not sufficient reproduction evidence.

Long-term release/evidence retention remains blocked by publication and licensing decisions, including Issue #18.

## 14. Non-conformance examples

```text
❌ Projection rows are edited and treated as history.
❌ Backend row IDs silently define semantic identity.
❌ Retrieval output becomes admitted knowledge without authority.
❌ Newest timestamp silently resolves semantic conflict.
❌ A hash chain is described as authenticity or consensus.
❌ ERASED is described as physical/global deletion.
❌ Unsupported assertions are omitted.
❌ A top-level C2 label is described as support for all 72.
❌ One PostgreSQL profile is described as C3.
❌ Proposed NK-EPI fixtures are described as accepted semantics.
❌ A replacement suite is described as recovered v0.1.2.1 evidence.
❌ Operator approval is presented as empirical proof.
```

## 15. Relationship to Issue #1

P1–P4 are accepted clean architecture/implementation lineage, not recovered historical design.

A future authentic import establishes evidence only for behavior proved by its original bytes/runtime/tests. It does not automatically satisfy current exact contracts, P4 mappings, `NK-EPI`, C3, C4, C5 or production readiness.

## 16. Next gate

P5 and C3 require a separate operator GO, a materially independent implementation profile, declared equivalence classes, comparison commands, negative cases and retained evidence.

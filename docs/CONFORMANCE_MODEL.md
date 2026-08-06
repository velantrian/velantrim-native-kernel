# 🧪 Conformance Model

> **Status:** `PROPOSED DOCUMENTATION CONTRACT / FIXTURE-INTEGRITY TOOLING IMPLEMENTED IN PROPOSAL BRANCH / NOT A CERTIFICATION PROGRAM`  
> **Purpose:** define how a present or future implementation can demonstrate that it follows Native Kernel architecture

## 1. Why conformance matters

Technology independence must be tested, not merely declared. A system is not a Native Kernel implementation because it uses the same terminology.

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

Levels are assertion-scoped and do not replace decision status, implementation status, evidence level, maturity or operator approval.

## 3. Contract families

The accepted ADR-0010 ownership map is:

```text
NK-SEM — semantic roles
NK-ID  — identity and canonical encoding
NK-EVT — event, observation and recorded change
NK-AUT — authority and admission
NK-CFL — conflict and explicit unknowns
NK-EQV — conformance and semantic equivalence
```

`NK-EPI-001…008` remains a proposed epistemic assertion family associated with ADR-0008.

Exact v1 proposals for Issues #14–#17 are maintained in:

- [`contracts/NORMATIVE_CONTRACTS_V1.md`](./contracts/NORMATIVE_CONTRACTS_V1.md);
- [`contracts/NORMATIVE_CONTRACTS_V1.ru.md`](./contracts/NORMATIVE_CONTRACTS_V1.ru.md);
- ADR-0011 through ADR-0014;
- machine-readable `../contracts/registry.json`.

## 4. Required semantic areas

A profile must explicitly map supported and unsupported assertions for:

- identity and lineage;
- authoritative history and ordering;
- deterministic reduction and schema/reducer versioning;
- disposable projections and rebuild;
- valid/observation/record time;
- conflict detection versus resolution;
- admission authority and policy;
- retrieval/selection without truth promotion;
- Receipt proof boundaries;
- deletion, restriction, retention and residual data;
- world/epistemic representation discipline where claimed.

Unsupported assertions remain visible. A profile cannot obtain a higher level by silently skipping them.

## 5. Executable artifact status

The proposal branch `agent/contracts-14-17` introduces:

```text
contracts/
├── registry.json        # stable family/assertion registry
├── schema-bundle.json   # neutral JSON Schema bundle
└── fixture-pack.json    # identity, event, deletion and epistemic corpora

tools/conformance/
├── runner.py            # standard-library fixture validator / adapter launcher
└── README.md

tests/test_conformance_runner.py
.github/workflows/conformance-fixtures.yml
```

Current evidence boundary:

```text
fixture-integrity tooling: IMPLEMENTED IN BRANCH
local focused tests:       5 PASS
local fixture validation:  PASS
Kernel runtime:            NOT IMPLEMENTED
Kernel conformance:        UNSUPPORTED
C2:                        NOT YET ESTABLISHED
C3:                        NOT ESTABLISHED
```

The built-in Python reader validates fixture integrity and deterministic reference algorithms. It does not store Kernel history, execute a reducer, rebuild a real projection or perform deletion.

## 6. Fixture families

### Identity

The proposed `nk-id/1` vectors cover:

- deterministic key ordering;
- NFC enforcement;
- rejection of floats and explicit null;
- domain-separated content/Claim/lineage IDs;
- golden and invalid cases.

### Event and replay boundary

The proposed scenarios cover contiguous single-writer ordering, payload/event commitments, previous-hash continuity and projection failure after committed history. They do not constitute a durable append implementation or crash-injection evidence.

### Deletion and restriction

The proposed state-machine scenarios cover restriction, erase request, partial completion, retry, retention hold, crypto-erasure/physical deletion and Receipt proof limits. They do not prove provider, backup or media deletion.

### Epistemic boundaries

Positive and negative fixtures exist for each proposed assertion:

| Assertion | Required discipline |
|---|---|
| `NK-EPI-001` | representation is not silently equated with represented reality |
| `NK-EPI-002` | observation is not silently equated with complete explanation |
| `NK-EPI-003` | transformation or assembly is not proof of origin |
| `NK-EPI-004` | unknown is not silently encoded as false |
| `NK-EPI-005` | missing provenance remains explicit |
| `NK-EPI-006` | current profile limits are not universalized into impossibility |
| `NK-EPI-007` | worldview-sensitive Claims retain domain and scope |
| `NK-EPI-008` | model/retrieval/utility/proposal output is not silently admitted as knowledge |

Fixture presence does not accept ADR-0008 or prove runtime enforcement.

## 7. Equivalence classes

| Class | Required comparison |
|---|---|
| **Byte** | identical canonical bytes or identifiers under one declared contract/version |
| **Structural** | equivalent required fields, entities and relations with allowed non-semantic differences |
| **Semantic** | preserved identity, lineage, time, scope, authority, conflict and unknown meaning |
| **Behavioural** | equivalent accepted/rejected commands and observable outcomes in a bounded workload |

Every claim must list allowed and forbidden differences. “Equivalent” without a definition is non-conforming language.

## 8. External adapter protocol

The support runner may invoke an external profile adapter:

```bash
python tools/conformance/runner.py adapter --output report.json -- <adapter-command>
```

The fixture-pack path is appended to the command. The adapter must emit one JSON report. Non-zero exit, malformed output, missing support state or silent skip is a failure.

A profile evidence report should include:

```yaml
report_version: nk-evidence-report/1
profile_id: <profile>
repository_commit: <sha>
contract_versions: [<versions>]
fixture_ids: [<ids>]
support_state: SUPPORTED | UNSUPPORTED | PARTIAL | FAILED
kernel_runtime_conformance: UNSUPPORTED | C0 | C1 | C2 | C3 | C4 | C5
evidence_level: DOCUMENTED | LOCALLY_TESTED | REPOSITORY_REPRODUCED | SHADOW_EVALUATED | OPERATIONALLY_VALIDATED
checks: [<results>]
limitations: [<limits>]
```

## 9. First real Kernel experiment

A future implementation profile should:

```text
load authoritative history
→ derive state
→ destroy all disposable projections
→ rebuild from empty projections
→ compare declared equivalence
→ emit reconstruction Receipt
```

Minimum proof includes invalid-event handling, exact versions, conflict visibility, temporal preservation and evidence commit. Fixture validation alone cannot satisfy this experiment.

## 10. Non-conformance examples

```text
❌ Projection rows are edited and treated as history.
❌ Backend row IDs silently define semantic identity.
❌ An LLM or retrieval result becomes admitted knowledge without authority.
❌ Newest timestamp silently resolves semantic conflict.
❌ A hash chain is described as complete authenticity or consensus.
❌ Tombstone/ERASED is described as physical or global deletion.
❌ Unsupported assertions are omitted from the report.
❌ Local fixture tests are presented as C2 or C3 Kernel evidence.
❌ A replacement suite is presented as recovered v0.1.2.1 evidence.
❌ Operator approval is presented as empirical proof.
```

## 11. Relationship to Issue #1

Issue #1 remains blocked by authentic source recovery. The Issues #14–#17 fixture/contract track is a new, explicitly separated architecture lineage.

A future authentic import may establish C2 only for assertions proved by its original committed runtime/tests. It does not automatically satisfy the proposed exact contracts, `NK-EPI`, C3, C4, C5 or production readiness.

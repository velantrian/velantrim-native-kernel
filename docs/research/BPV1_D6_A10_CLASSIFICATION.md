# BPV1-001 D6 — A10 Hypothesis Classification

**State:** `CANDIDATE / AUTHORITATIVE AFTER MERGE`  
**Protocol:** `nk-a10-hypothesis-classification/1`  
**Classification ID:** `BPV1-001-D6-A10-classification-v1`  
**Input truth checkpoint:** `4f1bdfd4e8203b1234972d4c06ff0ce15d1c28ec`  
**Runtime expansion:** `FROZEN`

## Purpose

D6 converts the qualified BPV1-001 evidence into explicit A10 research outcomes. It does not rerun or modify the experiment, and it does not copy the aggregate `SUPPORTED_FOR_SCOPE` outcome to every hypothesis.

Authoritative inputs are:

- frozen BPV1 plan merge `a538d7f1e28858a88b9ee777ac7d6e05b85943db`;
- frozen plan SHA-256 `7fe8174c604678c6b79d3fdeae83d7c5ab0d2fb15bfe343d41659d05d9496ad0`;
- historical D5 merge `a191e9c868c14af34a269dcdfae44406f1013bda`;
- D5-R1 qualification merge `3856740570620fb2243e2f0da76359281ec4068f`;
- external qualification `QUALIFIED`;
- unchanged frozen evaluator outcome `SUPPORTED_FOR_SCOPE` with `12/12` mandatory fixtures PASS.

Allowed A10 outcomes remain exactly:

```text
SUPPORTED_FOR_SCOPE
WEAKENED
REFUTED
INDETERMINATE
NOT_TESTED
```

## Classification summary

| Hypothesis | Preregistered role | D6 outcome | Core reason |
|---|---|---|---|
| `A10-H01` | secondary | `SUPPORTED_FOR_SCOPE` | A materially different Rust/custom-bounded representation preserved mandatory obligations without importing current Event/reducer/Receipt/SQL structures. |
| `A10-H02` | primary | `SUPPORTED_FOR_SCOPE` | FX11 preserved current accountability with no authoritative per-operation Event log and no exact-replay requirement. |
| `A10-H03` | informative / not adjudicated | `NOT_TESTED` | No representation-migration protocol tested identity/continuation across migration. |
| `A10-H04` | secondary | `SUPPORTED_FOR_SCOPE` | FX01/FX05/FX09 preserved Unknown, unresolved plurality and scoped uncertainty without forced binary/scalar collapse. |
| `A10-H05` | primary | `SUPPORTED_FOR_SCOPE` | FX04/FX06 plus bounded workload thresholds preserved revision accountability, retention scope and loss witnesses without unbounded predecessor retention. |
| `A10-H06` | not tested | `NOT_TESTED` | Physical and cryptographic erasure were explicitly not applicable to BPV1-001. |
| `A10-H07` | secondary | `SUPPORTED_FOR_SCOPE` | The qualified Rust/history-model realization provides a stronger evidence class than storage-profile variation inside one Python lineage, while remaining same-repository/conventional-digital evidence. |
| `A10-H08` | not tested | `NOT_TESTED` | No analog or neuromorphic realization was tested. |
| `A10-H09` | not tested | `NOT_TESTED` | No probabilistic substrate or statistical-conformance protocol was tested. |
| `A10-H10` | informative / not adjudicated | `NOT_TESTED` | Language, history model and storage representation varied together; storage/computation axes were not independently isolated. |
| `A10-H11` | not tested | `NOT_TESTED` | BPV1-001 did not preregister H11 as a falsification target; existing governance support is not rewritten. |
| `A10-H12` | secondary | `SUPPORTED_FOR_SCOPE` | FX10/FX12 demonstrated actionable loss-aware/scoped comparison and rejected false full conformance despite matching visible values. |

Counts:

```text
SUPPORTED_FOR_SCOPE: 6
WEAKENED:             0
REFUTED:              0
INDETERMINATE:        0
NOT_TESTED:           6
TOTAL:               12
```

## Why the six supported hypotheses are bounded support

### A10-H01

The subject is written in Rust, uses a custom bounded snapshot/history representation and does not reuse the current Native Kernel implementation, Event envelope, reducer, Receipt oracle shape or SQL profile. That is meaningful representation-independence evidence inside BPV1-001. It is not evidence for analog, neuromorphic, probabilistic or arbitrary future substrates.

### A10-H02

FX11 is the direct falsification attempt. Current accountability remained available while the external qualifier established `authoritative_per_operation_append_log=false` and `exact_replay_required=false`. HR01 was not observed.

### A10-H04

FX01 preserved `UNKNOWN` without False coercion; FX05 preserved unresolved plurality without an unauthorized winner; FX09 retained scoped uncertainty when counterevidence was withheld. HR03 was not observed.

### A10-H05

FX04 preserved retained-scope revision/supersession lineage; FX06 compacted detail only outside declared retention scope with a valid loss witness. The complete 512-mutation workload remained within the durable-state, retained-predecessor, retained-witness and growth bounds. HR02 and HR07 were not observed.

### A10-H07

The cross-language/history-model subject survived all mandatory fixtures without copying current Native Kernel/Event/reducer/Receipt/SQL structures. This is stronger portability evidence than PostgreSQL↔SQLite variation inside one Python lineage. It remains same-repository custody, not an independently authored implementation, and uses conventional digital computation. `SUPPORTED_FOR_SCOPE` therefore means stronger evidence class, not independent validation.

### A10-H12

FX10 emitted `LOSSY` rather than false full conformance. FX12 detected material semantic divergence even when final visible values matched and refused full conformance. This demonstrates that scoped/loss-aware comparison can remain actionable inside BPV1-001.

## Why H03 and H10 remain NOT_TESTED

The plan deliberately marked H03 and H10 `informative_not_adjudicated`.

- H03 requires a migration experiment that preserves or breaks identity/continuation relations across source and target representations. BPV1-001 did not perform that migration.
- H10 requires independent variation of storage and computation mechanisms. BPV1-001 changed multiple axes together, so it cannot isolate that claim.

Informative observations are not promoted to support.

## Explicitly untested hypotheses

H06, H08, H09 and H11 remain `NOT_TESTED` exactly as preregistered.

- H06: no physical/cryptographic erasure observability.
- H08: no non-address-based analog/neuromorphic substrate.
- H09: no probabilistic computation/statistical conformance.
- H11: no preregistered BPV1 falsification attempt for the governance/reproducibility claim.

The pre-existing A10 prose around H11 is preserved as historical research context; D6 does not rewrite it.

## Non-claims

D6 does not establish:

- Final Canon;
- production readiness;
- universal substrate portability;
- independent implementation team or custody;
- independent computation-model evidence;
- analog, neuromorphic, probabilistic or quantum support;
- product runtime suitability.

D6 does not change BPV1-001 scenario identity, plan, oracle, expected fixture outcomes, thresholds, HR01-HR10, subject implementation, or evidence bytes. Product runtime integration remains unauthorized and runtime expansion remains `FROZEN`.

## Next gate

After this D6 classification record becomes authoritative through merge and post-merge validation, the next bounded gate is:

```text
D7_INTEGRATED_RE_REVIEW
```

D7 must re-read A1-A10, the integrated review, IAR-1/IAR-1-R1, the frozen BPV1 plan, D5-R1 evidence qualification and this D6 classification. It may revise the provisional architecture assessment, but it may not silently promote Final Canon or thaw runtime.

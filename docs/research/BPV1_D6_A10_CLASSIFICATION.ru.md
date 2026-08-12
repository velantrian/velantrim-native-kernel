# BPV1-001 D6 — Классификация гипотез A10

**Состояние:** `CANDIDATE / AUTHORITATIVE AFTER MERGE`  
**Протокол:** `nk-a10-hypothesis-classification/1`  
**Classification ID:** `BPV1-001-D6-A10-classification-v1`  
**Входной truth checkpoint:** `4f1bdfd4e8203b1234972d4c06ff0ce15d1c28ec`  
**Runtime expansion:** `FROZEN`

## Цель

D6 превращает квалифицированные evidence BPV1-001 в явные исследовательские outcomes A10. Он не перезапускает и не меняет эксперимент и не переносит aggregate `SUPPORTED_FOR_SCOPE` автоматически на каждую гипотезу.

Authoritative inputs:

- frozen BPV1 plan merge `a538d7f1e28858a88b9ee777ac7d6e05b85943db`;
- frozen plan SHA-256 `7fe8174c604678c6b79d3fdeae83d7c5ab0d2fb15bfe343d41659d05d9496ad0`;
- historical D5 merge `a191e9c868c14af34a269dcdfae44406f1013bda`;
- D5-R1 qualification merge `3856740570620fb2243e2f0da76359281ec4068f`;
- external qualification `QUALIFIED`;
- неизменённый frozen evaluator outcome `SUPPORTED_FOR_SCOPE`, `12/12` mandatory fixtures PASS.

Допустимые outcomes A10 остаются ровно такими:

```text
SUPPORTED_FOR_SCOPE
WEAKENED
REFUTED
INDETERMINATE
NOT_TESTED
```

## Итоговая классификация

| Гипотеза | Preregistered role | D6 outcome | Основная причина |
|---|---|---|---|
| `A10-H01` | secondary | `SUPPORTED_FOR_SCOPE` | Существенно отличающаяся Rust/custom-bounded representation сохранила mandatory obligations без импорта текущих Event/reducer/Receipt/SQL structures. |
| `A10-H02` | primary | `SUPPORTED_FOR_SCOPE` | FX11 сохранил current accountability без authoritative per-operation Event log и без exact replay requirement. |
| `A10-H03` | informative / not adjudicated | `NOT_TESTED` | Не было migration protocol, проверяющего identity/continuation через миграцию representation. |
| `A10-H04` | secondary | `SUPPORTED_FOR_SCOPE` | FX01/FX05/FX09 сохранили Unknown, unresolved plurality и scoped uncertainty без принудительного binary/scalar collapse. |
| `A10-H05` | primary | `SUPPORTED_FOR_SCOPE` | FX04/FX06 и bounded thresholds сохранили revision accountability, retention scope и loss witnesses без unbounded predecessor retention. |
| `A10-H06` | not tested | `NOT_TESTED` | Physical и cryptographic erasure были явно not applicable для BPV1-001. |
| `A10-H07` | secondary | `SUPPORTED_FOR_SCOPE` | Qualified Rust/history-model realization даёт более сильный evidence class, чем storage-profile variation внутри одной Python lineage, оставаясь same-repository/conventional-digital evidence. |
| `A10-H08` | not tested | `NOT_TESTED` | Analog или neuromorphic realization не тестировалась. |
| `A10-H09` | not tested | `NOT_TESTED` | Probabilistic substrate и statistical-conformance protocol не тестировались. |
| `A10-H10` | informative / not adjudicated | `NOT_TESTED` | Language, history model и storage representation менялись вместе; storage/computation axes не были изолированы независимо. |
| `A10-H11` | not tested | `NOT_TESTED` | BPV1-001 не preregistered H11 как falsification target; существующий governance support не переписывается. |
| `A10-H12` | secondary | `SUPPORTED_FOR_SCOPE` | FX10/FX12 показали actionable loss-aware/scoped comparison и отказ от ложного full conformance при совпадающих visible values. |

Итоговые количества:

```text
SUPPORTED_FOR_SCOPE: 6
WEAKENED:             0
REFUTED:              0
INDETERMINATE:        0
NOT_TESTED:           6
TOTAL:               12
```

## Почему шесть гипотез получили только bounded support

### A10-H01

Subject написан на Rust, использует custom bounded snapshot/history representation и не переиспользует текущие Native Kernel implementation, Event envelope, reducer, Receipt oracle shape или SQL profile. Это meaningful representation-independence evidence внутри BPV1-001, но не evidence для analog, neuromorphic, probabilistic или arbitrary future substrates.

### A10-H02

FX11 — прямой falsification attempt. Current accountability сохранился, а external qualifier установил `authoritative_per_operation_append_log=false` и `exact_replay_required=false`. HR01 не наблюдался.

### A10-H04

FX01 сохранил `UNKNOWN` без coercion в False; FX05 сохранил unresolved plurality без unauthorized winner; FX09 сохранил scoped uncertainty при withheld counterevidence. HR03 не наблюдался.

### A10-H05

FX04 сохранил retained-scope revision/supersession lineage; FX06 compacted detail только за пределами declared retention scope и сохранил valid loss witness. Полный workload из 512 mutations остался в durable-state, retained-predecessor, retained-witness и growth bounds. HR02 и HR07 не наблюдались.

### A10-H07

Cross-language/history-model subject прошёл все mandatory fixtures без копирования текущих Native Kernel/Event/reducer/Receipt/SQL structures. Это более сильный portability evidence class, чем PostgreSQL↔SQLite variation внутри одной Python lineage. Но custody остаётся same-repository, implementation не создана независимой командой, а computation остаётся conventional digital. Поэтому `SUPPORTED_FOR_SCOPE` означает более сильный evidence class, а не independent validation.

### A10-H12

FX10 выдал `LOSSY`, а не ложный full conformance. FX12 обнаружил material semantic divergence даже при совпадающих final visible values и отказал в full conformance. Это показывает, что scoped/loss-aware comparison может оставаться actionable внутри BPV1-001.

## Почему H03 и H10 остаются NOT_TESTED

Plan намеренно пометил H03 и H10 как `informative_not_adjudicated`.

- H03 требует migration experiment, который сохраняет или ломает identity/continuation relations между source и target representations. BPV1-001 такую migration не выполнял.
- H10 требует независимого изменения storage и computation mechanisms. BPV1-001 менял несколько axes одновременно, поэтому не изолирует этот claim.

Informative observations не повышаются до support.

## Явно не протестированные гипотезы

H06, H08, H09 и H11 остаются `NOT_TESTED` ровно в соответствии с preregistration.

- H06: нет physical/cryptographic erasure observability.
- H08: нет non-address-based analog/neuromorphic substrate.
- H09: нет probabilistic computation/statistical conformance.
- H11: нет preregistered BPV1 falsification attempt для governance/reproducibility claim.

Предшествующий A10 prose вокруг H11 сохраняется как исторический research context; D6 его не переписывает.

## Non-claims

D6 не устанавливает:

- Final Canon;
- production readiness;
- universal substrate portability;
- independent implementation team или custody;
- independent computation-model evidence;
- analog, neuromorphic, probabilistic или quantum support;
- product runtime suitability.

D6 не меняет BPV1-001 scenario identity, plan, oracle, expected fixture outcomes, thresholds, HR01-HR10, subject implementation или evidence bytes. Product runtime integration остаётся unauthorized, runtime expansion — `FROZEN`.

## Следующий gate

После того как этот D6 classification record станет authoritative через merge и post-merge validation, следующий bounded gate:

```text
D7_INTEGRATED_RE_REVIEW
```

D7 должен заново прочитать A1-A10, integrated review, IAR-1/IAR-1-R1, frozen BPV1 plan, D5-R1 evidence qualification и эту D6 classification. Он может пересмотреть provisional architecture assessment, но не может молча повысить Final Canon или разморозить runtime.

# A10-H11 Preregistration — разделение лаборатории и Canon

**Protocol:** `nk-h11-preregistration/1`  
**Plan ID:** `H11-001-c5-lab-canon-separation-v1`  
**State:** `PREREGISTERED / EXECUTION_NOT_AUTHORIZED`  
**Target:** `A10-H11` / `RAVP-H11-LAB-CANON-SEPARATION`  
**Selection merge:** `bcd3b3f6c9d898315c93e5d24b5d0e02c95508cc` / PR #126  
**Runtime:** `FROZEN`

## Вопрос

Может ли точное воспроизведение принятого лабораторного evidence зависеть от конкретных Python/SQL/JSON/hash/Event/reducer-механизмов, в то время как Architecture specification и semantic oracle остаются на уровне смысла и не превращают эти механизмы в универсальные требования?

Эта preregistration не утверждает, что H11 поддержана. `A10-H11` остаётся `NOT_TESTED`, пока не завершены отдельно допущенные execution и независимая semantic adjudication.

## Зафиксированный лабораторный объект

Используется уже существующий repository-resident ADR-0023 C5 evidence bundle:

```text
bundle_id: native-kernel/c5/2026-08-08-adr0023
manifest: evidence/c5/2026-08-08-adr0023/manifest.json
protocol: nk-evidence-bundle/1
plan: native-kernel/c5-bounded-rehearsal-v1
checkpoints: 2
artifacts: 8 ZIPs
SQLite evidence floor: 3.51.3
```

Fail-closed verifier:

```text
python tools/evidence/verify_bundle.py evidence/c5/2026-08-08-adr0023/manifest.json --repo .
```

Точные bytes, ZIP inventories, sizes, SHA-256 digests, environment snapshots, metrics и checkpoint identities являются требованиями **только для воспроизведения лабораторного evidence**. Их точность не превращает Python, PostgreSQL, SQLite, SQL, JSON, ZIP, SHA-256, Event, reducer, Receipt, integer sequences или текущие report schemas в Architecture Canon.

## Зафиксированные H11 obligations

- `H11-O01` — laboratory evidence/profile mechanisms отделены от Architecture authority.
- `H11-O02` — semantic obligations отделимы от текущих механизмов их реализации.
- `H11-O03` — historical evidence identity воспроизводится без переписывания Architecture history или scope прошлого evidence.
- `H11-O04` — Architecture falsification/conformance выражается на meaning level без превращения текущих profile bytes в обязательный oracle input только потому, что они нужны исторической лаборатории.

## Dependency graph и leakage rubric

Execution должен построить полный graph из Architecture obligations, laboratory evidence, profile mechanisms и validator/oracle nodes. Зависимости классифицируются так:

- `LAB_ONLY` — обязательны только для точного воспроизведения указанного лабораторного artifact;
- `PROFILE_SPECIFIC` — допустимая profile realization, но не Architecture authority;
- `MEANING_LEVEL_JUSTIFIED` — требование выражено независимо от конкретного механизма;
- `UNJUSTIFIED_CANON_DEPENDENCY` — конкретный lab/profile mechanism становится обязательным для Architecture лишь потому, что историческая лаборатория зависит от него.

`UNJUSTIFIED_CANON_DEPENDENCY` — hard failure class. Для scoped support требуется `mandatory_profile_leakage_count == 0` и mechanism-neutral Architecture obligations/falsifiers.

## Independence gate

H11 требует `INDEPENDENT_SEMANTIC_ORACLE`. Авторы Architecture/preregistration не могут **самостоятельно сертифицировать H11**.

До execution admission должен существовать qualifying reviewer/reproducer с конкретно описанным основанием независимости; он не должен быть автором этой preregistration или frozen leakage rubric. Если такого reviewer/reproducer нет, корректный результат gate:

`BLOCKED_NO_QUALIFYING_INDEPENDENT_REVIEWER_REPRODUCER`

Этот blocker не является refutation H11 и не может превращаться в выдуманную validation.

## Зафиксированная adjudication

- `SUPPORTED_FOR_SCOPE` — exact lab verification проходит, qualifying independence подтверждена, leakage count равен нулю, Architecture остаётся meaning-level, история не переписана.
- `WEAKENED` — hard refutation нет, но часть Architecture wording требует сужения/profile scoping; post-hoc rescue под тем же experiment ID запрещён.
- `REFUTED` — наблюдается preregistered hard refutation.
- `INDETERMINATE` — недостаточно evidence, dependency visibility или independence.
- `NOT_TESTED` — qualifying execution/adjudication ещё не было.

Hard refutation:

> В данном scope необходимая принятая Architecture obligation не может оставаться воспроизводимой/проверяемой без превращения profile-specific C5 laboratory mechanism в универсальную Architecture только потому, что historical C5 evidence reproduction зависит от этого механизма.

## Authority boundary

```text
H11 preregistration ≠ H11 execution admission
execution admission ≠ execution
exact laboratory reproduction ≠ Architecture Canon
A10-H11 ≠ composition/federation
NOT_TESTED ≠ SUPPORTED
```

Этот plan сам фиксирует:

```text
implementation_authorized_by_this_plan: false
execution_authorized_by_this_plan: false
runtime_expansion: FROZEN
product_runtime_thaw: false
Final Canon: DEFERRED / NOT_AUTHORIZED
production_authorized: false
```

Следующий gate после authoritative preregistration — `A10_H11_EXECUTION_ADMISSION`. Он обязан зафиксировать digest plan, machine-readable dependency-graph format, разделение raw observations и adjudication, а также qualifying reviewer/reproducer evidence до любого execution.
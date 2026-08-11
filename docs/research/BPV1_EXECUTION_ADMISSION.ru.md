# 🔒 BPV-1 Execution Admission — Candidate Package

**[English](./BPV1_EXECUTION_ADMISSION.md) · [Русский](./BPV1_EXECUTION_ADMISSION.ru.md)**

> **Protocol:** `nk-bpv1-execution-admission/1`  
> **Admission ID:** `BPV1-001-execution-admission-v1`  
> **Scenario:** `BPV1-001-cross-lineage-bounded-accountability-v1`  
> **State:** `CANDIDATE_PACKAGE / EXECUTION_NOT_ADMITTED`

Этот package переводит уже authoritative preregistration в executable **oracle boundary до появления какого-либо Rust subject implementation**. Он не выполняет BPV-1 и не thaw product runtime.

## Frozen plan binding

```text
plan merge: a538d7f1e28858a88b9ee777ac7d6e05b85943db
plan SHA-256: 15c830ed195762d571cf675900303dfbfb29bf01a5cde2aac814388319585a91
plan path: docs/research/BPV1_PREREGISTRATION.json
```

Admission validator обязан пересчитать exact SHA-256 и проверить, что authoritative plan merge является ancestor. Semantically similar edited plan не является тем же admitted plan.

## External oracle package

```text
fixture protocol: nk-bpv1-fixtures/1
observation protocol: nk-bpv1-observations/1
evaluation protocol: nk-bpv1-evaluation/1
oracle authority: BPV1-ORACLE-001
fixture spec: experiments/bpv1/BPV1-001/admission/fixtures.json
evaluator: tools/bpv1/evaluate.py
```

Fixture file содержит ровно 12 preregistered fixture families. Evaluator принимает implementation-neutral observations; он не инспектирует Rust structs, current Python domain classes, SQL schemas, Event envelopes, reducers, Receipts или current ID prefixes.

Failure mandatory predicate даёт `REFUTED`; missing mandatory observable даёт `INDETERMINATE`; отсутствие observed fixtures даёт `NOT_TESTED`; полное mandatory success даёт `SUPPORTED_FOR_SCOPE`. Final A10 hypothesis classification остаётся later stage и не является automatic Canon promotion.

## Evaluator self-test до subject

`tests/test_bpv1_execution_admission.py` должен до появления subject source доказать:

- synthetic conforming observation bundle → `SUPPORTED_FOR_SCOPE`;
- semantic hard failure → `REFUTED`;
- missing mandatory observable → `INDETERMINATE`;
- отсутствие fixture observations → `NOT_TESTED`;
- wrong plan digest отвергается;
- превышение bounded-state limits даёт `REFUTED`;
- reuse current Native Kernel/Event/reducer/Receipt/SQL semantics как subject boundary даёт `REFUTED` или rejection scope validator.

Это oracle self-tests, не BPV-1 evidence.

## Rust toolchain и source boundary

```text
Rust channel: 1.97.1
language role: EXPERIMENTAL_INSTRUMENT_NOT_CANON
subject root: experiments/bpv1/BPV1-001/subject
independent team: NOT_ESTABLISHED
independent custody: NOT_ESTABLISHED
independent computation model: NOT_ESTABLISHED / CONVENTIONAL_DIGITAL
```

`experiments/bpv1/BPV1-001/rust-toolchain.toml` pin toolchain. Subject root должен отсутствовать в этом admission package. Future subject work изолируется под этим root и не может регистрировать product runtime/profile или менять `native_kernel/**`, `contracts/**`, `profiles/**`, current C5 evidence, migrations или ADR semantics.

## Static no-product-integration audit

`tools/bpv1/audit_scope.py` проверяет admission diff от current pre-admission main `20484a151bc7011509579353c2cf78845e3c33f9`. Admission packaging может касаться только declared admission docs/oracle/tooling/tests/workflow paths. Subject source в этом package запрещён.

## Two-phase admission rule

Этот package не может admit сам себя.

```text
#112 package merge
= fixtures/oracle/toolchain/source boundary READY
≠ execution admitted

separate post-merge state checkpoint
= binds #112 merge + exact/post-merge CI + scope audit
= may admit BPV1-001 subject implementation/execution only
≠ product runtime thaw
```

До authoritative separate checkpoint:

```text
BPV-1 execution: BLOCKED_PENDING_EXECUTION_ADMISSION
runtime expansion: FROZEN
product runtime thaw: NO
production: false
```

## Non-authorization

Ни этот candidate package, ни его future bounded admission не решают Issue #18, не принимают Issue #74/ADR-0024, не авторизуют reducer-v2, new Event verbs, NK-EPI runtime, Track H source admission, Final Canon, production и не доказывают universal substrate independence.

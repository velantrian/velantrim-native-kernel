# Спецификация контролируемого импорта Issue #1

> **Статус документа:** `PROPOSED / DOCUMENTED`  
> **Полномочие решения:** оператор/maintainer  
> **Целевой снимок:** заявленный внешний `v0.1.2.1`  
> **Состояние репозитория:** `DOCUMENTED_ONLY / NO PUBLIC RUNTIME`  
> **Текущее состояние исполнения:** `BLOCKED BY AUTHENTIC SOURCE RECOVERY`

## 1. Назначение

Документ сводит исполнимый gate для Issue #1, не изменяя Architecture Canon Native Kernel.

Нельзя смешивать два этапа:

```text
Stage 0.5 — восстановление аутентичного источника
        ↓ только после подтверждения происхождения
Stage 1 — точный контролируемый импорт
```

Заявленные реализация `v0.1.2.1` и исходный набор из 44 тестов являются внешним свидетельством. Их нет в `main`, а доступные источники проекта пока не дали аутентичный архив.

Приблизительную реконструкцию, clean-room реализацию, заново созданные тесты, рефакторинг или semantic redesign запрещено обозначать как проверенный снимок `v0.1.2.1`.

## 2. Stage 0.5 — Authentic Source Recovery

### 2.1 Цель

Найти исходное расположение или неизменяемый архив внешнего checkpoint `v0.1.2.1` и исходного набора из 44 тестов.

### 2.2 Разрешённая работа, пока этап заблокирован

- поиск в известных локальных архивах, backup, экспортированных workspace, старых ветках, носителях и прежних средах разработки;
- регистрация каждого проверенного расположения и результата;
- подготовка шаблонов manifest, CI и validation без runtime-claims;
- инвентаризация ожиданий из документации только как ожиданий, а не как восстановленного исходника;
- сохранение всех candidate-artifacts в read-only режиме до provenance review.

### 2.3 Запрещённая работа, пока этап заблокирован

- реконструировать реализацию по документации и называть её `v0.1.2.1`;
- создать 44 новых теста и представить их как исходный suite;
- повышать внешнее свидетельство до repository evidence;
- менять `STATUS.md` на `RUNNABLE RESEARCH PROTOTYPE`;
- считать совпадающее поведение доказательством аутентичности исходника;
- смешивать source recovery с Curiosity Core, causality, Event Integrity, Titan, Crystal или redesign read-path.

### 2.4 Журнал восстановления

Каждый проход поиска должен фиксировать:

```yaml
search_id: NK-SRC-RECOVERY-YYYYMMDD-NNN
performed_at: YYYY-MM-DDTHH:MM:SSZ
performed_by: operator-or-reviewer
locations_checked:
  - location: description
    access_mode: read-only
    result: found | not_found | inaccessible
candidate_artifacts:
  - path_or_reference: value
    size_bytes: 0
    sha256: value
    status: unverified_candidate
notes: free text
```

### 2.5 Exit gate Stage 0.5

Stage 1 можно начинать только при выполнении всех условий:

- [ ] найден аутентичный архив или исходное расположение;
- [ ] задокументирована lineage источника;
- [ ] архив сохранён read-only;
- [ ] записан SHA-256 всего архива;
- [ ] исходный test inventory присутствует и доступен для проверки;
- [ ] оператор явно разрешил controlled import.

Если источник не восстановлен после объявленного процесса поиска, проект должен обозначить `v0.1.2.1` как `LOST / NON-REPRODUCIBLE EXTERNAL CHECKPOINT` и начать новую clean implementation с отдельной версией. Новая реализация не наследует старый evidence state.

## 3. Stage 1 — Exact Controlled Import

### 3.1 Scope

Import PR должен содержать:

1. запечатанный аутентичный source snapshot;
2. полный исходный test suite;
3. исходные или максимально точно восстановленные metadata среды;
4. cryptographic provenance manifest;
5. минимальный repository wrapper для запуска sealed source;
6. compatibility CI;
7. benchmark workload harness со стабильными benchmark ID;
8. contract-to-test traceability review.

### 3.2 Явно отложено

Import PR не должен реализовывать или перерабатывать:

- broad-query optimization;
- полную write idempotency;
- Event Integrity;
- multi-writer concurrency;
- полную bi-temporal semantics;
- lifecycle разрешения конфликтов;
- State Checkpoints;
- Curiosity Core;
- causal relation runtime;
- runtime-интеграцию Titan или Crystal;
- production security, privacy или availability claims.

## 4. Раскладка репозитория

Точный источник должен оставаться sealed и отличаться от repository adapters:

```text
prototype/
├── recovered/
│   └── v0.1.2.1/          # неизменяемые восстановленные файлы
├── import_wrapper/         # минимальный adapter; без semantic redesign
├── manifests/
│   └── v0.1.2.1.json
├── benchmarks/
└── tests/                  # исходные тесты или точно сохранённая раскладка
```

Перемещение и переименование файлов не считаются автоматически безопасными. Каждая трансформация декларируется. Предпочтительно сохранить исходные пути внутри `prototype/recovered/v0.1.2.1/` и адаптировать запуск вокруг них.

## 5. Provenance manifest

Hash только repository-файлов не доказывает аутентичность источника. Manifest должен связывать восстановленный архив, source files, repository files, transformations, test inventory, environment и import commit.

Минимальная схема:

```json
{
  "manifest_version": "1.1",
  "snapshot_id": "v0.1.2.1",
  "snapshot_status": "AUTHENTIC_RECOVERED",
  "source_archive": {
    "filename": "<archive-name>",
    "sha256": "<archive-sha256>",
    "size_bytes": 0,
    "recovered_from": "<location-description>",
    "recovered_at": "YYYY-MM-DDTHH:MM:SSZ",
    "recovered_by": "<operator-or-reviewer>"
  },
  "files": [
    {
      "original_path": "kernel.py",
      "repository_path": "prototype/recovered/v0.1.2.1/kernel.py",
      "source_sha256": "<sha256>",
      "repository_sha256": "<sha256>",
      "size_bytes": 0,
      "role": "runtime",
      "transformation": "NONE"
    }
  ],
  "test_inventory": {
    "declared_count": 44,
    "collected_count": 44,
    "node_ids_sha256": "<sha256-normalized-test-node-id-list>"
  },
  "environment": {
    "original_python": "<version>",
    "dependency_lock_sha256": "<sha256>",
    "original_test_command": "<command>"
  },
  "repository": {
    "import_pr": "<number>",
    "import_commit": "<sha>"
  }
}
```

Допустимые значения transformation должны быть узкими и явными, например:

```text
NONE
LINE_ENDING_NORMALIZATION
PATH_RELOCATION_ONLY
REPOSITORY_WRAPPER_ONLY
```

Изменение imports, представления данных, ordering, defaults, event meaning, identity, reduction или output не является чистым импортом и требует отдельного review.

## 6. Test fidelity

Одного `declared_test_count: 44` недостаточно.

Импорт должен сохранить:

- исходные test files;
- collected test node IDs;
- identity параметризации;
- fixtures и data files;
- expected failures и skips;
- исходную команду тестирования и assumptions среды.

Нормализованный вывод `pytest --collect-only -q` или эквивалентного исходного runner должен храниться или быть захеширован. Новый набор с тем же количеством тестов не эквивалентен исходному.

## 7. CI и воспроизводимость

Используются два отдельных слоя.

### 7.1 Historical reproduction environment

Аутентичный snapshot воспроизводится в максимально близкой доступной исходной среде. Фиксируются:

- точная patch-версия Python, если известна;
- dependency lock или hashes;
- identity OS/container;
- locale, timezone и значимые environment variables;
- deterministic seeds;
- точная команда.

### 7.2 Compatibility CI

После успешного исторического воспроизведения проверяется совместимость с Python 3.11 и 3.12.

Предпочтителен фиксированный runner `ubuntu-24.04`, а не плавающий `ubuntu-latest`. Для усиленной воспроизводимости используется container image, pinned by digest.

Compatibility failure не отменяет исторический checkpoint. Он создаёт отдельную compatibility-задачу.

## 8. Benchmark evidence

Измерения имеют независимые evidence dimensions:

```text
workload reproduced
≠ historical number reproduced
≠ scaling shape observed
≠ production capacity validated
```

Рекомендуемые поля:

```yaml
benchmark_id: NK-BM-V0121-SELECTIVE-001
workload_evidence: REPOSITORY_REPRODUCED
historical_timing_evidence: EXTERNALLY_OBSERVED
scaling_shape_evidence: REPOSITORY_OBSERVED
production_capacity: NOT_EVALUATED
```

GitHub-hosted runner может воспроизвести semantics workload и показать regressions, но не обязан воспроизводить исторические абсолютные времена из-за нестабильных CPU allocation и contention.

Каждый результат фиксирует:

- benchmark ID;
- source snapshot hash;
- repository commit;
- Python и dependency identity;
- OS и CPU metadata;
- seed;
- параметры corpus;
- warm-up policy;
- количество повторов;
- median и p95;
- отдельные construction/query timings;
- timestamp.

## 9. Contract-to-test traceability

Prose-only или «построчный» review архитектуры недостаточен. Import PR должен включать traceability matrix:

| Contract assertion | Test ID | Runtime symbol/path | Result | Known limit |
|---|---|---|---|---|
| Claims являются immutable semantic records | `<test-id>` | `<symbol>` | pass/fail | `<limit>` |
| Replay восстанавливает заявленное состояние | `<test-id>` | `<symbol>` | pass/fail | `<limit>` |
| Candidate conflict не равен canonical conflict | `<test-id>` | `<symbol>` | pass/fail | `<limit>` |
| Selection relevance не является truth evidence | `<test-id>` | `<symbol>` | pass/fail | `<limit>` |

Матрица показывает, что именно доказывает импортированный snapshot. Отсутствующие строки остаются явными gaps.

## 10. Conformance и status gate

Успешный импорт может поддержать **C2 — Repository reproduced** только для явно протестированных contract assertions. Он не доказывает:

- cross-profile equivalence;
- ценность на Shadow-задачах;
- operational security;
- production readiness;
- универсальную technology independence.

`STATUS.md` можно изменить на `RUNNABLE RESEARCH PROTOTYPE` только после:

- принятия authentic provenance;
- воспроизведения исходных тестов;
- прохождения CI и traceability review;
- корректного ограничения benchmark claims;
- независимого review;
- записанного operator approval.

## 11. Contract-hardening backlog вне Issue #1

Важные gaps, которые остаются отдельно от controlled import:

1. canonical Claim encoding, Unicode normalization, hash domain/version и identity migration rules;
2. command validation, durable idempotency, atomic append, ordering, crash recovery, schema upcasting и deterministic replay;
3. deletion/restriction semantics для payloads, projections, embeddings, exports, Receipts и backups;
4. executable schemas, golden vectors, invalid-event corpora, expected reducer outputs и cross-profile conformance runner;
5. чёткое разделение decision status, empirical evidence, implementation status и operator approval.

Эти пункты решаются отдельными contracts, ADR, tests и PR. Их запрещено скрыто реализовывать во время source import.

## 12. Definition of Done

### Source recovery

- [ ] найден authentic source archive;
- [ ] записана source lineage;
- [ ] записан SHA-256 архива;
- [ ] найден исходный test inventory;
- [ ] записан operator GO.

### Source fidelity

- [ ] sealed snapshot импортирован без semantic rewrite;
- [ ] transformations явно задекларированы;
- [ ] записаны hashes source и repository files;
- [ ] исходный test inventory сохранён и захеширован;
- [ ] version labels совпадают в source, tests, Receipts и docs.

### Reproducibility

- [ ] исходная среда восстановлена настолько точно, насколько позволяет evidence;
- [ ] точная test command проходит;
- [ ] compatibility CI покрывает Python 3.11 и 3.12;
- [ ] identity среды и dependencies записана.

### Benchmarks

- [ ] испускаются stable benchmark IDs;
- [ ] selective и broad workloads разделены;
- [ ] workload evidence и timing evidence отчётно разделены;
- [ ] записаны metadata, median и p95.

### Governance

- [ ] production claim не добавлен;
- [ ] dependency на Titan или Crystal не добавлена;
- [ ] post-baseline redesign не смешан с импортом;
- [ ] contract-to-test traceability reviewed;
- [ ] `STATUS.md` меняется только после evidence и operator approval.

## 13. Правило ADR

Новый ADR не требуется для byte-faithful импорта, который только исполняет уже задокументированный gate.

Новый или обновлённый ADR обязателен, если PR меняет public contract meaning, event vocabulary, Claim identity, replay semantics, deletion semantics, conflict semantics, границы проектов или долгоживущий implementation-profile commitment.

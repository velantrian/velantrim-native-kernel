# RFC-0001: Архитектура Curiosity Core

- **Статус:** `PROPOSED / DOCUMENTED_ONLY`
- **Версия:** `RFC-0.1`
- **Дата:** `2026-07-24`
- **Основной host:** `исследовательский runtime Titan`
- **Ограниченный профиль:** `Crystal Audit Curiosity`
- **Связь с Native Kernel:** `опциональный клиент абстрактных контрактов`
- **Прямая запись в Canon:** `запрещена`
- **Runtime-реализация:** `отсутствует`
- **Production readiness:** `не заявляется`
- **Controlled import v0.1.2.1:** `вне области документа`
- **ADR границы:** [`ADR-0005`](../adr/0005-curiosity-core-is-optional-and-non-authoritative.md)
- **English:** [`0001-curiosity-core-architecture.md`](./0001-curiosity-core-architecture.md)

> [!IMPORTANT]
> Curiosity Core — это активная policy исследования, а не источник истины. Он определяет, какое незнание заслуживает ограниченного внимания, но не определяет, чему разрешено стать Canon.

## 1. Назначение

**Curiosity Core** — заменяемый метакогнитивный модуль, который обнаруживает значимое незнание, оценивает необходимость исследования, выделяет ограниченный бюджет внимания, формулирует вопросы и конкурирующие гипотезы, запрашивает доказательства или инструменты через явные шлюзы и фиксирует проверяемые ограничения системы.

Его функциональная задача:

> Обнаружить важный разрыв между текущим эпистемическим состоянием и требуемым пониманием, а затем организовать безопасную, аудируемую и ограниченную попытку уменьшить этот разрыв.

Он не имитирует биологическую систему вознаграждения, не заявляет эмоции и не доказывает сознание. Формулировка «хочет понять» является только объяснительной метафорой.

## 2. Почему модуль отделён от Native Kernel

Native Kernel сохраняет устойчивый смысл через:

- immutable Claims;
- append-only Event History;
- детерминированное восстановление состояния;
- rebuildable projections;
- provenance и lineage;
- временную и конфликтную семантику;
- task-specific context selection;
- аудируемые Receipts.

Kernel намеренно не закрепляет постоянный agent loop, curiosity score, способ обхода графа, LLM, tool runtime или модель активации процессора.

Curiosity Core закрывает промежуток между пассивной памятью и активным исследованием:

```text
память
  ↓
внимание
  ↓
вопрос
  ↓
исследование
  ↓
набор гипотез
  ↓
доказательства и проверка
  ↓
эпистемическое продвижение или честное Unknown
```

Модуль остаётся опциональным, чтобы изменение curiosity policy не требовало переписывать Claim identity, авторитетную историю или семантику истины.

## 3. Архитектурная формула

```text
Native Kernel
→ сохраняет смысл и записанную историю.

Curiosity Core
→ определяет, какое незнание заслуживает исследования.

Investigation Runtime
→ выполняет ограниченный анализ и сбор evidence.

Action Gate
→ контролирует инструменты и внешние/необратимые действия.

TruthGate
→ контролирует эпистемическое продвижение и отклонение.

Operator / Maintainer
→ утверждает изменения архитектуры и policy.
```

## 4. Место в системе

```text
┌──────────────────────────────────────────────────────────┐
│ 🧠 TITAN COGNITIVE RUNTIME                              │
│ Goals · SituationModel · Working Notebook · Tools        │
│ WhyEngine · Causal Context · RouteMemoryGate             │
└────────────────────────┬─────────────────────────────────┘
                         │ context / goals / constraints
                         ▼
┌──────────────────────────────────────────────────────────┐
│ 🔍 CURIOSITY CORE                                      │
│ 🛡 Guard Wrapper                                       │
│ Trigger · Evaluation · Allocation · Planning             │
│ Investigation · Hypothesis Sets · System Insights        │
│ Calibration · Stopping / Suspension                      │
└────────────┬────────────────────┬────────────────────────┘
             │                    │
             ▼                    ▼
      🧾 Event Admission     🛡 Action Gate
      operational records    tools / external actions
             │                    │
             ▼                    ▼
┌──────────────────────────────────────────────────────────┐
│ 🔱 VELANTRIM NATIVE KERNEL                             │
│ Claims · Events · Receipts · Replay · Projections        │
│ Questions · Candidates · Evidence · Experimental records │
└────────────────────────┬─────────────────────────────────┘
                         │ promotion request
                         ▼
┌──────────────────────────────────────────────────────────┐
│ 💎 TRUTHGATE                                             │
│ Evidence · Provenance · Conflict · Policy · Review       │
└────────────────────────┬─────────────────────────────────┘
                         ▼
                 ⚖️ Epistemic State
```

## 5. Три разных шлюза полномочий

### 5.1 Event Admission

Контролирует допустимость записи операционной истории:

- найден curiosity candidate;
- оценён trigger;
- зарезервирован budget;
- сформулирован вопрос;
- investigation приостановлено;
- обнаружен capability gap;
- цикл завершён.

Такие записи описывают процесс, но не устанавливают истину.

Admission может проверять:

- schema события и payload;
- actor и permissions;
- idempotency key;
- expected stream version;
- ограничения размера и retention;
- требования к Receipt;
- privacy classification;
- допустимость event type.

### 5.2 TruthGate

Используется, когда результат может изменить эпистемический статус.

```text
hypothesis
→ evidence attached
→ validation requested
→ TruthGate evaluation
→ supported / rejected / unresolved
```

TruthGate не обязан проверять каждое временное ранжирование или выделение внимания.

### 5.3 Action Gate

Контролирует возможности за пределами read-only анализа:

- доступ к вебу и внешним источникам;
- выполнение кода;
- изменение файлов и репозиториев;
- внешние API;
- коммуникации;
- чувствительные данные;
- финансовые, юридические, физические и необратимые действия.

Возможные решения:

```text
ALLOW
ALLOW_WITH_LIMITS
ANALYSE_ONLY
SANDBOX_REQUIRED
REDACT_REQUIRED
HUMAN_APPROVAL_REQUIRED
DENY
HALT
```

## 6. Safety & Resource Guard

Guard является обёрткой всего lifecycle, а не последним фильтром.

```text
Guard(
  Trigger → Evaluation → Allocation → Investigation
  → Hypotheses → System Insights → Calibration
)
```

### 6.1 Обязательные quotas

ResourceBudget может ограничивать:

- wall-clock duration;
- compute units;
- model tokens;
- tool calls;
- расширение графа или проекции;
- causal depth;
- размер active context;
- количество вопросов;
- количество гипотез;
- количество System Insights;
- retries и context switches;
- запросы внимания оператора.

### 6.2 Circuit breaker

Цикл останавливается или приостанавливается, если:

- исчерпан hard budget;
- один вопрос повторяется без прогресса;
- число гипотез растёт без различающего evidence;
- investigation становится рекурсивным;
- инструменты возвращают циклические ошибки;
- действие нарушает policy;
- вход выглядит adversarial или созданным для расхода ресурсов;
- модуль пытается изменить Guard;
- возникает угроза инварианту Native Kernel.

### 6.3 Безопасность по возможностям

Чувствительная тема не обязательно запрещается полностью. Ограничивается доступная способность.

```text
анализ сбоя security policy          → может быть разрешён
предложение проверяемого исправления → может быть разрешено
тихое отключение policy              → запрещено
получение защищённых секретов        → запрещено
автоматическое применение патча      → approval или deny
```

### 6.4 Ограничение мета-рефлексии

Для первого implementation profile:

> SystemInsight не может напрямую запускать другой SystemInsight.

Bounded meta-curiosity может рассматриваться позже как отдельная policy с ограниченной глубиной.

## 7. Trigger Layer

Trigger Layer — дешёвый и консервативный screening. Он отвечает:

> Нужно ли создать кандидата на исследование?

### 7.1 Hard triggers

- нарушение архитектурного инварианта;
- критический epistemic conflict;
- невозможное производное состояние;
- сильное разрушение ранее высокоуверенного Claim;
- нарушение provenance или replay;
- критическая evidence inconsistency;
- security incident;
- близкое необратимое действие при высокой неопределённости;
- семантическое расхождение двух реализаций одного контракта.

### 7.2 Soft triggers

- неопределённость;
- недостающее evidence;
- возможный causal или temporal gap;
- неразрешённое противоречие;
- неопределённое понятие;
- повторяющаяся ошибка;
- новый паттерн;
- изменение среды;
- новый вопрос оператора;
- mismatch с активной целью.

### 7.3 Типы пробелов

```text
SCHEMA_GAP
CAUSAL_GAP
EVIDENCE_GAP
CONFLICT_GAP
TEMPORAL_GAP
DEFINITION_GAP
CAPABILITY_GAP
TOOLING_GAP
GOAL_PATH_GAP
DATA_QUALITY_GAP
IMPLEMENTATION_GAP
```

Отсутствующая связь или узел — только кандидат на gap, а не доказательство скрытого Claim.

### 7.4 Контекстуальная важность

```text
ContextualImportance = f(
  stimulus,
  active goal,
  SituationModel,
  consequences,
  constraints,
  time sensitivity,
  affected invariants
)
```

Один и тот же стимул может быть шумом в одной задаче и критическим сигналом в другой.

## 8. Evaluation Layer

Evaluation оценивает исследовательский приоритет, а не истинность.

### 8.1 Положительные факторы

#### Epistemic Need

- низкая или некалиброванная confidence;
- unresolved conflict;
- слабый provenance;
- отсутствующее или недостаточное evidence;
- неясная область применимости;
- неизвестная temporal validity;
- неполная причинная структура.

#### Expected Information Value

На первом этапе это честно объявленная эвристика, а не декоративное утверждение о точном Shannon Information Gain.

Возможные proxy:

- число зависимых Claims и решений;
- downstream impact;
- вероятность разрешения конфликта;
- наличие различающего теста;
- число затронутых открытых вопросов;
- ожидаемое снижение неопределённости оператора;
- возможность разблокировать другое investigation.

#### Goal Relevance

Связь с CoreGoal, текущей задачей, долгосрочной миссией, активными ограничениями, риском, сроком или обязательством перед пользователем.

#### Conflict Severity

Зависит от типа Claim, последствий ошибки, масштаба зависимостей, независимости источников и возможности необратимого решения.

#### Actionability

Прогресс вероятнее, если доступен источник, инструмент, различающий тест, точный вопрос человеку или измеримый эксперимент.

#### Downstream Impact и Time Urgency

Небольшой gap может быть приоритетным, если от него зависит много решений или окно полезности короткое.

### 8.2 Отрицательные факторы

- computation и latency;
- токены и API cost;
- safety/privacy risk;
- duplication;
- context-switch cost;
- repeated failure;
- stale context;
- низкая вероятность реального прогресса.

### 8.3 Novelty

Novelty — вспомогательный сигнал. Она может означать важное открытие, шум, parser error, adversarial input или редкую, но бесполезную информацию.

Novelty не является evidence истины.

### 8.4 Формула приоритета

```text
ResearchPriority =
    + epistemic_need
    + expected_information_value
    + goal_relevance
    + conflict_severity
    + actionability
    + downstream_impact
    + time_urgency

    - estimated_cost
    - safety_risk
    - duplication_penalty
    - context_switch_cost
    - repeated_failure_penalty
    - staleness
```

Формула является заменяемой policy, а не Architecture Canon.

### 8.5 Metric adapters

```text
UncertaintyAdapter
├─ epistemic-state heuristic
├─ conflict/evidence proxy
└─ probabilistic model

InformationValueAdapter
├─ dependency impact
├─ graph centrality
├─ question density
└─ decision impact

NoveltyAdapter
├─ lexical
├─ symbolic
├─ graph pattern
└─ vector distance

GoalRelevanceAdapter
├─ operator rule
├─ causal path
├─ symbolic match
└─ semantic similarity
```

Native Kernel не требует graph, vectors или probabilistic model. Каждая оценка фиксирует версии adapter и policy.

## 9. Attention Allocator

Attention Allocator выделяет временный ограниченный budget. Он может менять порядок retrieval и investigation, но не truth и Canon.

Он может выбирать Claims, Links, вопросы, subgraphs, элементы Working Notebook, model calls, tool preparations и deferred candidates.

```text
ALLOCATE
QUEUE
MERGE_WITH_EXISTING
DEFER
COOLDOWN
DROP_AS_DUPLICATE
REQUIRE_OPERATOR
REJECT_BY_POLICY
```

Обязательные свойства:

- явный budget;
- TTL или condition expiry;
- explanation и reason codes;
- bounded preemption;
- объединение дублей;
- context-switch cost;
- bounded priority aging;
- отражение в Receipt.

### 9.1 Selective activation и будущее hardware

Сегодня selective activation может означать retrieval filtering, context loading, graph traversal, caching и selective model calls.

Будущие profiles могут сопоставить тот же семантический контракт с memory-local compute, processing-in-memory, neuromorphic routing, analog или другим substrate.

Устойчивый контракт:

> Выбирать семантически релевантную область работы, не превращая физический метод активации в Canon.

Совместимость или превосходство будущего hardware не заявляются.

## 10. Investigation Runtime

Curiosity Core выбирает и планирует исследование. Investigation Runtime выполняет ограниченную работу.

### 10.1 Lifecycle

```text
DETECTED
  ↓
SCREENING
  ↓
QUEUED
  ↓
ALLOCATED
  ↓
PLANNING
  ↓
INVESTIGATING
  ↓
┌───────────────┬──────────────────┐
│               │                  │
▼               ▼                  ▼
ANSWER        GAP FOUND       HYPOTHESIS NEEDED
│               │                  │
▼               ▼                  ▼
VALIDATION   ACTIVE QUERY      HYPOTHESIZING
│               │                  │
└───────────────┴──────────┬───────┘
                           ▼
                    RESULT EVALUATION
                           ↓
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
    SUPPORTED          REJECTED          UNRESOLVED
        └──────────────────┼──────────────────┘
                           ▼
                 PROMOTION REQUEST / CLOSE
```

Дополнительные состояния:

```text
DUPLICATE
COOLDOWN
SUSPENDED
BUDGET_EXHAUSTED
BLOCKED_BY_TOOL
BLOCKED_BY_EVIDENCE
BLOCKED_BY_OPERATOR
POLICY_DENIED
STALE
DORMANT
ABORTED
REOPENED
HALTED
```

### 10.2 Investigation patterns

- **Decompose:** объект → компоненты → функции → зависимости → ограничения → failure modes.
- **Root-Cause Drill:** углубляться до известного механизма, явного gap, budget limit или diminishing returns.
- **Contradiction Analysis:** сравнивать scope, time, definitions, sources, applicability и evidence.
- **Active Query:** формулировать точный вопрос оператору, источнику, инструменту или другому агенту.
- **Counterfactual Check:** определить, что должно наблюдаться при истинной и ложной гипотезе.
- **Falsification Search:** активно искать опровергающее evidence.

### 10.3 Stopping criteria

Исследование закрывается или приостанавливается, если:

- evidence достаточно по заявленной policy;
- отсутствует различающий тест;
- expected value ниже порога;
- budget исчерпан;
- шаги повторяются;
- нужен оператор;
- действие запрещено;
- контекст устарел;
- исчезла связь с целью;
- появился более высокий риск;
- корректный результат — `UNKNOWN` или `INSUFFICIENT_EVIDENCE`.

## 11. Hypothesis Engine

Hypothesis Engine создаёт Hypothesis Set, а не один привилегированный ответ.

```text
Question
  ↓
Hypothesis Set
├─ H1
├─ H2
├─ H3
└─ H0: неизвестная причина / недостаточно информации
```

Каждая HypothesisRecord содержит:

- ссылку на semantic Claim;
- assumptions;
- scope/applicability;
- generation lineage;
- supporting/contradicting evidence;
- missing evidence;
- competing hypotheses;
- falsification conditions;
- discriminating tests;
- confidence provenance;
- risk;
- lifecycle status;
- dormancy/reopen conditions.

Возможные результаты:

```text
BEST_SUPPORTED
MULTIPLE_PLAUSIBLE
UNDERDETERMINED
INSUFFICIENT_EVIDENCE
ALL_REJECTED
UNKNOWN_CAUSE
```

Система не обязана выбирать одну гипотезу.

### 11.1 Confidence и decay

Confidence выводится из evidence и версионированной policy. Не используется необъяснённое магическое число.

Temporal decay может менять attention priority, retrieval rank, активность, urgency и `DORMANT` status.

Temporal decay не должен молча менять truth, evidence-derived confidence, provenance или историческое состояние.

Отсутствие нового evidence не является автоматическим evidence против гипотезы.

### 11.2 Pruning и архивирование

Hypothesis может быть архивирована как duplicate, superseded, out-of-scope, rejected, непроверяемая текущими capabilities или закрытая оператором. История её существования сохраняется.

## 12. SystemInsight

`Self-Reflection` может оставаться объяснительным названием, но доменная сущность называется **SystemInsight**.

Это фальсифицируемое диагностическое предположение об ограничении системы.

```text
KNOWLEDGE_DEFICIT
CAPABILITY_DEFICIT
TOOLING_DEFICIT
DATA_QUALITY_ISSUE
PERFORMANCE_REGRESSION
ARCHITECTURE_LIMITATION
CALIBRATION_FAILURE
RESOURCE_BOTTLENECK
POLICY_CONFLICT
HARDWARE_LIMITATION
OBSERVABILITY_GAP
```

Обязательные поля:

- subject и affected scope;
- observed symptoms;
- evidence refs;
- inferred limitation;
- confidence/severity;
- proposed action;
- falsification condition;
- policy version;
- provenance;
- review status.

Статусы:

```text
OPEN
ACKNOWLEDGED
UNDER_REVIEW
ACCEPTED_FOR_EXPERIMENT
REJECTED
RESOLVED
SUPERSEDED
DORMANT
```

SystemInsight не является истиной, командой, автоматическим изменением кода/policy или автоматически принятым ADR.

## 13. Calibration Loop

Curiosity Core должен фиксировать собственные ошибки приоритизации.

```text
TRUE_POSITIVE
FALSE_POSITIVE
MISSED_IMPORTANCE
OVER_ALLOCATED
UNDER_ALLOCATED
DUPLICATE_TRIGGER
NO_PROGRESS
USEFUL_BUT_EXPENSIVE
POLICY_BLOCKED_CORRECTLY
```

Оценивается:

- уменьшилась ли неопределённость;
- появилось ли новое evidence;
- оправдан ли budget;
- была ли novelty шумом;
- существовало ли investigation ранее;
- правильно ли работали trigger, allocation и stopping.

Этапы адаптации:

```text
v0.1  static policy
v0.2  operator-selected profiles
v0.3  Shadow recommendations
v0.4  operator-approved policy updates
```

Активный модуль не переписывает собственную scoring policy молча.

## 14. Абстрактные data contracts

Это семантические контракты, а не обязательные Python dataclasses или SQLite tables.

### TargetRef

```text
TargetRef {
  kind: CLAIM | LINK | EVENT | QUESTION | GAP | HYPOTHESIS | INSIGHT
  id: string
}
```

### CuriosityCandidate

```text
CuriosityCandidate {
  candidate_id
  stimulus_ref
  trigger_reasons[]
  gap_type?
  affected_scope[]
  context_ref
  detected_at
  policy_version
  deduplication_key
}
```

### CuriosityEvaluation

```text
CuriosityEvaluation {
  evaluation_id
  candidate_id
  epistemic_need
  expected_information_value
  goal_relevance
  conflict_severity
  actionability
  downstream_impact
  novelty
  estimated_cost
  safety_risk
  duplication_penalty
  context_switch_cost
  repeated_failure_penalty
  raw_score
  normalized_priority
  metric_versions
  policy_version
  input_snapshot_hash
  evaluated_at
}
```

### AttentionAllocation

```text
AttentionAllocation {
  allocation_id
  investigation_id
  total_budget
  reserved_budget
  selected_targets[]
  deferred_targets[]
  rejected_targets[]
  expires_at
  policy_version
  created_at
}
```

### InvestigationRecord

```text
InvestigationRecord {
  investigation_id
  candidate_id
  state
  active_question_ids[]
  hypothesis_set_ids[]
  evidence_refs[]
  tool_request_refs[]
  system_insight_ids[]
  attempt_count
  started_at
  last_progress_at
  suspended_at?
  completed_at?
  stopping_reason?
  reopen_condition?
}
```

### HypothesisSet

```text
HypothesisSet {
  set_id
  question_id
  hypothesis_ids[]
  comparison_policy_version
  result
  created_at
  evaluated_at?
}
```

### HypothesisRecord

```text
HypothesisRecord {
  hypothesis_id
  claim_ref
  assumptions[]
  scope
  generated_from[]
  supporting_evidence[]
  contradicting_evidence[]
  competing_hypotheses[]
  falsification_conditions[]
  proposed_tests[]
  confidence_record
  lifecycle_status
  created_at
}
```

### ResourceBudget

```text
ResourceBudget {
  policy_version
  max_duration_ms
  max_compute_units
  max_tokens
  max_tool_calls
  max_projection_expansion
  max_depth
  max_hypotheses
  max_questions
  max_system_insights
  max_retries
}
```

## 15. Предлагаемое event namespace

Vocabulary является только proposed research и не входит в текущий малый набор event verbs или Issue #1.

```text
curiosity.candidate_detected
curiosity.trigger_evaluated
curiosity.candidate_accepted
curiosity.candidate_rejected

curiosity.investigation_queued
curiosity.budget_reserved
curiosity.attention_allocated
curiosity.plan_created

curiosity.question_raised
curiosity.evidence_requested
curiosity.evidence_observed
curiosity.tool_requested
curiosity.tool_result_attached

curiosity.hypothesis_proposed
curiosity.hypothesis_revised
curiosity.hypothesis_challenged
curiosity.hypothesis_supported
curiosity.hypothesis_rejected
curiosity.hypothesis_superseded

curiosity.system_insight_detected
curiosity.architecture_change_proposed
curiosity.capability_gap_detected
curiosity.calibration_issue_detected

curiosity.investigation_suspended
curiosity.investigation_resumed
curiosity.investigation_completed
curiosity.investigation_aborted
curiosity.budget_exhausted
curiosity.policy_denied

curiosity.promotion_requested
curiosity.promotion_approved
curiosity.promotion_rejected
```

## 16. Replay, time и idempotency

Reducers не генерируют новые UUID, timestamps, случайные scores, policy versions или evidence links.

ID может быть создан один раз при первоначальной команде через UUIDv4, UUIDv7, ULID или другой profile. Replay читает записанный ID из Event.

### CommandEnvelope

```text
CommandEnvelope {
  command_id
  idempotency_key
  actor
  issued_at
  context_id
  policy_version
  expected_stream_version
  input_snapshot_hash
  payload
}
```

### EventEnvelope

```text
EventEnvelope {
  event_id
  event_type
  schema_version
  stream_id
  stream_version
  idempotency_key
  occurred_at
  recorded_at
  actor
  payload
  previous_event_hash?
  event_hash?
}
```

### Временная семантика

```text
observed_at
received_at
evaluated_at
occurred_at
recorded_at
```

Время timezone-aware, предпочтительно UTC.

Точное повторение score требует frozen snapshot, policy version, metric-adapter versions, normalization version, стабильных external inputs и deterministic model settings. Если это невозможно, Receipt честно фиксирует уровень воспроизводимости.

## 17. Deduplication, cooldown и reopen

```text
deduplication_key
stimulus_fingerprint
topic_fingerprint
attempt_count
previous_investigation_ids[]
cooldown_until
last_progress_at
failure_reason
reopen_condition
```

Пример:

```text
один gap исследовался три раза
+ нет нового evidence
+ нет нового инструмента
+ низкий expected value
→ DORMANT
```

Reopen возможен при новом evidence, новой цели, новом инструменте, изменении policy, новом конфликте, росте severity, изменении scope или явном запросе оператора.

## 18. Инварианты Curiosity Core

1. Curiosity Core не изменяет Canon или Epistemic State напрямую.
2. Каждая persisted запись проходит Event Admission.
3. Operational curiosity events описывают процесс, а не истину.
4. Candidate, gap, question, hypothesis и SystemInsight не являются установленным знанием.
5. Epistemic promotion является отдельным решением TruthGate.
6. Внешние, чувствительные и необратимые действия требуют Action Gate.
7. Attention не равно validity.
8. Utility и novelty не являются evidence.
9. Влияние на context selection отражается в Receipt.
10. Replay использует записанные значения и не создаёт новую случайность в reducers.
11. Scoring и Guard policies версионируются.
12. Guard оборачивает полный lifecycle.
13. SystemInsight не является автоматическим самоизменением.
14. Temporal decay меняет внимание, а не evidence-derived confidence.
15. Curiosity Core можно отключить без повреждения Native Kernel.
16. Adaptive policy начинается в Shadow.
17. Architecture-policy promotion требует operator approval.
18. Legal deletion, restriction и privacy requirements сохраняются.
19. Каждое investigation имеет budget, stopping, suspension и reopen conditions.
20. `UNKNOWN` и `INSUFFICIENT_EVIDENCE` — допустимые результаты.
21. Controlled import Issue #1 остаётся без изменений.

## 19. Связь с модулями Velantrim

```text
WhyEngine
→ определяет, зачем нужно исследование

SituationModel
→ даёт текущий контекст

CausalContextBuilder
→ строит активные причинные связи

FQKVE / RouteMemoryGate
→ маршрутизирует память

Working Notebook
→ удерживает цель, вопрос и ограничения

Curiosity Core
→ выбирает, что исследовать

Investigation Runtime
→ выполняет ограниченную работу

Hypothesis Workspace
→ хранит конкурирующие объяснения

TruthGate
→ контролирует promotion

Native Kernel
→ сохраняет историю, Claims, state и Receipts
```

## 20. Профиль Titan

Titan является основным будущим host полного профиля:

- обнаружение gaps/conflicts;
- goal-aware prioritization;
- causal investigation;
- active queries;
- external tools через Action Gate;
- Hypothesis Sets и falsification;
- counterfactual checks;
- collaborative hypothesis building;
- System Insights;
- calibration и Shadow adaptation.

Titan остаётся независимой cognitive research environment и не сводится к Native Kernel projections.

## 21. Crystal Audit Curiosity

Ограниченный профиль Crystal:

```text
Audit Curiosity
├─ evidence gap
├─ provenance gap
├─ contradiction
├─ compliance uncertainty
├─ missing validation
├─ temporal-validity gap
├─ policy conflict
└─ recommended verification step
```

Crystal не требует широкого автономного исследования мира, неограниченной генерации теорий или self-modifying curiosity.

Crystal работает без Native Kernel. Любой перенос требует отдельного RFC, threat model, tests, privacy review, rollback и approval.

## 22. MVP Roadmap

### Phase 0 — Documentation

- boundary ADR;
- architecture RFC;
- threat/resource model;
- event namespace;
- `DOCUMENTED_ONLY`.

### Phase 1 — Passive Shadow evaluator

- read frozen snapshots;
- conflict/evidence gap detection;
- explainable score;
- report only;
- no external tools;
- no live context influence.

### Phase 2 — Receipted attention

- budget/queue;
- TTL;
- allocation и reason codes;
- cooldown/deduplication;
- operator-visible Receipts.

### Phase 3 — Questions and Hypothesis Sets

- structured questions;
- competing hypotheses;
- explicit H0 Unknown;
- falsification conditions;
- Experimental Workspace.

### Phase 4 — Controlled investigation

- Action Gate;
- sandboxed tools;
- evidence collection;
- suspension/resume;
- promotion requests.

### Phase 5 — System Insights

- capability/tooling gaps;
- data-quality/performance issues;
- calibration reports;
- operator review.

### Phase 6 — Shadow adaptation

- alternative policy profiles;
- offline comparison;
- rollback;
- operator approval.

### Phase 7 — Future hardware profiles

- memory-local compute;
- processing-in-memory;
- neuromorphic routing;
- другие substrates.

## 23. Минимальные тесты

- replay не создаёт новые IDs/times;
- frozen-input score воспроизводим по declared policy;
- Curiosity не меняет Epistemic State напрямую;
- SystemInsight не применяет изменения;
- tools не запускаются без Action Gate;
- hypothesis не становится Canon автоматически;
- budget exhaustion приводит к suspend/halt;
- recursion и meta-reflection ограничены;
- repeated command не создаёт duplicate hypotheses;
- competing hypotheses сохраняются;
- Unknown поддерживается;
- temporal decay не меняет truth confidence;
- новая policy не активируется без approval.

## 24. Метрики качества

```text
trigger_precision
trigger_recall
false_positive_rate
duplicate_investigation_rate
mean_information_value
cost_per_resolved_gap
budget_exhaustion_rate
operator_acceptance_rate
hypothesis_falsification_rate
unknown_completion_rate
unsafe_action_block_rate
replay_consistency_rate
context_switch_cost
time_to_first_useful_question
```

Метрики оценивают модуль, но не доказывают истинность его гипотез.

## 25. Anti-Canon

Curiosity Core не утверждает:

- наличие сознания или биологического желания;
- novelty = importance;
- priority = validity;
- utility/repeated use = truth;
- agreement нескольких моделей = approval;
- unverified hypothesis = established;
- доказанную совместимость с future hardware;
- универсальность scoring policy;
- SystemInsight = философское самосознание;
- безопасность автономного самоизменения;
- отсутствие evidence автоматически опровергает hypothesis;
- documentation = runtime implementation.

## 26. Финальный статус

```text
Name: Curiosity Core
Document version: RFC-0.1
Maturity: PROPOSED / DOCUMENTED_ONLY
Architecture role: optional active-cognition module
Primary host: Titan
Restricted profile: Crystal Audit Curiosity
Native Kernel dependency: abstract read, admission, Receipt, promotion contracts
Direct Canon write: forbidden
Autonomous self-modification: forbidden
Adaptive policy: Shadow-only until operator approval
Issue #1 integration: forbidden
Production readiness: not claimed
```

## 27. Итог

```text
«я не знаю»
→ «это незнание важно»
→ «вот точный вопрос»
→ «вот конкурирующие объяснения»
→ «вот что их различит»
→ «вот что удалось установить»
→ «вот что осталось неизвестным»
```

Curiosity Core — не второй Canon и не неконтролируемый автономный агент. Это ограниченный, аудируемый и заменяемый двигатель активного исследования.

> Native Kernel сохраняет то, что система записала и знает по declared policy.  
> Curiosity Core определяет, что стоит попытаться узнать.  
> TruthGate определяет, чему разрешено изменить Epistemic State.  
> Operator определяет, какие изменения архитектуры и policy приняты.

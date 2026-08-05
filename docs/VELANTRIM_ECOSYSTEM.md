# 🌐 Velantrim Ecosystem / Экосистема Velantrim

> **Document type:** navigation and integration-boundary map.  
> **Authority:** this document does not authorize runtime integration, shared event history, cross-project Canon writes, identity mutation or capability inheritance.  
> **Languages:** English first, followed by Russian. Other translations may be added later.

## English

### Native Kernel's role

**Velantrim Native Kernel** is the long-horizon, substrate-neutral architecture research track of the Velantrim ecosystem.

It studies durable semantic contracts for claims, events, provenance, time, conflict visibility, deterministic reduction, rebuildable projections, context selection and Receipts. Current databases, languages, models and processors are implementation profiles, not the permanent definition of the architecture.

```text
Native Kernel research
≠ production source of truth for all Velantrim projects
≠ hidden Crystal runtime
≠ Titan's mandatory storage layer
≠ Mentaury identity authority
```

### Project map

| Project | Primary role | Current relationship to Native Kernel |
|---|---|---|
| [🧬 Native Kernel](https://github.com/velantrian/velantrim-native-kernel) | Substrate-neutral event, memory and projection contracts | This repository; independent long-horizon architecture research |
| [💎 Crystal](https://github.com/velantrian/velantrim-exocortex-crystal) | Verifiable memory, evidence, provenance, trust and audit boundaries | Independent grant-facing product; no current Kernel runtime dependency |
| [🔱 Titan](https://github.com/velantrian/Velantrim-ExoCortex-Titan) | Cognition, orchestration, retrieval, tools and agents | Independent Exo-Cortex research environment; possible future Offline Shadow evaluation host |
| [⭐️ Mentaury Soul](https://github.com/velantrian/velantrim-mentaury-soul) | Digital individuality, identity continuity, relationships, commitments and governed development | Independent identity research; Kernel events do not define identity by themselves |

### Conceptual relationship map

```text
                         🌐 VELANTRIM ECOSYSTEM
                                   │
          ┌────────────────────────┼────────────────────────┐
          │                        │                        │
          ▼                        ▼                        ▼
  ⭐️ Mentaury Soul            🔱 Titan                 💎 Crystal
 identity / continuity     cognition / tools       evidence / trust
 relationships / M3        orchestration           provenance / audit
          │                        │                        │
          └──────── proposed governed contracts ──────────┘
                                   │
                                   ▼
                         🧬 Native Kernel
                 substrate-neutral contract research

Conceptual relationships are not claims of current runtime wiring.
```

### Mandatory boundaries

1. Native Kernel remains independent and does not become a universal Velantrim truth authority.
2. Crystal continues to work without Native Kernel and keeps its own Canon and grant scope.
3. Titan may evaluate Kernel ideas through bounded adapters or Offline Shadow, not through silent replacement of its source of truth.
4. Kernel event history, projections or Receipts do not become Mentaury identity, relationships, commitments or M3 state automatically.
5. Cross-project capabilities, credentials, consent and authority are never inherited implicitly.
6. Every transfer requires a scoped RFC/ADR, explicit semantic-equivalence contract, deterministic tests, threat/privacy review, rollback and operator approval.

### Safe future transfer pattern

```text
research primitive
→ abstract contract
→ reproducible implementation profile
→ deterministic replay and equivalence tests
→ isolated adapter
→ Offline Shadow / read-only evaluation
→ Receipts and failure analysis
→ explicit approval
→ separately versioned integration
```

---

## Русский

### Роль Native Kernel

**Velantrim Native Kernel** — долгосрочное substrate-neutral архитектурное исследование внутри экосистемы Velantrim.

Проект изучает устойчивые смысловые контракты для claims, events, provenance, времени, видимости конфликтов, deterministic reduction, восстанавливаемых projections, выбора контекста и Receipts. Современные базы данных, языки, модели и процессоры являются заменяемыми implementation profiles, а не окончательным определением архитектуры.

```text
Исследование Native Kernel
≠ production-источник истины для всех проектов Velantrim
≠ скрытый runtime Crystal
≠ обязательный storage-layer Titan
≠ authority над identity Mentaury
```

### Карта проектов

| Проект | Основная роль | Текущее отношение к Native Kernel |
|---|---|---|
| [🧬 Native Kernel](https://github.com/velantrian/velantrim-native-kernel) | Substrate-neutral event-, memory- и projection-контракты | Этот репозиторий; независимое долгосрочное исследование |
| [💎 Crystal](https://github.com/velantrian/velantrim-exocortex-crystal) | Проверяемая память, доказательства, provenance, доверие и аудит | Независимое грантовое направление; текущей runtime-зависимости от Kernel нет |
| [🔱 Titan](https://github.com/velantrian/Velantrim-ExoCortex-Titan) | Cognition, orchestration, retrieval, инструменты и агенты | Независимая Exo-Cortex среда; возможный будущий host для Offline Shadow |
| [⭐️ Mentaury Soul](https://github.com/velantrian/velantrim-mentaury-soul) | Цифровая индивидуальность, continuity, отношения, commitments и управляемое развитие | Независимое identity-исследование; события Kernel сами по себе не определяют identity |

### Обязательные границы

1. Native Kernel остаётся самостоятельным и не становится универсальным truth-authority Velantrim.
2. Crystal продолжает работать без Native Kernel и сохраняет собственный Canon и grant scope.
3. Titan может проверять идеи Kernel через ограниченные адаптеры или Offline Shadow, но не через скрытую замену своего источника истины.
4. Event history, projections или Receipts Kernel не становятся автоматически identity, relationships, commitments или M3-state Mentaury.
5. Capabilities, credentials, consent и authority не наследуются между проектами неявно.
6. Любой перенос требует ограниченного RFC/ADR, явного контракта semantic equivalence, детерминированных тестов, threat/privacy review, rollback и одобрения оператора.

### Безопасная последовательность переноса

```text
исследовательский примитив
→ абстрактный контракт
→ воспроизводимый implementation profile
→ deterministic replay и equivalence tests
→ изолированный адаптер
→ Offline Shadow / read-only оценка
→ Receipts и анализ отказов
→ явное одобрение
→ отдельно версионируемая интеграция
```

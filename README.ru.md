# 🧬 Velantrim Native Kernel

**[English](README.md) · [Русский](README.ru.md)**

> Технологически нейтральная исследовательская архитектура долговечного смысла, памяти, provenance, изменений и объяснений.

Native Kernel задаёт один главный вопрос: **какие семантические свойства должны сохраняться, если мы заменим базу данных, язык, модель, storage engine или вычислительный substrate?**

Это не ядро ОС, не database product, не vector store и не LLM memory plugin. Текущая кодовая база — **ограниченная reference laboratory**, а не окончательное определение архитектуры.

## 🧭 Проект одним взглядом

```text
🏛️ Смысл / invariants
        ↓
📐 Абстрактные контракты
        ↓
🔌 Заменяемые profiles
        ↓
🧪 Ограниченная laboratory
        ↓
📊 Evidence / conformance
        ↓
🚦 Отдельное решение Canon / runtime
```

**Главная дисциплина:** `meaning ≠ implementation` · `implementation ≠ universal proof` · `laboratory success ≠ Final Canon` · `merged code ≠ runtime authority`.

## 🌳 Основные слои

```text
🧬 Native Kernel
├── 🏛️ semantic invariants
├── 📐 architecture contracts
├── 🔌 replaceable implementation profiles
├── 🧪 reference laboratory
├── 📊 evidence & conformance
├── 🔬 post-blueprint validation
└── 🚦 explicit Canon/runtime/production gates
```

## 📚 С чего начать

| Цель | Документ |
|---|---|
| 👤 Понять проект | [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md) |
| 🚦 Узнать текущий authoritative state | [STATUS.md](STATUS.md) |
| 🧾 Машиночитаемый state | [project-state.json](project-state.json) |
| 🏛️ Изучить архитектуру | [docs/ARCHITECTURE_REFOUNDATION.ru.md](docs/ARCHITECTURE_REFOUNDATION.ru.md) |
| 🧪 Запустить laboratory | [docs/QUICKSTART.ru.md](docs/QUICKSTART.ru.md) |
| 🔬 Исследования | [docs/research/](docs/research/) |
| 🤖 Вход для AI | [AGENTS.md](AGENTS.md) → [docs/ai/README.md](docs/ai/README.md) |

> [!IMPORTANT]
> README — это **стабильная карта для человека**, а не live status ledger. Для текущего H11 admission, активных PR, runtime authority и production state используй `STATUS.md`, `project-state.json` и live GitHub.

## ⚖️ Что означает evidence

| Слой | Что подтверждает | Чего не подтверждает |
|---|---|---|
| 🏛️ Architecture | заявленный смысл/invariants | обязательность одной реализации |
| 🧪 Laboratory | bounded reproducible behavior | production readiness |
| 📊 Evidence | scoped support/refutation | автоматическое продвижение в Canon |
| 🧾 Receipt | provenance операции | semantic correctness само по себе |
| 🚦 Runtime gate | явную authority | разрешение только из-за passing tests |

## 🗂️ Карта репозитория

`README` 👤 вход для человека · `STATUS` 🚦 live human state · `project-state.json` 🧾 machine state · `docs/` 📚 architecture/research · `evidence/` 📊 evidence · `experiments/` 🧪 experiments · `src/` 🔧 reference implementation · `tests/` ✅ conformance · `tools/` 🛠️ validators.

## 🚫 Что проект не утверждает

Репозиторий не утверждает, что текущая реализация — universal Canon, что один storage/model/language обязателен, или что passing tests автоматически разрешают runtime expansion либо production.

> **Реализации могут меняться. Семантические обязательства должны либо пережить замену, либо быть явно пересмотрены на основании evidence.**
# 🧬 Velantrim Native Kernel

**[English](README.md) · [Русский](README.ru.md)**

> Technology-neutral research architecture for durable meaning, memory, provenance, change, and explanation.

Native Kernel asks: **what semantic properties must survive when databases, languages, models, storage engines, or compute substrates change?**

It is not an OS kernel, database product, vector store, or LLM memory plugin. The current codebase is a **bounded reference laboratory**, not the final definition of the architecture.

## 🧭 Project in one view

```text
🏛️ Meaning / invariants
        ↓
📐 Abstract contracts
        ↓
🔌 Replaceable profiles
        ↓
🧪 Bounded laboratory
        ↓
📊 Evidence / conformance
        ↓
🚦 Separate Canon / runtime decision
```

**Core discipline:** `meaning ≠ implementation` · `implementation ≠ universal proof` · `laboratory success ≠ Final Canon` · `merged code ≠ runtime authority`.

## 🌳 Main layers

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

## 📚 Start here

| Goal | Document |
|---|---|
| 👤 Understand the project | [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md) |
| 🚦 Current authoritative state | [STATUS.md](STATUS.md) |
| 🧾 Machine state | [project-state.json](project-state.json) |
| 🏛️ Architecture | [docs/ARCHITECTURE_REFOUNDATION.md](docs/ARCHITECTURE_REFOUNDATION.md) |
| 🧪 Run the laboratory | [docs/QUICKSTART.md](docs/QUICKSTART.md) |
| 🔬 Research | [docs/research/](docs/research/) |
| 🤖 AI entry | [AGENTS.md](AGENTS.md) → [docs/ai/README.md](docs/ai/README.md) |

> [!IMPORTANT]
> This README is the **stable human map**, not the live status ledger. Use `STATUS.md`, `project-state.json`, and live GitHub for current H11 admission, active PRs, runtime authority, and production state.

## ⚖️ What evidence means

| Layer | Proves | Does not prove |
|---|---|---|
| 🏛️ Architecture | declared meaning/invariants | one implementation is mandatory |
| 🧪 Laboratory | bounded reproducible behavior | production readiness |
| 📊 Evidence | scoped support/refutation | automatic Canon promotion |
| 🧾 Receipt | provenance of an operation | semantic correctness by itself |
| 🚦 Runtime gate | explicit authority | permission from passing tests |

## 🗂️ Repository map

`README` 👤 human entry · `STATUS` 🚦 live human state · `project-state.json` 🧾 machine state · `docs/` 📚 architecture/research · `evidence/` 📊 evidence · `experiments/` 🧪 experiments · `src/` 🔧 reference implementation · `tests/` ✅ conformance · `tools/` 🛠️ validators.

## 🚫 Non-goals

The repository does not claim that the current implementation is universal Canon, that one storage/model/language is mandatory, or that passing tests automatically authorizes runtime expansion or production.

> **Implementations may change. Semantic obligations must either survive the change or be explicitly revised with evidence.**
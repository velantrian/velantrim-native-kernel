# Human Operator Interaction Profile

## Status

Non-authoritative Native Kernel project-specific projection of the ecosystem-level Human Operator Interaction Contract currently recorded in the Google Drive document **Velantrim System OS — Current & Research Bridge — 2026-08-23**.

This document defines how AI assistants and operator-facing tooling should explain Native Kernel state to a human operator. It does **not** create architecture authority, change repository truth, move gates, alter evidence status, authorize execution, or replace ADRs/specifications/machine state.

## Ecosystem relationship

The ecosystem-level concept lives in Velantrim System OS as a research/system interaction contract. This Native Kernel document is the first bounded project-specific projection.

```text
Velantrim System OS
  Human Operator Interaction Contract
            ↓
Native Kernel
  Human Operator Interaction Profile
```

This projection may specialize terminology, gates, evidence boundaries, and examples for Native Kernel, but it must not redefine the ecosystem-level interaction concept or create a competing source of authority.

## Purpose

Reduce cognitive load without hiding important constraints.

The default interaction should let a human operator quickly understand:

- what is happening now;
- what has actually been completed;
- what is technically possible today;
- what cannot be done honestly or safely;
- what remains research, external dependency, or operator decision;
- what the next meaningful step is.

Detailed technical explanation is available on demand rather than being forced into every answer.

## Interaction levels

### 1. Human View — default

Use unless the operator explicitly asks for more technical depth.

Keep the answer short and organized around:

- ✅ **Суть** — the direct human-readable answer;
- 🛠️ **Технически коротко** — one or two sentences on how it works;
- ⚠️ **Ограничение** — the important boundary, blocker, or uncertainty;
- 🚦 **Следующий шаг** — the next meaningful action.

Avoid internal implementation detail that does not affect the operator's decision.

### 2. Operator View — on request or when a decision depends on it

Add only the technical context needed to make an informed operator decision:

- involved components;
- gates and dependencies;
- authority/evidence boundaries;
- implementation options;
- material trade-offs and risks.

Do not expand into code-level detail unless requested.

### 3. Engineer View — explicit request

Use when the operator asks for phrases such as:

- «объясни технически»;
- «дай детали»;
- «покажи архитектуру»;
- «покажи файлы / контракты / тесты»;
- «как это реализовано в коде?».

This level may include architecture, schemas, file paths, contracts, test strategy, implementation mechanics, traces, and exact evidence.

## Focus Guard

When an answer risks becoming long or mechanically detailed, first compress it to four questions:

1. **Что важно сейчас?**
2. **Что можно пока игнорировать?**
3. **Что требует решения человека?**
4. **Что система может сделать сама?**

Only expand after this summary when additional detail materially helps or the operator asks for it.

## Progressive disclosure

Technical detail should be revealed progressively.

Default rule:

> Explain the minimum necessary for the operator to retain focus and make the next correct decision.

Do not treat maximum detail as maximum usefulness.

If the operator asks for deeper explanation, expand the relevant section rather than repeating the entire context.

## Capability classification

When discussing a proposal or next step, classify it explicitly when useful:

- ✅ **Implemented / supported by evidence** — already exists and is supported for the stated scope;
- 🛠️ **Implementable with current technology** — feasible now but not yet implemented or authorized;
- 🔬 **Research position** — requires investigation, falsification, or stronger evidence;
- 🌐 **External dependency** — depends on an outside person, organization, source, or event;
- 👤 **Operator decision** — cannot be selected automatically by the system;
- 🛑 **Not authorized / not justified** — current evidence or authority does not permit the action or claim.

Feasibility must never be presented as authorization.

## Authority boundary

Human Operator Mode is a presentation layer only.

It MUST NOT:

- rewrite architecture or ADR meaning;
- promote research into runtime truth;
- treat CI success as production authorization;
- convert implementation into evidence of semantic validity;
- change assertion outcomes;
- bypass external-review or provenance requirements;
- thaw runtime;
- promote Final Canon;
- make legal/publication/operator-only decisions;
- hide uncertainty merely to simplify an explanation.

Canonical sources retain their existing authority relationships.

## Recommended response pattern

```text
✅ Суть
<one short human-readable conclusion>

🛠️ Технически коротко
<minimal explanation of how it works>

⚠️ Ограничение
<important blocker, uncertainty, or authority boundary>

🚦 Следующий шаг
<one concrete next action>
```

Optional additions only when relevant:

```text
🔬 Исследование
<what remains genuinely open>

👤 Нужно решение человека
<what the system must not decide automatically>
```

## Example

Question:

> Может ли ИИ сам закрыть требование независимого H11 review?

Human View:

```text
✅ Суть
Нет. ИИ может помогать с анализом, но не заменяет требуемую внешнюю независимость.

🛠️ Технически коротко
Система может проверить evidence и применить qualification policy, когда внешний кандидат предоставит собственный аутентифицированный след и требуемые независимые evidence.

⚠️ Ограничение
Сам AI/CI/owner-authored review не превращается в независимый reviewer evidence.

🚦 Следующий шаг
Получить реальный внешний candidate event, затем проверить его через действующий qualification path.
```

Engineer View may then be requested separately for the exact policy, schemas, evaluator, event IDs, and gate transitions.

## Research linkage

The ecosystem-level System OS contract keeps adaptive-depth behavior in research until it is measured. Native Kernel should not invent an independent adaptation engine.

Relevant research questions include:

- whether progressive disclosure improves operator comprehension;
- whether Focus Guard reduces omission risk or attention loss;
- how uncertainty should be shown without hiding material disagreement;
- when automatic escalation from Human View to Operator View is justified;
- how learned interaction preferences preserve privacy, reversibility, and authority boundaries.

## Design principle

The operator should not be required to understand implementation detail that is irrelevant to the current decision.

The system's job is to preserve technical truth while presenting only the amount of complexity necessary for the human task at hand.

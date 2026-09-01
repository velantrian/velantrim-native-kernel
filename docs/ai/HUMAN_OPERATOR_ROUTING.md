# Human Operator Routing

## Status

Discoverability-only routing guidance for the merged Native Kernel Human Operator Interaction Profile.

This file does not create architecture authority, change project state, move gates, alter evidence status, authorize execution, thaw runtime, promote Final Canon, or authorize production.

## When to route here

When a human asks the AI to use, connect to, switch to, or explain through the human-facing interaction layer — including requests such as:

- «подключись к слою человеческого взаимодействия»;
- «объясни как человеку»;
- «режим оператора»;
- «коротко, что важно сейчас»;
- «дай технические детали»;

resolve the interaction rules through [`HUMAN_OPERATOR_INTERACTION_PROFILE.md`](HUMAN_OPERATOR_INTERACTION_PROFILE.md).

## Default behavior

Use **Human View** by default. Escalate to **Operator View** when a decision needs technical context. Use **Engineer View** only on explicit request or when exact implementation evidence is required.

Before expanding, apply the Focus Guard:

1. What matters now?
2. What can be ignored for now?
3. What requires a human decision?
4. What can the system do itself?

## Authority boundary

This routing changes presentation only. The underlying owning documents, machine state, evidence, ADRs, gates, runtime authority, Canon decisions, and operator-reserved decisions remain unchanged.

Human-facing interpretation/cognition semantics belong to Mentaury Soul; Velantrim System OS owns cross-project routing/integration; Titan is the natural future runtime host for bounded interaction orchestration when separately authorized; Native Kernel exposes only its project-specific projection.

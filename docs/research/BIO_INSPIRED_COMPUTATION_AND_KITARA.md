# 🌿 Bio-Inspired Computation and Kitara

> **Status:** `PROPOSED / EXPERIMENTAL / NOT IMPLEMENTED`  
> **Architecture placement:** optional research profile outside Native Kernel Canon  
> **Issue #1:** not part of the controlled `v0.1.2.1` import  
> **Runtime dependency:** none
>
> This document records hypotheses extracted from an external Grok audit and design discussion supplied by the maintainer on 2026-07-23. The source is an input to research, not implementation evidence and not scientific proof.

**[English](./BIO_INSPIRED_COMPUTATION_AND_KITARA.md) · [Русский](./BIO_INSPIRED_COMPUTATION_AND_KITARA.ru.md)**

---

## 1. Why this document exists

The source material combines a repository audit with a separate future-facing discussion about biological systems, sensing, motor memory, distributed computation, and a possible system called **Kitara**.

Those ideas may be useful, but they must not be silently promoted into Native Kernel Canon.

```text
Native Kernel Canon
        ≠
bio-inspired implementation hypothesis
        ≠
Kitara future system
        ≠
scientific claim about biological intelligence
```

This document preserves the useful architectural patterns while marking the boundary clearly.

---

## 2. Project relationship

```text
🧬 Native Kernel
architecture for identity, event history, provenance,
time, conflict visibility, reconstruction, and Receipts

🔱 Titan
broader cognitive research environment and possible evaluator

🌿 Kitara
possible future embodied / bio-inspired research system

💎 Crystal
independent trust-facing product
```

Kitara is not currently a Native Kernel module, product commitment, or implementation dependency.

Native Kernel may define contracts that a future Kitara profile could use. Kitara-specific sensors, bodies, affective modulation, motor behaviour, or distributed routing remain outside Canon unless separately evaluated and approved.

---

## 3. Source-derived hypotheses

The supplied material proposes several patterns inspired by living systems:

1. **Distributed processing** — useful work can occur across a network rather than only in one central processor.
2. **Peripheral event processing** — local components filter and compress signals before sending meaningful events upstream.
3. **Adaptive gain** — sensitivity changes with context, risk, novelty, or task state.
4. **Sensorimotor loops** — perception and action can be coupled directly for bounded responses.
5. **Procedural or motor memory** — the system may remember successful action patterns, not only declarative Claims.
6. **Flow reinforcement** — frequently useful routes strengthen while weak routes decay.
7. **Multimodal fusion** — signals from different channels should be combined without collapsing their provenance.
8. **Graceful degradation** — distributed systems should continue bounded operation after partial damage or disconnection.

These are research hypotheses. The source does not prove that any one biological system provides a complete computational architecture for Velantrim.

---

## 4. Architectural extraction

The useful abstraction is not “copy a plant, fungus, insect, or animal.”

The useful abstraction is:

```text
local sensing
    ↓
local filtering and confidence
    ↓
typed event with provenance
    ↓
context-dependent gain
    ↓
distributed routing / competition
    ↓
bounded action or candidate context
    ↓
outcome event and Receipt
```

A future implementation may use conventional software, robotics, neuromorphic hardware, analog systems, or other substrates. Biological metaphors do not determine the implementation.

---

## 5. Proposed experimental layers

### 5.1 Peripheral Event Processing

A peripheral component may transform a continuous or noisy signal into a smaller typed event.

```text
raw stream
    ↓
calibration
    ↓
change / anomaly detection
    ↓
typed observation event
    ↓
central or distributed processing
```

Required boundaries:

- raw data and derived event remain distinguishable;
- provenance records the sensor, calibration, time, and transformation;
- filtering must not silently convert uncertainty into truth;
- local failure must be visible in diagnostics or Receipts.

### 5.2 Adaptive Gain

Gain changes operational sensitivity or priority.

```text
gain / salience / charge
        ≠
truth / evidence / epistemic status
```

A high-gain observation may deserve attention. It does not become more correct merely because it is urgent or repeated.

### 5.3 Sensorimotor Coupling

A future embodied system may support bounded reflex-like paths:

```text
observation
    ↓
validated local policy
    ↓
action
    ↓
outcome event
    ↓
Receipt and later review
```

Safety-critical or irreversible actions require explicit policy, authorization, rollback where possible, and independent review. Native Kernel itself does not grant actuator authority.

### 5.4 Procedural / Motor Memory

Procedural memory may represent:

- an action sequence;
- context and preconditions;
- expected and observed outcomes;
- failures and recovery paths;
- evidence of repetition or success;
- operator permissions.

Procedural success is evidence about an action policy, not evidence that unrelated semantic Claims are true.

### 5.5 Distributed Network Adaptation

A distributed profile may reinforce routes based on successful flow or utility. The route model must remain a projection or policy state unless a separate decision promotes part of it into an abstract contract.

---

## 6. Physarum-like routing

The strongest bounded idea in the source is a **Physarum-like adaptive flow algorithm**.

Conceptually:

```text
candidate graph
      ↓
flow through available paths
      ↓
useful paths gain conductivity
      ↓
unused paths decay
      ↓
adaptive routing state
```

Possible uses:

- context-routing experiments;
- graph traversal under changing costs;
- multiple-path discovery;
- adaptation after edge removal;
- allocation of a retrieval or compute budget;
- long-term route reinforcement.

Hard boundary:

```text
Physarum-like routing
may recommend where activation flows

Physarum-like routing
must not decide semantic truth
```

The algorithm is not assumed to find a global optimum for every task. Any claim about convergence, optimality, speed, or robustness must be tied to a defined model and reproducible experiment.

See [`PHYSARUM_ROUTING_EXPERIMENT.md`](./PHYSARUM_ROUTING_EXPERIMENT.md).

---

## 7. Multimodal and bio-sensor research

The source discusses possible sensing inspired by animals, insects, plants, fungi, and other organisms.

A future research system may study:

- chemical gradients;
- mechanical vibration;
- acoustic and visual signals;
- magnetic or electric-field sensing;
- temperature, humidity, pressure, and light;
- distributed sensor surfaces;
- local multimodal fusion.

This document does **not** claim that plants, fungi, or other organisms possess human-like cognition, intention, or language. Biological observations must be separated from metaphorical interpretation.

A machine sensor profile should be evaluated by measurable properties:

- range and resolution;
- calibration drift;
- latency;
- false-positive and false-negative rates;
- energy and compute cost;
- failure isolation;
- provenance completeness;
- privacy and safety impact.

---

## 8. What belongs to Native Kernel

Native Kernel may provide technology-neutral contracts for:

- typed observations;
- provenance;
- event history;
- temporal scope;
- policy decisions;
- outcome records;
- conflict and uncertainty visibility;
- reconstructable state;
- accountable Receipts.

Native Kernel does not need to define:

- a particular biological metaphor;
- physical sensors;
- actuator mechanics;
- a fixed emotional model;
- one flow algorithm;
- one robot body;
- one neuromorphic or analog substrate.

---

## 9. Claims explicitly rejected at this stage

```text
🚫 Event history is automatically truth.
🚫 A highly activated route is automatically correct.
🚫 Physarum solves every optimization problem.
🚫 Biological systems provide a ready-made AI architecture.
🚫 Plants or fungi are assumed to have human-like cognition.
🚫 Embodiment automatically creates understanding.
🚫 Adaptive gain may bypass admission or safety policy.
🚫 Motor habit may act without authorization boundaries.
🚫 Kitara is already implemented or production-ready.
🚫 This work expands Issue #1.
```

---

## 10. Promotion path

A bio-inspired hypothesis may move forward only through:

```text
source-derived hypothesis
        ↓
neutral architectural abstraction
        ↓
bounded experiment
        ↓
baseline comparison
        ↓
failure and safety analysis
        ↓
Receipt and reproducible report
        ↓
ADR / RFC
        ↓
operator decision
```

Multi-model enthusiasm, biological analogy, or attractive visualization is not approval.

---

## 11. Initial research priorities

| Priority | Experiment | Why first |
|---|---|---|
| **P1** | Physarum-like routing on a synthetic Claim graph | bounded, measurable, does not require sensors or live writes |
| **P2** | Adaptive gain versus fixed ranking | tests attention without changing truth state |
| **P3** | Peripheral event filtering on recorded sensor data | tests compression, provenance, and error visibility |
| **P4** | Procedural-memory representation | tests action/outcome semantics without actuator deployment |
| **P5** | Multimodal fusion | higher complexity; requires calibration and uncertainty policy |
| **P6** | Embodied sensorimotor loop | blocked on safety, authorization, and rollback design |

---

## 12. Decision summary

> **Bio-inspired computation is retained as an optional experimental research track. Physarum-like flow, adaptive gain, peripheral processing, procedural memory, and sensorimotor loops may be tested as replaceable profiles. They do not redefine Native Kernel Canon, do not determine truth, and do not enter the controlled prototype import.**

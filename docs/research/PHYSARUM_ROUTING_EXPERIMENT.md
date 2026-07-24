# 🦠 Physarum-Like Routing Experiment

> **Status:** `PROPOSED / NOT IMPLEMENTED`  
> **Purpose:** test adaptive flow routing without changing Native Kernel truth semantics  
> **Architecture placement:** experimental retrieval / activation profile  
> **Issue #1:** out of scope

**[English](./PHYSARUM_ROUTING_EXPERIMENT.md) · [Русский](./PHYSARUM_ROUTING_EXPERIMENT.ru.md)**

---

## 1. Research question

Can a Physarum-like adaptive flow model improve route selection on a changing Claim graph while remaining reproducible, explainable, and subordinate to Native Kernel eligibility and epistemic rules?

The experiment tests routing behaviour only.

```text
routing quality
    ≠
truth quality
```

---

## 2. Hypothesis

A flow-reinforcement profile may:

- discover useful alternative paths;
- adapt after edge-cost changes or edge removal;
- reduce unnecessary activation;
- retain route history in an inspectable policy state;
- produce a Receipt explaining why a route was strengthened or weakened.

The experiment does not assume universal optimality.

---

## 3. Test graph

Use a synthetic graph with:

- 100–1,000 Claims;
- typed directed edges;
- declared edge costs;
- several valid paths between selected endpoints;
- irrelevant branches;
- contested or ineligible Claims;
- controlled edge removal and cost changes.

The graph must be generated from a fixed seed and committed as a reproducible fixture.

---

## 4. Compared profiles

| Profile | Role |
|---|---|
| Shortest path | deterministic cost baseline |
| Breadth-first or bounded traversal | simple structural baseline |
| Personalized PageRank or existing activation baseline | diffusion baseline where available |
| Physarum-like flow | experimental adaptive profile |

All profiles receive the same eligible graph and task budget.

---

## 5. Safety and semantic boundary

Before routing:

```text
Admission / eligibility / access / temporal policy
                    ↓
              eligible graph
                    ↓
          routing profile comparison
```

The routing algorithm may not:

- promote a Claim into a higher epistemic state;
- bypass access or deletion restrictions;
- hide contested Claims;
- convert repeated use into evidence of truth;
- write into authoritative history without a separate command and policy decision.

---

## 6. Experimental dynamics

A candidate implementation may maintain edge conductivity `D_e` and update it from observed flow.

The exact equation is not Canon and must be documented by the implementation profile.

Minimum required controls:

- initial conductivity;
- decay rate;
- reinforcement rate;
- flow normalization;
- maximum iterations;
- convergence threshold;
- deterministic tie-breaking or declared stochastic seed;
- budget cap.

---

## 7. Scenarios

### Scenario A — Stable graph

Measure route quality and convergence on an unchanged graph.

### Scenario B — Edge removal

Remove one high-conductivity edge and measure recovery.

### Scenario C — Cost change

Increase the cost of a previously preferred path and observe adaptation.

### Scenario D — Multiple useful paths

Check whether the profile preserves useful alternatives instead of collapsing immediately to one path.

### Scenario E — Ineligible node

Mark a highly connected Claim ineligible and verify that routing never uses it.

### Scenario F — Noisy branches

Add many irrelevant branches and measure activated-to-used ratio.

---

## 8. Metrics

| Metric | Meaning |
|---|---|
| Path cost | total declared cost of selected route |
| Regret versus baseline | distance from best declared baseline result |
| Convergence iterations | updates required to stabilize |
| Recovery time | iterations after graph change |
| Alternative-path retention | whether useful secondary paths remain available |
| Activated-to-used ratio | routing efficiency |
| Determinism | parity under repeated fixed-seed runs |
| Receipt completeness | whether route choice and updates are explainable |
| Ineligible-node violations | must remain zero |
| Runtime and memory | bounded resource cost |

---

## 9. Receipt requirements

Each run should record:

```yaml
experiment_id: ...
profile: physarum_like
fixture_version: ...
seed: ...
source_claim: ...
target_claim: ...
eligibility_policy: ...
parameters: ...
selected_paths: ...
reinforced_edges: ...
decayed_edges: ...
excluded_nodes: ...
iterations: ...
converged: true|false
metrics: ...
limitations: ...
```

The Receipt explains the run. It does not certify semantic correctness of the Claims.

---

## 10. Acceptance gate

The profile may advance to a deeper RFC only if:

1. runs are reproducible from committed fixtures;
2. ineligible-node violations are zero;
3. adaptation after edge removal is demonstrated;
4. at least one baseline comparison is reported honestly;
5. failure cases and parameter sensitivity are documented;
6. routing state can be deleted without destroying authoritative history;
7. no truth or production claim is made from routing performance.

---

## 11. Rejection or pause conditions

Pause or reject the profile if:

- results depend on unstable hidden randomness;
- parameter tuning dominates any architectural benefit;
- it consistently performs worse than simpler baselines;
- Receipts cannot explain route changes;
- flow reinforcement creates truth-like authority;
- the profile requires Canon redesign before demonstrating value;
- resource cost is unbounded or unsuitable for the intended workload.

---

## 12. Next step after success

```text
bounded synthetic result
        ↓
recorded realistic graph workload
        ↓
Offline Shadow comparison
        ↓
separate ADR / RFC
        ↓
operator decision
```

No live integration is implied by a successful synthetic experiment.

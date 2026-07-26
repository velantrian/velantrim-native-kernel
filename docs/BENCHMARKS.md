# Benchmark Methodology

## Purpose

Benchmarks in this repository are diagnostic tools, not production capacity claims. They are intended to reveal workload behaviour, scaling shape, and regressions in bounded research profiles.

No benchmark result upgrades the repository from `DOCUMENTED_ONLY` while the authentic source snapshot and runnable harness are absent.

## Benchmark identity and lineage

Every published measurement set must have a stable `benchmark_id`. Results with different IDs are separate workloads unless a comparison artifact proves equivalence.

| Benchmark ID | Workload | Workload evidence | Historical timing evidence | Scaling evidence | Production capacity | Source snapshot |
|---|---|---|---|---|---|---|
| `NK-BM-V0121-SELECTIVE-001` | selective activation query | `EXTERNALLY_OBSERVED` | `EXTERNALLY_OBSERVED` | `EXTERNALLY_OBSERVED` | `NOT_EVALUATED` | reported local `v0.1.2.1`; source unavailable |
| `NK-BM-V0121-BROAD-001` | broad activation query | `EXTERNALLY_OBSERVED` | `EXTERNALLY_OBSERVED` | `EXTERNALLY_OBSERVED` | `NOT_EVALUATED` | reported local `v0.1.2.1`; source unavailable |
| `NK-BM-LEGACY-INDEXED-001` | earlier indexed read-path table preserved in Notion | `EXTERNALLY_OBSERVED` | `EXTERNALLY_OBSERVED` | `NOT_ESTABLISHED` | `NOT_EVALUATED` | local lineage not fully identified |

These benchmark IDs identify records; they do not upgrade evidence.

The three workloads must not be numerically compared as if they were repetitions of one benchmark. In particular, values at the same Claim count may come from different activation breadth, corpus construction, code revision, environment, or timing boundary.

## Independent evidence dimensions

Benchmark statements must distinguish:

```text
workload reproduced
≠ historical absolute timing reproduced
≠ scaling shape observed
≠ production capacity validated
```

### Workload evidence

Whether the corpus generation, activation pattern, query semantics, and timing boundary are reviewable and reproducible.

### Historical timing evidence

Whether the historical absolute values were reproduced in a sufficiently comparable environment.

### Scaling evidence

Whether the observed growth shape is supported by enough points, repetitions, diagnostics, and declared workload bounds.

### Production capacity

Whether a controlled operational environment has established throughput, latency objectives, resource limits, reliability, and incident behaviour. Repository microbenchmarks do not establish this.

## Prior local observations

The following measurements were previously reported from one local environment. They are retained only as external historical targets until the authentic code, benchmark harness, corpus generator, and environment are recovered or independently re-established under a new evidence lineage.

### `NK-BM-V0121-SELECTIVE-001` — Selective query

```text
50 claims    0.000540 s
100          0.000961 s
200          0.001856 s
400          0.003753 s
800          0.011988 s
1600         0.029115 s
```

### `NK-BM-V0121-BROAD-001` — Broad query

```text
50 claims    0.000777 s
100          0.001550 s
200          0.004160 s
400          0.016250 s
800          0.046970 s
```

These numbers are environment-specific, externally observed, and not repository reproduced. They must not be quoted as stable product performance.

## Interpretation boundary

The historical report stated that the selective workload benefited from an event index and cached charge calculations, while the broad workload remained superlinear because of repeated neighbour discovery, conclusion checks, and greedy ablation work.

The only currently supportable wording is:

```text
External observations reported faster selective read paths than an earlier prototype.
External observations also reported that the complete broad-query path remained superlinear.
Neither claim is currently reproducible from main.
```

## Reproduction gate

Before a workload becomes repository evidence, a dedicated benchmark artifact must be merged with:

- stable benchmark IDs emitted in every result;
- authentic source-snapshot hash or a clearly new implementation lineage;
- deterministic synthetic corpus generation;
- explicit selective and broad-query definitions;
- declared activation breadth;
- warm-up runs;
- multiple repetitions;
- median and p95 reporting;
- Python and dependency identity;
- OS, runner/container, and CPU metadata;
- repository commit SHA;
- seed and corpus parameters;
- timestamp;
- explicit separation between snapshot construction and query timing;
- machine-readable raw results.

A GitHub-hosted runner may establish workload reproducibility and detect regressions. It does not automatically establish historical absolute timing equivalence because hosted CPU allocation and contention are not stable.

## Recommended evidence record

```yaml
benchmark_id: NK-BM-V0121-SELECTIVE-001
source_snapshot_sha256: <sha256>
repository_commit: <sha>
workload_evidence: REPOSITORY_REPRODUCED
historical_timing_evidence: EXTERNALLY_OBSERVED
scaling_shape_evidence: REPOSITORY_OBSERVED
production_capacity: NOT_EVALUATED
python: <version>
dependency_lock_sha256: <sha256>
os: <value>
cpu: <value>
runner_or_container: <value>
seed: <value>
corpus_parameters: {}
warmup_iterations: 0
measured_iterations: 0
median_seconds: 0
p95_seconds: 0
snapshot_build_seconds: 0
query_seconds: 0
timestamp: <ISO-8601>
```

## Benchmark rules

1. Record benchmark ID, source lineage, Python, dependencies, OS, CPU, runner/container, commit SHA, seed, corpus parameters, and timestamp.
2. Warm up before timed iterations.
3. Use multiple repetitions and report median and p95.
4. Keep corpus generation deterministic.
5. Separate selective and broad activation workloads.
6. Declare activation breadth and timing boundaries.
7. Do not combine snapshot build and query timing without saying so.
8. Do not claim asymptotic complexity from a small number of points.
9. Treat regressions as investigation signals, not automatic architectural verdicts.
10. Do not present prototype numbers as Crystal or Titan production performance.
11. Keep workload evidence, historical timing evidence, scaling evidence, and production capacity separate.
12. Mark all external observations as external until supported by committed, reviewable artifacts.

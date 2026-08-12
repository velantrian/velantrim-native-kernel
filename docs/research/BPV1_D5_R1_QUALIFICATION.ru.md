# BPV1-001 D5-R1 — квалификация доказательств

Статус: **CANDIDATE / НЕ AUTHORITATIVE ДО MERGE PR + ЗЕЛЁНОГО POST-MERGE CI**  
Scope: только BPV1-001  
Исторический D5 merge: `a191e9c868c14af34a269dcdfae44406f1013bda`  
Frozen plan merge: `a538d7f1e28858a88b9ee777ac7d6e05b85943db`  
Frozen plan SHA-256: `7fe8174c604678c6b79d3fdeae83d7c5ab0d2fb15bfe343d41659d05d9496ad0`

## Зачем нужен D5-R1

PR #114 механически завершил D5 и получил `SUPPORTED_FOR_SCOPE`, однако post-merge аудит обнаружил четыре недостатка квалификации, которые нужно устранить до того, как D6 начнёт классифицировать A10-гипотезы:

1. current-truth surfaces репозитория всё ещё называли исполнение BPV1 subject следующим gate;
2. несколько структурных полей, проверяемых oracle, выдавались самим Rust-subject как готовые boolean-утверждения, что создавало HR10 self-report problem;
3. локальный corruption digest не покрывал `evidence` и `epistemic_position`;
4. хранилище подробных `loss_witnesses` не имело собственного retained-record bound.

D5-R1 — ограниченный corrective/qualification pass. Он не меняет preregistered semantics и не подгоняет критерии под уже полученный результат.

## Frozen authority не меняется

D5-R1 не имеет права изменять:

- `docs/research/BPV1_PREREGISTRATION.{json,md,ru.md}`;
- `experiments/bpv1/BPV1-001/admission/**`;
- `tools/bpv1/evaluate.py`;
- scenario identity, target hypotheses, HR01-HR10, expected fixture outcomes или thresholds.

CI scope guard закрывается с ошибкой при изменении этих путей.

## Исправленный evidence path

```text
Rust subject
  -> raw implementation-neutral facts
  -> внешний qualifier без frozen expected outcomes
  -> nk-bpv1-observations/1
  -> неизменённый frozen evaluator + fixture oracle
  -> outcome
```

Rust-subject больше не выдаёт oracle-facing значения о том, что отсутствует authoritative per-operation log, exact replay requirement или reuse текущей реализации. Эти свойства выводятся внешним qualifier из структуры исходного кода и попадают в observation bundle только если действительно установлены. Если нужное свойство установить нельзя, observable остаётся отсутствующим, и неизменённый evaluator может вернуть `INDETERMINATE`, а не получить искусственно заданный `false`.

Qualifier фиксирует:

- `oracle_fixture_expectations_read: false`;
- `implementation_private_runtime_state_read: false`;
- `subject_self_report_used_for_structural_oracle_fields: false`.

Таким образом устранён конкретный self-report pathway, из-за которого возник HR10-вопрос. Это не создаёт independent-team или independent-custody evidence.

## Усиление FX07

Integrity digest теперь покрывает materially relevant поля claim, включая список evidence и epistemic position. Дополнительные Rust-тесты меняют эти поля без пересчёта digest и требуют обнаружения corruption.

Frozen expected semantics FX07 не изменены.

## Bounded loss-witness storage

Подробные retained loss witnesses ограничены 32 записями. При превышении cap старые подробные witnesses сворачиваются в один bounded per-slot rollup с aggregate count, диапазоном witness IDs, количеством compacted detail по каждому slot и первым/последним compacted version ID. Это не является молчаливой потерей и не заменяет witness list новым бесконечным журналом.

Отдельный engineering stress test на 96 циклах проверяет механизм за пределами preregistered 16-cycle workload. Этот stress test не входит в adjudication BPV1-001 и не меняет frozen workload или thresholds.

## Qualification run до сохранения evidence

Exact head `5433ec0e56a2882ddfdd44e1d131cdca1ee1a082` проверил исправленный путь до публикации D5-R1 bundle.

- AI context integrity: run `31549755468` — SUCCESS;
- BPV1 execution admission: run `31549755493` — SUCCESS;
- BPV1 subject falsification instrument: run `31549755461` — SUCCESS;
- Python 3.11 job `93969695483` — SUCCESS;
- Python 3.12 job `93969695477` — SUCCESS;
- external qualification: `QUALIFIED`;
- неизменённый frozen evaluator: `SUPPORTED_FOR_SCOPE`;
- mandatory fixtures: `12/12 PASS`;
- workload: 512 mutations; checkpoints 128/256/512; 52 retained detailed predecessors; 13 retained witness records; 42 276 durable bytes на mutation 512; growth rule PASS.

Более ранний candidate head получил тот же semantic result `QUALIFIED` / `SUPPORTED_FOR_SCOPE`, но workflow упал на слишком буквальном meta-test, запрещавшем даже текст `evaluate.py` в docstring. Тест исправлен так, чтобы проверять реальные Python imports/dependencies. Preregistration, oracle, fixture semantics и экспериментальные критерии при этом не менялись.

## Evidence identity

Candidate D5-R1 evidence хранится отдельно:

`experiments/bpv1/BPV1-001/results/d5-r1/`

Исторические evidence files PR #114 остаются неизменёнными.

## Non-claims и следующий gate

Эта квалификация не доказывает Final Canon, production readiness, universal substrate portability, independent team/custody или независимую computation model. Rust остаётся `EXPERIMENTAL_INSTRUMENT_NOT_CANON`. Product runtime integration не разрешена; runtime expansion остаётся `FROZEN`.

D6 A10 hypothesis classification остаётся **NOT STARTED** до merge D5-R1 package, зелёного post-merge CI, проверки late review и отдельного current-truth checkpoint, который свяжет authoritative D5-R1 merge.

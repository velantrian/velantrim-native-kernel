# Residual A10 Validation Plan — русский

**Состояние:** `PLANNING_ONLY / EXECUTION_NOT_AUTHORIZED`  
**Протокол:** `nk-residual-a10-validation-plan/1`  
**Plan ID:** `RAVP-001-residual-a10-validation-plan-v1`  
**Source checkpoint:** `ec421410d6ea5df86adca3a962ad2c5ba699e297`  
**Operator decision:** ADR-0027 / `OD-POST-D8-001`  
**Decision merge:** `57993f39906ae7266011f6146c9a485d0587d2bf`  
**Архитектура:** `STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL`  
**Runtime expansion:** `FROZEN`  
**Product runtime thaw:** `false`  
**Production:** `false`

**[English](./RESIDUAL_A10_VALIDATION_PLAN.md) · [Русский](./RESIDUAL_A10_VALIDATION_PLAN.ru.md)**

## 1. Назначение

Этот документ превращает шесть оставшихся после D6 гипотез A10 со статусом `NOT_TESTED` в ограниченную программу исследовательского планирования. Он **не** preregister, не реализует, не запускает и не adjudicate новый experiment.

Residual targets ровно шесть:

```text
A10-H03
A10-H06
A10-H08
A10-H09
A10-H10
A10-H11
```

Допустимые A10 outcomes остаются ровно такими:

```text
SUPPORTED_FOR_SCOPE
WEAKENED
REFUTED
INDETERMINATE
NOT_TESTED
```

Новый epistemic outcome этим планом не вводится.

Основной принцип:

```text
один research question
→ одна bounded falsification family
→ отдельная preregistration
→ отдельное execution-admission решение
→ только затем, если явно разрешено, implementation и execution
```

Поэтому один огромный «BPV-2» для несвязанных гипотез не является исходным design.

## 2. Граница полномочий

ADR-0027 разрешает только `RESIDUAL_A10_VALIDATION_PLAN` в scope `RESEARCH_PLANNING_ONLY`.

Этот план не разрешает:

- implementation или execution residual experiment;
- product runtime integration или runtime thaw;
- Final Canon promotion;
- production authorization;
- reducer v2 или новые Event verbs;
- NK-EPI runtime;
- решение Issue #18 по license/publication;
- решение Issue #74 / ADR-0024;
- admission recovered sources Track H;
- новую product DB, implementation profile или product hardware profile;
- universal substrate-independence claim.

Будущая family preregistration должна быть отдельным authority layer. Будущее execution admission — ещё одним отдельным authority layer.

## 3. Коррекция handoff: H11 — не federation

Точная гипотеза A10:

> `A10-H11` — Laboratory mechanisms can remain reproducible without becoming Architecture Canon.

Composition/federation — **отдельный** capability class из D7-F08. BPV1-001 был single-node, поэтому composed/federated conformance остаётся непроверенным, но это не смысл H11.

Если тестировать federation под названием H11, evidence будет отвечать не на ту гипотезу.

## 4. Классы независимости

Residual research должен явно называть независимость, а не считать «другой язык» синонимом «другого substrate».

| Класс | Смысл |
|---|---|
| `INDEPENDENT_LANGUAGE` | materially different implementation language |
| `INDEPENDENT_IMPLEMENTATION_STRUCTURE` | implementation не является тонким переводом/import того же internal structure |
| `INDEPENDENT_TEAM` | authorship независимо в заявленном scope |
| `INDEPENDENT_CUSTODY` | evidence/artifacts не контролируются только владельцем subject implementation |
| `INDEPENDENT_STORAGE_MODEL` | materially different persistence/memory mechanism, а не только SQL dialect/schema |
| `INDEPENDENT_COMPUTATION_MODEL` | materially different computation mechanism, а не только programming language |
| `INDEPENDENT_HARDWARE_FAMILY` | materially different physical carrier/processor family для проверяемого claim |
| `INDEPENDENT_SEMANTIC_ORACLE` | adjudication внешняя по отношению к subject и не зависит от private subject state |

Это независимые оси. Один experiment может квалифицироваться по части из них и не квалифицироваться по другим.

## 5. Общие fail-closed rules

Перед будущей preregistration каждая residual family должна сохранить следующие правила:

1. Subject не может выдавать себе authoritative PASS.
2. Implementation self-report максимум является raw input, но не semantic truth.
3. Private implementation state не может быть обязательным oracle input.
4. Failure conditions фиксируются до просмотра adjudication data.
5. Oracle logic и thresholds фиксируются до adjudication.
6. Post-hoc изменение criteria не может спасти failed run под тем же experiment identity.
7. `INDETERMINATE` — легитимный результат.
8. `NOT_TESTED` — легитимный результат.
9. Pilot/calibration data отделяются от adjudication data.
10. Raw fact capture отделяется от semantic qualification.
11. Qualifier отделён от subject.
12. Outcome vocabulary остаётся пятью A10 outcomes.

Test, который не может завершиться failure, не является A10 falsification test.

## 6. Family H03 — continuity при representation migration

### Hypothesis

`A10-H03`: scoped identity и lineage continuity могут пережить representation migration.

### Почему BPV1 этого не проверял

BPV1-001 создал materially different realization, но не выполнял source→target migration с adjudication identity/continuation relations через migration boundary.

### Testable question

Может ли materially different target representation сохранить заявленные semantic identity и lineage при изменении substrate-local identity, не превращая source bytes, hashes, row IDs или physical carrier identity в semantic criterion?

### Required independence

Минимальная цель планирования:

```text
INDEPENDENT_IMPLEMENTATION_STRUCTURE
INDEPENDENT_STORAGE_MODEL
INDEPENDENT_SEMANTIC_ORACLE
```

Independent language/team/custody усиливают evidence, но не предполагаются автоматически.

### Core observables

- pre/post typed identity relation vectors;
- `MIGRATED_FROM` / `CONTINUATION_OF` lineage;
- сохранение Context, Provenance и Authority;
- declared substrate-local identity change;
- declared loss vector;
- raw transformation facts отдельно от adjudication.

### Equivalence predicate

Migrated target сохраняет все materially required semantic identity/lineage relations для preregistered cases, даже если local IDs, bytes, layout, storage representation и operation sequence отличаются.

### Allowed losses

Можно терять source serialization, local address/row/object identity, non-semantic layout/indexing details и другую явно non-material metadata вне scope.

### Failure / hard refutation

Failure включает silent Provenance/Authority loss, невозможность различать требуемые identity relations или вывод semantic continuity только по copied physical identifiers.

Hard refutation возникает, если migration сохраняет все заявленные meaning-level content, но required identity/continuation невозможно обосновать без превращения source-format physical identity в universal architecture requirement.

### Oracle boundary

Frozen implementation-neutral migration oracle получает только externally exposed identity/provenance/lineage observations и declared loss, а не private target internals.

## 7. Family H06 — forgetting, disposal и erasure epistemics

### Hypothesis

`A10-H06`: forgetting/disposal можно представлять без утверждений о физическом состоянии substrate, которое невозможно достоверно наблюдать.

### Почему BPV1 этого не проверял

Physical и cryptographic erasure были вне BPV1 applicability. Logical compaction/loss witnesses не доказывают уничтожение physical residue или key material.

### Три независимые evidence lanes

H06 не должен превращаться в один неясный “delete test”.

| Lane | Что может быть установлено | Обязательная граница |
|---|---|---|
| `LOGICAL_FORGETTING` | semantic/logical unavailability в scope | physical/crypto state остаётся `INDETERMINATE`, если отдельно не наблюдался |
| `CRYPTOGRAPHIC_ERASURE` | bounded crypto-erasure при declared key/custody/recoverability assumptions | subject self-report alone — non-qualifying |
| `PHYSICAL_ERASURE` | bounded sanitization/physical erasure при independently inspectable recovery/residue boundary | opaque residue остаётся `INDETERMINATE` |

### Testable question

Может ли архитектура сохранять различия между restriction, logical disposal, semantic forgetting/loss, cryptographic erasure, physical erasure и unknown physical residue, никогда не выдавая claim сильнее, чем позволяет evidence?

### Observables

- semantic recovery/query result после forgetting;
- non-content-bearing disposition/accountability witness;
- independent key custody/sanitization evidence для crypto-erasure;
- independent sanitization/residue validation для physical-erasure;
- declared adversarial recovery effort boundary;
- explicit claim-strength classification.

### Failure / hard refutation

Failure: logical inaccessibility повышается до physical erasure; принимается self-authored PASS; forgetting трактуется как “never existed”; запрещённый recoverable material хранится только для доказательства его отсутствия.

Hard refutation: semantic distinction между logical forgetting, cryptographic erasure, physical erasure и unknown residue невозможно сохранить без хранения запрещённого материала или unjustifiably strong claim.

### Роль внешних исследований

NIST SP 800-88 Rev. 2 используется только как design reference по media sanitization, cryptographic erase и validation/trust boundaries. Он не является Native Kernel authority и не создаёт H06 outcome сам по себе.

## 8. Family H08 — non-address-based dynamical continuity

### Hypothesis

`A10-H08`: non-address-based substrate может сохранять semantic identity/history через relational или dynamical continuity вместо stable byte addresses.

### Почему BPV1 этого не проверял

BPV1 оставался conventional digital computation. Ни analog, ни neuromorphic physical realization не adjudicated.

### Qualification tiers

```text
SIMULATION_OR_EMULATION
  → только method rehearsal
  → не может поддержать H08

PHYSICAL_NON_ADDRESS_REALIZATION
  → eligible для H08 только при прохождении остальных gates

HYBRID_PROFILE
  → eligible только для declared hybrid scope
  → companion не может тайно хранить весь authoritative semantic state
```

### Testable question

Может ли physical non-address-based dynamical realization сохранять scoped identity, lineage и accountability, когда exact microstate, stable row/byte/neuron address и exact deterministic replay недоступны?

### Required independence

```text
INDEPENDENT_COMPUTATION_MODEL
INDEPENDENT_HARDWARE_FAMILY
INDEPENDENT_IMPLEMENTATION_STRUCTURE
INDEPENDENT_SEMANTIC_ORACLE
```

### Anti-shadow rule

Conventional companion допустим только как явно ограниченная часть hybrid profile. Если именно companion хранит весь authoritative semantic state/history, а analog/neuromorphic component — лишь accelerator/calculator, такой run не поддерживает H08.

### Allowed losses

Допустимо потерять exact microstate, exact neuron/synapse/device identity, exact replay path, non-semantic physical coordinates и exact timings/weights вне declared semantic scope.

### Failure / hard refutation

Failure: hidden stable-address identity, full digital shadow, promotion simulation to hardware evidence, либо semantic observability доступна только через private internal state.

Hard refutation требует qualifying physical non-address-based realization, который не способен сохранить required semantic identity/lineage/accountability даже после явного исключения exact microstate и physical-address identity из требований.

## 9. Family H09 — probabilistic conformance

### Hypothesis

`A10-H09`: probabilistic substrates можно оценивать bounded statistical conformance без превращения uncertainty в failure.

### Почему BPV1 этого не проверял

Не было probabilistic substrate и preregistered repeated-trial statistical protocol.

### Qualification tiers

```text
SOFTWARE_STOCHASTIC_REHEARSAL
  → может квалифицировать statistical method
  → не может поддержать physical/probabilistic-substrate claim

MATERIALLY_PROBABILISTIC_REALIZATION
  → eligible только после semantic + statistical preregistration
```

### Two-layer oracle

H09 обязан разделять:

1. **hard semantic invariants** — zero-tolerance forbidden outcomes внутри declared scope;
2. **distributional obligations** — statistical properties с заранее заданными trial count/stopping rule, error/equivalence bounds и достаточной power.

Insufficient power → `INDETERMINATE`, не support.

### Failure / hard refutation

Failure: post-hoc thresholds, optional stopping, discarded adverse trials, объяснение любого semantic divergence как “noise”, либо insufficient-power data выдаётся за support.

Hard refutation: adequately powered preregistered protocol не способен отличить required semantics от stochastic divergence настолько, чтобы claim оставался falsifiable, либо hard invariant воспроизводимо нарушается в заявленном scope.

### Роль внешних исследований

Литература о physical p-bit/stochastic hardware — только candidate-realization reference. Она показывает, что materially stochastic realization class существует физически, но не является Native Kernel evidence.

## 10. Family H10 — orthogonal variation storage/computation

### Hypothesis

`A10-H10`: storage и computation mechanisms могут изменяться независимо в declared semantic constraints.

### Почему BPV1 этого не проверял

BPV1 одновременно менял language, history model и representation, поэтому не изолировал storage independence от computation independence.

### Minimum design

Qualifying family должна использовать как минимум 2×2 matrix:

```text
           Storage S1   Storage S2
Compute C1     C1/S1        C1/S2
Compute C2     C2/S1        C2/S2
```

`C1` и `C2` должны различаться computation mechanism, а не только language. `S1` и `S2` должны различаться storage model, а не лишь SQL dialect/schema layout.

### Testable question

Можно ли менять storage при materially fixed computation и computation при materially fixed storage без изменения required semantic law, identity relation, Authority rule или accountability property?

### Failure / hard refutation

Failure: thin wrappers над shared mechanism, semantic logic спрятан в storage adapter, oracle зависит от одной matrix cell, либо обе axes меняются одновременно без контроля.

Hard refutation: isolated storage/computation change неизбежно меняет required meaning-level obligation, а не только implementation mechanics или declared loss.

## 11. Family H11 — laboratory/Canon separation

### Hypothesis

`A10-H11`: laboratory mechanisms могут оставаться воспроизводимыми, не превращаясь в Architecture Canon.

### Почему BPV1 этого не проверял

H11 не был preregistered BPV1 falsification target. Текущий `BOUNDED_REFERENCE_LABORATORY` boundary — информативное repository governance evidence, но не BPV1 adjudication H11.

### Dual-layer challenge

Будущая H11 family должна сознательно поддерживать два слоя:

```text
Historical laboratory reproduction layer
  → может требовать exact Python / SQL / JSON / SHA / Event / reducer / versioned bytes
  → exactness допустима, потому что воспроизводится исторический profile

Architecture conformance layer
  → остаётся meaning-level
  → эти exact mechanisms не становятся universal requirements только из-за требований laboratory reproduction
```

### Testable question

Может ли accepted laboratory evidence точно воспроизводиться по собственному versioned profile manifest, пока Architecture и её conformance/falsification rules остаются mechanism-neutral?

### Failure / hard refutation

Failure: Architecture docs/validators требуют Python, SQL, JSON, SHA-256, Event, reducer, exact replay, UUID, current clocks или эквивалентный profile mechanism только потому, что historical lab evidence зависит от него.

Hard refutation: necessary architecture obligation невозможно сделать reproducible/testable без повышения profile-specific lab mechanism до universal Architecture **только потому**, что его требует historical evidence reproduction.

### Independence target

Минимально критична `INDEPENDENT_SEMANTIC_ORACLE`; independent reviewer/reproducer, team или custody заметно усиливают результат, поскольку same-author boundary review уязвим к circular reasoning.

## 12. Рекомендуемый порядок

Порядок намеренно не числовой H03→H11:

| Порядок | Family | Причина |
|---|---|---|
| 1 | H11 | защищает все последующие families от profile→Canon leakage; наименьшая execution burden |
| 2 | H03 | проверяет representation migration conventional-digital средствами без нового hardware claim |
| 3 | H10 | уточняет смысл independent computation model до hardware claims |
| 4 | H06 | logical lane tractable; crypto/physical lanes требуют stronger custody/observability |
| 5 | H09 | statistical protocol лучше квалифицировать до дорогого probabilistic-substrate run |
| 6 | H08 | strongest specialized hardware/anti-shadow requirement; oracle discipline должна быть зрелой |

Это recommendation для planning, а не authorization на execution.

## 13. Expected evidence для любой будущей family

Future preregistration должна задать минимум:

```text
hypothesis + scope
frozen semantic obligation inventory
independence-axis qualification
candidate realization identity
raw observables
external qualifier
frozen semantic oracle
failure / hard-refutation rules
allowed losses
threat/trust model
complete reproduction path
A10 outcome
```

Evidence должен позволять реально сломать hypothesis. Красивый demo без credible negative path — non-qualifying.

## 14. Внешние research references

Эти источники только помогают design candidate experiments. Они не являются architecture authority и не меняют A10 outcomes.

- NIST SP 800-88 Rev. 2, *Guidelines for Media Sanitization* (2025) — reference для H06 sanitization/cryptographic-erasure/validation boundaries.
- Singh et al., *Nature Communications* 15, 2685 (2024), DOI `10.1038/s41467-024-46645-6` — physical stochastic p-bit hardware как candidate realization для H09 research.
- Cotteret et al., arXiv:`2405.01305` (2024) — distributed representations in neuromorphic hardware как H08 research reference.

Citation может мотивировать test class. Citation не может создать `SUPPORTED_FOR_SCOPE` для Native Kernel.

## 15. Non-target: composition/federation

D7-F08 остаётся важным:

```text
BPV1 single-node local/scoped conformance
≠ composition/federation conformance
```

Но это не H11. Composition/federation нужен отдельный future architecture/research gate, если оператор его разрешит. Этот residual plan его не тестирует и не admission.

## 16. Non-target: quantum/non-classical computation

A10-Q16 остаётся open. Этот plan не создаёт quantum family только ради красивой roadmap completeness.

Quantum/non-classical mapping потребует собственного research question об identity, observation history и accountability при measurement/state-change semantics. Сейчас он остаётся `NOT_TESTED` и вне этого plan.

## 17. Completion criteria planning gate

`RESIDUAL_A10_VALIDATION_PLAN` complete только если reviewer может подтвердить:

1. представлены ровно шесть D6 `NOT_TESTED` hypotheses;
2. H11 не перепутан с federation;
3. у каждой hypothesis своя bounded falsification family;
4. каждая family описывает semantic obligations, question, independence, realization class, observables, equivalence predicate, allowed loss, failure, hard refutation, grounding, trust model, oracle, reproduction и expected evidence;
5. H06 разделяет logical, cryptographic и physical claims;
6. H08 не получает substrate support из simulation/emulation;
7. H09 не получает substrate support из stochastic software rehearsal;
8. H10 не считает language change computation-model change;
9. H11 сохраняет exact lab reproduction без universalization lab machinery;
10. ни одна family не разрешает implementation/execution;
11. runtime остаётся frozen;
12. Final Canon и production остаются unauthorized.

## 18. Следующий gate после plan

Если этот plan станет authoritative через merge и post-merge validation, следующий bounded gate:

```text
SEPARATE_FAMILY_PREREGISTRATION_SELECTION
```

Он тоже **не** разрешает residual experiment execution.

Selected family потребует отдельный preregistration PR, а затем отдельное execution-admission решение. Пока эти gates не созданы и явно не разрешили execution:

```text
residual experiment implementation: NOT AUTHORIZED
residual experiment execution:      NOT AUTHORIZED
product runtime integration:         NOT AUTHORIZED
runtime expansion:                   FROZEN
Final Canon:                         DEFERRED
production:                          false
```

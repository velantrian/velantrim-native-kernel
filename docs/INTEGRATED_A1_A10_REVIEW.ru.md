# Integrated A1–A10 Blueprint Review

**State:** `COMPLETED / PROVISIONAL / OPERATOR_DECISION_PENDING`  
**Review identity:** `nk-integrated-blueprint-review/A1-A10-review-1`  
**Architecture phase:** ADR-0025 / Issue #88  
**Reviewed inventory:** first-draft blueprint A1–A10  
**Next gate:** `OPERATOR_POST_BLUEPRINT_DECISION`  
**Runtime expansion:** `FROZEN`

## 1. Назначение и граница Authority

Этот review оценивает A1–A10 как одну архитектуру, а не как десять изолированных документов. Проверяются terminology, dependency direction, semantic non-equivalences, contradictions, duplicate concepts, implementation capture, laboratory mapping, falsifiability и граница между architecture research и operator authority.

Это repository-integrated review pass. Он **не является independent validation**: те же project/operator lineage подготовили drafts и это reconciliation. Он также не является operator acceptance, Canon promotion, runtime authorization, production authorization или proof arbitrary-substrate portability.

First-draft A1–A10 сохраняются как historical drafted slices. Если review выявляет конфликт, explicit reconciliation decisions в §4 являются current provisional interpretation integrated blueprint. Так history не переписывается silently.

## 2. Assessment dependency chain

Intended chain coherent:

```text
A1 purpose / non-goals
→ A2 meaning-level ontology
→ A3 obligation-and-transition machine
→ A4 semantic laws / non-collapse invariants
→ A5 identity / time / change
→ A6 lifecycle positions / accountable transitions
→ A7 conflict / uncertainty / revision
→ A8 substrate mapping / conformance
→ A9 reference-laboratory classification
→ A10 open hypotheses / falsification
→ this integrated review
```

Ни один reviewed later slice не требует Python, PostgreSQL, SQLite, SQL, JSON, SHA-256, Event sourcing, reducer replay, global integer sequence, LLM, embeddings или один processor model как universal Canon. Current P1–C5 mechanisms остаются bounded laboratory realizations и evidence instruments.

## 3. Cross-slice consistency results

### 3.1 Representation и epistemic boundaries — coherent

Technology-neutral purpose A1, Observation/Claim/Evidence/Source distinctions A2, A4-L01…L10, uncertainty rules A7 и mapping states A8 согласованно запрещают collapse representation-as-reality и unknown-as-false.

### 3.2 Identity, time и ordering — coherent

A4-L11…L19, typed identity relations/temporal dimensions A5, lifecycle order A6 и portability rules A8 согласованно сохраняют:

```text
semantic identity ≠ storage identity
write order ≠ occurrence order ≠ causal order
Revision ≠ overwrite
Supersession ≠ deletion or falsity
```

### 3.3 Conflict, uncertainty и revision — coherent после terminology reconciliation

A2/A4/A7/A8/A10 согласованно сохраняют unresolved plurality, scoped Authority, detection ≠ resolution и uncertainty ≠ one universal confidence scalar. IR-F03 и IR-F04 снимают wording/protocol ambiguity на integrated layer.

### 3.4 Substrate independence — coherent, но не proved

A1/A3/A8/A9/A10 согласованно определяют substrate independence как specification/conformance discipline, а не claim, что каждый substrate способен реализовать Kernel. PostgreSQL↔SQLite C3 остаётся narrow same-language storage-profile evidence.

### 3.5 Laboratory boundary — coherent

A9 правильно предотвращает implementation capture, сохраняя reproducibility и evidence lineage. Ни один laboratory mechanism не становится universal Canon только потому, что существует или проходит CI.

## 4. Integrated findings и explicit reconciliation decisions

### `IR-F01` — Physical deletion и cryptographic erasure были объединены в A6

**Severity:** material semantic inconsistency.  
**Source:** A5 явно говорит `physical deletion ≠ cryptographic erasure`; A6 first draft объединяет их как `PHYSICALLY_OR_CRYPTOGRAPHICALLY_ERASED`.

**Integrated correction:** current provisional blueprint использует **четыре** closure meanings:

```text
LOGICALLY_ERASED
PHYSICALLY_ERASED
CRYPTOGRAPHICALLY_ERASED
FORGOTTEN_OR_LOST
```

- `LOGICALLY_ERASED` — ordinary semantic/operational availability withdrawn в declared scope; physical residue может существовать.
- `PHYSICALLY_ERASED` — relevant physical carrier/state уничтожен, перезаписан или изменён beyond declared recovery boundary через named physical method и observation scope. Если residue невозможно достаточно проверить, stronger claim остаётся `INDETERMINATE`.
- `CRYPTOGRAPHICALLY_ERASED` — required cryptographic secret/key material уничтожен через named method и declared cryptographic assumptions, поэтому protected content computationally inaccessible для stated threat/scope. Это **не** утверждает удаление physical ciphertext/residue.
- `FORGOTTEN_OR_LOST` — material не reconstructible из declared accessible-source boundary, без implication deliberate erasure, universal loss или non-existence.

Original combined A6 token сохраняется только как historical first-draft wording и не должен использоваться как current integrated closure taxonomy.

### `IR-F02` — A6 требовал named erasure method для любого closure kind

**Severity:** internal contradiction.  
**Source:** A6 допускает `FORGOTTEN_OR_LOST` без recorded deliberate erasure method, но позже говорит, что closure kind без named method invalid.

**Integrated correction:** любой closure claim требует named **basis/assessment/observation method и scope**. Только deliberate `PHYSICALLY_ERASED` и `CRYPTOGRAPHICALLY_ERASED` claims дополнительно требуют named erasure method. `FORGOTTEN_OR_LOST` может быть accidental/unexplained loss и не требует deliberate erasure method.

### `IR-F03` — A1 foundational question использовал “confidence attached” слишком широко

**Severity:** terminology drift, non-blocking после reconciliation.  
**Source:** A1 спрашивает про “confidence attached” к Claim, тогда как A7 устанавливает `uncertainty ≠ one universal confidence scalar` и model confidence ≠ Evidence.

**Integrated correction:** A1 research question следует читать как вопрос об **uncertainty and epistemic position associated with the Claim**, а не о mandatory confidence scalar/field. Profile-specific confidence value — только один возможный input/representation и не получает automatic epistemic Authority.

### `IR-F04` — A10 hypothesis table использовал labels вне собственного five-outcome protocol

**Severity:** protocol vocabulary inconsistency.  
**Source:** A10 задаёт ровно `SUPPORTED_FOR_SCOPE / WEAKENED / REFUTED / INDETERMINATE / NOT_TESTED`, но first-draft table также использует `PARTIALLY_SUPPORTED` и `OPEN / INDETERMINATE`.

**Integrated correction:** machine/review outcome vocabulary A10 содержит ровно пять declared outcomes. Contextual evidence notes не создают новые states.

Normalized current interpretations:

- `A10-H03`: `NOT_TESTED` across independent representation/substrate migrations; current same-lineage mappings — contextual prior evidence only.
- `A10-H06`: `INDETERMINATE`; problem remains open.
- `A10-H10`: `NOT_TESTED` для independently varying storage/computation axes; P5 даёт storage-only contextual evidence.
- `A10-H11`: `SUPPORTED_FOR_SCOPE` только для governance discipline, что reproducible laboratory mechanisms могут оставаться non-Canon; это не substrate evidence.

### `IR-F05` — Erasure observability требует explicit physical/cryptographic separation

**Severity:** clarification needed for A8/A10 consistency.

**Integrated correction:** physical и cryptographic erasure — разные claims с разными observables. Lack of physical-residue visibility оставляет physical-erasure claim `INDETERMINATE`; cryptographic erasure требует evidence key/secret destruction + stated cryptographic assumptions/threat boundary и никогда не implies physical deletion.

### `IR-F06` — “Conflict visibility” не должен означать, что любой tension является Contradiction

**Severity:** terminology clarification.

**Integrated correction:** durable-quality statement A1 про contradiction интерпретируется шире как **material tension/conflict visibility**, где `Contradiction` — только один A7 tension kind после alignment. Conflict может остаться unresolved, dissolve после scope/time alignment или быть handled-for-scope без превращения одной стороны в false.

### `IR-F07` — Lifecycle wording должен оставаться non-linear и non-mandatory

**Severity:** wording clarification.

**Integrated correction:** A6 phases — recurring positions, которые item **может занимать**, включая concurrent positions under different identity relations. Это не mandatory stages, через которые каждый item обязан пройти; нет требования eventual progression или closure.

## 5. Assessment duplicate concepts

Review обнаружил deliberate overlap, но не обнаружил remaining known duplicate, требующий второй competing ontology:

- A2 defines concepts; A4 constrains silent collapse этих concepts.
- A3 defines transition families; A6 defines lifecycle positions/relations over them.
- A5 defines identity/time/change; A7 uses those relations for conflict/revision.
- A8 defines preservation/conformance; A9 classifies current mechanisms against it.
- A10 defines falsification/open questions; он не заменяет P4 assertion states или A8 conformance states.

Поэтому integrated review не объединяет эти layers в один document или universal state machine.

## 6. Implementation-capture audit

Следующие mechanisms остаются profile/laboratory mechanisms, а не architecture requirements:

- Python classes/runtime;
- PostgreSQL/SQLite/SQL;
- current Event verbs/envelope;
- reducer v1 и replay shape;
- SHA-256 и current ID/hash prefixes;
- global/stream integer sequences;
- current Receipt encoding;
- GitHub Actions и evidence ZIP packaging.

Architecture-level obligations — preserved meaning, identity/lineage, scope/provenance/Authority, explicit uncertainty/loss, accountable change и scoped conformance behavior across A1–A10.

## 7. Assessment falsification coverage

A10 даёт минимум один weakening/refutation condition для каждой major hypothesis и explicit stop conditions. Важные unresolved hypotheses действительно остаются unresolved:

- independent computation-model preservation;
- non-event-sourced minimum history/accountability;
- lossy/bounded-memory accountability;
- analog/neuromorphic persistence и lineage;
- probabilistic conformance;
- independent-language/team/custody evidence thresholds;
- physical/cryptographic erasure observability;
- decentralized Authority;
- non-classical/quantum mapping;
- self-modifying realization continuity.

Absence of evidence нигде не promoted to support.

## 8. Current contracts и reference laboratory

Accepted/versioned contracts и P1–C5 evidence остаются historically valid в declared scope. Review не переписывает их retroactively. Если accepted contract смешивает architecture-level meaning и profile mechanism, later work может явно split/map layers только через separate decision без relabelling historical evidence.

Issue #14/#15/#16/#17 сохраняют existing scopes. Issue #18 и Issue #74/ADR-0024 остаются operator-controlled. ADR-0003 остаётся proposed/not started. Track H source admission остаётся operator-controlled.

## 9. Review conclusion

После explicit reconciliation decisions §4:

- **в этом review pass не осталось известных blocking internal semantic contradictions across A1–A10**;
- terminology/dependency direction достаточно coherent для представления blueprint оператору;
- unresolved research остаётся explicit, а не “закрывается” документацией;
- reference laboratory остаётся bounded и не захватывает Canon;
- substrate independence остаётся falsifiable architecture hypothesis, а не universal portability proof.

Conclusion provisional и не является independent validation. Future independent reviewer может weaken, reject, split или reopen любое finding/draft assumption.

## 10. Next gate и hard stop

```text
A1–A10 drafting: COMPLETE / PROVISIONAL
integrated A1–A10 review: COMPLETE / PROVISIONAL
independent architectural validation: NOT ESTABLISHED
next gate: OPERATOR_POST_BLUEPRINT_DECISION
runtime expansion: FROZEN
reference laboratory: BOUNDED_REFERENCE_LABORATORY
production authorization: false
```

Operator должен отдельно решить, что следует дальше. Этот review не выбирает next phase и не authorizes runtime thaw, contract promotion, new implementation profiles, licensing, reducer-v2 или production work.

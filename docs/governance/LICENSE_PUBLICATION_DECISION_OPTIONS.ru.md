# ⚖️ Варианты решения по лицензии и публикации

**[English](./LICENSE_PUBLICATION_DECISION_OPTIONS.md) · [Русский](./LICENSE_PUBLICATION_DECISION_OPTIONS.ru.md)**

```yaml
document_role: OPERATOR_DECISION_PACKAGE
issue: 18
status_as_of: 2026-08-09
decision_state: PENDING_OPERATOR
selected_option: null
runtime_effect: NO_LICENSE_OR_PUBLICATION_POLICY_CHANGE
legal_status: NOT LEGAL ADVICE
```

> Этот пакет подготавливает решение. Он не выбирает лицензию, не предоставляет права, не принимает внешние contributions и не разрешает публикацию packages.

## 1. Текущая граница

Репозиторий публичный, но в нём нет явно утверждённой software license. Согласно опубликованному руководству GitHub, по умолчанию действует copyright; пользователи могут просматривать и fork публичный репозиторий в рамках GitHub Terms of Service, однако отсутствие лицензии обычно не предоставляет права использовать, изменять или распространять работу за пределами этой платформенной границы.

До operator decision действует консервативная граница:

```text
PUBLIC RESEARCH REPOSITORY
NO EXPLICIT SOFTWARE LICENSE
ALL RIGHTS RESERVED BY DEFAULT
NO IMPLIED RIGHT TO COPY, MODIFY OR REDISTRIBUTE
EXTERNAL CONTRIBUTIONS NOT ACCEPTED
PACKAGE PUBLICATION NOT AUTHORIZED
```

Это governance boundary, а не юридическая консультация.

## 2. Решения, которые нельзя смешивать

Одного файла `LICENSE` недостаточно, пока оператор отдельно не определит:

| Поверхность | Необходимое решение |
|---|---|
| Source code | software license или restrictive terms |
| Documentation | та же лицензия, Creative Commons или отдельные условия |
| Diagrams и media | reuse, attribution и modification terms |
| Fixtures и datasets | provenance, redistribution и privacy terms |
| Contributions | закрытая, invitation-only или публичная модель |
| Contributor rights | DCO, CLA или отсутствие внешних contributions |
| Patents | explicit grant, defensive termination или отсутствие express grant |
| Trademarks и имя проекта | использование `Velantrim` и branding |
| AI-assisted contributions | disclosure, provenance и rights requirements |
| Recovered historical source | отдельная проверка provenance и relicensing |
| Packages и releases | разрешение PyPI, crates.io, containers или binaries |

## 3. Матрица вариантов

### Вариант A — Apache License 2.0

**Класс:** OSI-approved permissive open-source license.

**Свойства:**

- широкие права на использование, воспроизведение, изменение и распространение;
- express patent license от contributors;
- прекращение patent license при определённом patent litigation;
- сохранение notices и текста лицензии;
- разрешено коммерческое и closed-source использование при соблюдении условий.

**Преимущества для Native Kernel:**

- сильный вариант для interoperability/reference architecture;
- явные patent terms полезны для широко реализуемых contracts;
- низкий барьер для компаний, лабораторий и независимых implementations.

**Компромиссы:**

- forks и коммерческие derivatives могут оставаться закрытыми;
- улучшения не обязаны возвращаться в проект;
- provenance и patent authority contributors всё равно требуют governance.

**Подходит, если:** широкое распространение, стандартизация и независимые реализации важнее reciprocity.

### Вариант B — MIT License

**Класс:** OSI-approved permissive open-source license.

**Свойства:**

- короткий и широко известный текст;
- широкое разрешение использовать, копировать, изменять, публиковать, распространять, sublicense и продавать;
- требуется сохранять copyright и license notice;
- текст лицензии не содержит express patent-grant clause.

**Преимущества:**

- минимальная сложность;
- удобен для research prototypes и широкого reuse;
- хорошо понятен разработчикам.

**Компромиссы:**

- меньше явной patent clarity, чем у Apache-2.0;
- разрешены proprietary forks и closed derivatives;
- contributor и trademark policies необходимо определять отдельно.

**Подходит, если:** главные цели — простота и максимальная permissiveness.

### Вариант C — Mozilla Public License 2.0

**Класс:** OSI-approved file-level copyleft open-source license.

**Свойства:**

- изменённые MPL-covered files при распространении executable должны оставаться доступными по MPL;
- larger work может сочетать MPL files с файлами под другими terms;
- присутствуют express patent grant и patent-defense provisions;
- reciprocity ограничена covered files, а не всей системой.

**Преимущества:**

- улучшения core files вероятнее останутся доступными;
- допускает коммерческую интеграцию без whole-program copyleft;
- может защищать reference implementation и не блокировать ecosystem adapters.

**Компромиссы:**

- compliance сложнее, чем у MIT или Apache-2.0;
- file boundaries получают юридическое значение;
- некоторые организации предпочитают permissive licenses для foundation/standards проектов.

**Подходит, если:** требуется ограниченная reciprocity для core implementation files.

### Вариант D — Business Source License 1.1 с будущим переходом на open-source Change License

**Класс:** source-available до Change Date; не является OSI open source в период ограничений.

**Свойства:**

- source остаётся доступным для чтения;
- стандартная структура BSL разрешает non-production use;
- Additional Use Grant может разрешать ограниченное production use;
- версия переходит на указанную open-source Change License к Change Date в пределах максимального периода BSL;
- production use вне grant может требовать commercial license.

**Преимущества:**

- сохраняет публичную проверяемость и research access;
- может защищать период коммерческого внедрения;
- обеспечивает будущий переход на open-source license при корректной настройке.

**Компромиссы:**

- до перехода это не open source;
- необходимо точно определить production, Additional Use Grant, Change Date и Change License;
- требуется licensing administration и enforcement;
- может снизить adoption и участие сообщества.

**Подходит, если:** нужен commercial protection window при публичном source и заранее определённом open-source переходе.

### Вариант E — Research-only или custom source-available terms

**Класс:** restrictive source-available или all-rights-reserved публикация; не open source, если ограничиваются области применения, commercial use или категории пользователей.

**Возможные разрешения:**

- inspection и evaluation;
- non-commercial research;
- internal experimentation;
- запрет production use, redistribution или публикации derivatives без разрешения.

**Преимущества:**

- максимальный контроль, пока architecture и provenance не стабилизированы;
- подходит для invitation-only research stage;
- позволяет отложить необратимые широкие grants.

**Компромиссы:**

- custom drafting создаёт ambiguity и требует legal review;
- слабее ecosystem adoption и incentives для contributors;
- не соответствует обычным ожиданиям open-source collaboration;
- нельзя называть open source при field-of-use restrictions.

**Подходит, если:** контроль и staged research access важнее открытого collaboration.

### Вариант F — All rights reserved / без внешних contributions

**Класс:** отсутствует публичная reuse license.

**Свойства:**

- репозиторий остаётся читаемым как public research artifact;
- нет общего разрешения копировать, изменять, распространять или публиковать packages;
- внешние contributions не принимаются;
- отдельные разрешения могут выдаваться индивидуально.

**Преимущества:**

- минимальный текущий риск relicensing и provenance;
- сохраняет все будущие варианты лицензирования;
- подходит, пока ownership исторических материалов или commercialization strategy не ясны.

**Компромиссы:**

- блокирует обычное open-source collaboration и независимый reuse;
- публичные forks не становятся свободно используемыми implementations;
- снижает adoption, independent review и conformance work.

**Подходит, если:** проект пока не готов предоставлять reusable rights.

### Вариант G — Dual licensing

**Класс:** один и тот же контролируемый оператором код предлагается по двум маршрутам, например open source + commercial license или source-available + commercial exception.

**Преимущества:**

- может сочетать ecosystem access и коммерческие условия;
- позволяет выдавать договорные deployment rights;
- может поддерживать sustainability model.

**Компромиссы:**

- проект должен контролировать достаточные copyright права на contributed code;
- обычно нужен CLA, copyright assignment или строго контролируемая contribution policy;
- значительно возрастает governance, legal и operational complexity.

**Подходит, если:** планируется реальная commercial licensing operation и contributor-rights process.

## 4. Критерии решения

Оценить каждый критерий от `0` до `5`:

| Критерий | Вопрос |
|---|---|
| Adoption | Должны ли независимые implementations использоваться без переговоров? |
| Reciprocity | Обязаны ли распространяемые изменения core files оставаться открытыми? |
| Patent clarity | Нужен ли express contributor patent grant? |
| Commercial protection | Должны ли competing production services получать разрешение или платить? |
| Standards role | Должна ли architecture легко реализовываться разными организациями и substrates? |
| Contribution model | Нужны ли публичные contributions сейчас? |
| Relicensing control | Нужно ли сохранить возможность позднее менять terms? |
| Enforcement capacity | Может ли проект управлять exceptions, CLA или commercial licenses? |
| Historical provenance | Ясно ли ownership и право лицензирования всех материалов? |
| Funding strategy | Ожидается ли revenue из licensing, services, certification или deployment? |

## 5. Техническая governance-оценка

Это не operator decision:

```text
Если главная цель — широкое принятие нейтральной архитектуры:
  основной permissive candidate — Apache-2.0 из-за express patent terms.

Если важнее минимальный текст и friction:
  наиболее простой candidate — MIT.

Если нужна reciprocity на уровне core files:
  bounded copyleft candidate — MPL-2.0.

Если требуется commercial protection window:
  candidate — BSL 1.1 или юридически проверенная dual/source-available модель.

Если rights, provenance или strategy ещё не определены:
  временно сохранить текущую all-rights-reserved границу.
```

Custom license нежелательна без квалифицированного legal review. Standard licenses снижают interpretation и compatibility risk.

## 6. Варианты contribution policy

License decision нужно соединить с одним из режимов:

1. **No external contributions** — только issues и design feedback.
2. **DCO** — contributor подтверждает право отправить contribution под лицензией проекта.
3. **CLA** — contributor предоставляет более широкие права, возможно включая relicensing и patent terms.
4. **Invitation-only contributions** — выбранные contributors подписывают отдельное agreement.

Permissive license без contribution policy не решает provenance и future relicensing.

## 7. Обязательные operator selections

```yaml
code_terms: UNSELECTED
documentation_terms: UNSELECTED
diagram_media_terms: UNSELECTED
fixture_dataset_terms: UNSELECTED
contribution_mode: UNSELECTED
dco_or_cla: UNSELECTED
patent_policy: UNSELECTED
trademark_policy: UNSELECTED
ai_contribution_policy: UNSELECTED
historical_source_policy: UNSELECTED
package_publication: UNSELECTED
```

## 8. Acceptance gates

Перед финальным решением:

- проверить ownership и provenance всего содержимого;
- проверить compatibility dependency licenses;
- решить, исключается ли recovered historical source до отдельного review;
- отдельно выбрать terms для code, documentation и data;
- определить contribution и patent policy;
- получить legal review при commercial restrictions, dual licensing или custom terms;
- создать explicit ADR/operator decision;
- добавить выбранные license files и notices отдельным PR;
- обновить Issue #18, README, CONTRIBUTING, package metadata и Notion;
- выполнить exact-head и post-merge checks.

## 9. Что доказывает пакет

Только наличие структурированных вариантов и сохранение состояния `PENDING_OPERATOR`.

## 10. Чего пакет не доказывает

Он не предоставляет лицензию, не является legal advice, не устанавливает ownership, не принимает contributions, не разрешает package publication и не выбирает commercial model.

## Официальные источники

- GitHub Docs — Licensing a repository: <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository>
- Choose a License — No License: <https://choosealicense.com/no-permission/>
- Open Source Initiative — MIT License: <https://opensource.org/license/mit>
- Apache Software Foundation — Apache License 2.0: <https://www.apache.org/licenses/LICENSE-2.0>
- Mozilla — MPL 2.0 FAQ: <https://www.mozilla.org/en-US/MPL/2.0/FAQ/>
- MariaDB — BSL adoption FAQ: <https://mariadb.com/bsl-faq-adopting/>
- Open Source Initiative — Open Source Definition: <https://opensource.org/definition-annotated>

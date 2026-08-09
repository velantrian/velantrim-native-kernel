# ⚖️ License and Publication Decision Options

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

> This package prepares a decision. It does not select a license, grant permissions, accept contributions or authorize package publication.

## 1. Current boundary

The repository is public but has no explicit approved software license. Under GitHub's published guidance, copyright law applies by default; users may view and fork a public repository under GitHub's Terms of Service, but an absent license does not generally grant permission to use, modify or redistribute the work outside that platform boundary.

Until an operator decision is recorded, the conservative repository boundary remains:

```text
PUBLIC RESEARCH REPOSITORY
NO EXPLICIT SOFTWARE LICENSE
ALL RIGHTS RESERVED BY DEFAULT
NO IMPLIED RIGHT TO COPY, MODIFY OR REDISTRIBUTE
EXTERNAL CONTRIBUTIONS NOT ACCEPTED
PACKAGE PUBLICATION NOT AUTHORIZED
```

This wording is a governance boundary, not a substitute for legal advice.

## 2. Decisions that must be separated

A single `LICENSE` file is not sufficient unless the operator also decides:

| Surface | Required decision |
|---|---|
| Source code | software license or restrictive terms |
| Documentation | same license, Creative Commons license or separate terms |
| Diagrams and media | reuse, attribution and modification terms |
| Fixtures and datasets | provenance, redistribution and privacy terms |
| Contributions | closed, invitation-only or public contribution policy |
| Contributor rights | DCO, CLA or no external contributions |
| Patents | explicit grant, defensive termination or no express grant |
| Trademarks and project name | use of `Velantrim` and project branding |
| AI-assisted contributions | disclosure, provenance and rights requirements |
| Recovered historical source | separate provenance and relicensing review |
| Packages and releases | whether PyPI, crates.io, containers or binaries may be published |

## 3. Option matrix

### Option A — Apache License 2.0

**Class:** OSI-approved permissive open-source license.

**Characteristics:**

- broad rights to use, reproduce, modify and distribute;
- express patent license from contributors;
- patent-litigation termination provision;
- preservation of notices and license terms;
- compatible with commercial and closed-source use, subject to the license.

**Advantages for Native Kernel:**

- strong fit for an interoperability/reference-architecture project;
- explicit patent language is useful if contracts or implementations become broadly adopted;
- easy for companies, laboratories and independent implementers to consume.

**Trade-offs:**

- forks and commercial derivatives may remain proprietary;
- it does not require improvements to return to the project;
- contributor provenance and patent authority still need governance.

**Best fit when:** maximum adoption, standardization and independent implementation matter more than reciprocity.

### Option B — MIT License

**Class:** OSI-approved permissive open-source license.

**Characteristics:**

- short and widely understood;
- broad permission to use, copy, modify, merge, publish, distribute, sublicense and sell;
- requires preservation of copyright and license notice;
- the license text contains no express patent-grant clause.

**Advantages:**

- minimal friction;
- simple for small projects, research prototypes and broad reuse;
- highly familiar to developers.

**Trade-offs:**

- weaker explicit patent clarity than Apache-2.0;
- proprietary forks and closed derivatives are allowed;
- minimal text places more burden on separate contributor and trademark policies.

**Best fit when:** simplicity and maximum permissiveness are the primary goals.

### Option C — Mozilla Public License 2.0

**Class:** OSI-approved file-level copyleft open-source license.

**Characteristics:**

- modifications to MPL-covered files distributed in executable form must remain available under MPL terms;
- larger works may combine MPL files with files under other terms;
- includes an express patent grant and patent-defense provisions;
- keeps reciprocity focused on covered files rather than the entire combined system.

**Advantages:**

- improvements to core files are more likely to remain available;
- supports commercial integration without imposing whole-program copyleft;
- can protect the reference implementation while permitting ecosystem adapters.

**Trade-offs:**

- more compliance work than MIT or Apache-2.0;
- file boundaries become legally meaningful;
- some organizations prefer permissive licenses for foundational standards.

**Best fit when:** the operator wants bounded reciprocity for core implementation files.

### Option D — Business Source License 1.1 with a later open-source Change License

**Class:** source-available before the Change Date; not OSI open source during the restricted period.

**Characteristics:**

- source remains visible;
- non-production use is permitted by the standard BSL structure;
- an Additional Use Grant may permit bounded production use;
- restricted versions convert to a stated open-source Change License by the Change Date, no later than the BSL maximum period;
- commercial production use outside the grant can require a separate commercial license.

**Advantages:**

- preserves public inspectability and research access;
- can protect a commercial deployment window;
- guarantees a later transition to an open-source license when configured correctly.

**Trade-offs:**

- not open source before conversion;
- requires precise definitions of production, Additional Use Grant, Change Date and Change License;
- creates operational licensing questions and commercial-enforcement burden;
- may reduce community and standards adoption.

**Best fit when:** commercial protection is required while retaining public source and a defined future open-source transition.

### Option E — Research-only or custom source-available terms

**Class:** restrictive source-available or all-rights-reserved publication; not open source when use fields, commercial activity or persons are restricted.

**Possible permissions:**

- inspection and evaluation;
- non-commercial research;
- internal experimentation;
- no production use, redistribution or derivative publication without permission.

**Advantages:**

- maximum control while architecture and provenance remain unsettled;
- compatible with an invitation-only research stage;
- can postpone irreversible broad grants.

**Trade-offs:**

- custom drafting creates ambiguity and legal-review cost;
- weak ecosystem adoption and contribution incentives;
- incompatible with the normal expectations of open-source collaboration;
- field-of-use restrictions mean the license must not be called open source.

**Best fit when:** control and staged research access are more important than open collaboration.

### Option F — All rights reserved / no external contributions

**Class:** no public reuse license.

**Characteristics:**

- repository remains readable as a public research artifact;
- no general permission to copy, modify, redistribute or publish packages;
- no external contribution intake;
- individual permissions may be granted separately.

**Advantages:**

- lowest immediate relicensing and provenance risk;
- preserves all future licensing options;
- appropriate while historical-source ownership or commercialization strategy is unresolved.

**Trade-offs:**

- prevents normal open-source collaboration and independent reuse;
- public forks do not become usable implementations outside the platform permission boundary;
- reduces adoption, review and independent conformance work.

**Best fit when:** the project is not yet ready to grant reusable rights.

### Option G — Dual licensing

**Class:** the same operator-owned code is offered under two compatible routes, commonly open source plus a commercial license, or source-available plus a commercial exception.

**Advantages:**

- can combine ecosystem access with commercial terms;
- permits negotiated deployment rights;
- can support a later sustainability model.

**Trade-offs:**

- requires the project to control sufficient copyright in contributed code;
- usually requires a CLA, copyright assignment or tightly controlled contribution policy;
- substantially increases governance, legal and operational complexity.

**Best fit when:** a credible commercial licensing operation and contributor-rights process are planned.

## 4. Decision criteria

Score each criterion from `0` to `5` before choosing:

| Criterion | Question |
|---|---|
| Adoption | Should independent implementations be usable without negotiation? |
| Reciprocity | Must distributed modifications to core files remain open? |
| Patent clarity | Is an express contributor patent grant important? |
| Commercial protection | Must competing production services require permission or payment? |
| Standards role | Should the architecture be easy to implement across organizations and substrates? |
| Contribution model | Are public contributions desired now? |
| Relicensing control | Must the operator preserve the ability to change terms later? |
| Enforcement capacity | Can the project administer exceptions, CLAs or commercial licenses? |
| Historical provenance | Is every included source artifact clearly owned and licensable? |
| Funding strategy | Is revenue expected from code licensing, services, certification or deployment? |

## 5. Technical governance assessment

This is not an operator decision:

```text
If the primary goal is broad neutral-architecture adoption:
  Apache-2.0 is the strongest permissive candidate because of its express patent terms.

If minimal text and friction dominate:
  MIT is the simplest candidate.

If core-file reciprocity is required:
  MPL-2.0 is the bounded copyleft candidate.

If a commercial protection window is required:
  BSL 1.1 or a carefully reviewed dual/source-available model is the candidate.

If rights, provenance or strategy remain unresolved:
  keep the current all-rights-reserved boundary temporarily.
```

Avoid a custom license unless qualified legal review is available. Standard licenses reduce interpretation and compatibility risk.

## 6. Contribution policy choices

The license decision must be paired with one of:

1. **No external contributions** — issues and design feedback only.
2. **DCO** — contributors certify the right to submit under the project license.
3. **CLA** — contributors grant broader rights, potentially including relicensing and patent terms.
4. **Invitation-only contributions** — selected contributors sign an explicit agreement.

A permissive license without a contribution policy does not solve provenance or future relicensing.

## 7. Required operator selections

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

Before recording a final decision:

- verify ownership and provenance of all repository content;
- review dependency-license compatibility;
- decide whether historical recovered source would be excluded pending review;
- select code, documentation and data terms separately;
- define contribution and patent policy;
- obtain legal review if commercial restrictions, dual licensing or custom terms are chosen;
- create an explicit ADR/operator decision;
- add the selected license files and notices in a separate PR;
- update Issue #18, README, CONTRIBUTING, package metadata and Notion;
- run exact-head and post-merge integrity checks.

## 9. What this package proves

It proves only that the repository contains a structured set of decision options and preserves `PENDING_OPERATOR` state.

## 10. What this package does not prove

It does not grant a license, provide legal advice, establish ownership, accept contributions, permit package publication or choose a commercial model.

## Official references

- GitHub Docs — Licensing a repository: <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository>
- Choose a License — No License: <https://choosealicense.com/no-permission/>
- Open Source Initiative — MIT License: <https://opensource.org/license/mit>
- Apache Software Foundation — Apache License 2.0: <https://www.apache.org/licenses/LICENSE-2.0>
- Mozilla — MPL 2.0 FAQ: <https://www.mozilla.org/en-US/MPL/2.0/FAQ/>
- MariaDB — BSL adoption FAQ: <https://mariadb.com/bsl-faq-adopting/>
- Open Source Initiative — Open Source Definition: <https://opensource.org/definition-annotated>

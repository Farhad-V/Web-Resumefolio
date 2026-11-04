# Resumefolio — FAU References and Design Coverage

**Purpose:** identify the teaching sources behind the design approach and map their concerns to the project's current owning documents.

Updated November 2, 2026. **Status:** source-provenance and documentation-coverage map; no technical selection, criterion closure, standards compliance or baseline acceptance is established here.

[Provenance](#1-source-provenance-and-limits) · [FAU content](#2-what-the-lectures-support) · [Coverage](#3-current-project-coverage-map) · [Adaptations](#4-project-adaptations-and-source-authority) · [Use](#5-reading-and-maintenance)

## MVP system allocation and design status

The accepted system boundary separates the Resumefolio core from ProjectForge, joined by an authenticated user-scoped API. Logical responsibilities remain useful within each system; they do not authorize a shared core/ProjectForge process, database or transaction. Core owns dashboard, invited accounts, professional presentation, protected sharing, manual applications and same-server private My Files & Media. ProjectForge MVP owns real repositories/transfers/permissions, file/history browsing, issues and simple Kanban. Its selected engine is native Git Smart HTTP behind the independent Laravel ProjectForge service, with its own MySQL 8.4 database and OS/storage boundaries on the existing host; BL-MVP-2026-11-04.1 governs implementation and evidence gates. The future communications system is independently private and API connected. Advanced Git review/releases, backlog/Sprints and execution/deployment remain deferred. Keep source, independent resume draft, explicit publication and actual submitted material identities distinct. Profile changes require preview/select/apply and cannot mutate publication or submitted history. Manual applications include status, next action and follow-up date without mail/calendar dependencies.

Authority: [OWNER-MVP-2026-11-04](../01-project-planning/owner-mvp-decision-2026-11-04.md).

## 1. Source provenance and limits

The supplied FAU Applied Software Engineering material identifies Dr. Ralf Ellner and Thomas Rau. This update inspected the saved text extracts `V07_System_Design_1.txt` and `V08_System_Design_2.txt` in the chat workspace's working material. The original user-specified D: location was unavailable during the earlier structure work; original PDFs/slide graphics were not re-inspected here.

Locators below refer to the extracts' `PDF PAGE` markers. Their content supports textual attribution; diagram-only pages may contain little extracted detail. Page markers are not independently verified against a new original-PDF render. The working extracts are outside the main repository and are not portable dependencies or required build inputs.

Extract identities inspected for this update (SHA-256):

- **V07:** `BA0A489C868564AD3F956575B7A4A26E2DB3FD9F726E2CBEE81A527E9481E0C6`
- **V08:** `E4B0B63428672EE5D5C339698480A5E5EE6E7CE76965D575C92D0184E12649D4`

Hashes identify the inspected text bytes, not an independently authenticated original publication. The textbook/framework references below are attributed through those lecture extracts; their full original publications were not reviewed by this mapping exercise.

## 2. What the lectures support

### V07 — System Design 1

| PDF page(s) | Taught concern and attribution limit |
| --- | --- |
| 13–14 | Architecture definitions referencing Shaw/Garlan (1996) and IEEE 1471 (2000); historical lecture references, not a current compliance claim |
| 19–20 | Consolidated architecture model, consistent extension of analysis and structured documentation; arc42 is named as an example |
| 21–28 | Stakeholder viewpoints and Kruchten's 4+1: logical, use-case, implementation, process and deployment views, with UML representations |
| 30–34 | Cross-cutting concerns, persistence selection rationale, abstraction, modularization/cohesion/coupling and encapsulation |
| 35–38 | Modeling approaches and degree of formality; no project-wide mandatory formal-method exercise is inferred |
| 39–49 | Component/interface and interaction/behavior concepts, artifacts, nodes, communication/deployment and layers/tiers; component definition references Szyperski (1998) |
| 50 | arc42 documentation example; the project does not reproduce its chapter tree |
| 51–55 | Architecture use during implementation, testing, change management and evolution; examples do not mandate code generation |

### V08 — System Design 2

| PDF page(s) | Taught concern and attribution limit |
| --- | --- |
| 11–15 | Refinement from architecture toward implementation/code-level structures and interfaces; record decisions, reasons and alternatives |
| 22–23 | Typically one component design model per component: computational data/classes, fine-grained dynamics, coding constraints and technical scenarios such as initialization/transactions |
| 24–35 | Pattern scope and reuse, GoF (1994)/POSA (1996) references and examples including Façade, Observer and Singleton; examples are not mandatory project patterns |
| 36–38 | Anti-patterns, Budgen (2003), design smells and model refactoring; naming a smell is not an observed product defect |
| 39–41 | Model/package structure, content conventions, overview diagrams and example coverage rules; example metrics are not automatically adopted thresholds |
| 42 | Iterative work, recalibration, prioritization and clear interfaces/separation of concerns |

Together the lectures support **analysis → architecture model → component design models → code**, with consistency across views and iterative refinement. They combine several sources and teaching choices; they do not prescribe this repository's Markdown filenames, six-topic directory tree, ADR format or evidence gates through one international standard.

## 3. Current project coverage map

The six topics organize documentation, not runtime services. Architecture Model information spans several topics; concrete Component Design Models stay with their owners in topic 03 and reference shared guidance. “Covered” below means an owning record exists and is populated, not that every source criterion is semantically closed or verified.

### Architecture concerns

| Concern | Owning project record |
| --- | --- |
| Drivers, alternatives and solution rationale | [Architecture drivers/options](01-software-architecture/01-design-drivers-and-solution-options.md) and [ADRs](07-design-decisions/README.md) |
| Logical decomposition and resource ownership | [System decomposition/boundaries](01-software-architecture/02-system-decomposition-and-boundaries.md) |
| Use-case (+1) technical collaborations | [Use-case realizations](05-interface-and-api-design/03-use-case-realizations-and-interactions.md), linked to component-owned sequences |
| Process/runtime communication and concurrency | [Runtime behavior](01-software-architecture/03-process-view-concurrency-and-runtime-behavior.md) |
| Implementation/package/artifact organization | [Implementation view/artifacts](03-component-and-module-design/02-implementation-view-and-artifacts.md) |
| Deployment nodes and communication paths | [Deployment topology](01-software-architecture/04-deployment-topology-nodes-and-networks.md) |
| Cross-cutting concern navigation | [Cross-cutting overview](01-software-architecture/05-cross-cutting-concerns-overview.md); detailed rules remain with their owners |

### Component and shared design concerns

| Concern | Owning project record |
| --- | --- |
| Modularity, dependencies and encapsulation | [Module design](03-component-and-module-design/01-modularity-dependencies-and-encapsulation.md) |
| Responsibilities, data/classes, algorithms, failures and coding constraints | [Component catalog](03-component-and-module-design/README.md) and [complete component template](03-component-and-module-design/component-template/README.md) |
| OO principles and justified patterns | [Design principles/OO approach](02-detailed-and-object-oriented-design/01-design-principles-and-object-oriented-approach.md) |
| Evolution, smells, refactoring and debt | [Evolution record](02-detailed-and-object-oriented-design/05-design-evolution-refactoring-and-technical-debt.md) |
| Logical/physical data refinement and integrity | [Data model](04-data-design/01-analysis-to-logical-and-physical-data-models.md) |
| Persistence, cache freshness and reference-aware lifecycle | [Persistence/lifecycle](04-data-design/03-persistence-caching-and-data-lifecycle.md) |
| Provided/required contracts and compatibility | [API/protocol contracts](05-interface-and-api-design/01-api-protocols-contracts-and-compatibility.md) |

### Quality, operation and review concerns

| Concern | Owning project record |
| --- | --- |
| Quality attributes, scenarios and trade-offs | [Quality evaluation](06-design-quality-and-security-analysis/01-quality-attributes-and-design-trade-offs.md) |
| Assets, trust crossings, threats and control responsibility | [Security model](06-design-quality-and-security-analysis/02-security-threat-modeling-and-trust-boundaries.md) |
| Supervision, backup, usable recovery and resilience | [Operations/recovery](06-design-quality-and-security-analysis/03-operations-backup-recovery-and-resilience.md) |
| User journeys, feedback, keyboard/responsive and accessibility design | [UI/interaction quality](06-design-quality-and-security-analysis/04-user-interface-accessibility-and-interaction-quality.md) |
| Exact traceability, testability, findings and scoped handoff | [Review/handoff](06-design-quality-and-security-analysis/05-design-review-traceability-and-handoff.md) |
| Actual sanitized evidence requirements | [Evidence guidance](06-design-quality-and-security-analysis/review-and-traceability/evidence/README.md) |

This mapping reconciles teaching concerns with the current populated documents. It is not a complete implementation-class catalog, physical schema, threat proof or test-coverage report. Use each topic's diagram catalog for editable source/export links rather than duplicate every diagram here.

## 4. Project adaptations and source authority

**Retained teaching structure:** coherent architecture viewpoints, explicit component interfaces, refinement toward code, computational data/dynamics/technical scenarios, justified patterns and iterative review.

**Project conventions:** six topical folders plus shared decision records; numbered Markdown locators; local component/quality/threat labels; ADR status/trace fields; diagram catalogs; protected-reference/durable-attempt protocols; and implementation handoff/evidence records. These organize this product's needs and are not a claimed FAU folder standard.

**Supplementary techniques:** DDD/C4, SOLID/DRY/KISS/YAGNI, HTTP/REST/GraphQL/gRPC, STRIDE, lightweight ATAM-inspired evaluation, WCAG/accessibility and resilience/cloud patterns may inform applicable records. Not all are explicitly taught in V07/V08; mentioning them neither selects a product technology nor requires implementing every technique. Exact official technical guidance is linked in the owning record where used.

**Analysis/design distinction:** requirements and analysis retain domain meanings, required outcomes, conceptual data, system scenarios and source threats/quality inputs. Design refines technical mechanisms and trade-offs. A conceptual entity is not automatically a table, aggregate, microservice or deployment node. A populated technical proposal does not accept unresolved source policy.

In particular, preserve the [accepted profile-update/publication core](../02-requirements-engineering/07-change-and-baseline/open-questions-and-decisions.md#owner-accepted-profile-update-policy) while keeping its physical realization proposed where recorded. Existing [ADR statuses](07-design-decisions/README.md), feasibility/recovery gaps and quantitative target proposals retain their own authority.

## 5. Reading and maintenance

Start with [purpose/scope/approach](00-design-purpose-scope-and-approach.md), then architecture drivers/boundaries. Refine affected components, data, contracts, runtime and quality iteratively. Use [review/handoff](06-design-quality-and-security-analysis/05-design-review-traceability-and-handoff.md) for exact criterion comparisons and actual scoped disposition; this source map supplies neither coding approval nor phase acceptance.

Keep shared rules with one owner and link their concrete component realization. Split documents only when substantive content or ownership makes it useful; stable numbering does not require filling gaps with empty files. Each identified component needs coherent design detail, not copied unused templates or a folder for every buzzword.

When lecture provenance changes, identify the newly inspected source and locators without rewriting earlier inspection claims. When project records move/change, update this map and affected topic indexes, preserve historical evidence and check local links. Document/reference checks remain separate from semantic sufficiency and product verification.

[System Design home](README.md) · [Purpose and approach](00-design-purpose-scope-and-approach.md) · [Component catalog](03-component-and-module-design/README.md) · [Design decisions](07-design-decisions/README.md)

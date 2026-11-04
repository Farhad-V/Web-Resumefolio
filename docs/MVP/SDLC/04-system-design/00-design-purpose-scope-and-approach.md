# Resumefolio — Design Purpose, Scope and Approach

**Purpose:** translate the identified requirements and analysis into an explainable technical candidate, coherent component prescriptions and a reviewable implementation handoff.

Owner and decision authority: Farhad. Updated November 2, 2026.

**Current position:** architecture, shared design topics, component records, diagrams and three proposed ADRs have been populated. Exact criterion closure, final physical/compatibility prescriptions, applicable feasibility evidence and owner baseline disposition remain pending. Documentation completion is not implementation readiness or product verification.

[Authority](#1-inputs-and-source-authority) · [Scope](#2-design-scope-and-project-boundaries) · [Organization](#3-model-organization-and-ownership) · [Approach](#4-working-approach) · [Gates](#5-independent-work-and-dependent-gates) · [Handoff](#6-completion-and-implementation-handoff)

## Current MVP boundary figure

![Accepted core and separate ProjectForge boundary](01-software-architecture/diagrams/mvp-system-boundaries.svg)

[Editable source](01-software-architecture/diagrams/mvp-system-boundaries.puml) · [PNG](01-software-architecture/diagrams/mvp-system-boundaries.png). Historical broader-product figures below retain earlier alternatives/detail; they do not define the current system boundary.

Current MVP scope and selected mechanisms: [Baseline](../../baseline/README.md). Deferred provider, advanced collaboration and workflow-execution designs are not MVP prerequisites.

## 1. Inputs and source authority

Use [accepted scope](../01-project-planning/02-scope.md), [resources/constraints](../01-project-planning/05-resources-and-constraints.md), [requirements specification](../02-requirements-engineering/03-requirements-specification/requirements-specification.md), [source decisions](../02-requirements-engineering/07-change-and-baseline/open-questions-and-decisions.md), [qualified analysis handoff](../03-system-analysis/07-review-and-design-handoff/14-feasibility-dependencies-and-design-handoff.md) and [analysis review](../03-system-analysis/07-review-and-design-handoff/11-model-consistency-traceability-and-review.md).

Requirements define required behavior and source status; analysis defines domain/scenario/rule/information meaning; design specifies how the candidate realizes it. A technical model cannot silently alter a permission, accepted capability or numerical target. Preserve exact source revisions and decisions, including the [accepted profile-update/publication core](../02-requirements-engineering/07-change-and-baseline/open-questions-and-decisions.md#owner-accepted-profile-update-policy); do not request settled approval again.

The inherited 157 provisional requirement identities and 470 criterion locators are source inventory counts, not completed design coverage. Broad references, populated files and valid links do not establish exact semantic sufficiency. Follow the [traceability/review procedure](06-design-quality-and-security-analysis/05-design-review-traceability-and-handoff.md) for identified comparisons and actual findings.

## 2. Design scope and project boundaries

The current candidate covers core identity/dashboard, presentation/private media/protected PDFs and sharing, manual applications/history/follow-up, and separate basic ProjectForge integration. Provider communication/calendar, advanced work/Sprints/Git review/releases and workflow execution/deployment are future candidate models. Allocate only the owner-defined MVP to Version 1; retain broader capability as explicitly deferred proposals.

Laravel and object-oriented development are recorded constraints. Initial ten-user scope and possible future growth are not measured concurrency or capacity. The sole owner's total capacity is 20 project hours/week, including design, delivery, operation and recovery. The dated small-server observations are feasibility inputs, not final platform selection or proof of workload fit.

AI features, automatic translation and legacy demo migration remain outside Version 1. Professional English/German content is manually maintained. Do not introduce new services, paid infrastructure, public API consumers or product policies merely to fill a design topic.

**Current direction:** distinct Resumefolio core and ProjectForge systems through user-scoped API; explicit core module ownership, publication/history identities and truthful external outcomes. Physical mechanisms remain proposed. Actual engine/frontend/Git/queue/runner/provider/backup facilities and numerical policies require evaluated choices and their proper disposition. A module is not automatically a separate deployment or security boundary.

## 3. Model organization and ownership

The six core topics organize technical concerns; shared ADRs occupy a seventh supporting folder. This is a project documentation convention, not a prescribed international standard or the system's deployment topology.

| Topic | Responsibility |
| --- | --- |
| [01 — Software Architecture](01-software-architecture/README.md) | Drivers/options, logical boundaries, runtime/concurrency, deployment and cross-cutting coordination |
| [02 — Detailed and Object-Oriented Design](02-detailed-and-object-oriented-design/README.md) | Shared design principles, justified patterns, object/dependency conventions and evolution/debt |
| [03 — Component and Module Design](03-component-and-module-design/README.md) | Modularity/artifacts and complete concrete component responsibilities, data/classes, algorithms and technical scenarios |
| [04 — Data Design](04-data-design/README.md) | Logical/physical mapping, integrity, persistence/cache protocols and reference-aware lifecycle |
| [05 — Interface and API Design](05-interface-and-api-design/README.md) | Consumer protocols/contracts, result/repetition/compatibility rules and use-case realizations |
| [06 — Design Quality and Security Analysis](06-design-quality-and-security-analysis/README.md) | Quality trade-offs, threat boundaries, operations/recovery, interaction/accessibility and review/handoff |
| [07 — Design Decisions](07-design-decisions/README.md) | Consequential alternatives, rationale, costs, evidence gates and actual ADR status |

FAU's architecture model to component design model to code progression informs the approach. Its logical, use-case, process, implementation and deployment viewpoints are distributed across these topic owners. The [reference/coverage map](01-reference-and-coverage-map.md) records lecture provenance and adaptation limits; it does not establish standards compliance.

Each concrete component keeps one coherent design record/package under topic 03, using the [component template](03-component-and-module-design/README.md). Shared topics own common rules; resource owners specify their exact realization and invariants. Requirements/analysis remain in their existing folders. Cross-cutting overviews provide navigation rather than a competing policy source.

## 4. Working approach

1. **Identify drivers and scope.** Fix the candidate/source revisions, important stakeholder concerns, actual constraints and unresolved prerequisites. Separate accepted behavior from detailed proposals.
2. **Compare material options.** Use consistent scenario/quality/resource/operating criteria; record alternatives and consequences in an ADR when the choice is consequential. Do not invent scores, measured benefits or acceptance.
3. **Develop consistent architecture views.** Align ownership, interactions, concurrency, implementation artifacts, placement and trust boundaries. Native Git/provider/storage/executor/target effects must not be mistaken for atomic local state.
4. **Refine concrete components.** Specify provided/required contracts, data identities/types, algorithms, initialization/lifetime, transaction/reference/version guards and denied/failure/uncertain/recovery paths. Add readable editable diagrams where they explain material relationships or behavior.
5. **Allocate exact criteria and verification.** Connect each claimed source obligation to an owner/operation/model, realization rationale, protected state and suitable observable check. Keep planned versus executed evidence separate.
6. **Evaluate and iterate.** Review cross-view consistency, scenario trade-offs, security/feasibility and implementation sufficiency. Resolve actual findings through their owners; preserve historical evidence and source status.
7. **Prepare scoped handoff.** Record actual disposition of the identified candidate, conditions and affected commitments; align estimates/backlog with capacity and the agreed baseline sequence.

Work iteratively across topics rather than filling every file once and declaring the design complete. Reuse owning diagrams/contracts, keep source and exports synchronized and check links/tables. These documentation checks support review but cannot prove runtime behavior, interoperability or recovery.

## 5. Independent work and dependent gates

Independent technical proposals may proceed while specific facilities/policies are unresolved. Identify the exact commitment affected rather than treating every open item as either globally blocking or irrelevant.

- **Provider access and delivery:** OAuth is not created; actual consent/capabilities, outbound delivery and compatibility need evidence. Log-only mail is not recipient delivery.
- **Git:** native engine/transport/client and ref/permission/storage behavior require actual evaluation; metadata pages are not real transfer evidence.
- **Execution/deployment:** safe containment, resource/secret/network/cleanup controls and supported workflow feasibility gate real execution. Target approval is separate; validation-only work does not satisfy agreed execution capability.
- **Recovery:** backups are not set up. Independent protected destination/key access, consistent capture and isolated usable restoration remain prerequisites at their applicable gates.
- **Quality/policies:** proposed workload/latency/availability/client/accessibility/recovery targets and detailed limits retain source status. Capacity observations cannot substitute for an agreed measurement contract or actual results.
- **Physical realization:** exact types/schema, guarded transactions/reference deletion, dispatch/fencing and operating supervision/scheduler facilities remain implementation prescriptions to finalize.

Existing setup facts are work to perform, not questions to ask repeatedly. Constraints/evidence conflicts require an explicit scope/resource/target decision through existing authority; they do not authorize new spending or silent capability removal.

## 6. Completion and implementation handoff

Use [design review/handoff](06-design-quality-and-security-analysis/05-design-review-traceability-and-handoff.md) for four scoped gates: identified traceable candidate; sufficient technical prescriptions; applicable feasibility/verification prerequisites; and actual owner disposition with delivery alignment.

The handoff package identifies exact source/design/ADR revisions, comparison coverage, component/data/interface/runtime prescriptions, verification plan and actual evidence, findings/residual risks, unresolved commitments and owner disposition. Preserve the agreed pre-implementation baseline sequence; populated prose does not supply coding authorization or a release forecast.

Record actual sanitized evidence using [evidence guidance](06-design-quality-and-security-analysis/review-and-traceability/evidence/README.md). A prior observation retains its candidate/time/scope; a mock result or rendered diagram cannot establish provider acceptance, native interoperability, containment or usable restoration. No exact-criterion closure, live action, product-test Pass, purchase or baseline acceptance is created by this purpose document.

[System Design home](README.md) · [Reference/coverage map](01-reference-and-coverage-map.md) · [Component catalog](03-component-and-module-design/README.md) · [Design decisions](07-design-decisions/README.md)

# 2. Module Breakdown

[Low-Level Design index](03-Low-Level-Design.md)

## 2.1 Module List
Core owns Identity and Access, Professional Presentation, Files and Operations, Representation and Sharing, and Applications. ProjectForge owns Git Collaboration and Work Management. Shared operational support stays local to each application.

## 2.2 Module Dependencies
Presentation uses authorized profile data and immutable artifact references. Sharing resolves a specific publication and selected files. Applications capture submitted artifacts without changing the publication. Core reaches ProjectForge through its scoped API. Keep persistence within the owning module and database.

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md"></a>

<details>
<summary>Resumefolio — Modularity Dependencies and Encapsulation</summary>

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-resumefolio--modularity-dependencies-and-encapsulation"></a>

### Resumefolio — Modularity Dependencies and Encapsulation

**Proposed rule:** each logical module owns its domain state and invariant-enforcing operations. Consumers use explicit public contracts and permitted projections; infrastructure realizes technical ports without acquiring universal business authority.

**Status:** proposed implementation organization, November 2, 2026. No code package, selected dependency-checking tool, measured metric or accepted baseline is created here. Farhad retains decision authority.

[Boundaries](#design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-1-module-boundaries-and-owned-responsibilities) · [Contracts](#design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-2-public-contracts-and-internal-encapsulation) · [Dependencies](#design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-3-dependency-direction-and-coordination) · [Injection](#design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-4-dependency-injection-and-object-lifetime) · [Evaluation](#design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-5-cohesion-coupling-and-boundary-review) · [Handoff](#design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-6-implementation-handoff-and-current-limits) · [Essential views](#design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-8-essential-modularity-and-encapsulation-views)

Current MVP scope and selected mechanisms: [Baseline](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/README.md). Deferred provider, advanced collaboration and workflow-execution designs are not MVP prerequisites.

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-source-context"></a>

#### Source context

This document refines the [logical component catalog](../01-High-Level-Design/14-Appendices.md#design-record-01-software-architecture-02-system-decomposition-and-boundaries-md), [runtime protocol](../01-High-Level-Design/14-Appendices.md#design-record-01-software-architecture-03-process-view-concurrency-and-runtime-behavior-md) and [OO principles](03-Detailed-Module-Design.md#design-record-02-detailed-and-object-oriented-design-01-design-principles-and-object-oriented-approach-md). Required meanings remain in the [analysis domain model](../../03-System-Analysis/01-System-Analysis.md#analysis-domain-and-information-analysis--03-domain-model-and-object-oriented-view), [operation contracts](../../03-System-Analysis/01-System-Analysis.md#analysis-business-rules-and-operation-contracts--10-domain-constraints-and-operation-contracts) and [source decisions](../../02-Requirements-Engineering/01-Software-Requirements-Specification.md#change-and-baseline-open-questions-and-decisions).

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-1-module-boundaries-and-owned-responsibilities"></a>

#### 1. Module boundaries and owned responsibilities

[Proposed module boundary](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/03-component-and-module-design/diagrams/module-public-and-private-boundary.svg)

[Editable DOT](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/03-component-and-module-design/diagrams/module-public-and-private-boundary.dot) · ![module public and private boundary](../Diagrams/Archived-Png/Module-Public-And-Private-Boundary.png)

**Logical component:** a coherent architectural responsibility, such as Presentation or Sharing. **Code module:** the package structure that realizes that responsibility and makes exported/internal elements identifiable. **Deployment unit:** an artifact/process arrangement that can be installed or run. These concepts are related but are not interchangeable: several modules can share one release and database.

The nine candidate responsibility owners are Identity/Access, Presentation, Representation/Sharing, Applications, Communication/Calendar, Work, Git Collaboration, Workflow/Deployment Coordination and Files/Operations. Their [component records](#design-record-03-component-and-module-design-component-and-module-design-md) own concrete prescriptions. Do not copy a shared user/resume model into every module merely to simulate service boundaries.

Within a module, identify application contracts/handlers, invariant-enforcing domain policy, infrastructure mappings/adapters and permitted query projections. Use structure appropriate to actual complexity; folders named Domain or Application do not by themselves enforce encapsulation.

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-ownership-examples"></a>

##### Ownership examples

- Presentation owns draft mutation, overrides and publication identity; another module cannot update its live pointer directly.
- Sharing owns link eligibility/version and viewer authorization; PDF mode changes do not implicitly disable a link.
- Applications owns actual submission manifests; a new live revision cannot overwrite actual historical materials.
- Files owns usable-artifact admission, reservation accounting and protected-reference-aware reclamation; a consumer's logical unlink does not prove freed storage.
- Git owns native ref/review integration semantics; Work links do not extend grants, and a merge does not supply execution/deployment permission.

DDD bounded contexts can help explain vocabulary and invariant ownership. They remain candidate design boundaries, not an instruction to adopt event sourcing, a DDD framework or independent microservices.

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-2-public-contracts-and-internal-encapsulation"></a>

#### 2. Public contracts and internal encapsulation

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-what-a-module-exports"></a>

##### What a module exports

Export named application operations, validated request/value types, stable identifiers and permitted result projections that an actual consumer needs. Record current authority, expected version where relevant, input meaning, intended effect, protected state, result classifications and safe repetition/concurrency behavior.

Examples are ResolvePublication, RetrieveRepresentation, CaptureActualSubmission and MergeExpectedRefs. They describe responsibilities, not final language signatures. Public means consumable by another authorized module; it does not mean internet-accessible or exempt from policy.

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-what-remains-internal"></a>

##### What remains internal

Keep mutation-capable domain objects, ORM mappings, internal repositories, storage paths, provider credentials and transaction implementation private to their owner. A consumer cannot instantiate an internal handler to skip the public command boundary, reach into another module's database tables, or treat a file path as authorization.

Do not expose a mutable ORM entity across modules and rely on callers not to save it. Return a projection containing only permitted fields and explicit identity/version/provenance. A shared identifier establishes a reference, not access to the referenced content.

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-owner-side-enforcement"></a>

##### Owner-side enforcement

The resource owner verifies current actor/resource/action/lifecycle policy at the actual operation boundary. Gateway middleware can enforce common admission requirements, but cannot replace operation-specific checks. The same contract applies when called from a web controller, a worker, an administrative action or another module. Jobs reconstruct current context; an old session snapshot cannot grant indefinite authority.

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-3-dependency-direction-and-coordination"></a>

#### 3. Dependency direction and coordination

[Allowed dependencies and infrastructure realization](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/03-component-and-module-design/diagrams/module-dependency-direction.svg)

[Editable DOT](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/03-component-and-module-design/diagrams/module-dependency-direction.dot) · ![module dependency direction](../Diagrams/Archived-Png/Module-Dependency-Direction.png)

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-allowed-dependency-rules"></a>

##### Allowed dependency rules

1. Transport code invokes its owning module’s public use-case entry point; domain mutation and cross-module storage access do not belong in controllers.
2. A module consumes another module’s exported contract and permitted projection, never its internal persistence or mutable domain implementation.
3. Application/domain responsibilities depend on meaningful capability contracts where separation is useful. Provider/storage/Git/executor infrastructure implements those contracts.
4. Shared primitives stay small: explicit identifiers, outcome/clock abstractions and justified common technical capabilities. Business lifecycle/authority remains at the actual owner, not a universal Shared service.
5. Cross-module dependency cycles are a review finding. Resolve them through clearer ownership, a permitted projection or an explicit coordinating use case, rather than mutual internal service calls.
6. Technical credentials are not human authority. A worker's ability to reach storage or an executor does not authorize the requested product operation.

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-coordinating-multiple-owners"></a>

##### Coordinating multiple owners

Applications may store a correspondence identifier while Communication supplies an independently authorized summary. Neither imports the other's ORM entity. Work may associate a repository/revision without acquiring Git write access. Sharing asks Presentation for the intended publication and Files for an eligible usable artifact; each owner preserves its contract.

For changes spanning local owners, define the application orchestration, actual local consistency boundary and explicit pending work. A shared transaction may coordinate a justified local invariant, but must not become permission for arbitrary cross-module table writes. Remote mutations remain outside a local database rollback. See [runtime coordination](../01-High-Level-Design/14-Appendices.md#design-record-01-software-architecture-03-process-view-concurrency-and-runtime-behavior-md).

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-events-and-asynchronous-dependencies"></a>

##### Events and asynchronous dependencies

An event is a named observation with identity/provenance, not automatic permission for every consumer. A confirmed Git change can be input to workflow eligibility; it cannot itself authorize execution or deployment. A saved profile cannot trigger implicit publication. Durable consequential reactions need pending-intent/attempt handling and reconciliation rather than fire-and-forget observers.

Avoid using a generic event bus to conceal a required synchronous invariant or a dependency cycle. Each reaction needs an identified owner, source rule, current authority, result/failure contract and verification path.

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-4-dependency-injection-and-object-lifetime"></a>

#### 4. Dependency injection and object lifetime

[Composition and lifetime boundaries](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/03-component-and-module-design/diagrams/module-composition-and-lifetimes.svg)

[Editable DOT](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/03-component-and-module-design/diagrams/module-composition-and-lifetimes.dot) · ![module composition and lifetimes](../Diagrams/Archived-Png/Module-Composition-And-Lifetimes.png)

Use the framework composition root to register approved implementations and construct explicit dependencies. Controllers/handlers receive needed collaborators rather than finding arbitrary services through global lookups. Introduce a port when actual variability, effect control or verification warrants it, not simply to wrap every framework method.

**Command/request scope:** actor context, expected revision, transaction/unit of work and sensitive intent belong to the bounded operation. Do not hold them in shared static state or a singleton that can serve another user or job.

**Worker scope:** a long-lived process may reuse suitable stateless infrastructure, but each job establishes fresh command/claim/authority context and releases/reset resource state. No prior job’s credentials, ORM identity map, transaction or private payload may leak into the next operation.

**External adapters:** inject provider/native Git/storage/executor clients with explicit scope and result semantics. Keep clocks and operation identities controllable where deterministic checks need them. Replacing a client with a mock does not verify the real protocol, isolation or recovery facility.

**Lifetime verification:** evaluate actual framework/runtime lifecycle before selecting concrete registration lifetimes. Request-scoped assumptions from traditional HTTP execution must not silently carry into persistent workers. Secrets and cancellation/resource cleanup require explicit ownership on successful and exceptional paths.

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-5-cohesion-coupling-and-boundary-review"></a>

#### 5. Cohesion coupling and boundary review

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-cohesion-questions"></a>

##### Cohesion questions

Do the module’s state and operations protect a common responsibility or invariant? Can publication, link controls, actual history and file lifecycle be explained without an ambiguous all-purpose manager? Does a technical adapter change for different reasons from domain policy? A small module count or method count alone proves none of these properties.

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-coupling-indicators"></a>

##### Coupling indicators

Review forbidden internal imports/table access, cyclic dependencies, broad interfaces, excessive consumer knowledge of another owner's internals, shared mutable models and scattered policy duplication. Record actual imports/consumers/scenarios and their consequences when implementation exists. No universal coupling/cohesion score or threshold is adopted here.

A dependency count can support a diagnosis, but a shared authority contract may legitimately have many consumers. Conversely one generic service can hide extensive informal coupling. Examine semantic dependence and change impact rather than maximizing interfaces or minimizing counts mechanically.

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-planned-enforcement"></a>

##### Planned enforcement

Once a concrete source layout/toolchain exists, configure boundary checks to allow public contracts and reject forbidden internal imports/cycles. Add focused handler/domain tests, real persistence/concurrency integration and controlled external adapter checks where applicable. The dependency-checking tool and package rules are not selected or executed in this authoring task.

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-required-review-walkthroughs"></a>

##### Required review walkthroughs

- A consumer attempts to mutate another owner’s state: only the public authorized operation is permitted.
- A background task executes after a grant/link/account change: current authority and actual prior effects are reassessed.
- Presentation changes draft/publication internals: Applications retains actual history and Sharing retains its independent controls.
- A provider/renderer adapter changes: source outcome, language, denial and unknown-effect semantics remain compatible.
- A long-lived worker handles different actors: no mutable identity/credential/transaction state crosses job boundaries.
- A new event reaction is proposed: confirm it does not silently send, publish, execute or deploy without the required intent/authority.

These are review/check specifications, not observed tests or proven module enforcement.

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-6-implementation-handoff-and-current-limits"></a>

#### 6. Implementation handoff and current limits

For each actual module package, document exported/internal elements, provided/required operations, owned records/invariants, consumer projections, dependency/transaction boundaries, adapter contracts and construction/lifetime rules. Keep exact types/classes/algorithms and technical scenarios together using the [component package template](#design-record-03-component-and-module-design-component-and-module-design-md).

Map the package to the [implementation artifacts](12-Appendices.md#design-record-03-component-and-module-design-02-implementation-view-and-artifacts-md), [shared data design](04-Database-Design.md#design-record-04-data-design-data-design-md), [interface contracts](05-API-Specification.md#design-record-05-interface-and-api-design-interface-and-api-design-md) and [security/quality](../01-High-Level-Design/14-Appendices.md#design-record-06-design-quality-and-security-analysis-design-quality-and-security-analysis-md). A physical schema, shared database or common release artifact must not erase logical ownership.

Significant dependency changes need [ADR rationale](../ADR/Decision-Index.md#design-record-07-design-decisions-design-decisions-md) and targeted impact assessment. Record actual findings/debt under the [evolution procedure](12-Appendices.md#design-record-02-detailed-and-object-oriented-design-05-design-evolution-refactoring-and-technical-debt-md) and [design review/handoff](../01-High-Level-Design/14-Appendices.md#design-record-06-design-quality-and-security-analysis-05-design-review-traceability-and-handoff-md). Do not label unresolved evidence as accepted debt.

Final language namespaces, framework lifetimes, allowed-import configuration, exact public signatures, complete class models and physical transaction mappings remain implementation-level design follow-up. This guide does not claim that production modules exist or that boundaries have been tested.

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-7-fau-basis-and-diagram-reading"></a>

#### 7. FAU basis and diagram reading

FAU V07 introduces abstraction, modularization, cohesion/coupling, encapsulation and component interfaces; V08 refines components into implementation classes/contracts with conventions and review. The module conventions here adapt those ideas to Resumefolio, rather than prescribe nine deployable services or a mandatory framework package tree.

The diagrams show ownership, dependency and lifetime relationships. Arrows do not mean a temporal call chain or automatic permission inheritance. Editable DOT and SVG/PNG outputs are linked in the [diagram catalog](12-Appendices.md#design-record-03-component-and-module-design-diagrams-diagram-catalog-md). See the [FAU reference map](../01-High-Level-Design/14-Appendices.md#design-record-design-references-and-coverage-md) for source/adaptation limits.

No production source change, provider operation, migration, live security/capacity check or baseline approval is performed by this document update. Advisor transport remains unavailable as previously recorded; no independent endorsement is claimed.

[Component and Module Design index](#design-record-03-component-and-module-design-component-and-module-design-md) · [Architecture boundaries](../01-High-Level-Design/14-Appendices.md#design-record-01-software-architecture-02-system-decomposition-and-boundaries-md)

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-8-essential-modularity-and-encapsulation-views"></a>

#### 8. Essential modularity and encapsulation views

This focused package adds **four diagrams and four reference tables**. Reuse the existing boundary, dependency and lifetime views above and the [architecture module dependency view](../01-High-Level-Design/14-Appendices.md#design-record-01-software-architecture-02-system-decomposition-and-boundaries-md). It does not fabricate a measured whole-code dependency graph, hotspot score or populated import DSM before actual implementation/import inspection. Several logical owners can share one deployable application.

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-81-owner-packages-and-source-dependency-direction"></a>

##### 8.1 Owner packages and source dependency direction

[Owner packages and source dependency direction](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/03-component-and-module-design/diagrams/modularity-essential-packages.svg)

[Editable PlantUML](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/03-component-and-module-design/diagrams/modularity-essential-packages.puml) · ![modularity essential packages](../Diagrams/Archived-Png/Modularity-Essential-Packages.png)

Proposed acyclic source graph, not actual namespaces or a measured import audit. Ports belong in the actual owning contract/application location selected for the codebase; the package label is illustrative. Composition root wires concrete adapters rather than domain code locating arbitrary services.

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-82-allowed-layers-and-forbidden-bypasses"></a>

##### 8.2 Allowed layers and forbidden bypasses

[Allowed layers and forbidden bypasses](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/03-component-and-module-design/diagrams/modularity-essential-layers.svg)

[Editable PlantUML](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/03-component-and-module-design/diagrams/modularity-essential-layers.puml) · ![modularity essential layers](../Diagrams/Archived-Png/Modularity-Essential-Layers.png)

Combines layering, public boundary and dependency inversion in one essential view. Runtime calls may reach an injected adapter while source dependency points toward an abstraction. A shared database or process does not relax another owner’s write boundary.

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-83-public-contract-and-hidden-implementation"></a>

##### 8.3 Public contract and hidden implementation

[Public contract and hidden implementation](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/03-component-and-module-design/diagrams/modularity-essential-encapsulation.svg)

[Editable PlantUML](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/03-component-and-module-design/diagrams/modularity-essential-encapsulation.puml) · ![modularity essential encapsulation](../Diagrams/Archived-Png/Modularity-Essential-Encapsulation.png)

Plus marks public, minus private; tilde denotes package visibility conceptually, not a PHP access modifier. Actual module-internal visibility needs namespaces/import rules and review beyond language member visibility. Return a scoped projection rather than mutable ORM entity, credentials or raw private path. Interface access itself is not permission.

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-84-tangled-versus-owner-controlled-dependencies"></a>

##### 8.4 Tangled versus owner-controlled dependencies

[Tangled versus owner-controlled dependencies](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/03-component-and-module-design/diagrams/modularity-essential-before-after.svg)

[Editable PlantUML](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/03-component-and-module-design/diagrams/modularity-essential-before-after.puml) · ![modularity essential before after](../Diagrams/Archived-Png/Modularity-Essential-Before-After.png)

Illustrates information hiding and cohesion without claiming production smells. Removing a source cycle requires actual ownership/import analysis; a generic event bus cannot conceal an invariant dependency or authorize hidden effects. Do not split every method into an interface merely to lower arrow count.

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-85-information-hiding-and-module-secrets"></a>

##### 8.5 Information hiding and module secrets

“Secret” here means a change-prone implementation detail, not only a credential. Public examples are proposed contracts, not final signatures. Hiding internals never means hiding actual failure/unknown outcomes from consumers.

| Owner | Hidden implementation / decision | Public responsibility |
| --- | --- | --- |
| Identity | Verifiers, session backend, grant storage/invalidation mechanism | Current context and exact scoped evaluation; no raw secrets |
| Presentation | Draft/override persistence, comparison algorithm and manifest mapping | Explicit compare/apply/preview/publish; exact permitted revision projection |
| Sharing | Verifier/viewer storage, serving/invalidation mechanism | Link controls and current exact representation eligibility |
| Applications | Preparation/progress/correction mapping and consumer commit internals | Attributable actual event/material capture and permitted history |
| Communication | Provider client formats, credential handling and correlation mechanism | Explicit reviewed operations with truthful supported observations |
| Work | Ordering/mapping/persistence and cross-item Sprint guard | Coherent work mutation, explicit acceptance and period outcome |
| Git | Native backend integration, canonical storage and ref/SQL reconciliation details | Actual permitted native transfer and exact-revision review/merge |
| Workflow | Dispatch/claim/observation mechanics, workspace/secret implementation | Evidence-gated execution coordination and separate exact target intent |
| Files | Storage keys, accounting/reference/reclamation guards | Usable exact artifacts, protected-reference protocol and real accounting evidence |

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-86-dependency-kinds-to-review"></a>

##### 8.6 Dependency kinds to review

| Kind | Project example | Design / verification implication |
| --- | --- | --- |
| Source / compile-time | Applications imports Presentation's exported projection contract | Inspect actual namespace/import graph; no internal ORM/domain import |
| Runtime | Sharing invokes Files to resolve exact usable bytes | Actual authority, usability and unavailable/unknown semantics still apply |
| Data | Submission manifest retains opaque artifact and provenance identity | Cross-owner references do not grant CRUD; pin/finalize protocol must exclude cleanup races |
| Temporal | Protect exact bytes before consumer commit; finalize against actual result | Ordered steps and unknown-commit reconciliation cannot be replaced by a package diagram |
| Deployment / resource | Modules share web/worker/database/storage budgets | Logical isolation is not executor containment, independent capacity or separate failure domains |

For PHP, “compile-time” is often better described as source/load dependency: actual autoloading and runtime binding determine mechanics. A source dependency graph/DSM must state which kind its edges represent. Runtime callbacks and temporal handshakes do not automatically mean source import cycles.

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-87-public-api-surface-and-stability"></a>

##### 8.7 Public API surface and stability

| Surface | Export status | Stability / evolution obligation |
| --- | --- | --- |
| Named owner operations, validated intent/value types | Export only where an actual consumer needs them | Proposed now; actual compatibility and protected-frame semantics must be versioned/reviewed |
| Permitted result/projection and opaque identity | Export only allowed fields with actual outcome/provenance | No mutable ORM, secret or unrestricted path; identity alone conveys no access |
| Required effect/persistence port | Visible to its justified consumer/adapter/composition scope | Preserve substitution, denial, conflict, partial and unknown semantics |
| Domain mutation objects / ORM mappings / transaction helpers | Owner internal | May evolve internally while actual observable contracts/invariants remain preserved |
| Adapter credentials / storage locators / native workspace | Restricted infrastructure implementation | Never exposed through convenience DTOs/logs or broad service locator |
| Stable shared technical primitive | Shared only with named justified consumers | Keep small; no universal mutable business lifecycle/authority model |

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-88-planned-architecture-fitness-checks"></a>

##### 8.8 Planned architecture fitness checks

No analyzer, CI job or accepted threshold is installed/selected by this document. Choose tools compatible with actual manifests/runtime: ArchUnit is Java-specific and dependency-cruiser targets JavaScript/TypeScript, so neither is assumed to enforce this proposed PHP/Laravel codebase.

| Rule | Tool / method to select | Planned CI / review evidence |
| --- | --- | --- |
| Consumers import only allowed owner contracts | Actual stack-compatible import/dependency analyzer or inspected graph | Check actual namespace allowlist and prohibited internal edges |
| Source dependencies remain acyclic | Actual source-kind graph / DSM and cycle analysis | Report exact participating packages; record actual exception disposition if any |
| Public contracts preserve actual types and outcomes | Selected type/static analysis plus focused contract checks | Signature compatibility alone insufficient for behavioral substitution |
| No foreign state write or hidden consequential effect | Call/write-path review and affected persistence/integration checks | Actual code/transaction/reference evidence; text matching alone not enough |
| No mutable actor/session leaks across jobs | Actual framework binding/lifetime review and concurrent worker cases | Fresh per-operation current scope and released/reset resources |
| Diagram and implementation boundaries agree | Identified candidate import map, public API catalog and source/export checks | Reconcile drift explicitly; document renders are not runtime enforcement |

<a id="design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md--heading-deliberately-omitted-duplicates"></a>

##### Deliberately omitted duplicates

Component provided/required interfaces and boundary sequences already live in the actual [component records](#design-record-03-component-and-module-design-component-and-module-design-md) and [complete template](#design-record-03-component-and-module-design-component-and-module-design-md); do not copy their contracts into a second source here. The layered view combines dependency inversion with allowed/prohibited direction; the before/after view explains coupling/cohesion without another nearly identical diagram. Populate a code DSM only after selecting actual packages, dependency kind and inspected candidate. Intended architecture links are not measured implementation imports or proof of no cycles.

No source module, dependency tool/configuration, CI check, import analysis or production mutation is created by this authoring update. Exact package/visibility enforcement, actual source graph, compatibility and owner-policy checks remain implementation/evidence work.

</details>

<a id="design-record-03-component-and-module-design-component-and-module-design-md"></a>

<details>
<summary>Component and Module Design</summary>

<a id="design-record-03-component-and-module-design-component-and-module-design-md--heading-component-and-module-design"></a>

### Component and Module Design

The [Baseline](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/README.md) selects the MVP system/technical boundaries. These project-specific records retain detailed operation, data, behavior and failure analysis; no source modules or product tests exist yet.

<a id="design-record-03-component-and-module-design-component-and-module-design-md--heading-1-reading-route"></a>

#### 1. Reading route

Start with [architecture decomposition](../01-High-Level-Design/14-Appendices.md#design-record-01-software-architecture-02-system-decomposition-and-boundaries-md), [module/dependency rules](#design-record-03-component-and-module-design-01-modularity-dependencies-and-encapsulation-md) and [implementation artifacts](12-Appendices.md#design-record-03-component-and-module-design-02-implementation-view-and-artifacts-md), then the affected component below. Use shared [Data](04-Database-Design.md#design-record-04-data-design-data-design-md), [API](05-API-Specification.md#design-record-05-interface-and-api-design-interface-and-api-design-md) and [Security/Quality](../01-High-Level-Design/14-Appendices.md#design-record-06-design-quality-and-security-analysis-design-quality-and-security-analysis-md) owners rather than copy their policies into each record.

<a id="design-record-03-component-and-module-design-component-and-module-design-md--heading-2-shared-module-and-implementation-guidance"></a>

#### 2. Shared module and implementation guidance

For each component keep responsibilities/contracts, identities/classes/data, algorithms/concurrency, failure/recovery scenarios and justified coding constraints together. Refine the existing actual record instead of creating a second generic package. Link exact source criteria and important [ADRs](../ADR/Decision-Index.md#design-record-07-design-decisions-design-decisions-md); retain allowed/denied/stale/repeated/failure outcomes and their verification needs.

<a id="design-record-03-component-and-module-design-component-and-module-design-md--heading-3-proposed-component-catalog"></a>

#### 3. Proposed component catalog

Current MVP slices are governed by the Baseline. Component models may include explicitly deferred extensions; their existence does not add those features to the current Release.

<a id="design-record-03-component-and-module-design-component-and-module-design-md--heading-lc-01--identity-and-access"></a>

##### LC-01 — Identity and Access

[Component record](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-identity-and-access-md). Owns accounts, invitations, sessions and scoped grant context. Resource owners still apply current operation/lifecycle rules; successful sign-in or a membership never supplies universal access.

<a id="design-record-03-component-and-module-design-component-and-module-design-md--heading-lc-02--professional-presentation"></a>

##### LC-02 — Professional Presentation

[Component record](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-professional-presentation-md). Owns profiles, independent drafts/overrides, selected evidence and identified publication revisions. Selected source application and separate publication preserve independent resume content and actual history.

<a id="design-record-03-component-and-module-design-component-and-module-design-md--heading-lc-03--representation-and-sharing"></a>

##### LC-03 — Representation and Sharing

[Component record](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-representation-and-sharing-md). Owns download settings, independent links and viewer authorization. Current eligibility, selected publication/language/rendition and artifact availability remain distinct; direct retrieval cannot bypass them.

<a id="design-record-03-component-and-module-design-component-and-module-design-md--heading-lc-04--manual-applications"></a>

##### LC-04 — Manual Applications

[Component record](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-applications-md). Owns opportunity/preparation, manual progress and actual submission material manifests. Progress, provider acceptance and actual submitted evidence are different facts; current live content does not replace historical material.

<a id="design-record-03-component-and-module-design-component-and-module-design-md--heading-lc-05--communication-and-calendar"></a>

##### LC-05 — Communication and Calendar

**After MVP.** Shared operating and recovery controls still apply where relevant.

[Component record](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-communication-and-calendar-md). Owns provider capability, local drafts/activities, attributable send attempts and synchronization mappings. Disconnect/unlink/provider mutation and uncertain effects need explicit handling rather than replay or silent conflict resolution.

<a id="design-record-03-component-and-module-design-component-and-module-design-md--heading-lc-06--work-management"></a>

##### LC-06 — Work Management

[Component record](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-work-management-md). MVP owns ProjectForge issues and fixed simple Kanban, membership and safe movement. General projects/backlog/Sprints and advanced planning remain after MVP.

<a id="design-record-03-component-and-module-design-component-and-module-design-md--heading-lc-07--git-collaboration"></a>

##### LC-07 — Git Collaboration

[Component record](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-git-collaboration-md). MVP owns authorized repositories, real native Git transfers, file/history and basic issues. Advanced fork/review/merge/releases are deferred; Git operations never authorize user workflow execution or production deployment.

<a id="design-record-03-component-and-module-design-component-and-module-design-md--heading-lc-08--workflow-and-deployment-coordination"></a>

##### LC-08 — Workflow and Deployment Coordination

**After MVP.** Shared operating and recovery controls still apply where relevant.

[Component record](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-workflow-and-deployment-md). Owns supported workflow definitions, admitted attempts, restricted output references and separately authorized target attempts. Execution requires actual enabling evidence; cancellation intent is not confirmed termination.

<a id="design-record-03-component-and-module-design-component-and-module-design-md--heading-lc-09--files-and-operations"></a>

##### LC-09 — Files and Operations

[Component record](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-files-and-operations-md). Owns admitted artifact identity/usability, quota reservations, protected-reference accounting and recovery records. Replacement, retirement, physical reclamation and usable recovery require their actual attributable outcomes.

<a id="design-record-03-component-and-module-design-component-and-module-design-md--heading-4-completing-one-component-package"></a>

#### 4. Completing one component package

Use the selected mechanisms in the Baseline. During implementation add actual operation signatures, schema/migration and code paths plus criterion-linked checks. Source/draft/publication/submission identity, current grant/link revocation, protected references and durable truthful effects must remain consistent across owners. The Core and ProjectForge retain independent DB/process/key/session/storage boundaries.

<a id="design-record-03-component-and-module-design-component-and-module-design-md--heading-5-diagram-guide"></a>

#### 5. Diagram guide

[Shared module diagrams](12-Appendices.md#design-record-03-component-and-module-design-diagrams-diagram-catalog-md) and [component diagrams](12-Appendices.md#design-record-03-component-and-module-design-components-diagrams-diagram-catalog-md) link editable sources and exports. Byte-identical views use one canonical asset; distinct models and their meanings are retained. Generic uninstantiated examples are omitted from current Documentation.

<a id="design-record-03-component-and-module-design-component-and-module-design-md--heading-6-review-and-current-limits"></a>

#### 6. Review and current limits

Review contracts against the owning requirements, current authority, data/state invariants and consumer/failure consequences. Link actual targeted results before accepting dependent capability. Security, compatibility, resource suitability and demonstrated restore remain named gates; no provider/runner/Git capability is established by a model or diagram count.

<a id="design-record-03-component-and-module-design-component-and-module-design-md--heading-7-fau-basis-and-maintenance"></a>

#### 7. FAU basis and maintenance

Keep analysis meaning separate from physical deployment/code mechanisms. Use the [reference map](../01-High-Level-Design/14-Appendices.md#design-record-design-references-and-coverage-md), [evolution procedure](12-Appendices.md#design-record-02-detailed-and-object-oriented-design-05-design-evolution-refactoring-and-technical-debt-md) and [Design review/handoff](../01-High-Level-Design/14-Appendices.md#design-record-06-design-quality-and-security-analysis-05-design-review-traceability-and-handoff-md) when a material interface/ownership choice changes.

</details>

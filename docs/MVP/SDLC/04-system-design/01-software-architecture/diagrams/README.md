# Resumefolio — Architecture Diagram Catalog

Status: Proposed design views, November 2, 2026. No topology, capacity or control is demonstrated by a diagram.

| Diagram | Purpose | Editable source | PNG |
|---|---|---|---|
| [Drivers and design implications](drivers-to-architecture.svg) | Drivers and design implications | [DOT](drivers-to-architecture.dot) | [PNG](drivers-to-architecture.png) |
| [Proposed application and effect boundaries](proposed-solution-boundaries.svg) | Proposed application and effect boundaries | [DOT](proposed-solution-boundaries.dot) | [PNG](proposed-solution-boundaries.png) |
| [Decision and evidence route](architecture-decision-route.svg) | Decision and evidence route | [DOT](architecture-decision-route.dot) | [PNG](architecture-decision-route.png) |

[Owning assessment](../01-design-drivers-and-solution-options.md) · [Architecture index](../README.md)

Keep source and SVG/PNG exports together. Update source and rerender when meaning changes; inspect readable output and preserve proposal/observation labels.

## MVP system allocation and design status

The accepted system boundary separates the Resumefolio core from ProjectForge, joined by an authenticated user-scoped API. Logical responsibilities remain useful within each system; they do not authorize a shared core/ProjectForge process, database or transaction. Core owns dashboard, invited accounts, professional presentation, protected sharing, manual applications and same-server private My Files & Media. ProjectForge MVP owns real repositories/transfers/permissions, file/history browsing, issues and simple Kanban. Its engine, deployment and database remain open. The future communications system is independently private and API connected. Advanced Git review/releases, backlog/Sprints and execution/deployment remain deferred. Keep source, independent resume draft, explicit publication and actual submitted material identities distinct. Profile changes require preview/select/apply and cannot mutate publication or submitted history. Manual applications include status, next action and follow-up date without mail/calendar dependencies.

Authority: [OWNER-MVP-2026-11-04](../../../01-project-planning/owner-mvp-decision-2026-11-04.md).

## System decomposition and boundaries

- [Logical component ownership](logical-component-ownership.svg) · [DOT](logical-component-ownership.dot) · [PNG](logical-component-ownership.png)
- [Public contracts and adapter boundaries](component-contract-boundaries.svg) · [DOT](component-contract-boundaries.dot) · [PNG](component-contract-boundaries.png)
- [Presentation and historical identity boundaries](presentation-history-boundaries.svg) · [DOT](presentation-history-boundaries.dot) · [PNG](presentation-history-boundaries.png)

[Owning decomposition document](../02-system-decomposition-and-boundaries.md). All three diagrams describe proposed logical boundaries, not verified physical facilities.

## Runtime concurrency and failure handling

- [Runtime responsibilities](runtime-responsibilities.svg) · [DOT](runtime-responsibilities.dot) · [PNG](runtime-responsibilities.png)
- [Durable intent and external effects](durable-attempt-protocol.svg) · [DOT](durable-attempt-protocol.dot) · [PNG](durable-attempt-protocol.png)
- [Cancellation and reconciliation](cancellation-reconciliation.svg) · [DOT](cancellation-reconciliation.dot) · [PNG](cancellation-reconciliation.png)

[Owning runtime design](../03-process-view-concurrency-and-runtime-behavior.md). Proposed process/behavior views; no queue, executor or runtime result is established by the diagrams.

## Deployment topology and operating boundaries

- [Proposed deployment candidate](deployment-candidate-topology.svg) · [DOT](deployment-candidate-topology.dot) · [PNG](deployment-candidate-topology.png)
- [Network access zones](network-access-zones.svg) · [DOT](network-access-zones.dot) · [PNG](network-access-zones.png)
- [Release and recovery route](release-and-recovery-route.svg) · [DOT](release-and-recovery-route.dot) · [PNG](release-and-recovery-route.png)

[Owning deployment design](../04-deployment-topology-nodes-and-networks.md). Proposed placements and paths; backup/executor facilities and capacity remain unverified.

## Cross-cutting concern coordination

- [Shared concern ownership](cross-cutting-ownership.svg) · [DOT](cross-cutting-ownership.dot) · [PNG](cross-cutting-ownership.png)
- [Cross-cutting change route](cross-cutting-change-route.svg) · [DOT](cross-cutting-change-route.dot) · [PNG](cross-cutting-change-route.png)

[Owning overview](../05-cross-cutting-concerns-overview.md). Coordination views; detailed mechanisms remain in their authoritative topic records.

## Drivers and options — complete visual comparison package

- [C4 Level 1 — system context](drivers-c4-system-context.svg) · [PlantUML](drivers-c4-system-context.puml) · [PNG](drivers-c4-system-context.png)
- [Quality attribute utility tree](drivers-quality-utility-tree.svg) · [PlantUML](drivers-quality-utility-tree.puml) · [PNG](drivers-quality-utility-tree.png)
- [UML use-case scope overview](drivers-uml-use-cases.svg) · [PlantUML](drivers-uml-use-cases.puml) · [PNG](drivers-uml-use-cases.png)
- [Option A — weakly bounded monolith](drivers-option-a-components.svg) · [PlantUML](drivers-option-a-components.puml) · [PNG](drivers-option-a-components.png)
- [Option B — modular monolith](drivers-option-b-components.svg) · [PlantUML](drivers-option-b-components.puml) · [PNG](drivers-option-b-components.png)
- [Option C — initial microservices](drivers-option-c-components.svg) · [PlantUML](drivers-option-c-components.puml) · [PNG](drivers-option-c-components.png)
- [UML deployment — Option B candidate](drivers-uml-deployment.svg) · [PlantUML](drivers-uml-deployment.puml) · [PNG](drivers-uml-deployment.png)
- [Critical sequence — explicit publication](drivers-critical-publication-sequence.svg) · [PlantUML](drivers-critical-publication-sequence.puml) · [PNG](drivers-critical-publication-sequence.png)
- [Illustrative qualitative radar](drivers-options-radar.svg) · [Python generator](drivers-options-radar.py) · [Rubric/data](drivers-options-radar.json) · [PNG](drivers-options-radar.png)

[Owning driver/option assessment](../01-design-drivers-and-solution-options.md). Proposed views and unweighted ordinal judgments, not benchmark results or selected facilities. ADR-001 remains the single decision record.

## Decomposition — expanded boundary views

- [DDD context map](boundaries-ddd-context-map.svg) · [PlantUML](boundaries-ddd-context-map.puml) · [PNG](boundaries-ddd-context-map.png)
- [Candidate bounded contexts](boundaries-ddd-contexts.svg) · [PlantUML](boundaries-ddd-contexts.puml) · [PNG](boundaries-ddd-contexts.png)
- [C4 Level 2 container candidate](boundaries-c4-containers.svg) · [PlantUML](boundaries-c4-containers.puml) · [PNG](boundaries-c4-containers.png)
- [UML logical component and contract view](boundaries-uml-components.svg) · [PlantUML](boundaries-uml-components.puml) · [PNG](boundaries-uml-components.png)
- [UML candidate package organization](boundaries-uml-packages.svg) · [PlantUML](boundaries-uml-packages.puml) · [PNG](boundaries-uml-packages.png)
- [Hexagonal component realization](boundaries-hexagonal-module.svg) · [PlantUML](boundaries-hexagonal-module.puml) · [PNG](boundaries-hexagonal-module.png)
- [Selected module dependency diagram](boundaries-module-dependencies.svg) · [PlantUML](boundaries-module-dependencies.puml) · [PNG](boundaries-module-dependencies.png)
- [Proposed big-picture event-storming board](boundaries-big-picture-events.svg) · [PlantUML](boundaries-big-picture-events.puml) · [PNG](boundaries-big-picture-events.png)
- [Cross-boundary actual-material capture sequence](boundaries-cross-context-capture.svg) · [PlantUML](boundaries-cross-context-capture.puml) · [PNG](boundaries-cross-context-capture.png)

[C4 Level 1 context](drivers-c4-system-context.svg) is reused from the driver assessment. [Owning decomposition document](../02-system-decomposition-and-boundaries.md). Candidate contexts/contracts and desk-synthesized events do not establish accepted services, workshop outcomes, configured facilities or implemented control.

## Runtime — expanded process and concurrency views

- [Sequence — guarded local command](runtime-local-command-sequence.svg) · [PlantUML](runtime-local-command-sequence.puml) · [PNG](runtime-local-command-sequence.png)
- [Sequence — lost external response](runtime-remote-effect-sequence.svg) · [PlantUML](runtime-remote-effect-sequence.puml) · [PNG](runtime-remote-effect-sequence.png)
- [UML activity — lanes and fork/join](runtime-swimlane-fork-join.svg) · [PlantUML](runtime-swimlane-fork-join.puml) · [PNG](runtime-swimlane-fork-join.png)
- [UML state machine — attempt knowledge](runtime-attempt-state-machine.svg) · [PlantUML](runtime-attempt-state-machine.puml) · [PNG](runtime-attempt-state-machine.png)
- [UML communication — numbered collaboration](runtime-communication-diagram.svg) · [PlantUML](runtime-communication-diagram.puml) · [PNG](runtime-communication-diagram.png)
- [UML timing — lease versus effect knowledge](runtime-claim-timing.svg) · [PlantUML](runtime-claim-timing.puml) · [PNG](runtime-claim-timing.png)
- [Process/thread view — bounded execution units](runtime-process-thread-view.svg) · [PlantUML](runtime-process-thread-view.puml) · [PNG](runtime-process-thread-view.png)
- [Concurrency model — bounded processes and scoped work](runtime-concurrency-model.svg) · [PlantUML](runtime-concurrency-model.puml) · [PNG](runtime-concurrency-model.png)
- [Message flow and logical queue topology](runtime-queue-topology.svg) · [PlantUML](runtime-queue-topology.puml) · [PNG](runtime-queue-topology.png)
- [UML deployment — runtime processes on candidate nodes](runtime-process-deployment.svg) · [PlantUML](runtime-process-deployment.puml) · [PNG](runtime-process-deployment.png)
- [Resource contention — guards and shared capacity](runtime-resource-contention.svg) · [PlantUML](runtime-resource-contention.puml) · [PNG](runtime-resource-contention.png)
- [DFD — intent and observation data](runtime-dataflow.svg) · [PlantUML](runtime-dataflow.puml) · [PNG](runtime-dataflow.png)
- [Optional wait-for graph — hypothetical deadlock](runtime-wait-for-example.svg) · [PlantUML](runtime-wait-for-example.puml) · [PNG](runtime-wait-for-example.png)

[Owning runtime document](../03-process-view-concurrency-and-runtime-behavior.md#8-runtime-diagram-package). Synthetic timing and hypothetical wait-for analysis are illustrations, not measurements/observed defects; runtime/queue/containment facilities remain pending.

## Deployment — expanded topology, environments and resilience package

- [UML deployment — nodes, artifacts and environments](deployment-uml-nodes-artifacts.svg) · [PlantUML](deployment-uml-nodes-artifacts.puml) · [PNG](deployment-uml-nodes-artifacts.png)
- [Network topology — subnets and routing concepts](deployment-network-topology.svg) · [PlantUML](deployment-network-topology.puml) · [PNG](deployment-network-topology.png)
- [Infrastructure — provider context and optional components](deployment-provider-infrastructure.svg) · [PlantUML](deployment-provider-infrastructure.puml) · [PNG](deployment-provider-infrastructure.png)
- [Container/orchestration — optional cluster design](deployment-orchestration-alternative.svg) · [PlantUML](deployment-orchestration-alternative.puml) · [PNG](deployment-orchestration-alternative.png)
- [Network segmentation — logical security zones](deployment-security-segmentation.svg) · [PlantUML](deployment-security-segmentation.puml) · [PNG](deployment-security-segmentation.png)
- [Traffic flow — proxy and optional balancing](deployment-traffic-flow.svg) · [PlantUML](deployment-traffic-flow.puml) · [PNG](deployment-traffic-flow.png)
- [Multi-region / failure-zone alternative](deployment-multiregion-alternative.svg) · [PlantUML](deployment-multiregion-alternative.puml) · [PNG](deployment-multiregion-alternative.png)
- [Failover and disaster recovery](deployment-failover-dr-route.svg) · [PlantUML](deployment-failover-dr-route.puml) · [PNG](deployment-failover-dr-route.png)
- [Environment topology — dev, staging, production](deployment-environment-topology.svg) · [PlantUML](deployment-environment-topology.puml) · [PNG](deployment-environment-topology.png)
- [CI/CD — exact artifact to target mapping](deployment-cicd-artifact-nodes.svg) · [PlantUML](deployment-cicd-artifact-nodes.puml) · [PNG](deployment-cicd-artifact-nodes.png)
- [Sequence — protected request across tiers](deployment-network-request-sequence.svg) · [PlantUML](deployment-network-request-sequence.puml) · [PNG](deployment-network-request-sequence.png)

[Owning deployment document and tables](../04-deployment-topology-nodes-and-networks.md#9-deployment-diagram-and-sizing-package). C4 context is reused from the driver view. Cloud/cluster/region/standby alternatives are not selected facilities; ports and sizing are candidate contracts or dated inventory, not live configuration.

## Cross-cutting concerns — expanded realization package

- [Hexagonal architecture with concern overlays](concerns-hexagonal-overlay.svg) · [PlantUML](concerns-hexagonal-overlay.puml) · [PNG](concerns-hexagonal-overlay.png)
- [Security architecture and trust crossings](concerns-security-architecture.svg) · [PlantUML](concerns-security-architecture.puml) · [PNG](concerns-security-architecture.png)
- [Authentication and authorization sequence](concerns-authn-authz-sequence.svg) · [PlantUML](concerns-authn-authz-sequence.puml) · [PNG](concerns-authn-authz-sequence.png)
- [Observability — logs, metrics and tracing](concerns-observability-pipeline.svg) · [PlantUML](concerns-observability-pipeline.puml) · [PNG](concerns-observability-pipeline.png)
- [Activity — error and exception outcomes](concerns-error-flow.svg) · [PlantUML](concerns-error-flow.puml) · [PNG](concerns-error-flow.png)
- [Configuration management and effective identity](concerns-configuration-management.svg) · [PlantUML](concerns-configuration-management.puml) · [PNG](concerns-configuration-management.png)
- [Caching strategy and current authority](concerns-cache-strategy.svg) · [PlantUML](concerns-cache-strategy.puml) · [PNG](concerns-cache-strategy.png)
- [Local transaction and external effect boundaries](concerns-transaction-boundary.svg) · [PlantUML](concerns-transaction-boundary.puml) · [PNG](concerns-transaction-boundary.png)
- [Resilience — bounded protection and safe repetition](concerns-resilience-patterns.svg) · [PlantUML](concerns-resilience-patterns.puml) · [PNG](concerns-resilience-patterns.png)
- [UML circuit-breaker state machine](concerns-circuit-breaker-states.svg) · [PlantUML](concerns-circuit-breaker-states.puml) · [PNG](concerns-circuit-breaker-states.png)
- [Interceptor / middleware chain](concerns-middleware-chain.svg) · [PlantUML](concerns-middleware-chain.puml) · [PNG](concerns-middleware-chain.png)
- [Shared libraries and optional sidecar responsibilities](concerns-shared-components.svg) · [PlantUML](concerns-shared-components.puml) · [PNG](concerns-shared-components.png)
- [DFD with trust boundaries](concerns-trust-dfd.svg) · [PlantUML](concerns-trust-dfd.puml) · [PNG](concerns-trust-dfd.png)

[Owning concern overview and matrices](../05-cross-cutting-concerns-overview.md#7-cross-cutting-realization-package). Shared responsibilities and optional resilience/sidecar examples do not establish selected facilities, numerical policies or verified controls.

## November 4 release applicability

Current MVP figures replace the former common-product boundary. Future and historical figures retain their details without committing them to MVP.

| Editable source | Current applicability |
| --- | --- |
| [boundaries-c4-containers.puml](boundaries-c4-containers.puml) | MVP systems|
| [boundaries-ddd-context-map.puml](boundaries-ddd-context-map.puml) | MVP systems|
| [boundaries-ddd-contexts.puml](boundaries-ddd-contexts.puml) | MVP systems|
| [boundaries-module-dependencies.puml](boundaries-module-dependencies.puml) | MVP systems|
| [boundaries-uml-components.puml](boundaries-uml-components.puml) | MVP systems|
| [boundaries-uml-packages.puml](boundaries-uml-packages.puml) | MVP systems|
| [deployment-candidate-topology.dot](deployment-candidate-topology.dot) | MVP core / cross-cutting|
| [deployment-cicd-artifact-nodes.puml](deployment-cicd-artifact-nodes.puml) | MVP core / cross-cutting|
| [deployment-failover-dr-route.puml](deployment-failover-dr-route.puml) | MVP core / cross-cutting|
| [deployment-network-request-sequence.puml](deployment-network-request-sequence.puml) | MVP core / cross-cutting|
| [deployment-network-topology.puml](deployment-network-topology.puml) | Historical / alternative|
| [deployment-orchestration-alternative.puml](deployment-orchestration-alternative.puml) | Historical / alternative|
| [deployment-provider-infrastructure.puml](deployment-provider-infrastructure.puml) | Historical / alternative|
| [deployment-security-segmentation.puml](deployment-security-segmentation.puml) | MVP systems|
| [deployment-traffic-flow.puml](deployment-traffic-flow.puml) | MVP core / cross-cutting|
| [deployment-uml-nodes-artifacts.puml](deployment-uml-nodes-artifacts.puml) | MVP deployment|
| [drivers-c4-system-context.puml](drivers-c4-system-context.puml) | MVP systems|
| [drivers-uml-deployment.puml](drivers-uml-deployment.puml) | MVP deployment|
| [logical-component-ownership.dot](logical-component-ownership.dot) | MVP core / cross-cutting|
| [network-access-zones.dot](network-access-zones.dot) | MVP core / cross-cutting|
| [proposed-solution-boundaries.dot](proposed-solution-boundaries.dot) | MVP core / cross-cutting|
| [runtime-communication-diagram.puml](runtime-communication-diagram.puml) | Method / document navigation|
| [runtime-process-deployment.puml](runtime-process-deployment.puml) | MVP deployment|
| [mvp-private-media.puml](mvp-private-media.puml) | MVP core / cross-cutting|
| [mvp-system-boundaries.puml](mvp-system-boundaries.puml) | MVP core / cross-cutting|

| [boundaries-big-picture-events.puml](boundaries-big-picture-events.puml) | Mixed MVP / future|
| [drivers-uml-use-cases.puml](drivers-uml-use-cases.puml) | Mixed MVP / future|

## Complete diagram alignment — November 4

[Full project inventory and verification limits](../../../diagram-alignment-review-2026-11-04.md). This current disposition supersedes earlier partial diagram-allocation lists.

| Editable source or visual | Current applicability | Matching exports |
| --- | --- | --- |
| [architecture-decision-route.dot](architecture-decision-route.dot) | Method / document navigation| [SVG](architecture-decision-route.svg) · [PNG](architecture-decision-route.png) |
| [boundaries-big-picture-events.puml](boundaries-big-picture-events.puml) | Mixed MVP / future| [SVG](boundaries-big-picture-events.svg) · [PNG](boundaries-big-picture-events.png) |
| [boundaries-c4-containers.puml](boundaries-c4-containers.puml) | MVP systems| [SVG](boundaries-c4-containers.svg) · [PNG](boundaries-c4-containers.png) |
| [boundaries-cross-context-capture.puml](boundaries-cross-context-capture.puml) | MVP core / cross-cutting| [SVG](boundaries-cross-context-capture.svg) · [PNG](boundaries-cross-context-capture.png) |
| [boundaries-ddd-context-map.puml](boundaries-ddd-context-map.puml) | MVP systems| [SVG](boundaries-ddd-context-map.svg) · [PNG](boundaries-ddd-context-map.png) |
| [boundaries-ddd-contexts.puml](boundaries-ddd-contexts.puml) | MVP systems| [SVG](boundaries-ddd-contexts.svg) · [PNG](boundaries-ddd-contexts.png) |
| [boundaries-hexagonal-module.puml](boundaries-hexagonal-module.puml) | MVP core / cross-cutting| [SVG](boundaries-hexagonal-module.svg) · [PNG](boundaries-hexagonal-module.png) |
| [boundaries-module-dependencies.puml](boundaries-module-dependencies.puml) | MVP systems| [SVG](boundaries-module-dependencies.svg) · [PNG](boundaries-module-dependencies.png) |
| [boundaries-uml-components.puml](boundaries-uml-components.puml) | MVP systems| [SVG](boundaries-uml-components.svg) · [PNG](boundaries-uml-components.png) |
| [boundaries-uml-packages.puml](boundaries-uml-packages.puml) | MVP systems| [SVG](boundaries-uml-packages.svg) · [PNG](boundaries-uml-packages.png) |
| [cancellation-reconciliation.dot](cancellation-reconciliation.dot) | MVP core / cross-cutting| [SVG](cancellation-reconciliation.svg) · [PNG](cancellation-reconciliation.png) |
| [component-contract-boundaries.dot](component-contract-boundaries.dot) | Mixed MVP / future| [SVG](component-contract-boundaries.svg) · [PNG](component-contract-boundaries.png) |
| [concerns-authn-authz-sequence.puml](concerns-authn-authz-sequence.puml) | MVP core / cross-cutting| [SVG](concerns-authn-authz-sequence.svg) · [PNG](concerns-authn-authz-sequence.png) |
| [concerns-cache-strategy.puml](concerns-cache-strategy.puml) | MVP core / cross-cutting| [SVG](concerns-cache-strategy.svg) · [PNG](concerns-cache-strategy.png) |
| [concerns-circuit-breaker-states.puml](concerns-circuit-breaker-states.puml) | MVP core / cross-cutting| [SVG](concerns-circuit-breaker-states.svg) · [PNG](concerns-circuit-breaker-states.png) |
| [concerns-configuration-management.puml](concerns-configuration-management.puml) | MVP core / cross-cutting| [SVG](concerns-configuration-management.svg) · [PNG](concerns-configuration-management.png) |
| [concerns-error-flow.puml](concerns-error-flow.puml) | MVP core / cross-cutting| [SVG](concerns-error-flow.svg) · [PNG](concerns-error-flow.png) |
| [concerns-hexagonal-overlay.puml](concerns-hexagonal-overlay.puml) | MVP core / cross-cutting| [SVG](concerns-hexagonal-overlay.svg) · [PNG](concerns-hexagonal-overlay.png) |
| [concerns-middleware-chain.puml](concerns-middleware-chain.puml) | MVP core / cross-cutting| [SVG](concerns-middleware-chain.svg) · [PNG](concerns-middleware-chain.png) |
| [concerns-observability-pipeline.puml](concerns-observability-pipeline.puml) | MVP core / cross-cutting| [SVG](concerns-observability-pipeline.svg) · [PNG](concerns-observability-pipeline.png) |
| [concerns-resilience-patterns.puml](concerns-resilience-patterns.puml) | MVP core / cross-cutting| [SVG](concerns-resilience-patterns.svg) · [PNG](concerns-resilience-patterns.png) |
| [concerns-security-architecture.puml](concerns-security-architecture.puml) | Mixed MVP / future| [SVG](concerns-security-architecture.svg) · [PNG](concerns-security-architecture.png) |
| [concerns-shared-components.puml](concerns-shared-components.puml) | MVP core / cross-cutting| [SVG](concerns-shared-components.svg) · [PNG](concerns-shared-components.png) |
| [concerns-transaction-boundary.puml](concerns-transaction-boundary.puml) | MVP core / cross-cutting| [SVG](concerns-transaction-boundary.svg) · [PNG](concerns-transaction-boundary.png) |
| [concerns-trust-dfd.puml](concerns-trust-dfd.puml) | Mixed MVP / future| [SVG](concerns-trust-dfd.svg) · [PNG](concerns-trust-dfd.png) |
| [cross-cutting-change-route.dot](cross-cutting-change-route.dot) | MVP core / cross-cutting| [SVG](cross-cutting-change-route.svg) · [PNG](cross-cutting-change-route.png) |
| [cross-cutting-ownership.dot](cross-cutting-ownership.dot) | MVP core / cross-cutting| [SVG](cross-cutting-ownership.svg) · [PNG](cross-cutting-ownership.png) |
| [deployment-candidate-topology.dot](deployment-candidate-topology.dot) | MVP core / cross-cutting| [SVG](deployment-candidate-topology.svg) · [PNG](deployment-candidate-topology.png) |
| [deployment-cicd-artifact-nodes.puml](deployment-cicd-artifact-nodes.puml) | MVP core / cross-cutting| [SVG](deployment-cicd-artifact-nodes.svg) · [PNG](deployment-cicd-artifact-nodes.png) |
| [deployment-environment-topology.puml](deployment-environment-topology.puml) | MVP core / cross-cutting| [SVG](deployment-environment-topology.svg) · [PNG](deployment-environment-topology.png) |
| [deployment-failover-dr-route.puml](deployment-failover-dr-route.puml) | MVP core / cross-cutting| [SVG](deployment-failover-dr-route.svg) · [PNG](deployment-failover-dr-route.png) |
| [deployment-multiregion-alternative.puml](deployment-multiregion-alternative.puml) | MVP core / cross-cutting| [SVG](deployment-multiregion-alternative.svg) · [PNG](deployment-multiregion-alternative.png) |
| [deployment-network-request-sequence.puml](deployment-network-request-sequence.puml) | MVP core / cross-cutting| [SVG](deployment-network-request-sequence.svg) · [PNG](deployment-network-request-sequence.png) |
| [deployment-network-topology.puml](deployment-network-topology.puml) | Historical / alternative| [SVG](deployment-network-topology.svg) · [PNG](deployment-network-topology.png) |
| [deployment-orchestration-alternative.puml](deployment-orchestration-alternative.puml) | Historical / alternative| [SVG](deployment-orchestration-alternative.svg) · [PNG](deployment-orchestration-alternative.png) |
| [deployment-provider-infrastructure.puml](deployment-provider-infrastructure.puml) | Historical / alternative| [SVG](deployment-provider-infrastructure.svg) · [PNG](deployment-provider-infrastructure.png) |
| [deployment-security-segmentation.puml](deployment-security-segmentation.puml) | MVP systems| [SVG](deployment-security-segmentation.svg) · [PNG](deployment-security-segmentation.png) |
| [deployment-traffic-flow.puml](deployment-traffic-flow.puml) | MVP core / cross-cutting| [SVG](deployment-traffic-flow.svg) · [PNG](deployment-traffic-flow.png) |
| [deployment-uml-nodes-artifacts.puml](deployment-uml-nodes-artifacts.puml) | MVP deployment| [SVG](deployment-uml-nodes-artifacts.svg) · [PNG](deployment-uml-nodes-artifacts.png) |
| [drivers-c4-system-context.puml](drivers-c4-system-context.puml) | MVP systems| [SVG](drivers-c4-system-context.svg) · [PNG](drivers-c4-system-context.png) |
| [drivers-critical-publication-sequence.puml](drivers-critical-publication-sequence.puml) | MVP core / cross-cutting| [SVG](drivers-critical-publication-sequence.svg) · [PNG](drivers-critical-publication-sequence.png) |
| [drivers-option-a-components.puml](drivers-option-a-components.puml) | Historical / alternative| [SVG](drivers-option-a-components.svg) · [PNG](drivers-option-a-components.png) |
| [drivers-option-b-components.puml](drivers-option-b-components.puml) | MVP systems| [SVG](drivers-option-b-components.svg) · [PNG](drivers-option-b-components.png) |
| [drivers-option-c-components.puml](drivers-option-c-components.puml) | Historical / alternative| [SVG](drivers-option-c-components.svg) · [PNG](drivers-option-c-components.png) |
| [drivers-options-radar.py](drivers-options-radar.py) | Historical / alternative | [SVG](drivers-options-radar.svg) · [PNG](drivers-options-radar.png) |
| [drivers-quality-utility-tree.puml](drivers-quality-utility-tree.puml) | MVP core / cross-cutting| [SVG](drivers-quality-utility-tree.svg) · [PNG](drivers-quality-utility-tree.png) |
| [drivers-to-architecture.dot](drivers-to-architecture.dot) | MVP core / cross-cutting| [SVG](drivers-to-architecture.svg) · [PNG](drivers-to-architecture.png) |
| [drivers-uml-deployment.puml](drivers-uml-deployment.puml) | MVP deployment| [SVG](drivers-uml-deployment.svg) · [PNG](drivers-uml-deployment.png) |
| [drivers-uml-use-cases.puml](drivers-uml-use-cases.puml) | Mixed MVP / future| [SVG](drivers-uml-use-cases.svg) · [PNG](drivers-uml-use-cases.png) |
| [durable-attempt-protocol.dot](durable-attempt-protocol.dot) | MVP core / cross-cutting| [SVG](durable-attempt-protocol.svg) · [PNG](durable-attempt-protocol.png) |
| [logical-component-ownership.dot](logical-component-ownership.dot) | MVP core / cross-cutting| [SVG](logical-component-ownership.svg) · [PNG](logical-component-ownership.png) |
| [mvp-private-media.puml](mvp-private-media.puml) | MVP core / cross-cutting| [SVG](mvp-private-media.svg) · [PNG](mvp-private-media.png) |
| [mvp-system-boundaries.puml](mvp-system-boundaries.puml) | MVP core / cross-cutting| [SVG](mvp-system-boundaries.svg) · [PNG](mvp-system-boundaries.png) |
| [network-access-zones.dot](network-access-zones.dot) | MVP core / cross-cutting| [SVG](network-access-zones.svg) · [PNG](network-access-zones.png) |
| [presentation-history-boundaries.dot](presentation-history-boundaries.dot) | Method / document navigation| [SVG](presentation-history-boundaries.svg) · [PNG](presentation-history-boundaries.png) |
| [proposed-solution-boundaries.dot](proposed-solution-boundaries.dot) | MVP core / cross-cutting| [SVG](proposed-solution-boundaries.svg) · [PNG](proposed-solution-boundaries.png) |
| [release-and-recovery-route.dot](release-and-recovery-route.dot) | MVP core / cross-cutting| [SVG](release-and-recovery-route.svg) · [PNG](release-and-recovery-route.png) |
| [runtime-attempt-state-machine.puml](runtime-attempt-state-machine.puml) | MVP core / cross-cutting| [SVG](runtime-attempt-state-machine.svg) · [PNG](runtime-attempt-state-machine.png) |
| [runtime-claim-timing.puml](runtime-claim-timing.puml) | MVP core / cross-cutting| [SVG](runtime-claim-timing.svg) · [PNG](runtime-claim-timing.png) |
| [runtime-communication-diagram.puml](runtime-communication-diagram.puml) | Method / document navigation| [SVG](runtime-communication-diagram.svg) · [PNG](runtime-communication-diagram.png) |
| [runtime-concurrency-model.puml](runtime-concurrency-model.puml) | MVP core / cross-cutting| [SVG](runtime-concurrency-model.svg) · [PNG](runtime-concurrency-model.png) |
| [runtime-dataflow.puml](runtime-dataflow.puml) | MVP core / cross-cutting| [SVG](runtime-dataflow.svg) · [PNG](runtime-dataflow.png) |
| [runtime-local-command-sequence.puml](runtime-local-command-sequence.puml) | MVP core / cross-cutting| [SVG](runtime-local-command-sequence.svg) · [PNG](runtime-local-command-sequence.png) |
| [runtime-process-deployment.puml](runtime-process-deployment.puml) | MVP deployment| [SVG](runtime-process-deployment.svg) · [PNG](runtime-process-deployment.png) |
| [runtime-process-thread-view.puml](runtime-process-thread-view.puml) | Mixed MVP / future| [SVG](runtime-process-thread-view.svg) · [PNG](runtime-process-thread-view.png) |
| [runtime-queue-topology.puml](runtime-queue-topology.puml) | MVP core / cross-cutting| [SVG](runtime-queue-topology.svg) · [PNG](runtime-queue-topology.png) |
| [runtime-remote-effect-sequence.puml](runtime-remote-effect-sequence.puml) | MVP core / cross-cutting| [SVG](runtime-remote-effect-sequence.svg) · [PNG](runtime-remote-effect-sequence.png) |
| [runtime-resource-contention.puml](runtime-resource-contention.puml) | MVP systems| [SVG](runtime-resource-contention.svg) · [PNG](runtime-resource-contention.png) |
| [runtime-responsibilities.dot](runtime-responsibilities.dot) | Mixed MVP / future| [SVG](runtime-responsibilities.svg) · [PNG](runtime-responsibilities.png) |
| [runtime-swimlane-fork-join.puml](runtime-swimlane-fork-join.puml) | MVP core / cross-cutting| [SVG](runtime-swimlane-fork-join.svg) · [PNG](runtime-swimlane-fork-join.png) |
| [runtime-wait-for-example.puml](runtime-wait-for-example.puml) | MVP core / cross-cutting| [SVG](runtime-wait-for-example.svg) · [PNG](runtime-wait-for-example.png) |

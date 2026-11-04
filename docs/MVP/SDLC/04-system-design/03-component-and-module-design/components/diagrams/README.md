# Resumefolio — Component-Specific Diagrams

Proposed implementation views; not executed product evidence.

Current MVP scope and selected mechanisms: [Baseline](../../../../../baseline/README.md). Deferred provider, advanced collaboration and workflow-execution designs are not MVP prerequisites.

## Manual Applications LC-04

- [Applications owned classes and references](applications-owned-model.svg) · [PlantUML](applications-owned-model.puml) · [PNG](applications-owned-model.png)
- [Actual-material capture coordination](applications-capture-sequence.svg) · [PlantUML](applications-capture-sequence.puml) · [PNG](applications-capture-sequence.png)

[Owning component](../applications.md). Source policy, physical mapping and reference coordination retain their explicit pending decisions.

## Communication and Calendar LC-05

**Release applicability:** future-domain design retained after MVP; core operating/deployment and recovery controls still apply to MVP where relevant.

- [Connection intent and calendar identities](communication-owned-model.svg) · [PlantUML](communication-owned-model.puml) · [PNG](communication-owned-model.png)
- [Reviewed send and uncertain result](communication-send-sequence.svg) · [PlantUML](communication-send-sequence.puml) · [PNG](communication-send-sequence.png)
- [Local/provider calendar reconciliation](calendar-reconciliation-route.svg) · [PlantUML](calendar-reconciliation-route.puml) · [PNG](calendar-reconciliation-route.png)

[Owning component](../communication-and-calendar.md). Proposed contracts; actual provider capability/source-policy acceptance and concrete schema remain explicit gates.

## Files and Operations LC-09

- [Artifact accounting and protected references](files-owned-model.svg) · [PlantUML](files-owned-model.puml) · [PNG](files-owned-model.png)
- [Admission finalization and actual usage](files-admission-sequence.svg) · [PlantUML](files-admission-sequence.puml) · [PNG](files-admission-sequence.png)
- [Reference-aware reclamation guard](files-reclamation-route.svg) · [PlantUML](files-reclamation-route.puml) · [PNG](files-reclamation-route.png)

[Owning component](../files-and-operations.md). Proposed protocols; actual quota values, schema/locking, backend and usable recovery remain pending evidence/decisions.

## Git Collaboration LC-07

- [Repository revision and review identities](git-owned-model.svg) · [PlantUML](git-owned-model.puml) · [PNG](git-owned-model.png)
- [Guarded merge and native/metadata reconciliation](git-merge-sequence.svg) · [PlantUML](git-merge-sequence.puml) · [PNG](git-merge-sequence.png)

[Owning component](../git-collaboration.md). Proposed contracts; engine/transport and concrete cross-store/ref/policy coordination remain evaluated decisions.

## Identity and Access LC-01

- [Account session and scoped authority model](identity-owned-model.svg) · [PlantUML](identity-owned-model.puml) · [PNG](identity-owned-model.png)
- [Current authority and revocation boundary](identity-authorization-sequence.svg) · [PlantUML](identity-authorization-sequence.puml) · [PNG](identity-authorization-sequence.png)

[Owning component](../identity-and-access.md). Proposed enforcement structure; actual administrative policy, credential/session mechanisms and concrete synchronization remain unresolved choices.

## Professional Presentation LC-02

- [Source, independent draft and publication model](presentation-owned-model.svg) · [PlantUML](presentation-owned-model.puml) · [PNG](presentation-owned-model.png)
- [Selected apply and separate publication](presentation-update-publication.svg) · [PlantUML](presentation-update-publication.puml) · [PNG](presentation-update-publication.png)

[Owning component](../professional-presentation.md). Proposed technical realization of the accepted update/publication core; detailed source policies and concrete persistence/reference mechanisms retain review status.

## Representation and Sharing LC-03

- [Independent access and rendition state](sharing-owned-model.svg) · [PlantUML](sharing-owned-model.puml) · [PNG](sharing-owned-model.png)
- [Current-authority protected retrieval](sharing-protected-retrieval.svg) · [PlantUML](sharing-protected-retrieval.puml) · [PNG](sharing-protected-retrieval.png)

[Owning component](../representation-and-sharing.md). Proposed representation and protected retrieval mechanisms; detailed link/session/rendition policies and serving synchronization retain review status.

## Work Management LC-06

- [Work views and coherent Sprint Backlog](work-owned-model.svg) · [PlantUML](work-owned-model.puml) · [PNG](work-owned-model.png)
- [Guarded mutation and explicit Sprint-period close](work-mutation-sprint-close.svg) · [PlantUML](work-mutation-sprint-close.puml) · [PNG](work-mutation-sprint-close.png)

[Owning component](../work-management.md). Proposed work and Sprint mechanisms; detailed workflow, role, cardinality and disposition policies retain review status.

## Workflow and Deployment LC-08

**Release applicability:** future-domain design retained after MVP; core operating/deployment and recovery controls still apply to MVP where relevant.

- [Coordination and execution trust boundaries](workflow-trust-model.svg) · [PlantUML](workflow-trust-model.puml) · [PNG](workflow-trust-model.png)
- [Separate deployment and effect reconciliation](workflow-deployment-sequence.svg) · [PlantUML](workflow-deployment-sequence.puml) · [PNG](workflow-deployment-sequence.png)

[Owning component](../workflow-and-deployment.md). Proposed gated execution and separately authorized deployment; actual isolation, capacity, cleanup and recovery evidence remain enabling gates.

## Applications context and logical landscape package

- [Provided and required component interfaces](applications-interfaces.svg) · [PlantUML](applications-interfaces.puml) · [PNG](applications-interfaces.png)
- [C4 Level 1: Resumefolio system context](../../../01-software-architecture/diagrams/drivers-c4-system-context.svg) · [PlantUML](../../../01-software-architecture/diagrams/drivers-c4-system-context.puml) · [PNG](../../../01-software-architecture/diagrams/drivers-c4-system-context.png)
- [C4 Level 2: modular application and stores](../../../01-software-architecture/diagrams/boundaries-c4-containers.svg) · [PlantUML](../../../01-software-architecture/diagrams/boundaries-c4-containers.puml) · [PNG](../../../01-software-architecture/diagrams/boundaries-c4-containers.png)
- [Logical capability landscape](../../../../03-system-analysis/diagrams/scope-stakeholder-map.svg) · [PlantUML](../../../../03-system-analysis/diagrams/scope-stakeholder-map.puml) · [PNG](../../../../03-system-analysis/diagrams/scope-stakeholder-map.png)
- [Applications inbound and outbound dependencies](applications-dependencies.svg) · [PlantUML](applications-dependencies.puml) · [PNG](applications-dependencies.png)
- [Applications layered architecture](applications-layers.svg) · [PlantUML](applications-layers.puml) · [PNG](applications-layers.png)
- [Internal responsibility areas within LC-04](applications-internal-structure.svg) · [PlantUML](applications-internal-structure.puml) · [PNG](applications-internal-structure.png)
- [Candidate package dependencies](applications-packages.svg) · [PlantUML](applications-packages.puml) · [PNG](applications-packages.png)
- [Integration types and evidence boundaries](applications-integration.svg) · [PlantUML](applications-integration.puml) · [PNG](applications-integration.png)
- [Actual submission capture across owner contracts](applications-cross-owner-sequence.svg) · [PlantUML](applications-cross-owner-sequence.puml) · [PNG](applications-cross-owner-sequence.png)
- [UML use cases for the manual Applications capability](applications-use-cases.svg) · [PlantUML](applications-use-cases.puml) · [PNG](applications-use-cases.png)
- [Optional deployment mapping of logical roles](../../../01-software-architecture/diagrams/drivers-uml-deployment.svg) · [PlantUML](../../../01-software-architecture/diagrams/drivers-uml-deployment.puml) · [PNG](../../../01-software-architecture/diagrams/drivers-uml-deployment.png)

[Owning LC-04 document, inventory/capability/interface/stack/data/quality/lifecycle tables and decision note](../applications.md#7-application-context-and-landscape-package). Applications means manual job applications; logical neighbors are not separate deployed software applications.

## Communication and calendar expanded package

**Release applicability:** future-domain design retained after MVP; core operating/deployment and recovery controls still apply to MVP where relevant.

- [Communication and calendar interfaces](comm-interfaces.svg) · [PlantUML](comm-interfaces.puml) · [PNG](comm-interfaces.png)
- [C4 Level 1: users and external provider](../../../../02-requirements-engineering/diagrams/use-cases-mail-and-calendar.svg) · [PlantUML](../../../../02-requirements-engineering/diagrams/use-cases-mail-and-calendar.puml) · [PNG](../../../../02-requirements-engineering/diagrams/use-cases-mail-and-calendar.png)
- [C4 Level 2: actual proposed runtime boundaries](../../../../02-requirements-engineering/diagrams/use-cases-mail-and-calendar.svg) · [PlantUML](../../../../02-requirements-engineering/diagrams/use-cases-mail-and-calendar.puml) · [PNG](../../../../02-requirements-engineering/diagrams/use-cases-mail-and-calendar.png)
- [Owner communication and calendar use cases](comm-use-cases.svg) · [PlantUML](comm-use-cases.puml) · [PNG](comm-use-cases.png)
- [Domain classes and optional requested concepts](comm-domain.svg) · [PlantUML](comm-domain.puml) · [PNG](comm-domain.png)
- [Logical ERD: owned and observed records](comm-erd.svg) · [PlantUML](comm-erd.puml) · [PNG](comm-erd.png)
- [Reviewed send and delivery observations](comm-send.svg) · [PlantUML](comm-send.puml) · [PNG](comm-send.png)
- [Conditional event creation and attendee response](comm-invitation.svg) · [PlantUML](comm-invitation.puml) · [PNG](comm-invitation.png)
- [Reminder trigger and actual notification outcome](comm-reminder.svg) · [PlantUML](comm-reminder.puml) · [PNG](comm-reminder.png)
- [Message and send knowledge: distinct dimensions](comm-message-state.svg) · [PlantUML](comm-message-state.puml) · [PNG](comm-message-state.png)
- [Event status and attendee response dimensions](comm-event-state.svg) · [PlantUML](comm-event-state.puml) · [PNG](comm-event-state.png)
- [Conditional scheduling and conflict detection](comm-scheduling.svg) · [PlantUML](comm-scheduling.puml) · [PNG](comm-scheduling.png)
- [Bounded recurrence expansion and exception identity](comm-recurrence.svg) · [PlantUML](comm-recurrence.puml) · [PNG](comm-recurrence.png)
- [Logical work flow and channel eligibility](comm-notification-flow.svg) · [PlantUML](comm-notification-flow.puml) · [PNG](comm-notification-flow.png)
- [Selected scope versus protocol alternatives](comm-integration-options.svg) · [PlantUML](comm-integration-options.puml) · [PNG](comm-integration-options.png)
- [Conditional free-busy lookup](comm-free-busy.svg) · [PlantUML](comm-free-busy.puml) · [PNG](comm-free-busy.png)
- [Conditional calendar reconciliation and conflict resolution](comm-sync.svg) · [PlantUML](comm-sync.puml) · [PNG](comm-sync.png)
- [Optional trusted runtime placement](../../../../02-requirements-engineering/diagrams/use-cases-mail-and-calendar.svg) · [PlantUML](../../../../02-requirements-engineering/diagrams/use-cases-mail-and-calendar.puml) · [PNG](../../../../02-requirements-engineering/diagrams/use-cases-mail-and-calendar.png)

[Owning LC-05 document and seven time/interface/channel/ownership/privacy/failure/quality tables](../communication-and-calendar.md#8-communication-calendar-and-delivery-view-package). Unselected protocols/channels and conditional invitation/free-busy behavior are not new accepted capabilities.

## Files and Operations expanded package

- [Files provided and required interfaces](files-interfaces.svg) · [PlantUML](files-interfaces.puml) · [PNG](files-interfaces.png)
- [C4 Level 1: artifact-related system context](files-context.svg) · [PlantUML](files-context.puml) · [PNG](files-context.png)
- [C4 Level 2: modular runtime and storage](files-context.svg) · [PlantUML](files-context.puml) · [PNG](files-context.png)
- [Artifact operations and separately owned sharing](files-use-cases.svg) · [PlantUML](files-use-cases.puml) · [PNG](files-use-cases.png)
- [Artifact, reference and operation classes](files-domain.svg) · [PlantUML](files-domain.puml) · [PNG](files-domain.png)
- [Logical artifact and ledger relationships](files-erd.svg) · [PlantUML](files-erd.puml) · [PNG](files-erd.png)
- [Upload with conditional resumable transport](files-upload.svg) · [PlantUML](files-upload.puml) · [PNG](files-upload.png)
- [Exact download and current access admission](files-download.svg) · [PlantUML](files-download.puml) · [PNG](files-download.png)
- [Share link creation and access through its owner](files-share.svg) · [PlantUML](files-share.puml) · [PNG](files-share.png)
- [Artifact usability, lifecycle and presence dimensions](files-artifact-state.svg) · [PlantUML](files-artifact-state.puml) · [PNG](files-artifact-state.png)
- [Operation and job knowledge states](files-job-state.svg) · [PlantUML](files-job-state.puml) · [PNG](files-job-state.png)
- [Private candidate processing pipeline](files-pipeline.svg) · [PlantUML](files-pipeline.puml) · [PNG](files-pipeline.png)
- [Concurrent reference replacement conflict resolution](files-concurrent-edits.svg) · [PlantUML](files-concurrent-edits.puml) · [PNG](files-concurrent-edits.png)
- [Storage architecture options and unselected tiers](files-context.svg) · [PlantUML](files-context.puml) · [PNG](files-context.png)
- [Logical hierarchy versus canonical storage identity](files-paths.svg) · [PlantUML](files-paths.puml) · [PNG](files-paths.png)
- [Version, trash, restore and physical reclaim flow](files-trash.svg) · [PlantUML](files-trash.puml) · [PNG](files-trash.png)
- [Logical job lanes, reconciliation and intervention](files-queues.svg) · [PlantUML](files-queues.puml) · [PNG](files-queues.png)
- [Storage and sync integration options](files-context.svg) · [PlantUML](files-context.puml) · [PNG](files-context.png)
- [Optional deployment mapping for Files capabilities](../../../01-software-architecture/diagrams/drivers-uml-deployment.svg) · [PlantUML](../../../01-software-architecture/diagrams/drivers-uml-deployment.puml) · [PNG](../../../01-software-architecture/diagrams/drivers-uml-deployment.png)

[Owning LC-09 document and seven interface/permission/audit/policy/failure/ownership/quality tables](../files-and-operations.md#8-files-storage-and-operations-view-package). Conditional folder/transport/backend/processing views are not new scope or installed facilities.

## Essential Git collaboration views

- [Native Git objects and references](git-essential-objects.svg) · [PlantUML](git-essential-objects.puml) · [PNG](git-essential-objects.png)
- [Commit graph: branches, merge and tag](git-essential-graph.svg) · [PlantUML](git-essential-graph.puml) · [PNG](git-essential-graph.png)
- [Candidate short-lived branch and guarded integration flow](git-essential-branching.svg) · [PlantUML](git-essential-branching.puml) · [PNG](git-essential-branching.png)
- [Pull request lifecycle and revision-bound readiness](git-essential-pr-state.svg) · [PlantUML](git-essential-pr-state.puml) · [PNG](git-essential-pr-state.png)
- [Push, checks, review and guarded merge](git-essential-pr-sequence.svg) · [PlantUML](git-essential-pr-sequence.puml) · [PNG](git-essential-pr-sequence.png)
- [Repository and collaboration identity model](git-essential-domain.svg) · [PlantUML](git-essential-domain.puml) · [PNG](git-essential-domain.png)
- [Git and collaboration capability boundaries](git-essential-components.svg) · [PlantUML](git-essential-components.puml) · [PNG](git-essential-components.png)

[Owning LC-07 essential package and permission matrix](../git-collaboration.md#7-essential-git-and-collaboration-views). Seven selected views only; native facts do not select engine, branching, review or transport policies.

## Essential Identity and Access views

- [Identity responsibilities and scoped contracts](identity-essential-components.svg) · [PlantUML](identity-essential-components.puml) · [PNG](identity-essential-components.png)
- [Authentication and conditional second factor](identity-essential-authentication.svg) · [PlantUML](identity-essential-authentication.puml) · [PNG](identity-essential-authentication.png)
- [Authorization decision and enforcement flow](identity-essential-authorization.svg) · [PlantUML](identity-essential-authorization.puml) · [PNG](identity-essential-authorization.png)
- [Scoped roles, attributes and resource ownership](identity-essential-access-model.svg) · [PlantUML](identity-essential-access-model.puml) · [PNG](identity-essential-access-model.png)
- [Session lifecycle and separate credential scopes](identity-essential-session-state.svg) · [PlantUML](identity-essential-session-state.puml) · [PNG](identity-essential-session-state.png)
- [Clients, trusted application and external scopes](../../../06-design-quality-and-security-analysis/diagrams/security-trust-boundaries.svg) · [PlantUML](../../../06-design-quality-and-security-analysis/diagrams/security-trust-boundaries.puml) · [PNG](../../../06-design-quality-and-security-analysis/diagrams/security-trust-boundaries.png)

[Owning LC-01 essential package and scope rationale](../identity-and-access.md#7-essential-identity-and-access-views). Reuses the existing domain model; federation and role hierarchy are not selected.

## Essential Professional Presentation views

- [Presentation ownership and provided/required contracts](presentation-essential-components.svg) · [PlantUML](presentation-essential-components.puml) · [PNG](presentation-essential-components.png)
- [Essential owner and viewer intentions](presentation-essential-use-cases.svg) · [PlantUML](presentation-essential-use-cases.puml) · [PNG](presentation-essential-use-cases.png)
- [Draft, preview and immutable publication dimensions](presentation-essential-lifecycle.svg) · [PlantUML](presentation-essential-lifecycle.puml) · [PNG](presentation-essential-lifecycle.png)
- [Visitor resolves an exact eligible publication](presentation-essential-visitor.svg) · [PlantUML](presentation-essential-visitor.puml) · [PNG](presentation-essential-visitor.png)
- [Version-bound rendering inputs and separate outputs](presentation-essential-rendering.svg) · [PlantUML](presentation-essential-rendering.puml) · [PNG](presentation-essential-rendering.png)

[Owning LC-02 essential package](../professional-presentation.md#7-essential-presentation-views). Reuses existing domain and update/publication diagrams; no speculative CDN, analytics or social sync selection.

## Essential Representation and Sharing views

- [Representation and sharing contracts](sharing-essential-components.svg) · [PlantUML](sharing-essential-components.puml) · [PNG](sharing-essential-components.png)
- [Essential representation routes](sharing-essential-formats.svg) · [PlantUML](sharing-essential-formats.puml) · [PNG](sharing-essential-formats.png)
- [Link eligibility and viewer generation](sharing-essential-link-state.svg) · [PlantUML](sharing-essential-link-state.puml) · [PNG](sharing-essential-link-state.png)
- [Create link, verify viewer and admit exact retrieval](sharing-essential-link-sequence.svg) · [PlantUML](sharing-essential-link-sequence.puml) · [PNG](sharing-essential-link-sequence.png)

[Owning LC-03 essential package and two control tables](../representation-and-sharing.md#7-essential-representation-and-sharing-views). Existing domain/retrieval views reused; no speculative channel, audience, CDN or export integration selected.

## Essential Work Management views

- [Work ownership and scoped interfaces](work-essential-views.svg) · [PlantUML](work-essential-views.puml) · [PNG](work-essential-views.png)
- [Candidate task lifecycle versus acceptance](work-essential-task-state.svg) · [PlantUML](work-essential-task-state.puml) · [PNG](work-essential-task-state.png)
- [Guarded work creation, assignment and transition](work-essential-transition.svg) · [PlantUML](work-essential-transition.puml) · [PNG](work-essential-transition.png)
- [One authoritative work model, multiple permitted projections](work-essential-views.svg) · [PlantUML](work-essential-views.puml) · [PNG](work-essential-views.png)
- [Coherent Sprint planning, execution and review](work-essential-sprint-planning.svg) · [PlantUML](work-essential-sprint-planning.puml) · [PNG](work-essential-sprint-planning.png)

[Owning LC-06 essential package and scoped permission/integration tables](../work-management.md#7-essential-work-management-views). Existing domain/mutation views reused; no extra generic workflow or automation scope selected.

## Workflow, executor and deployment views

**Release applicability:** future-domain design retained after MVP; core operating/deployment and recovery controls still apply to MVP where relevant.

- [Coordination, executor and target contracts](workflow-essential-components.svg) · [PlantUML](workflow-essential-components.puml) · [PNG](workflow-essential-components.png)
- [Candidate CI/CD path with distinct execution and deployment gates](workflow-essential-pipeline.svg) · [PlantUML](workflow-essential-pipeline.puml) · [PNG](workflow-essential-pipeline.png)
- [Run observation, cancellation and cleanup dimensions](workflow-essential-run-state.svg) · [PlantUML](workflow-essential-run-state.puml) · [PNG](workflow-essential-run-state.png)
- [Deployment approval and actual target outcome](workflow-essential-deployment-state.svg) · [PlantUML](workflow-essential-deployment-state.puml) · [PNG](workflow-essential-deployment-state.png)
- [Deployment strategy alternatives, not a selection](workflow-essential-strategies.svg) · [PlantUML](workflow-essential-strategies.puml) · [PNG](workflow-essential-strategies.png)
- [Failed verification and safe recovery decision](workflow-essential-recovery.svg) · [PlantUML](workflow-essential-recovery.puml) · [PNG](workflow-essential-recovery.png)
- [Conditional environment promotion and exact approval gates](workflow-essential-promotion.svg) · [PlantUML](workflow-essential-promotion.puml) · [PNG](workflow-essential-promotion.png)
- [Runner architecture and trust isolation](workflow-essential-executor.svg) · [PlantUML](workflow-essential-executor.puml) · [PNG](workflow-essential-executor.png)
- [Candidate executor and deployment placement](workflow-essential-topology.svg) · [PlantUML](workflow-essential-topology.puml) · [PNG](workflow-essential-topology.png)

[Owning LC-08 package and scoped target-approval matrix](../workflow-and-deployment.md#8-workflow-executor-and-deployment-views). Existing domain/deployment sequence reused; isolation, strategy, topology and approval gates are not completed by diagrams.

## November 4 release applicability

Current MVP figures replace the former common-product boundary. Future and historical figures retain their details without committing them to MVP.

| Editable source | Current applicability |
| --- | --- |
| [applications-containers.puml](../../../01-software-architecture/diagrams/boundaries-c4-containers.puml) | MVP systems|
| [applications-deployment.puml](../../../01-software-architecture/diagrams/drivers-uml-deployment.puml) | MVP deployment|
| [applications-integration.puml](applications-integration.puml) | MVP core / cross-cutting|
| [calendar-reconciliation-route.puml](calendar-reconciliation-route.puml) | Future after MVP|
| [comm-deployment.puml](../../../../02-requirements-engineering/diagrams/use-cases-mail-and-calendar.puml) | Future communications|
| [communication-owned-model.puml](communication-owned-model.puml) | Future after MVP|
| [communication-send-sequence.puml](communication-send-sequence.puml) | Future after MVP|
| [files-deployment.puml](../../../01-software-architecture/diagrams/drivers-uml-deployment.puml) | MVP deployment|
| [identity-essential-trust-boundaries.puml](../../../06-design-quality-and-security-analysis/diagrams/security-trust-boundaries.puml) | MVP systems|
| [work-essential-sprint-planning.puml](work-essential-sprint-planning.puml) | Future after MVP|
| [work-mutation-sprint-close.puml](work-mutation-sprint-close.puml) | Future after MVP|
| [workflow-deployment-sequence.puml](workflow-deployment-sequence.puml) | Future after MVP|
| [workflow-essential-components.puml](workflow-essential-components.puml) | Future after MVP|
| [workflow-essential-deployment-state.puml](workflow-essential-deployment-state.puml) | Future after MVP|
| [workflow-essential-executor.puml](workflow-essential-executor.puml) | Future after MVP|
| [workflow-essential-pipeline.puml](workflow-essential-pipeline.puml) | Future after MVP|
| [workflow-essential-promotion.puml](workflow-essential-promotion.puml) | Future after MVP|
| [workflow-essential-recovery.puml](workflow-essential-recovery.puml) | Future after MVP|
| [workflow-essential-run-state.puml](workflow-essential-run-state.puml) | Future after MVP|
| [workflow-essential-strategies.puml](workflow-essential-strategies.puml) | Future after MVP|
| [workflow-essential-topology.puml](workflow-essential-topology.puml) | Future after MVP|
| [workflow-trust-model.puml](workflow-trust-model.puml) | Future after MVP|

| [applications-portfolio.puml](../../../../03-system-analysis/diagrams/scope-stakeholder-map.puml) | MVP systems|
| [comm-containers.puml](../../../../02-requirements-engineering/diagrams/use-cases-mail-and-calendar.puml) | Future communications|
| [comm-context.puml](../../../../02-requirements-engineering/diagrams/use-cases-mail-and-calendar.puml) | Future communications|
| [comm-domain.puml](comm-domain.puml) | Future after MVP|
| [comm-erd.puml](comm-erd.puml) | Future after MVP|
| [comm-event-state.puml](comm-event-state.puml) | Future after MVP|
| [comm-free-busy.puml](comm-free-busy.puml) | Future after MVP|
| [comm-integration-options.puml](comm-integration-options.puml) | Future after MVP|
| [comm-interfaces.puml](comm-interfaces.puml) | Future after MVP|
| [comm-invitation.puml](comm-invitation.puml) | Future after MVP|
| [comm-message-state.puml](comm-message-state.puml) | Future after MVP|
| [comm-notification-flow.puml](comm-notification-flow.puml) | Future after MVP|
| [comm-recurrence.puml](comm-recurrence.puml) | Future after MVP|
| [comm-reminder.puml](comm-reminder.puml) | Future after MVP|
| [comm-scheduling.puml](comm-scheduling.puml) | Future after MVP|
| [comm-send.puml](comm-send.puml) | Future after MVP|
| [comm-sync.puml](comm-sync.puml) | Future after MVP|
| [comm-use-cases.puml](comm-use-cases.puml) | Future after MVP|
| [git-essential-components.puml](git-essential-components.puml) | MVP ProjectForge|
| [git-essential-domain.puml](git-essential-domain.puml) | Future after MVP|
| [git-essential-pr-sequence.puml](git-essential-pr-sequence.puml) | Future after MVP|
| [git-essential-pr-state.puml](git-essential-pr-state.puml) | Future after MVP|
| [git-merge-sequence.puml](git-merge-sequence.puml) | Future after MVP|
| [git-owned-model.puml](git-owned-model.puml) | Future after MVP|
| [work-essential-components.puml](work-essential-views.puml) | MVP ProjectForge|
| [work-essential-task-state.puml](work-essential-task-state.puml) | Future after MVP|
| [work-essential-views.puml](work-essential-views.puml) | MVP ProjectForge|
| [work-owned-model.puml](work-owned-model.puml) | Future after MVP|

## Complete diagram alignment — November 4

[Full project inventory and verification limits](../../../01-software-architecture/diagrams/README.md). This current disposition supersedes earlier partial diagram-allocation lists.

| Editable source or visual | Current applicability | Matching exports |
| --- | --- | --- |
| [applications-capture-sequence.puml](applications-capture-sequence.puml) | MVP core / cross-cutting| [SVG](applications-capture-sequence.svg) · [PNG](applications-capture-sequence.png) |
| [applications-containers.puml](../../../01-software-architecture/diagrams/boundaries-c4-containers.puml) | MVP systems| [SVG](../../../01-software-architecture/diagrams/boundaries-c4-containers.svg) · [PNG](../../../01-software-architecture/diagrams/boundaries-c4-containers.png) |
| [applications-cross-owner-sequence.puml](applications-cross-owner-sequence.puml) | MVP core / cross-cutting| [SVG](applications-cross-owner-sequence.svg) · [PNG](applications-cross-owner-sequence.png) |
| [applications-dependencies.puml](applications-dependencies.puml) | MVP core / cross-cutting| [SVG](applications-dependencies.svg) · [PNG](applications-dependencies.png) |
| [applications-deployment.puml](../../../01-software-architecture/diagrams/drivers-uml-deployment.puml) | MVP deployment| [SVG](../../../01-software-architecture/diagrams/drivers-uml-deployment.svg) · [PNG](../../../01-software-architecture/diagrams/drivers-uml-deployment.png) |
| [applications-integration.puml](applications-integration.puml) | MVP core / cross-cutting| [SVG](applications-integration.svg) · [PNG](applications-integration.png) |
| [applications-interfaces.puml](applications-interfaces.puml) | MVP core / cross-cutting| [SVG](applications-interfaces.svg) · [PNG](applications-interfaces.png) |
| [applications-internal-structure.puml](applications-internal-structure.puml) | MVP core| [SVG](applications-internal-structure.svg) · [PNG](applications-internal-structure.png) |
| [applications-layers.puml](applications-layers.puml) | MVP core / cross-cutting| [SVG](applications-layers.svg) · [PNG](applications-layers.png) |
| [applications-owned-model.puml](applications-owned-model.puml) | MVP core| [SVG](applications-owned-model.svg) · [PNG](applications-owned-model.png) |
| [applications-packages.puml](applications-packages.puml) | MVP core / cross-cutting| [SVG](applications-packages.svg) · [PNG](applications-packages.png) |
| [applications-portfolio.puml](../../../../03-system-analysis/diagrams/scope-stakeholder-map.puml) | MVP systems| [SVG](../../../../03-system-analysis/diagrams/scope-stakeholder-map.svg) · [PNG](../../../../03-system-analysis/diagrams/scope-stakeholder-map.png) |
| [applications-system-context.puml](../../../01-software-architecture/diagrams/drivers-c4-system-context.puml) | MVP systems| [SVG](../../../01-software-architecture/diagrams/drivers-c4-system-context.svg) · [PNG](../../../01-software-architecture/diagrams/drivers-c4-system-context.png) |
| [applications-use-cases.puml](applications-use-cases.puml) | MVP core / cross-cutting| [SVG](applications-use-cases.svg) · [PNG](applications-use-cases.png) |
| [calendar-reconciliation-route.puml](calendar-reconciliation-route.puml) | Future after MVP| [SVG](calendar-reconciliation-route.svg) · [PNG](calendar-reconciliation-route.png) |
| [comm-containers.puml](../../../../02-requirements-engineering/diagrams/use-cases-mail-and-calendar.puml) | Future communications| [SVG](../../../../02-requirements-engineering/diagrams/use-cases-mail-and-calendar.svg) · [PNG](../../../../02-requirements-engineering/diagrams/use-cases-mail-and-calendar.png) |
| [comm-context.puml](../../../../02-requirements-engineering/diagrams/use-cases-mail-and-calendar.puml) | Future communications| [SVG](../../../../02-requirements-engineering/diagrams/use-cases-mail-and-calendar.svg) · [PNG](../../../../02-requirements-engineering/diagrams/use-cases-mail-and-calendar.png) |
| [comm-deployment.puml](../../../../02-requirements-engineering/diagrams/use-cases-mail-and-calendar.puml) | Future communications| [SVG](../../../../02-requirements-engineering/diagrams/use-cases-mail-and-calendar.svg) · [PNG](../../../../02-requirements-engineering/diagrams/use-cases-mail-and-calendar.png) |
| [comm-domain.puml](comm-domain.puml) | Future after MVP| [SVG](comm-domain.svg) · [PNG](comm-domain.png) |
| [comm-erd.puml](comm-erd.puml) | Future after MVP| [SVG](comm-erd.svg) · [PNG](comm-erd.png) |
| [comm-event-state.puml](comm-event-state.puml) | Future after MVP| [SVG](comm-event-state.svg) · [PNG](comm-event-state.png) |
| [comm-free-busy.puml](comm-free-busy.puml) | Future after MVP| [SVG](comm-free-busy.svg) · [PNG](comm-free-busy.png) |
| [comm-integration-options.puml](comm-integration-options.puml) | Future after MVP| [SVG](comm-integration-options.svg) · [PNG](comm-integration-options.png) |
| [comm-interfaces.puml](comm-interfaces.puml) | Future after MVP| [SVG](comm-interfaces.svg) · [PNG](comm-interfaces.png) |
| [comm-invitation.puml](comm-invitation.puml) | Future after MVP| [SVG](comm-invitation.svg) · [PNG](comm-invitation.png) |
| [comm-message-state.puml](comm-message-state.puml) | Future after MVP| [SVG](comm-message-state.svg) · [PNG](comm-message-state.png) |
| [comm-notification-flow.puml](comm-notification-flow.puml) | Future after MVP| [SVG](comm-notification-flow.svg) · [PNG](comm-notification-flow.png) |
| [comm-recurrence.puml](comm-recurrence.puml) | Future after MVP| [SVG](comm-recurrence.svg) · [PNG](comm-recurrence.png) |
| [comm-reminder.puml](comm-reminder.puml) | Future after MVP| [SVG](comm-reminder.svg) · [PNG](comm-reminder.png) |
| [comm-scheduling.puml](comm-scheduling.puml) | Future after MVP| [SVG](comm-scheduling.svg) · [PNG](comm-scheduling.png) |
| [comm-send.puml](comm-send.puml) | Future after MVP| [SVG](comm-send.svg) · [PNG](comm-send.png) |
| [comm-sync.puml](comm-sync.puml) | Future after MVP| [SVG](comm-sync.svg) · [PNG](comm-sync.png) |
| [comm-use-cases.puml](comm-use-cases.puml) | Future after MVP| [SVG](comm-use-cases.svg) · [PNG](comm-use-cases.png) |
| [communication-owned-model.puml](communication-owned-model.puml) | Future after MVP| [SVG](communication-owned-model.svg) · [PNG](communication-owned-model.png) |
| [communication-send-sequence.puml](communication-send-sequence.puml) | Future after MVP| [SVG](communication-send-sequence.svg) · [PNG](communication-send-sequence.png) |
| [files-admission-sequence.puml](files-admission-sequence.puml) | MVP core / cross-cutting| [SVG](files-admission-sequence.svg) · [PNG](files-admission-sequence.png) |
| [files-artifact-state.puml](files-artifact-state.puml) | MVP core / cross-cutting| [SVG](files-artifact-state.svg) · [PNG](files-artifact-state.png) |
| [files-concurrent-edits.puml](files-concurrent-edits.puml) | MVP core / cross-cutting| [SVG](files-concurrent-edits.svg) · [PNG](files-concurrent-edits.png) |
| [files-containers.puml](files-context.puml) | MVP core media| [SVG](files-context.svg) · [PNG](files-context.png) |
| [files-context.puml](files-context.puml) | MVP core media| [SVG](files-context.svg) · [PNG](files-context.png) |
| [files-deployment.puml](../../../01-software-architecture/diagrams/drivers-uml-deployment.puml) | MVP deployment| [SVG](../../../01-software-architecture/diagrams/drivers-uml-deployment.svg) · [PNG](../../../01-software-architecture/diagrams/drivers-uml-deployment.png) |
| [files-domain.puml](files-domain.puml) | MVP core / cross-cutting| [SVG](files-domain.svg) · [PNG](files-domain.png) |
| [files-download.puml](files-download.puml) | MVP core / cross-cutting| [SVG](files-download.svg) · [PNG](files-download.png) |
| [files-erd.puml](files-erd.puml) | MVP core / cross-cutting| [SVG](files-erd.svg) · [PNG](files-erd.png) |
| [files-integrations.puml](files-context.puml) | MVP core media| [SVG](files-context.svg) · [PNG](files-context.png) |
| [files-interfaces.puml](files-interfaces.puml) | MVP core / cross-cutting| [SVG](files-interfaces.svg) · [PNG](files-interfaces.png) |
| [files-job-state.puml](files-job-state.puml) | MVP core / cross-cutting| [SVG](files-job-state.svg) · [PNG](files-job-state.png) |
| [files-owned-model.puml](files-owned-model.puml) | MVP core / cross-cutting| [SVG](files-owned-model.svg) · [PNG](files-owned-model.png) |
| [files-paths.puml](files-paths.puml) | MVP core / cross-cutting| [SVG](files-paths.svg) · [PNG](files-paths.png) |
| [files-pipeline.puml](files-pipeline.puml) | MVP core / cross-cutting| [SVG](files-pipeline.svg) · [PNG](files-pipeline.png) |
| [files-queues.puml](files-queues.puml) | MVP core / cross-cutting| [SVG](files-queues.svg) · [PNG](files-queues.png) |
| [files-reclamation-route.puml](files-reclamation-route.puml) | MVP core / cross-cutting| [SVG](files-reclamation-route.svg) · [PNG](files-reclamation-route.png) |
| [files-share.puml](files-share.puml) | MVP core / cross-cutting| [SVG](files-share.svg) · [PNG](files-share.png) |
| [files-storage-options.puml](files-context.puml) | MVP core media| [SVG](files-context.svg) · [PNG](files-context.png) |
| [files-trash.puml](files-trash.puml) | MVP core / cross-cutting| [SVG](files-trash.svg) · [PNG](files-trash.png) |
| [files-upload.puml](files-upload.puml) | MVP core / cross-cutting| [SVG](files-upload.svg) · [PNG](files-upload.png) |
| [files-use-cases.puml](files-use-cases.puml) | MVP core / cross-cutting| [SVG](files-use-cases.svg) · [PNG](files-use-cases.png) |
| [git-essential-branching.puml](git-essential-branching.puml) | Future after MVP| [SVG](git-essential-branching.svg) · [PNG](git-essential-branching.png) |
| [git-essential-components.puml](git-essential-components.puml) | MVP ProjectForge| [SVG](git-essential-components.svg) · [PNG](git-essential-components.png) |
| [git-essential-domain.puml](git-essential-domain.puml) | Future after MVP| [SVG](git-essential-domain.svg) · [PNG](git-essential-domain.png) |
| [git-essential-graph.puml](git-essential-graph.puml) | Reference / design method| [SVG](git-essential-graph.svg) · [PNG](git-essential-graph.png) |
| [git-essential-objects.puml](git-essential-objects.puml) | Reference / design method| [SVG](git-essential-objects.svg) · [PNG](git-essential-objects.png) |
| [git-essential-pr-sequence.puml](git-essential-pr-sequence.puml) | Future after MVP| [SVG](git-essential-pr-sequence.svg) · [PNG](git-essential-pr-sequence.png) |
| [git-essential-pr-state.puml](git-essential-pr-state.puml) | Future after MVP| [SVG](git-essential-pr-state.svg) · [PNG](git-essential-pr-state.png) |
| [git-merge-sequence.puml](git-merge-sequence.puml) | Future after MVP| [SVG](git-merge-sequence.svg) · [PNG](git-merge-sequence.png) |
| [git-owned-model.puml](git-owned-model.puml) | Future after MVP| [SVG](git-owned-model.svg) · [PNG](git-owned-model.png) |
| [identity-authorization-sequence.puml](identity-authorization-sequence.puml) | MVP core / cross-cutting| [SVG](identity-authorization-sequence.svg) · [PNG](identity-authorization-sequence.png) |
| [identity-essential-access-model.puml](identity-essential-access-model.puml) | MVP core / cross-cutting| [SVG](identity-essential-access-model.svg) · [PNG](identity-essential-access-model.png) |
| [identity-essential-authentication.puml](identity-essential-authentication.puml) | MVP core / cross-cutting| [SVG](identity-essential-authentication.svg) · [PNG](identity-essential-authentication.png) |
| [identity-essential-authorization.puml](identity-essential-authorization.puml) | MVP core / cross-cutting| [SVG](identity-essential-authorization.svg) · [PNG](identity-essential-authorization.png) |
| [identity-essential-components.puml](identity-essential-components.puml) | MVP core / cross-cutting| [SVG](identity-essential-components.svg) · [PNG](identity-essential-components.png) |
| [identity-essential-session-state.puml](identity-essential-session-state.puml) | MVP core / cross-cutting| [SVG](identity-essential-session-state.svg) · [PNG](identity-essential-session-state.png) |
| [identity-essential-trust-boundaries.puml](../../../06-design-quality-and-security-analysis/diagrams/security-trust-boundaries.puml) | MVP systems| [SVG](../../../06-design-quality-and-security-analysis/diagrams/security-trust-boundaries.svg) · [PNG](../../../06-design-quality-and-security-analysis/diagrams/security-trust-boundaries.png) |
| [identity-owned-model.puml](identity-owned-model.puml) | MVP core / cross-cutting| [SVG](identity-owned-model.svg) · [PNG](identity-owned-model.png) |
| [presentation-essential-components.puml](presentation-essential-components.puml) | MVP core / cross-cutting| [SVG](presentation-essential-components.svg) · [PNG](presentation-essential-components.png) |
| [presentation-essential-lifecycle.puml](presentation-essential-lifecycle.puml) | MVP core / cross-cutting| [SVG](presentation-essential-lifecycle.svg) · [PNG](presentation-essential-lifecycle.png) |
| [presentation-essential-rendering.puml](presentation-essential-rendering.puml) | MVP core / cross-cutting| [SVG](presentation-essential-rendering.svg) · [PNG](presentation-essential-rendering.png) |
| [presentation-essential-use-cases.puml](presentation-essential-use-cases.puml) | MVP core / cross-cutting| [SVG](presentation-essential-use-cases.svg) · [PNG](presentation-essential-use-cases.png) |
| [presentation-essential-visitor.puml](presentation-essential-visitor.puml) | MVP core / cross-cutting| [SVG](presentation-essential-visitor.svg) · [PNG](presentation-essential-visitor.png) |
| [presentation-owned-model.puml](presentation-owned-model.puml) | MVP core / cross-cutting| [SVG](presentation-owned-model.svg) · [PNG](presentation-owned-model.png) |
| [presentation-update-publication.puml](presentation-update-publication.puml) | MVP core / cross-cutting| [SVG](presentation-update-publication.svg) · [PNG](presentation-update-publication.png) |
| [sharing-essential-components.puml](sharing-essential-components.puml) | MVP core / cross-cutting| [SVG](sharing-essential-components.svg) · [PNG](sharing-essential-components.png) |
| [sharing-essential-formats.puml](sharing-essential-formats.puml) | MVP core / cross-cutting| [SVG](sharing-essential-formats.svg) · [PNG](sharing-essential-formats.png) |
| [sharing-essential-link-sequence.puml](sharing-essential-link-sequence.puml) | MVP core / cross-cutting| [SVG](sharing-essential-link-sequence.svg) · [PNG](sharing-essential-link-sequence.png) |
| [sharing-essential-link-state.puml](sharing-essential-link-state.puml) | MVP core / cross-cutting| [SVG](sharing-essential-link-state.svg) · [PNG](sharing-essential-link-state.png) |
| [sharing-owned-model.puml](sharing-owned-model.puml) | MVP core / cross-cutting| [SVG](sharing-owned-model.svg) · [PNG](sharing-owned-model.png) |
| [sharing-protected-retrieval.puml](sharing-protected-retrieval.puml) | MVP core / cross-cutting| [SVG](sharing-protected-retrieval.svg) · [PNG](sharing-protected-retrieval.png) |
| [work-essential-components.puml](work-essential-views.puml) | MVP ProjectForge| [SVG](work-essential-views.svg) · [PNG](work-essential-views.png) |
| [work-essential-sprint-planning.puml](work-essential-sprint-planning.puml) | Future after MVP| [SVG](work-essential-sprint-planning.svg) · [PNG](work-essential-sprint-planning.png) |
| [work-essential-task-state.puml](work-essential-task-state.puml) | Future after MVP| [SVG](work-essential-task-state.svg) · [PNG](work-essential-task-state.png) |
| [work-essential-transition.puml](work-essential-transition.puml) | MVP ProjectForge| [SVG](work-essential-transition.svg) · [PNG](work-essential-transition.png) |
| [work-essential-views.puml](work-essential-views.puml) | MVP ProjectForge| [SVG](work-essential-views.svg) · [PNG](work-essential-views.png) |
| [work-mutation-sprint-close.puml](work-mutation-sprint-close.puml) | Future after MVP| [SVG](work-mutation-sprint-close.svg) · [PNG](work-mutation-sprint-close.png) |
| [work-owned-model.puml](work-owned-model.puml) | Future after MVP| [SVG](work-owned-model.svg) · [PNG](work-owned-model.png) |
| [workflow-deployment-sequence.puml](workflow-deployment-sequence.puml) | Future after MVP| [SVG](workflow-deployment-sequence.svg) · [PNG](workflow-deployment-sequence.png) |
| [workflow-essential-components.puml](workflow-essential-components.puml) | Future after MVP| [SVG](workflow-essential-components.svg) · [PNG](workflow-essential-components.png) |
| [workflow-essential-deployment-state.puml](workflow-essential-deployment-state.puml) | Future after MVP| [SVG](workflow-essential-deployment-state.svg) · [PNG](workflow-essential-deployment-state.png) |
| [workflow-essential-executor.puml](workflow-essential-executor.puml) | Future after MVP| [SVG](workflow-essential-executor.svg) · [PNG](workflow-essential-executor.png) |
| [workflow-essential-pipeline.puml](workflow-essential-pipeline.puml) | Future after MVP| [SVG](workflow-essential-pipeline.svg) · [PNG](workflow-essential-pipeline.png) |
| [workflow-essential-promotion.puml](workflow-essential-promotion.puml) | Future after MVP| [SVG](workflow-essential-promotion.svg) · [PNG](workflow-essential-promotion.png) |
| [workflow-essential-recovery.puml](workflow-essential-recovery.puml) | Future after MVP| [SVG](workflow-essential-recovery.svg) · [PNG](workflow-essential-recovery.png) |
| [workflow-essential-run-state.puml](workflow-essential-run-state.puml) | Future after MVP| [SVG](workflow-essential-run-state.svg) · [PNG](workflow-essential-run-state.png) |
| [workflow-essential-strategies.puml](workflow-essential-strategies.puml) | Future after MVP| [SVG](workflow-essential-strategies.svg) · [PNG](workflow-essential-strategies.png) |
| [workflow-essential-topology.puml](workflow-essential-topology.puml) | Future after MVP| [SVG](workflow-essential-topology.svg) · [PNG](workflow-essential-topology.png) |
| [workflow-trust-model.puml](workflow-trust-model.puml) | Future after MVP| [SVG](workflow-trust-model.svg) · [PNG](workflow-trust-model.png) |

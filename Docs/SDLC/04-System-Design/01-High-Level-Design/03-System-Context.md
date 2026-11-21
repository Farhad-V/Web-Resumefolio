<a id="3-system-context"></a>

# 3. System Context

[Previous: Architectural Goals & Constraints](02-Architectural-Goals-And-Constraints.md) · [High-Level Design introduction](01-Introduction.md) · [Next: Architecture Overview](04-Architecture-Overview.md)

## 3.1 Actors / Users

Resumefolio supports invited users preparing and tracking professional materials, recipients accessing selected shared content, and collaborators working within ProjectForge repository grants. These are authorization roles in a scenario; one person may participate in more than one role without receiving unrestricted access across them.

| Actor | Main interactions | Authority and limits |
| --- | --- | --- |
| Invited user / applicant | Maintain profile content, tailor drafts, explicitly publish, manage private files and sharing, track manual applications | Acts on authorized resources; profile edits do not silently alter independent drafts or submitted history |
| Employer / share recipient | View selected published materials and retrieve eligible files or PDFs | Access is link-scoped under current sharing policy; viewer context does not establish a named employer identity or workspace membership |
| Repository collaborator | Perform permitted Git operations and work with repository issues and Kanban | Requires current Core entitlement and the applicable ProjectForge grant; issue authority does not imply Git write permission |
| Administrator | Manage admission, accounts and authorized operational metadata | Administrative duties do not confer unrestricted access to private content or repository operations |
| Operator / maintainer | Deploy verified candidates, supervise jobs, monitor health and perform protected backup/restore procedures | Uses explicitly authorized operational access; deployment and recovery privileges remain distinct from product roles |

The actor initiating a request and the service carrying it are different identities. Core forwarding a request to ProjectForge must preserve the required user context rather than replacing user authorization with broad service trust.

## 3.2 External Systems

The context includes two independent applications. From Core's perspective, ProjectForge is an external service; from the complete MVP perspective, both are in scope. System mail delivery and native Git clients are supporting external participants. Private databases, worker processes and storage roots belong to the lower-level architecture views.

| System / participant | Relationship to the MVP | Information crossing the boundary |
| --- | --- | --- |
| Resumefolio Core | Owns invited identity, professional presentation, private files, protected sharing and manual application history | Browser commands, selected recipient-facing content, scoped ProjectForge requests and narrow entitlement/status results |
| ProjectForge | Independently owns repositories, local grants, native Git operations, file history, issues and simple Kanban | Scoped commands/results, current entitlement validation and authorized Git exchanges |
| Browser | Presents each application's server-directed pages and protected recipient views | Session or viewer context, permitted input and authorized response content over HTTPS |
| Native Git client | Performs real repository transfers against ProjectForge | Git protocol exchanges and transport credentials; clone/fetch/push are separate from JSON API operations |
| Transactional mail delivery service | Supports system messages such as invitations and account recovery | Necessary recipient/message data through the configured delivery mechanism; delivery errors require operational handling |

Mail delivery is not a personal mailbox integration. Cloud identity providers, personal mail/calendar providers, AI services, workflow executors and deployment targets are not introduced as MVP product dependencies by this context.

## 3.3 Context Diagram (C4 Level 1)

![Dark-mode Resumefolio MVP system context](Diagrams/hld-context.svg)

[Editable PlantUML source](Diagrams/hld-context.puml) · [PNG alternative](Diagrams/hld-context.png)

The diagram shows the logical MVP boundary and major relationships. The invited-user/administrator node groups browser actors for readability; it does not merge their permissions. A repository collaborator uses the authorized Git-client path for Git transfers and the applicable browser/API path for issue or board actions. The operator's deployment and recovery activities are described in [Deployment Architecture](09-Deployment-Architecture.md).

Arrows name the principal interaction and do not specify every response, network hop or authentication handshake. Core-to-ProjectForge scoped requests and ProjectForge-to-Core entitlement checks are distinct relationships. Mail delivery is shown as a supporting dependency rather than a third product application. Physical placement, databases and worker topology belong in [Architecture Overview](04-Architecture-Overview.md) and [Deployment Architecture](09-Deployment-Architecture.md).

This chapter reuses the shared dark-mode PlantUML source embedded in the Introduction so the same context does not acquire conflicting diagram copies. Use the [selected system boundary](14-Appendices.md#design-record-01-software-architecture-02-system-decomposition-and-boundaries-md) and relevant ADR status when interpreting retained alternative or deferred designs.

## 3.4 System Responsibilities and Scope Boundary

| Concern | Core responsibility | ProjectForge responsibility |
| --- | --- | --- |
| Identity and entitlement | Establish invited identity and current Core entitlement | Validate applicable current entitlement and enforce local grants |
| Professional presentation | Own profiles, independent drafts, explicit publication and protected sharing | No ownership of Core publication or recipient access policy |
| Private files and submission history | Own private artifact bytes/references and immutable submission events | Do not mutate or directly retrieve Core-owned private storage outside an authorized contract |
| Repository collaboration | Initiate permitted scoped interactions and present relevant results | Own repository grants, Git transfers/history, issues and basic Kanban |
| Persistence and durable work | Commit Core records and reconcile Core-owned effects | Commit ProjectForge records and reconcile ProjectForge-owned effects |
| Operations | Protect and recover Core records/files | Protect and recover ProjectForge metadata/repositories |

Each application writes its own data. Shared hosting does not authorize direct cross-database access, shared sessions or unrestricted filesystem access. The API carries only the identifiers and data permitted by its contract.

Manual application tracking records the user's application and actual submitted materials. It does not imply automatic submission to employer systems or job boards. Protected sharing likewise does not imply that a recipient can edit the source profile, browse the owner's files or access application history.

Personal mail/calendar, AI, advanced repository review/releases, general Sprints and user workflow/deployment execution remain deferred. Developer CI/CD and operational deployment support the software lifecycle and do not enable a user workflow-execution feature.

## 3.5 Entry Paths and Trust Boundaries

| Entry path | Authority evaluated | Required boundary behavior |
| --- | --- | --- |
| Authenticated browser workspace | Current account/session plus resource/action policy in the receiving application | Server-side validation and authorization remain authoritative; hiding a UI control is insufficient |
| Employer view or direct shared-file request | Current link/viewer context, selected publication/content, language and download eligibility | No broader account access; apply policy to direct and alternate retrieval paths |
| Core-to-ProjectForge scoped API | Authenticated caller, permitted scope, current user entitlement and local resource grant | Service credentials alone cannot authorize arbitrary user content or repository actions |
| ProjectForge-to-Core status check | Narrow service authority for current identity/entitlement status | Status access does not grant access to Core content |
| Native Git transport | Applicable Git credentials, current entitlement and repository/action grant | Browser/API success is not proof of Git transport permission or interoperability |
| Operational access | Explicit deployment, monitoring, backup or recovery privileges | Keep keys and private content protected and record bounded operational evidence |

Revocation must be evaluated under the selected contract, including applicable active-context, direct-path and cache/range behavior. Already delivered or downloaded bytes cannot be recalled. Do not promise retroactive erasure of a recipient's copy when a publication or share is withdrawn.

## 3.6 Representative Context Scenarios

1. **Prepare and publish:** the invited user changes private source information, explicitly applies selected changes to a draft and separately confirms publication. Core preserves the distinct lifecycle records.
2. **Receive shared materials:** a recipient presents the required sharing context. Core resolves current policy and returns only eligible selected content. Invalid, withdrawn or otherwise unauthorized requests do not disclose private bytes.
3. **Record an application:** the user records a manual submission and selects its exact revision/files. Core preserves the submission event and retained materials independently of later edits or sharing changes.
4. **Use repository collaboration:** an authorized actor requests a ProjectForge operation. ProjectForge validates the caller, current entitlement and applicable grant. Native Git exchanges retain their own transport contract.
5. **Handle dependency uncertainty:** if required authority is unavailable, protected work returns the documented safe unavailable outcome. If a response is lost after a local or remote effect, preserve the recorded outcome and reconcile through the owner rather than assuming rollback or blindly duplicating work.

Detailed command preconditions, payloads, response codes, idempotency and reconciliation rules belong in the [API specification](../03-Low-Level-Design/05-API-Specification.md). This context does not allocate new routes or credential formats.

## 3.7 Dependency and Failure Expectations

Core and ProjectForge remain independently owned even when deployed on one host. A ProjectForge failure affects repository capabilities and must not be represented as a successful repository operation. Core entitlement unavailability can block protected ProjectForge work because current authority cannot be established. Do not substitute stale or broad service authority to conceal that failure.

Transactional mail failures must be visible and handled under the owning delivery/retry policy; a successful local business commit does not prove delivery. Background processing uses durable owner-local work records where required. Host or storage failure can affect both applications under initial colocation, so isolated recovery must cover related records, private bytes and repositories.

Avoid promising complete service independence or automatic failover from a logical boundary diagram. Record and test actual dependency behavior in [Integration & Interfaces](07-Integration-And-Interfaces.md), [Security Architecture](10-Security-Architecture.md) and [Non-Functional Strategy](11-Non-Functional-Strategy.md).

## 3.8 Context Verification and Traceability

| Context obligation | Verification focus | Design reference |
| --- | --- | --- |
| Private workspace and selected recipient access | Cross-user identifiers, direct-file requests, link/viewer scope and changed sharing policy | [Security Architecture](10-Security-Architecture.md) |
| Independent drafts and exact submitted history | Profile updates, explicit publication, withdrawal and preserved artifacts | [Data Architecture](06-Data-Architecture.md) |
| Separate service and user authority | Wrong scope/user/resource, revoked entitlement and unavailable status authority | [API specification](../03-Low-Level-Design/05-API-Specification.md) |
| Repository-specific authority | Actual authorized/denied Git transfers and issue/board operations with distinct grants | [Components](05-Components.md) |
| Observable dependency failures | Lost responses, retries, mail failure and interrupted durable work | [Integration & Interfaces](07-Integration-And-Interfaces.md) |
| Recoverable ownership boundaries | Isolated restoration of records, artifacts and Git storage | [Deployment Architecture](09-Deployment-Architecture.md) |

Use the [SRS](../../02-Requirements-Engineering/01-Software-Requirements-Specification.md) for governing requirements, [System Analysis](../../03-System-Analysis/01-System-Context-And-Gap-Analysis.md) for logical context and domain inputs, and the [RTM](../../02-Requirements-Engineering/03-Requirements-Traceability-Matrix.md) for exact criterion identifiers and evidence. These are planned verification obligations; this chapter does not claim that runtime checks have passed.

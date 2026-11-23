<a id="2-architectural-goals--constraints"></a>

# 2. Architectural Goals & Constraints

[Previous: Introduction](01-Introduction.md) · [Next: System Context](03-System-Context.md)

**Status:** planned MVP architecture. Selected decisions constrain the design; implementation and release evidence remain outstanding. This chapter preserves the distinction between accepted choices, deployment assumptions and verification gates.

## 2.1 Business Drivers

Resumefolio enables invited users to prepare professional materials, control what an employer sees and retain the actual materials submitted with a manual application. ProjectForge adds repository collaboration through a separate system with its own authorization and data ownership.

| Driver | Architectural goal | Consequence for design |
| --- | --- | --- |
| Tailored professional presentation | Let users change source profiles and independent drafts deliberately | Explicit update and publication operations; no silent propagation into historical records |
| Controlled employer access | Expose only the selected representation and artifacts | Sharing policy and current access checks govern direct retrieval as well as browser navigation |
| Trustworthy application history | Preserve exact submission materials | Immutable submission events and retained artifact references survive later edits or publication withdrawal |
| Real Git collaboration | Support native transfers, permissions and file history | ProjectForge owns repositories and local grants; Core entitlement remains part of protected access |
| Maintainable MVP delivery | Keep responsibilities and integration explicit | Separate applications with internally owned modules and scoped contracts |
| Safe operation on initial infrastructure | Bound work and preserve recoverability | Enforce storage/resource policy, supervise durable jobs and rehearse restoration |

Three outcomes guide architecture review: the employer sees only authorized selected materials; the applicant can retrieve the original submission; and a repository action uses current authority for that actor, resource and action.

## 2.2 Key Quality Attributes

The following scenarios define what the architecture must support. They summarize verification concerns and do not assign new requirement identifiers, service targets or acceptance status. Exact criteria and their status belong in the [SRS](../../02-Requirements-Engineering/01-Software-Requirements-Specification/03-Requirements-Specification/14-Quality-Security-And-Recovery-Requirements.md#requirements-specification-quality-security-and-recovery-requirements) and [RTM](../../02-Requirements-Engineering/03-Requirements-Traceability-Matrix/README.md).

| Attribute | Representative stimulus | Required architectural response | Evidence to collect |
| --- | --- | --- | --- |
| Confidentiality and authorization | Another actor requests a private record, direct file URL or repository action | Owning entry point checks current actor/resource/action authority; unauthorized content and mutations are prevented | Cross-user, direct-retrieval and repository permission scenarios |
| Revocation correctness | A share, entitlement or repository grant changes | Protected requests apply current policy; unavailable authority yields the documented safe unavailable outcome | Fresh and active-context scenarios under the selected contract, including Git and downloads |
| Historical integrity | Profile content changes or a publication is withdrawn after submission | Previously recorded submission events and exact referenced artifacts remain intact | Before/after comparison of records, selected versions and file digests |
| Reliable effects | A remote call times out or a worker restarts | Preserve durable local outcomes, distinguish uncertainty from rejection and reconcile under owner control | Lost-response, repeated-request and interrupted-job scenarios |
| Recoverability | Application records, private files or repository storage are lost | Restore protected backups in isolation and validate related records and bytes together | Restore rehearsal with file digests, references and Git consistency checks |
| Performance and resource control | Normal views compete with upload, PDF or Git work | Apply applicable limits and measure workloads separately before changing capacity | Candidate-specific latency, error, resource and quota/concurrency measurements |
| Accessibility and usability | Users navigate forms, validation and protected views with different input/access needs | Maintain accessible navigation, feedback and usable recovery paths | Requirement-linked accessibility and browser-journey evidence |
| Maintainability and compatibility | A component or API contract changes | Keep ownership local, version/evolve contracts compatibly and review affected consumers | Contract checks, migration review and updated criterion traces |
| Observability | Work fails or dependencies become unavailable | Expose accurate status with correlation IDs and bounded diagnostic metadata | Failure-path inspection without credentials or private content in diagnostics |

Do not treat successful page navigation as proof of secure direct access, a successful upload as proof of concurrent quota enforcement, or a completed backup job as proof of recoverability. Validate the relevant boundary and failure case directly.

### 2.2.1 Measurement rules

Record the tested revision, configuration, environment, representative workload and observed results. Measure ordinary view/save activity separately from bulk upload, PDF generation and Git operations. Compare observations with the governing criterion and retain its status if a threshold is proposed or unresolved.

This chapter does not introduce numerical latency, throughput, availability, retention, RPO, RTO or accessibility-conformance targets. Identify unresolved numerical inputs in the applicable requirements or risk record and obtain the required evidence before claiming the affected gate has passed.

## 2.3 Constraints & Assumptions

### 2.3.1 Selected architectural constraints

| Constraint | Design implication | Governing reference |
| --- | --- | --- |
| Core and ProjectForge remain independent systems | Separate databases, credentials, keys, sessions and private storage; each owner persists its own changes | [Selected baseline ADR](../ADR/ADR-006-Selected-Mvp-Implementation-Baseline.md) |
| Core owns professional presentation, private media and application history | ProjectForge cannot become an alternate owner or bypass Core's artifact/sharing policy | [Introduction and scope](01-Introduction.md) |
| ProjectForge owns repository operations, grants, issues and basic Kanban | Use the scoped integration and enforce repository-specific authority, including native Git | [Components](05-Components.md) and [API specification](../03-Low-Level-Design/05-API-Specification.md) |
| Interactive UI uses React/Inertia inside each Laravel application | Laravel retains routing, validation, sessions, authentication and policies; no independently deployed frontend or additional browser REST authentication layer is introduced | [Frontend ADR](../ADR/ADR-007-React-Inertia-Frontend.md) |
| Trusted Blade templates remain for PDF rendering | User-facing React components do not replace the controlled PDF rendering boundary | [Frontend ADR](../ADR/ADR-007-React-Inertia-Frontend.md) |
| MySQL and owner-private filesystem storage support the selected design | Preserve local integrity and authorized references; native Git owns repository object behavior | [Data architecture](06-Data-Architecture.md) and [technology stack](08-Technology-Stack.md) |
| Publication and submission history have explicit lifecycles | Keep mutable source/drafts distinct from immutable revisions/events; retain exact referenced artifacts | [Data architecture](06-Data-Architecture.md) |
| Deferred features remain outside MVP | Do not add personal mail/calendar, AI, advanced review/releases, general Sprints or user workflow/deployment execution | [Project charter](../../01-Project-Planning/01-Project-Charter.md#mvp-scope) |

ADR-007 selects React 19, Inertia 3, Laravel 13, Tailwind 4 and Vite, while retaining trusted Blade/Dompdf templates. Compatible maintained package patches must be resolved and verified at setup with lockfiles. This chapter records the repository's selected direction; it does not assert that dependencies are installed or compatible builds have run.

### 2.3.2 Deployment assumptions and evidence gates

| Assumption / input | Architectural impact | Required validation or revisit condition |
| --- | --- | --- |
| Initial shared Linux host with Nginx/TLS | Both applications share host, disk and resource failure risks despite logical separation | Check process/storage/credential isolation and host headroom; revisit placement if measured workload or isolation needs require it |
| Effective runtime/package compatibility | Both application builds depend on compatible PHP, Node and framework/tooling versions | Record effective versions, install locked dependencies and verify builds during [setup](../../05-Agile-Iterative-Development/01-Project-Setup.md) |
| Current actor validation across the service boundary | Repository access depends on Core entitlement and ProjectForge local grants | Validate actor, scope, revocation and unavailable-authority behavior before enabling the boundary; preserve the baseline's mandatory G2 gate |
| SMTP configuration and transactional delivery | Invitations/recovery require operational system mail | Verify configuration, delivery and failure handling without exposing credentials |
| Backup destination and protected access | Shared-host loss requires recovery copies that remain usable under the chosen failure scenario | Confirm destination, protection and coverage; demonstrate isolated restoration |
| Target capacity and workload | Resource policies and placement depend on actual infrastructure | Measure representative workload, disk reserve, quota enforcement and concurrent admission |

The baseline distinguishes these evidence/input gates from already selected stack choices. Do not reopen a selected architecture merely because verification has not run; revise an ADR when new evidence requires a different decision.

### 2.3.3 Integration and consistency constraints

Synchronous JSON calls cross an authenticated, scoped boundary. Browser sessions, employer-sharing access, service credentials and native Git credentials have different responsibilities. A service call or known identifier does not confer unrestricted resource authority.

Each application commits locally. Do not imply a distributed transaction or report a remote effect as complete solely because the initiating application saved a record. Use contract-defined request identity, local durable records/outboxes and owner-controlled reconciliation for uncertain or repeated work. Recheck current authority on retries and preserve separately recorded outcomes.

If required authority cannot be established, return the documented safe denied or unavailable result without performing an unauthorized operation. Precise response codes, idempotency scope, transaction boundaries and retry behavior belong in the [API specification](../03-Low-Level-Design/05-API-Specification.md) and detailed component contracts.

### 2.3.4 Storage and lifecycle constraints

Private bytes must remain behind the owning authorization boundary. Hashes and metadata support integrity checks but do not replace access checks. Submission references must protect the exact retained materials from ordinary edits, replacements, withdrawal or cleanup.

Concurrent admissions and background work must respect the selected file-type, per-file, aggregate-quota and disk-reserve policy. Validate the policy's effective point and partial-failure handling in the detailed design. Avoid exposing partial artifacts or releasing quota that remains required by retained material.

## 2.4 Trade-offs and Consequences

| Choice | Benefit | Cost / residual risk | Revisit trigger |
| --- | --- | --- | --- |
| Separate Core and ProjectForge | Clear data and authorization ownership | Independent identity/API/Git boundary adds failure and verification work | Evidence shows the current integration contract cannot meet accepted criteria |
| Initial colocation | Practical initial deployment | Shared outage and contention; logical isolation does not provide host resilience | Measured capacity, security or recovery needs exceed verified host capability |
| Immutable historical records and retained bytes | Reliable proof of submitted materials | Additional storage and retention/cleanup coordination | Governing retention requirements or measured storage needs change |
| Current authority checks | Revocation and access policy remain enforceable | Dependency unavailability can block protected actions | Review availability requirements and the accepted trust model through an ADR |
| Durable asynchronous work | Recoverable processing outside immediate requests | Pending work, retries and reconciliation require visible states | Backlog or failure evidence exceeds accepted operational bounds |
| React/Inertia with server-owned policies | Interactive UI within Laravel's application model | Frontend state, validation and navigation require explicit verification | Requirement or compatibility evidence warrants a revised frontend decision |

See the [quality and trade-off design](14-Appendices.md#design-record-06-design-quality-and-security-analysis-01-quality-attributes-and-design-trade-offs-md) for retained analysis. Trade-offs do not waive acceptance criteria or remove scope to hide a boundary risk.

## 2.5 Architecture Review Criteria

For a proposed design change, establish the affected requirement and selected decision before implementation. Review the following questions against concrete scenarios:

1. Does each record, artifact and operation still have one explicit owning system/component?
2. Can every protected path establish current actor, resource and action authority, including direct media and Git requests?
3. Do profile edits, explicit publication and withdrawal preserve previously submitted materials?
4. Are local success, remote rejection and uncertain remote outcomes distinguishable and recoverable under the contract?
5. Can repeated, interrupted or concurrent work violate grant, integrity, quota or retention rules?
6. Can operators observe failure without exposing private bytes or credentials, then restore consistent records and storage?
7. Are performance and accessibility conclusions supported by the actual candidate and applicable criteria?
8. Are changed contracts, migrations, ADR status, diagrams and criterion-level traces updated together?

Use [Risks & Key Decisions](12-Risks-And-Key-Decisions.md) to follow unresolved architecture risks and the [RTM](../../02-Requirements-Engineering/03-Requirements-Traceability-Matrix/README.md) for exact evidence links. Assign an owner and required evidence to unresolved gates; documentation completion alone does not establish release readiness.

## 2.6 Related Architecture Views

The [Introduction](01-Introduction.md#18-architecture-overview-and-chapter-guide) contains the shared dark-mode PlantUML context, application structure, lifecycle and deployment diagrams. Those views illustrate the constraints in this chapter and are reused to keep a single source for each architecture view.

Continue with [System Context](03-System-Context.md) for actors and external boundaries, [Security Architecture](10-Security-Architecture.md) for controls, and [Non-Functional Strategy](11-Non-Functional-Strategy.md) for measurement and operational evidence.

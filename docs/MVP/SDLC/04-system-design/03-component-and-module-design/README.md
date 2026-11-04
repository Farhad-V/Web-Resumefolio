# Component and Module Design

The [Baseline](../../../baseline/README.md) selects the MVP system/technical boundaries. These project-specific records retain detailed operation, data, behavior and failure analysis; no source modules or product tests exist yet.

## 1. Reading route

Start with [architecture decomposition](../01-software-architecture/02-system-decomposition-and-boundaries.md), [module/dependency rules](01-modularity-dependencies-and-encapsulation.md) and [implementation artifacts](02-implementation-view-and-artifacts.md), then the affected component below. Use shared [Data](../04-data-design/README.md), [API](../05-interface-and-api-design/README.md) and [Security/Quality](../06-design-quality-and-security-analysis/README.md) owners rather than copy their policies into each record.

## 2. Shared module and implementation guidance

For each component keep responsibilities/contracts, identities/classes/data, algorithms/concurrency, failure/recovery scenarios and justified coding constraints together. Refine the existing actual record instead of creating a second generic package. Link exact source criteria and important [ADRs](../07-design-decisions/README.md); retain allowed/denied/stale/repeated/failure outcomes and their verification needs.

## 3. Proposed component catalog

Current MVP slices are governed by the Baseline. Component models may include explicitly deferred extensions; their existence does not add those features to the current Release.

### LC-01 — Identity and Access

[Component record](components/identity-and-access.md). Owns accounts, invitations, sessions and scoped grant context. Resource owners still apply current operation/lifecycle rules; successful sign-in or a membership never supplies universal access.

### LC-02 — Professional Presentation

[Component record](components/professional-presentation.md). Owns profiles, independent drafts/overrides, selected evidence and identified publication revisions. Selected source application and separate publication preserve independent resume content and actual history.

### LC-03 — Representation and Sharing

[Component record](components/representation-and-sharing.md). Owns download settings, independent links and viewer authorization. Current eligibility, selected publication/language/rendition and artifact availability remain distinct; direct retrieval cannot bypass them.

### LC-04 — Manual Applications

[Component record](components/applications.md). Owns opportunity/preparation, manual progress and actual submission material manifests. Progress, provider acceptance and actual submitted evidence are different facts; current live content does not replace historical material.

### LC-05 — Communication and Calendar

**Release applicability:** future-domain design retained after MVP; core operating/deployment and recovery controls still apply to MVP where relevant.

[Component record](components/communication-and-calendar.md). Owns provider capability, local drafts/activities, attributable send attempts and synchronization mappings. Disconnect/unlink/provider mutation and uncertain effects need explicit handling rather than replay or silent conflict resolution.

### LC-06 — Work Management

[Component record](components/work-management.md). MVP owns ProjectForge issues and fixed simple Kanban, membership and safe movement. General projects/backlog/Sprints and advanced planning remain after MVP.

### LC-07 — Git Collaboration

[Component record](components/git-collaboration.md). MVP owns authorized repositories, real native Git transfers, file/history and basic issues. Advanced fork/review/merge/releases are deferred; Git operations never authorize user workflow execution or production deployment.

### LC-08 — Workflow and Deployment Coordination

**Release applicability:** future-domain design retained after MVP; core operating/deployment and recovery controls still apply to MVP where relevant.

[Component record](components/workflow-and-deployment.md). Owns supported workflow definitions, admitted attempts, restricted output references and separately authorized target attempts. Execution requires actual enabling evidence; cancellation intent is not confirmed termination.

### LC-09 — Files and Operations

[Component record](components/files-and-operations.md). Owns admitted artifact identity/usability, quota reservations, protected-reference accounting and recovery records. Replacement, retirement, physical reclamation and usable recovery require their actual attributable outcomes.

## 4. Completing one component package

Use the selected mechanisms in the Baseline. During implementation add actual operation signatures, schema/migration and code paths plus criterion-linked checks. Source/draft/publication/submission identity, current grant/link revocation, protected references and durable truthful effects must remain consistent across owners. The Core and ProjectForge retain independent DB/process/key/session/storage boundaries.

## 5. Diagram guide

[Shared module diagrams](diagrams/README.md) and [component diagrams](components/diagrams/README.md) link editable sources and exports. Byte-identical views use one canonical asset; distinct models and their meanings are retained. Generic uninstantiated examples are omitted from current Documentation.

## 6. Review and current limits

Review contracts against the owning requirements, current authority, data/state invariants and consumer/failure consequences. Link actual targeted results before accepting dependent capability. Security, compatibility, resource suitability and demonstrated restore remain named gates; no provider/runner/Git capability is established by a model or diagram count.

## 7. FAU basis and maintenance

Keep analysis meaning separate from physical deployment/code mechanisms. Use the [reference map](../01-reference-and-coverage-map.md), [evolution procedure](../02-detailed-and-object-oriented-design/05-design-evolution-refactoring-and-technical-debt.md) and [Design review/handoff](../06-design-quality-and-security-analysis/05-design-review-traceability-and-handoff.md) when a material interface/ownership choice changes.

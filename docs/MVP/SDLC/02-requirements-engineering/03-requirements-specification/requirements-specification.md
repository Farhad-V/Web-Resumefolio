# Resumefolio — Software Requirements Specification

## Current implementation baseline — November 4, 2026

[BL-MVP-2026-11-04.1](../../../baseline/README.md) selects the MVP technical mechanisms, numerical policies, priorities and requirement/criterion dispositions under Farhad’s explicit delegation. It supersedes earlier Proposed/pending mechanism and whole-baseline statements below for MVP design input. Future clauses and dated evidence remain separate. Runtime/actor validation, credentials, Git isolation, capacity and backup/restore still require the named implementation/Release gates; this update reports no product test Pass.

### Prior source material and rationale (superseded where this Baseline selects a different MVP choice)

| Item | Current position |
| --- | --- |
| Purpose | Coordinate the distributed SRS: authority, product boundary, requirement levels, source ownership and acceptance gates |
| Owner | Farhad; sole delivery and operations owner |
| Status | Proposed SRS overview — M-02 baseline pending |
| Detailed content | 15 primary specification drafts with 157 provisional candidate records; this overview allocates no duplicate product requirements |
| Planning authority | Accepted Version 1 scope and constraints; M-01 accepted only for the identified snapshot under DEC-116 |
| Revision | November 1, 2026 — explicit functional/non-functional navigation; baseline still pending |

**At a glance:** the MVP combines core professional presentation/private media/manual applications with separately authorized basic ProjectForge. Mail/calendar and advanced work/Git/execution are future. All paths retain resource-specific access. This SRS coordinates required outcomes and evidence;
domain files own the primary wording. Detailed policies and verification remain
open, and documentation completion does not constitute baseline or release approval.

[Authority](#1-status-and-authority) · [Context](#2-introduction-system-boundary-and-operating-context)
· [Levels](#3-requirement-levels-and-record-conventions) · [Functional requirements](#functional-requirements)
· [Non-functional requirements](#non-functional-requirements) · [Coverage](#4-functional-areas-and-primary-record-ownership)
· [Supporting views](#5-supporting-views-and-traceability) · [Acceptance](#6-review-baseline-and-later-verification)
· [Gaps](#7-open-definitions-and-dependent-gates) · [Maintenance](#8-maintenance-and-diagrams)

<a id="status-and-authority"></a>
## MVP requirement applicability and remaining review

Apply the current candidate release register: retain core presentation/sharing/manual applications/private files and basic ProjectForge; defer mail/calendar, advanced Git review/releases, advanced backlog/Sprints and YAML execution/deployment. Candidate IDs and planned verification stay intact. Mixed criteria must be scoped individually; allocation does not approve proposed numbers, priority or a complete baseline. Older 157-candidate/470-criterion evidence is historical larger-product coverage, not an MVP pass. Keep source, independent resume draft, explicit publication and actual submitted material identities distinct. Profile changes require preview/select/apply and cannot mutate publication or submitted history. Manual applications include status, next action and follow-up date without mail/calendar dependencies.

Authority: [OWNER-MVP-2026-11-04](../../01-project-planning/owner-mvp-decision-2026-11-04.md). [Candidate allocation](mvp-release-allocation.md).

## 1. Status and Authority

This is the entry point to a **distributed** Software Requirements Specification.
Use the [folder guide](README.md) for reading paths, document statuses and diagrams.
Accepted [Version 1 Scope](../../01-project-planning/02-scope.md) governs inclusions,
exclusions and conditional commitments. [Resources and Constraints](../../01-project-planning/05-resources-and-constraints.md)
governs agreed delivery restrictions; [Planning Completion](../../01-project-planning/10-planning-completion-criteria.md)
retains actual M-01 acceptance and GAP-D follow-up. Later working drafts do not
silently replace the accepted planning snapshot or record a new owner decision.

| Statement type | Authority and treatment |
| --- | --- |
| Accepted scope/constraint | Link the exact original source; preserve its limits and conditions |
| Proposed requirement/refinement | Review source, rationale, actors/conditions, behavior and acceptance criteria separately |
| Interpretation or open question | Identify uncertainty/owner/gate; do not present as stakeholder approval |
| External-source finding | Retain publisher/date/applicability and distinguish it from actual project access/configuration |
| Verification/review result | Record actual candidate, method, outcome/evidence and limits only when performed |
| Baseline/change decision | Identify owner outcome and reviewed revision; document material impacts and follow-up |

The records in this set remain proposed. No global FR/NFR notation, priority
ranking, detailed role policy or numeric service target is established merely by
the local candidate prefixes or the presentation order.

<a id="introduction-system-boundary-and-operating-context"></a>
## 2. Introduction, System Boundary and Operating Context

The MVP core supports private professional information and independent resumes/portfolio, generated/uploaded PDFs, protected sharing, My Files & Media on the same server, cover letters and manual application status/next action/follow-up with actual submitted materials. The separate ProjectForge supports real Git repositories/transfers/permissions/file-history, issues and simple Kanban through user-scoped API. Gmail/calendar, advanced backlog/Sprints/review/releases and YAML execution/deployment are future-only.

| Boundary | Required context / limit |
| --- | --- |
| Human participants | Registered applicant/resource owner, invited collaborator, employer viewer, administrator/platform owner and project owner/operator; roles are contexts, not inherited universal grants |
| Private workspace | Individual identity and resource/action/state permissions; unified sign-in does not expose unrelated private mail/resumes/repositories |
| Employer disclosure | No viewer account required; password-protected intended resume and selected content, including authorized direct files/PDFs |
| External exchange | Browser/Git clients, selected Google operations and operational dependencies; exact contracts/actual access remain to be established |
| Execution/deployment | Real agreed execution only after required feasibility/security/resource gates; Push/merge does not inherently authorize production deployment |
| Operating scale | Initial target 10 users; workload/concurrency/capacity need evidence; roughly 1,000 users is a growth direction |
| Delivery resources | One owner; current owner input: 20 project hours/week including learning/docs/tests; existing server/budget and Laravel/OOP; architecture, database, frontend, Git engine and runner not selected here |
| Delivery date | November 8, 2026 requested target, not a validated forecast |

Product AI, automatic translation and automatic legacy-demo migration remain
excluded. Manually maintained English/German content is included. Portfolio
media/diagrams are externally authored content, not new in-product authoring tools.
Automatic external job submission and universal GitHub Actions compatibility are
not implied. Existing demo/reference projects remain preserved references.

[Actors and Context](../02-stakeholders-and-elicitation/actors-and-system-context.md)
owns actor definitions; [Assumptions and Dependencies](../../01-project-planning/06-assumptions-and-dependencies.md)
owns ASM/DEP status. A reference project's features, development GitHub or a prior
tool demonstration does not prove a product requirement has been implemented.

<a id="requirement-levels"></a>
## 3. Requirement Levels and Record Conventions

| Level / view | Question answered | Primary file |
| --- | --- | --- |
| Business | Why is the product needed, and what outcome evidence matters? | [Business Requirements](business-requirements.md), BIZ-D |
| User | Which actor needs what observable outcome in which context? | [User Requirements](user-requirements.md), USR-D |
| Functional | What behavior is required, including normal/denied/failure paths? | Domain files in section 4 |
| Business rule/lifecycle | Which cross-module invariants and change/removal effects apply? | [Business Rules](business-rules-and-data-lifecycle.md), BRL-D |
| Domain/constraint | What is inherent meaning, deliberate policy, imposed project constraint or externally applicable obligation? | [Domain Constraints](domain-requirements-and-constraints.md), DOM-D |
| Interface | What crosses a boundary, under whose authority and with what outcome? | [External Interfaces](external-interface-requirements.md), EIF-D |
| Quality | Under which conditions/measure does behavior or recovery satisfy the agreed criterion? | [Quality/Security/Recovery](quality-security-and-recovery-requirements.md), QSR-D |

Each final allocated record needs identifier, level/type, source, rationale,
actor/context, obligation, observable criteria, owner, justified priority, actual
status, planned method, dependencies and unresolved decisions. Use the
[requirement template](../templates/requirement-template.md). Local references
such as PRP-D01 remain proposed navigation until the final convention is reconciled.

Use explicit stimulus/environment/response/measurement for quantitative quality.
Do not replace undecided thresholds, retention or recovery targets with arbitrary
numbers. Conditional criteria are not ready for acceptance until their referenced
policies are decided. Architecture/schema/tool selections belong in later justified design.

<a id="functional-requirements"></a>
### 3.1 Functional Requirements

Functional requirements describe **what the system does**: inputs it accepts, information it manages, operations it performs and observable responses to actors or external events. This is the explicit functional index of the distributed SRS. The linked primary records own the complete proposed obligation, criteria, source and open detail; this index does not duplicate or accept their wording.

| Functional capability | Primary records | Observable behavior covered |
| --- | --- | --- |
| Accounts, sign-in and permission enforcement | [ACC-D01–ACC-D12](accounts-authentication-and-permissions.md) | Establish the required account context; continue authorized journeys; allow/deny resource operations; handle sharing and access changes under explicit policies. |
| Professional profiles, tailored resumes and evidence | [PRP-D01–PRP-D10](profiles-resumes-and-portfolio.md) | Maintain reusable content, select/override it independently, manage selected evidence and manually maintained language variants, and report save/lifecycle outcomes. |
| PDF generation, uploaded variants and protected sharing | [PDF-D01–PDF-D10](pdf-and-controlled-sharing.md) | Generate or associate PDFs, configure download availability, authorize selected retrieval and apply owner link/password controls. |
| Manual application management | [APP-D01–APP-D09](manual-application-management.md) | Record opportunities, prepare cover letters, associate resumes, record progress and preserve actual submitted materials. |
| Gmail and calendar operations | [EGC-D01–EGC-D12](email-calendar-and-google-integration.md) | Connect the intended account, read/compose/send/reply, manage agreed activities, synchronize selected information and handle disconnection/outcomes.  **After MVP.** |
| Work, Kanban and Sprint planning | [PKS-D01–PKS-D11](projects-kanban-and-sprints.md) | Manage work contexts, items/tasks, assignments, authorized collaboration and a coherent Sprint Backlog. |
| Real Git hosting and collaboration | [GIT-D01–GIT-D10](git-hosting-and-collaboration.md) | Create/browse repositories, support agreed real-client transfer, forks, pull requests, reviews, merge and repository tracking/releases. |
| Conditional workflow execution and deployment | [YML-D01–YML-D12](yaml-workflows-and-cicd.md) | Validate definitions, admit eligible runs, expose results, handle cancellation and separately authorize deployment, subject to retained enabling gates.  **After MVP.** |
| Administration and file operations | [AFO-D01–AFO-D12](administration-files-and-operational-behavior.md) | Configure effective policy, validate/admit files, enforce quotas and expose authorized operational information and lifecycle actions. |
| Boundary operations | [EIF-D03–EIF-D08](external-interface-requirements.md) | Apply authorization, file exchange, Google, real Git and execution contracts with operation-specific outcomes. |

These are functional **aspects** of the cited records. A range does not assert that every sentence or criterion in a domain file is exclusively functional: security, timing, integrity and lifecycle constraints also apply through the next section. Use the [external scenarios](../04-scenarios-and-models/user-stories-and-scenarios.md) for actor-facing examples; internal implementation design is not specified here.

<a id="non-functional-requirements"></a>
### 3.2 Non-Functional Requirements

Non-functional requirements describe **the quality and conditions under which the required functions must operate**, together with imposed technical and management constraints. They are not optional merely because they are non-functional, and they also require assessable criteria. This category is broader than the quality file alone.

| Non-functional aspect | Primary records / authoritative source | Required assessment boundary |
| --- | --- | --- |
| Response performance and capacity | [QSR-D01/D02](quality-security-and-recovery-requirements.md) | Defined operations, workload, data volumes, concurrency, measurement and decided thresholds; initial user count alone is not a load model. |
| Usability, accessibility and client compatibility | [QSR-D03](quality-security-and-recovery-requirements.md), [EIF-D02](external-interface-requirements.md) | Reviewable task, supported-client/input and accessibility criteria with understandable outcomes. |
| Availability, reliability and degradation | [QSR-D04](quality-security-and-recovery-requirements.md), [EIF-D08](external-interface-requirements.md) | Define usable/degraded/unavailable outcomes, observation conditions and safe failure/reconciliation expectations. |
| Confidentiality, isolation and secret protection | [QSR-D05–QSR-D07](quality-security-and-recovery-requirements.md), [ACC](accounts-authentication-and-permissions.md), [YML](yaml-workflows-and-cicd.md) | Cross-user/trust boundaries, direct access and secret/content handling; exact mechanisms remain later justified design. |
| Integrity and lifecycle consistency | [QSR-D08/D09](quality-security-and-recovery-requirements.md), [BRL-D01–BRL-D10](business-rules-and-data-lifecycle.md) | Independent tailoring, actual submitted history, references, changes and retention/restore semantics remain coherent. |
| Backup and recoverability | [QSR-D10–QSR-D12](quality-security-and-recovery-requirements.md) | Explicit coverage, recovery point/time targets, consistent usable restoration and current-access/external-state reconciliation. |
| Operational evidence and maintainability | [QSR-D13/D14](quality-security-and-recovery-requirements.md), [AFO-D09–AFO-D12](administration-files-and-operational-behavior.md) | Restricted useful diagnostics and version/environment-specific procedures with actual evidence and stated limitations. |
| Interoperability and representation constraints | [EIF-D01/D05/D06/D09/D10](external-interface-requirements.md), [DOM-D05–DOM-D08](domain-requirements-and-constraints.md) | Review supported clients/exchanges, identity/time/language semantics and actual external applicability; documentation is not provider access or compliance proof. |
| Technical and platform constraints | [Resources and Constraints](../../01-project-planning/05-resources-and-constraints.md), [DOM-D08](domain-requirements-and-constraints.md) | Preserve Laravel/OOP, existing resource/budget boundaries and actual platform feasibility; no database/frontend/Git engine/runner is selected here. |
| Management and delivery constraints | [Resources](../../01-project-planning/05-resources-and-constraints.md), [Roadmap](../../01-project-planning/08-roadmap-and-milestones.md), [Working Method](../../01-project-planning/09-working-method-and-change-control.md) | Solo capacity, spending authority, agreed phase gates and requested dates; a requested deadline is not a verified forecast. |

Operation and quality are complementary aspects, not mutually exclusive file labels. For example, rejecting an unauthorized PDF request is functional behavior; protecting confidentiality across every retrieval path is a cross-cutting quality requirement. Configuring a quota is a function; respecting actual combined capacity is a constraint. Do not allocate duplicate FR/NFR records merely to repeat those meanings.

### 3.3 Business Outcomes, User Goals and Rules

[BIZ-D](business-requirements.md) explains why the product is needed; [USR-D](user-requirements.md) expresses actor outcomes. [BRL-D](business-rules-and-data-lifecycle.md) and [DOM-D](domain-requirements-and-constraints.md) constrain or explain the functions and qualities. These are additional levels/aspects, not reasons to force every business statement into one exclusive FR or NFR bucket.

### 3.4 Shared Readiness and Identifier Rules

Both categories remain proposed and follow the same source, criterion, feasibility, traceability and owner-review gates. Existing 157 candidate identifiers remain unchanged; the headings FR/NFR do not create 157 new records or establish a new numbering convention. [Priority proposals](requirements-priority-and-readiness.md) remain proposals. [Quantitative target contracts](quality-security-and-recovery-requirements.md#target-decision-contracts) explicitly retain missing numerical decisions as acceptance blockers. This classification is navigation, not baseline acceptance.

<a id="functional-areas"></a>
## 4. Functional Areas and Primary Record Ownership

| Scope coverage | Primary specification | Candidate count / related rules |
| --- | --- | --- |
| SCP-01 / DEC-028: identity, grants, unified sign-in | [Accounts](accounts-authentication-and-permissions.md) | 12 ACC-D; every domain enforces applicable resource/action authority |
| SCP-02/03 / DEC-027/026: reusable content and selected evidence | [Profiles/Resumes/Portfolio](profiles-resumes-and-portfolio.md) | 10 PRP-D; BRL-D propagation and independent tailoring |
| SCP-04/05 / DEC-025/024: PDF variants and employer sharing | [PDF/Sharing](pdf-and-controlled-sharing.md) | 10 PDF-D; ACC-D direct access and owner controls |
| SCP-06 / DEC-023: manual applications and submitted copies | [Applications](manual-application-management.md) | 9 APP-D; actual submitted set differs from current source/live view |
| SCP-07 / DEC-022: correspondence/calendar | [Google Integration](email-calendar-and-google-integration.md) | 12 EGC-D; provider permissions/source notes differ from actual access  **After MVP.** |
| SCP-08 / DEC-021: projects, Kanban, backlogs/Sprints | [Work Management](projects-kanban-and-sprints.md) | 11 PKS-D; item/task distinction and composite Sprint Backlog |
| SCP-09 / DEC-020: real Git hosting/collaboration | [Git Hosting](git-hosting-and-collaboration.md) | 10 GIT-D; real-client and current revision context |
| SCP-10 / DEC-019: conditional execution | [YAML/CI/CD](yaml-workflows-and-cicd.md) | 12 YML-D; isolation/resources/secrets and separate deployment grants  **After MVP.** |
| SCP-11 / DEC-018: effective file/storage policy | [Administration/Files](administration-files-and-operational-behavior.md) | 12 AFO-D; infrastructure/accounting/lifecycle consistency |
| SCP-12 / DEC-017: operational readiness | [Quality/Recovery](quality-security-and-recovery-requirements.md) and [Administration](administration-files-and-operational-behavior.md) | 14 QSR-D overall; actual restoration and versioned guidance required later |

The remaining primary views are 5 BIZ-D, 12 USR-D, 10 BRL-D, 8 DOM-D and 10 EIF-D.
Together the 15 detailed files contain **157 provisional records**. Counts are
working inventory, not approved scope size, effort estimates, tests or acceptance
evidence. Detailed wording belongs in the primary file; cross-cutting rules apply
to it without creating competing duplicates in this overview.

## 5. Supporting Views and Traceability
<a id="supporting-views"></a>

![Evidence chain from accepted intent to proposed records and later results](../diagrams/srs-traceability-map.png)

[Scalable SVG](../diagrams/srs-traceability-map.svg) · [Graphviz source](../diagrams/srs-traceability-map.dot)

Arrows indicate relationships to maintain, not a populated formal traceability
register or an implementation sequence. Colors supplement labels. One user goal
may need several functional/quality records, and one cross-cutting rule may affect
many scenarios; no one-to-one relation is imposed.

| Supporting view | Use / evidence boundary |
| --- | --- |
| [Elicitation Plan](../02-stakeholders-and-elicitation/elicitation-plan-and-techniques.md) / [Log](../02-stakeholders-and-elicitation/elicitation-log.md) | Planned research versus actual documentary extraction and unresolved interpretation |
| [Scenarios](../04-scenarios-and-models/user-stories-and-scenarios.md) | Actor/context, preconditions, normal/alternative/denied/failure/recovery examples |
| [Dictionary](../05-data-definitions/data-dictionary.md) / [Glossary](../05-data-definitions/glossary.md) | Shared conceptual meaning, authority and lifecycle; not schema |
| [Traceability](../06-validation-and-traceability/requirements-traceability.md) | Final allocated source/requirement/scenario/design/verification links; do not infer population from this map |
| [Review Findings](../06-validation-and-traceability/review-plan-and-findings.md) | Actual inspection issues, dispositions and rechecks |
| [Questions](../07-change-and-baseline/open-questions-and-decisions.md) / [Change Control](../07-change-and-baseline/change-control.md) | Actual decisions, owner/gate and material impact |

**Consistency anchors:** independent resume selections/overrides; actual submitted
materials not overwritten by later source edits; selected direct-file sharing;
downloaded copies outside product revocation; no private-resource access from
unrelated membership; Product Backlog Items distinct from tasks; Sprint Backlog
includes goal/items/plan; Git hosting distinct from execution; deployment separately
authorized; provider synchronization explicit; backup existence distinct from recovery.

## 6. Review, Baseline and Later Verification

![Reconcile records and gates before recording an identified baseline disposition](../diagrams/srs-baseline-decision.png)

[Scalable SVG](../diagrams/srs-baseline-decision.svg) · [PlantUML source](../diagrams/srs-baseline-decision.puml)

Apply the [requirements baseline criteria](../07-change-and-baseline/requirements-review-and-baseline-criteria.md):

1. Check scope coverage, source/status, actor outcomes and exclusions/conditions.
2. Resolve acceptance-blocking inputs, states, permissions, lifecycles, contracts and quantitative targets; retain justified dependency gates and real findings.
3. Reconcile identifiers/priorities, scenarios/dictionary and traceability; record actual inspections and addressed contradictions.
4. Present an identifiable candidate and evidence to the owner; record the actual outcome and remaining obligations separately from file creation.

M-02 acceptance is not a product test Pass, provider approval, successful recovery
or release decision. Actual integrated behavior/quality/restoration belongs to
later capability and M-09/M-10 evidence under [Milestones](../../01-project-planning/08-roadmap-and-milestones.md).
The agreed initial SDLC documentation, analysis/design and tracking reconciliation,
and wider pre-implementation agreement still precede product coding.

## 7. Open Definitions and Dependent Gates

| Group | Required next decisions/findings | Existing gate |
| --- | --- | --- |
| Core behavior | Fields/required inputs, states, task/item/Sprint relations, source update and submission capture | GAP-D06; affected M-02 acceptance |
| Identity/access/content | Role/action matrix, authentication/session/revocation, safe serving, languages and lifecycle | Affected M-02/M-03 security/data decisions |
| Provider/delivery | Required Google operations/access/conditions, sync/conflicts; distinct authentication/notification delivery | GAP-D02/D03; access before dependent development |
| Resources/quality | Actual combined demand, file limits, client matrix, performance/availability/accessibility and costs | GAP-D01/D08/D10; dependent design/target commitments |
| Recovery | Coverage/storage, retention, RPO/RTO, restored grants/deleted-data and external-state reconciliation | GAP-D04; M-03 design, actual restoration before M-09 |
| Conditional execution | Syntax/triggers, untrusted-code isolation, secrets/limits and target approval | GAP-D09; before execution design acceptance/enabling |
| Delivery/baseline | Feasible effort/solo operation, domain/TLS, compatibility and tracking alignment | GAP-D05/D07/D08/D11 and agreed pre-coding gate |

Farhad coordinates all gaps. This table summarizes retained follow-up; it does
not allocate new shared questions or claim completed investigations. Material scope,
cost or delivery changes need documented owner decisions, not silent scope reduction.

## 8. Maintenance and Diagrams

- [ ] Reconcile this overview and folder counts whenever primary records change.
- [ ] Preserve source decisions, semantic boundaries, explicit open policies and exact review status.
- [ ] Keep actual question/scenario/traceability/evidence links current; avoid duplicate detailed obligations.
- [ ] Check diagram labels/arrows, source-render synchronization and file/section links.
- [ ] Record identifiable owner review before changing baseline status.

| Diagram | Source | SVG | PNG |
| --- | --- | --- | --- |
| SRS traceability relationships | [DOT](../diagrams/srs-traceability-map.dot) | [SVG](../diagrams/srs-traceability-map.svg) | [PNG](../diagrams/srs-traceability-map.png) |
| SRS baseline decision | [PlantUML](../diagrams/srs-baseline-decision.puml) | [SVG](../diagrams/srs-baseline-decision.svg) | [PNG](../diagrams/srs-baseline-decision.png) |

Follow the [diagram guide](../diagrams/README.md). Save UTF-8 without BOM; retain
editable sources and SVG/PNG outputs together. Colors supplement labels; diagrams
are conceptual requirements models, not selected architecture or actual acceptance.

**Current outcome:** Expanded proposed distributed SRS overview. No duplicate SRS
candidate IDs are allocated; no owner baseline acceptance or implementation,
provider, capacity, security or recovery result is established by this revision.

[Specification guide](README.md) · [Requirements index](../README.md)

## Course Alignment: Stakeholder View and Assessable Detail

The stakeholder-facing specification is provided by business/user outcomes, actor/context descriptions and concise external use cases. The system/software view adds necessary behavioral, quality, interface and imposed-constraint detail in the primary domain records. These are linked views of one specification, not duplicated competing requirements or a mandated two-file layout. FAU V02 slides 10–12 and 25 permit domain-specific organization.

The [priority/readiness register](requirements-priority-and-readiness.md) provides per-candidate proposals without changing accepted scope. Actual priorities remain unassigned. The [quality target decision contracts](quality-security-and-recovery-requirements.md#target-decision-contracts) explicitly identify missing quantitative decisions. Context and external use-case modeling are part of Requirements Engineering; later System Analysis refines internal domain relationships and behavior.

Keep stakeholder goals concise. Supporting audit/administration obligations remain in their appropriate detailed records rather than crowding high-level use cases with implementation detail. Existing candidate IDs are usable unique locators; preservation matters more than adopting a particular FR/NFR spelling.

## Proposed Answers for Detailed Requirements Review — November 1, 2026

The owner requested completion of the outstanding questions. The sections below supply concrete **proposed** answers rather than infer approval of previously unspecified policy. They supersede the absence of a proposal in earlier open-detail paragraphs, not accepted scope or historical decisions. Their fields, limits and behavior require review before affected requirement acceptance; no implementation or product-test Pass is reported. Existing candidate IDs and primary obligations are retained. See the [review package](../07-change-and-baseline/requirements-answer-review.md) for authority, evidence gates and cross-document navigation.

<a id="resolution-q-d01"></a>
### Proposed answer Q-D01: Identifiers, priorities and traceability

**Affected records:** All 157 existing candidates; RF-D01–RF-D04. **Disposition:** Answer proposed; owner acceptance pending.

1. Keep the existing BIZ/USR/ACC/PRP/PDF/APP/EGC/PKS/GIT/YML/AFO/QSR/BRL/DOM/EIF candidate IDs as stable requirement locators; do not rename them merely to introduce FR/NFR navigation. Allocate a new candidate only through change control. A changed meaning retains revision history; a superseded requirement points to its replacement.

2. Name acceptance criteria locally as <candidate>-AC01, AC02 and so on in their existing bullet order. Future insertions get a new suffix; do not renumber established criteria. Classify behavior versus quality/constraint in the SRS index; cross-cutting records can affect both views without duplicate requirements.

3. Retain the 98 existing proposed Must classifications. Propose Must also for the 59 unclassified business/user/cross-cutting candidates because their stated outcomes support accepted scope, access/integrity or operational gates. This is an individual review proposal for every linked record, not an accepted priority or a proof that every refinement is necessary. No accepted capability is removed; split any unsupported refinement during owner review.

4. Separate scope priority from build order. Investigate identity/access, submitted history, provider access, recovery and untrusted execution before accepting dependent design. Require criterion-to-review/test evidence, not token presence alone; preserve historical citation counts as history.

**Assessable review cases:** [RC-Q01-01 through RC-Q01-03](../04-scenarios-and-models/user-stories-and-scenarios.md#review-q-d01). These are planned checks, not executed results.

**Remaining evidence / acceptance condition:** Owner review of the proposed rule and its affected criteria is required; no product test is reported.

<a id="resolution-q-d28"></a>
### Proposed answer Q-D28: Forecast, work mapping and baseline candidate

**Affected records:** SRS; USR; traceability; GAP-D05/D11. **Disposition:** Evidence-gated investigation with a complete proposal.

1. Treat the November 8, 2026 date as the historical requested target, not a validated forecast. Do not silently reduce accepted Version 1 scope or declare M-02/M-03 complete to fit it. Complete analysis/design and decisive feasibility work before a delivery commitment.

2. Propose workstreams for estimation: requirements/owner review, full domain/behavior analysis, design/feasibility, identity/access, presentation/PDF/sharing, application/history, Google mail/calendar, work/Sprints, real Git collaboration, isolated execution/deployment, integrated quality/security/recovery, and operating documentation. Include learning, integration and rework in each estimate; do not count document size as engineering progress.

3. Build actual backlog links from reviewed criterion groups and justified technical investigations. Require item outcome, criteria, dependencies, effort range and readiness before Sprint selection. Plan only the next Sprint in detail; later Sprints stay forecast. A candidate contains exact source hashes/commit and scope, criteria, unresolved gates and actual owner disposition.

4. Use evidence-based effort ranges after decomposition and actual usable weekly time confirmation. Do not invent task hours, a new delivery date, GitHub issue IDs, completed Sprints or review approval. Record a measured throughput basis once execution exists. The present proposal package is an input to review, not that review's acceptance.

**Assessable review cases:** [RC-Q28-01 through RC-Q28-03](../04-scenarios-and-models/user-stories-and-scenarios.md#review-q-d28). These are planned checks, not executed results.

**Remaining evidence / acceptance condition:** Full analysis/design, decomposed estimates, confirmed usable numerical capacity, actual live-work mappings and owner baseline disposition do not yet exist. A credible completed forecast cannot be manufactured from the server inventory.

## November 1, 2026 — Q-D28 Capacity Evidence

The owner supplied 20 project hours/week. [Confirmed capacity and preliminary sizing](../../01-project-planning/11-capacity-and-preliminary-sizing.md) now answer the numerical availability input and expose the historical target conflict. Exact design-dependent effort, live tracking reconciliation and baseline disposition remain pending. This updates a current working constraint without changing requirement IDs or historical accepted scope.

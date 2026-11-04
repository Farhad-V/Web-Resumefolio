# Resumefolio — Requirements Specification Guide

Current implementation choices and scope: [Baseline](../../../baseline/README.md). Runtime verification remains subject to its gates.

| Item | Current position |
| --- | --- |
| Purpose | Navigate the distributed Software Requirements Specification (SRS), its detailed drafts and remaining review work |
| Owner | Farhad; sole project delivery and operations owner |
| Status | Proposed documentation set — M-02 requirements baseline pending |
| Inventory | 16 primary specification documents: 15 detailed proposed drafts and one SRS entry point; plus a supporting priority/readiness register |
| Candidate records | 157 provisional document-local records in the 15 detailed drafts; not final global IDs, approved requirements or verified capabilities |
| Revision | November 1, 2026 — functional/non-functional reading routes added |

**Start with [Functional Requirements](requirements-specification.md#functional-requirements) and [Non-Functional Requirements](requirements-specification.md#non-functional-requirements)** for explicit classification. Continue with **[the SRS entry point](requirements-specification.md)** for product
boundary and requirement levels. Use this guide to find the primary record owner,
choose a reading path and identify unfinished work. Keep detailed requirements in
their domain files rather than duplicating them in this index.

[Reading paths](#1-reading-paths) · [Documents](#documents)
· [Consistency](#3-cross-document-boundaries) · [Remaining work](#4-remaining-work-and-review-roadmap)
· [Diagrams](#5-diagram-catalog) · [Maintenance](#6-maintenance)

## 1. Reading Paths

| Your question | Suggested route |
| --- | --- |
| Why is the product needed, and what is its boundary? | [SRS](requirements-specification.md) → [Business outcomes](business-requirements.md) → [Accepted Scope](../../01-project-planning/02-scope.md) |
| Who needs what, and with which authority? | [Actors](../02-stakeholders-and-elicitation/actors-and-system-context.md) → [User Requirements](user-requirements.md) → [Accounts](accounts-authentication-and-permissions.md) → [Scenarios](../04-scenarios-and-models/user-stories-and-scenarios.md) |
| How do professional information and applications fit together? | [Profiles/Resumes](profiles-resumes-and-portfolio.md) → [PDF/Sharing](pdf-and-controlled-sharing.md) → [Applications](manual-application-management.md) → [Google Integration](email-calendar-and-google-integration.md) |
| How is collaborative work organized? | [Projects/Kanban/Sprints](projects-kanban-and-sprints.md) → [Git Hosting](git-hosting-and-collaboration.md) → [YAML/CI/CD](yaml-workflows-and-cicd.md) |
| Which rules apply across all features? | [Business Lifecycle](business-rules-and-data-lifecycle.md) → [Domain Constraints](domain-requirements-and-constraints.md) → [Interfaces](external-interface-requirements.md) → [Quality/Security/Recovery](quality-security-and-recovery-requirements.md) |
| What is needed to operate and review the release? | [Administration/Files](administration-files-and-operational-behavior.md) → [Quality/Recovery](quality-security-and-recovery-requirements.md) → [Traceability](../06-validation-and-traceability/requirements-traceability.md) → [Baseline criteria](../07-change-and-baseline/requirements-review-and-baseline-criteria.md) |

![Reading groups in the distributed specification](../diagrams/specification-reading-map.png)

[Scalable SVG](../diagrams/specification-reading-map.svg) ·
[Editable Graphviz](../diagrams/specification-reading-map.dot)

The map groups reading topics, not services, delivery increments or staffing.
Read cross-cutting rules alongside domain behavior. Colors supplement labels;
draft status and open decisions are explicit rather than distinguished by color alone.

## Documents

The table covers the 16 primary specification documents in this folder. The [priority/readiness register](requirements-priority-and-readiness.md) is a supporting attribute view, not an additional primary requirements draft.
**Detailed draft** means proposed records with criteria/methods/open decisions; it
does not mean the questions are resolved, the records approved or the product tested.

| Document | Primary responsibility | Current content / remaining boundary |
| --- | --- | --- |
| [Software Requirements Specification](requirements-specification.md) | SRS entry point, product boundary and requirement levels | Expanded overview, scope/primary ownership, conventions and review gates; baseline pending |
| [Business Requirements](business-requirements.md) | Intended business outcomes and success evidence | Detailed draft; 5 BIZ-D records; intended benefit is not measured benefit |
| [User Requirements](user-requirements.md) | Actor goals, contexts and expected outcomes | Detailed draft; 12 USR-D records; derived actor goals and scenarios still require owner review |
| [Accounts, Authentication and Permissions](accounts-authentication-and-permissions.md) | Identity, resource/action isolation, sharing and explicit administrative powers | Detailed draft; 12 ACC-D records; exact auth/grant/session policies pending |
| [Profiles, Resumes and Portfolio](profiles-resumes-and-portfolio.md) | Reusable information, independent tailoring, evidence and manual language variants | Detailed draft; 10 PRP-D records; fields, propagation and presentation policies pending |
| [PDF and Controlled Sharing](pdf-and-controlled-sharing.md) | Generated/uploaded PDFs, availability, employer links and direct retrieval | Detailed draft; 10 PDF-D records; rendition, session/revocation and lifecycle details pending |
| [Manual Application Management](manual-application-management.md) | Company/opportunity, manual cover letters, progress and actual submitted copies | Detailed draft; 9 APP-D records; capture, transitions, corrections and retention pending |
| [Email, Calendar and Google Integration](email-calendar-and-google-integration.md) | Authorized mail/calendar operations, synchronization and failures | Detailed draft; 12 EGC-D records; limited dated provider-source notes, actual project access unverified |
| [Projects, Kanban and Sprints](projects-kanban-and-sprints.md) | Boards, items/tasks, assignments, collaboration and Sprint Backlog | Detailed draft; 11 PKS-D records; relationships, workflows and completion policies pending |
| [Git Hosting and Collaboration](git-hosting-and-collaboration.md) | Real Git clients, repository presentation, forks/review/merge and tracking/releases | Detailed draft; 10 GIT-D records; transports, grants, review and lifecycle policies pending |
| [YAML Workflows and CI/CD](yaml-workflows-and-cicd.md) | Supported syntax/execution, isolation, secrets, limits and deployment controls | Detailed draft; 12 YML-D records; execution, isolation, limits and deployment policies/evidence pending |
| [Administration, Files and Operational Behavior](administration-files-and-operational-behavior.md) | Policy configuration, file admission, quotas, failures, cleanup and operational evidence | Detailed draft; 12 AFO-D records; limits, powers, accounting and retention pending |
| [Business Rules and Data Lifecycle](business-rules-and-data-lifecycle.md) | Cross-module invariants, ownership, updates, history, retirement and recovery | Detailed draft; 10 BRL-D records; detailed propagation/synchronization/removal rules pending |
| [Domain Requirements and Constraints](domain-requirements-and-constraints.md) | Domain meaning, product policies, project mandates and external applicability | Detailed draft; 8 DOM-D records; provider/legal/licensing applicability investigations incomplete |
| [External Interface Requirements](external-interface-requirements.md) | Eight boundary inventories and explicit interaction contracts | Detailed draft; 10 EIF-D records; exact protocols, representations, clients and actual access findings pending |
| [Quality, Security and Recovery](quality-security-and-recovery-requirements.md) | Measurement contracts, controls, capacity, backup coverage and demonstrated recovery | Detailed draft; 14 QSR-D records; targets, controls and actual verification/restoration pending |

Counts describe this working set on the revision date and require updating when
records change. Prefixes are local draft references; they do not establish the
final FR/NFR/business-rule identifier convention. No priority order or approval is
inferred from row order or document length.

## 3. Cross-document Boundaries

| Invariant | Read together |
| --- | --- |
| Shared profile information does not erase independent resume selections/layouts/overrides | PRP-D + BRL-D + dictionary |
| Current sources, live employer views and actual submitted copies have distinct meaning | PRP-D + PDF-D + APP-D + BRL-D |
| Employer links expose selected authorized content, including direct file/PDF paths | ACC-D + PDF-D + EIF-D + QSR-D |
| A downloaded copy cannot be recalled by disabling product retrieval | PDF-D + APP-D distinction + BRL-D |
| Unified sign-in or board membership supplies no unrelated private-resource grant | ACC-D + EGC-D + PKS-D + GIT-D |
| Product Backlog Item, task, board position and acceptance are not interchangeable | PKS-D + dictionary; Sprint Backlog includes goal, selected items and delivery plan |
| Real Git hosting differs from development GitHub; Push/merge does not inherently authorize deployment | GIT-D + YML-D + EIF-D + QSR-D |
| Provider guidance differs from actual project access; synchronization direction must be decided | EGC-D + DOM-D + BRL-D + feasibility findings |
| Backup existence differs from demonstrated usable, consistent and safely authorized recovery | QSR-D + AFO-D + domain artifacts/access + actual later evidence |

Detailed permissions, lifecycles and numerical targets remain open. These rows
summarize review boundaries; primary candidate wording remains in the linked files.

## 4. Remaining Work and Review Roadmap

The set is organized, but the requirements baseline is not complete. In particular:

1. Review the new actor-specific **User Requirements** and detailed **YAML/CI/CD** records; resolve open goal, execution and deployment policies while retaining explicit gates.
2. Resolve affected fields, relationships, state/transition, authority, propagation, language, capture, synchronization and retention questions with actual owner decisions.
3. Establish measurable quality/resource/recovery criteria and actual provider/feasibility findings at their dependent gates; do not invent targets or assume access.
4. Reconcile the SRS entry point, dictionary, scenarios and all domain drafts; allocate the final identifier convention and justified priorities.
5. Populate actual traceability and review findings, assess unresolved blockers and record owner review against an identifiable candidate before M-02 acceptance.

![Evidence-based route from draft specification to a separate baseline decision](../diagrams/specification-baseline-review.png)

[Scalable SVG](../diagrams/specification-baseline-review.svg) ·
[Editable PlantUML](../diagrams/specification-baseline-review.puml)

This is a review roadmap, not a dated forecast or proof that a gate has passed.
Investigate decisive feasibility/security questions early and iterate related
requirements together. M-02 review is separate from product verification/release.
The agreed initial SDLC documentation, analysis/design, tracking reconciliation
and pre-implementation agreement still precede product coding.

| Supporting source / register | Use |
| --- | --- |
| [Version 1 Scope](../../01-project-planning/02-scope.md) | Accepted inclusions/exclusions and conditional commitments |
| [Resources](../../01-project-planning/05-resources-and-constraints.md) / [Planning Gates](../../01-project-planning/10-planning-completion-criteria.md) | Existing constraints, planning-only acceptance and retained GAP-D follow-up |
| [Elicitation Plan](../02-stakeholders-and-elicitation/elicitation-plan-and-techniques.md) / [Log](../02-stakeholders-and-elicitation/elicitation-log.md) | Planned clarification versus actual documented source extraction |
| [Dictionary](../05-data-definitions/data-dictionary.md) / [Scenarios](../04-scenarios-and-models/user-stories-and-scenarios.md) | Shared meaning and actor/normal/alternative/denied/failure examples |
| [Questions and Decisions](../07-change-and-baseline/open-questions-and-decisions.md) / [Change Control](../07-change-and-baseline/change-control.md) | Actual decisions, impact and unresolved commitments |
| [Traceability](../06-validation-and-traceability/requirements-traceability.md) / [Review Findings](../06-validation-and-traceability/review-plan-and-findings.md) | Allocated links, actual inspections, dispositions and rechecks |
| [Baseline Criteria](../07-change-and-baseline/requirements-review-and-baseline-criteria.md) | Separate acceptance conditions and identifiable owner outcome |

No current documentation count, rendered diagram or link check establishes a
product Pass, provider approval, recovery result, M-02 completion or new baseline
acceptance. Accepted planning history remains attached to its identified snapshot.

## 5. Diagram Catalog

Every row links editable source and SVG/PNG output. The catalog includes two guide
diagrams, two SRS diagrams and the 30 diagrams referenced by the 15 detailed drafts. None is an
implemented architecture or an executed test result.

| Topic / diagram | Editable source | SVG | PNG |
| --- | --- | --- | --- |
| Guide: reading map | [DOT](../diagrams/specification-reading-map.dot) | [SVG](../diagrams/specification-reading-map.svg) | [PNG](../diagrams/specification-reading-map.png) |
| Guide: baseline review | [PUML](../diagrams/specification-baseline-review.puml) | [SVG](../diagrams/specification-baseline-review.svg) | [PNG](../diagrams/specification-baseline-review.png) |
| Accounts, Authentication and Permissions — accounts access contexts | [DOT](../diagrams/accounts-access-contexts.dot) | [SVG](../diagrams/accounts-access-contexts.svg) | [PNG](../diagrams/accounts-access-contexts.png) |
| Accounts, Authentication and Permissions — accounts request authorization | [PUML](../diagrams/accounts-request-authorization.puml) | [SVG](../diagrams/accounts-request-authorization.svg) | [PNG](../diagrams/accounts-request-authorization.png) |
| Administration, Files and Operational Behavior — administration file admission flow | [PUML](../diagrams/administration-file-admission-flow.puml) | [SVG](../diagrams/administration-file-admission-flow.svg) | [PNG](../diagrams/administration-file-admission-flow.png) |
| Administration, Files and Operational Behavior — administration files policy map | [DOT](../diagrams/administration-files-policy-map.dot) | [SVG](../diagrams/administration-files-policy-map.svg) | [PNG](../diagrams/administration-files-policy-map.png) |
| Business Requirements — business outcome assessment | [PUML](../diagrams/business-outcome-assessment.puml) | [SVG](../diagrams/business-outcome-assessment.svg) | [PNG](../diagrams/business-outcome-assessment.png) |
| Business Requirements — business outcomes map | [DOT](../diagrams/business-outcomes-map.dot) | [SVG](../diagrams/business-outcomes-map.svg) | [PNG](../diagrams/business-outcomes-map.png) |
| Business Rules and Data Lifecycle — data lifecycle boundaries | [DOT](../diagrams/data-lifecycle-boundaries.dot) | [SVG](../diagrams/data-lifecycle-boundaries.svg) | [PNG](../diagrams/data-lifecycle-boundaries.png) |
| Business Rules and Data Lifecycle — data retirement review | [PUML](../diagrams/data-retirement-review.puml) | [SVG](../diagrams/data-retirement-review.svg) | [PNG](../diagrams/data-retirement-review.png) |
| Domain Requirements and Constraints — domain authority map | [DOT](../diagrams/domain-authority-map.dot) | [SVG](../diagrams/domain-authority-map.svg) | [PNG](../diagrams/domain-authority-map.png) |
| Domain Requirements and Constraints — domain constraint review | [PUML](../diagrams/domain-constraint-review.puml) | [SVG](../diagrams/domain-constraint-review.svg) | [PNG](../diagrams/domain-constraint-review.png) |
| Email, Calendar and Google Integration — google integration context | [DOT](../diagrams/google-integration-context.dot) | [SVG](../diagrams/google-integration-context.svg) | [PNG](../diagrams/google-integration-context.png) |
| Email, Calendar and Google Integration — google operation outcomes | [PUML](../diagrams/google-operation-outcomes.puml) | [SVG](../diagrams/google-operation-outcomes.svg) | [PNG](../diagrams/google-operation-outcomes.png) |
| External Interface Requirements — external interface context | [DOT](../../04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot) | [SVG](../../04-system-design/01-software-architecture/diagrams/logical-component-ownership.svg) | [PNG](../../04-system-design/01-software-architecture/diagrams/logical-component-ownership.png) |
| External Interface Requirements — external interface outcomes | [PUML](../diagrams/external-interface-outcomes.puml) | [SVG](../diagrams/external-interface-outcomes.svg) | [PNG](../diagrams/external-interface-outcomes.png) |
| Git Hosting and Collaboration — git hosting capability map | [DOT](../diagrams/git-hosting-capability-map.dot) | [SVG](../diagrams/git-hosting-capability-map.svg) | [PNG](../diagrams/git-hosting-capability-map.png) |
| Git Hosting and Collaboration — git review merge flow | [PUML](../diagrams/git-review-merge-flow.puml) | [SVG](../diagrams/git-review-merge-flow.svg) | [PNG](../diagrams/git-review-merge-flow.png) |
| Manual Application Management — application submission capture | [PUML](../diagrams/application-submission-capture.puml) | [SVG](../diagrams/application-submission-capture.svg) | [PNG](../diagrams/application-submission-capture.png) |
| Manual Application Management — manual application history map | [DOT](../diagrams/manual-application-history-map.dot) | [SVG](../diagrams/manual-application-history-map.svg) | [PNG](../diagrams/manual-application-history-map.png) |
| PDF and Controlled Sharing — pdf protected retrieval | [PUML](../diagrams/pdf-protected-retrieval.puml) | [SVG](../diagrams/pdf-protected-retrieval.svg) | [PNG](../diagrams/pdf-protected-retrieval.png) |
| PDF and Controlled Sharing — pdf sharing boundaries | [DOT](../diagrams/pdf-sharing-boundaries.dot) | [SVG](../diagrams/pdf-sharing-boundaries.svg) | [PNG](../diagrams/pdf-sharing-boundaries.png) |
| Profiles, Resumes and Portfolio — profile resume evidence map | [DOT](../diagrams/profile-resume-evidence-map.dot) | [SVG](../diagrams/profile-resume-evidence-map.svg) | [PNG](../diagrams/profile-resume-evidence-map.png) |
| Profiles, Resumes and Portfolio — profile update review | [PUML](../diagrams/profile-update-review.puml) | [SVG](../diagrams/profile-update-review.svg) | [PNG](../diagrams/profile-update-review.png) |
| Projects, Kanban and Sprints — kanban sprint concept map | [DOT](../diagrams/kanban-sprint-concept-map.dot) | [SVG](../diagrams/kanban-sprint-concept-map.svg) | [PNG](../diagrams/kanban-sprint-concept-map.png) |
| Projects, Kanban and Sprints — sprint planning review flow | [PUML](../diagrams/sprint-planning-review-flow.puml) | [SVG](../diagrams/sprint-planning-review-flow.svg) | [PNG](../diagrams/sprint-planning-review-flow.png) |
| Quality, Security and Recovery Requirements — quality evidence map | [DOT](../diagrams/quality-evidence-map.dot) | [SVG](../diagrams/quality-evidence-map.svg) | [PNG](../diagrams/quality-evidence-map.png) |
| Quality, Security and Recovery Requirements — recovery evidence roadmap | [PUML](../diagrams/recovery-evidence-roadmap.puml) | [SVG](../diagrams/recovery-evidence-roadmap.svg) | [PNG](../diagrams/recovery-evidence-roadmap.png) |
| Software Requirements Specification — srs baseline decision | [PUML](../diagrams/srs-baseline-decision.puml) | [SVG](../diagrams/srs-baseline-decision.svg) | [PNG](../diagrams/srs-baseline-decision.png) |
| Software Requirements Specification — srs traceability map | [DOT](../diagrams/srs-traceability-map.dot) | [SVG](../diagrams/srs-traceability-map.svg) | [PNG](../diagrams/srs-traceability-map.png) |
| User Requirements — user goal map | [DOT](../diagrams/user-goal-map.dot) | [SVG](../diagrams/user-goal-map.svg) | [PNG](../diagrams/user-goal-map.png) |
| User Requirements — user requirement review | [PUML](../diagrams/user-requirement-review.puml) | [SVG](../diagrams/user-requirement-review.svg) | [PNG](../diagrams/user-requirement-review.png) |
| YAML Workflows and CI/CD — workflow execution boundaries | [DOT](../diagrams/workflow-execution-boundaries.dot) | [SVG](../diagrams/workflow-execution-boundaries.svg) | [PNG](../diagrams/workflow-execution-boundaries.png) |
| YAML Workflows and CI/CD — workflow run control flow | [PUML](../diagrams/workflow-run-control-flow.puml) | [SVG](../diagrams/workflow-run-control-flow.svg) | [PNG](../diagrams/workflow-run-control-flow.png) |

## 6. Maintenance

When a specification changes, update its sources, status, criteria, open decisions,
related dictionary/scenario/traceability links and diagrams together. Keep this
catalog and record counts accurate. Read primary records before summarizing them;
do not copy detailed obligations into multiple competing files.

Check local file/section links, readable labels/arrows, table layout and synchronized
editable/rendered diagrams. Render the two guide diagrams from repository root:

```powershell
$diagramFolder = 'docs\MVP\SDLC\02-requirements-engineering\diagrams'
$graphvizExe = 'C:\Program Files\Graphviz\bin\dot.exe'
$plantUmlJar = 'C:\Users\fvali\AppData\Local\Resumefolio\DiagramTools\plantuml.jar'
foreach ($format in 'svg', 'png') {
    & $graphvizExe "-T$format" -Gdpi=140 "$diagramFolder\specification-reading-map.dot" -o "$diagramFolder\specification-reading-map.$format"
    if ($LASTEXITCODE -ne 0) { throw "Graphviz failed: $format" }
    java '-Djava.awt.headless=true' -jar $plantUmlJar -charset UTF-8 "-t$format" "$diagramFolder\specification-baseline-review.puml"
    if ($LASTEXITCODE -ne 0) { throw "PlantUML failed: $format" }
}
```

Use actual installed paths on other machines. Save UTF-8 without BOM and retain
source/SVG/PNG outputs together. See the [shared diagram guide](../diagrams/README.md).

[Requirements index](../README.md) · [SRS entry point](requirements-specification.md)

## Course-Aligned Refinement — November 1, 2026

Use the [proposed priority/readiness register](requirements-priority-and-readiness.md) as a supporting attribute view, not a sixteenth primary requirement draft. The 15 primary drafts still contain 157 candidates. Their actual priorities remain unassigned; proposals are explicitly separate. Quality targets have decision contracts, and external scenario narratives are separated from later verification steps. M-02 remains pending.

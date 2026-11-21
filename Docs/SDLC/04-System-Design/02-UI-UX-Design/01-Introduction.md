# 1. Introduction to UI/UX Design

[Next: Design Goals and Principles](02-Design-Goals-And-Principles.md)

Part of the [Software Design Document](../../01-Project-Planning/02-Project-Management-Plan.md#stage-4-system-design).

## Purpose

The UI/UX design describes how invited users, employer viewers, repository collaborators and administrators understand and operate the Resumefolio MVP. It translates required behavior into information structure, user journeys, screen states, interaction feedback and accessible presentation.

The experience must make consequential choices clear: editing a profile is different from applying selected changes to a tailored draft; saving a draft is different from publishing; publication is different from PDF availability; and a recorded submission preserves what was actually submitted. The interface must communicate these distinctions without requiring users to understand the underlying architecture.

This chapter introduces scope, users, shared experience boundaries and the design handoff. Detailed screens, tokens, validation patterns and prototype behavior belong in the linked UI/UX chapters. Completing documentation does not establish an implemented interface, validated usability findings or passed accessibility checks.

## Scope

### Core Workspace

| Journey | Experience covered | Boundary to preserve |
| --- | --- | --- |
| Invited admission and account access | Invitation, sign-in, selected recovery/admin interactions and current access feedback | Invitation-based scope and server-enforced authority |
| Professional content | Private profile, tailored resumes/portfolios, independent drafts and manually maintained language variants | Source edits do not silently change existing drafts or submitted history |
| Explicit updates and publication | Compare/select/apply changes, preview and separate publication confirmation | User intent and affected revision/content remain clear |
| Files and PDF | Private upload/library selection, processing status and eligible representations | Uploaded, usable, selected, published and downloadable are distinct states |
| Employer sharing | Owner-side sharing controls and focused recipient-facing views | Expose only the currently allowed selection; no broader workspace access |
| Manual applications | Application progress, follow-up, cover letters and exact submitted-material history | Recording a manual submission does not imply automatic employer delivery |

### ProjectForge Journeys

Cover authorized repository summaries, files/history, real Git access guidance, issues and simple Kanban. Keep repository permissions and unavailable/denied outcomes understandable. A permitted issue action does not imply Git write authority. Core and ProjectForge remain independent systems with separate session and resource boundaries, even where navigation connects the experience.

### Outside MVP

Personal mail/calendar, AI, automatic translation, advanced repository review/releases, general Sprints and user workflow/deployment execution remain deferred. Developer CI/CD and operator recovery procedures support the product lifecycle; they are not user-facing workflow-execution features introduced by this design.

## Users and Experience Context

| Role | Primary need | Design implication |
| --- | --- | --- |
| Invited account holder / applicant | Tailor materials deliberately and trust the recorded history | Clear source/draft/publication labels, explicit selection and discoverable exact submitted materials |
| Employer / share recipient | Read the intended professional presentation without entering the owner's workspace | Focused content, understandable access errors and only eligible download actions |
| Repository collaborator | Find permitted repository work and understand action limits | Resource-specific actions, stable issue identity, conflict handling and accurate Git permission guidance |
| Administrator | Perform selected account/operational duties safely | Clear action scope and bounded feedback; administrator status does not imply unrestricted private-content access |

These are role-based design profiles, not claims of completed user research. One person may act in several roles without their permissions merging. See [Users](03-Users.md) for task/context validation and [Usability Testing](12-Usability-Testing.md) for planned sessions and actual findings.

Design for intended desktop/mobile browser use, keyboard operation and assistive technology. Record tested browser, viewport and input configurations rather than claiming universal support. Documentation diagrams use dark mode; that preference does not select the product's visual theme or prove its contrast/accessibility.

## Shared Experience Boundaries

### Content, Publication and Historical Truth

Preserve the [accepted update/publication policy](../../02-Requirements-Engineering/01-Software-Requirements-Specification.md#change-and-baseline-open-questions-and-decisions--id-owner-accepted-profile-update-policy). Changes are previewed/selected/applied explicitly, publication requires its own confirmation, and independently authored text and actual submitted materials remain preserved.

The interface must identify the material being edited or viewed and the operation that completed. Avoid a single ambiguous “saved” message for draft persistence, publication, PDF creation and remote effects. A history view must resolve exact retained material rather than silently showing today's live resume.

### Permissions and Recipient Access

Current authorization is enforced by the server at the receiving resource owner. Hidden or disabled controls explain available actions but cannot enforce security. Direct file requests, alternate routes and native Git transport retain their own checks.

An employer viewer context is link-scoped and does not prove a named employer identity or create an account. A withdrawn share changes future access under policy; the UI must not promise to recall already delivered/downloaded bytes. Owner-side sharing actions, publication state and PDF/download configuration remain distinct controls.

### Feedback, Conflicts and Uncertain Work

Distinguish validation errors, denied/hidden resources, stale-version conflicts, pending processing, unavailable dependencies and confirmed success. Preserve permitted input and offer the contract-defined recovery path. Announce relevant state changes accessibly without unexpected focus movement.

A timeout or lost response may leave an operation's result uncertain. Offer status resolution or reconciliation under the same recorded operation rather than implying failure and encouraging a duplicate consequential action. Queue acceptance is not proof that a PDF, mail delivery or ProjectForge write completed.

See [Interaction and Feedback](09-Interaction-And-Feedback.md), [User Flows](05-User-Flows.md) and the [API specification](../03-Low-Level-Design/05-API-Specification.md) for state/result details.

### Language, Layout and Accessibility

The current design uses English interface copy and manually maintained English/German professional content. Content language is separate from interface language, uploaded-document language and user-local follow-up context. Automatic translation is outside scope; unresolved fallback/completeness rules retain their governing status.

At narrow widths, keep essential content/actions reachable in reading order; use additional space for supporting preview where appropriate. Test long labels/content and validation messages without hiding consequential controls. Accessibility checks must cover actual navigation, forms, feedback, focus and recipient views, not just isolated styling.

See [Accessibility](10-Accessibility.md) and [Responsive and Localization](11-Responsive-And-Localization.md). Do not introduce an unsupported conformance level or browser/device commitment here.

## Design Deliverables and Reading Guide

| Chapter group | Deliverable |
| --- | --- |
| [Goals and principles](02-Design-Goals-And-Principles.md), [Users](03-Users.md) | Experience priorities, role tasks and design assumptions |
| [Information architecture](04-Information-Architecture.md), [User flows](05-User-Flows.md) | Navigation, content organization, decision points and normal/failure journeys |
| [Wireframes and prototypes](06-Wireframes-And-Prototypes.md), [Design system](07-Design-System.md) | Reviewable layouts and reusable presentation rules |
| [Screen specifications](08-Screen-Specifications.md), [Interaction and feedback](09-Interaction-And-Feedback.md) | Screen states, action behavior, validation, conflicts and consequential confirmations |
| [Accessibility](10-Accessibility.md), [Responsive/localization](11-Responsive-And-Localization.md) | Inclusive behavior, viewport adaptation and language/content presentation |
| [Usability testing](12-Usability-Testing.md) | Planned tasks, observation method and actual findings when executed |
| [Development handoff](13-Handoff-To-Development.md), [Traceability](14-Traceability.md) | Implementable behavior, ownership, exact criteria and verification links |
| [Appendices](15-Appendices.md) | Supporting records and retained reference material |

Architectural relationships are documented in the [HLD System Context](../01-High-Level-Design/03-System-Context.md). User-journey diagrams belong with User Flows. Maintain UML views as editable dark-mode PlantUML with matching rendered assets.

## References

| Reference | Authority |
| --- | --- |
| [Project charter](../../01-Project-Planning/01-Project-Charter.md#mvp-scope) | Accepted product scope |
| [SRS](../../02-Requirements-Engineering/01-Software-Requirements-Specification.md) and [user stories/scenarios](../../02-Requirements-Engineering/01-Software-Requirements-Specification.md#scenarios-and-models-user-stories-and-scenarios) | Required user behavior, definitions and criterion status |
| [Interface requirements](../../02-Requirements-Engineering/01-Software-Requirements-Specification.md#requirements-specification-external-interface-requirements) and [quality/accessibility disposition](../../02-Requirements-Engineering/01-Software-Requirements-Specification.md#requirements-specification-quality-security-and-recovery-requirements--id-resolution-q-d25) | Interaction/accessibility constraints and unresolved targets |
| [Analysis interactions](../../03-System-Analysis/03-Processes-Scenarios-And-Business-Rules.md#analysis-behavioral-and-scenario-analysis--06-scenario-based-view) | Logical scenarios and behavior inputs |
| [HLD](../01-High-Level-Design/01-Introduction.md) and [Security Architecture](../01-High-Level-Design/10-Security-Architecture.md) | System ownership, current authority and private-content boundaries |
| [Component design](../03-Low-Level-Design/02-Module-Breakdown.md#design-record-03-component-and-module-design-component-and-module-design-md) and [Detailed Module Design](../03-Low-Level-Design/03-Detailed-Module-Design.md) | Owning operations and invariants |
| [API specification](../03-Low-Level-Design/05-API-Specification.md) | Permitted results, errors, request identity and retry semantics |
| [Frontend ADR](../ADR/ADR-007-React-Inertia-Frontend.md) | React/Inertia inside independent Laravel applications, with trusted Blade PDF templates |
| [RTM](../../02-Requirements-Engineering/03-Requirements-Traceability-Matrix.md) | Exact criteria, scope disposition and implementation/execution evidence |

## Design Authority and Handoff

Business meaning remains with governing requirements, source decisions and owning components, not button labels or visual prototypes. UI/UX specifies how required actions and results are understood and operated. Resolve a disagreement against the accepted requirement/decision before changing the product behavior.

Before implementation, identify the exact actor/task, resource/version, prerequisite, allowed action, expected result and denied/conflict/pending/unavailable states. Supply keyboard/focus, validation, responsive and language behavior where relevant. Link the screen/flow to its owning contract and criterion rather than relying on a picture alone.

Before acceptance, record observations on the actual candidate, including normal and relevant failure journeys, accessibility checks and usability evidence. Keep assumed needs separate from observed findings and planned checks separate from executed results. Update the affected UI/UX chapters, contracts, diagrams and RTM together when behavior changes.

## Existing Design Records

<a id="1-sources-and-experience-boundaries"></a>

### Sources and Experience Boundaries

The references and shared-boundary guidance above consolidate the existing introductory record. Interface wording cannot override the accepted update/publication policy, content-language separation, current authority or truthful result semantics. Retained detailed material is available through the [UI/UX appendices](15-Appendices.md).


## Sections

1. Introduction (this document)
2. [Design Goals And Principles](02-Design-Goals-And-Principles.md)
3. [Users](03-Users.md)
4. [Information Architecture](04-Information-Architecture.md)
5. [User Flows](05-User-Flows.md)
6. [Wireframes And Prototypes](06-Wireframes-And-Prototypes.md)
7. [Design System](07-Design-System.md)
8. [Screen Specifications](08-Screen-Specifications.md)
9. [Interaction And Feedback](09-Interaction-And-Feedback.md)
10. [Accessibility](10-Accessibility.md)
11. [Responsive And Localization](11-Responsive-And-Localization.md)
12. [Usability Testing](12-Usability-Testing.md)
13. [Handoff To Development](13-Handoff-To-Development.md)
14. [Traceability](14-Traceability.md)
15. [Appendices](15-Appendices.md)

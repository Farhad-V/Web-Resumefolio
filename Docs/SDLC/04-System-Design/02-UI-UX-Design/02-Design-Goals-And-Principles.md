# 2. Design Goals And Principles

[Previous: Introduction](01-Introduction.md) · [UI/UX Design introduction](01-Introduction.md) · [Next: Users](03-Users.md)

## UX Goals

The MVP experience should help users prepare professional materials deliberately, understand what a recipient can access and trust the record of what they submitted. Interface clarity must preserve the underlying business boundaries rather than hiding them behind a generic save/share action.

| Goal | Intended user outcome | Design response | Verification focus |
| --- | --- | --- | --- |
| Deliberate tailoring | Reuse profile information without losing independent draft choices | Preview/select/apply changes with a clear target and current draft context | User identifies affected fields and completes or cancels the selected update without unintended propagation |
| Predictable publication | Understand when private work becomes available under sharing policy | Separate draft save from publication confirmation; show the selected revision/content | User distinguishes saved draft, published snapshot and currently shared material |
| Focused employer access | Read only the intended professional presentation | Recipient view prioritizes selected content and eligible downloads, without owner workspace controls | Authorized/denied/link-change journeys expose only the allowed selection |
| Trustworthy application history | Retrieve the actual submitted materials after later edits | History identifies the recorded submission and exact retained material rather than today's live resume | User finds the original material and understands its distinction from the current draft/publication |
| Understandable repository work | Find permitted files/history, issues and board actions | Resource-scoped navigation, clear permission feedback and stable issue identity | User completes authorized work and understands denied, stale or unavailable outcomes |
| Recoverable interaction | Know whether an action completed and what can safely happen next | Distinct validation, conflict, pending, unavailable and confirmed states; preserve permitted input | User recovers without losing safe work or repeating an uncertain consequential effect |
| Inclusive operation | Complete essential journeys using intended input and viewport conditions | Semantic controls, keyboard paths, visible focus, responsive content and accessible feedback | Actual journey-level accessibility/usability observations on recorded configurations |

These are design objectives, not observed research findings or invented numerical acceptance thresholds. Exact expected outcomes and criterion status remain in the [SRS](../../02-Requirements-Engineering/01-Software-Requirements-Specification.md) and [RTM](../../02-Requirements-Engineering/03-Requirements-Traceability-Matrix.md).

## Design Principles

### 2.1 Make the Current Material and Context Clear

Identify whether the user is editing source profile content, an independent tailored draft, publication settings or an immutable submission record. Show meaningful revision/language context where it affects the action. Avoid asking users to infer the active target from a route, icon or remembered navigation step.

Use task language in the product: selecting content, saving a draft, publishing selected material and viewing a submitted copy. Keep database keys, outbox terminology and internal service details out of normal flows unless an operation reference helps resolve a failure.

### 2.2 Separate Consequential Intent

Draft apply, publication, sharing configuration and manual submission capture are different operations. Give each an explicit purpose and accurately scoped confirmation where consequences warrant it. State what changes, which material is affected and the next permitted step.

Do not auto-publish through a save action, silently apply every profile edit to existing drafts, or imply that recording a manual application sends it to an employer. Changing download mode must not silently rotate a password or disable a share unless the governing contract explicitly requires that operation.

### 2.3 Use Consistent Language and Action Hierarchy

Keep terminology consistent across navigation, headings, buttons, validation and history. Label actions with the operation they perform and keep the primary task visually clear within its section. Supporting preview, comparison and secondary actions must remain discoverable without competing with consequential confirmation.

Use readable text labels for status and unfamiliar icons. Color or position alone must not carry publication, permission or error meaning. Define reusable visual treatments in [Design System](07-Design-System.md), preserving the same behavioral meaning across screens.

### 2.4 Show Accurate Outcomes

| Outcome | Feedback obligation | Safe next action |
| --- | --- | --- |
| Validation failure | Identify correctable input and associate feedback with the field/context | Correct input without losing unrelated permitted work |
| Denied or hidden resource | Provide policy-appropriate feedback without disclosing private information | Return to an allowed context or follow the applicable access route |
| Stale-version conflict | Explain that newer state prevents the requested write | Review/compare current state before resubmitting |
| Accepted / processing | Name the pending operation and distinguish acceptance from completion | Observe status without duplicate submission |
| Unavailable dependency | State that the required capability cannot currently establish/complete its contract | Use the documented retry/status path |
| Unknown remote outcome | Avoid claiming either completion or rollback without evidence | Resolve the recorded operation outcome before an unsafe repeat |
| Confirmed completion | Name exactly what completed and the affected material | Continue from the recorded result |

A successful draft save does not prove publication, PDF availability, mail delivery or a ProjectForge write. Avoid transient-only messages for unresolved conflicts or consequential pending work. See [Interaction and Feedback](09-Interaction-And-Feedback.md) for detailed patterns.

### 2.5 Preserve Work and Provide Recovery

Keep safe user input available after correctable errors and conflicts. Explain navigation/confirmation consequences where unsaved edits could be lost. Do not promise preservation of sensitive content beyond the selected privacy/session policy.

A disabled action should have understandable context where that helps the user, but it is not an authorization mechanism. Do not offer an unconditional repeat action for work whose remote outcome is unknown. Cancellation intent is not proof that a dispatched effect stopped.

### 2.6 Design Complete Accessible Journeys

Use native semantic controls, meaningful labels, keyboard-operable actions and visible focus. Maintain logical reading/focus order, usable validation and appropriate focus restoration. Provide an operable alternative when interaction would otherwise depend only on drag, hover, color or precise pointer placement.

Accessibility covers complete forms, dialogs, publication/sharing, protected views and repository journeys. The [Accessibility chapter](10-Accessibility.md) identifies WCAG 2.2 AA as the planned target; preserve its proposed/verification status and assess applicable criteria on the actual implementation. Do not claim conformance from a component screenshot or automated scan alone. PDF accessibility requires its separate evaluation.

### 2.7 Adapt Without Hiding Essential Meaning

Use available width to support comparison/preview, and stack content in a meaningful order on narrow layouts. Keep essential actions, labels, relationships and feedback reachable. For genuinely two-dimensional tables/boards, provide understandable navigation and useful detail/list alternatives rather than removing required information.

Support long English/German professional content and validation feedback without brittle fixed-height assumptions. Content language, interface language and document language remain separate. Current interface copy is English, professional variants are manually maintained, and automatic translation remains outside MVP scope. See [Responsive and Localization](11-Responsive-And-Localization.md).

### 2.8 Respect Privacy and Current Authority

Employer views expose only selected eligible content; they do not reveal the owner workspace or private application history. A link-scoped viewer is not proof of named employer identity. Explain access changes accurately without promising recall of bytes already downloaded.

Repository actions reflect current permitted scope. Issue-write permission is not Git write authority. Administrators receive only their selected duties, not assumed unrestricted content access. Every protected request is authorized by the server owner, including direct-file and Git paths; hidden UI controls cannot enforce permission.

## Constraints

| Constraint | Design implication |
| --- | --- |
| React/Inertia inside independent Laravel applications | Design server-authorized page/form journeys; do not introduce a separate browser REST-authentication layer or imply a shared Core/ProjectForge session |
| Explicit update/publication and preserved history | Keep draft, publication, selected delivery and actual submission states distinct |
| Private media and controlled delivery | Use eligible selection and current policy, not exposed filesystem paths or unrestricted URLs |
| Scoped ProjectForge integration and native Git | Distinguish browser/API/Git authority and accurate unavailable outcomes |
| Visual branding, palette and typography pending | Establish tokens in Design System; do not present arbitrary brand values as selected |
| Intended browser/mobile/keyboard/assistive use | Verify actual configurations and journeys; do not invent universal compatibility claims |
| Deferred capabilities | Personal mail/calendar, AI, advanced review/releases, general Sprints and user workflow execution do not enter MVP flows |
| Dark-mode PlantUML documentation | Use editable PlantUML and matching renders for UML; diagram styling does not select the product UI theme |

The [frontend ADR](../ADR/ADR-007-React-Inertia-Frontend.md), [accepted update/publication policy](../../02-Requirements-Engineering/01-Software-Requirements-Specification.md#change-and-baseline-open-questions-and-decisions--id-owner-accepted-profile-update-policy) and [HLD](../01-High-Level-Design/01-Introduction.md) govern these boundaries.

## Experience Acceptance

Review representative tasks with the actor, starting state, intended action, expected outcome and permitted recovery path identified. Record observed behavior rather than assuming a visible primary button makes a task understandable.

| Review question | Evidence to collect |
| --- | --- |
| Can the user identify what they are editing or viewing? | Correct recognition of source/draft/publication/submission context and relevant language/revision |
| Does the user understand the consequence before confirming? | Correct selection and explanation of apply, publish, share or record-submission intent |
| Can a recipient find intended material without seeing private content? | Authorized selection and appropriate denied/changed-access behavior |
| Does feedback distinguish completed, pending, conflicting and uncertain work? | Correct next step without accidental duplicate consequential action |
| Can the task be completed with intended input/viewport conditions? | Keyboard/focus, reflow, validation and assistive-technology observations as applicable |
| Does later change preserve historical understanding? | Retrieval of exact submitted materials after edits, withdrawal or replacement |

Use the existing criterion-linked checks and [Usability Testing](12-Usability-Testing.md) method. Do not assign arbitrary task-time, success-rate or participant-count targets here. Unexecuted reviews remain planned; failures or missing policy inputs require follow-up before claiming acceptance.

## Handoff and Change Review

For each affected screen/flow, specify actor/resource context, permitted actions, validation, normal and failure states, consequential confirmation, focus/keyboard behavior and responsive/language handling. Link the owning operation/API contract and exact requirement criterion.

When a shared pattern changes, inspect all affected screens and the protected direct-request behavior. Update [User Flows](05-User-Flows.md), [Screen Specifications](08-Screen-Specifications.md), Design System and [UI/UX Traceability](14-Traceability.md) as applicable. Record actual candidate-specific results centrally in the RTM rather than duplicating unsupported passes across chapters.

These principles guide design decisions; they do not constitute implemented controls, completed user research, passed accessibility tests or release approval.

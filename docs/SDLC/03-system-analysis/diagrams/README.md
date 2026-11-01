# System Analysis — Diagram Catalog

Revision: November 1, 2026. Active sources are **PlantUML `.puml`** and native **BPMN `.bpmn`**, with SVG and PNG exports. The catalog covers reviewed documents 00–03 and the populated data (05), scenario (06), state (07), activity (08), rule (09) and contract (10) and consistency-review (11) and interface (12) and security/quality/operating (13) and handoff (14) views. Functional and behavioral views are populated; exact semantic review and phase acceptance remain separate work.

## Reading and Maintenance Rules

- Activity diagrams show decisions and control flow; class associations do not show execution order.
- Context associations identify actors/participants and logical exchanges; dependency notation is explained next to each figure.
- Class diagrams show concepts and semantic properties. Detailed responsibilities, policy status and sources stay in the nearby tables.
- Multiplicity is shown only when justified. Unlabeled association ends are intentionally unspecified, not one-to-one.
- Every active figure has one matching `.puml`, `.svg` and `.png` set. Render locally with PlantUML; no remote service is required.
- Earlier `.dot` sources are retained as historical artifacts and are not authoritative for the revised images. Do not regenerate current figures from them.

| Document / section | Figure | Notation | Source | SVG | PNG |
|---|---|---|---|---|---|
| 00 / section 2 | System Analysis — iterative working route | Activity / analysis process | [PlantUML](start-here-analysis-route.puml) | [SVG](start-here-analysis-route.svg) | [PNG](start-here-analysis-route.png) |
| 00 / section 3 | Accepted core — explicit apply and separate publication | Activity / accepted successful path | [PlantUML](start-here-profile-publication.puml) | [SVG](start-here-profile-publication.svg) | [PNG](start-here-profile-publication.png) |
| 01 / section 2 | Analysis — source authority and feedback | Artifact dependency | [PlantUML](analysis-inputs-and-outputs.puml) | [SVG](analysis-inputs-and-outputs.svg) | [PNG](analysis-inputs-and-outputs.png) |
| 01 / section 4 | Seven views — complementary questions, one coherent model | Model-view map | [PlantUML](analysis-seven-view-consistency.puml) | [SVG](analysis-seven-view-consistency.svg) | [PNG](analysis-seven-view-consistency.png) |
| 02 / section 2 | Resumefolio — human roles and authority contexts | UML actor / system context | [PlantUML](system-context-human.puml) | [SVG](system-context-human.svg) | [PNG](system-context-human.png) |
| 02 / section 3 | Resumefolio — clients, providers and operating dependencies | Logical external context | [PlantUML](system-context-external.puml) | [SVG](system-context-external.svg) | [PNG](system-context-external.png) |
| 02 / section 6 | Information authority — edit, publish, retrieve and preserve | Information-authority context | [PlantUML](system-context-information-boundaries.puml) | [SVG](system-context-information-boundaries.svg) | [PNG](system-context-information-boundaries.png) |
| 03 / section 2.1 | Professional source and independent resume | UML conceptual class view | [PlantUML](domain-professional-presentation.puml) | [SVG](domain-professional-presentation.svg) | [PNG](domain-professional-presentation.png) |
| 03 / section 2.1 | Evidence selection and manually authored language | UML conceptual class view | [PlantUML](domain-evidence-and-language.puml) | [SVG](domain-evidence-and-language.svg) | [PNG](domain-evidence-and-language.png) |
| 03 / section 2.2 | Publication, PDF availability and protected link | UML conceptual class view | [PlantUML](domain-publication-and-sharing.puml) | [SVG](domain-publication-and-sharing.svg) | [PNG](domain-publication-and-sharing.png) |
| 03 / section 2.3 | Application preparation and actual submitted history | UML conceptual class view | [PlantUML](domain-applications-and-communication.puml) | [SVG](domain-applications-and-communication.svg) | [PNG](domain-applications-and-communication.png) |
| 03 / section 2.3 | Provider communication and explicit application links | UML conceptual class view | [PlantUML](domain-provider-communication.puml) | [SVG](domain-provider-communication.svg) | [PNG](domain-provider-communication.png) |
| 03 / section 2.4 | Work views, items, tasks and one Sprint Backlog | UML conceptual class view | [PlantUML](domain-work-management.puml) | [SVG](domain-work-management.svg) | [PNG](domain-work-management.png) |
| 03 / section 2.5 | Real Git history and repository collaboration | UML conceptual class view | [PlantUML](domain-git-collaboration.puml) | [SVG](domain-git-collaboration.svg) | [PNG](domain-git-collaboration.png) |
| 03 / section 2.6 | Execution provenance and separate deployment authority | UML conceptual class view | [PlantUML](domain-execution-and-deployment.puml) | [SVG](domain-execution-and-deployment.svg) | [PNG](domain-execution-and-deployment.png) |
| 03 / section 2.7 | Contextual authority, file policy and recoverable data | UML conceptual class view | [PlantUML](domain-access-files-and-recovery.puml) | [SVG](domain-access-files-and-recovery.svg) | [PNG](domain-access-files-and-recovery.png) |

[System Analysis index](../README.md) · [Four-document review](../evidence/four-document-diagram-review-2026-11-01.md)

## Conceptual Data / ER Views

[Document 05](../05-data-oriented-view.md) uses entity rectangles and crow-foot ends. **P** counts instantiate working proposals; **A** labels an established scope meaning. Plain associations leave counts unspecified. No physical schema or acceptance follows from this notation.

| Data view | Source | SVG | PNG |
|---|---|---|---|
| Data — source information and independent tailoring | [PlantUML](data-profile-and-tailoring.puml) | [SVG](data-profile-and-tailoring.svg) | [PNG](data-profile-and-tailoring.png) |
| Data — evidence disclosure and language context | [PlantUML](data-evidence-language-and-selection.puml) | [SVG](data-evidence-language-and-selection.svg) | [PNG](data-evidence-language-and-selection.png) |
| Data — publication identity, PDF provenance and access | [PlantUML](data-publication-pdf-and-sharing.puml) | [SVG](data-publication-pdf-and-sharing.svg) | [PNG](data-publication-pdf-and-sharing.png) |
| Data — application preparation and actual submission records | [PlantUML](data-applications-and-actual-material.puml) | [SVG](data-applications-and-actual-material.svg) | [PNG](data-applications-and-actual-material.png) |
| Data — provider identities and local associations | [PlantUML](data-provider-and-calendar-context.puml) | [SVG](data-provider-and-calendar-context.svg) | [PNG](data-provider-and-calendar-context.png) |
| Data — work identities and one coherent Sprint Backlog | [PlantUML](data-work-and-sprint-planning.puml) | [SVG](data-work-and-sprint-planning.svg) | [PNG](data-work-and-sprint-planning.png) |
| Data — repository identity and evaluated Git context | [PlantUML](data-git-revisions-and-collaboration.puml) | [SVG](data-git-revisions-and-collaboration.svg) | [PNG](data-git-revisions-and-collaboration.png) |
| Data — run provenance, attempts and deployment approval | [PlantUML](data-execution-provenance-and-targets.puml) | [SVG](data-execution-provenance-and-targets.svg) | [PNG](data-execution-provenance-and-targets.png) |
| Data — contextual access, effective policy and recovery coverage | [PlantUML](data-authority-policy-and-recovery.puml) | [SVG](data-authority-policy-and-recovery.svg) | [PNG](data-authority-policy-and-recovery.png) |

## Scenario / Logical Sequence Views

[Document 06](../06-scenario-based-view.md) explains guards, optional actions, alternative results and source status. These PlantUML lifelines are domain collaborators/context groupings, not selected runtime services. Diagram numbering is local; original UC/ST/SCN identifiers remain authoritative.

| Local model | Source | SVG | PNG |
|---|---|---|---|
| SB-M01 — Explicit source application and separate publication | [PlantUML](scenario-profile-apply-publication.puml) | [SVG](scenario-profile-apply-publication.svg) | [PNG](scenario-profile-apply-publication.png) |
| SB-M02 — PDF settings without implicit link changes | [PlantUML](scenario-pdf-settings.puml) | [SVG](scenario-pdf-settings.svg) | [PNG](scenario-pdf-settings.png) |
| SB-M03 — Independent link disable and fresh access | [PlantUML](scenario-disable-sharing-link.puml) | [SVG](scenario-disable-sharing-link.svg) | [PNG](scenario-disable-sharing-link.png) |
| SB-M04 — Selected protected retrieval and unavailable variants | [PlantUML](scenario-protected-retrieval.puml) | [SVG](scenario-protected-retrieval.svg) | [PNG](scenario-protected-retrieval.png) |
| SB-M05 — Manual preparation and separate progress change | [PlantUML](scenario-application-preparation.puml) | [SVG](scenario-application-preparation.svg) | [PNG](scenario-application-preparation.png) |
| SB-M06 — Preserve actual material, not current live substitutes | [PlantUML](scenario-actual-submission-capture.puml) | [SVG](scenario-actual-submission-capture.svg) | [PNG](scenario-actual-submission-capture.png) |
| SB-M07 — Read or deliberately send with truthful provider outcomes | [PlantUML](scenario-gmail-read-send-outcomes.puml) | [SVG](scenario-gmail-read-send-outcomes.svg) | [PNG](scenario-gmail-read-send-outcomes.png) |
| SB-M08 — Local calendar action versus selected provider synchronization | [PlantUML](scenario-calendar-local-sync.puml) | [SVG](scenario-calendar-local-sync.svg) | [PNG](scenario-calendar-local-sync.png) |
| SB-M09 — Independent refinement, Sprint planning and Sprint-end actions | [PlantUML](scenario-work-refine-plan-end.puml) | [SVG](scenario-work-refine-plan-end.svg) | [PNG](scenario-work-refine-plan-end.png) |
| SB-M10 — Invitation acceptance and resource-scoped changed access | [PlantUML](scenario-collaboration-and-changed-grant.puml) | [SVG](scenario-collaboration-and-changed-grant.svg) | [PNG](scenario-collaboration-and-changed-grant.png) |
| SB-M11 — Real Git read transfer versus authorized ref update | [PlantUML](scenario-git-transfer.puml) | [SVG](scenario-git-transfer.svg) | [PNG](scenario-git-transfer.png) |
| SB-M12 — Current source/target and revision-related review | [PlantUML](scenario-pull-request-review-merge.puml) | [SVG](scenario-pull-request-review-merge.svg) | [PNG](scenario-pull-request-review-merge.png) |
| SB-M13 — Gated run admission and attributable actual attempts | [PlantUML](scenario-workflow-admission-attempt.puml) | [SVG](scenario-workflow-admission-attempt.svg) | [PNG](scenario-workflow-admission-attempt.png) |
| SB-M14 — Target-authorized deployment is a separate goal | [PlantUML](scenario-separate-deployment.puml) | [SVG](scenario-separate-deployment.svg) | [PNG](scenario-separate-deployment.png) |
| SB-M15 — Effective policy, file admission and restricted evidence | [PlantUML](scenario-policy-admission-evidence.puml) | [SVG](scenario-policy-admission-evidence.svg) | [PNG](scenario-policy-admission-evidence.png) |
| SB-M16 — Conditional isolated restoration and safe reconciliation | [PlantUML](scenario-isolated-recovery-assessment.puml) | [SVG](scenario-isolated-recovery-assessment.svg) | [PNG](scenario-isolated-recovery-assessment.png) |

## State-based view — 07

18 bounded statecharts; full transition contracts and authority labels are maintained in [the state view](../07-state-based-view.md). Existing proposals remain proposals.

| Model | Editable source | SVG | PNG |
|---|---|---|---|
| SM-M01 — Independent draft and live presentation context | [state-resume-draft-publication.puml](state-resume-draft-publication.puml) | [SVG](state-resume-draft-publication.svg) | [PNG](state-resume-draft-publication.png) |
| SM-M02 — Proposed account access eligibility | [state-account-eligibility.puml](state-account-eligibility.puml) | [SVG](state-account-eligibility.svg) | [PNG](state-account-eligibility.png) |
| SM-M03 — Invitation and scoped grant instance | [state-collaboration-grant.puml](state-collaboration-grant.puml) | [SVG](state-collaboration-grant.svg) | [PNG](state-collaboration-grant.png) |
| SM-M04 — Enabled link is separate from current retrieval eligibility | [state-protected-link.puml](state-protected-link.puml) | [SVG](state-protected-link.svg) | [PNG](state-protected-link.png) |
| SM-M05 — Candidate admission and confirmed usable artifact | [state-artifact-availability.puml](state-artifact-availability.puml) | [SVG](state-artifact-availability.svg) | [PNG](state-artifact-availability.png) |
| SM-M06 — Proposed manual application progress | [state-application-progress.puml](state-application-progress.puml) | [SVG](state-application-progress.svg) | [PNG](state-application-progress.png) |
| SM-M07 — Actual submitted-set completeness | [state-submitted-set-completeness.puml](state-submitted-set-completeness.puml) | [SVG](state-submitted-set-completeness.svg) | [PNG](state-submitted-set-completeness.png) |
| SM-M08 — Usable provider capability versus disconnected data | [state-provider-connection.puml](state-provider-connection.puml) | [SVG](state-provider-connection.svg) | [PNG](state-provider-connection.png) |
| SM-M09 — Provider acceptance and unknown mail outcome | [state-mail-send-attempt.puml](state-mail-send-attempt.puml) | [SVG](state-mail-send-attempt.svg) | [PNG](state-mail-send-attempt.png) |
| SM-M10 — Local/provider mapping and freshness | [state-calendar-mapping.puml](state-calendar-mapping.puml) | [SVG](state-calendar-mapping.svg) | [PNG](state-calendar-mapping.png) |
| SM-M11 — Work status with subject-specific completion guards | [state-work-item-task.puml](state-work-item-task.puml) | [SVG](state-work-item-task.svg) | [PNG](state-work-item-task.png) |
| SM-M12 — Sprint period and recorded actual outcome | [state-sprint-lifecycle.puml](state-sprint-lifecycle.puml) | [SVG](state-sprint-lifecycle.svg) | [PNG](state-sprint-lifecycle.png) |
| SM-M13 — Request lifecycle with revision-specific eligibility | [state-pull-request-lifecycle.puml](state-pull-request-lifecycle.puml) | [SVG](state-pull-request-lifecycle.svg) | [PNG](state-pull-request-lifecycle.png) |
| SM-M14 — Actual attempt, cancellation request and runner uncertainty | [state-execution-attempt.puml](state-execution-attempt.puml) | [SVG](state-execution-attempt.svg) | [PNG](state-execution-attempt.png) |
| SM-M15 — Separate target authority and actual deployment effect | [state-deployment-effect.puml](state-deployment-effect.puml) | [SVG](state-deployment-effect.svg) | [PNG](state-deployment-effect.png) |
| SM-M16 — User-managed record retention and actual reclamation | [state-reference-aware-retention.puml](state-reference-aware-retention.puml) | [SVG](state-reference-aware-retention.svg) | [PNG](state-reference-aware-retention.png) |
| SM-M17 — Gated isolated restoration and demonstrated usable state | [state-recovery-assessment.puml](state-recovery-assessment.puml) | [SVG](state-recovery-assessment.svg) | [PNG](state-recovery-assessment.png) |
| SM-M18 — Observed operation result is separate from subject state | [state-operation-observation.puml](state-operation-observation.puml) | [SVG](state-operation-observation.svg) | [PNG](state-operation-observation.png) |

## Control-flow-based view — 08

16 source-aligned domain activities plus one reusable result-classification subactivity. Full step meanings and proposal boundaries are in [the control-flow view](../08-control-flow-based-view.md). Arrows show logical control, not atomic transactions or product execution proof.

| Model | Editable source | SVG | PNG |
|---|---|---|---|
| CF-M01 — Selected resume update and separate publication | [activity-profile-apply-publication.puml](activity-profile-apply-publication.puml) | [SVG](activity-profile-apply-publication.svg) | [PNG](activity-profile-apply-publication.png) |
| CF-M02 — Download settings without link side effects | [activity-pdf-settings.puml](activity-pdf-settings.puml) | [SVG](activity-pdf-settings.svg) | [PNG](activity-pdf-settings.png) |
| CF-M03 — Independent link disablement and fresh request | [activity-disable-sharing-link.puml](activity-disable-sharing-link.puml) | [SVG](activity-disable-sharing-link.svg) | [PNG](activity-disable-sharing-link.png) |
| CF-M04 — Controlled page and artifact retrieval | [activity-protected-retrieval.puml](activity-protected-retrieval.puml) | [SVG](activity-protected-retrieval.svg) | [PNG](activity-protected-retrieval.png) |
| CF-M05 — Manual application preparation or progress recording | [activity-application-preparation.puml](activity-application-preparation.puml) | [SVG](activity-application-preparation.svg) | [PNG](activity-application-preparation.png) |
| CF-M06 — Capture actual submitted materials | [activity-actual-submission-capture.puml](activity-actual-submission-capture.puml) | [SVG](activity-actual-submission-capture.svg) | [PNG](activity-actual-submission-capture.png) |
| CF-M07 — Read correspondence or deliberately send | [activity-gmail-read-send-outcomes.puml](activity-gmail-read-send-outcomes.puml) | [SVG](activity-gmail-read-send-outcomes.svg) | [PNG](activity-gmail-read-send-outcomes.png) |
| CF-M08 — Local activity versus selected calendar synchronization | [activity-calendar-local-sync.puml](activity-calendar-local-sync.puml) | [SVG](activity-calendar-local-sync.svg) | [PNG](activity-calendar-local-sync.png) |
| CF-M09 — Refinement, Sprint planning and Sprint completion | [activity-work-refine-plan-end.puml](activity-work-refine-plan-end.puml) | [SVG](activity-work-refine-plan-end.svg) | [PNG](activity-work-refine-plan-end.png) |
| CF-M10 — Invitation acceptance and subsequent scoped access | [activity-collaboration-and-changed-grant.puml](activity-collaboration-and-changed-grant.puml) | [SVG](activity-collaboration-and-changed-grant.svg) | [PNG](activity-collaboration-and-changed-grant.png) |
| CF-M11 — Real Git read transfer or ref update | [activity-git-transfer.puml](activity-git-transfer.puml) | [SVG](activity-git-transfer.svg) | [PNG](activity-git-transfer.png) |
| CF-M12 — Request, review or eligible integration | [activity-pull-request-review-merge.puml](activity-pull-request-review-merge.puml) | [SVG](activity-pull-request-review-merge.svg) | [PNG](activity-pull-request-review-merge.png) |
| CF-M13 — Gated execution attempt and cancellation race | [activity-workflow-admission-attempt.puml](activity-workflow-admission-attempt.puml) | [SVG](activity-workflow-admission-attempt.svg) | [PNG](activity-workflow-admission-attempt.png) |
| CF-M14 — Separate target-authorized deployment | [activity-separate-deployment.puml](activity-separate-deployment.puml) | [SVG](activity-separate-deployment.svg) | [PNG](activity-separate-deployment.png) |
| CF-M15 — Effective policy, file admission or restricted evidence | [activity-policy-admission-evidence.puml](activity-policy-admission-evidence.puml) | [SVG](activity-policy-admission-evidence.svg) | [PNG](activity-policy-admission-evidence.png) |
| CF-M16 — Conditional isolated restore and usability assessment | [activity-isolated-recovery-assessment.puml](activity-isolated-recovery-assessment.puml) | [SVG](activity-isolated-recovery-assessment.svg) | [PNG](activity-isolated-recovery-assessment.png) |
| CF-M17 — Reusable actual operation-result classification | [activity-operation-result-classification.puml](activity-operation-result-classification.puml) | [SVG](activity-operation-result-classification.svg) | [PNG](activity-operation-result-classification.png) |

## Rule-based view — 09

Eight focused decision trees accompany 18 finite-domain decision tables in [the rule view](../09-rule-based-view.md). These are decision alternatives, not execution order. Full conditions, results and authority remain in the tables.

| Decision | Editable source | SVG | PNG |
|---|---|---|---|
| RB-D01 — Resource-scoped operation eligibility | [rule-rb-d01-decision.puml](rule-rb-d01-decision.puml) | [SVG](rule-rb-d01-decision.svg) | [PNG](rule-rb-d01-decision.png) |
| RB-D04 — Protected selected representation eligibility | [rule-rb-d04-decision.puml](rule-rb-d04-decision.puml) | [SVG](rule-rb-d04-decision.svg) | [PNG](rule-rb-d04-decision.png) |
| RB-D06 — Actual submitted-set completeness | [rule-rb-d06-decision.puml](rule-rb-d06-decision.puml) | [SVG](rule-rb-d06-decision.svg) | [PNG](rule-rb-d06-decision.png) |
| RB-D07 — Reviewed provider send eligibility | [rule-rb-d07-decision.puml](rule-rb-d07-decision.puml) | [SVG](rule-rb-d07-decision.svg) | [PNG](rule-rb-d07-decision.png) |
| RB-D11 — Current revision-specific merge eligibility | [rule-rb-d11-decision.puml](rule-rb-d11-decision.puml) | [SVG](rule-rb-d11-decision.svg) | [PNG](rule-rb-d11-decision.png) |
| RB-D12 — Workflow execution admission | [rule-rb-d12-decision.puml](rule-rb-d12-decision.puml) | [SVG](rule-rb-d12-decision.svg) | [PNG](rule-rb-d12-decision.png) |
| RB-D15 — Reference-aware physical reclamation eligibility | [rule-rb-d15-decision.puml](rule-rb-d15-decision.puml) | [SVG](rule-rb-d15-decision.svg) | [PNG](rule-rb-d15-decision.png) |
| RB-D16 — Scoped usable recovery assessment | [rule-rb-d16-decision.puml](rule-rb-d16-decision.puml) | [SVG](rule-rb-d16-decision.svg) | [PNG](rule-rb-d16-decision.png) |

## Domain constraints and operation contracts — 10

Eight before/confirmed-after/frame relations illustrate selected contracts from [the contract view](../10-domain-constraints-and-operation-contracts.md). After-state applies only to actual confirmed permitted success; frame does not freeze independent concurrent actions or guarantee failure rollback. Full obligations/policy status remain in the text.

| Contract | Editable source | SVG | PNG |
|---|---|---|---|
| DC-O02 — Apply selected source changes to one draft | [contract-dc-o02-boundary.puml](contract-dc-o02-boundary.puml) | [SVG](contract-dc-o02-boundary.svg) | [PNG](contract-dc-o02-boundary.png) |
| DC-O03 — Publish separately confirmed intended presentation | [contract-dc-o03-boundary.puml](contract-dc-o03-boundary.puml) | [SVG](contract-dc-o03-boundary.svg) | [PNG](contract-dc-o03-boundary.png) |
| DC-O05 — Disable a specific protected link | [contract-dc-o05-boundary.puml](contract-dc-o05-boundary.puml) | [SVG](contract-dc-o05-boundary.svg) | [PNG](contract-dc-o05-boundary.png) |
| DC-O12 — Submit a reviewed mail send/reply attempt | [contract-dc-o12-boundary.puml](contract-dc-o12-boundary.puml) | [SVG](contract-dc-o12-boundary.svg) | [PNG](contract-dc-o12-boundary.png) |
| DC-O14 — Unlink a local provider mapping | [contract-dc-o14-boundary.puml](contract-dc-o14-boundary.puml) | [SVG](contract-dc-o14-boundary.svg) | [PNG](contract-dc-o14-boundary.png) |
| DC-O26 — Merge only current eligible evaluated revisions | [contract-dc-o26-boundary.puml](contract-dc-o26-boundary.puml) | [SVG](contract-dc-o26-boundary.svg) | [PNG](contract-dc-o26-boundary.png) |
| DC-O30 — Attempt a separately target-authorized deployment | [contract-dc-o30-boundary.puml](contract-dc-o30-boundary.puml) | [SVG](contract-dc-o30-boundary.svg) | [PNG](contract-dc-o30-boundary.png) |
| DC-O37 — Perform and assess an authorized isolated recovery drill | [contract-dc-o37-boundary.puml](contract-dc-o37-boundary.puml) | [SVG](contract-dc-o37-boundary.svg) | [PNG](contract-dc-o37-boundary.png) |

## Model consistency, traceability and review — 11

Three evidence/review relationship views accompany [SA-RV02](../11-model-consistency-traceability-and-review.md). A citation is not semantic criterion sufficiency, and a rendered diagram is not a product test or owner acceptance.

| View | Editable source | SVG | PNG |
|---|---|---|---|
| SA-RV02 — association is not verification | [review-trace-evidence-levels.puml](review-trace-evidence-levels.puml) | [SVG](review-trace-evidence-levels.svg) | [PNG](review-trace-evidence-levels.png) |
| SA-RV02 — current analysis position | [review-current-position.puml](review-current-position.puml) | [SVG](review-current-position.svg) | [PNG](review-current-position.png) |
| SA-RV02 — review and change-impact route | [review-change-impact-route.puml](review-change-impact-route.puml) | [SVG](review-change-impact-route.svg) | [PNG](review-change-impact-route.png) |

## Interfaces and external interactions — 12

Eight focused logical exchange views accompany [file 12](../12-interfaces-and-external-interactions.md). Arrows identify direction; conditional access/facilities are not claims of installed components, selected transports, completed operations or automatically inherited authority.

| Family | Editable source | SVG | PNG |
|---|---|---|---|
| IF-01 — Private human interface | [interface-private-human-context.puml](interface-private-human-context.puml) | [SVG](interface-private-human-context.svg) | [PNG](interface-private-human-context.png) |
| IF-02 — Protected employer representation | [interface-employer-protected-representation.puml](interface-employer-protected-representation.puml) | [SVG](interface-employer-protected-representation.svg) | [PNG](interface-employer-protected-representation.png) |
| IF-03 — Authorized file/PDF exchange | [interface-file-candidate-result.puml](interface-file-candidate-result.puml) | [SVG](interface-file-candidate-result.svg) | [PNG](interface-file-candidate-result.png) |
| IF-04 — Gmail provider operations | [interface-gmail-reviewed-effects.puml](interface-gmail-reviewed-effects.puml) | [SVG](interface-gmail-reviewed-effects.svg) | [PNG](interface-gmail-reviewed-effects.png) |
| IF-05 — Calendar provider and local mapping | [interface-calendar-local-provider.puml](interface-calendar-local-provider.puml) | [SVG](interface-calendar-local-provider.svg) | [PNG](interface-calendar-local-provider.png) |
| IF-06 — Real Git-client boundary | [interface-real-git-client.puml](interface-real-git-client.puml) | [SVG](interface-real-git-client.svg) | [PNG](interface-real-git-client.png) |
| IF-07 — Conditional execution and separate deployment target | [interface-execution-separate-target.puml](interface-execution-separate-target.puml) | [SVG](interface-execution-separate-target.svg) | [PNG](interface-execution-separate-target.png) |
| IF-08 — Operational configuration, delivery and recovery | [interface-operating-delivery-recovery.puml](interface-operating-delivery-recovery.puml) | [SVG](interface-operating-delivery-recovery.svg) | [PNG](interface-operating-delivery-recovery.png) |

## Security, quality and operational analysis — 13

Six focused analysis/evidence views accompany [file 13](../13-security-quality-and-operational-analysis.md). They do not select architecture, certify controls, prove capacity or authorize host/provider/execution/restore operations.

| View | Editable source | SVG | PNG |
|---|---|---|---|
| SQ — scoped authority across entry paths | [security-scoped-authority.puml](security-scoped-authority.puml) | [SVG](security-scoped-authority.svg) | [PNG](security-scoped-authority.png) |
| SQ — data trust and conditional execution | [security-untrusted-content-execution.puml](security-untrusted-content-execution.puml) | [SVG](security-untrusted-content-execution.svg) | [PNG](security-untrusted-content-execution.png) |
| SQ — measurable quality scenario contract | [quality-scenario-measurement.puml](quality-scenario-measurement.puml) | [SVG](quality-scenario-measurement.svg) | [PNG](quality-scenario-measurement.png) |
| SQ — recovery evidence and current authority | [recovery-scoped-usable-state.puml](recovery-scoped-usable-state.puml) | [SVG](recovery-scoped-usable-state.svg) | [PNG](recovery-scoped-usable-state.png) |
| SQ — operation effect versus observation | [operations-effect-evidence.puml](operations-effect-evidence.puml) | [SVG](operations-effect-evidence.svg) | [PNG](operations-effect-evidence.png) |
| SQ — mixed workload and observed host limits | [operations-resource-envelope.puml](operations-resource-envelope.puml) | [SVG](operations-resource-envelope.svg) | [PNG](operations-resource-envelope.png) |

## Feasibility, dependencies and design handoff — 14

Five qualified evidence/gate/handoff/design-question/delivery views accompany [file 14](../14-feasibility-dependencies-and-design-handoff.md). They do not select architecture, certify feasibility, approve a forecast, change parent gates or authorize product work.

| View | Editable source | SVG | PNG |
|---|---|---|---|
| HD — evidence and dependent commitments | [handoff-evidence-dependent-commitment.puml](handoff-evidence-dependent-commitment.puml) | [SVG](handoff-evidence-dependent-commitment.svg) | [PNG](handoff-evidence-dependent-commitment.png) |
| HD — existing gate relationships | [handoff-existing-review-gates.puml](handoff-existing-review-gates.puml) | [SVG](handoff-existing-review-gates.svg) | [PNG](handoff-existing-review-gates.png) |
| HD — conditional handoff position | [handoff-package-position.puml](handoff-package-position.puml) | [SVG](handoff-package-position.svg) | [PNG](handoff-package-position.png) |
| HD — design evaluation record | [handoff-design-question-record.puml](handoff-design-question-record.puml) | [SVG](handoff-design-question-record.svg) | [PNG](handoff-design-question-record.png) |
| HD — delivery reconciliation before coding | [handoff-delivery-reconciliation.puml](handoff-delivery-reconciliation.puml) | [SVG](handoff-delivery-reconciliation.svg) | [PNG](handoff-delivery-reconciliation.png) |


## Current Processes and Bottleneck Analysis — File 15

Evidence classification and investigation logic; not observed daily-business workflows.

| View | Source | SVG | PNG |
|---|---|---|---|
| CP — current evidence versus target and hypothesis | [PlantUML](process-evidence-classes.puml) | [SVG](process-evidence-classes.svg) | [PNG](process-evidence-classes.png) |
| CP — documented artifact relationships | [PlantUML](process-documented-artifact-trail.puml) | [SVG](process-documented-artifact-trail.svg) | [PNG](process-documented-artifact-trail.png) |
| CP — bounded current-process evidence need | [PlantUML](process-current-workflow-questions.puml) | [SVG](process-current-workflow-questions.svg) | [PNG](process-current-workflow-questions.png) |
| CP — hypothesis support or rejection | [PlantUML](process-hypothesis-validation.puml) | [SVG](process-hypothesis-validation.svg) | [PNG](process-hypothesis-validation.png) |
| CP — intended improvement versus demonstrated result | [PlantUML](process-improvement-evidence.puml) | [SVG](process-improvement-evidence.svg) | [PNG](process-improvement-evidence.png) |


## Diagram notation alignment — November 1, 2026

See the [file-by-file report](../evidence/notation-alignment-review-2026-11-01.md). New diagrams complement existing models. BPMN uses native XML; other new diagrams use PlantUML.

| Diagram | Notation | Editable | SVG | PNG |
|---|---|---|---|---|
| Document navigation — 00 through 15 | Document dependency graph | [Source](documentation-navigation.puml) | [SVG](documentation-navigation.svg) | [PNG](documentation-navigation.png) |
| Scope and stakeholder map | Stakeholder and scope diagram | [Source](scope-stakeholder-map.puml) | [SVG](scope-stakeholder-map.svg) | [PNG](scope-stakeholder-map.png) |
| C4 Level 1 — target product context | C4 Level 1 | [Source](c4-system-context.puml) | [SVG](c4-system-context.svg) | [PNG](c4-system-context.png) |
| C4 Level 2 — historical demo evidence only | C4 Level 2, bounded historical inventory | [Source](c4-observed-demo-containers.puml) | [SVG](c4-observed-demo-containers.svg) | [PNG](c4-observed-demo-containers.png) |
| UML packages — logical domain groupings | UML package | [Source](domain-package-responsibilities.puml) | [SVG](domain-package-responsibilities.svg) | [PNG](domain-package-responsibilities.png) |
| UML class detail — explicit proposed relationship ends | UML class with multiplicities | [Source](domain-proposed-multiplicity.puml) | [SVG](domain-proposed-multiplicity.svg) | [PNG](domain-proposed-multiplicity.png) |
| DFD context — external information boundary | DFD context | [Source](function-dfd-context.puml) | [SVG](function-dfd-context.svg) | [PNG](function-dfd-context.png) |
| DFD Level 1 — content | DFD Level 1 | [Source](function-dfd-level1-content.puml) | [SVG](function-dfd-level1-content.svg) | [PNG](function-dfd-level1-content.png) |
| DFD Level 1 — work-operations | DFD Level 1 | [Source](function-dfd-level1-work-operations.puml) | [SVG](function-dfd-level1-work-operations.svg) | [PNG](function-dfd-level1-work-operations.png) |
| Functional decomposition — responsibilities, not services | Functional decomposition tree | [Source](function-decomposition.puml) | [SVG](function-decomposition.svg) | [PNG](function-decomposition.png) |
| DFD — logical information ownership | DFD logical stores | [Source](function-store-information.puml) | [SVG](function-store-information.svg) | [PNG](function-store-information.png) |
| DFD Level 2 — F02 selected apply and publication | DFD Level 2 | [Source](function-profile-level2.puml) | [SVG](function-profile-level2.svg) | [PNG](function-profile-level2.png) |
| DC-O02 — UML object snapshots and frame condition | UML object snapshots | [Source](contract-apply-object-snapshots.puml) | [SVG](contract-apply-object-snapshots.svg) | [PNG](contract-apply-object-snapshots.png) |
| Selected traceability matrix — associations, not test results | Traceability matrix graphic | [Source](traceability-selected-matrix.puml) | [SVG](traceability-selected-matrix.svg) | [PNG](traceability-selected-matrix.png) |
| UML component view — interface responsibilities | UML component-style logical interface view | [Source](interface-logical-components.puml) | [SVG](interface-logical-components.svg) | [PNG](interface-logical-components.png) |
| Request/response boundary — protocol-neutral contract | UML sequence | [Source](interface-request-response-contract.puml) | [SVG](interface-request-response-contract.svg) | [PNG](interface-request-response-contract.png) |
| Trust-boundary DFD — logical protections to establish | Security DFD | [Source](security-data-flow-trust.puml) | [SVG](security-data-flow-trust.svg) | [PNG](security-data-flow-trust.png) |
| UML deployment — historical demo observation | UML deployment | [Source](deployment-observed-host.puml) | [SVG](deployment-observed-host.svg) | [PNG](deployment-observed-host.png) |
| Dependency network — conditions, not scheduled dates | Dependency network | [Source](handoff-dependency-network.puml) | [SVG](handoff-dependency-network.svg) | [PNG](handoff-dependency-network.png) |
| Resumefolio — analysis ecosystem | High-level system overview | [Source](ecosystem-overview.puml) | [SVG](ecosystem-overview.svg) | [PNG](ecosystem-overview.png) |
| As-Is — evidence-bounded current-process view | BPMN 2.0 | [Source](process-bpmn-as-is-boundary.bpmn) | [SVG](process-bpmn-as-is-boundary.svg) | [PNG](process-bpmn-as-is-boundary.png) |
| To-Be — selected apply and separate publication | BPMN 2.0 | [Source](process-bpmn-target-publication.bpmn) | [SVG](process-bpmn-target-publication.svg) | [PNG](process-bpmn-target-publication.png) |


## File 10 — constraint and outcome clarification

The eight existing contract-boundary views now use vertical layouts. The existing object snapshot remains.

| View | Source | SVG | PNG |
|---|---|---|---|
| Constraint application — common rules and accepted core | [PlantUML](contract-constraint-application.puml) | [SVG](contract-constraint-application.svg) | [PNG](contract-constraint-application.png) |
| Contract outcomes — evidence required for a claim | [PlantUML](contract-outcome-interpretation.puml) | [SVG](contract-outcome-interpretation.svg) | [PNG](contract-outcome-interpretation.png) |


## File 13 — threats, infrastructure and conditional recovery

These views distinguish candidate controls, dated inventory and conditional future procedures.

| View | Editable | SVG | PNG |
|---|---|---|---|
| Trust boundaries and candidate threats | [PlantUML](security-threat-boundary-model.puml) | [SVG](security-threat-boundary-model.svg) | [PNG](security-threat-boundary-model.png) |
| Infrastructure topology — observed demo and explicit gaps | [PlantUML](security-infrastructure-topology.puml) | [SVG](security-infrastructure-topology.svg) | [PNG](security-infrastructure-topology.png) |
| HA / failover — conditional decision and verification sequence | [PlantUML](security-ha-failover-sequence.puml) | [SVG](security-ha-failover-sequence.svg) | [PNG](security-ha-failover-sequence.png) |
| Disaster recovery — restore, validate and controlled resumption | [PlantUML](security-disaster-recovery-sequence.puml) | [SVG](security-disaster-recovery-sequence.svg) | [PNG](security-disaster-recovery-sequence.png) |

## Whole-product ecosystem and connected platforms

The two coordinated maps cover logical product areas and all eight existing IF families. Status labels distinguish target exchanges from dated demo observations and unconfigured facilities.

| View | Source | SVG | PNG |
|---|---|---|---|
| Internal ecosystem and information relationships | [PlantUML](ecosystem-overview.puml) | [SVG](ecosystem-overview.svg) | [PNG](ecosystem-overview.png) |
| External connections, directions and status | [PlantUML](ecosystem-platform-connections.puml) | [SVG](ecosystem-platform-connections.svg) | [PNG](ecosystem-platform-connections.png) |

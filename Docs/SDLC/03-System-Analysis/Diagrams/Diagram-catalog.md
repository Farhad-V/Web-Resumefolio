# System Analysis — Diagram Catalog

Revision: November 1, 2026. Active sources are **PlantUML `.puml`** and native **BPMN `.bpmn`**, with SVG and PNG exports. The catalog covers reviewed documents 00–03 and the populated data (05), scenario (06), state (07), activity (08), rule (09) and contract (10) and consistency-review (11) and interface (12) and security/quality/operating (13) and handoff (14) views. Functional and behavioral views are populated; exact semantic review and phase acceptance remain separate work.

Current MVP scope and selected mechanisms: [Baseline](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/README.md). Deferred provider, advanced collaboration and workflow-execution designs are not MVP prerequisites.

## Reading and Maintenance Rules

- Activity diagrams show decisions and control flow; class associations do not show execution order.

- Context associations identify actors/participants and logical exchanges; dependency notation is explained next to each figure.

- Class diagrams show concepts and semantic properties. Detailed responsibilities, policy status and sources stay in the nearby tables.

- Multiplicity is shown only when justified. Unlabeled association ends are intentionally unspecified, not one-to-one.

- Every active figure has one matching `.puml`, `.svg` and `.png` set. Render locally with PlantUML; no remote service is required.

- Earlier `.dot` sources are retained as historical artifacts and are not authoritative for the revised images. Do not regenerate current figures from them.

| Document / section | Figure | Notation | Source | SVG | PNG |
| --- | --- | --- | --- | --- | --- |
| 00 / section 2 | System Analysis — iterative working route | Activity / analysis process | [PlantUML](Start-here-analysis-route.puml) | [SVG](Start-here-analysis-route.svg) | ![start here analysis route](Start-here-analysis-route.png) |
| 00 / section 3 | Accepted core — explicit apply and separate publication | Activity / accepted successful path | [PlantUML](Start-here-profile-publication.puml) | [SVG](Start-here-profile-publication.svg) | ![start here profile publication](Start-here-profile-publication.png) |
| 01 / section 2 | Analysis — source authority and feedback | Artifact dependency | [PlantUML](Analysis-inputs-and-outputs.puml) | [SVG](Analysis-inputs-and-outputs.svg) | ![analysis inputs and outputs](Analysis-inputs-and-outputs.png) |
| 01 / section 4 | Seven views — complementary questions, one coherent model | Model-view map | [PlantUML](Analysis-seven-view-consistency.puml) | [SVG](Analysis-seven-view-consistency.svg) | ![analysis seven view consistency](Analysis-seven-view-consistency.png) |
| 02 / section 2 | Resumefolio — human roles and authority contexts | UML actor / system context | [PlantUML](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) | ![mvp system boundaries](../../Design-assets/Archived-png/Mvp-system-boundaries.png) |
| 02 / section 3 | Resumefolio — clients, providers and operating dependencies | Logical external context | [PlantUML](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) | ![mvp system boundaries](../../Design-assets/Archived-png/Mvp-system-boundaries.png) |
| 02 / section 6 | Information authority — edit, publish, retrieve and preserve | Information-authority context | [PlantUML](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) | ![mvp system boundaries](../../Design-assets/Archived-png/Mvp-system-boundaries.png) |
| 03 / section 2.1 | Professional source and independent resume | UML conceptual class view | [PlantUML](Domain-professional-presentation.puml) | [SVG](Domain-professional-presentation.svg) | ![domain professional presentation](Domain-professional-presentation.png) |
| 03 / section 2.1 | Evidence selection and manually authored language | UML conceptual class view | [PlantUML](Domain-evidence-and-language.puml) | [SVG](Domain-evidence-and-language.svg) | ![domain evidence and language](Domain-evidence-and-language.png) |
| 03 / section 2.2 | Publication, PDF availability and protected link | UML conceptual class view | [PlantUML](Domain-publication-and-sharing.puml) | [SVG](Domain-publication-and-sharing.svg) | ![domain publication and sharing](Domain-publication-and-sharing.png) |
| 03 / section 2.3 | Application preparation and actual submitted history | UML conceptual class view | [PlantUML](Domain-applications-and-communication.puml) | [SVG](Domain-applications-and-communication.svg) | ![domain applications and communication](Domain-applications-and-communication.png) |
| 03 / section 2.3 | Provider communication and explicit application links | UML conceptual class view | [PlantUML](Domain-provider-communication.puml) | [SVG](Domain-provider-communication.svg) | ![domain provider communication](Domain-provider-communication.png) |
| 03 / section 2.4 | Work views, items, tasks and one Sprint Backlog | UML conceptual class view | [PlantUML](Domain-work-management.puml) | [SVG](Domain-work-management.svg) | ![domain work management](Domain-work-management.png) |
| 03 / section 2.5 | Real Git history and repository collaboration | UML conceptual class view | [PlantUML](Domain-git-collaboration.puml) | [SVG](Domain-git-collaboration.svg) | ![domain git collaboration](Domain-git-collaboration.png) |
| 03 / section 2.6 | Execution provenance and separate deployment authority | UML conceptual class view | [PlantUML](Domain-execution-and-deployment.puml) | [SVG](Domain-execution-and-deployment.svg) | ![domain execution and deployment](Domain-execution-and-deployment.png) |
| 03 / section 2.7 | Contextual authority, file policy and recoverable data | UML conceptual class view | [PlantUML](Domain-access-files-and-recovery.puml) | [SVG](Domain-access-files-and-recovery.svg) | ![domain access files and recovery](Domain-access-files-and-recovery.png) |

[System Analysis index](../System-analysis.md) · [Four-document review](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/03-system-analysis/evidence/four-document-diagram-review-2026-11-01.md)

## Conceptual Data / ER Views

[Document 05](../System-analysis.md#analysis-domain-and-information-analysis--05-data-oriented-view) uses entity rectangles and crow-foot ends. **P** counts instantiate working proposals; **A** labels an established scope meaning. Plain associations leave counts unspecified. No physical schema or acceptance follows from this notation.

| Data view | Source | SVG | PNG |
| --- | --- | --- | --- |
| Data — source information and independent tailoring | [PlantUML](Data-profile-and-tailoring.puml) | [SVG](Data-profile-and-tailoring.svg) | ![data profile and tailoring](Data-profile-and-tailoring.png) |
| Data — evidence disclosure and language context | [PlantUML](Data-evidence-language-and-selection.puml) | [SVG](Data-evidence-language-and-selection.svg) | ![data evidence language and selection](Data-evidence-language-and-selection.png) |
| Data — publication identity, PDF provenance and access | [PlantUML](Data-publication-pdf-and-sharing.puml) | [SVG](Data-publication-pdf-and-sharing.svg) | ![data publication pdf and sharing](Data-publication-pdf-and-sharing.png) |
| Data — application preparation and actual submission records | [PlantUML](Data-applications-and-actual-material.puml) | [SVG](Data-applications-and-actual-material.svg) | ![data applications and actual material](Data-applications-and-actual-material.png) |
| Data — provider identities and local associations | [PlantUML](Data-provider-and-calendar-context.puml) | [SVG](Data-provider-and-calendar-context.svg) | ![data provider and calendar context](Data-provider-and-calendar-context.png) |
| Data — work identities and one coherent Sprint Backlog | [PlantUML](Data-work-and-sprint-planning.puml) | [SVG](Data-work-and-sprint-planning.svg) | ![data work and sprint planning](Data-work-and-sprint-planning.png) |
| Data — repository identity and evaluated Git context | [PlantUML](Data-git-revisions-and-collaboration.puml) | [SVG](Data-git-revisions-and-collaboration.svg) | ![data git revisions and collaboration](Data-git-revisions-and-collaboration.png) |
| Data — run provenance, attempts and deployment approval | [PlantUML](Data-execution-provenance-and-targets.puml) | [SVG](Data-execution-provenance-and-targets.svg) | ![data execution provenance and targets](Data-execution-provenance-and-targets.png) |
| Data — contextual access, effective policy and recovery coverage | [PlantUML](Data-authority-policy-and-recovery.puml) | [SVG](Data-authority-policy-and-recovery.svg) | ![data authority policy and recovery](Data-authority-policy-and-recovery.png) |

## Scenario / Logical Sequence Views

[Document 06](../System-analysis.md#analysis-behavioral-and-scenario-analysis--06-scenario-based-view) explains guards, optional actions, alternative results and source status. These PlantUML lifelines are domain collaborators/context groupings, not selected runtime services. Diagram numbering is local; original UC/ST/SCN identifiers remain authoritative.

| Local model | Source | SVG | PNG |
| --- | --- | --- | --- |
| SB-M01 — Explicit source application and separate publication | [PlantUML](Scenario-profile-apply-publication.puml) | [SVG](Scenario-profile-apply-publication.svg) | ![scenario profile apply publication](Scenario-profile-apply-publication.png) |
| SB-M02 — PDF settings without implicit link changes | [PlantUML](Scenario-pdf-settings.puml) | [SVG](Scenario-pdf-settings.svg) | ![scenario pdf settings](Scenario-pdf-settings.png) |
| SB-M03 — Independent link disable and fresh access | [PlantUML](Scenario-disable-sharing-link.puml) | [SVG](Scenario-disable-sharing-link.svg) | ![scenario disable sharing link](Scenario-disable-sharing-link.png) |
| SB-M04 — Selected protected retrieval and unavailable variants | [PlantUML](Scenario-protected-retrieval.puml) | [SVG](Scenario-protected-retrieval.svg) | ![scenario protected retrieval](Scenario-protected-retrieval.png) |
| SB-M05 — Manual preparation and separate progress change | [PlantUML](Scenario-application-preparation.puml) | [SVG](Scenario-application-preparation.svg) | ![scenario application preparation](Scenario-application-preparation.png) |
| SB-M06 — Preserve actual material, not current live substitutes | [PlantUML](Scenario-actual-submission-capture.puml) | [SVG](Scenario-actual-submission-capture.svg) | ![scenario actual submission capture](Scenario-actual-submission-capture.png) |
| SB-M07 — Read or deliberately send with truthful provider outcomes | [PlantUML](Scenario-gmail-read-send-outcomes.puml) | [SVG](Scenario-gmail-read-send-outcomes.svg) | ![scenario gmail read send outcomes](Scenario-gmail-read-send-outcomes.png) |
| SB-M08 — Local calendar action versus selected provider synchronization | [PlantUML](Scenario-calendar-local-sync.puml) | [SVG](Scenario-calendar-local-sync.svg) | ![scenario calendar local sync](Scenario-calendar-local-sync.png) |
| SB-M09 — Independent refinement, Sprint planning and Sprint-end actions | [PlantUML](Scenario-work-refine-plan-end.puml) | [SVG](Scenario-work-refine-plan-end.svg) | ![scenario work refine plan end](Scenario-work-refine-plan-end.png) |
| SB-M10 — Invitation acceptance and resource-scoped changed access | [PlantUML](Scenario-collaboration-and-changed-grant.puml) | [SVG](Scenario-collaboration-and-changed-grant.svg) | ![scenario collaboration and changed grant](Scenario-collaboration-and-changed-grant.png) |
| SB-M11 — Real Git read transfer versus authorized ref update | [PlantUML](Scenario-git-transfer.puml) | [SVG](Scenario-git-transfer.svg) | ![scenario git transfer](Scenario-git-transfer.png) |
| SB-M12 — Current source/target and revision-related review | [PlantUML](Scenario-pull-request-review-merge.puml) | [SVG](Scenario-pull-request-review-merge.svg) | ![scenario pull request review merge](Scenario-pull-request-review-merge.png) |
| SB-M13 — Gated run admission and attributable actual attempts | [PlantUML](Scenario-workflow-admission-attempt.puml) | [SVG](Scenario-workflow-admission-attempt.svg) | ![scenario workflow admission attempt](Scenario-workflow-admission-attempt.png) |
| SB-M14 — Target-authorized deployment is a separate goal | [PlantUML](Scenario-separate-deployment.puml) | [SVG](Scenario-separate-deployment.svg) | ![scenario separate deployment](Scenario-separate-deployment.png) |
| SB-M15 — Effective policy, file admission and restricted evidence | [PlantUML](Scenario-policy-admission-evidence.puml) | [SVG](Scenario-policy-admission-evidence.svg) | ![scenario policy admission evidence](Scenario-policy-admission-evidence.png) |
| SB-M16 — Conditional isolated restoration and safe reconciliation | [PlantUML](Scenario-isolated-recovery-assessment.puml) | [SVG](Scenario-isolated-recovery-assessment.svg) | ![scenario isolated recovery assessment](Scenario-isolated-recovery-assessment.png) |

## State-based view — 07

18 bounded statecharts; full transition contracts and authority labels are maintained in [the state view](../System-analysis.md#analysis-behavioral-and-scenario-analysis--07-state-based-view). Existing proposals remain proposals.

| Model | Editable source | SVG | PNG |
| --- | --- | --- | --- |
| SM-M01 — Independent draft and live presentation context | [state-resume-draft-publication.puml](State-resume-draft-publication.puml) | [SVG](State-resume-draft-publication.svg) | ![state resume draft publication](State-resume-draft-publication.png) |
| SM-M02 — Proposed account access eligibility | [state-account-eligibility.puml](State-account-eligibility.puml) | [SVG](State-account-eligibility.svg) | ![state account eligibility](State-account-eligibility.png) |
| SM-M03 — Invitation and scoped grant instance | [state-collaboration-grant.puml](State-collaboration-grant.puml) | [SVG](State-collaboration-grant.svg) | ![state collaboration grant](State-collaboration-grant.png) |
| SM-M04 — Enabled link is separate from current retrieval eligibility | [state-protected-link.puml](State-protected-link.puml) | [SVG](State-protected-link.svg) | ![state protected link](State-protected-link.png) |
| SM-M05 — Candidate admission and confirmed usable artifact | [state-artifact-availability.puml](State-artifact-availability.puml) | [SVG](State-artifact-availability.svg) | ![state artifact availability](State-artifact-availability.png) |
| SM-M06 — Proposed manual application progress | [state-application-progress.puml](State-application-progress.puml) | [SVG](State-application-progress.svg) | ![state application progress](State-application-progress.png) |
| SM-M07 — Actual submitted-set completeness | [state-submitted-set-completeness.puml](State-submitted-set-completeness.puml) | [SVG](State-submitted-set-completeness.svg) | ![state submitted set completeness](State-submitted-set-completeness.png) |
| SM-M08 — Usable provider capability versus disconnected data | [state-provider-connection.puml](State-provider-connection.puml) | [SVG](State-provider-connection.svg) | ![state provider connection](State-provider-connection.png) |
| SM-M09 — Provider acceptance and unknown mail outcome | [state-mail-send-attempt.puml](State-mail-send-attempt.puml) | [SVG](State-mail-send-attempt.svg) | ![state mail send attempt](State-mail-send-attempt.png) |
| SM-M10 — Local/provider mapping and freshness | [state-calendar-mapping.puml](State-calendar-mapping.puml) | [SVG](State-calendar-mapping.svg) | ![state calendar mapping](State-calendar-mapping.png) |
| SM-M11 — Work status with subject-specific completion guards | [state-work-item-task.puml](State-work-item-task.puml) | [SVG](State-work-item-task.svg) | ![state work item task](State-work-item-task.png) |
| SM-M12 — Sprint period and recorded actual outcome | [state-sprint-lifecycle.puml](State-sprint-lifecycle.puml) | [SVG](State-sprint-lifecycle.svg) | ![state sprint lifecycle](State-sprint-lifecycle.png) |
| SM-M13 — Request lifecycle with revision-specific eligibility | [state-pull-request-lifecycle.puml](State-pull-request-lifecycle.puml) | [SVG](State-pull-request-lifecycle.svg) | ![state pull request lifecycle](State-pull-request-lifecycle.png) |
| SM-M14 — Actual attempt, cancellation request and runner uncertainty | [state-execution-attempt.puml](State-execution-attempt.puml) | [SVG](State-execution-attempt.svg) | ![state execution attempt](State-execution-attempt.png) |
| SM-M15 — Separate target authority and actual deployment effect | [state-deployment-effect.puml](State-deployment-effect.puml) | [SVG](State-deployment-effect.svg) | ![state deployment effect](State-deployment-effect.png) |
| SM-M16 — User-managed record retention and actual reclamation | [state-reference-aware-retention.puml](State-reference-aware-retention.puml) | [SVG](State-reference-aware-retention.svg) | ![state reference aware retention](State-reference-aware-retention.png) |
| SM-M17 — Gated isolated restoration and demonstrated usable state | [state-recovery-assessment.puml](State-recovery-assessment.puml) | [SVG](State-recovery-assessment.svg) | ![state recovery assessment](State-recovery-assessment.png) |
| SM-M18 — Observed operation result is separate from subject state | [state-operation-observation.puml](State-operation-observation.puml) | [SVG](State-operation-observation.svg) | ![state operation observation](State-operation-observation.png) |

## Control-flow-based view — 08

16 source-aligned domain activities plus one reusable result-classification subactivity. Full step meanings and proposal boundaries are in [the control-flow view](../System-analysis.md#analysis-functional-and-process-analysis--08-control-flow-based-view). Arrows show logical control, not atomic transactions or product execution proof.

| Model | Editable source | SVG | PNG |
| --- | --- | --- | --- |
| CF-M01 — Selected resume update and separate publication | [activity-profile-apply-publication.puml](Activity-profile-apply-publication.puml) | [SVG](Activity-profile-apply-publication.svg) | ![activity profile apply publication](Activity-profile-apply-publication.png) |
| CF-M02 — Download settings without link side effects | [activity-pdf-settings.puml](Activity-pdf-settings.puml) | [SVG](Activity-pdf-settings.svg) | ![activity pdf settings](Activity-pdf-settings.png) |
| CF-M03 — Independent link disablement and fresh request | [activity-disable-sharing-link.puml](Activity-disable-sharing-link.puml) | [SVG](Activity-disable-sharing-link.svg) | ![activity disable sharing link](Activity-disable-sharing-link.png) |
| CF-M04 — Controlled page and artifact retrieval | [activity-protected-retrieval.puml](Activity-protected-retrieval.puml) | [SVG](Activity-protected-retrieval.svg) | ![activity protected retrieval](Activity-protected-retrieval.png) |
| CF-M05 — Manual application preparation or progress recording | [activity-application-preparation.puml](Activity-application-preparation.puml) | [SVG](Activity-application-preparation.svg) | ![activity application preparation](Activity-application-preparation.png) |
| CF-M06 — Capture actual submitted materials | [activity-actual-submission-capture.puml](Activity-actual-submission-capture.puml) | [SVG](Activity-actual-submission-capture.svg) | ![activity actual submission capture](Activity-actual-submission-capture.png) |
| CF-M07 — Read correspondence or deliberately send | [activity-gmail-read-send-outcomes.puml](Activity-gmail-read-send-outcomes.puml) | [SVG](Activity-gmail-read-send-outcomes.svg) | ![activity gmail read send outcomes](Activity-gmail-read-send-outcomes.png) |
| CF-M08 — Local activity versus selected calendar synchronization | [activity-calendar-local-sync.puml](Activity-calendar-local-sync.puml) | [SVG](Activity-calendar-local-sync.svg) | ![activity calendar local sync](Activity-calendar-local-sync.png) |
| CF-M09 — Refinement, Sprint planning and Sprint completion | [activity-work-refine-plan-end.puml](Activity-work-refine-plan-end.puml) | [SVG](Activity-work-refine-plan-end.svg) | ![activity work refine plan end](Activity-work-refine-plan-end.png) |
| CF-M10 — Invitation acceptance and subsequent scoped access | [activity-collaboration-and-changed-grant.puml](Activity-collaboration-and-changed-grant.puml) | [SVG](Activity-collaboration-and-changed-grant.svg) | ![activity collaboration and changed grant](Activity-collaboration-and-changed-grant.png) |
| CF-M11 — Real Git read transfer or ref update | [activity-git-transfer.puml](Activity-git-transfer.puml) | [SVG](Activity-git-transfer.svg) | ![activity git transfer](Activity-git-transfer.png) |
| CF-M12 — Request, review or eligible integration | [activity-pull-request-review-merge.puml](Activity-pull-request-review-merge.puml) | [SVG](Activity-pull-request-review-merge.svg) | ![activity pull request review merge](Activity-pull-request-review-merge.png) |
| CF-M13 — Gated execution attempt and cancellation race | [activity-workflow-admission-attempt.puml](Activity-workflow-admission-attempt.puml) | [SVG](Activity-workflow-admission-attempt.svg) | ![activity workflow admission attempt](Activity-workflow-admission-attempt.png) |
| CF-M14 — Separate target-authorized deployment | [activity-separate-deployment.puml](Activity-separate-deployment.puml) | [SVG](Activity-separate-deployment.svg) | ![activity separate deployment](Activity-separate-deployment.png) |
| CF-M15 — Effective policy, file admission or restricted evidence | [activity-policy-admission-evidence.puml](Activity-policy-admission-evidence.puml) | [SVG](Activity-policy-admission-evidence.svg) | ![activity policy admission evidence](Activity-policy-admission-evidence.png) |
| CF-M16 — Conditional isolated restore and usability assessment | [activity-isolated-recovery-assessment.puml](Activity-isolated-recovery-assessment.puml) | [SVG](Activity-isolated-recovery-assessment.svg) | ![activity isolated recovery assessment](Activity-isolated-recovery-assessment.png) |
| CF-M17 — Reusable actual operation-result classification | [activity-operation-result-classification.puml](Activity-operation-result-classification.puml) | [SVG](Activity-operation-result-classification.svg) | ![activity operation result classification](Activity-operation-result-classification.png) |

## Rule-based view — 09

Eight focused decision trees accompany 18 finite-domain decision tables in [the rule view](../System-analysis.md#analysis-business-rules-and-operation-contracts--09-rule-based-view). These are decision alternatives, not execution order. Full conditions, results and authority remain in the tables.

| Decision | Editable source | SVG | PNG |
| --- | --- | --- | --- |
| RB-D01 — Resource-scoped operation eligibility | [rule-rb-d01-decision.puml](Rule-rb-d01-decision.puml) | [SVG](Rule-rb-d01-decision.svg) | ![rule rb d01 decision](Rule-rb-d01-decision.png) |
| RB-D04 — Protected selected representation eligibility | [rule-rb-d04-decision.puml](Rule-rb-d04-decision.puml) | [SVG](Rule-rb-d04-decision.svg) | ![rule rb d04 decision](Rule-rb-d04-decision.png) |
| RB-D06 — Actual submitted-set completeness | [rule-rb-d06-decision.puml](Rule-rb-d06-decision.puml) | [SVG](Rule-rb-d06-decision.svg) | ![rule rb d06 decision](Rule-rb-d06-decision.png) |
| RB-D07 — Reviewed provider send eligibility | [rule-rb-d07-decision.puml](Rule-rb-d07-decision.puml) | [SVG](Rule-rb-d07-decision.svg) | ![rule rb d07 decision](Rule-rb-d07-decision.png) |
| RB-D11 — Current revision-specific merge eligibility | [rule-rb-d11-decision.puml](Rule-rb-d11-decision.puml) | [SVG](Rule-rb-d11-decision.svg) | ![rule rb d11 decision](Rule-rb-d11-decision.png) |
| RB-D12 — Workflow execution admission | [rule-rb-d12-decision.puml](Rule-rb-d12-decision.puml) | [SVG](Rule-rb-d12-decision.svg) | ![rule rb d12 decision](Rule-rb-d12-decision.png) |
| RB-D15 — Reference-aware physical reclamation eligibility | [rule-rb-d15-decision.puml](Rule-rb-d15-decision.puml) | [SVG](Rule-rb-d15-decision.svg) | ![rule rb d15 decision](Rule-rb-d15-decision.png) |
| RB-D16 — Scoped usable recovery assessment | [rule-rb-d16-decision.puml](Rule-rb-d16-decision.puml) | [SVG](Rule-rb-d16-decision.svg) | ![rule rb d16 decision](Rule-rb-d16-decision.png) |

## Domain constraints and operation contracts — 10

Eight before/confirmed-after/frame relations illustrate selected contracts from [the contract view](../System-analysis.md#analysis-business-rules-and-operation-contracts--10-domain-constraints-and-operation-contracts). After-state applies only to actual confirmed permitted success; frame does not freeze independent concurrent actions or guarantee failure rollback. Full obligations/policy status remain in the text.

| Contract | Editable source | SVG | PNG |
| --- | --- | --- | --- |
| DC-O02 — Apply selected source changes to one draft | [contract-dc-o02-boundary.puml](Contract-dc-o02-boundary.puml) | [SVG](Contract-dc-o02-boundary.svg) | ![contract dc o02 boundary](Contract-dc-o02-boundary.png) |
| DC-O03 — Publish separately confirmed intended presentation | [contract-dc-o03-boundary.puml](Contract-dc-o03-boundary.puml) | [SVG](Contract-dc-o03-boundary.svg) | ![contract dc o03 boundary](Contract-dc-o03-boundary.png) |
| DC-O05 — Disable a specific protected link | [contract-dc-o05-boundary.puml](Contract-dc-o05-boundary.puml) | [SVG](Contract-dc-o05-boundary.svg) | ![contract dc o05 boundary](Contract-dc-o05-boundary.png) |
| DC-O12 — Submit a reviewed mail send/reply attempt | [contract-dc-o12-boundary.puml](Contract-dc-o12-boundary.puml) | [SVG](Contract-dc-o12-boundary.svg) | ![contract dc o12 boundary](Contract-dc-o12-boundary.png) |
| DC-O14 — Unlink a local provider mapping | [contract-dc-o14-boundary.puml](Contract-dc-o14-boundary.puml) | [SVG](Contract-dc-o14-boundary.svg) | ![contract dc o14 boundary](Contract-dc-o14-boundary.png) |
| DC-O26 — Merge only current eligible evaluated revisions | [contract-dc-o26-boundary.puml](Contract-dc-o26-boundary.puml) | [SVG](Contract-dc-o26-boundary.svg) | ![contract dc o26 boundary](Contract-dc-o26-boundary.png) |
| DC-O30 — Attempt a separately target-authorized deployment | [contract-dc-o30-boundary.puml](Contract-dc-o30-boundary.puml) | [SVG](Contract-dc-o30-boundary.svg) | ![contract dc o30 boundary](Contract-dc-o30-boundary.png) |
| DC-O37 — Perform and assess an authorized isolated recovery drill | [contract-dc-o37-boundary.puml](Contract-dc-o37-boundary.puml) | [SVG](Contract-dc-o37-boundary.svg) | ![contract dc o37 boundary](Contract-dc-o37-boundary.png) |

## Model consistency, traceability and review — 11

Three evidence/review relationship views accompany [SA-RV02](../System-analysis.md#analysis-review-and-design-handoff--11-model-consistency-traceability-and-review). A citation is not semantic criterion sufficiency, and a rendered diagram is not a product test or owner acceptance.

| View | Editable source | SVG | PNG |
| --- | --- | --- | --- |
| SA-RV02 — association is not verification | [review-trace-evidence-levels.puml](Review-trace-evidence-levels.puml) | [SVG](Review-trace-evidence-levels.svg) | ![review trace evidence levels](Review-trace-evidence-levels.png) |
| SA-RV02 — current analysis position | [review-current-position.puml](Review-current-position.puml) | [SVG](Review-current-position.svg) | ![review current position](Review-current-position.png) |
| SA-RV02 — review and change-impact route | [review-change-impact-route.puml](Review-change-impact-route.puml) | [SVG](Review-change-impact-route.svg) | ![review change impact route](Review-change-impact-route.png) |

## Interfaces and external interactions — 12

Eight focused logical exchange views accompany [file 12](../System-analysis.md#analysis-interfaces-security-and-quality-analysis--12-interfaces-and-external-interactions). Arrows identify direction; conditional access/facilities are not claims of installed components, selected transports, completed operations or automatically inherited authority.

| Family | Editable source | SVG | PNG |
| --- | --- | --- | --- |
| IF-01 — Private human interface | [interface-private-human-context.puml](Interface-private-human-context.puml) | [SVG](Interface-private-human-context.svg) | ![interface private human context](Interface-private-human-context.png) |
| IF-02 — Protected employer representation | [interface-employer-protected-representation.puml](Interface-employer-protected-representation.puml) | [SVG](Interface-employer-protected-representation.svg) | ![interface employer protected representation](Interface-employer-protected-representation.png) |
| IF-03 — Authorized file/PDF exchange | [interface-file-candidate-result.puml](Interface-file-candidate-result.puml) | [SVG](Interface-file-candidate-result.svg) | ![interface file candidate result](Interface-file-candidate-result.png) |
| IF-04 — Gmail provider operations | [interface-gmail-reviewed-effects.puml](Interface-gmail-reviewed-effects.puml) | [SVG](Interface-gmail-reviewed-effects.svg) | ![interface gmail reviewed effects](Interface-gmail-reviewed-effects.png) |
| IF-05 — Calendar provider and local mapping | [interface-calendar-local-provider.puml](Interface-calendar-local-provider.puml) | [SVG](Interface-calendar-local-provider.svg) | ![interface calendar local provider](Interface-calendar-local-provider.png) |
| IF-06 — Real Git-client boundary | [interface-real-git-client.puml](Interface-real-git-client.puml) | [SVG](Interface-real-git-client.svg) | ![interface real git client](Interface-real-git-client.png) |
| IF-07 — Conditional execution and separate deployment target | [interface-execution-separate-target.puml](Interface-execution-separate-target.puml) | [SVG](Interface-execution-separate-target.svg) | ![interface execution separate target](Interface-execution-separate-target.png) |
| IF-08 — Operational configuration, delivery and recovery | [interface-operating-delivery-recovery.puml](Interface-operating-delivery-recovery.puml) | [SVG](Interface-operating-delivery-recovery.svg) | ![interface operating delivery recovery](Interface-operating-delivery-recovery.png) |

## Security, quality and operational analysis — 13

Six focused analysis/evidence views accompany [file 13](../System-analysis.md#analysis-interfaces-security-and-quality-analysis--13-security-quality-and-operational-analysis). They do not select architecture, certify controls, prove capacity or authorize host/provider/execution/restore operations.

| View | Editable source | SVG | PNG |
| --- | --- | --- | --- |
| SQ — scoped authority across entry paths | [security-scoped-authority.puml](Security-scoped-authority.puml) | [SVG](Security-scoped-authority.svg) | ![security scoped authority](Security-scoped-authority.png) |
| SQ — data trust and conditional execution | [security-untrusted-content-execution.puml](Security-untrusted-content-execution.puml) | [SVG](Security-untrusted-content-execution.svg) | ![security untrusted content execution](Security-untrusted-content-execution.png) |
| SQ — measurable quality scenario contract | [quality-scenario-measurement.puml](Quality-scenario-measurement.puml) | [SVG](Quality-scenario-measurement.svg) | ![quality scenario measurement](Quality-scenario-measurement.png) |
| SQ — recovery evidence and current authority | [recovery-scoped-usable-state.puml](Recovery-scoped-usable-state.puml) | [SVG](Recovery-scoped-usable-state.svg) | ![recovery scoped usable state](Recovery-scoped-usable-state.png) |
| SQ — operation effect versus observation | [operations-effect-evidence.puml](Operations-effect-evidence.puml) | [SVG](Operations-effect-evidence.svg) | ![operations effect evidence](Operations-effect-evidence.png) |
| SQ — mixed workload and observed host limits | [operations-resource-envelope.puml](Operations-resource-envelope.puml) | [SVG](Operations-resource-envelope.svg) | ![operations resource envelope](Operations-resource-envelope.png) |

## Feasibility, dependencies and design handoff — 14

Five qualified evidence/gate/handoff/design-question/delivery views accompany [file 14](../System-analysis.md#analysis-review-and-design-handoff--14-feasibility-dependencies-and-design-handoff). They do not select architecture, certify feasibility, approve a forecast, change parent gates or authorize product work.

| View | Editable source | SVG | PNG |
| --- | --- | --- | --- |
| HD — evidence and dependent commitments | [handoff-evidence-dependent-commitment.puml](Handoff-evidence-dependent-commitment.puml) | [SVG](Handoff-evidence-dependent-commitment.svg) | ![handoff evidence dependent commitment](Handoff-evidence-dependent-commitment.png) |
| HD — existing gate relationships | [handoff-existing-review-gates.puml](Handoff-existing-review-gates.puml) | [SVG](Handoff-existing-review-gates.svg) | ![handoff existing review gates](Handoff-existing-review-gates.png) |
| HD — conditional handoff position | [handoff-package-position.puml](Handoff-package-position.puml) | [SVG](Handoff-package-position.svg) | ![handoff package position](Handoff-package-position.png) |
| HD — design evaluation record | [handoff-design-question-record.puml](Handoff-design-question-record.puml) | [SVG](Handoff-design-question-record.svg) | ![handoff design question record](Handoff-design-question-record.png) |
| HD — delivery reconciliation before coding | [handoff-delivery-reconciliation.puml](Handoff-delivery-reconciliation.puml) | [SVG](Handoff-delivery-reconciliation.svg) | ![handoff delivery reconciliation](Handoff-delivery-reconciliation.png) |

## Current Processes and Bottleneck Analysis — File 15

Evidence classification and investigation logic; not observed daily-business workflows.

| View | Source | SVG | PNG |
| --- | --- | --- | --- |
| CP — current evidence versus target and hypothesis | [PlantUML](Process-evidence-classes.puml) | [SVG](Process-evidence-classes.svg) | ![process evidence classes](Process-evidence-classes.png) |
| CP — documented artifact relationships | [PlantUML](Process-documented-artifact-trail.puml) | [SVG](Process-documented-artifact-trail.svg) | ![process documented artifact trail](Process-documented-artifact-trail.png) |
| CP — bounded current-process evidence need | [PlantUML](Process-current-workflow-questions.puml) | [SVG](Process-current-workflow-questions.svg) | ![process current workflow questions](Process-current-workflow-questions.png) |
| CP — hypothesis support or rejection | [PlantUML](Process-hypothesis-validation.puml) | [SVG](Process-hypothesis-validation.svg) | ![process hypothesis validation](Process-hypothesis-validation.png) |
| CP — intended improvement versus demonstrated result | [PlantUML](Process-improvement-evidence.puml) | [SVG](Process-improvement-evidence.svg) | ![process improvement evidence](Process-improvement-evidence.png) |

## Diagram notation alignment — November 1, 2026

See the [file-by-file report](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/03-system-analysis/evidence/notation-alignment-review-2026-11-01.md). New diagrams complement existing models. BPMN uses native XML; other new diagrams use PlantUML.

| Diagram | Notation | Editable | SVG | PNG |
| --- | --- | --- | --- | --- |
| Document navigation — 00 through 15 | Document dependency graph | [Source](Documentation-navigation.puml) | [SVG](Documentation-navigation.svg) | ![documentation navigation](Documentation-navigation.png) |
| Scope and stakeholder map | Stakeholder and scope diagram | [Source](Scope-stakeholder-map.puml) | [SVG](Scope-stakeholder-map.svg) | ![scope stakeholder map](Scope-stakeholder-map.png) |
| C4 Level 1 — target product context | C4 Level 1 | [Source](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/drivers-c4-system-context.puml) | [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/drivers-c4-system-context.svg) | ![drivers c4 system context](../../Design-assets/Archived-png/Drivers-c4-system-context.png) |
| C4 Level 2 — historical demo evidence only | C4 Level 2, bounded historical inventory | [Source](C4-observed-demo-containers.puml) | [SVG](C4-observed-demo-containers.svg) | ![c4 observed demo containers](C4-observed-demo-containers.png) |
| UML packages — logical domain groupings | UML package | [Source](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) | ![mvp system boundaries](../../Design-assets/Archived-png/Mvp-system-boundaries.png) |
| UML class detail — explicit proposed relationship ends | UML class with multiplicities | [Source](Domain-proposed-multiplicity.puml) | [SVG](Domain-proposed-multiplicity.svg) | ![domain proposed multiplicity](Domain-proposed-multiplicity.png) |
| DFD context — external information boundary | DFD context | [Source](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) | ![mvp system boundaries](../../Design-assets/Archived-png/Mvp-system-boundaries.png) |
| DFD Level 1 — content | DFD Level 1 | [Source](Function-dfd-level1-content.puml) | [SVG](Function-dfd-level1-content.svg) | ![function dfd level1 content](Function-dfd-level1-content.png) |
| DFD Level 1 — work-operations | DFD Level 1 | [Source](Function-store-information.puml) | [SVG](Function-store-information.svg) | ![function store information](Function-store-information.png) |
| Functional decomposition — responsibilities, not services | Functional decomposition tree | [Source](Function-decomposition.puml) | [SVG](Function-decomposition.svg) | ![function decomposition](Function-decomposition.png) |
| DFD — logical information ownership | DFD logical stores | [Source](Function-store-information.puml) | [SVG](Function-store-information.svg) | ![function store information](Function-store-information.png) |
| DFD Level 2 — F02 selected apply and publication | DFD Level 2 | [Source](Function-profile-level2.puml) | [SVG](Function-profile-level2.svg) | ![function profile level2](Function-profile-level2.png) |
| DC-O02 — UML object snapshots and frame condition | UML object snapshots | [Source](Contract-apply-object-snapshots.puml) | [SVG](Contract-apply-object-snapshots.svg) | ![contract apply object snapshots](Contract-apply-object-snapshots.png) |
| Selected traceability matrix — associations, not test results | Traceability matrix graphic | [Source](Traceability-selected-matrix.puml) | [SVG](Traceability-selected-matrix.svg) | ![traceability selected matrix](Traceability-selected-matrix.png) |
| UML component view — interface responsibilities | UML component-style logical interface view | [Source](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) | ![mvp system boundaries](../../Design-assets/Archived-png/Mvp-system-boundaries.png) |
| Request/response boundary — protocol-neutral contract | UML sequence | [Source](Interface-request-response-contract.puml) | [SVG](Interface-request-response-contract.svg) | ![interface request response contract](Interface-request-response-contract.png) |
| Trust-boundary DFD — logical protections to establish | Security DFD | [Source](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/06-design-quality-and-security-analysis/diagrams/security-trust-boundaries.puml) | [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/06-design-quality-and-security-analysis/diagrams/security-trust-boundaries.svg) | ![security trust boundaries](../../Design-assets/Archived-png/Security-trust-boundaries.png) |
| UML deployment — historical demo observation | UML deployment | [Source](Deployment-observed-host.puml) | [SVG](Deployment-observed-host.svg) | ![deployment observed host](Deployment-observed-host.png) |
| Dependency network — conditions, not scheduled dates | Dependency network | [Source](Handoff-dependency-network.puml) | [SVG](Handoff-dependency-network.svg) | ![handoff dependency network](Handoff-dependency-network.png) |
| Resumefolio — analysis ecosystem | High-level system overview | [Source](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) | ![mvp system boundaries](../../Design-assets/Archived-png/Mvp-system-boundaries.png) |
| As-Is — evidence-bounded current-process view | BPMN 2.0 | [Source](Process-bpmn-as-is-boundary.bpmn) | [SVG](Process-bpmn-as-is-boundary.svg) | ![process bpmn as is boundary](Process-bpmn-as-is-boundary.png) |
| To-Be — selected apply and separate publication | BPMN 2.0 | [Source](Process-bpmn-target-publication.bpmn) | [SVG](Process-bpmn-target-publication.svg) | ![process bpmn target publication](Process-bpmn-target-publication.png) |

## File 10 — constraint and outcome clarification

The eight existing contract-boundary views now use vertical layouts. The existing object snapshot remains.

| View | Source | SVG | PNG |
| --- | --- | --- | --- |
| Constraint application — common rules and accepted core | [PlantUML](Contract-constraint-application.puml) | [SVG](Contract-constraint-application.svg) | ![contract constraint application](Contract-constraint-application.png) |
| Contract outcomes — evidence required for a claim | [PlantUML](Contract-outcome-interpretation.puml) | [SVG](Contract-outcome-interpretation.svg) | ![contract outcome interpretation](Contract-outcome-interpretation.png) |

## File 13 — threats, infrastructure and conditional recovery

These views distinguish candidate controls, dated inventory and conditional future procedures.

| View | Editable | SVG | PNG |
| --- | --- | --- | --- |
| Trust boundaries and candidate threats | [PlantUML](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/06-design-quality-and-security-analysis/diagrams/security-trust-boundaries.puml) | [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/06-design-quality-and-security-analysis/diagrams/security-trust-boundaries.svg) | ![security trust boundaries](../../Design-assets/Archived-png/Security-trust-boundaries.png) |
| Infrastructure topology — observed demo and explicit gaps | [PlantUML](Security-infrastructure-topology.puml) | [SVG](Security-infrastructure-topology.svg) | ![security infrastructure topology](Security-infrastructure-topology.png) |
| HA / failover — conditional decision and verification sequence | [PlantUML](Security-ha-failover-sequence.puml) | [SVG](Security-ha-failover-sequence.svg) | ![security ha failover sequence](Security-ha-failover-sequence.png) |
| Disaster recovery — restore, validate and controlled resumption | [PlantUML](Security-disaster-recovery-sequence.puml) | [SVG](Security-disaster-recovery-sequence.svg) | ![security disaster recovery sequence](Security-disaster-recovery-sequence.png) |

## Whole-product ecosystem and connected platforms

The two coordinated maps cover logical product areas and all eight existing IF families. Status labels distinguish target exchanges from dated demo observations and unconfigured facilities.

| View | Source | SVG | PNG |
| --- | --- | --- | --- |
| Internal ecosystem and information relationships | [PlantUML](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) | ![mvp system boundaries](../../Design-assets/Archived-png/Mvp-system-boundaries.png) |
| External connections, directions and status | [PlantUML](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) | ![mvp system boundaries](../../Design-assets/Archived-png/Mvp-system-boundaries.png) |

## November 4 release applicability

Current MVP figures replace the former common-product boundary. Future and historical figures retain their details without committing them to MVP.

| Editable source | Current applicability |
| --- | --- |
| [activity-calendar-local-sync.puml](Activity-calendar-local-sync.puml) | MVP core / cross-cutting|
| [activity-gmail-read-send-outcomes.puml](Activity-gmail-read-send-outcomes.puml) | Future after MVP|
| [activity-pull-request-review-merge.puml](Activity-pull-request-review-merge.puml) | Future after MVP|
| [activity-separate-deployment.puml](Activity-separate-deployment.puml) | Future after MVP|
| [activity-workflow-admission-attempt.puml](Activity-workflow-admission-attempt.puml) | Future after MVP|
| [c4-system-context.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/drivers-c4-system-context.puml) | MVP systems|
| [data-execution-provenance-and-targets.puml](Data-execution-provenance-and-targets.puml) | Future after MVP|
| [data-provider-and-calendar-context.puml](Data-provider-and-calendar-context.puml) | Future after MVP|
| [data-work-and-sprint-planning.puml](Data-work-and-sprint-planning.puml) | Future after MVP|
| [domain-applications-and-communication.dot](Domain-applications-and-communication.dot) | MVP core / cross-cutting|
| [domain-applications-and-communication.puml](Domain-applications-and-communication.puml) | MVP core|
| [domain-execution-and-deployment.dot](Domain-execution-and-deployment.dot) | Future after MVP|
| [domain-execution-and-deployment.puml](Domain-execution-and-deployment.puml) | Future after MVP|
| [domain-package-responsibilities.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting|
| [domain-provider-communication.puml](Domain-provider-communication.puml) | Future after MVP|
| [ecosystem-overview.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting|
| [ecosystem-platform-connections.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting|
| [function-decomposition.puml](Function-decomposition.puml) | MVP systems|
| [function-dfd-context.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting|
| [interface-calendar-local-provider.puml](Interface-calendar-local-provider.puml) | Mixed MVP / future|
| [interface-execution-separate-target.puml](Interface-execution-separate-target.puml) | Future after MVP|
| [interface-gmail-reviewed-effects.puml](Interface-gmail-reviewed-effects.puml) | Future after MVP|
| [interface-logical-components.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting|
| [process-current-workflow-questions.puml](Process-current-workflow-questions.puml) | Method / document navigation|
| [scenario-calendar-local-sync.puml](Scenario-calendar-local-sync.puml) | Mixed MVP / future|
| [scenario-gmail-read-send-outcomes.puml](Scenario-gmail-read-send-outcomes.puml) | Future after MVP|
| [scenario-pull-request-review-merge.puml](Scenario-pull-request-review-merge.puml) | Future after MVP|
| [scenario-separate-deployment.puml](Scenario-separate-deployment.puml) | Future after MVP|
| [scenario-workflow-admission-attempt.puml](Scenario-workflow-admission-attempt.puml) | Future after MVP|
| [scope-stakeholder-map.puml](Scope-stakeholder-map.puml) | MVP systems|
| [security-untrusted-content-execution.puml](Security-untrusted-content-execution.puml) | Mixed MVP / future|
| [state-calendar-mapping.puml](State-calendar-mapping.puml) | MVP core / cross-cutting|
| [state-deployment-effect.puml](State-deployment-effect.puml) | Future after MVP|
| [state-execution-attempt.puml](State-execution-attempt.puml) | Future after MVP|
| [state-provider-connection.puml](State-provider-connection.puml) | Future after MVP|
| [state-pull-request-lifecycle.puml](State-pull-request-lifecycle.puml) | Future after MVP|
| [state-sprint-lifecycle.puml](State-sprint-lifecycle.puml) | Future after MVP|
| [system-context-external.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot) | MVP core / cross-cutting|
| [system-context-external.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting|
| [system-context-human.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot) | MVP core / cross-cutting|
| [system-context-human.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting|
| [system-context-information-boundaries.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot) | MVP core / cross-cutting|
| [system-context-information-boundaries.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting|

| [domain-work-management.puml](Domain-work-management.puml) | Future after MVP|
| [function-store-information.puml](Function-store-information.puml) | MVP systems|
| [process-documented-artifact-trail.puml](Process-documented-artifact-trail.puml) | Historical / alternative|
| [scenario-work-refine-plan-end.puml](Scenario-work-refine-plan-end.puml) | Mixed MVP / future|
| [traceability-selected-matrix.puml](Traceability-selected-matrix.puml) | Historical / alternative|

Alternative Graphviz export for [domain-applications-and-communication.dot](Domain-applications-and-communication.dot): [SVG](Domain-applications-and-communication-graphviz.svg) · ![domain applications and communication graphviz](Domain-applications-and-communication-graphviz.png). The ordinary same-stem exports follow the PlantUML source.

Alternative Graphviz export for [domain-execution-and-deployment.dot](Domain-execution-and-deployment.dot): [SVG](Domain-execution-and-deployment-graphviz.svg) · ![domain execution and deployment graphviz](Domain-execution-and-deployment-graphviz.png). The ordinary same-stem exports follow the PlantUML source.

Alternative Graphviz export for [system-context-external.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot): [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.svg) · ![logical component ownership](../../Design-assets/Archived-png/Logical-component-ownership.png). The ordinary same-stem exports follow the PlantUML source.

Alternative Graphviz export for [system-context-human.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot): [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.svg) · ![logical component ownership](../../Design-assets/Archived-png/Logical-component-ownership.png). The ordinary same-stem exports follow the PlantUML source.

Alternative Graphviz export for [system-context-information-boundaries.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot): [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.svg) · ![logical component ownership](../../Design-assets/Archived-png/Logical-component-ownership.png). The ordinary same-stem exports follow the PlantUML source.

## Complete diagram alignment — November 4

[Full project inventory and verification limits](../../04-System-design/01-High-level-design/High-level-design.md#design-record-01-software-architecture-diagrams-diagram-catalog-md). This current disposition supersedes earlier partial diagram-allocation lists.

| Editable source or visual | Current applicability | Matching exports |
| --- | --- | --- |
| [activity-actual-submission-capture.puml](Activity-actual-submission-capture.puml) | MVP core / cross-cutting| [SVG](Activity-actual-submission-capture.svg) · ![activity actual submission capture](Activity-actual-submission-capture.png) |
| [activity-application-preparation.puml](Activity-application-preparation.puml) | MVP core / cross-cutting| [SVG](Activity-application-preparation.svg) · ![activity application preparation](Activity-application-preparation.png) |
| [activity-calendar-local-sync.puml](Activity-calendar-local-sync.puml) | MVP core / cross-cutting| [SVG](Activity-calendar-local-sync.svg) · ![activity calendar local sync](Activity-calendar-local-sync.png) |
| [activity-collaboration-and-changed-grant.puml](Activity-collaboration-and-changed-grant.puml) | MVP core / cross-cutting| [SVG](Activity-collaboration-and-changed-grant.svg) · ![activity collaboration and changed grant](Activity-collaboration-and-changed-grant.png) |
| [activity-disable-sharing-link.puml](Activity-disable-sharing-link.puml) | MVP core / cross-cutting| [SVG](Activity-disable-sharing-link.svg) · ![activity disable sharing link](Activity-disable-sharing-link.png) |
| [activity-git-transfer.puml](Activity-git-transfer.puml) | MVP ProjectForge| [SVG](Activity-git-transfer.svg) · ![activity git transfer](Activity-git-transfer.png) |
| [activity-gmail-read-send-outcomes.puml](Activity-gmail-read-send-outcomes.puml) | Future after MVP| [SVG](Activity-gmail-read-send-outcomes.svg) · ![activity gmail read send outcomes](Activity-gmail-read-send-outcomes.png) |
| [activity-isolated-recovery-assessment.puml](Activity-isolated-recovery-assessment.puml) | MVP core / cross-cutting| [SVG](Activity-isolated-recovery-assessment.svg) · ![activity isolated recovery assessment](Activity-isolated-recovery-assessment.png) |
| [activity-operation-result-classification.puml](Activity-operation-result-classification.puml) | MVP core / cross-cutting| [SVG](Activity-operation-result-classification.svg) · ![activity operation result classification](Activity-operation-result-classification.png) |
| [activity-pdf-settings.puml](Activity-pdf-settings.puml) | MVP core / cross-cutting| [SVG](Activity-pdf-settings.svg) · ![activity pdf settings](Activity-pdf-settings.png) |
| [activity-policy-admission-evidence.puml](Activity-policy-admission-evidence.puml) | MVP core / cross-cutting| [SVG](Activity-policy-admission-evidence.svg) · ![activity policy admission evidence](Activity-policy-admission-evidence.png) |
| [activity-profile-apply-publication.puml](Activity-profile-apply-publication.puml) | MVP core / cross-cutting| [SVG](Activity-profile-apply-publication.svg) · ![activity profile apply publication](Activity-profile-apply-publication.png) |
| [activity-protected-retrieval.puml](Activity-protected-retrieval.puml) | MVP core / cross-cutting| [SVG](Activity-protected-retrieval.svg) · ![activity protected retrieval](Activity-protected-retrieval.png) |
| [activity-pull-request-review-merge.puml](Activity-pull-request-review-merge.puml) | Future after MVP| [SVG](Activity-pull-request-review-merge.svg) · ![activity pull request review merge](Activity-pull-request-review-merge.png) |
| [activity-separate-deployment.puml](Activity-separate-deployment.puml) | Future after MVP| [SVG](Activity-separate-deployment.svg) · ![activity separate deployment](Activity-separate-deployment.png) |
| [activity-work-refine-plan-end.puml](Activity-work-refine-plan-end.puml) | Mixed MVP / future| [SVG](Activity-work-refine-plan-end.svg) · ![activity work refine plan end](Activity-work-refine-plan-end.png) |
| [activity-workflow-admission-attempt.puml](Activity-workflow-admission-attempt.puml) | Future after MVP| [SVG](Activity-workflow-admission-attempt.svg) · ![activity workflow admission attempt](Activity-workflow-admission-attempt.png) |
| [analysis-inputs-and-outputs.dot](Analysis-inputs-and-outputs.dot) | MVP core / cross-cutting| [SVG](Analysis-inputs-and-outputs-graphviz.svg) · ![analysis inputs and outputs graphviz](Analysis-inputs-and-outputs-graphviz.png) |
| [analysis-inputs-and-outputs.puml](Analysis-inputs-and-outputs.puml) | MVP core / cross-cutting| [SVG](Analysis-inputs-and-outputs.svg) · ![analysis inputs and outputs](Analysis-inputs-and-outputs.png) |
| [analysis-seven-view-consistency.dot](Analysis-seven-view-consistency.dot) | MVP core / cross-cutting| [SVG](Analysis-seven-view-consistency-graphviz.svg) · ![analysis seven view consistency graphviz](Analysis-seven-view-consistency-graphviz.png) |
| [analysis-seven-view-consistency.puml](Analysis-seven-view-consistency.puml) | MVP core / cross-cutting| [SVG](Analysis-seven-view-consistency.svg) · ![analysis seven view consistency](Analysis-seven-view-consistency.png) |
| [c4-observed-demo-containers.puml](C4-observed-demo-containers.puml) | Historical / alternative| [SVG](C4-observed-demo-containers.svg) · ![c4 observed demo containers](C4-observed-demo-containers.png) |
| [c4-system-context.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/drivers-c4-system-context.puml) | MVP systems| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/drivers-c4-system-context.svg) · ![drivers c4 system context](../../Design-assets/Archived-png/Drivers-c4-system-context.png) |
| [contract-apply-object-snapshots.puml](Contract-apply-object-snapshots.puml) | MVP core / cross-cutting| [SVG](Contract-apply-object-snapshots.svg) · ![contract apply object snapshots](Contract-apply-object-snapshots.png) |
| [contract-constraint-application.puml](Contract-constraint-application.puml) | MVP core / cross-cutting| [SVG](Contract-constraint-application.svg) · ![contract constraint application](Contract-constraint-application.png) |
| [contract-dc-o02-boundary.puml](Contract-dc-o02-boundary.puml) | MVP core / cross-cutting| [SVG](Contract-dc-o02-boundary.svg) · ![contract dc o02 boundary](Contract-dc-o02-boundary.png) |
| [contract-dc-o03-boundary.puml](Contract-dc-o03-boundary.puml) | MVP core / cross-cutting| [SVG](Contract-dc-o03-boundary.svg) · ![contract dc o03 boundary](Contract-dc-o03-boundary.png) |
| [contract-dc-o05-boundary.puml](Contract-dc-o05-boundary.puml) | MVP core / cross-cutting| [SVG](Contract-dc-o05-boundary.svg) · ![contract dc o05 boundary](Contract-dc-o05-boundary.png) |
| [contract-dc-o12-boundary.puml](Contract-dc-o12-boundary.puml) | Future after MVP| [SVG](Contract-dc-o12-boundary.svg) · ![contract dc o12 boundary](Contract-dc-o12-boundary.png) |
| [contract-dc-o14-boundary.puml](Contract-dc-o14-boundary.puml) | Future after MVP| [SVG](Contract-dc-o14-boundary.svg) · ![contract dc o14 boundary](Contract-dc-o14-boundary.png) |
| [contract-dc-o26-boundary.puml](Contract-dc-o26-boundary.puml) | Future after MVP| [SVG](Contract-dc-o26-boundary.svg) · ![contract dc o26 boundary](Contract-dc-o26-boundary.png) |
| [contract-dc-o30-boundary.puml](Contract-dc-o30-boundary.puml) | Future after MVP| [SVG](Contract-dc-o30-boundary.svg) · ![contract dc o30 boundary](Contract-dc-o30-boundary.png) |
| [contract-dc-o37-boundary.puml](Contract-dc-o37-boundary.puml) | MVP core / cross-cutting| [SVG](Contract-dc-o37-boundary.svg) · ![contract dc o37 boundary](Contract-dc-o37-boundary.png) |
| [contract-outcome-interpretation.puml](Contract-outcome-interpretation.puml) | MVP core / cross-cutting| [SVG](Contract-outcome-interpretation.svg) · ![contract outcome interpretation](Contract-outcome-interpretation.png) |
| [data-applications-and-actual-material.puml](Data-applications-and-actual-material.puml) | MVP core| [SVG](Data-applications-and-actual-material.svg) · ![data applications and actual material](Data-applications-and-actual-material.png) |
| [data-authority-policy-and-recovery.puml](Data-authority-policy-and-recovery.puml) | MVP core / cross-cutting| [SVG](Data-authority-policy-and-recovery.svg) · ![data authority policy and recovery](Data-authority-policy-and-recovery.png) |
| [data-evidence-language-and-selection.puml](Data-evidence-language-and-selection.puml) | MVP core / cross-cutting| [SVG](Data-evidence-language-and-selection.svg) · ![data evidence language and selection](Data-evidence-language-and-selection.png) |
| [data-execution-provenance-and-targets.puml](Data-execution-provenance-and-targets.puml) | Future after MVP| [SVG](Data-execution-provenance-and-targets.svg) · ![data execution provenance and targets](Data-execution-provenance-and-targets.png) |
| [data-git-revisions-and-collaboration.puml](Data-git-revisions-and-collaboration.puml) | Future after MVP| [SVG](Data-git-revisions-and-collaboration.svg) · ![data git revisions and collaboration](Data-git-revisions-and-collaboration.png) |
| [data-profile-and-tailoring.puml](Data-profile-and-tailoring.puml) | MVP core / cross-cutting| [SVG](Data-profile-and-tailoring.svg) · ![data profile and tailoring](Data-profile-and-tailoring.png) |
| [data-provider-and-calendar-context.puml](Data-provider-and-calendar-context.puml) | Future after MVP| [SVG](Data-provider-and-calendar-context.svg) · ![data provider and calendar context](Data-provider-and-calendar-context.png) |
| [data-publication-pdf-and-sharing.puml](Data-publication-pdf-and-sharing.puml) | MVP core / cross-cutting| [SVG](Data-publication-pdf-and-sharing.svg) · ![data publication pdf and sharing](Data-publication-pdf-and-sharing.png) |
| [data-work-and-sprint-planning.puml](Data-work-and-sprint-planning.puml) | Future after MVP| [SVG](Data-work-and-sprint-planning.svg) · ![data work and sprint planning](Data-work-and-sprint-planning.png) |
| [deployment-observed-host.puml](Deployment-observed-host.puml) | Historical / alternative| [SVG](Deployment-observed-host.svg) · ![deployment observed host](Deployment-observed-host.png) |
| [documentation-navigation.puml](Documentation-navigation.puml) | MVP core / cross-cutting| [SVG](Documentation-navigation.svg) · ![documentation navigation](Documentation-navigation.png) |
| [domain-access-files-and-recovery.dot](Domain-access-files-and-recovery.dot) | MVP core / cross-cutting| [SVG](Domain-access-files-and-recovery-graphviz.svg) · ![domain access files and recovery graphviz](Domain-access-files-and-recovery-graphviz.png) |
| [domain-access-files-and-recovery.puml](Domain-access-files-and-recovery.puml) | MVP core / cross-cutting| [SVG](Domain-access-files-and-recovery.svg) · ![domain access files and recovery](Domain-access-files-and-recovery.png) |
| [domain-applications-and-communication.dot](Domain-applications-and-communication.dot) | MVP core / cross-cutting| [SVG](Domain-applications-and-communication-graphviz.svg) · ![domain applications and communication graphviz](Domain-applications-and-communication-graphviz.png) |
| [domain-applications-and-communication.puml](Domain-applications-and-communication.puml) | MVP core| [SVG](Domain-applications-and-communication.svg) · ![domain applications and communication](Domain-applications-and-communication.png) |
| [domain-evidence-and-language.puml](Domain-evidence-and-language.puml) | MVP core / cross-cutting| [SVG](Domain-evidence-and-language.svg) · ![domain evidence and language](Domain-evidence-and-language.png) |
| [domain-execution-and-deployment.dot](Domain-execution-and-deployment.dot) | Future after MVP| [SVG](Domain-execution-and-deployment-graphviz.svg) · ![domain execution and deployment graphviz](Domain-execution-and-deployment-graphviz.png) |
| [domain-execution-and-deployment.puml](Domain-execution-and-deployment.puml) | Future after MVP| [SVG](Domain-execution-and-deployment.svg) · ![domain execution and deployment](Domain-execution-and-deployment.png) |
| [domain-git-collaboration.dot](Domain-git-collaboration.dot) | Future after MVP| [SVG](Domain-git-collaboration-graphviz.svg) · ![domain git collaboration graphviz](Domain-git-collaboration-graphviz.png) |
| [domain-git-collaboration.puml](Domain-git-collaboration.puml) | Future after MVP| [SVG](Domain-git-collaboration.svg) · ![domain git collaboration](Domain-git-collaboration.png) |
| [domain-package-responsibilities.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) · ![mvp system boundaries](../../Design-assets/Archived-png/Mvp-system-boundaries.png) |
| [domain-professional-presentation.dot](Domain-professional-presentation.dot) | MVP core / cross-cutting| [SVG](Domain-professional-presentation-graphviz.svg) · ![domain professional presentation graphviz](Domain-professional-presentation-graphviz.png) |
| [domain-professional-presentation.puml](Domain-professional-presentation.puml) | MVP core / cross-cutting| [SVG](Domain-professional-presentation.svg) · ![domain professional presentation](Domain-professional-presentation.png) |
| [domain-proposed-multiplicity.puml](Domain-proposed-multiplicity.puml) | MVP core / cross-cutting| [SVG](Domain-proposed-multiplicity.svg) · ![domain proposed multiplicity](Domain-proposed-multiplicity.png) |
| [domain-provider-communication.puml](Domain-provider-communication.puml) | Future after MVP| [SVG](Domain-provider-communication.svg) · ![domain provider communication](Domain-provider-communication.png) |
| [domain-publication-and-sharing.dot](Domain-publication-and-sharing.dot) | MVP core / cross-cutting| [SVG](Domain-publication-and-sharing-graphviz.svg) · ![domain publication and sharing graphviz](Domain-publication-and-sharing-graphviz.png) |
| [domain-publication-and-sharing.puml](Domain-publication-and-sharing.puml) | MVP core / cross-cutting| [SVG](Domain-publication-and-sharing.svg) · ![domain publication and sharing](Domain-publication-and-sharing.png) |
| [domain-work-management.dot](Domain-work-management.dot) | Future after MVP| [SVG](Domain-work-management-graphviz.svg) · ![domain work management graphviz](Domain-work-management-graphviz.png) |
| [domain-work-management.puml](Domain-work-management.puml) | Future after MVP| [SVG](Domain-work-management.svg) · ![domain work management](Domain-work-management.png) |
| [ecosystem-overview.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) · ![mvp system boundaries](../../Design-assets/Archived-png/Mvp-system-boundaries.png) |
| [ecosystem-platform-connections.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) · ![mvp system boundaries](../../Design-assets/Archived-png/Mvp-system-boundaries.png) |
| [function-decomposition.puml](Function-decomposition.puml) | MVP systems| [SVG](Function-decomposition.svg) · ![function decomposition](Function-decomposition.png) |
| [function-dfd-context.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) · ![mvp system boundaries](../../Design-assets/Archived-png/Mvp-system-boundaries.png) |
| [function-dfd-level1-content.puml](Function-dfd-level1-content.puml) | MVP core| [SVG](Function-dfd-level1-content.svg) · ![function dfd level1 content](Function-dfd-level1-content.png) |
| [function-dfd-level1-work-operations.puml](Function-store-information.puml) | MVP systems| [SVG](Function-store-information.svg) · ![function store information](Function-store-information.png) |
| [function-profile-level2.puml](Function-profile-level2.puml) | MVP core / cross-cutting| [SVG](Function-profile-level2.svg) · ![function profile level2](Function-profile-level2.png) |
| [function-store-information.puml](Function-store-information.puml) | MVP systems| [SVG](Function-store-information.svg) · ![function store information](Function-store-information.png) |
| [handoff-delivery-reconciliation.puml](Handoff-delivery-reconciliation.puml) | Method / document navigation| [SVG](Handoff-delivery-reconciliation.svg) · ![handoff delivery reconciliation](Handoff-delivery-reconciliation.png) |
| [handoff-dependency-network.puml](Handoff-dependency-network.puml) | MVP delivery| [SVG](Handoff-dependency-network.svg) · ![handoff dependency network](Handoff-dependency-network.png) |
| [handoff-design-question-record.puml](Handoff-design-question-record.puml) | MVP core / cross-cutting| [SVG](Handoff-design-question-record.svg) · ![handoff design question record](Handoff-design-question-record.png) |
| [handoff-evidence-dependent-commitment.puml](Handoff-evidence-dependent-commitment.puml) | MVP core / cross-cutting| [SVG](Handoff-evidence-dependent-commitment.svg) · ![handoff evidence dependent commitment](Handoff-evidence-dependent-commitment.png) |
| [handoff-existing-review-gates.puml](Handoff-existing-review-gates.puml) | MVP core / cross-cutting| [SVG](Handoff-existing-review-gates.svg) · ![handoff existing review gates](Handoff-existing-review-gates.png) |
| [handoff-package-position.puml](Handoff-package-position.puml) | MVP core / cross-cutting| [SVG](Handoff-package-position.svg) · ![handoff package position](Handoff-package-position.png) |
| [interface-calendar-local-provider.puml](Interface-calendar-local-provider.puml) | Mixed MVP / future| [SVG](Interface-calendar-local-provider.svg) · ![interface calendar local provider](Interface-calendar-local-provider.png) |
| [interface-employer-protected-representation.puml](Interface-employer-protected-representation.puml) | MVP core / cross-cutting| [SVG](Interface-employer-protected-representation.svg) · ![interface employer protected representation](Interface-employer-protected-representation.png) |
| [interface-execution-separate-target.puml](Interface-execution-separate-target.puml) | Future after MVP| [SVG](Interface-execution-separate-target.svg) · ![interface execution separate target](Interface-execution-separate-target.png) |
| [interface-file-candidate-result.puml](Interface-file-candidate-result.puml) | MVP core / cross-cutting| [SVG](Interface-file-candidate-result.svg) · ![interface file candidate result](Interface-file-candidate-result.png) |
| [interface-gmail-reviewed-effects.puml](Interface-gmail-reviewed-effects.puml) | Future after MVP| [SVG](Interface-gmail-reviewed-effects.svg) · ![interface gmail reviewed effects](Interface-gmail-reviewed-effects.png) |
| [interface-logical-components.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) · ![mvp system boundaries](../../Design-assets/Archived-png/Mvp-system-boundaries.png) |
| [interface-operating-delivery-recovery.puml](Interface-operating-delivery-recovery.puml) | Mixed MVP / future| [SVG](Interface-operating-delivery-recovery.svg) · ![interface operating delivery recovery](Interface-operating-delivery-recovery.png) |
| [interface-private-human-context.puml](Interface-private-human-context.puml) | MVP core / cross-cutting| [SVG](Interface-private-human-context.svg) · ![interface private human context](Interface-private-human-context.png) |
| [interface-real-git-client.puml](Interface-real-git-client.puml) | MVP ProjectForge| [SVG](Interface-real-git-client.svg) · ![interface real git client](Interface-real-git-client.png) |
| [interface-request-response-contract.puml](Interface-request-response-contract.puml) | MVP core / cross-cutting| [SVG](Interface-request-response-contract.svg) · ![interface request response contract](Interface-request-response-contract.png) |
| [operations-effect-evidence.puml](Operations-effect-evidence.puml) | MVP core / cross-cutting| [SVG](Operations-effect-evidence.svg) · ![operations effect evidence](Operations-effect-evidence.png) |
| [operations-resource-envelope.puml](Operations-resource-envelope.puml) | MVP core / cross-cutting| [SVG](Operations-resource-envelope.svg) · ![operations resource envelope](Operations-resource-envelope.png) |
| [process-bpmn-as-is-boundary.bpmn](Process-bpmn-as-is-boundary.bpmn) | Historical / evidence limit | [SVG](Process-bpmn-as-is-boundary.svg) · ![process bpmn as is boundary](Process-bpmn-as-is-boundary.png) |
| [process-bpmn-target-publication.bpmn](Process-bpmn-target-publication.bpmn) | MVP core publication | [SVG](Process-bpmn-target-publication.svg) · ![process bpmn target publication](Process-bpmn-target-publication.png) |
| [process-current-workflow-questions.puml](Process-current-workflow-questions.puml) | Method / document navigation| [SVG](Process-current-workflow-questions.svg) · ![process current workflow questions](Process-current-workflow-questions.png) |
| [process-documented-artifact-trail.puml](Process-documented-artifact-trail.puml) | Historical / alternative| [SVG](Process-documented-artifact-trail.svg) · ![process documented artifact trail](Process-documented-artifact-trail.png) |
| [process-evidence-classes.puml](Process-evidence-classes.puml) | MVP core / cross-cutting| [SVG](Process-evidence-classes.svg) · ![process evidence classes](Process-evidence-classes.png) |
| [process-hypothesis-validation.puml](Process-hypothesis-validation.puml) | MVP core / cross-cutting| [SVG](Process-hypothesis-validation.svg) · ![process hypothesis validation](Process-hypothesis-validation.png) |
| [process-improvement-evidence.puml](Process-improvement-evidence.puml) | MVP core / cross-cutting| [SVG](Process-improvement-evidence.svg) · ![process improvement evidence](Process-improvement-evidence.png) |
| [quality-scenario-measurement.puml](Quality-scenario-measurement.puml) | MVP core / cross-cutting| [SVG](Quality-scenario-measurement.svg) · ![quality scenario measurement](Quality-scenario-measurement.png) |
| [recovery-scoped-usable-state.puml](Recovery-scoped-usable-state.puml) | MVP core / cross-cutting| [SVG](Recovery-scoped-usable-state.svg) · ![recovery scoped usable state](Recovery-scoped-usable-state.png) |
| [review-change-impact-route.puml](Review-change-impact-route.puml) | MVP core / cross-cutting| [SVG](Review-change-impact-route.svg) · ![review change impact route](Review-change-impact-route.png) |
| [review-current-position.puml](Review-current-position.puml) | Historical / alternative| [SVG](Review-current-position.svg) · ![review current position](Review-current-position.png) |
| [review-trace-evidence-levels.puml](Review-trace-evidence-levels.puml) | Historical / alternative| [SVG](Review-trace-evidence-levels.svg) · ![review trace evidence levels](Review-trace-evidence-levels.png) |
| [rule-rb-d01-decision.puml](Rule-rb-d01-decision.puml) | MVP core / cross-cutting| [SVG](Rule-rb-d01-decision.svg) · ![rule rb d01 decision](Rule-rb-d01-decision.png) |
| [rule-rb-d04-decision.puml](Rule-rb-d04-decision.puml) | MVP core / cross-cutting| [SVG](Rule-rb-d04-decision.svg) · ![rule rb d04 decision](Rule-rb-d04-decision.png) |
| [rule-rb-d06-decision.puml](Rule-rb-d06-decision.puml) | MVP core / cross-cutting| [SVG](Rule-rb-d06-decision.svg) · ![rule rb d06 decision](Rule-rb-d06-decision.png) |
| [rule-rb-d07-decision.puml](Rule-rb-d07-decision.puml) | Future after MVP| [SVG](Rule-rb-d07-decision.svg) · ![rule rb d07 decision](Rule-rb-d07-decision.png) |
| [rule-rb-d11-decision.puml](Rule-rb-d11-decision.puml) | Future after MVP| [SVG](Rule-rb-d11-decision.svg) · ![rule rb d11 decision](Rule-rb-d11-decision.png) |
| [rule-rb-d12-decision.puml](Rule-rb-d12-decision.puml) | Future after MVP| [SVG](Rule-rb-d12-decision.svg) · ![rule rb d12 decision](Rule-rb-d12-decision.png) |
| [rule-rb-d15-decision.puml](Rule-rb-d15-decision.puml) | MVP core / cross-cutting| [SVG](Rule-rb-d15-decision.svg) · ![rule rb d15 decision](Rule-rb-d15-decision.png) |
| [rule-rb-d16-decision.puml](Rule-rb-d16-decision.puml) | MVP core / cross-cutting| [SVG](Rule-rb-d16-decision.svg) · ![rule rb d16 decision](Rule-rb-d16-decision.png) |
| [scenario-actual-submission-capture.puml](Scenario-actual-submission-capture.puml) | MVP core / cross-cutting| [SVG](Scenario-actual-submission-capture.svg) · ![scenario actual submission capture](Scenario-actual-submission-capture.png) |
| [scenario-application-preparation.puml](Scenario-application-preparation.puml) | MVP core / cross-cutting| [SVG](Scenario-application-preparation.svg) · ![scenario application preparation](Scenario-application-preparation.png) |
| [scenario-calendar-local-sync.puml](Scenario-calendar-local-sync.puml) | Mixed MVP / future| [SVG](Scenario-calendar-local-sync.svg) · ![scenario calendar local sync](Scenario-calendar-local-sync.png) |
| [scenario-collaboration-and-changed-grant.puml](Scenario-collaboration-and-changed-grant.puml) | MVP core / cross-cutting| [SVG](Scenario-collaboration-and-changed-grant.svg) · ![scenario collaboration and changed grant](Scenario-collaboration-and-changed-grant.png) |
| [scenario-disable-sharing-link.puml](Scenario-disable-sharing-link.puml) | MVP core / cross-cutting| [SVG](Scenario-disable-sharing-link.svg) · ![scenario disable sharing link](Scenario-disable-sharing-link.png) |
| [scenario-git-transfer.puml](Scenario-git-transfer.puml) | MVP ProjectForge| [SVG](Scenario-git-transfer.svg) · ![scenario git transfer](Scenario-git-transfer.png) |
| [scenario-gmail-read-send-outcomes.puml](Scenario-gmail-read-send-outcomes.puml) | Future after MVP| [SVG](Scenario-gmail-read-send-outcomes.svg) · ![scenario gmail read send outcomes](Scenario-gmail-read-send-outcomes.png) |
| [scenario-isolated-recovery-assessment.puml](Scenario-isolated-recovery-assessment.puml) | MVP core / cross-cutting| [SVG](Scenario-isolated-recovery-assessment.svg) · ![scenario isolated recovery assessment](Scenario-isolated-recovery-assessment.png) |
| [scenario-pdf-settings.puml](Scenario-pdf-settings.puml) | MVP core / cross-cutting| [SVG](Scenario-pdf-settings.svg) · ![scenario pdf settings](Scenario-pdf-settings.png) |
| [scenario-policy-admission-evidence.puml](Scenario-policy-admission-evidence.puml) | MVP core / cross-cutting| [SVG](Scenario-policy-admission-evidence.svg) · ![scenario policy admission evidence](Scenario-policy-admission-evidence.png) |
| [scenario-profile-apply-publication.puml](Scenario-profile-apply-publication.puml) | MVP core / cross-cutting| [SVG](Scenario-profile-apply-publication.svg) · ![scenario profile apply publication](Scenario-profile-apply-publication.png) |
| [scenario-protected-retrieval.puml](Scenario-protected-retrieval.puml) | MVP core / cross-cutting| [SVG](Scenario-protected-retrieval.svg) · ![scenario protected retrieval](Scenario-protected-retrieval.png) |
| [scenario-pull-request-review-merge.puml](Scenario-pull-request-review-merge.puml) | Future after MVP| [SVG](Scenario-pull-request-review-merge.svg) · ![scenario pull request review merge](Scenario-pull-request-review-merge.png) |
| [scenario-separate-deployment.puml](Scenario-separate-deployment.puml) | Future after MVP| [SVG](Scenario-separate-deployment.svg) · ![scenario separate deployment](Scenario-separate-deployment.png) |
| [scenario-work-refine-plan-end.puml](Scenario-work-refine-plan-end.puml) | Mixed MVP / future| [SVG](Scenario-work-refine-plan-end.svg) · ![scenario work refine plan end](Scenario-work-refine-plan-end.png) |
| [scenario-workflow-admission-attempt.puml](Scenario-workflow-admission-attempt.puml) | Future after MVP| [SVG](Scenario-workflow-admission-attempt.svg) · ![scenario workflow admission attempt](Scenario-workflow-admission-attempt.png) |
| [scope-stakeholder-map.puml](Scope-stakeholder-map.puml) | MVP systems| [SVG](Scope-stakeholder-map.svg) · ![scope stakeholder map](Scope-stakeholder-map.png) |
| [security-data-flow-trust.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/06-design-quality-and-security-analysis/diagrams/security-trust-boundaries.puml) | MVP systems| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/06-design-quality-and-security-analysis/diagrams/security-trust-boundaries.svg) · ![security trust boundaries](../../Design-assets/Archived-png/Security-trust-boundaries.png) |
| [security-disaster-recovery-sequence.puml](Security-disaster-recovery-sequence.puml) | MVP core / cross-cutting| [SVG](Security-disaster-recovery-sequence.svg) · ![security disaster recovery sequence](Security-disaster-recovery-sequence.png) |
| [security-ha-failover-sequence.puml](Security-ha-failover-sequence.puml) | MVP core / cross-cutting| [SVG](Security-ha-failover-sequence.svg) · ![security ha failover sequence](Security-ha-failover-sequence.png) |
| [security-infrastructure-topology.puml](Security-infrastructure-topology.puml) | Historical / alternative| [SVG](Security-infrastructure-topology.svg) · ![security infrastructure topology](Security-infrastructure-topology.png) |
| [security-scoped-authority.puml](Security-scoped-authority.puml) | MVP core / cross-cutting| [SVG](Security-scoped-authority.svg) · ![security scoped authority](Security-scoped-authority.png) |
| [security-threat-boundary-model.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/06-design-quality-and-security-analysis/diagrams/security-trust-boundaries.puml) | MVP systems| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/06-design-quality-and-security-analysis/diagrams/security-trust-boundaries.svg) · ![security trust boundaries](../../Design-assets/Archived-png/Security-trust-boundaries.png) |
| [security-untrusted-content-execution.puml](Security-untrusted-content-execution.puml) | Mixed MVP / future| [SVG](Security-untrusted-content-execution.svg) · ![security untrusted content execution](Security-untrusted-content-execution.png) |
| [start-here-analysis-route.dot](Start-here-analysis-route.dot) | MVP core / cross-cutting| [SVG](Start-here-analysis-route-graphviz.svg) · ![start here analysis route graphviz](Start-here-analysis-route-graphviz.png) |
| [start-here-analysis-route.puml](Start-here-analysis-route.puml) | MVP core / cross-cutting| [SVG](Start-here-analysis-route.svg) · ![start here analysis route](Start-here-analysis-route.png) |
| [start-here-profile-publication.dot](Start-here-profile-publication.dot) | MVP core / cross-cutting| [SVG](Start-here-profile-publication-graphviz.svg) · ![start here profile publication graphviz](Start-here-profile-publication-graphviz.png) |
| [start-here-profile-publication.puml](Start-here-profile-publication.puml) | MVP core / cross-cutting| [SVG](Start-here-profile-publication.svg) · ![start here profile publication](Start-here-profile-publication.png) |
| [state-account-eligibility.puml](State-account-eligibility.puml) | MVP core / cross-cutting| [SVG](State-account-eligibility.svg) · ![state account eligibility](State-account-eligibility.png) |
| [state-application-progress.puml](State-application-progress.puml) | MVP core| [SVG](State-application-progress.svg) · ![state application progress](State-application-progress.png) |
| [state-artifact-availability.puml](State-artifact-availability.puml) | MVP core / cross-cutting| [SVG](State-artifact-availability.svg) · ![state artifact availability](State-artifact-availability.png) |
| [state-calendar-mapping.puml](State-calendar-mapping.puml) | MVP core / cross-cutting| [SVG](State-calendar-mapping.svg) · ![state calendar mapping](State-calendar-mapping.png) |
| [state-collaboration-grant.puml](State-collaboration-grant.puml) | MVP core / cross-cutting| [SVG](State-collaboration-grant.svg) · ![state collaboration grant](State-collaboration-grant.png) |
| [state-deployment-effect.puml](State-deployment-effect.puml) | Future after MVP| [SVG](State-deployment-effect.svg) · ![state deployment effect](State-deployment-effect.png) |
| [state-execution-attempt.puml](State-execution-attempt.puml) | Future after MVP| [SVG](State-execution-attempt.svg) · ![state execution attempt](State-execution-attempt.png) |
| [state-mail-send-attempt.puml](State-mail-send-attempt.puml) | Future after MVP| [SVG](State-mail-send-attempt.svg) · ![state mail send attempt](State-mail-send-attempt.png) |
| [state-operation-observation.puml](State-operation-observation.puml) | MVP core / cross-cutting| [SVG](State-operation-observation.svg) · ![state operation observation](State-operation-observation.png) |
| [state-protected-link.puml](State-protected-link.puml) | MVP core / cross-cutting| [SVG](State-protected-link.svg) · ![state protected link](State-protected-link.png) |
| [state-provider-connection.puml](State-provider-connection.puml) | Future after MVP| [SVG](State-provider-connection.svg) · ![state provider connection](State-provider-connection.png) |
| [state-pull-request-lifecycle.puml](State-pull-request-lifecycle.puml) | Future after MVP| [SVG](State-pull-request-lifecycle.svg) · ![state pull request lifecycle](State-pull-request-lifecycle.png) |
| [state-recovery-assessment.puml](State-recovery-assessment.puml) | MVP core / cross-cutting| [SVG](State-recovery-assessment.svg) · ![state recovery assessment](State-recovery-assessment.png) |
| [state-reference-aware-retention.puml](State-reference-aware-retention.puml) | MVP core / cross-cutting| [SVG](State-reference-aware-retention.svg) · ![state reference aware retention](State-reference-aware-retention.png) |
| [state-resume-draft-publication.puml](State-resume-draft-publication.puml) | MVP core / cross-cutting| [SVG](State-resume-draft-publication.svg) · ![state resume draft publication](State-resume-draft-publication.png) |
| [state-sprint-lifecycle.puml](State-sprint-lifecycle.puml) | Future after MVP| [SVG](State-sprint-lifecycle.svg) · ![state sprint lifecycle](State-sprint-lifecycle.png) |
| [state-submitted-set-completeness.puml](State-submitted-set-completeness.puml) | MVP core / cross-cutting| [SVG](State-submitted-set-completeness.svg) · ![state submitted set completeness](State-submitted-set-completeness.png) |
| [state-work-item-task.puml](State-work-item-task.puml) | MVP core / cross-cutting| [SVG](State-work-item-task.svg) · ![state work item task](State-work-item-task.png) |
| [system-context-external.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.svg) · ![logical component ownership](../../Design-assets/Archived-png/Logical-component-ownership.png) |
| [system-context-external.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) · ![mvp system boundaries](../../Design-assets/Archived-png/Mvp-system-boundaries.png) |
| [system-context-human.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.svg) · ![logical component ownership](../../Design-assets/Archived-png/Logical-component-ownership.png) |
| [system-context-human.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) · ![mvp system boundaries](../../Design-assets/Archived-png/Mvp-system-boundaries.png) |
| [system-context-information-boundaries.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.svg) · ![logical component ownership](../../Design-assets/Archived-png/Logical-component-ownership.png) |
| [system-context-information-boundaries.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) · ![mvp system boundaries](../../Design-assets/Archived-png/Mvp-system-boundaries.png) |
| [traceability-selected-matrix.puml](Traceability-selected-matrix.puml) | Historical / alternative| [SVG](Traceability-selected-matrix.svg) · ![traceability selected matrix](Traceability-selected-matrix.png) |

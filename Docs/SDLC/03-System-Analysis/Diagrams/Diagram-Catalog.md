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
| 00 / section 2 | System Analysis — iterative working route | Activity / analysis process | [PlantUML](Start-Here-Analysis-Route.puml) | [SVG](Start-Here-Analysis-Route.svg) | ![start here analysis route](Start-Here-Analysis-Route.png) |
| 00 / section 3 | Accepted core — explicit apply and separate publication | Activity / accepted successful path | [PlantUML](Start-Here-Profile-Publication.puml) | [SVG](Start-Here-Profile-Publication.svg) | ![start here profile publication](Start-Here-Profile-Publication.png) |
| 01 / section 2 | Analysis — source authority and feedback | Artifact dependency | [PlantUML](Analysis-Inputs-And-Outputs.puml) | [SVG](Analysis-Inputs-And-Outputs.svg) | ![analysis inputs and outputs](Analysis-Inputs-And-Outputs.png) |
| 01 / section 4 | Seven views — complementary questions, one coherent model | Model-view map | [PlantUML](Analysis-Seven-View-Consistency.puml) | [SVG](Analysis-Seven-View-Consistency.svg) | ![analysis seven view consistency](Analysis-Seven-View-Consistency.png) |
| 02 / section 2 | Resumefolio — human roles and authority contexts | UML actor / system context | [PlantUML](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) | ![mvp system boundaries](../../04-System-Design/Diagrams/Archived-Png/Mvp-System-Boundaries.png) |
| 02 / section 3 | Resumefolio — clients, providers and operating dependencies | Logical external context | [PlantUML](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) | ![mvp system boundaries](../../04-System-Design/Diagrams/Archived-Png/Mvp-System-Boundaries.png) |
| 02 / section 6 | Information authority — edit, publish, retrieve and preserve | Information-authority context | [PlantUML](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) | ![mvp system boundaries](../../04-System-Design/Diagrams/Archived-Png/Mvp-System-Boundaries.png) |
| 03 / section 2.1 | Professional source and independent resume | UML conceptual class view | [PlantUML](Domain-Professional-Presentation.puml) | [SVG](Domain-Professional-Presentation.svg) | ![domain professional presentation](Domain-Professional-Presentation.png) |
| 03 / section 2.1 | Evidence selection and manually authored language | UML conceptual class view | [PlantUML](Domain-Evidence-And-Language.puml) | [SVG](Domain-Evidence-And-Language.svg) | ![domain evidence and language](Domain-Evidence-And-Language.png) |
| 03 / section 2.2 | Publication, PDF availability and protected link | UML conceptual class view | [PlantUML](Domain-Publication-And-Sharing.puml) | [SVG](Domain-Publication-And-Sharing.svg) | ![domain publication and sharing](Domain-Publication-And-Sharing.png) |
| 03 / section 2.3 | Application preparation and actual submitted history | UML conceptual class view | [PlantUML](Domain-Applications-And-Communication.puml) | [SVG](Domain-Applications-And-Communication.svg) | ![domain applications and communication](Domain-Applications-And-Communication.png) |
| 03 / section 2.3 | Provider communication and explicit application links | UML conceptual class view | [PlantUML](Domain-Provider-Communication.puml) | [SVG](Domain-Provider-Communication.svg) | ![domain provider communication](Domain-Provider-Communication.png) |
| 03 / section 2.4 | Work views, items, tasks and one Sprint Backlog | UML conceptual class view | [PlantUML](Domain-Work-Management.puml) | [SVG](Domain-Work-Management.svg) | ![domain work management](Domain-Work-Management.png) |
| 03 / section 2.5 | Real Git history and repository collaboration | UML conceptual class view | [PlantUML](Domain-Git-Collaboration.puml) | [SVG](Domain-Git-Collaboration.svg) | ![domain git collaboration](Domain-Git-Collaboration.png) |
| 03 / section 2.6 | Execution provenance and separate deployment authority | UML conceptual class view | [PlantUML](Domain-Execution-And-Deployment.puml) | [SVG](Domain-Execution-And-Deployment.svg) | ![domain execution and deployment](Domain-Execution-And-Deployment.png) |
| 03 / section 2.7 | Contextual authority, file policy and recoverable data | UML conceptual class view | [PlantUML](Domain-Access-Files-And-Recovery.puml) | [SVG](Domain-Access-Files-And-Recovery.svg) | ![domain access files and recovery](Domain-Access-Files-And-Recovery.png) |

[System Analysis index](../01-System-Analysis.md) · [Four-document review](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/03-system-analysis/evidence/four-document-diagram-review-2026-11-01.md)

## Conceptual Data / ER Views

[Document 05](../01-System-Analysis.md#analysis-domain-and-information-analysis--05-data-oriented-view) uses entity rectangles and crow-foot ends. **P** counts instantiate working proposals; **A** labels an established scope meaning. Plain associations leave counts unspecified. No physical schema or acceptance follows from this notation.

| Data view | Source | SVG | PNG |
| --- | --- | --- | --- |
| Data — source information and independent tailoring | [PlantUML](Data-Profile-And-Tailoring.puml) | [SVG](Data-Profile-And-Tailoring.svg) | ![data profile and tailoring](Data-Profile-And-Tailoring.png) |
| Data — evidence disclosure and language context | [PlantUML](Data-Evidence-Language-And-Selection.puml) | [SVG](Data-Evidence-Language-And-Selection.svg) | ![data evidence language and selection](Data-Evidence-Language-And-Selection.png) |
| Data — publication identity, PDF provenance and access | [PlantUML](Data-Publication-Pdf-And-Sharing.puml) | [SVG](Data-Publication-Pdf-And-Sharing.svg) | ![data publication pdf and sharing](Data-Publication-Pdf-And-Sharing.png) |
| Data — application preparation and actual submission records | [PlantUML](Data-Applications-And-Actual-Material.puml) | [SVG](Data-Applications-And-Actual-Material.svg) | ![data applications and actual material](Data-Applications-And-Actual-Material.png) |
| Data — provider identities and local associations | [PlantUML](Data-Provider-And-Calendar-Context.puml) | [SVG](Data-Provider-And-Calendar-Context.svg) | ![data provider and calendar context](Data-Provider-And-Calendar-Context.png) |
| Data — work identities and one coherent Sprint Backlog | [PlantUML](Data-Work-And-Sprint-Planning.puml) | [SVG](Data-Work-And-Sprint-Planning.svg) | ![data work and sprint planning](Data-Work-And-Sprint-Planning.png) |
| Data — repository identity and evaluated Git context | [PlantUML](Data-Git-Revisions-And-Collaboration.puml) | [SVG](Data-Git-Revisions-And-Collaboration.svg) | ![data git revisions and collaboration](Data-Git-Revisions-And-Collaboration.png) |
| Data — run provenance, attempts and deployment approval | [PlantUML](Data-Execution-Provenance-And-Targets.puml) | [SVG](Data-Execution-Provenance-And-Targets.svg) | ![data execution provenance and targets](Data-Execution-Provenance-And-Targets.png) |
| Data — contextual access, effective policy and recovery coverage | [PlantUML](Data-Authority-Policy-And-Recovery.puml) | [SVG](Data-Authority-Policy-And-Recovery.svg) | ![data authority policy and recovery](Data-Authority-Policy-And-Recovery.png) |

## Scenario / Logical Sequence Views

[Document 06](../01-System-Analysis.md#analysis-behavioral-and-scenario-analysis--06-scenario-based-view) explains guards, optional actions, alternative results and source status. These PlantUML lifelines are domain collaborators/context groupings, not selected runtime services. Diagram numbering is local; original UC/ST/SCN identifiers remain authoritative.

| Local model | Source | SVG | PNG |
| --- | --- | --- | --- |
| SB-M01 — Explicit source application and separate publication | [PlantUML](Scenario-Profile-Apply-Publication.puml) | [SVG](Scenario-Profile-Apply-Publication.svg) | ![scenario profile apply publication](Scenario-Profile-Apply-Publication.png) |
| SB-M02 — PDF settings without implicit link changes | [PlantUML](Scenario-Pdf-Settings.puml) | [SVG](Scenario-Pdf-Settings.svg) | ![scenario pdf settings](Scenario-Pdf-Settings.png) |
| SB-M03 — Independent link disable and fresh access | [PlantUML](Scenario-Disable-Sharing-Link.puml) | [SVG](Scenario-Disable-Sharing-Link.svg) | ![scenario disable sharing link](Scenario-Disable-Sharing-Link.png) |
| SB-M04 — Selected protected retrieval and unavailable variants | [PlantUML](Scenario-Protected-Retrieval.puml) | [SVG](Scenario-Protected-Retrieval.svg) | ![scenario protected retrieval](Scenario-Protected-Retrieval.png) |
| SB-M05 — Manual preparation and separate progress change | [PlantUML](Scenario-Application-Preparation.puml) | [SVG](Scenario-Application-Preparation.svg) | ![scenario application preparation](Scenario-Application-Preparation.png) |
| SB-M06 — Preserve actual material, not current live substitutes | [PlantUML](Scenario-Actual-Submission-Capture.puml) | [SVG](Scenario-Actual-Submission-Capture.svg) | ![scenario actual submission capture](Scenario-Actual-Submission-Capture.png) |
| SB-M07 — Read or deliberately send with truthful provider outcomes | [PlantUML](Scenario-Gmail-Read-Send-Outcomes.puml) | [SVG](Scenario-Gmail-Read-Send-Outcomes.svg) | ![scenario gmail read send outcomes](Scenario-Gmail-Read-Send-Outcomes.png) |
| SB-M08 — Local calendar action versus selected provider synchronization | [PlantUML](Scenario-Calendar-Local-Sync.puml) | [SVG](Scenario-Calendar-Local-Sync.svg) | ![scenario calendar local sync](Scenario-Calendar-Local-Sync.png) |
| SB-M09 — Independent refinement, Sprint planning and Sprint-end actions | [PlantUML](Scenario-Work-Refine-Plan-End.puml) | [SVG](Scenario-Work-Refine-Plan-End.svg) | ![scenario work refine plan end](Scenario-Work-Refine-Plan-End.png) |
| SB-M10 — Invitation acceptance and resource-scoped changed access | [PlantUML](Scenario-Collaboration-And-Changed-Grant.puml) | [SVG](Scenario-Collaboration-And-Changed-Grant.svg) | ![scenario collaboration and changed grant](Scenario-Collaboration-And-Changed-Grant.png) |
| SB-M11 — Real Git read transfer versus authorized ref update | [PlantUML](Scenario-Git-Transfer.puml) | [SVG](Scenario-Git-Transfer.svg) | ![scenario git transfer](Scenario-Git-Transfer.png) |
| SB-M12 — Current source/target and revision-related review | [PlantUML](Scenario-Pull-Request-Review-Merge.puml) | [SVG](Scenario-Pull-Request-Review-Merge.svg) | ![scenario pull request review merge](Scenario-Pull-Request-Review-Merge.png) |
| SB-M13 — Gated run admission and attributable actual attempts | [PlantUML](Scenario-Workflow-Admission-Attempt.puml) | [SVG](Scenario-Workflow-Admission-Attempt.svg) | ![scenario workflow admission attempt](Scenario-Workflow-Admission-Attempt.png) |
| SB-M14 — Target-authorized deployment is a separate goal | [PlantUML](Scenario-Separate-Deployment.puml) | [SVG](Scenario-Separate-Deployment.svg) | ![scenario separate deployment](Scenario-Separate-Deployment.png) |
| SB-M15 — Effective policy, file admission and restricted evidence | [PlantUML](Scenario-Policy-Admission-Evidence.puml) | [SVG](Scenario-Policy-Admission-Evidence.svg) | ![scenario policy admission evidence](Scenario-Policy-Admission-Evidence.png) |
| SB-M16 — Conditional isolated restoration and safe reconciliation | [PlantUML](Scenario-Isolated-Recovery-Assessment.puml) | [SVG](Scenario-Isolated-Recovery-Assessment.svg) | ![scenario isolated recovery assessment](Scenario-Isolated-Recovery-Assessment.png) |

## State-based view — 07

18 bounded statecharts; full transition contracts and authority labels are maintained in [the state view](../01-System-Analysis.md#analysis-behavioral-and-scenario-analysis--07-state-based-view). Existing proposals remain proposals.

| Model | Editable source | SVG | PNG |
| --- | --- | --- | --- |
| SM-M01 — Independent draft and live presentation context | [state-resume-draft-publication.puml](State-Resume-Draft-Publication.puml) | [SVG](State-Resume-Draft-Publication.svg) | ![state resume draft publication](State-Resume-Draft-Publication.png) |
| SM-M02 — Proposed account access eligibility | [state-account-eligibility.puml](State-Account-Eligibility.puml) | [SVG](State-Account-Eligibility.svg) | ![state account eligibility](State-Account-Eligibility.png) |
| SM-M03 — Invitation and scoped grant instance | [state-collaboration-grant.puml](State-Collaboration-Grant.puml) | [SVG](State-Collaboration-Grant.svg) | ![state collaboration grant](State-Collaboration-Grant.png) |
| SM-M04 — Enabled link is separate from current retrieval eligibility | [state-protected-link.puml](State-Protected-Link.puml) | [SVG](State-Protected-Link.svg) | ![state protected link](State-Protected-Link.png) |
| SM-M05 — Candidate admission and confirmed usable artifact | [state-artifact-availability.puml](State-Artifact-Availability.puml) | [SVG](State-Artifact-Availability.svg) | ![state artifact availability](State-Artifact-Availability.png) |
| SM-M06 — Proposed manual application progress | [state-application-progress.puml](State-Application-Progress.puml) | [SVG](State-Application-Progress.svg) | ![state application progress](State-Application-Progress.png) |
| SM-M07 — Actual submitted-set completeness | [state-submitted-set-completeness.puml](State-Submitted-Set-Completeness.puml) | [SVG](State-Submitted-Set-Completeness.svg) | ![state submitted set completeness](State-Submitted-Set-Completeness.png) |
| SM-M08 — Usable provider capability versus disconnected data | [state-provider-connection.puml](State-Provider-Connection.puml) | [SVG](State-Provider-Connection.svg) | ![state provider connection](State-Provider-Connection.png) |
| SM-M09 — Provider acceptance and unknown mail outcome | [state-mail-send-attempt.puml](State-Mail-Send-Attempt.puml) | [SVG](State-Mail-Send-Attempt.svg) | ![state mail send attempt](State-Mail-Send-Attempt.png) |
| SM-M10 — Local/provider mapping and freshness | [state-calendar-mapping.puml](State-Calendar-Mapping.puml) | [SVG](State-Calendar-Mapping.svg) | ![state calendar mapping](State-Calendar-Mapping.png) |
| SM-M11 — Work status with subject-specific completion guards | [state-work-item-task.puml](State-Work-Item-Task.puml) | [SVG](State-Work-Item-Task.svg) | ![state work item task](State-Work-Item-Task.png) |
| SM-M12 — Sprint period and recorded actual outcome | [state-sprint-lifecycle.puml](State-Sprint-Lifecycle.puml) | [SVG](State-Sprint-Lifecycle.svg) | ![state sprint lifecycle](State-Sprint-Lifecycle.png) |
| SM-M13 — Request lifecycle with revision-specific eligibility | [state-pull-request-lifecycle.puml](State-Pull-Request-Lifecycle.puml) | [SVG](State-Pull-Request-Lifecycle.svg) | ![state pull request lifecycle](State-Pull-Request-Lifecycle.png) |
| SM-M14 — Actual attempt, cancellation request and runner uncertainty | [state-execution-attempt.puml](State-Execution-Attempt.puml) | [SVG](State-Execution-Attempt.svg) | ![state execution attempt](State-Execution-Attempt.png) |
| SM-M15 — Separate target authority and actual deployment effect | [state-deployment-effect.puml](State-Deployment-Effect.puml) | [SVG](State-Deployment-Effect.svg) | ![state deployment effect](State-Deployment-Effect.png) |
| SM-M16 — User-managed record retention and actual reclamation | [state-reference-aware-retention.puml](State-Reference-Aware-Retention.puml) | [SVG](State-Reference-Aware-Retention.svg) | ![state reference aware retention](State-Reference-Aware-Retention.png) |
| SM-M17 — Gated isolated restoration and demonstrated usable state | [state-recovery-assessment.puml](State-Recovery-Assessment.puml) | [SVG](State-Recovery-Assessment.svg) | ![state recovery assessment](State-Recovery-Assessment.png) |
| SM-M18 — Observed operation result is separate from subject state | [state-operation-observation.puml](State-Operation-Observation.puml) | [SVG](State-Operation-Observation.svg) | ![state operation observation](State-Operation-Observation.png) |

## Control-flow-based view — 08

16 source-aligned domain activities plus one reusable result-classification subactivity. Full step meanings and proposal boundaries are in [the control-flow view](../01-System-Analysis.md#analysis-functional-and-process-analysis--08-control-flow-based-view). Arrows show logical control, not atomic transactions or product execution proof.

| Model | Editable source | SVG | PNG |
| --- | --- | --- | --- |
| CF-M01 — Selected resume update and separate publication | [activity-profile-apply-publication.puml](Activity-Profile-Apply-Publication.puml) | [SVG](Activity-Profile-Apply-Publication.svg) | ![activity profile apply publication](Activity-Profile-Apply-Publication.png) |
| CF-M02 — Download settings without link side effects | [activity-pdf-settings.puml](Activity-Pdf-Settings.puml) | [SVG](Activity-Pdf-Settings.svg) | ![activity pdf settings](Activity-Pdf-Settings.png) |
| CF-M03 — Independent link disablement and fresh request | [activity-disable-sharing-link.puml](Activity-Disable-Sharing-Link.puml) | [SVG](Activity-Disable-Sharing-Link.svg) | ![activity disable sharing link](Activity-Disable-Sharing-Link.png) |
| CF-M04 — Controlled page and artifact retrieval | [activity-protected-retrieval.puml](Activity-Protected-Retrieval.puml) | [SVG](Activity-Protected-Retrieval.svg) | ![activity protected retrieval](Activity-Protected-Retrieval.png) |
| CF-M05 — Manual application preparation or progress recording | [activity-application-preparation.puml](Activity-Application-Preparation.puml) | [SVG](Activity-Application-Preparation.svg) | ![activity application preparation](Activity-Application-Preparation.png) |
| CF-M06 — Capture actual submitted materials | [activity-actual-submission-capture.puml](Activity-Actual-Submission-Capture.puml) | [SVG](Activity-Actual-Submission-Capture.svg) | ![activity actual submission capture](Activity-Actual-Submission-Capture.png) |
| CF-M07 — Read correspondence or deliberately send | [activity-gmail-read-send-outcomes.puml](Activity-Gmail-Read-Send-Outcomes.puml) | [SVG](Activity-Gmail-Read-Send-Outcomes.svg) | ![activity gmail read send outcomes](Activity-Gmail-Read-Send-Outcomes.png) |
| CF-M08 — Local activity versus selected calendar synchronization | [activity-calendar-local-sync.puml](Activity-Calendar-Local-Sync.puml) | [SVG](Activity-Calendar-Local-Sync.svg) | ![activity calendar local sync](Activity-Calendar-Local-Sync.png) |
| CF-M09 — Refinement, Sprint planning and Sprint completion | [activity-work-refine-plan-end.puml](Activity-Work-Refine-Plan-End.puml) | [SVG](Activity-Work-Refine-Plan-End.svg) | ![activity work refine plan end](Activity-Work-Refine-Plan-End.png) |
| CF-M10 — Invitation acceptance and subsequent scoped access | [activity-collaboration-and-changed-grant.puml](Activity-Collaboration-And-Changed-Grant.puml) | [SVG](Activity-Collaboration-And-Changed-Grant.svg) | ![activity collaboration and changed grant](Activity-Collaboration-And-Changed-Grant.png) |
| CF-M11 — Real Git read transfer or ref update | [activity-git-transfer.puml](Activity-Git-Transfer.puml) | [SVG](Activity-Git-Transfer.svg) | ![activity git transfer](Activity-Git-Transfer.png) |
| CF-M12 — Request, review or eligible integration | [activity-pull-request-review-merge.puml](Activity-Pull-Request-Review-Merge.puml) | [SVG](Activity-Pull-Request-Review-Merge.svg) | ![activity pull request review merge](Activity-Pull-Request-Review-Merge.png) |
| CF-M13 — Gated execution attempt and cancellation race | [activity-workflow-admission-attempt.puml](Activity-Workflow-Admission-Attempt.puml) | [SVG](Activity-Workflow-Admission-Attempt.svg) | ![activity workflow admission attempt](Activity-Workflow-Admission-Attempt.png) |
| CF-M14 — Separate target-authorized deployment | [activity-separate-deployment.puml](Activity-Separate-Deployment.puml) | [SVG](Activity-Separate-Deployment.svg) | ![activity separate deployment](Activity-Separate-Deployment.png) |
| CF-M15 — Effective policy, file admission or restricted evidence | [activity-policy-admission-evidence.puml](Activity-Policy-Admission-Evidence.puml) | [SVG](Activity-Policy-Admission-Evidence.svg) | ![activity policy admission evidence](Activity-Policy-Admission-Evidence.png) |
| CF-M16 — Conditional isolated restore and usability assessment | [activity-isolated-recovery-assessment.puml](Activity-Isolated-Recovery-Assessment.puml) | [SVG](Activity-Isolated-Recovery-Assessment.svg) | ![activity isolated recovery assessment](Activity-Isolated-Recovery-Assessment.png) |
| CF-M17 — Reusable actual operation-result classification | [activity-operation-result-classification.puml](Activity-Operation-Result-Classification.puml) | [SVG](Activity-Operation-Result-Classification.svg) | ![activity operation result classification](Activity-Operation-Result-Classification.png) |

## Rule-based view — 09

Eight focused decision trees accompany 18 finite-domain decision tables in [the rule view](../01-System-Analysis.md#analysis-business-rules-and-operation-contracts--09-rule-based-view). These are decision alternatives, not execution order. Full conditions, results and authority remain in the tables.

| Decision | Editable source | SVG | PNG |
| --- | --- | --- | --- |
| RB-D01 — Resource-scoped operation eligibility | [rule-rb-d01-decision.puml](Rule-Rb-D01-Decision.puml) | [SVG](Rule-Rb-D01-Decision.svg) | ![rule rb d01 decision](Rule-Rb-D01-Decision.png) |
| RB-D04 — Protected selected representation eligibility | [rule-rb-d04-decision.puml](Rule-Rb-D04-Decision.puml) | [SVG](Rule-Rb-D04-Decision.svg) | ![rule rb d04 decision](Rule-Rb-D04-Decision.png) |
| RB-D06 — Actual submitted-set completeness | [rule-rb-d06-decision.puml](Rule-Rb-D06-Decision.puml) | [SVG](Rule-Rb-D06-Decision.svg) | ![rule rb d06 decision](Rule-Rb-D06-Decision.png) |
| RB-D07 — Reviewed provider send eligibility | [rule-rb-d07-decision.puml](Rule-Rb-D07-Decision.puml) | [SVG](Rule-Rb-D07-Decision.svg) | ![rule rb d07 decision](Rule-Rb-D07-Decision.png) |
| RB-D11 — Current revision-specific merge eligibility | [rule-rb-d11-decision.puml](Rule-Rb-D11-Decision.puml) | [SVG](Rule-Rb-D11-Decision.svg) | ![rule rb d11 decision](Rule-Rb-D11-Decision.png) |
| RB-D12 — Workflow execution admission | [rule-rb-d12-decision.puml](Rule-Rb-D12-Decision.puml) | [SVG](Rule-Rb-D12-Decision.svg) | ![rule rb d12 decision](Rule-Rb-D12-Decision.png) |
| RB-D15 — Reference-aware physical reclamation eligibility | [rule-rb-d15-decision.puml](Rule-Rb-D15-Decision.puml) | [SVG](Rule-Rb-D15-Decision.svg) | ![rule rb d15 decision](Rule-Rb-D15-Decision.png) |
| RB-D16 — Scoped usable recovery assessment | [rule-rb-d16-decision.puml](Rule-Rb-D16-Decision.puml) | [SVG](Rule-Rb-D16-Decision.svg) | ![rule rb d16 decision](Rule-Rb-D16-Decision.png) |

## Domain constraints and operation contracts — 10

Eight before/confirmed-after/frame relations illustrate selected contracts from [the contract view](../01-System-Analysis.md#analysis-business-rules-and-operation-contracts--10-domain-constraints-and-operation-contracts). After-state applies only to actual confirmed permitted success; frame does not freeze independent concurrent actions or guarantee failure rollback. Full obligations/policy status remain in the text.

| Contract | Editable source | SVG | PNG |
| --- | --- | --- | --- |
| DC-O02 — Apply selected source changes to one draft | [contract-dc-o02-boundary.puml](Contract-Dc-O02-Boundary.puml) | [SVG](Contract-Dc-O02-Boundary.svg) | ![contract dc o02 boundary](Contract-Dc-O02-Boundary.png) |
| DC-O03 — Publish separately confirmed intended presentation | [contract-dc-o03-boundary.puml](Contract-Dc-O03-Boundary.puml) | [SVG](Contract-Dc-O03-Boundary.svg) | ![contract dc o03 boundary](Contract-Dc-O03-Boundary.png) |
| DC-O05 — Disable a specific protected link | [contract-dc-o05-boundary.puml](Contract-Dc-O05-Boundary.puml) | [SVG](Contract-Dc-O05-Boundary.svg) | ![contract dc o05 boundary](Contract-Dc-O05-Boundary.png) |
| DC-O12 — Submit a reviewed mail send/reply attempt | [contract-dc-o12-boundary.puml](Contract-Dc-O12-Boundary.puml) | [SVG](Contract-Dc-O12-Boundary.svg) | ![contract dc o12 boundary](Contract-Dc-O12-Boundary.png) |
| DC-O14 — Unlink a local provider mapping | [contract-dc-o14-boundary.puml](Contract-Dc-O14-Boundary.puml) | [SVG](Contract-Dc-O14-Boundary.svg) | ![contract dc o14 boundary](Contract-Dc-O14-Boundary.png) |
| DC-O26 — Merge only current eligible evaluated revisions | [contract-dc-o26-boundary.puml](Contract-Dc-O26-Boundary.puml) | [SVG](Contract-Dc-O26-Boundary.svg) | ![contract dc o26 boundary](Contract-Dc-O26-Boundary.png) |
| DC-O30 — Attempt a separately target-authorized deployment | [contract-dc-o30-boundary.puml](Contract-Dc-O30-Boundary.puml) | [SVG](Contract-Dc-O30-Boundary.svg) | ![contract dc o30 boundary](Contract-Dc-O30-Boundary.png) |
| DC-O37 — Perform and assess an authorized isolated recovery drill | [contract-dc-o37-boundary.puml](Contract-Dc-O37-Boundary.puml) | [SVG](Contract-Dc-O37-Boundary.svg) | ![contract dc o37 boundary](Contract-Dc-O37-Boundary.png) |

## Model consistency, traceability and review — 11

Three evidence/review relationship views accompany [SA-RV02](../01-System-Analysis.md#analysis-review-and-design-handoff--11-model-consistency-traceability-and-review). A citation is not semantic criterion sufficiency, and a rendered diagram is not a product test or owner acceptance.

| View | Editable source | SVG | PNG |
| --- | --- | --- | --- |
| SA-RV02 — association is not verification | [review-trace-evidence-levels.puml](Review-Trace-Evidence-Levels.puml) | [SVG](Review-Trace-Evidence-Levels.svg) | ![review trace evidence levels](Review-Trace-Evidence-Levels.png) |
| SA-RV02 — current analysis position | [review-current-position.puml](Review-Current-Position.puml) | [SVG](Review-Current-Position.svg) | ![review current position](Review-Current-Position.png) |
| SA-RV02 — review and change-impact route | [review-change-impact-route.puml](Review-Change-Impact-Route.puml) | [SVG](Review-Change-Impact-Route.svg) | ![review change impact route](Review-Change-Impact-Route.png) |

## Interfaces and external interactions — 12

Eight focused logical exchange views accompany [file 12](../01-System-Analysis.md#analysis-interfaces-security-and-quality-analysis--12-interfaces-and-external-interactions). Arrows identify direction; conditional access/facilities are not claims of installed components, selected transports, completed operations or automatically inherited authority.

| Family | Editable source | SVG | PNG |
| --- | --- | --- | --- |
| IF-01 — Private human interface | [interface-private-human-context.puml](Interface-Private-Human-Context.puml) | [SVG](Interface-Private-Human-Context.svg) | ![interface private human context](Interface-Private-Human-Context.png) |
| IF-02 — Protected employer representation | [interface-employer-protected-representation.puml](Interface-Employer-Protected-Representation.puml) | [SVG](Interface-Employer-Protected-Representation.svg) | ![interface employer protected representation](Interface-Employer-Protected-Representation.png) |
| IF-03 — Authorized file/PDF exchange | [interface-file-candidate-result.puml](Interface-File-Candidate-Result.puml) | [SVG](Interface-File-Candidate-Result.svg) | ![interface file candidate result](Interface-File-Candidate-Result.png) |
| IF-04 — Gmail provider operations | [interface-gmail-reviewed-effects.puml](Interface-Gmail-Reviewed-Effects.puml) | [SVG](Interface-Gmail-Reviewed-Effects.svg) | ![interface gmail reviewed effects](Interface-Gmail-Reviewed-Effects.png) |
| IF-05 — Calendar provider and local mapping | [interface-calendar-local-provider.puml](Interface-Calendar-Local-Provider.puml) | [SVG](Interface-Calendar-Local-Provider.svg) | ![interface calendar local provider](Interface-Calendar-Local-Provider.png) |
| IF-06 — Real Git-client boundary | [interface-real-git-client.puml](Interface-Real-Git-Client.puml) | [SVG](Interface-Real-Git-Client.svg) | ![interface real git client](Interface-Real-Git-Client.png) |
| IF-07 — Conditional execution and separate deployment target | [interface-execution-separate-target.puml](Interface-Execution-Separate-Target.puml) | [SVG](Interface-Execution-Separate-Target.svg) | ![interface execution separate target](Interface-Execution-Separate-Target.png) |
| IF-08 — Operational configuration, delivery and recovery | [interface-operating-delivery-recovery.puml](Interface-Operating-Delivery-Recovery.puml) | [SVG](Interface-Operating-Delivery-Recovery.svg) | ![interface operating delivery recovery](Interface-Operating-Delivery-Recovery.png) |

## Security, quality and operational analysis — 13

Six focused analysis/evidence views accompany [file 13](../01-System-Analysis.md#analysis-interfaces-security-and-quality-analysis--13-security-quality-and-operational-analysis). They do not select architecture, certify controls, prove capacity or authorize host/provider/execution/restore operations.

| View | Editable source | SVG | PNG |
| --- | --- | --- | --- |
| SQ — scoped authority across entry paths | [security-scoped-authority.puml](Security-Scoped-Authority.puml) | [SVG](Security-Scoped-Authority.svg) | ![security scoped authority](Security-Scoped-Authority.png) |
| SQ — data trust and conditional execution | [security-untrusted-content-execution.puml](Security-Untrusted-Content-Execution.puml) | [SVG](Security-Untrusted-Content-Execution.svg) | ![security untrusted content execution](Security-Untrusted-Content-Execution.png) |
| SQ — measurable quality scenario contract | [quality-scenario-measurement.puml](Quality-Scenario-Measurement.puml) | [SVG](Quality-Scenario-Measurement.svg) | ![quality scenario measurement](Quality-Scenario-Measurement.png) |
| SQ — recovery evidence and current authority | [recovery-scoped-usable-state.puml](Recovery-Scoped-Usable-State.puml) | [SVG](Recovery-Scoped-Usable-State.svg) | ![recovery scoped usable state](Recovery-Scoped-Usable-State.png) |
| SQ — operation effect versus observation | [operations-effect-evidence.puml](Operations-Effect-Evidence.puml) | [SVG](Operations-Effect-Evidence.svg) | ![operations effect evidence](Operations-Effect-Evidence.png) |
| SQ — mixed workload and observed host limits | [operations-resource-envelope.puml](Operations-Resource-Envelope.puml) | [SVG](Operations-Resource-Envelope.svg) | ![operations resource envelope](Operations-Resource-Envelope.png) |

## Feasibility, dependencies and design handoff — 14

Five qualified evidence/gate/handoff/design-question/delivery views accompany [file 14](../01-System-Analysis.md#analysis-review-and-design-handoff--14-feasibility-dependencies-and-design-handoff). They do not select architecture, certify feasibility, approve a forecast, change parent gates or authorize product work.

| View | Editable source | SVG | PNG |
| --- | --- | --- | --- |
| HD — evidence and dependent commitments | [handoff-evidence-dependent-commitment.puml](Handoff-Evidence-Dependent-Commitment.puml) | [SVG](Handoff-Evidence-Dependent-Commitment.svg) | ![handoff evidence dependent commitment](Handoff-Evidence-Dependent-Commitment.png) |
| HD — existing gate relationships | [handoff-existing-review-gates.puml](Handoff-Existing-Review-Gates.puml) | [SVG](Handoff-Existing-Review-Gates.svg) | ![handoff existing review gates](Handoff-Existing-Review-Gates.png) |
| HD — conditional handoff position | [handoff-package-position.puml](Handoff-Package-Position.puml) | [SVG](Handoff-Package-Position.svg) | ![handoff package position](Handoff-Package-Position.png) |
| HD — design evaluation record | [handoff-design-question-record.puml](Handoff-Design-Question-Record.puml) | [SVG](Handoff-Design-Question-Record.svg) | ![handoff design question record](Handoff-Design-Question-Record.png) |
| HD — delivery reconciliation before coding | [handoff-delivery-reconciliation.puml](Handoff-Delivery-Reconciliation.puml) | [SVG](Handoff-Delivery-Reconciliation.svg) | ![handoff delivery reconciliation](Handoff-Delivery-Reconciliation.png) |

## Current Processes and Bottleneck Analysis — File 15

Evidence classification and investigation logic; not observed daily-business workflows.

| View | Source | SVG | PNG |
| --- | --- | --- | --- |
| CP — current evidence versus target and hypothesis | [PlantUML](Process-Evidence-Classes.puml) | [SVG](Process-Evidence-Classes.svg) | ![process evidence classes](Process-Evidence-Classes.png) |
| CP — documented artifact relationships | [PlantUML](Process-Documented-Artifact-Trail.puml) | [SVG](Process-Documented-Artifact-Trail.svg) | ![process documented artifact trail](Process-Documented-Artifact-Trail.png) |
| CP — bounded current-process evidence need | [PlantUML](Process-Current-Workflow-Questions.puml) | [SVG](Process-Current-Workflow-Questions.svg) | ![process current workflow questions](Process-Current-Workflow-Questions.png) |
| CP — hypothesis support or rejection | [PlantUML](Process-Hypothesis-Validation.puml) | [SVG](Process-Hypothesis-Validation.svg) | ![process hypothesis validation](Process-Hypothesis-Validation.png) |
| CP — intended improvement versus demonstrated result | [PlantUML](Process-Improvement-Evidence.puml) | [SVG](Process-Improvement-Evidence.svg) | ![process improvement evidence](Process-Improvement-Evidence.png) |

## Diagram notation alignment — November 1, 2026

See the [file-by-file report](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/03-system-analysis/evidence/notation-alignment-review-2026-11-01.md). New diagrams complement existing models. BPMN uses native XML; other new diagrams use PlantUML.

| Diagram | Notation | Editable | SVG | PNG |
| --- | --- | --- | --- | --- |
| Document navigation — 00 through 15 | Document dependency graph | [Source](Documentation-Navigation.puml) | [SVG](Documentation-Navigation.svg) | ![documentation navigation](Documentation-Navigation.png) |
| Scope and stakeholder map | Stakeholder and scope diagram | [Source](Scope-Stakeholder-Map.puml) | [SVG](Scope-Stakeholder-Map.svg) | ![scope stakeholder map](Scope-Stakeholder-Map.png) |
| C4 Level 1 — target product context | C4 Level 1 | [Source](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/drivers-c4-system-context.puml) | [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/drivers-c4-system-context.svg) | ![drivers c4 system context](../../04-System-Design/Diagrams/Archived-Png/Drivers-C4-System-Context.png) |
| C4 Level 2 — historical demo evidence only | C4 Level 2, bounded historical inventory | [Source](C4-Observed-Demo-Containers.puml) | [SVG](C4-Observed-Demo-Containers.svg) | ![c4 observed demo containers](C4-Observed-Demo-Containers.png) |
| UML packages — logical domain groupings | UML package | [Source](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) | ![mvp system boundaries](../../04-System-Design/Diagrams/Archived-Png/Mvp-System-Boundaries.png) |
| UML class detail — explicit proposed relationship ends | UML class with multiplicities | [Source](Domain-Proposed-Multiplicity.puml) | [SVG](Domain-Proposed-Multiplicity.svg) | ![domain proposed multiplicity](Domain-Proposed-Multiplicity.png) |
| DFD context — external information boundary | DFD context | [Source](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) | ![mvp system boundaries](../../04-System-Design/Diagrams/Archived-Png/Mvp-System-Boundaries.png) |
| DFD Level 1 — content | DFD Level 1 | [Source](Function-Dfd-Level1-Content.puml) | [SVG](Function-Dfd-Level1-Content.svg) | ![function dfd level1 content](Function-Dfd-Level1-Content.png) |
| DFD Level 1 — work-operations | DFD Level 1 | [Source](Function-Store-Information.puml) | [SVG](Function-Store-Information.svg) | ![function store information](Function-Store-Information.png) |
| Functional decomposition — responsibilities, not services | Functional decomposition tree | [Source](Function-Decomposition.puml) | [SVG](Function-Decomposition.svg) | ![function decomposition](Function-Decomposition.png) |
| DFD — logical information ownership | DFD logical stores | [Source](Function-Store-Information.puml) | [SVG](Function-Store-Information.svg) | ![function store information](Function-Store-Information.png) |
| DFD Level 2 — F02 selected apply and publication | DFD Level 2 | [Source](Function-Profile-Level2.puml) | [SVG](Function-Profile-Level2.svg) | ![function profile level2](Function-Profile-Level2.png) |
| DC-O02 — UML object snapshots and frame condition | UML object snapshots | [Source](Contract-Apply-Object-Snapshots.puml) | [SVG](Contract-Apply-Object-Snapshots.svg) | ![contract apply object snapshots](Contract-Apply-Object-Snapshots.png) |
| Selected traceability matrix — associations, not test results | Traceability matrix graphic | [Source](Traceability-Selected-Matrix.puml) | [SVG](Traceability-Selected-Matrix.svg) | ![traceability selected matrix](Traceability-Selected-Matrix.png) |
| UML component view — interface responsibilities | UML component-style logical interface view | [Source](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) | ![mvp system boundaries](../../04-System-Design/Diagrams/Archived-Png/Mvp-System-Boundaries.png) |
| Request/response boundary — protocol-neutral contract | UML sequence | [Source](Interface-Request-Response-Contract.puml) | [SVG](Interface-Request-Response-Contract.svg) | ![interface request response contract](Interface-Request-Response-Contract.png) |
| Trust-boundary DFD — logical protections to establish | Security DFD | [Source](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/06-design-quality-and-security-analysis/diagrams/security-trust-boundaries.puml) | [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/06-design-quality-and-security-analysis/diagrams/security-trust-boundaries.svg) | ![security trust boundaries](../../04-System-Design/Diagrams/Archived-Png/Security-Trust-Boundaries.png) |
| UML deployment — historical demo observation | UML deployment | [Source](Deployment-Observed-Host.puml) | [SVG](Deployment-Observed-Host.svg) | ![deployment observed host](Deployment-Observed-Host.png) |
| Dependency network — conditions, not scheduled dates | Dependency network | [Source](Handoff-Dependency-Network.puml) | [SVG](Handoff-Dependency-Network.svg) | ![handoff dependency network](Handoff-Dependency-Network.png) |
| Resumefolio — analysis ecosystem | High-level system overview | [Source](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) | ![mvp system boundaries](../../04-System-Design/Diagrams/Archived-Png/Mvp-System-Boundaries.png) |
| As-Is — evidence-bounded current-process view | BPMN 2.0 | [Source](Process-Bpmn-As-Is-Boundary.bpmn) | [SVG](Process-Bpmn-As-Is-Boundary.svg) | ![process bpmn as is boundary](Process-Bpmn-As-Is-Boundary.png) |
| To-Be — selected apply and separate publication | BPMN 2.0 | [Source](Process-Bpmn-Target-Publication.bpmn) | [SVG](Process-Bpmn-Target-Publication.svg) | ![process bpmn target publication](Process-Bpmn-Target-Publication.png) |

## File 10 — constraint and outcome clarification

The eight existing contract-boundary views now use vertical layouts. The existing object snapshot remains.

| View | Source | SVG | PNG |
| --- | --- | --- | --- |
| Constraint application — common rules and accepted core | [PlantUML](Contract-Constraint-Application.puml) | [SVG](Contract-Constraint-Application.svg) | ![contract constraint application](Contract-Constraint-Application.png) |
| Contract outcomes — evidence required for a claim | [PlantUML](Contract-Outcome-Interpretation.puml) | [SVG](Contract-Outcome-Interpretation.svg) | ![contract outcome interpretation](Contract-Outcome-Interpretation.png) |

## File 13 — threats, infrastructure and conditional recovery

These views distinguish candidate controls, dated inventory and conditional future procedures.

| View | Editable | SVG | PNG |
| --- | --- | --- | --- |
| Trust boundaries and candidate threats | [PlantUML](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/06-design-quality-and-security-analysis/diagrams/security-trust-boundaries.puml) | [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/06-design-quality-and-security-analysis/diagrams/security-trust-boundaries.svg) | ![security trust boundaries](../../04-System-Design/Diagrams/Archived-Png/Security-Trust-Boundaries.png) |
| Infrastructure topology — observed demo and explicit gaps | [PlantUML](Security-Infrastructure-Topology.puml) | [SVG](Security-Infrastructure-Topology.svg) | ![security infrastructure topology](Security-Infrastructure-Topology.png) |
| HA / failover — conditional decision and verification sequence | [PlantUML](Security-Ha-Failover-Sequence.puml) | [SVG](Security-Ha-Failover-Sequence.svg) | ![security ha failover sequence](Security-Ha-Failover-Sequence.png) |
| Disaster recovery — restore, validate and controlled resumption | [PlantUML](Security-Disaster-Recovery-Sequence.puml) | [SVG](Security-Disaster-Recovery-Sequence.svg) | ![security disaster recovery sequence](Security-Disaster-Recovery-Sequence.png) |

## Whole-product ecosystem and connected platforms

The two coordinated maps cover logical product areas and all eight existing IF families. Status labels distinguish target exchanges from dated demo observations and unconfigured facilities.

| View | Source | SVG | PNG |
| --- | --- | --- | --- |
| Internal ecosystem and information relationships | [PlantUML](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) | ![mvp system boundaries](../../04-System-Design/Diagrams/Archived-Png/Mvp-System-Boundaries.png) |
| External connections, directions and status | [PlantUML](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) | ![mvp system boundaries](../../04-System-Design/Diagrams/Archived-Png/Mvp-System-Boundaries.png) |

## November 4 release applicability

Current MVP figures replace the former common-product boundary. Future and historical figures retain their details without committing them to MVP.

| Editable source | Current applicability |
| --- | --- |
| [activity-calendar-local-sync.puml](Activity-Calendar-Local-Sync.puml) | MVP core / cross-cutting|
| [activity-gmail-read-send-outcomes.puml](Activity-Gmail-Read-Send-Outcomes.puml) | Future after MVP|
| [activity-pull-request-review-merge.puml](Activity-Pull-Request-Review-Merge.puml) | Future after MVP|
| [activity-separate-deployment.puml](Activity-Separate-Deployment.puml) | Future after MVP|
| [activity-workflow-admission-attempt.puml](Activity-Workflow-Admission-Attempt.puml) | Future after MVP|
| [c4-system-context.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/drivers-c4-system-context.puml) | MVP systems|
| [data-execution-provenance-and-targets.puml](Data-Execution-Provenance-And-Targets.puml) | Future after MVP|
| [data-provider-and-calendar-context.puml](Data-Provider-And-Calendar-Context.puml) | Future after MVP|
| [data-work-and-sprint-planning.puml](Data-Work-And-Sprint-Planning.puml) | Future after MVP|
| [domain-applications-and-communication.dot](Domain-Applications-And-Communication.dot) | MVP core / cross-cutting|
| [domain-applications-and-communication.puml](Domain-Applications-And-Communication.puml) | MVP core|
| [domain-execution-and-deployment.dot](Domain-Execution-And-Deployment.dot) | Future after MVP|
| [domain-execution-and-deployment.puml](Domain-Execution-And-Deployment.puml) | Future after MVP|
| [domain-package-responsibilities.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting|
| [domain-provider-communication.puml](Domain-Provider-Communication.puml) | Future after MVP|
| [ecosystem-overview.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting|
| [ecosystem-platform-connections.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting|
| [function-decomposition.puml](Function-Decomposition.puml) | MVP systems|
| [function-dfd-context.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting|
| [interface-calendar-local-provider.puml](Interface-Calendar-Local-Provider.puml) | Mixed MVP / future|
| [interface-execution-separate-target.puml](Interface-Execution-Separate-Target.puml) | Future after MVP|
| [interface-gmail-reviewed-effects.puml](Interface-Gmail-Reviewed-Effects.puml) | Future after MVP|
| [interface-logical-components.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting|
| [process-current-workflow-questions.puml](Process-Current-Workflow-Questions.puml) | Method / document navigation|
| [scenario-calendar-local-sync.puml](Scenario-Calendar-Local-Sync.puml) | Mixed MVP / future|
| [scenario-gmail-read-send-outcomes.puml](Scenario-Gmail-Read-Send-Outcomes.puml) | Future after MVP|
| [scenario-pull-request-review-merge.puml](Scenario-Pull-Request-Review-Merge.puml) | Future after MVP|
| [scenario-separate-deployment.puml](Scenario-Separate-Deployment.puml) | Future after MVP|
| [scenario-workflow-admission-attempt.puml](Scenario-Workflow-Admission-Attempt.puml) | Future after MVP|
| [scope-stakeholder-map.puml](Scope-Stakeholder-Map.puml) | MVP systems|
| [security-untrusted-content-execution.puml](Security-Untrusted-Content-Execution.puml) | Mixed MVP / future|
| [state-calendar-mapping.puml](State-Calendar-Mapping.puml) | MVP core / cross-cutting|
| [state-deployment-effect.puml](State-Deployment-Effect.puml) | Future after MVP|
| [state-execution-attempt.puml](State-Execution-Attempt.puml) | Future after MVP|
| [state-provider-connection.puml](State-Provider-Connection.puml) | Future after MVP|
| [state-pull-request-lifecycle.puml](State-Pull-Request-Lifecycle.puml) | Future after MVP|
| [state-sprint-lifecycle.puml](State-Sprint-Lifecycle.puml) | Future after MVP|
| [system-context-external.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot) | MVP core / cross-cutting|
| [system-context-external.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting|
| [system-context-human.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot) | MVP core / cross-cutting|
| [system-context-human.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting|
| [system-context-information-boundaries.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot) | MVP core / cross-cutting|
| [system-context-information-boundaries.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting|

| [domain-work-management.puml](Domain-Work-Management.puml) | Future after MVP|
| [function-store-information.puml](Function-Store-Information.puml) | MVP systems|
| [process-documented-artifact-trail.puml](Process-Documented-Artifact-Trail.puml) | Historical / alternative|
| [scenario-work-refine-plan-end.puml](Scenario-Work-Refine-Plan-End.puml) | Mixed MVP / future|
| [traceability-selected-matrix.puml](Traceability-Selected-Matrix.puml) | Historical / alternative|

Alternative Graphviz export for [domain-applications-and-communication.dot](Domain-Applications-And-Communication.dot): [SVG](Domain-Applications-And-Communication-Graphviz.svg) · ![domain applications and communication graphviz](Domain-Applications-And-Communication-Graphviz.png). The ordinary same-stem exports follow the PlantUML source.

Alternative Graphviz export for [domain-execution-and-deployment.dot](Domain-Execution-And-Deployment.dot): [SVG](Domain-Execution-And-Deployment-Graphviz.svg) · ![domain execution and deployment graphviz](Domain-Execution-And-Deployment-Graphviz.png). The ordinary same-stem exports follow the PlantUML source.

Alternative Graphviz export for [system-context-external.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot): [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.svg) · ![logical component ownership](../../04-System-Design/Diagrams/Archived-Png/Logical-Component-Ownership.png). The ordinary same-stem exports follow the PlantUML source.

Alternative Graphviz export for [system-context-human.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot): [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.svg) · ![logical component ownership](../../04-System-Design/Diagrams/Archived-Png/Logical-Component-Ownership.png). The ordinary same-stem exports follow the PlantUML source.

Alternative Graphviz export for [system-context-information-boundaries.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot): [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.svg) · ![logical component ownership](../../04-System-Design/Diagrams/Archived-Png/Logical-Component-Ownership.png). The ordinary same-stem exports follow the PlantUML source.

## Complete diagram alignment — November 4

[Full project inventory and verification limits](../../04-System-Design/01-High-Level-Design/14-Appendices.md#design-record-01-software-architecture-diagrams-diagram-catalog-md). This current disposition supersedes earlier partial diagram-allocation lists.

| Editable source or visual | Current applicability | Matching exports |
| --- | --- | --- |
| [activity-actual-submission-capture.puml](Activity-Actual-Submission-Capture.puml) | MVP core / cross-cutting| [SVG](Activity-Actual-Submission-Capture.svg) · ![activity actual submission capture](Activity-Actual-Submission-Capture.png) |
| [activity-application-preparation.puml](Activity-Application-Preparation.puml) | MVP core / cross-cutting| [SVG](Activity-Application-Preparation.svg) · ![activity application preparation](Activity-Application-Preparation.png) |
| [activity-calendar-local-sync.puml](Activity-Calendar-Local-Sync.puml) | MVP core / cross-cutting| [SVG](Activity-Calendar-Local-Sync.svg) · ![activity calendar local sync](Activity-Calendar-Local-Sync.png) |
| [activity-collaboration-and-changed-grant.puml](Activity-Collaboration-And-Changed-Grant.puml) | MVP core / cross-cutting| [SVG](Activity-Collaboration-And-Changed-Grant.svg) · ![activity collaboration and changed grant](Activity-Collaboration-And-Changed-Grant.png) |
| [activity-disable-sharing-link.puml](Activity-Disable-Sharing-Link.puml) | MVP core / cross-cutting| [SVG](Activity-Disable-Sharing-Link.svg) · ![activity disable sharing link](Activity-Disable-Sharing-Link.png) |
| [activity-git-transfer.puml](Activity-Git-Transfer.puml) | MVP ProjectForge| [SVG](Activity-Git-Transfer.svg) · ![activity git transfer](Activity-Git-Transfer.png) |
| [activity-gmail-read-send-outcomes.puml](Activity-Gmail-Read-Send-Outcomes.puml) | Future after MVP| [SVG](Activity-Gmail-Read-Send-Outcomes.svg) · ![activity gmail read send outcomes](Activity-Gmail-Read-Send-Outcomes.png) |
| [activity-isolated-recovery-assessment.puml](Activity-Isolated-Recovery-Assessment.puml) | MVP core / cross-cutting| [SVG](Activity-Isolated-Recovery-Assessment.svg) · ![activity isolated recovery assessment](Activity-Isolated-Recovery-Assessment.png) |
| [activity-operation-result-classification.puml](Activity-Operation-Result-Classification.puml) | MVP core / cross-cutting| [SVG](Activity-Operation-Result-Classification.svg) · ![activity operation result classification](Activity-Operation-Result-Classification.png) |
| [activity-pdf-settings.puml](Activity-Pdf-Settings.puml) | MVP core / cross-cutting| [SVG](Activity-Pdf-Settings.svg) · ![activity pdf settings](Activity-Pdf-Settings.png) |
| [activity-policy-admission-evidence.puml](Activity-Policy-Admission-Evidence.puml) | MVP core / cross-cutting| [SVG](Activity-Policy-Admission-Evidence.svg) · ![activity policy admission evidence](Activity-Policy-Admission-Evidence.png) |
| [activity-profile-apply-publication.puml](Activity-Profile-Apply-Publication.puml) | MVP core / cross-cutting| [SVG](Activity-Profile-Apply-Publication.svg) · ![activity profile apply publication](Activity-Profile-Apply-Publication.png) |
| [activity-protected-retrieval.puml](Activity-Protected-Retrieval.puml) | MVP core / cross-cutting| [SVG](Activity-Protected-Retrieval.svg) · ![activity protected retrieval](Activity-Protected-Retrieval.png) |
| [activity-pull-request-review-merge.puml](Activity-Pull-Request-Review-Merge.puml) | Future after MVP| [SVG](Activity-Pull-Request-Review-Merge.svg) · ![activity pull request review merge](Activity-Pull-Request-Review-Merge.png) |
| [activity-separate-deployment.puml](Activity-Separate-Deployment.puml) | Future after MVP| [SVG](Activity-Separate-Deployment.svg) · ![activity separate deployment](Activity-Separate-Deployment.png) |
| [activity-work-refine-plan-end.puml](Activity-Work-Refine-Plan-End.puml) | Mixed MVP / future| [SVG](Activity-Work-Refine-Plan-End.svg) · ![activity work refine plan end](Activity-Work-Refine-Plan-End.png) |
| [activity-workflow-admission-attempt.puml](Activity-Workflow-Admission-Attempt.puml) | Future after MVP| [SVG](Activity-Workflow-Admission-Attempt.svg) · ![activity workflow admission attempt](Activity-Workflow-Admission-Attempt.png) |
| [analysis-inputs-and-outputs.dot](Analysis-Inputs-And-Outputs.dot) | MVP core / cross-cutting| [SVG](Analysis-Inputs-And-Outputs-Graphviz.svg) · ![analysis inputs and outputs graphviz](Analysis-Inputs-And-Outputs-Graphviz.png) |
| [analysis-inputs-and-outputs.puml](Analysis-Inputs-And-Outputs.puml) | MVP core / cross-cutting| [SVG](Analysis-Inputs-And-Outputs.svg) · ![analysis inputs and outputs](Analysis-Inputs-And-Outputs.png) |
| [analysis-seven-view-consistency.dot](Analysis-Seven-View-Consistency.dot) | MVP core / cross-cutting| [SVG](Analysis-Seven-View-Consistency-Graphviz.svg) · ![analysis seven view consistency graphviz](Analysis-Seven-View-Consistency-Graphviz.png) |
| [analysis-seven-view-consistency.puml](Analysis-Seven-View-Consistency.puml) | MVP core / cross-cutting| [SVG](Analysis-Seven-View-Consistency.svg) · ![analysis seven view consistency](Analysis-Seven-View-Consistency.png) |
| [c4-observed-demo-containers.puml](C4-Observed-Demo-Containers.puml) | Historical / alternative| [SVG](C4-Observed-Demo-Containers.svg) · ![c4 observed demo containers](C4-Observed-Demo-Containers.png) |
| [c4-system-context.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/drivers-c4-system-context.puml) | MVP systems| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/drivers-c4-system-context.svg) · ![drivers c4 system context](../../04-System-Design/Diagrams/Archived-Png/Drivers-C4-System-Context.png) |
| [contract-apply-object-snapshots.puml](Contract-Apply-Object-Snapshots.puml) | MVP core / cross-cutting| [SVG](Contract-Apply-Object-Snapshots.svg) · ![contract apply object snapshots](Contract-Apply-Object-Snapshots.png) |
| [contract-constraint-application.puml](Contract-Constraint-Application.puml) | MVP core / cross-cutting| [SVG](Contract-Constraint-Application.svg) · ![contract constraint application](Contract-Constraint-Application.png) |
| [contract-dc-o02-boundary.puml](Contract-Dc-O02-Boundary.puml) | MVP core / cross-cutting| [SVG](Contract-Dc-O02-Boundary.svg) · ![contract dc o02 boundary](Contract-Dc-O02-Boundary.png) |
| [contract-dc-o03-boundary.puml](Contract-Dc-O03-Boundary.puml) | MVP core / cross-cutting| [SVG](Contract-Dc-O03-Boundary.svg) · ![contract dc o03 boundary](Contract-Dc-O03-Boundary.png) |
| [contract-dc-o05-boundary.puml](Contract-Dc-O05-Boundary.puml) | MVP core / cross-cutting| [SVG](Contract-Dc-O05-Boundary.svg) · ![contract dc o05 boundary](Contract-Dc-O05-Boundary.png) |
| [contract-dc-o12-boundary.puml](Contract-Dc-O12-Boundary.puml) | Future after MVP| [SVG](Contract-Dc-O12-Boundary.svg) · ![contract dc o12 boundary](Contract-Dc-O12-Boundary.png) |
| [contract-dc-o14-boundary.puml](Contract-Dc-O14-Boundary.puml) | Future after MVP| [SVG](Contract-Dc-O14-Boundary.svg) · ![contract dc o14 boundary](Contract-Dc-O14-Boundary.png) |
| [contract-dc-o26-boundary.puml](Contract-Dc-O26-Boundary.puml) | Future after MVP| [SVG](Contract-Dc-O26-Boundary.svg) · ![contract dc o26 boundary](Contract-Dc-O26-Boundary.png) |
| [contract-dc-o30-boundary.puml](Contract-Dc-O30-Boundary.puml) | Future after MVP| [SVG](Contract-Dc-O30-Boundary.svg) · ![contract dc o30 boundary](Contract-Dc-O30-Boundary.png) |
| [contract-dc-o37-boundary.puml](Contract-Dc-O37-Boundary.puml) | MVP core / cross-cutting| [SVG](Contract-Dc-O37-Boundary.svg) · ![contract dc o37 boundary](Contract-Dc-O37-Boundary.png) |
| [contract-outcome-interpretation.puml](Contract-Outcome-Interpretation.puml) | MVP core / cross-cutting| [SVG](Contract-Outcome-Interpretation.svg) · ![contract outcome interpretation](Contract-Outcome-Interpretation.png) |
| [data-applications-and-actual-material.puml](Data-Applications-And-Actual-Material.puml) | MVP core| [SVG](Data-Applications-And-Actual-Material.svg) · ![data applications and actual material](Data-Applications-And-Actual-Material.png) |
| [data-authority-policy-and-recovery.puml](Data-Authority-Policy-And-Recovery.puml) | MVP core / cross-cutting| [SVG](Data-Authority-Policy-And-Recovery.svg) · ![data authority policy and recovery](Data-Authority-Policy-And-Recovery.png) |
| [data-evidence-language-and-selection.puml](Data-Evidence-Language-And-Selection.puml) | MVP core / cross-cutting| [SVG](Data-Evidence-Language-And-Selection.svg) · ![data evidence language and selection](Data-Evidence-Language-And-Selection.png) |
| [data-execution-provenance-and-targets.puml](Data-Execution-Provenance-And-Targets.puml) | Future after MVP| [SVG](Data-Execution-Provenance-And-Targets.svg) · ![data execution provenance and targets](Data-Execution-Provenance-And-Targets.png) |
| [data-git-revisions-and-collaboration.puml](Data-Git-Revisions-And-Collaboration.puml) | Future after MVP| [SVG](Data-Git-Revisions-And-Collaboration.svg) · ![data git revisions and collaboration](Data-Git-Revisions-And-Collaboration.png) |
| [data-profile-and-tailoring.puml](Data-Profile-And-Tailoring.puml) | MVP core / cross-cutting| [SVG](Data-Profile-And-Tailoring.svg) · ![data profile and tailoring](Data-Profile-And-Tailoring.png) |
| [data-provider-and-calendar-context.puml](Data-Provider-And-Calendar-Context.puml) | Future after MVP| [SVG](Data-Provider-And-Calendar-Context.svg) · ![data provider and calendar context](Data-Provider-And-Calendar-Context.png) |
| [data-publication-pdf-and-sharing.puml](Data-Publication-Pdf-And-Sharing.puml) | MVP core / cross-cutting| [SVG](Data-Publication-Pdf-And-Sharing.svg) · ![data publication pdf and sharing](Data-Publication-Pdf-And-Sharing.png) |
| [data-work-and-sprint-planning.puml](Data-Work-And-Sprint-Planning.puml) | Future after MVP| [SVG](Data-Work-And-Sprint-Planning.svg) · ![data work and sprint planning](Data-Work-And-Sprint-Planning.png) |
| [deployment-observed-host.puml](Deployment-Observed-Host.puml) | Historical / alternative| [SVG](Deployment-Observed-Host.svg) · ![deployment observed host](Deployment-Observed-Host.png) |
| [documentation-navigation.puml](Documentation-Navigation.puml) | MVP core / cross-cutting| [SVG](Documentation-Navigation.svg) · ![documentation navigation](Documentation-Navigation.png) |
| [domain-access-files-and-recovery.dot](Domain-Access-Files-And-Recovery.dot) | MVP core / cross-cutting| [SVG](Domain-Access-Files-And-Recovery-Graphviz.svg) · ![domain access files and recovery graphviz](Domain-Access-Files-And-Recovery-Graphviz.png) |
| [domain-access-files-and-recovery.puml](Domain-Access-Files-And-Recovery.puml) | MVP core / cross-cutting| [SVG](Domain-Access-Files-And-Recovery.svg) · ![domain access files and recovery](Domain-Access-Files-And-Recovery.png) |
| [domain-applications-and-communication.dot](Domain-Applications-And-Communication.dot) | MVP core / cross-cutting| [SVG](Domain-Applications-And-Communication-Graphviz.svg) · ![domain applications and communication graphviz](Domain-Applications-And-Communication-Graphviz.png) |
| [domain-applications-and-communication.puml](Domain-Applications-And-Communication.puml) | MVP core| [SVG](Domain-Applications-And-Communication.svg) · ![domain applications and communication](Domain-Applications-And-Communication.png) |
| [domain-evidence-and-language.puml](Domain-Evidence-And-Language.puml) | MVP core / cross-cutting| [SVG](Domain-Evidence-And-Language.svg) · ![domain evidence and language](Domain-Evidence-And-Language.png) |
| [domain-execution-and-deployment.dot](Domain-Execution-And-Deployment.dot) | Future after MVP| [SVG](Domain-Execution-And-Deployment-Graphviz.svg) · ![domain execution and deployment graphviz](Domain-Execution-And-Deployment-Graphviz.png) |
| [domain-execution-and-deployment.puml](Domain-Execution-And-Deployment.puml) | Future after MVP| [SVG](Domain-Execution-And-Deployment.svg) · ![domain execution and deployment](Domain-Execution-And-Deployment.png) |
| [domain-git-collaboration.dot](Domain-Git-Collaboration.dot) | Future after MVP| [SVG](Domain-Git-Collaboration-Graphviz.svg) · ![domain git collaboration graphviz](Domain-Git-Collaboration-Graphviz.png) |
| [domain-git-collaboration.puml](Domain-Git-Collaboration.puml) | Future after MVP| [SVG](Domain-Git-Collaboration.svg) · ![domain git collaboration](Domain-Git-Collaboration.png) |
| [domain-package-responsibilities.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) · ![mvp system boundaries](../../04-System-Design/Diagrams/Archived-Png/Mvp-System-Boundaries.png) |
| [domain-professional-presentation.dot](Domain-Professional-Presentation.dot) | MVP core / cross-cutting| [SVG](Domain-Professional-Presentation-Graphviz.svg) · ![domain professional presentation graphviz](Domain-Professional-Presentation-Graphviz.png) |
| [domain-professional-presentation.puml](Domain-Professional-Presentation.puml) | MVP core / cross-cutting| [SVG](Domain-Professional-Presentation.svg) · ![domain professional presentation](Domain-Professional-Presentation.png) |
| [domain-proposed-multiplicity.puml](Domain-Proposed-Multiplicity.puml) | MVP core / cross-cutting| [SVG](Domain-Proposed-Multiplicity.svg) · ![domain proposed multiplicity](Domain-Proposed-Multiplicity.png) |
| [domain-provider-communication.puml](Domain-Provider-Communication.puml) | Future after MVP| [SVG](Domain-Provider-Communication.svg) · ![domain provider communication](Domain-Provider-Communication.png) |
| [domain-publication-and-sharing.dot](Domain-Publication-And-Sharing.dot) | MVP core / cross-cutting| [SVG](Domain-Publication-And-Sharing-Graphviz.svg) · ![domain publication and sharing graphviz](Domain-Publication-And-Sharing-Graphviz.png) |
| [domain-publication-and-sharing.puml](Domain-Publication-And-Sharing.puml) | MVP core / cross-cutting| [SVG](Domain-Publication-And-Sharing.svg) · ![domain publication and sharing](Domain-Publication-And-Sharing.png) |
| [domain-work-management.dot](Domain-Work-Management.dot) | Future after MVP| [SVG](Domain-Work-Management-Graphviz.svg) · ![domain work management graphviz](Domain-Work-Management-Graphviz.png) |
| [domain-work-management.puml](Domain-Work-Management.puml) | Future after MVP| [SVG](Domain-Work-Management.svg) · ![domain work management](Domain-Work-Management.png) |
| [ecosystem-overview.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) · ![mvp system boundaries](../../04-System-Design/Diagrams/Archived-Png/Mvp-System-Boundaries.png) |
| [ecosystem-platform-connections.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) · ![mvp system boundaries](../../04-System-Design/Diagrams/Archived-Png/Mvp-System-Boundaries.png) |
| [function-decomposition.puml](Function-Decomposition.puml) | MVP systems| [SVG](Function-Decomposition.svg) · ![function decomposition](Function-Decomposition.png) |
| [function-dfd-context.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) · ![mvp system boundaries](../../04-System-Design/Diagrams/Archived-Png/Mvp-System-Boundaries.png) |
| [function-dfd-level1-content.puml](Function-Dfd-Level1-Content.puml) | MVP core| [SVG](Function-Dfd-Level1-Content.svg) · ![function dfd level1 content](Function-Dfd-Level1-Content.png) |
| [function-dfd-level1-work-operations.puml](Function-Store-Information.puml) | MVP systems| [SVG](Function-Store-Information.svg) · ![function store information](Function-Store-Information.png) |
| [function-profile-level2.puml](Function-Profile-Level2.puml) | MVP core / cross-cutting| [SVG](Function-Profile-Level2.svg) · ![function profile level2](Function-Profile-Level2.png) |
| [function-store-information.puml](Function-Store-Information.puml) | MVP systems| [SVG](Function-Store-Information.svg) · ![function store information](Function-Store-Information.png) |
| [handoff-delivery-reconciliation.puml](Handoff-Delivery-Reconciliation.puml) | Method / document navigation| [SVG](Handoff-Delivery-Reconciliation.svg) · ![handoff delivery reconciliation](Handoff-Delivery-Reconciliation.png) |
| [handoff-dependency-network.puml](Handoff-Dependency-Network.puml) | MVP delivery| [SVG](Handoff-Dependency-Network.svg) · ![handoff dependency network](Handoff-Dependency-Network.png) |
| [handoff-design-question-record.puml](Handoff-Design-Question-Record.puml) | MVP core / cross-cutting| [SVG](Handoff-Design-Question-Record.svg) · ![handoff design question record](Handoff-Design-Question-Record.png) |
| [handoff-evidence-dependent-commitment.puml](Handoff-Evidence-Dependent-Commitment.puml) | MVP core / cross-cutting| [SVG](Handoff-Evidence-Dependent-Commitment.svg) · ![handoff evidence dependent commitment](Handoff-Evidence-Dependent-Commitment.png) |
| [handoff-existing-review-gates.puml](Handoff-Existing-Review-Gates.puml) | MVP core / cross-cutting| [SVG](Handoff-Existing-Review-Gates.svg) · ![handoff existing review gates](Handoff-Existing-Review-Gates.png) |
| [handoff-package-position.puml](Handoff-Package-Position.puml) | MVP core / cross-cutting| [SVG](Handoff-Package-Position.svg) · ![handoff package position](Handoff-Package-Position.png) |
| [interface-calendar-local-provider.puml](Interface-Calendar-Local-Provider.puml) | Mixed MVP / future| [SVG](Interface-Calendar-Local-Provider.svg) · ![interface calendar local provider](Interface-Calendar-Local-Provider.png) |
| [interface-employer-protected-representation.puml](Interface-Employer-Protected-Representation.puml) | MVP core / cross-cutting| [SVG](Interface-Employer-Protected-Representation.svg) · ![interface employer protected representation](Interface-Employer-Protected-Representation.png) |
| [interface-execution-separate-target.puml](Interface-Execution-Separate-Target.puml) | Future after MVP| [SVG](Interface-Execution-Separate-Target.svg) · ![interface execution separate target](Interface-Execution-Separate-Target.png) |
| [interface-file-candidate-result.puml](Interface-File-Candidate-Result.puml) | MVP core / cross-cutting| [SVG](Interface-File-Candidate-Result.svg) · ![interface file candidate result](Interface-File-Candidate-Result.png) |
| [interface-gmail-reviewed-effects.puml](Interface-Gmail-Reviewed-Effects.puml) | Future after MVP| [SVG](Interface-Gmail-Reviewed-Effects.svg) · ![interface gmail reviewed effects](Interface-Gmail-Reviewed-Effects.png) |
| [interface-logical-components.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) · ![mvp system boundaries](../../04-System-Design/Diagrams/Archived-Png/Mvp-System-Boundaries.png) |
| [interface-operating-delivery-recovery.puml](Interface-Operating-Delivery-Recovery.puml) | Mixed MVP / future| [SVG](Interface-Operating-Delivery-Recovery.svg) · ![interface operating delivery recovery](Interface-Operating-Delivery-Recovery.png) |
| [interface-private-human-context.puml](Interface-Private-Human-Context.puml) | MVP core / cross-cutting| [SVG](Interface-Private-Human-Context.svg) · ![interface private human context](Interface-Private-Human-Context.png) |
| [interface-real-git-client.puml](Interface-Real-Git-Client.puml) | MVP ProjectForge| [SVG](Interface-Real-Git-Client.svg) · ![interface real git client](Interface-Real-Git-Client.png) |
| [interface-request-response-contract.puml](Interface-Request-Response-Contract.puml) | MVP core / cross-cutting| [SVG](Interface-Request-Response-Contract.svg) · ![interface request response contract](Interface-Request-Response-Contract.png) |
| [operations-effect-evidence.puml](Operations-Effect-Evidence.puml) | MVP core / cross-cutting| [SVG](Operations-Effect-Evidence.svg) · ![operations effect evidence](Operations-Effect-Evidence.png) |
| [operations-resource-envelope.puml](Operations-Resource-Envelope.puml) | MVP core / cross-cutting| [SVG](Operations-Resource-Envelope.svg) · ![operations resource envelope](Operations-Resource-Envelope.png) |
| [process-bpmn-as-is-boundary.bpmn](Process-Bpmn-As-Is-Boundary.bpmn) | Historical / evidence limit | [SVG](Process-Bpmn-As-Is-Boundary.svg) · ![process bpmn as is boundary](Process-Bpmn-As-Is-Boundary.png) |
| [process-bpmn-target-publication.bpmn](Process-Bpmn-Target-Publication.bpmn) | MVP core publication | [SVG](Process-Bpmn-Target-Publication.svg) · ![process bpmn target publication](Process-Bpmn-Target-Publication.png) |
| [process-current-workflow-questions.puml](Process-Current-Workflow-Questions.puml) | Method / document navigation| [SVG](Process-Current-Workflow-Questions.svg) · ![process current workflow questions](Process-Current-Workflow-Questions.png) |
| [process-documented-artifact-trail.puml](Process-Documented-Artifact-Trail.puml) | Historical / alternative| [SVG](Process-Documented-Artifact-Trail.svg) · ![process documented artifact trail](Process-Documented-Artifact-Trail.png) |
| [process-evidence-classes.puml](Process-Evidence-Classes.puml) | MVP core / cross-cutting| [SVG](Process-Evidence-Classes.svg) · ![process evidence classes](Process-Evidence-Classes.png) |
| [process-hypothesis-validation.puml](Process-Hypothesis-Validation.puml) | MVP core / cross-cutting| [SVG](Process-Hypothesis-Validation.svg) · ![process hypothesis validation](Process-Hypothesis-Validation.png) |
| [process-improvement-evidence.puml](Process-Improvement-Evidence.puml) | MVP core / cross-cutting| [SVG](Process-Improvement-Evidence.svg) · ![process improvement evidence](Process-Improvement-Evidence.png) |
| [quality-scenario-measurement.puml](Quality-Scenario-Measurement.puml) | MVP core / cross-cutting| [SVG](Quality-Scenario-Measurement.svg) · ![quality scenario measurement](Quality-Scenario-Measurement.png) |
| [recovery-scoped-usable-state.puml](Recovery-Scoped-Usable-State.puml) | MVP core / cross-cutting| [SVG](Recovery-Scoped-Usable-State.svg) · ![recovery scoped usable state](Recovery-Scoped-Usable-State.png) |
| [review-change-impact-route.puml](Review-Change-Impact-Route.puml) | MVP core / cross-cutting| [SVG](Review-Change-Impact-Route.svg) · ![review change impact route](Review-Change-Impact-Route.png) |
| [review-current-position.puml](Review-Current-Position.puml) | Historical / alternative| [SVG](Review-Current-Position.svg) · ![review current position](Review-Current-Position.png) |
| [review-trace-evidence-levels.puml](Review-Trace-Evidence-Levels.puml) | Historical / alternative| [SVG](Review-Trace-Evidence-Levels.svg) · ![review trace evidence levels](Review-Trace-Evidence-Levels.png) |
| [rule-rb-d01-decision.puml](Rule-Rb-D01-Decision.puml) | MVP core / cross-cutting| [SVG](Rule-Rb-D01-Decision.svg) · ![rule rb d01 decision](Rule-Rb-D01-Decision.png) |
| [rule-rb-d04-decision.puml](Rule-Rb-D04-Decision.puml) | MVP core / cross-cutting| [SVG](Rule-Rb-D04-Decision.svg) · ![rule rb d04 decision](Rule-Rb-D04-Decision.png) |
| [rule-rb-d06-decision.puml](Rule-Rb-D06-Decision.puml) | MVP core / cross-cutting| [SVG](Rule-Rb-D06-Decision.svg) · ![rule rb d06 decision](Rule-Rb-D06-Decision.png) |
| [rule-rb-d07-decision.puml](Rule-Rb-D07-Decision.puml) | Future after MVP| [SVG](Rule-Rb-D07-Decision.svg) · ![rule rb d07 decision](Rule-Rb-D07-Decision.png) |
| [rule-rb-d11-decision.puml](Rule-Rb-D11-Decision.puml) | Future after MVP| [SVG](Rule-Rb-D11-Decision.svg) · ![rule rb d11 decision](Rule-Rb-D11-Decision.png) |
| [rule-rb-d12-decision.puml](Rule-Rb-D12-Decision.puml) | Future after MVP| [SVG](Rule-Rb-D12-Decision.svg) · ![rule rb d12 decision](Rule-Rb-D12-Decision.png) |
| [rule-rb-d15-decision.puml](Rule-Rb-D15-Decision.puml) | MVP core / cross-cutting| [SVG](Rule-Rb-D15-Decision.svg) · ![rule rb d15 decision](Rule-Rb-D15-Decision.png) |
| [rule-rb-d16-decision.puml](Rule-Rb-D16-Decision.puml) | MVP core / cross-cutting| [SVG](Rule-Rb-D16-Decision.svg) · ![rule rb d16 decision](Rule-Rb-D16-Decision.png) |
| [scenario-actual-submission-capture.puml](Scenario-Actual-Submission-Capture.puml) | MVP core / cross-cutting| [SVG](Scenario-Actual-Submission-Capture.svg) · ![scenario actual submission capture](Scenario-Actual-Submission-Capture.png) |
| [scenario-application-preparation.puml](Scenario-Application-Preparation.puml) | MVP core / cross-cutting| [SVG](Scenario-Application-Preparation.svg) · ![scenario application preparation](Scenario-Application-Preparation.png) |
| [scenario-calendar-local-sync.puml](Scenario-Calendar-Local-Sync.puml) | Mixed MVP / future| [SVG](Scenario-Calendar-Local-Sync.svg) · ![scenario calendar local sync](Scenario-Calendar-Local-Sync.png) |
| [scenario-collaboration-and-changed-grant.puml](Scenario-Collaboration-And-Changed-Grant.puml) | MVP core / cross-cutting| [SVG](Scenario-Collaboration-And-Changed-Grant.svg) · ![scenario collaboration and changed grant](Scenario-Collaboration-And-Changed-Grant.png) |
| [scenario-disable-sharing-link.puml](Scenario-Disable-Sharing-Link.puml) | MVP core / cross-cutting| [SVG](Scenario-Disable-Sharing-Link.svg) · ![scenario disable sharing link](Scenario-Disable-Sharing-Link.png) |
| [scenario-git-transfer.puml](Scenario-Git-Transfer.puml) | MVP ProjectForge| [SVG](Scenario-Git-Transfer.svg) · ![scenario git transfer](Scenario-Git-Transfer.png) |
| [scenario-gmail-read-send-outcomes.puml](Scenario-Gmail-Read-Send-Outcomes.puml) | Future after MVP| [SVG](Scenario-Gmail-Read-Send-Outcomes.svg) · ![scenario gmail read send outcomes](Scenario-Gmail-Read-Send-Outcomes.png) |
| [scenario-isolated-recovery-assessment.puml](Scenario-Isolated-Recovery-Assessment.puml) | MVP core / cross-cutting| [SVG](Scenario-Isolated-Recovery-Assessment.svg) · ![scenario isolated recovery assessment](Scenario-Isolated-Recovery-Assessment.png) |
| [scenario-pdf-settings.puml](Scenario-Pdf-Settings.puml) | MVP core / cross-cutting| [SVG](Scenario-Pdf-Settings.svg) · ![scenario pdf settings](Scenario-Pdf-Settings.png) |
| [scenario-policy-admission-evidence.puml](Scenario-Policy-Admission-Evidence.puml) | MVP core / cross-cutting| [SVG](Scenario-Policy-Admission-Evidence.svg) · ![scenario policy admission evidence](Scenario-Policy-Admission-Evidence.png) |
| [scenario-profile-apply-publication.puml](Scenario-Profile-Apply-Publication.puml) | MVP core / cross-cutting| [SVG](Scenario-Profile-Apply-Publication.svg) · ![scenario profile apply publication](Scenario-Profile-Apply-Publication.png) |
| [scenario-protected-retrieval.puml](Scenario-Protected-Retrieval.puml) | MVP core / cross-cutting| [SVG](Scenario-Protected-Retrieval.svg) · ![scenario protected retrieval](Scenario-Protected-Retrieval.png) |
| [scenario-pull-request-review-merge.puml](Scenario-Pull-Request-Review-Merge.puml) | Future after MVP| [SVG](Scenario-Pull-Request-Review-Merge.svg) · ![scenario pull request review merge](Scenario-Pull-Request-Review-Merge.png) |
| [scenario-separate-deployment.puml](Scenario-Separate-Deployment.puml) | Future after MVP| [SVG](Scenario-Separate-Deployment.svg) · ![scenario separate deployment](Scenario-Separate-Deployment.png) |
| [scenario-work-refine-plan-end.puml](Scenario-Work-Refine-Plan-End.puml) | Mixed MVP / future| [SVG](Scenario-Work-Refine-Plan-End.svg) · ![scenario work refine plan end](Scenario-Work-Refine-Plan-End.png) |
| [scenario-workflow-admission-attempt.puml](Scenario-Workflow-Admission-Attempt.puml) | Future after MVP| [SVG](Scenario-Workflow-Admission-Attempt.svg) · ![scenario workflow admission attempt](Scenario-Workflow-Admission-Attempt.png) |
| [scope-stakeholder-map.puml](Scope-Stakeholder-Map.puml) | MVP systems| [SVG](Scope-Stakeholder-Map.svg) · ![scope stakeholder map](Scope-Stakeholder-Map.png) |
| [security-data-flow-trust.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/06-design-quality-and-security-analysis/diagrams/security-trust-boundaries.puml) | MVP systems| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/06-design-quality-and-security-analysis/diagrams/security-trust-boundaries.svg) · ![security trust boundaries](../../04-System-Design/Diagrams/Archived-Png/Security-Trust-Boundaries.png) |
| [security-disaster-recovery-sequence.puml](Security-Disaster-Recovery-Sequence.puml) | MVP core / cross-cutting| [SVG](Security-Disaster-Recovery-Sequence.svg) · ![security disaster recovery sequence](Security-Disaster-Recovery-Sequence.png) |
| [security-ha-failover-sequence.puml](Security-Ha-Failover-Sequence.puml) | MVP core / cross-cutting| [SVG](Security-Ha-Failover-Sequence.svg) · ![security ha failover sequence](Security-Ha-Failover-Sequence.png) |
| [security-infrastructure-topology.puml](Security-Infrastructure-Topology.puml) | Historical / alternative| [SVG](Security-Infrastructure-Topology.svg) · ![security infrastructure topology](Security-Infrastructure-Topology.png) |
| [security-scoped-authority.puml](Security-Scoped-Authority.puml) | MVP core / cross-cutting| [SVG](Security-Scoped-Authority.svg) · ![security scoped authority](Security-Scoped-Authority.png) |
| [security-threat-boundary-model.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/06-design-quality-and-security-analysis/diagrams/security-trust-boundaries.puml) | MVP systems| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/06-design-quality-and-security-analysis/diagrams/security-trust-boundaries.svg) · ![security trust boundaries](../../04-System-Design/Diagrams/Archived-Png/Security-Trust-Boundaries.png) |
| [security-untrusted-content-execution.puml](Security-Untrusted-Content-Execution.puml) | Mixed MVP / future| [SVG](Security-Untrusted-Content-Execution.svg) · ![security untrusted content execution](Security-Untrusted-Content-Execution.png) |
| [start-here-analysis-route.dot](Start-Here-Analysis-Route.dot) | MVP core / cross-cutting| [SVG](Start-Here-Analysis-Route-Graphviz.svg) · ![start here analysis route graphviz](Start-Here-Analysis-Route-Graphviz.png) |
| [start-here-analysis-route.puml](Start-Here-Analysis-Route.puml) | MVP core / cross-cutting| [SVG](Start-Here-Analysis-Route.svg) · ![start here analysis route](Start-Here-Analysis-Route.png) |
| [start-here-profile-publication.dot](Start-Here-Profile-Publication.dot) | MVP core / cross-cutting| [SVG](Start-Here-Profile-Publication-Graphviz.svg) · ![start here profile publication graphviz](Start-Here-Profile-Publication-Graphviz.png) |
| [start-here-profile-publication.puml](Start-Here-Profile-Publication.puml) | MVP core / cross-cutting| [SVG](Start-Here-Profile-Publication.svg) · ![start here profile publication](Start-Here-Profile-Publication.png) |
| [state-account-eligibility.puml](State-Account-Eligibility.puml) | MVP core / cross-cutting| [SVG](State-Account-Eligibility.svg) · ![state account eligibility](State-Account-Eligibility.png) |
| [state-application-progress.puml](State-Application-Progress.puml) | MVP core| [SVG](State-Application-Progress.svg) · ![state application progress](State-Application-Progress.png) |
| [state-artifact-availability.puml](State-Artifact-Availability.puml) | MVP core / cross-cutting| [SVG](State-Artifact-Availability.svg) · ![state artifact availability](State-Artifact-Availability.png) |
| [state-calendar-mapping.puml](State-Calendar-Mapping.puml) | MVP core / cross-cutting| [SVG](State-Calendar-Mapping.svg) · ![state calendar mapping](State-Calendar-Mapping.png) |
| [state-collaboration-grant.puml](State-Collaboration-Grant.puml) | MVP core / cross-cutting| [SVG](State-Collaboration-Grant.svg) · ![state collaboration grant](State-Collaboration-Grant.png) |
| [state-deployment-effect.puml](State-Deployment-Effect.puml) | Future after MVP| [SVG](State-Deployment-Effect.svg) · ![state deployment effect](State-Deployment-Effect.png) |
| [state-execution-attempt.puml](State-Execution-Attempt.puml) | Future after MVP| [SVG](State-Execution-Attempt.svg) · ![state execution attempt](State-Execution-Attempt.png) |
| [state-mail-send-attempt.puml](State-Mail-Send-Attempt.puml) | Future after MVP| [SVG](State-Mail-Send-Attempt.svg) · ![state mail send attempt](State-Mail-Send-Attempt.png) |
| [state-operation-observation.puml](State-Operation-Observation.puml) | MVP core / cross-cutting| [SVG](State-Operation-Observation.svg) · ![state operation observation](State-Operation-Observation.png) |
| [state-protected-link.puml](State-Protected-Link.puml) | MVP core / cross-cutting| [SVG](State-Protected-Link.svg) · ![state protected link](State-Protected-Link.png) |
| [state-provider-connection.puml](State-Provider-Connection.puml) | Future after MVP| [SVG](State-Provider-Connection.svg) · ![state provider connection](State-Provider-Connection.png) |
| [state-pull-request-lifecycle.puml](State-Pull-Request-Lifecycle.puml) | Future after MVP| [SVG](State-Pull-Request-Lifecycle.svg) · ![state pull request lifecycle](State-Pull-Request-Lifecycle.png) |
| [state-recovery-assessment.puml](State-Recovery-Assessment.puml) | MVP core / cross-cutting| [SVG](State-Recovery-Assessment.svg) · ![state recovery assessment](State-Recovery-Assessment.png) |
| [state-reference-aware-retention.puml](State-Reference-Aware-Retention.puml) | MVP core / cross-cutting| [SVG](State-Reference-Aware-Retention.svg) · ![state reference aware retention](State-Reference-Aware-Retention.png) |
| [state-resume-draft-publication.puml](State-Resume-Draft-Publication.puml) | MVP core / cross-cutting| [SVG](State-Resume-Draft-Publication.svg) · ![state resume draft publication](State-Resume-Draft-Publication.png) |
| [state-sprint-lifecycle.puml](State-Sprint-Lifecycle.puml) | Future after MVP| [SVG](State-Sprint-Lifecycle.svg) · ![state sprint lifecycle](State-Sprint-Lifecycle.png) |
| [state-submitted-set-completeness.puml](State-Submitted-Set-Completeness.puml) | MVP core / cross-cutting| [SVG](State-Submitted-Set-Completeness.svg) · ![state submitted set completeness](State-Submitted-Set-Completeness.png) |
| [state-work-item-task.puml](State-Work-Item-Task.puml) | MVP core / cross-cutting| [SVG](State-Work-Item-Task.svg) · ![state work item task](State-Work-Item-Task.png) |
| [system-context-external.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.svg) · ![logical component ownership](../../04-System-Design/Diagrams/Archived-Png/Logical-Component-Ownership.png) |
| [system-context-external.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) · ![mvp system boundaries](../../04-System-Design/Diagrams/Archived-Png/Mvp-System-Boundaries.png) |
| [system-context-human.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.svg) · ![logical component ownership](../../04-System-Design/Diagrams/Archived-Png/Logical-Component-Ownership.png) |
| [system-context-human.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) · ![mvp system boundaries](../../04-System-Design/Diagrams/Archived-Png/Mvp-System-Boundaries.png) |
| [system-context-information-boundaries.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.svg) · ![logical component ownership](../../04-System-Design/Diagrams/Archived-Png/Logical-Component-Ownership.png) |
| [system-context-information-boundaries.puml](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.puml) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/mvp-system-boundaries.svg) · ![mvp system boundaries](../../04-System-Design/Diagrams/Archived-Png/Mvp-System-Boundaries.png) |
| [traceability-selected-matrix.puml](Traceability-Selected-Matrix.puml) | Historical / alternative| [SVG](Traceability-Selected-Matrix.svg) · ![traceability selected matrix](Traceability-Selected-Matrix.png) |

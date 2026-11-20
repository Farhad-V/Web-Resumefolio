# Requirements Diagrams

Current MVP scope and selected mechanisms: [Baseline](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/README.md). Deferred provider, advanced collaboration and workflow-execution designs are not MVP prerequisites.

## November 4 release applicability

Current MVP figures replace the former common-product boundary. Future and historical figures retain their details without committing them to MVP.

| Editable source | Current applicability |
| --- | --- |
| [actors-system-context.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot) | MVP core / cross-cutting|
| [external-interface-context.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot) | MVP core / cross-cutting|
| [git-hosting-capability-map.dot](Git-hosting-capability-map.dot) | Mixed MVP / future|
| [git-review-merge-flow.puml](Git-review-merge-flow.puml) | Future after MVP|
| [google-integration-context.dot](Google-integration-context.dot) | Future communications|
| [google-operation-outcomes.puml](Google-operation-outcomes.puml) | Future after MVP|
| [kanban-sprint-concept-map.dot](Kanban-sprint-concept-map.dot) | Future after MVP|
| [pdf-sharing-boundaries.dot](Pdf-sharing-boundaries.dot) | MVP core / cross-cutting|
| [sprint-planning-review-flow.puml](Sprint-planning-review-flow.puml) | Method / document navigation|
| [use-cases-execution-and-deployment.puml](Use-cases-execution-and-deployment.puml) | Future after MVP|
| [use-cases-mail-and-calendar.puml](Use-cases-mail-and-calendar.puml) | Future communications|
| [use-cases-work-and-sprints.puml](Use-cases-work-and-sprints.puml) | Future after MVP|
| [workflow-execution-boundaries.dot](Workflow-execution-boundaries.dot) | Future after MVP|
| [workflow-run-control-flow.puml](Workflow-run-control-flow.puml) | Future after MVP|

## Complete diagram alignment — November 4

[Full project inventory and verification limits](../../04-System-design/01-High-level-design/High-level-design.md#design-record-01-software-architecture-diagrams-diagram-catalog-md). This current disposition supersedes earlier partial diagram-allocation lists.

| Editable source or visual | Current applicability | Matching exports |
| --- | --- | --- |
| [accounts-access-contexts.dot](Accounts-access-contexts.dot) | MVP core / cross-cutting| [SVG](Accounts-access-contexts.svg) · ![accounts access contexts](Accounts-access-contexts.png) |
| [accounts-request-authorization.puml](Accounts-request-authorization.puml) | MVP core / cross-cutting| [SVG](Accounts-request-authorization.svg) · ![accounts request authorization](Accounts-request-authorization.png) |
| [actors-goal-overview.puml](Actors-goal-overview.puml) | MVP actor goals| [SVG](Actors-goal-overview.svg) · ![actors goal overview](Actors-goal-overview.png) |
| [actors-system-context.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.svg) · ![logical component ownership](../../Design-assets/Archived-png/Logical-component-ownership.png) |
| [administration-file-admission-flow.puml](Administration-file-admission-flow.puml) | MVP core / cross-cutting| [SVG](Administration-file-admission-flow.svg) · ![administration file admission flow](Administration-file-admission-flow.png) |
| [administration-files-policy-map.dot](Administration-files-policy-map.dot) | MVP core / cross-cutting| [SVG](Administration-files-policy-map.svg) · ![administration files policy map](Administration-files-policy-map.png) |
| [application-submission-capture.puml](Application-submission-capture.puml) | MVP core / cross-cutting| [SVG](Application-submission-capture.svg) · ![application submission capture](Application-submission-capture.png) |
| [business-outcome-assessment.puml](Business-outcome-assessment.puml) | MVP core / cross-cutting| [SVG](Business-outcome-assessment.svg) · ![business outcome assessment](Business-outcome-assessment.png) |
| [business-outcomes-map.dot](Business-outcomes-map.dot) | MVP core / cross-cutting| [SVG](Business-outcomes-map.svg) · ![business outcomes map](Business-outcomes-map.png) |
| [change-baseline-record-map.dot](Change-baseline-record-map.dot) | Method / document navigation| [SVG](Change-baseline-record-map.svg) · ![change baseline record map](Change-baseline-record-map.png) |
| [data-definition-review-flow.puml](Data-definition-review-flow.puml) | Method / document navigation| [SVG](Data-definition-review-flow.svg) · ![data definition review flow](Data-definition-review-flow.png) |
| [data-definitions-map.dot](Data-definitions-map.dot) | Mixed MVP / future| [SVG](Data-definitions-map.svg) · ![data definitions map](Data-definitions-map.png) |
| [data-lifecycle-boundaries.dot](Data-lifecycle-boundaries.dot) | MVP core / cross-cutting| [SVG](Data-lifecycle-boundaries.svg) · ![data lifecycle boundaries](Data-lifecycle-boundaries.png) |
| [data-retirement-review.puml](Data-retirement-review.puml) | MVP core / cross-cutting| [SVG](Data-retirement-review.svg) · ![data retirement review](Data-retirement-review.png) |
| [data-submission-boundaries.puml](Data-submission-boundaries.puml) | MVP core / cross-cutting| [SVG](Data-submission-boundaries.svg) · ![data submission boundaries](Data-submission-boundaries.png) |
| [data-terminology-boundaries.dot](Data-terminology-boundaries.dot) | Mixed MVP / future| [SVG](Data-terminology-boundaries.svg) · ![data terminology boundaries](Data-terminology-boundaries.png) |
| [domain-authority-map.dot](Domain-authority-map.dot) | MVP core / cross-cutting| [SVG](Domain-authority-map.svg) · ![domain authority map](Domain-authority-map.png) |
| [domain-constraint-review.puml](Domain-constraint-review.puml) | Method / document navigation| [SVG](Domain-constraint-review.svg) · ![domain constraint review](Domain-constraint-review.png) |
| [elicitation-log-provenance.dot](Elicitation-log-provenance.dot) | Method / document navigation| [SVG](Elicitation-log-provenance.svg) · ![elicitation log provenance](Elicitation-log-provenance.png) |
| [elicitation-log-recording-cycle.puml](Elicitation-log-recording-cycle.puml) | Method / document navigation| [SVG](Elicitation-log-recording-cycle.svg) · ![elicitation log recording cycle](Elicitation-log-recording-cycle.png) |
| [elicitation-plan-roadmap.puml](Elicitation-plan-roadmap.puml) | Method / document navigation| [SVG](Elicitation-plan-roadmap.svg) · ![elicitation plan roadmap](Elicitation-plan-roadmap.png) |
| [elicitation-source-map.dot](Elicitation-source-map.dot) | Method / document navigation| [SVG](Elicitation-source-map.svg) · ![elicitation source map](Elicitation-source-map.png) |
| [elicitation-technique-selection.dot](Elicitation-technique-selection.dot) | Method / document navigation| [SVG](Elicitation-technique-selection.svg) · ![elicitation technique selection](Elicitation-technique-selection.png) |
| [elicitation-working-cycle.puml](Elicitation-working-cycle.puml) | Method / document navigation| [SVG](Elicitation-working-cycle.svg) · ![elicitation working cycle](Elicitation-working-cycle.png) |
| [external-interface-context.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.svg) · ![logical component ownership](../../Design-assets/Archived-png/Logical-component-ownership.png) |
| [external-interface-outcomes.puml](External-interface-outcomes.puml) | MVP core / cross-cutting| [SVG](External-interface-outcomes.svg) · ![external interface outcomes](External-interface-outcomes.png) |
| [feasibility-assessment-map.dot](Feasibility-assessment-map.dot) | Mixed MVP / future| [SVG](Feasibility-assessment-map.svg) · ![feasibility assessment map](Feasibility-assessment-map.png) |
| [feasibility-review-flow.puml](Feasibility-review-flow.puml) | Method / document navigation| [SVG](Feasibility-review-flow.svg) · ![feasibility review flow](Feasibility-review-flow.png) |
| [git-hosting-capability-map.dot](Git-hosting-capability-map.dot) | Mixed MVP / future| [SVG](Git-hosting-capability-map.svg) · ![git hosting capability map](Git-hosting-capability-map.png) |
| [git-review-merge-flow.puml](Git-review-merge-flow.puml) | Future after MVP| [SVG](Git-review-merge-flow.svg) · ![git review merge flow](Git-review-merge-flow.png) |
| [google-integration-context.dot](Google-integration-context.dot) | Future communications| [SVG](Google-integration-context.svg) · ![google integration context](Google-integration-context.png) |
| [google-operation-outcomes.puml](Google-operation-outcomes.puml) | Future after MVP| [SVG](Google-operation-outcomes.svg) · ![google operation outcomes](Google-operation-outcomes.png) |
| [kanban-sprint-concept-map.dot](Kanban-sprint-concept-map.dot) | Future after MVP| [SVG](Kanban-sprint-concept-map.svg) · ![kanban sprint concept map](Kanban-sprint-concept-map.png) |
| [manual-application-history-map.dot](Manual-application-history-map.dot) | Method / document navigation| [SVG](Manual-application-history-map.svg) · ![manual application history map](Manual-application-history-map.png) |
| [pdf-protected-retrieval.puml](Pdf-protected-retrieval.puml) | MVP core / cross-cutting| [SVG](Pdf-protected-retrieval.svg) · ![pdf protected retrieval](Pdf-protected-retrieval.png) |
| [pdf-sharing-boundaries.dot](Pdf-sharing-boundaries.dot) | MVP core / cross-cutting| [SVG](Pdf-sharing-boundaries.svg) · ![pdf sharing boundaries](Pdf-sharing-boundaries.png) |
| [profile-resume-evidence-map.dot](Profile-resume-evidence-map.dot) | Method / document navigation| [SVG](Profile-resume-evidence-map.svg) · ![profile resume evidence map](Profile-resume-evidence-map.png) |
| [profile-update-review.puml](Profile-update-review.puml) | MVP core / cross-cutting| [SVG](Profile-update-review.svg) · ![profile update review](Profile-update-review.png) |
| [protected-sharing-sequence.puml](Protected-sharing-sequence.puml) | MVP core / cross-cutting| [SVG](Protected-sharing-sequence.svg) · ![protected sharing sequence](Protected-sharing-sequence.png) |
| [quality-evidence-map.dot](Quality-evidence-map.dot) | Method / document navigation| [SVG](Quality-evidence-map.svg) · ![quality evidence map](Quality-evidence-map.png) |
| [recovery-evidence-roadmap.puml](Recovery-evidence-roadmap.puml) | MVP core / cross-cutting| [SVG](Recovery-evidence-roadmap.svg) · ![recovery evidence roadmap](Recovery-evidence-roadmap.png) |
| [requirements-analysis-map.dot](Requirements-analysis-map.dot) | Method / document navigation| [SVG](Requirements-analysis-map.svg) · ![requirements analysis map](Requirements-analysis-map.png) |
| [requirements-approach-cycle.puml](Requirements-approach-cycle.puml) | Method / document navigation| [SVG](Requirements-approach-cycle.svg) · ![requirements approach cycle](Requirements-approach-cycle.png) |
| [requirements-approach-roadmap.dot](Requirements-approach-roadmap.dot) | Method / document navigation| [SVG](Requirements-approach-roadmap.svg) · ![requirements approach roadmap](Requirements-approach-roadmap.png) |
| [requirements-baseline-gates.puml](Requirements-baseline-gates.puml) | Method / document navigation| [SVG](Requirements-baseline-gates.svg) · ![requirements baseline gates](Requirements-baseline-gates.png) |
| [requirements-change-flow.puml](Requirements-change-flow.puml) | Method / document navigation| [SVG](Requirements-change-flow.svg) · ![requirements change flow](Requirements-change-flow.png) |
| [requirements-document-map.dot](Requirements-document-map.dot) | Method / document navigation| [SVG](Requirements-document-map.svg) · ![requirements document map](Requirements-document-map.png) |
| [requirements-management-change-cycle.puml](Requirements-management-change-cycle.puml) | Method / document navigation| [SVG](Requirements-management-change-cycle.svg) · ![requirements management change cycle](Requirements-management-change-cycle.png) |
| [requirements-management-traceability.dot](Requirements-management-traceability.dot) | Method / document navigation| [SVG](Requirements-management-traceability.svg) · ![requirements management traceability](Requirements-management-traceability.png) |
| [requirements-negotiation-flow.puml](Requirements-negotiation-flow.puml) | Method / document navigation| [SVG](Requirements-negotiation-flow.svg) · ![requirements negotiation flow](Requirements-negotiation-flow.png) |
| [requirements-process-overview.dot](Requirements-process-overview.dot) | Method / document navigation| [SVG](Requirements-process-overview.svg) · ![requirements process overview](Requirements-process-overview.png) |
| [requirements-question-map.dot](Requirements-question-map.dot) | Method / document navigation| [SVG](Requirements-question-map.svg) · ![requirements question map](Requirements-question-map.png) |
| [requirements-review-flow.puml](Requirements-review-flow.puml) | Method / document navigation| [SVG](Requirements-review-flow.svg) · ![requirements review flow](Requirements-review-flow.png) |
| [requirements-specification-cycle.puml](Requirements-specification-cycle.puml) | Method / document navigation| [SVG](Requirements-specification-cycle.svg) · ![requirements specification cycle](Requirements-specification-cycle.png) |
| [requirements-specification-map.dot](Requirements-specification-map.dot) | Method / document navigation| [SVG](Requirements-specification-map.svg) · ![requirements specification map](Requirements-specification-map.png) |
| [requirements-vv-perspectives.dot](Requirements-vv-perspectives.dot) | Method / document navigation| [SVG](Requirements-vv-perspectives.svg) · ![requirements vv perspectives](Requirements-vv-perspectives.png) |
| [requirements-vv-review-cycle.puml](Requirements-vv-review-cycle.puml) | Method / document navigation| [SVG](Requirements-vv-review-cycle.svg) · ![requirements vv review cycle](Requirements-vv-review-cycle.png) |
| [review-finding-disposition.puml](Review-finding-disposition.puml) | MVP core / cross-cutting| [SVG](Review-finding-disposition.svg) · ![review finding disposition](Review-finding-disposition.png) |
| [scenario-refinement-map.dot](Scenario-refinement-map.dot) | Method / document navigation| [SVG](Scenario-refinement-map.svg) · ![scenario refinement map](Scenario-refinement-map.png) |
| [specification-baseline-review.puml](Specification-baseline-review.puml) | Method / document navigation| [SVG](Specification-baseline-review.svg) · ![specification baseline review](Specification-baseline-review.png) |
| [specification-reading-map.dot](Specification-reading-map.dot) | Method / document navigation| [SVG](Specification-reading-map.svg) · ![specification reading map](Specification-reading-map.png) |
| [sprint-planning-review-flow.puml](Sprint-planning-review-flow.puml) | Method / document navigation| [SVG](Sprint-planning-review-flow.svg) · ![sprint planning review flow](Sprint-planning-review-flow.png) |
| [srs-baseline-decision.puml](Srs-baseline-decision.puml) | Method / document navigation| [SVG](Srs-baseline-decision.svg) · ![srs baseline decision](Srs-baseline-decision.png) |
| [srs-traceability-map.dot](Srs-traceability-map.dot) | Method / document navigation| [SVG](Srs-traceability-map.svg) · ![srs traceability map](Srs-traceability-map.png) |
| [stakeholders-elicitation-overview.dot](Stakeholders-elicitation-overview.dot) | Method / document navigation| [SVG](Stakeholders-elicitation-overview.svg) · ![stakeholders elicitation overview](Stakeholders-elicitation-overview.png) |
| [story-scenario-relationships.dot](Story-scenario-relationships.dot) | Method / document navigation| [SVG](Story-scenario-relationships.svg) · ![story scenario relationships](Story-scenario-relationships.png) |
| [submission-history-scenario.puml](Submission-history-scenario.puml) | Method / document navigation| [SVG](Submission-history-scenario.svg) · ![submission history scenario](Submission-history-scenario.png) |
| [template-readiness-flow.puml](Template-readiness-flow.puml) | Method / document navigation| [SVG](Template-readiness-flow.svg) · ![template readiness flow](Template-readiness-flow.png) |
| [template-record-relationships.dot](Template-record-relationships.dot) | Method / document navigation| [SVG](Template-record-relationships.svg) · ![template record relationships](Template-record-relationships.png) |
| [traceability-evidence-map.dot](Traceability-evidence-map.dot) | Method / document navigation| [SVG](Traceability-evidence-map.svg) · ![traceability evidence map](Traceability-evidence-map.png) |
| [use-cases-administration.puml](Use-cases-administration.puml) | MVP core / cross-cutting| [SVG](Use-cases-administration.svg) · ![use cases administration](Use-cases-administration.png) |
| [use-cases-execution-and-deployment.puml](Use-cases-execution-and-deployment.puml) | Future after MVP| [SVG](Use-cases-execution-and-deployment.svg) · ![use cases execution and deployment](Use-cases-execution-and-deployment.png) |
| [use-cases-git-collaboration.puml](Use-cases-git-collaboration.puml) | Mixed MVP / future| [SVG](Use-cases-git-collaboration.svg) · ![use cases git collaboration](Use-cases-git-collaboration.png) |
| [use-cases-mail-and-calendar.puml](Use-cases-mail-and-calendar.puml) | Future communications| [SVG](Use-cases-mail-and-calendar.svg) · ![use cases mail and calendar](Use-cases-mail-and-calendar.png) |
| [use-cases-work-and-sprints.puml](Use-cases-work-and-sprints.puml) | Future after MVP| [SVG](Use-cases-work-and-sprints.svg) · ![use cases work and sprints](Use-cases-work-and-sprints.png) |
| [user-goal-map.dot](User-goal-map.dot) | MVP core / cross-cutting| [SVG](User-goal-map.svg) · ![user goal map](User-goal-map.png) |
| [user-requirement-review.puml](User-requirement-review.puml) | Method / document navigation| [SVG](User-requirement-review.svg) · ![user requirement review](User-requirement-review.png) |
| [validation-traceability-roadmap.dot](Validation-traceability-roadmap.dot) | Method / document navigation| [SVG](Validation-traceability-roadmap.svg) · ![validation traceability roadmap](Validation-traceability-roadmap.png) |
| [workflow-execution-boundaries.dot](Workflow-execution-boundaries.dot) | Future after MVP| [SVG](Workflow-execution-boundaries.svg) · ![workflow execution boundaries](Workflow-execution-boundaries.png) |
| [workflow-run-control-flow.puml](Workflow-run-control-flow.puml) | Future after MVP| [SVG](Workflow-run-control-flow.svg) · ![workflow run control flow](Workflow-run-control-flow.png) |

# Requirements Diagrams

Current MVP scope and selected mechanisms: [Baseline](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/README.md). Deferred provider, advanced collaboration and workflow-execution designs are not MVP prerequisites.

## November 4 release applicability

Current MVP figures replace the former common-product boundary. Future and historical figures retain their details without committing them to MVP.

| Editable source | Current applicability |
| --- | --- |
| [actors-system-context.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot) | MVP core / cross-cutting|
| [external-interface-context.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot) | MVP core / cross-cutting|
| [git-hosting-capability-map.dot](Git-Hosting-Capability-Map.dot) | Mixed MVP / future|
| [git-review-merge-flow.puml](Git-Review-Merge-Flow.puml) | Future after MVP|
| [google-integration-context.dot](Google-Integration-Context.dot) | Future communications|
| [google-operation-outcomes.puml](Google-Operation-Outcomes.puml) | Future after MVP|
| [kanban-sprint-concept-map.dot](Kanban-Sprint-Concept-Map.dot) | Future after MVP|
| [pdf-sharing-boundaries.dot](Pdf-Sharing-Boundaries.dot) | MVP core / cross-cutting|
| [sprint-planning-review-flow.puml](Sprint-Planning-Review-Flow.puml) | Method / document navigation|
| [use-cases-execution-and-deployment.puml](Use-Cases-Execution-And-Deployment.puml) | Future after MVP|
| [use-cases-mail-and-calendar.puml](Use-Cases-Mail-And-Calendar.puml) | Future communications|
| [use-cases-work-and-sprints.puml](Use-Cases-Work-And-Sprints.puml) | Future after MVP|
| [workflow-execution-boundaries.dot](Workflow-Execution-Boundaries.dot) | Future after MVP|
| [workflow-run-control-flow.puml](Workflow-Run-Control-Flow.puml) | Future after MVP|

## Complete diagram alignment — November 4

[Full project inventory and verification limits](../../04-System-Design/01-High-Level-Design/14-Appendices.md#design-record-01-software-architecture-diagrams-diagram-catalog-md). This current disposition supersedes earlier partial diagram-allocation lists.

| Editable source or visual | Current applicability | Matching exports |
| --- | --- | --- |
| [accounts-access-contexts.dot](Accounts-Access-Contexts.dot) | MVP core / cross-cutting| [SVG](Accounts-Access-Contexts.svg) · ![accounts access contexts](Accounts-Access-Contexts.png) |
| [accounts-request-authorization.puml](Accounts-Request-Authorization.puml) | MVP core / cross-cutting| [SVG](Accounts-Request-Authorization.svg) · ![accounts request authorization](Accounts-Request-Authorization.png) |
| [actors-goal-overview.puml](Actors-Goal-Overview.puml) | MVP actor goals| [SVG](Actors-Goal-Overview.svg) · ![actors goal overview](Actors-Goal-Overview.png) |
| [actors-system-context.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.svg) · ![logical component ownership](../../04-System-Design/Diagrams/Archived-Png/Logical-Component-Ownership.png) |
| [administration-file-admission-flow.puml](Administration-File-Admission-Flow.puml) | MVP core / cross-cutting| [SVG](Administration-File-Admission-Flow.svg) · ![administration file admission flow](Administration-File-Admission-Flow.png) |
| [administration-files-policy-map.dot](Administration-Files-Policy-Map.dot) | MVP core / cross-cutting| [SVG](Administration-Files-Policy-Map.svg) · ![administration files policy map](Administration-Files-Policy-Map.png) |
| [application-submission-capture.puml](Application-Submission-Capture.puml) | MVP core / cross-cutting| [SVG](Application-Submission-Capture.svg) · ![application submission capture](Application-Submission-Capture.png) |
| [business-outcome-assessment.puml](Business-Outcome-Assessment.puml) | MVP core / cross-cutting| [SVG](Business-Outcome-Assessment.svg) · ![business outcome assessment](Business-Outcome-Assessment.png) |
| [business-outcomes-map.dot](Business-Outcomes-Map.dot) | MVP core / cross-cutting| [SVG](Business-Outcomes-Map.svg) · ![business outcomes map](Business-Outcomes-Map.png) |
| [change-baseline-record-map.dot](Change-Baseline-Record-Map.dot) | Method / document navigation| [SVG](Change-Baseline-Record-Map.svg) · ![change baseline record map](Change-Baseline-Record-Map.png) |
| [data-definition-review-flow.puml](Data-Definition-Review-Flow.puml) | Method / document navigation| [SVG](Data-Definition-Review-Flow.svg) · ![data definition review flow](Data-Definition-Review-Flow.png) |
| [data-definitions-map.dot](Data-Definitions-Map.dot) | Mixed MVP / future| [SVG](Data-Definitions-Map.svg) · ![data definitions map](Data-Definitions-Map.png) |
| [data-lifecycle-boundaries.dot](Data-Lifecycle-Boundaries.dot) | MVP core / cross-cutting| [SVG](Data-Lifecycle-Boundaries.svg) · ![data lifecycle boundaries](Data-Lifecycle-Boundaries.png) |
| [data-retirement-review.puml](Data-Retirement-Review.puml) | MVP core / cross-cutting| [SVG](Data-Retirement-Review.svg) · ![data retirement review](Data-Retirement-Review.png) |
| [data-submission-boundaries.puml](Data-Submission-Boundaries.puml) | MVP core / cross-cutting| [SVG](Data-Submission-Boundaries.svg) · ![data submission boundaries](Data-Submission-Boundaries.png) |
| [data-terminology-boundaries.dot](Data-Terminology-Boundaries.dot) | Mixed MVP / future| [SVG](Data-Terminology-Boundaries.svg) · ![data terminology boundaries](Data-Terminology-Boundaries.png) |
| [domain-authority-map.dot](Domain-Authority-Map.dot) | MVP core / cross-cutting| [SVG](Domain-Authority-Map.svg) · ![domain authority map](Domain-Authority-Map.png) |
| [domain-constraint-review.puml](Domain-Constraint-Review.puml) | Method / document navigation| [SVG](Domain-Constraint-Review.svg) · ![domain constraint review](Domain-Constraint-Review.png) |
| [elicitation-log-provenance.dot](Elicitation-Log-Provenance.dot) | Method / document navigation| [SVG](Elicitation-Log-Provenance.svg) · ![elicitation log provenance](Elicitation-Log-Provenance.png) |
| [elicitation-log-recording-cycle.puml](Elicitation-Log-Recording-Cycle.puml) | Method / document navigation| [SVG](Elicitation-Log-Recording-Cycle.svg) · ![elicitation log recording cycle](Elicitation-Log-Recording-Cycle.png) |
| [elicitation-plan-roadmap.puml](Elicitation-Plan-Roadmap.puml) | Method / document navigation| [SVG](Elicitation-Plan-Roadmap.svg) · ![elicitation plan roadmap](Elicitation-Plan-Roadmap.png) |
| [elicitation-source-map.dot](Elicitation-Source-Map.dot) | Method / document navigation| [SVG](Elicitation-Source-Map.svg) · ![elicitation source map](Elicitation-Source-Map.png) |
| [elicitation-technique-selection.dot](Elicitation-Technique-Selection.dot) | Method / document navigation| [SVG](Elicitation-Technique-Selection.svg) · ![elicitation technique selection](Elicitation-Technique-Selection.png) |
| [elicitation-working-cycle.puml](Elicitation-Working-Cycle.puml) | Method / document navigation| [SVG](Elicitation-Working-Cycle.svg) · ![elicitation working cycle](Elicitation-Working-Cycle.png) |
| [external-interface-context.dot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot) | MVP core / cross-cutting| [SVG](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/01-software-architecture/diagrams/logical-component-ownership.svg) · ![logical component ownership](../../04-System-Design/Diagrams/Archived-Png/Logical-Component-Ownership.png) |
| [external-interface-outcomes.puml](External-Interface-Outcomes.puml) | MVP core / cross-cutting| [SVG](External-Interface-Outcomes.svg) · ![external interface outcomes](External-Interface-Outcomes.png) |
| [feasibility-assessment-map.dot](Feasibility-Assessment-Map.dot) | Mixed MVP / future| [SVG](Feasibility-Assessment-Map.svg) · ![feasibility assessment map](Feasibility-Assessment-Map.png) |
| [feasibility-review-flow.puml](Feasibility-Review-Flow.puml) | Method / document navigation| [SVG](Feasibility-Review-Flow.svg) · ![feasibility review flow](Feasibility-Review-Flow.png) |
| [git-hosting-capability-map.dot](Git-Hosting-Capability-Map.dot) | Mixed MVP / future| [SVG](Git-Hosting-Capability-Map.svg) · ![git hosting capability map](Git-Hosting-Capability-Map.png) |
| [git-review-merge-flow.puml](Git-Review-Merge-Flow.puml) | Future after MVP| [SVG](Git-Review-Merge-Flow.svg) · ![git review merge flow](Git-Review-Merge-Flow.png) |
| [google-integration-context.dot](Google-Integration-Context.dot) | Future communications| [SVG](Google-Integration-Context.svg) · ![google integration context](Google-Integration-Context.png) |
| [google-operation-outcomes.puml](Google-Operation-Outcomes.puml) | Future after MVP| [SVG](Google-Operation-Outcomes.svg) · ![google operation outcomes](Google-Operation-Outcomes.png) |
| [kanban-sprint-concept-map.dot](Kanban-Sprint-Concept-Map.dot) | Future after MVP| [SVG](Kanban-Sprint-Concept-Map.svg) · ![kanban sprint concept map](Kanban-Sprint-Concept-Map.png) |
| [manual-application-history-map.dot](Manual-Application-History-Map.dot) | Method / document navigation| [SVG](Manual-Application-History-Map.svg) · ![manual application history map](Manual-Application-History-Map.png) |
| [pdf-protected-retrieval.puml](Pdf-Protected-Retrieval.puml) | MVP core / cross-cutting| [SVG](Pdf-Protected-Retrieval.svg) · ![pdf protected retrieval](Pdf-Protected-Retrieval.png) |
| [pdf-sharing-boundaries.dot](Pdf-Sharing-Boundaries.dot) | MVP core / cross-cutting| [SVG](Pdf-Sharing-Boundaries.svg) · ![pdf sharing boundaries](Pdf-Sharing-Boundaries.png) |
| [profile-resume-evidence-map.dot](Profile-Resume-Evidence-Map.dot) | Method / document navigation| [SVG](Profile-Resume-Evidence-Map.svg) · ![profile resume evidence map](Profile-Resume-Evidence-Map.png) |
| [profile-update-review.puml](Profile-Update-Review.puml) | MVP core / cross-cutting| [SVG](Profile-Update-Review.svg) · ![profile update review](Profile-Update-Review.png) |
| [protected-sharing-sequence.puml](Protected-Sharing-Sequence.puml) | MVP core / cross-cutting| [SVG](Protected-Sharing-Sequence.svg) · ![protected sharing sequence](Protected-Sharing-Sequence.png) |
| [quality-evidence-map.dot](Quality-Evidence-Map.dot) | Method / document navigation| [SVG](Quality-Evidence-Map.svg) · ![quality evidence map](Quality-Evidence-Map.png) |
| [recovery-evidence-roadmap.puml](Recovery-Evidence-Roadmap.puml) | MVP core / cross-cutting| [SVG](Recovery-Evidence-Roadmap.svg) · ![recovery evidence roadmap](Recovery-Evidence-Roadmap.png) |
| [requirements-analysis-map.dot](Requirements-Analysis-Map.dot) | Method / document navigation| [SVG](Requirements-Analysis-Map.svg) · ![requirements analysis map](Requirements-Analysis-Map.png) |
| [requirements-approach-cycle.puml](Requirements-Approach-Cycle.puml) | Method / document navigation| [SVG](Requirements-Approach-Cycle.svg) · ![requirements approach cycle](Requirements-Approach-Cycle.png) |
| [requirements-approach-roadmap.dot](Requirements-Approach-Roadmap.dot) | Method / document navigation| [SVG](Requirements-Approach-Roadmap.svg) · ![requirements approach roadmap](Requirements-Approach-Roadmap.png) |
| [requirements-baseline-gates.puml](Requirements-Baseline-Gates.puml) | Method / document navigation| [SVG](Requirements-Baseline-Gates.svg) · ![requirements baseline gates](Requirements-Baseline-Gates.png) |
| [requirements-change-flow.puml](Requirements-Change-Flow.puml) | Method / document navigation| [SVG](Requirements-Change-Flow.svg) · ![requirements change flow](Requirements-Change-Flow.png) |
| [requirements-document-map.dot](Requirements-Document-Map.dot) | Method / document navigation| [SVG](Requirements-Document-Map.svg) · ![requirements document map](Requirements-Document-Map.png) |
| [requirements-management-change-cycle.puml](Requirements-Management-Change-Cycle.puml) | Method / document navigation| [SVG](Requirements-Management-Change-Cycle.svg) · ![requirements management change cycle](Requirements-Management-Change-Cycle.png) |
| [requirements-management-traceability.dot](Requirements-Management-Traceability.dot) | Method / document navigation| [SVG](Requirements-Management-Traceability.svg) · ![requirements management traceability](Requirements-Management-Traceability.png) |
| [requirements-negotiation-flow.puml](Requirements-Negotiation-Flow.puml) | Method / document navigation| [SVG](Requirements-Negotiation-Flow.svg) · ![requirements negotiation flow](Requirements-Negotiation-Flow.png) |
| [requirements-process-overview.dot](Requirements-Process-Overview.dot) | Method / document navigation| [SVG](Requirements-Process-Overview.svg) · ![requirements process overview](Requirements-Process-Overview.png) |
| [requirements-question-map.dot](Requirements-Question-Map.dot) | Method / document navigation| [SVG](Requirements-Question-Map.svg) · ![requirements question map](Requirements-Question-Map.png) |
| [requirements-review-flow.puml](Requirements-Review-Flow.puml) | Method / document navigation| [SVG](Requirements-Review-Flow.svg) · ![requirements review flow](Requirements-Review-Flow.png) |
| [requirements-specification-cycle.puml](Requirements-Specification-Cycle.puml) | Method / document navigation| [SVG](Requirements-Specification-Cycle.svg) · ![requirements specification cycle](Requirements-Specification-Cycle.png) |
| [requirements-specification-map.dot](Requirements-Specification-Map.dot) | Method / document navigation| [SVG](Requirements-Specification-Map.svg) · ![requirements specification map](Requirements-Specification-Map.png) |
| [requirements-vv-perspectives.dot](Requirements-Vv-Perspectives.dot) | Method / document navigation| [SVG](Requirements-Vv-Perspectives.svg) · ![requirements vv perspectives](Requirements-Vv-Perspectives.png) |
| [requirements-vv-review-cycle.puml](Requirements-Vv-Review-Cycle.puml) | Method / document navigation| [SVG](Requirements-Vv-Review-Cycle.svg) · ![requirements vv review cycle](Requirements-Vv-Review-Cycle.png) |
| [review-finding-disposition.puml](Review-Finding-Disposition.puml) | MVP core / cross-cutting| [SVG](Review-Finding-Disposition.svg) · ![review finding disposition](Review-Finding-Disposition.png) |
| [scenario-refinement-map.dot](Scenario-Refinement-Map.dot) | Method / document navigation| [SVG](Scenario-Refinement-Map.svg) · ![scenario refinement map](Scenario-Refinement-Map.png) |
| [specification-baseline-review.puml](Specification-Baseline-Review.puml) | Method / document navigation| [SVG](Specification-Baseline-Review.svg) · ![specification baseline review](Specification-Baseline-Review.png) |
| [specification-reading-map.dot](Specification-Reading-Map.dot) | Method / document navigation| [SVG](Specification-Reading-Map.svg) · ![specification reading map](Specification-Reading-Map.png) |
| [sprint-planning-review-flow.puml](Sprint-Planning-Review-Flow.puml) | Method / document navigation| [SVG](Sprint-Planning-Review-Flow.svg) · ![sprint planning review flow](Sprint-Planning-Review-Flow.png) |
| [srs-baseline-decision.puml](Srs-Baseline-Decision.puml) | Method / document navigation| [SVG](Srs-Baseline-Decision.svg) · ![srs baseline decision](Srs-Baseline-Decision.png) |
| [srs-traceability-map.dot](Srs-Traceability-Map.dot) | Method / document navigation| [SVG](Srs-Traceability-Map.svg) · ![srs traceability map](Srs-Traceability-Map.png) |
| [stakeholders-elicitation-overview.dot](Stakeholders-Elicitation-Overview.dot) | Method / document navigation| [SVG](Stakeholders-Elicitation-Overview.svg) · ![stakeholders elicitation overview](Stakeholders-Elicitation-Overview.png) |
| [story-scenario-relationships.dot](Story-Scenario-Relationships.dot) | Method / document navigation| [SVG](Story-Scenario-Relationships.svg) · ![story scenario relationships](Story-Scenario-Relationships.png) |
| [submission-history-scenario.puml](Submission-History-Scenario.puml) | Method / document navigation| [SVG](Submission-History-Scenario.svg) · ![submission history scenario](Submission-History-Scenario.png) |
| [template-readiness-flow.puml](Template-Readiness-Flow.puml) | Method / document navigation| [SVG](Template-Readiness-Flow.svg) · ![template readiness flow](Template-Readiness-Flow.png) |
| [template-record-relationships.dot](Template-Record-Relationships.dot) | Method / document navigation| [SVG](Template-Record-Relationships.svg) · ![template record relationships](Template-Record-Relationships.png) |
| [traceability-evidence-map.dot](Traceability-Evidence-Map.dot) | Method / document navigation| [SVG](Traceability-Evidence-Map.svg) · ![traceability evidence map](Traceability-Evidence-Map.png) |
| [use-cases-administration.puml](Use-Cases-Administration.puml) | MVP core / cross-cutting| [SVG](Use-Cases-Administration.svg) · ![use cases administration](Use-Cases-Administration.png) |
| [use-cases-execution-and-deployment.puml](Use-Cases-Execution-And-Deployment.puml) | Future after MVP| [SVG](Use-Cases-Execution-And-Deployment.svg) · ![use cases execution and deployment](Use-Cases-Execution-And-Deployment.png) |
| [use-cases-git-collaboration.puml](Use-Cases-Git-Collaboration.puml) | Mixed MVP / future| [SVG](Use-Cases-Git-Collaboration.svg) · ![use cases git collaboration](Use-Cases-Git-Collaboration.png) |
| [use-cases-mail-and-calendar.puml](Use-Cases-Mail-And-Calendar.puml) | Future communications| [SVG](Use-Cases-Mail-And-Calendar.svg) · ![use cases mail and calendar](Use-Cases-Mail-And-Calendar.png) |
| [use-cases-work-and-sprints.puml](Use-Cases-Work-And-Sprints.puml) | Future after MVP| [SVG](Use-Cases-Work-And-Sprints.svg) · ![use cases work and sprints](Use-Cases-Work-And-Sprints.png) |
| [user-goal-map.dot](User-Goal-Map.dot) | MVP core / cross-cutting| [SVG](User-Goal-Map.svg) · ![user goal map](User-Goal-Map.png) |
| [user-requirement-review.puml](User-Requirement-Review.puml) | Method / document navigation| [SVG](User-Requirement-Review.svg) · ![user requirement review](User-Requirement-Review.png) |
| [validation-traceability-roadmap.dot](Validation-Traceability-Roadmap.dot) | Method / document navigation| [SVG](Validation-Traceability-Roadmap.svg) · ![validation traceability roadmap](Validation-Traceability-Roadmap.png) |
| [workflow-execution-boundaries.dot](Workflow-Execution-Boundaries.dot) | Future after MVP| [SVG](Workflow-Execution-Boundaries.svg) · ![workflow execution boundaries](Workflow-Execution-Boundaries.png) |
| [workflow-run-control-flow.puml](Workflow-Run-Control-Flow.puml) | Future after MVP| [SVG](Workflow-Run-Control-Flow.svg) · ![workflow run control flow](Workflow-Run-Control-Flow.png) |

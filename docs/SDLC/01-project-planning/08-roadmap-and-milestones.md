# Roadmap and Milestones

Status: Reviewed - roadmap definitions and planning methods accepted; schedule reconciliation and milestone completion pending

## 1. Delivery Approach

Develop the product incrementally through reviewable outcomes.
Each increment includes relevant requirements, design,
implementation, verification, and documentation.

The sequence below is provisional. Technical findings may
change the order without automatically changing version 1 scope.

Testing begins with requirements review and continues
through development, deployment, and maintenance.

## 2. Proposed Milestones

| ID | Milestone | Reviewable outcome | Main dependencies |
|---|---|---|---|
| M-01 | Planning baseline | Planning documents reviewed; significant unknowns have owners and review points | Planning completion criteria |
| M-02 | Requirements baseline | Version 1 workflows, permissions, lifecycle rules, and acceptance criteria reviewed | M-01; stakeholder input |
| M-03 | Feasibility and design baseline | Architecture and delivery approach justified against resources, integrations, security, and recovery needs | Relevant requirements; resource and dependency investigations |
| M-04 | Application foundation | Identity, permissions, navigation, and application structure verified | Relevant M-02 and M-03 outcomes |
| M-05 | Professional presentation | Profiles, resumes, portfolio, media, PDF, and controlled sharing workflows verified | Foundation; file and data lifecycle decisions |
| M-06 | Manual application management | Manual ApplyFlow, email, and calendar workflows verified together | Foundation; resume workflows; integration validation |
| M-07 | Work and collaboration | Kanban, collaboration, and agreed Git Forge workflows verified | Foundation; permission model; Git feasibility |
| M-08 | CI/CD capability | Agreed YAML workflows execute with verified isolation, permissions, secret handling, and resource limits | Git workflows; early CI/CD feasibility and security investigation |
| M-09 | Integrated release candidate | Cross-module workflows and agreed quality targets verified; operating guides and restoration evidence available | All version 1 capability milestones |
| M-10 | Initial deployment and handover | Identified release deployed; smoke checks completed; operating responsibilities and release decision recorded | M-09; deployment readiness |

Milestones describe outcomes, not fixed-length work periods.
A milestone may require several sprints.
A sprint may contribute to more than one milestone.

## 3. Early Investigations

Do not postpone high-impact feasibility questions until
the corresponding feature is due for implementation.

Investigate early:
- Existing server capacity and competing workloads.
- Safe Git CI/CD execution within available resources.
- Required Google integration access and operations.
- Email delivery arrangements.
- Backup storage and restoration options.

Use ASM, DEP, and RSK identifiers to connect findings
to assumptions, dependencies, and the risk register.

## 4. Estimates and Scheduling

The project owner requests full Version 1 delivery by November 8, 2026 (Europe/Berlin). Three dated sprint cycles are recorded provisionally and require reconciliation after analysis and design. Effort estimates and schedule feasibility remain unresolved.

Before committing to delivery dates:
- Establish available development hours.
- Break milestone outcomes into estimable work.
- Identify dependencies and unresolved investigations.
- Include learning, verification, documentation, and rework.
- Review estimates against demonstrated progress.

Record estimates as ranges where uncertainty remains.
Document the basis for significant estimates and revisions.

## 5. Milestone Reviews

For each milestone, record:
- The outcome and agreed completion conditions.
- Related requirements and deliverables.
- The reviewed version or document revision.
- Verification evidence and known limitations.
- Open risks, issues, and follow-up actions.
- The project owner's review decision.

Current status: M-01 is accepted with tracked follow-up under [DEC-116](10-planning-completion-criteria.md#dec-116); M-02 through M-10 completion decisions remain pending.
Existing planning drafts do not establish completion of M-01.

## 6. Scope and Change

Incremental delivery does not remove agreed version 1 scope.
AI remains outside version 1.

Changes affecting scope, cost, quality commitments, or
delivery expectations must be assessed and recorded.

## 7. References

- [Scope](02-scope.md)
- [Deliverables](04-deliverables.md)
- [Resources and Constraints](05-resources-and-constraints.md)
- [Assumptions and Dependencies](06-assumptions-and-dependencies.md)
- [Risk Register](07-risks.md)
- [Planning Completion Criteria](10-planning-completion-criteria.md)


## 8. Target Delivery Checkpoints

[Delivery plan](../../Project-Management/version-1-delivery-plan.md) | [Product backlog](../../Project-Management/product-backlog.md)

| Milestone | Target date (Europe/Berlin) |
|---|---|
| M-01 - Planning baseline | 2026-10-30 |
| M-02 - Requirements baseline | 2026-10-31 |
| M-03 - Feasibility and design baseline | 2026-11-01 |
| M-04 - Application foundation | 2026-11-01 |
| M-05 - Professional presentation | 2026-11-03 |
| M-06 - Manual application management | 2026-11-04 |
| M-07 - Work and collaboration | 2026-11-05 |
| M-08 - CI/CD capability | 2026-11-06 |
| M-09 - Integrated release candidate | 2026-11-07 |
| M-10 - Initial deployment and handover | 2026-11-08 |

Dates are requested delivery targets, not evidence of feasibility or completion.

## Roadmap Review Decisions

### Outcome-Based Roadmap and Provisional Scheduling Review

Decision ID: DEC-089
<a id="dec-089"></a>

Status: Roadmap approach accepted by the project owner;
individual milestone definitions accepted in the records below; schedule revision remains pending
Review date: October 31, 2026

Decision: Define milestones by reviewable outcomes and completion
evidence rather than only dates or task counts. For example, a
requirements baseline requires reviewed requirements and explicit
acceptance criteria; document existence alone is insufficient.

Retain the existing target dates and Sprint assignments as provisional
planning records. After the agreed analysis and design work, reconcile
the product backlog, Sprint backlogs, milestones, effort estimates,
and delivery forecasts against the reviewed documentation and baseline.
Record reasons and impacts for material revisions.

Rationale: Ground sequencing and delivery expectations in actual
scope, dependencies, risks, and evidence while supporting iterative
review and incremental delivery. Do not silently remove agreed
capabilities to preserve an earlier target.

Preserve the agreed documentation-first sequence before product
implementation. This record does not revise live GitHub dates,
accept any milestone as complete, validate the requested deadline,
or approve the overall planning baseline.

### M-01 Planning Baseline Review

Decision ID: DEC-088
<a id="dec-088"></a>

Status: Milestone definition and completion criteria accepted by the project owner; milestone completion remains pending
Review date: October 31, 2026

Decision: Complete M-01 when all ten planning documents have been reviewed, the planning decisions are explicit, and significant open matters have an identified owner and review point. Assess completion against the planning completion criteria; file existence alone is insufficient.

Technical investigations may remain open where their findings are not required to accept the planning baseline, provided they are tracked and must be reviewed before the dependent commitment. An unresolved matter that prevents a sound planning agreement must be addressed before accepting M-01.

The baseline identifies a specific agreed revision. Subsequent revisions remain possible, with the reason for change and its effects recorded and reviewed.

Rationale: Establish a traceable planning agreement without presenting unresolved technical assumptions as verified facts or preventing iterative improvement.

Acceptance of this definition does not mark M-01 complete. Review of the remaining planning documents is still in progress, and this milestone does not authorize product implementation.

### M-02 Requirements Baseline Review

Decision ID: DEC-087
<a id="dec-087"></a>

Status: Milestone definition and completion criteria accepted by the project owner; milestone completion remains pending
Review date: October 31, 2026

Decision: Complete M-02 when the agreed Version 1 requirements have identifiers, scenarios, relevant access rules, and testable acceptance criteria, and have been reviewed by the project owner. Resolve ambiguities that would prevent agreement on expected behavior. Track other open matters with an owner and review point before dependent commitments.

For example, password-protected sharing requirements must specify authorized content, behavior for an incorrect password, and the effect of disabling a link. This example identifies matters to specify during Requirements Engineering; it does not replace the detailed requirements.

Identify the agreed requirements revision as the baseline. Record and review subsequent changes and their effects on related analysis, design, tests, and delivery planning.

Rationale: Give system analysis, design, and verification a clear, traceable statement of expected behavior instead of relying on assumptions or feature names alone.

Acceptance of this milestone definition does not establish the requirements baseline or mark M-02 complete. Detailed Requirements Engineering and its review remain pending.

### M-03 Feasibility and Design Baseline Review

Decision ID: DEC-086
<a id="dec-086"></a>

Status: Milestone definition and completion criteria accepted by the project owner; milestone completion remains pending
Review date: October 31, 2026

Decision: Complete M-03 when the architecture, data model, module interactions, access boundaries, deployment approach, recovery approach, and CI/CD execution isolation have been defined and reviewed against the agreed requirements and actual project resources. Include explanatory text and consistent diagrams with editable sources and rendered outputs. Document alternatives considered, selection rationale, constraints, and significant consequences.

Obtain findings for investigations that determine the feasibility of the dependent design before accepting that design, including relevant server resources and external service access. Track remaining open matters with an owner and review point. An unresolved issue that prevents a justified feasibility or design decision must be addressed before accepting the affected baseline.

Identify the agreed design revision and its supporting evidence. Record and review subsequent changes and their effects on requirements, diagrams, implementation planning, verification, deployment, and recovery documentation as applicable.

Rationale: Establish a design that covers the agreed requirements and can be supported by actual resources, rather than treating an architectural preference or an unverified technical assumption as proof of feasibility.

Acceptance of this milestone definition does not select a final architecture, verify technical capacity or integrations, mark M-03 complete, or authorize product implementation. The agreed documentation and baseline review sequence remains in effect.

### M-04 Application Foundation Review

Decision ID: DEC-085
<a id="dec-085"></a>

Status: Milestone definition and completion criteria accepted by the project owner; milestone completion remains pending
Review date: October 31, 2026

Decision: Define M-04 as the implemented and verified application foundation: user accounts, sign-in and sign-out, roles and permissions, the initial application structure, and consistent navigation between modules with unified sign-in. Detailed behavior must follow the reviewed requirements and design.

Complete this milestone when the agreed foundation capabilities operate in an identified application revision and verification results demonstrate the expected behavior, including denial of unauthorized access to information and operations. Link the verification evidence and remaining limitations to that revision. File or code existence alone is insufficient.

Rationale: Provide a shared, dependable foundation for subsequent capabilities, with identity and authorization established before dependent private workflows are accepted.

This acceptance defines a future delivery outcome. It does not claim implementation or verification has occurred, mark M-04 complete, or start product coding. Implementation remains subject to the agreed documentation-first sequence and baseline agreement.

### M-05 Professional Presentation Review

Decision ID: DEC-084
<a id="dec-084"></a>

Status: Milestone definition and completion criteria accepted by the project owner; milestone completion remains pending
Review date: October 31, 2026

Decision: Define M-05 as the implemented and verified professional presentation capabilities: professional profiles, opportunity-specific resumes, portfolio and supporting evidence, generated and uploaded PDFs, and password-protected sharing, within the agreed Version 1 scope.

Complete this milestone when an end-to-end workflow has been verified in an identified application revision: enter professional information, prepare a tailored resume, select permitted evidence and PDF downloads, and share the selected content with an employer. Verify independence of resume-specific settings, download authorization, and prevention of unauthorized access through direct file URLs against the reviewed requirements. Link actual results and remaining limitations to the application revision.

Rationale: Ensure these capabilities form a usable professional presentation workflow while preserving privacy and deliberate control over resume content and shared files.

Acceptance defines a future delivery outcome. It does not claim that implementation or verification has occurred, mark M-05 complete, or authorize product coding before the agreed documentation and baseline review sequence is complete.

### M-06 Manual Application Management Review

Decision ID: DEC-083
<a id="dec-083"></a>

Status: Milestone definition and completion criteria accepted by the project owner; milestone completion remains pending
Review date: October 31, 2026

Decision: Define M-06 as the implemented and verified manual job application management workflow, including associated email and calendar capabilities within the agreed Version 1 scope.

Complete this milestone when the connected workflow has been verified: record a company and opportunity, associate a resume, manually prepare a cover letter, record submission and application status, and follow up correspondence and interview dates. Preserve the actual submitted versions so subsequent resume edits do not alter the application history.

Verify Gmail and Google Calendar integrations against the reviewed requirements and validated provider access. Link actual verification results and remaining limitations to an identified application revision. Unavailable integration access is an unresolved dependency requiring an explicit decision, not evidence of milestone completion.

Rationale: Maintain a clear, traceable history for each application and coordinate related communications and deadlines while keeping content preparation and application decisions under user control.

Acceptance defines a future delivery outcome. It does not claim implementation, provider validation, or verification has occurred, mark M-06 complete, or authorize product coding before the agreed documentation and baseline review sequence is complete.

### M-07 Work and Collaboration Review

Decision ID: DEC-082
<a id="dec-082"></a>

Status: Milestone definition and completion criteria accepted by the project owner; milestone completion remains pending
Review date: October 31, 2026

Decision: Define M-07 as the implemented and verified work management and collaboration capabilities inside Resumefolio. Include projects, Kanban, product backlog items, Sprints, Sprint backlogs, and tasks in accordance with the reviewed requirements and agreed scope.

Complete this milestone when the agreed work management workflows and real Git hosting operations have been verified, including push and clone, branches, fork, pull requests, review and merge, issues, milestones, tags, and releases. Verify that collaborators can access only authorized resources and operations. Link actual results and remaining limitations to an identified application revision.

These product capabilities are distinct from the GitHub board used to manage development of Resumefolio. Workflow execution and CI/CD completion are assessed separately under M-08; this separation does not remove any agreed Git operations from Version 1.

Rationale: Provide traceable work planning and code collaboration within a consistent product environment while preserving resource-specific authorization boundaries.

Acceptance defines a future delivery outcome. It does not claim implementation or verification has occurred, mark M-07 complete, or authorize product coding before the agreed documentation and baseline review sequence is complete.

### M-08 CI/CD Capability Review

Decision ID: DEC-081
<a id="dec-081"></a>

Status: Milestone definition and completion criteria accepted by the project owner; milestone completion remains pending
Review date: October 31, 2026

Decision: Define M-08 as implemented and verified execution of real YAML workflows, including agreed triggers such as push, test and build execution, and reporting of results. Deployment stages must follow the reviewed authorization and approval rules.

Complete this milestone when the agreed workflow behavior and execution isolation, secret protection, permissions, and resource limits have been verified against the reviewed requirements and design. Link actual results, remaining limitations, and relevant unresolved risks to an identified application revision and execution environment.

Feasibility of the dependent execution and deployment design must have been investigated before accepting that design under M-03. The existence of YAML files or a successful build alone is insufficient evidence of M-08 completion.

Rationale: Make verification and release preparation repeatable while controlling the risks of executing project code on the available infrastructure.

Acceptance defines a future delivery outcome. It does not claim workflow execution or security verification has occurred, mark M-08 complete, or authorize product coding before the agreed documentation and baseline review sequence is complete.

### M-09 Integrated Release Candidate Review

Decision ID: DEC-080
<a id="dec-080"></a>

Status: Milestone definition and completion criteria accepted by the project owner; milestone completion remains pending
Review date: October 31, 2026

Decision: Define M-09 as an integrated, identified release candidate ready for release assessment. Complete it when connected cross-module workflows, authorization boundaries, and agreed quality criteria have been verified, and the relevant guides match that candidate revision.

Require evidence of actual backup restoration in a separate environment, including checks of restored data integrity. Link actual test results, defects, remaining risks, and recovery evidence to identified revisions and environments. Resolve release-blocking matters in accordance with the agreed acceptance and release criteria.

Rationale: Successful checks of individual components alone do not establish that the complete product works correctly across module boundaries or can be recovered after failure.

Acceptance defines a future delivery outcome. It does not claim integration testing or restoration has occurred, mark M-09 complete, approve production deployment, or authorize product coding before the agreed documentation and baseline review sequence is complete.

### M-10 Initial Deployment and Handover Review

Decision ID: DEC-079
<a id="dec-079"></a>

Status: Milestone definition and completion criteria accepted by the project owner; milestone completion remains pending
Review date: October 31, 2026

Decision: Define M-10 as deployment of an identified release to the target server and readiness for actual use and maintenance. Complete it when the release decision has been recorded against M-09 evidence, deployment has been performed, and the agreed initial checks in the live environment have passed with recorded results.

Ensure operating, update, rollback, backup, and maintenance guidance matches the deployed revision. Record the deployed version, environment, known limitations, and release decision without exposing secrets.

Handover means that the project owner, currently the sole person carrying out the project and its operations, can use and operate the product with the supporting guidance. Do not assume a separate delivery team or operations team.

Rationale: Deliver a product that is usable and maintainable in its actual environment, beyond merely having executable source code.

Acceptance defines a future delivery outcome. It does not claim deployment or live verification has occurred, mark M-10 complete, authorize deployment now, or authorize product coding before the agreed documentation and baseline review sequence is complete.

### Early Feasibility Investigations Review

Decision ID: DEC-078
<a id="dec-078"></a>

Status: Investigation approach accepted by the project owner; technical investigations remain pending
Review date: October 31, 2026

Decision: Investigate server capacity and competing workloads, CI/CD execution feasibility and isolation, required Google access, email delivery arrangements, and backup storage and restoration options before accepting dependent design decisions. Do not defer a decisive feasibility investigation until implementation of the affected capability is due.

Link findings and supporting evidence to the relevant ASM, DEP, and RSK identifiers. Record unresolved matters and their effects on dependent design and scheduling decisions.

Rationale: Prevent design and delivery commitments from relying on hidden or unvalidated assumptions, and expose constraints while meaningful design alternatives can still be evaluated.

Acceptance concerns the investigation approach. It does not claim these investigations have been performed or that technical feasibility has been established.

### Estimation and Scheduling Method Review

Decision ID: DEC-077
<a id="dec-077"></a>

Status: Estimation and scheduling method accepted by the project owner; effort estimates and schedule feasibility remain unresolved
Review date: October 31, 2026

Decision: After the agreed analysis and design work, divide delivery outcomes into estimable work and account for dependencies, learning, testing, documentation, and rework as well as implementation. Use estimate ranges where uncertainty remains, record the basis of significant estimates, and revise them against observed progress.

Retain November 8, 2026 as the requested delivery target. Existing Sprint and milestone dates remain provisional until reconciliation with the reviewed work and estimates. If the forecast conflicts with that target, explicitly document the conflict, options, and consequences for the project owner's decision without silently removing agreed scope or assuming additional spending.

Rationale: Base the delivery plan on the full engineering workload and actual progress, making uncertainty and conflicts visible rather than treating a requested date as a verified forecast.

Acceptance concerns the planning method. It does not validate the deadline, establish an effort estimate, or change live GitHub dates or Sprint assignments.

### Milestone Review Method Acceptance

Decision ID: DEC-076
<a id="dec-076"></a>

Status: Milestone review method accepted by the project owner; milestone completion decisions remain pending
Review date: October 31, 2026

Decision: For each milestone review, record the outcome and agreed completion criteria, related requirements and deliverables, the reviewed application version or document revision, actual supporting evidence, known limitations, and open risks, issues, and follow-up work. Record the project owner's decision to accept the outcome or require further work, with the basis for that decision.

Reaching a target date or finishing a number of tasks alone does not establish milestone completion. Acceptance of milestone definitions during planning is distinct from acceptance of completed outcomes.

Rationale: Make it possible to identify which outcome was accepted, in which revision, and on what evidence, while retaining visibility of remaining limitations and responsibilities.

This acceptance records the review method only. It does not mark any milestone complete or approve the overall planning baseline.

### Roadmap and Scope Change Review

Decision ID: DEC-075
<a id="dec-075"></a>

Status: Scope change rule accepted by the project owner
Review date: October 31, 2026

Decision: Incremental delivery and changes to work sequencing do not automatically remove agreed Version 1 capabilities. For changes affecting scope, cost, quality commitments, or delivery expectations, document the reasons, options, and consequences for the project owner's decision. AI capabilities remain outside Version 1 as agreed.

Rationale: Keep changes to delivery planning transparent and prevent the agreed product scope from changing without an explicit decision.

## Document Review Summary

Status: Roadmap definitions and planning methods reviewed and accepted; schedule reconciliation and milestone completion remain pending
Review date: October 31, 2026

The project owner has accepted the outcome-based roadmap approach, definitions and completion criteria for M-01 through M-10, early feasibility investigation approach, estimation and scheduling method, milestone review method, and scope change rule.

Existing dates and Sprint assignments remain provisional. Reconcile the backlog, Sprint backlogs, milestones, estimates, and forecasts after the agreed analysis and design work. This review does not validate the requested deadline, complete any milestone, approve the overall planning baseline, or authorize product coding. Technical findings and delivery evidence remain to be obtained in the relevant work.

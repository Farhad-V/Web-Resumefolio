# Working Method and Change Control

Status: Reviewed - working method and change control accepted

## 1. Working Agreement

The shared working agreement is maintained in
[Stakeholders and Responsibilities](03-stakeholders-and-responsibilities.md#73-working-agreement).

Continue step by step through PowerShell:
explain commands, inspect actual results, and review changes
before recording the next checkpoint.

## 2. Organizing Work

- Maintain product work in Project Management.
- Keep authoritative requirements, User Stories, Job Stories,
  scenarios, and Acceptance Criteria in Requirements Engineering.
- Link backlog items to the relevant requirements.
- Include defects, investigations, documentation, and
  technical work in the backlog where appropriate.
- Give work items an identifier, intended outcome,
  priority, status, and completion conditions.
- Link selected work to relevant milestones and risks.

The [Product Backlog](../../Project-Management/product-backlog.md) indexes
GitHub issues. GitHub issues and the private delivery board own live status,
priority, milestone and sprint assignment; avoid duplicate status tables.
The GitHub delivery project and linked issues are now configured.

## 3. Incremental Development

Select a manageable set of work with a clear outcome.
Review dependencies and unresolved questions before starting.

For each increment:
1. Clarify the relevant requirements and completion conditions.
2. Analyze and design the necessary behavior.
3. Implement the scoped change.
4. Perform appropriate verification.
5. Update affected documentation and diagrams.
6. Review results, limitations, and follow-up work.
7. Save a focused Git checkpoint.

These activities can repeat as findings emerge.
A successful commit or push does not establish feature completion.

## 4. Sprint Planning and Review

Three dated sprint backlogs are configured for October 29-November 8, 2026. See the [delivery plan](../../Project-Management/version-1-delivery-plan.md). Assignment does not establish verified capacity or feature completion.

When using sprints:
- Define a Sprint Goal.
- Select realistic work based on available time and dependencies.
- Maintain one Sprint Backlog for the sprint.
- Update tasks as understanding changes.
- Review the delivered outcome and verification evidence.
- Record lessons and improvements for the next sprint.

A milestone is an outcome checkpoint.
A sprint is a work period and may contribute to several outcomes.

## 5. Change Assessment

For a proposed change, record:
- The requested change and its reason.
- Affected requirements, documents, diagrams, and milestones.
- Expected effects on effort, cost, quality, and operations.
- Dependencies, risks, and available alternatives.
- The decision, decision-maker, date, and follow-up actions.

Changes to agreed scope, spending, or delivery commitments
require an explicit project-owner decision.

Routine corrections and implementation choices within the
agreed scope do not require a separate approval for every step.

## 6. Decision Records

Stable references to accepted planning decisions: [Planning Decision Register](decision-register.md).

Record significant decisions in the affected authoritative
document or a linked decision record.

Use a stable identifier such as DEC-001.
Distinguish proposed, accepted, rejected, and superseded decisions.

When a decision changes, preserve its history and explain
which earlier decision it supersedes.

Git records document changes. Commit history alone does not
replace the reason for a significant product or technical decision.

## 7. Completion and Review

Work is complete when its agreed conditions are satisfied
and supporting evidence is available.

Record incomplete checks, unresolved defects, and limitations.
Do not report unexecuted tests as successful.

Milestone and release decisions use the relevant completion
criteria and remain separate from routine Git checkpoints.

## 8. References

- [Stakeholders and Responsibilities](03-stakeholders-and-responsibilities.md)
- [Deliverables](04-deliverables.md)
- [Risk Register](07-risks.md)
- [Roadmap and Milestones](08-roadmap-and-milestones.md)

## 9. Confirmed Agile Direction

Decision ID: DEC-115
<a id="dec-115"></a>

Status: Iterative and incremental approach confirmed by the project owner
Review date: October 30, 2026

Use iterations for feedback, learning, and revision, and deliver
integrated, verified product increments during implementation.
Keep decision rationale and subsequent revisions documented.

The initial documentation-first review and agreed baseline precede
product coding. This is not a freeze on later changes: update
requirements, designs, tests, and delivery tracking as evidence emerges.
Agile does not imply additional staff, a guaranteed release date,
or automatic adoption of every Scrum ceremony.

Rationale: Support incremental progress and controlled adaptation
without abandoning traceability or the actual solo-delivery constraints.
The completed document review is recorded in the Document Review Summary below.

## Working Method Review Decisions

### Working Agreement Review

Decision ID: DEC-096
<a id="dec-096"></a>

Status: Working method accepted by the project owner
Review date: October 31, 2026

Decision: Proceed step by step through PowerShell. Explain the purpose of commands before execution, inspect actual results, and review changes before recording a Git checkpoint. Distinguish saved local changes from committed and pushed changes. Do not repeatedly request content approval for an accepted decision unless new information or a material proposed change requires further review.

Maintain consistency with the shared working agreement in the stakeholders and responsibilities document. Preserve the agreed documentation-first sequence and baseline agreement before product implementation.

Rationale: Keep the work understandable and traceable while preserving the project owner's control and avoiding redundant approval requests.

This acceptance records the working method; it does not establish completion of the remaining document review or approve the overall planning baseline.

### Work Organization Review

Decision ID: DEC-095
<a id="dec-095"></a>

Status: Work organization method accepted by the project owner
Review date: October 31, 2026

Decision: Maintain authoritative requirements, scenarios, and acceptance criteria in Requirements Engineering documentation, and link relevant backlog items to those definitions. Include defects, technical investigations, and documentation work in the backlog where appropriate.

Give each work item an identifier, intended outcome, priority, status, and completion conditions. Link relevant items to milestones and risks. Maintain live status and Sprint and milestone assignments in GitHub issues and the delivery project, using the repository product backlog as an index rather than maintaining competing live status tables.

Rationale: Distinguish the definition of expected product behavior from tracking its execution, preserve traceability between them, and avoid contradictory parallel records.

This acceptance defines the organization method. It does not claim that all existing items have been reconciled with future requirements or that the current Sprint assignments constitute a validated delivery forecast.

### Iterative and Incremental Development Review

Decision ID: DEC-094
<a id="dec-094"></a>

Status: Development method accepted by the project owner; product implementation has not been authorized by this review
Review date: October 31, 2026

Decision: After completing the agreed initial documentation and reaching baseline agreement, select a manageable increment with a clear outcome. Review relevant requirements, completion conditions, dependencies, and design; implement the scoped work; perform appropriate verification; update affected documentation and diagrams; review actual results, limitations, and follow-up work; and record a focused Git checkpoint.

Repeat relevant activities as findings emerge. Document the rationale and effects of revised decisions and keep the product, evidence, and documentation consistent. A successful commit or push alone does not establish capability completion.

Rationale: Support iterative learning and incremental delivery without allowing implementation, verification evidence, and documentation to diverge.

This acceptance defines the future development method. It does not start product implementation, complete an increment, or approve the overall baseline.

### Sprint Planning and Review Acceptance

Decision ID: DEC-093
<a id="dec-093"></a>

Status: Sprint planning and review method accepted by the project owner; existing schedule remains provisional
Review date: October 31, 2026

Decision: Define a clear Sprint Goal and select realistic work according to available time, capacity, and dependencies. Maintain one Sprint Backlog containing the goal, selected backlog items, and the plan for delivering them. Update tasks as understanding improves while keeping changes and their effects visible.

At the end of the Sprint, review the actual outcome and supporting verification evidence, and record lessons and working-method improvements for the next Sprint. Distinguish a Sprint, which is a work period, from a milestone, which is an outcome checkpoint. A Sprint may contribute to several milestones.

Retain the three existing Sprint schedules as provisional until reconciliation after the agreed analysis and design work. Assignment to a Sprint does not demonstrate capacity or capability completion.

Rationale: Give each work period a coherent goal, base selection on realistic constraints, and use evidence and feedback to improve subsequent delivery.

This acceptance records the method only; it does not revise live dates, assignments, or completion status, or authorize product implementation before baseline agreement.

### Change Assessment Method Review

Decision ID: DEC-092
<a id="dec-092"></a>

Status: Change assessment method accepted by the project owner
Review date: October 31, 2026

Decision: For a significant proposed change, record what changes and why; affected requirements, documents, diagrams, and milestones; expected effects on effort, schedule, cost, quality, and operations; relevant dependencies, risks, and alternatives; and the final decision, decision-maker, date, and follow-up actions.

Changes to agreed scope, spending, or delivery commitments require an explicit project-owner decision. Routine corrections and implementation choices within the agreed boundaries do not require separate content approval at every step. This distinction does not bypass applicable filesystem or execution permissions.

Rationale: Preserve informed control and traceability for material changes without slowing routine authorized work through redundant approval requests.

Acceptance records the assessment method. It does not approve an unspecified change, revise existing delivery commitments, or authorize implementation before the agreed baseline.

### Decision Records Method Review

Decision ID: DEC-091
<a id="dec-091"></a>

Status: Decision recording method accepted by the project owner
Review date: October 31, 2026

Decision: Record significant decisions in the affected authoritative document or a linked decision record. Give each significant decision a stable identifier, such as DEC-001, and state the subject, alternatives considered, selection rationale, and consequences. Distinguish proposed, accepted, rejected, and superseded decisions.

When a decision changes, preserve its history and identify the replacement decision, the earlier decision it supersedes, and the reason for the change. Git history records text changes but does not replace explicit documentation of decision rationale.

Rationale: Make important product and technical choices understandable and traceable over time, including the basis for revising earlier decisions.

This acceptance records the method. It does not claim that all existing review entries have already been reconciled with a stable decision identifier scheme or approve an unspecified technical decision.

### Completion and Review Rule Acceptance

Decision ID: DEC-090
<a id="dec-090"></a>

Status: Completion and review rule accepted by the project owner
Review date: October 31, 2026

Decision: Treat work as complete when its agreed completion conditions are satisfied and supporting review or verification evidence is available. Explicitly record unperformed checks, unresolved defects, and known limitations. Do not report an unexecuted test as successful.

Milestone completion and release decisions must use their own agreed criteria and remain distinct from routine Git commits and pushes.

Rationale: Make Done represent an evidenced, reviewable outcome rather than merely a recorded source change.

This acceptance defines the completion rule; it does not mark existing work items or milestones complete or establish release readiness.

## Document Review Summary

Status: Working method and change control reviewed and accepted
Review date: October 31, 2026

The project owner has accepted the working agreement, work organization, iterative and incremental development method, Sprint planning and review, change assessment, decision recording, and completion and review rules. The previously confirmed Agile direction remains in effect.

This review does not approve the overall planning baseline, authorize product coding, validate the delivery forecast, or establish completion of work items. Reconciliation of existing records and delivery tracking remains pending where identified above.

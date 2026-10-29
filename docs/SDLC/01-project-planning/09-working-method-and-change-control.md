# Working Method and Change Control

Status: Proposed draft for review

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

The proposed initial work-tracking location is the
[Product Backlog](../../Project-Management/product-backlog.md).
It is maintained as Markdown in this repository.
This document does not create GitHub Issues or Projects.

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

Sprint duration and the first sprint plan are not yet agreed.

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

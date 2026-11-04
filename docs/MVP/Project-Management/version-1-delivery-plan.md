# MVP Delivery Workflow

Updated November 4, 2026. Current mode: continuous Kanban; no active Sprint planning or dates. Capacity remains 20 total project hours/week. The historical November 8 target and dated Sprint assignments are not current commitments.

## One authority for each concern

| Concern | Authoritative location |
| --- | --- |
| Scope, selected requirements/technical policies | [Baseline](../baseline/README.md) |
| Milestone outcome and acceptance criteria | [Planning — Roadmap and Milestones](../SDLC/01-project-planning/08-roadmap-and-milestones.md#2-milestone-catalog) |
| Backlog package definition/dependencies | [Product Backlog](product-backlog.md) |
| Actual task status, blockers, code and acceptance evidence | [GitHub Issues](https://github.com/Farhad-V/Web-Resumefolio/issues) |
| Daily workflow visualization | [Private MVP Kanban](https://github.com/users/Farhad-V/projects/7/views/1) |
| Issue grouping and progress by outcome | [GitHub Milestones](https://github.com/Farhad-V/Web-Resumefolio/milestones), with canonical documentation links |
| Actual implementation facts | [Implementation documentation](../SDLC/05-implementation/README.md) |

## Documentation before synchronization

Finalize milestone definitions, MVP/future allocations, package criteria and dependencies first. Then reconcile existing GitHub milestones/issues by stable IDs, creating only missing items. Remove obsolete requested due dates and Sprint instructions from current PBI descriptions. Preserve old snapshots and future specifications. Do not infer completed implementation from document availability.

## Kanban and readiness

Backlog → In Progress → Done. All packages start in Backlog. Move work to In Progress only when execution actually starts and prerequisites are satisfied. Keep blockers and review notes in the Issue. After-MVP scope is separated by labels and its own view, rather than a status column. Product Backlog shows the same MVP Issues as a table. No Sprint/Iteration is assigned.

Select the next task only after prerequisites are checked. Move a task to Done only with linked outcome/criterion evidence, updated documentation and a recorded review. Record a failed check explicitly; do not drop a security or restore condition to clear a column.

## Milestones and Release gates

Retain M-01–M-10 identities. M-08 (user workflow execution) is after MVP and is not a predecessor to M-09. M-06 is manual applications without Gmail/Calendar. M-07 is separate basic ProjectForge, real Git, issues and simple Kanban. Preserve milestone acceptance history separately from GitHub issue state; do not close milestones merely because their definitions exist.

M-02/M-03 documentary choices are selected in the Baseline, while actor validation, actual host/dependency feasibility and operational evidence remain at their named gates. G1–G6 remain unexecuted unless real evidence is linked. M-09 needs the retained MVP acceptance/security/capacity/guidance and demonstrated restore; M-10 needs an actual reviewed deployment and live checks. Creating deployment work items authorizes no live deployment.

## Execution scope

Use the current Backlog, Milestones and Kanban. Superseded Sprint plans are available only through Git history; no Sprint or delivery date is assigned. No automatic monitor is configured.

# Roadmap and Milestones

Status: Proposed draft for review

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

The project owner requests full Version 1 delivery by November 8, 2026 (Europe/Berlin). Three dated sprint cycles are planned. Effort estimates and schedule feasibility remain unresolved.

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

Current status: all milestone completion decisions are pending.
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

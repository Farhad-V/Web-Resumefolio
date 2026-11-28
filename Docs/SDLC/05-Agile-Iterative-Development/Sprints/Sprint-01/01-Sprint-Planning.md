# Sprint 01 Planning

[Development overview](../../00-Agile-Iterative-Development.md) · [Review](02-Sprint-Review.md) · [Retrospective](03-Sprint-Retrospective.md)

**Goal:** review MVP scope, actual host prerequisites and implementation inputs before isolated setup. Farhad owns delivery and decisions. Work has started on #1, #2, #7 and #8; this record does not claim a planning meeting or completed readiness gate.

## Sprint Backlog

This is the evolving plan for the selected work, not a copy of the [Product Backlog](../../../02-Requirements-Engineering/02-Product-Backlog/README.md). The [GitHub board](https://github.com/users/Farhad-V/projects/7/views/1) owns live execution status; issues own exact acceptance criteria.

| Order / issue | Outcome | Prerequisite | Recorded position |
| --- | --- | --- | --- |
| [#1](https://github.com/Farhad-V/Web-Resumefolio/issues/1) | Scope, exclusions, responsibilities and constraints | None | Done; both documentary slices explicitly accepted. [Evidence](Evidence/PBI-001.md) |
| [#2](https://github.com/Farhad-V/Web-Resumefolio/issues/2) | Actual host capacity and isolation inventory | None | In Progress; [inventory complete](Evidence/PBI-002.md), candidate targets checked; provisional capacity allocation pending; independent off-host backup destination not selected/verified; isolation unverified |
| [#7](https://github.com/Farhad-V/Web-Resumefolio/issues/7) | Planning, risks and evidence gates | #1 accepted | Done; [planning/gate review accepted](Evidence/PBI-007.md) |
| [#8](https://github.com/Farhad-V/Web-Resumefolio/issues/8) | Applicable requirements and criterion coverage | #7 accepted | Done; [coverage and check plan](Evidence/PBI-008.md) explicitly owner-accepted |
| [#9](https://github.com/Farhad-V/Web-Resumefolio/issues/9) | Selected design contracts and setup handoff | #8 accepted | To do; prerequisite satisfied |

Start/read in order **#1 → #2 → #7 → #8 → #9**; #2 is independent. Use the existing [item slices](../../03-Sprint-Delivery-Plan.md#sprint-01), record actual evidence under this sprint and refine the backlog as inputs change. Setup #37, SMTP #5 and backup prerequisites #6 remain in Sprint 02.

## Planned checks and exit

- **S01-T01:** #1 scope/responsibilities and #2 host/isolation have exact evidence or named blockers. #1 documentary outcome is accepted; #2 has partial host readiness evidence; the combined check is incomplete.
- **S01-T02:** #7/#8 accepted; #9 not started. Combined check incomplete.
- **S01-T03:** the next setup slice has explicit prerequisites and planned checks. Not executed.

Exit requires reviewed item-level results and explicit remaining gaps. Documentation does not establish runtime, legal/license, capacity or release acceptance. Preserve selected MVP exclusions; no application code or server change belongs to this sprint record.

## Milestone and release alignment

Checked against existing GitHub assignments and the [outcome catalog](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/01-project-planning/08-roadmap-and-milestones.md#2-milestone-catalog): #1/#7 contribute to [M-01](https://github.com/Farhad-V/Web-Resumefolio/milestone/1) (reviewed planning and assigned unknowns); #8 to [M-02](https://github.com/Farhad-V/Web-Resumefolio/milestone/2) (reviewed requirements/scenarios/criteria); #2/#9 to [M-03](https://github.com/Farhad-V/Web-Resumefolio/milestone/3) (justified feasibility/design and resource/dependency evidence). Assignments match; all three remain open. M-01's accepted historical snapshot does not close current follow-up. Partial item evidence or Sprint 01 completion cannot close these outcomes; M-03 also has work beyond this sprint.

Under the [release policy](../../../06-Deployment-Release/01-Deployment-Plan.md#stable-mvp-release), the planned first stable tag is v1.0.0: exact applicable MVP criteria, required security/operational gates, isolated restore and rollback verification must pass on an identified candidate, with explicit release-publication authority. Deployment is separately authorized and verified. No tag/release is created by this alignment check.

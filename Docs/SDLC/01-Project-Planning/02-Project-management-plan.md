# Project Management Plan

## Delivery approach

Resumefolio uses **Agile with Upfront Architecture** from project initiation, following sections 1–3 of the SDLC Complete Engineering Guide. Establish system boundaries, important quality constraints and high-risk decisions early. Revisit affected requirements and designs as implementation and evidence clarify them.

Use the [GitHub board](https://github.com/users/Farhad-V/projects/7/views/1) to track work. Apply the [Development cycle](../Sdlc-guide.md#stage-5-agile-iterative-development) to each increment: plan the sprint goal, refine work items, clarify detailed design, implement, test, review the outcome and record an improvement for the next cycle.

## Deliverables and control

- Begin with [isolated project setup](../05-Agile-iterative-development/00-Project-setup.md). Verify that both applications can be built and tested independently.
- Maintain the software, engineering documents and test evidence associated with each increment. Use the [outcome roadmap](02-Project-management-plan.md#delivery-sequence) for milestones and prerequisites.
- Record the issue, intended outcome, acceptance checks, tested revision and review result. Keep proposed, accepted and demonstrated outcomes distinguishable.
- Carry open issues from the [feasibility and risk assessment](03-Feasibility-and-risk-assessment.md) into the affected work items. Verify the [release criteria](../06-Deployment-release/Deployment-release.md) before publishing the MVP.

## Delivery sequence

1. Establish and verify an isolated local setup for both applications.
2. Build invited access and the core workspace. Verify the ProjectForge identity and Git boundary early, before dependent integration.
3. Deliver resumes and portfolios, private files, PDFs and employer sharing, then application tracking with preserved submitted materials.
4. Integrate the agreed basic ProjectForge capabilities. Verify the complete user journeys, security and recovery before the first stable MVP release.

Use roadmap milestones as outcome checkpoints. Link each completed outcome to its work item and evidence.

## Change control

For a change to accepted scope, an interface or a design decision, record what is changing, why, which requirements and tests are affected and who decides. Update the owning documents and backlog after the decision. Link the implementation and verification evidence when available.

Use the [decision register](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/01-project-planning/decision-register.md) for earlier decisions, the [planning acceptance record](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/01-project-planning/10-planning-completion-criteria.md) for the recorded review and follow-up, and the [planning diagram map](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/01-project-planning/diagrams/planning-document-map.svg) for the original visual overview.

## Work breakdown, quality and communication

Use one issue per reviewable outcome. Include the requirement or decision it implements, its dependencies, acceptance checks and expected demonstration. Split work that cannot be verified independently into smaller steps. The GitHub board reflects current progress. Use each issue to record results, blockers and decisions as work is reviewed.

For each increment, check the affected acceptance criteria, relevant failure paths and regression behavior. Record the checked revision and result. Resolve or explicitly track gaps before marking the work verified. For the release, use the quality and recovery criteria in the release document.

### Outcome roadmap

```mermaid
flowchart LR
  Setup[Isolated setup] --> Core[Invited access and core workspace]
  Core --> Sharing[Resumes, files, PDFs and sharing]
  Sharing --> Applications[Applications and submitted history]
  Setup --> Git[ProjectForge authorization and Git checks]
  Git --> Integration[Basic ProjectForge integration]
  Integration --> Release[MVP verification and release]
  Applications --> Release
```

## Decision and review records

Record accepted changes in the owning document and link the outcome from the relevant issue. Preserve decisions with their context, rationale and status. The past planning review accepted the identified snapshot with follow-up. Its open items require their own evidence before closure.


# Product Backlog

Use the [GitHub board](https://github.com/users/Farhad-V/projects/7/views/1) and linked issues for priority, execution status and evidence. The [SRS](01-Software-Requirements-Specification.md) defines the required behavior. Use the [traceability matrix](03-Requirements-Traceability-Matrix.md) to resolve the applicable acceptance criteria. The package list retains existing issue identities and dependencies from the recorded backlog.

Follow the [dependency-ordered delivery plan](../05-Agile-Iterative-Development/03-Sprint-Delivery-Plan.md): scope/host/readiness first, then [isolated project setup](../05-Agile-Iterative-Development/01-Project-Setup.md). During [backlog refinement](../05-Agile-Iterative-Development/Sprints/Sprint-01/01-Sprint-Planning.md), give each selected issue an observable outcome and the specific acceptance checks that apply. Track deferred scope separately from the MVP path.

| Work item | Outcome | Dependencies | Requirement areas and gates |
| --- | --- | --- | --- |
| <a id="pbi-001"></a>[PBI-001](https://github.com/Farhad-V/Web-Resumefolio/issues/1) | Record 20-hour capacity and MVP scope | None | BIZ / DOM; G0 |
| <a id="pbi-002"></a>[PBI-002](https://github.com/Farhad-V/Web-Resumefolio/issues/2) | Verify shared-host capacity and isolation prerequisites | None | AFO / QSR; G1; G5 |
| <a id="pbi-005"></a>[PBI-005](https://github.com/Farhad-V/Web-Resumefolio/issues/5) | Verify invitation and recovery SMTP delivery | PBI-002 | ACC / EIF; G4 |
| <a id="pbi-006"></a>[PBI-006](https://github.com/Farhad-V/Web-Resumefolio/issues/6) | Verify independent backup destination and restore plan | PBI-002 | QSR / AFO; G4 |
| <a id="pbi-007"></a>[PBI-007](https://github.com/Farhad-V/Web-Resumefolio/issues/7) | Review current planning allocation and tracked follow-ups | PBI-001 | BIZ / DOM; G0 |
| <a id="pbi-008"></a>[PBI-008](https://github.com/Farhad-V/Web-Resumefolio/issues/8) | Validate MVP requirement and criterion coverage | PBI-007 | USR / BIZ / DOM; G0 |
| <a id="pbi-009"></a>[PBI-009](https://github.com/Farhad-V/Web-Resumefolio/issues/9) | Reconcile selected Design and technical baseline | PBI-008 | DOM / EIF / QSR; G0; G1 |
| <a id="pbi-010"></a>[PBI-010](https://github.com/Farhad-V/Web-Resumefolio/issues/10) | Implement invited identity and resource authorization | PBI-030, PBI-005 | ACC; G3 |
| <a id="pbi-011"></a>[PBI-011](https://github.com/Farhad-V/Web-Resumefolio/issues/11) | Implement dashboard and responsive application shell | PBI-010 | EIF / USR; G3; G5 |
| <a id="pbi-012"></a>[PBI-012](https://github.com/Farhad-V/Web-Resumefolio/issues/12) | Implement Profile and independent Resume drafts | PBI-010 | PRP / BRL; G3 |
| <a id="pbi-013"></a>[PBI-013](https://github.com/Farhad-V/Web-Resumefolio/issues/13) | Implement private My Files and Media library | PBI-010, PBI-002, PBI-034 | AFO / PRP; G3; G5 |
| <a id="pbi-014"></a>[PBI-014](https://github.com/Farhad-V/Web-Resumefolio/issues/14) | Implement generated and uploaded language-specific PDFs | PBI-012, PBI-013 | PDF; G3; G5 |
| <a id="pbi-015"></a>[PBI-015](https://github.com/Farhad-V/Web-Resumefolio/issues/15) | Implement password links and protected selected-content retrieval | PBI-012, PBI-013, PBI-014, PBI-033 | PDF / ACC; G3 |
| <a id="pbi-016"></a>[PBI-016](https://github.com/Farhad-V/Web-Resumefolio/issues/16) | Implement manual applications and actual submitted history | PBI-012, PBI-014, PBI-033 | APP / BRL; G3 |
| <a id="pbi-019"></a>[PBI-019](https://github.com/Farhad-V/Web-Resumefolio/issues/19) | Implement ProjectForge fixed issue Kanban | PBI-022 | PKS; G3 |
| <a id="pbi-020"></a>[PBI-020](https://github.com/Farhad-V/Web-Resumefolio/issues/20) | Implement native repositories and real Git transfers | PBI-031, PBI-032, PBI-034 | GIT; G2; G3 |
| <a id="pbi-022"></a>[PBI-022](https://github.com/Farhad-V/Web-Resumefolio/issues/22) | Implement basic ProjectForge repository issues | PBI-032, PBI-020 | GIT / PKS; G3 |
| <a id="pbi-024"></a>[PBI-024](https://github.com/Farhad-V/Web-Resumefolio/issues/24) | Implement account suspension, lifecycle and audit | PBI-010, PBI-013, PBI-033 | ACC / AFO / BRL / QSR; G3; G4 |
| <a id="pbi-025"></a>[PBI-025](https://github.com/Farhad-V/Web-Resumefolio/issues/25) | Verify integrated MVP acceptance and authorization | PBI-011, PBI-015, PBI-016, PBI-019, PBI-024, PBI-032 | ACC / PRP / PDF / APP / GIT / PKS; G3; G6 |
| <a id="pbi-026"></a>[PBI-026](https://github.com/Farhad-V/Web-Resumefolio/issues/26) | Measure capacity, browsers and accessibility | PBI-025, PBI-034 | QSR / EIF; G5 |
| <a id="pbi-027"></a>[PBI-027](https://github.com/Farhad-V/Web-Resumefolio/issues/27) | Demonstrate coherent restore and deployment recovery | PBI-006, PBI-024, PBI-020, PBI-033 | QSR / AFO; G4 |
| <a id="pbi-028"></a>[PBI-028](https://github.com/Farhad-V/Web-Resumefolio/issues/28) | Complete user, admin and operating guidance | PBI-025, PBI-027 | EIF / QSR / USR; G4; G6 |
| <a id="pbi-029"></a>[PBI-029](https://github.com/Farhad-V/Web-Resumefolio/issues/29) | Review and deploy the initial MVP release | PBI-025, PBI-026, PBI-027, PBI-028 | USR / QSR; G6 |
| <a id="pbi-030"></a>[PBI-030](https://github.com/Farhad-V/Web-Resumefolio/issues/37) | Create isolated Laravel applications and reproducible Setup | PBI-009, PBI-002 | DOM / EIF; G1 |
| <a id="pbi-031"></a>[PBI-031](https://github.com/Farhad-V/Web-Resumefolio/issues/38) | Prove ProjectForge SSO and native Git security spike | PBI-030, PBI-010, PBI-002 | ACC / GIT; G2 |
| <a id="pbi-032"></a>[PBI-032](https://github.com/Farhad-V/Web-Resumefolio/issues/39) | Implement Core and ProjectForge scoped identity/API | PBI-031, PBI-010 | ACC / EIF; G2; G3 |
| <a id="pbi-033"></a>[PBI-033](https://github.com/Farhad-V/Web-Resumefolio/issues/40) | Implement atomic publication and protected artifact history | PBI-012, PBI-013, PBI-014 | PRP / BRL / APP; G3 |
| <a id="pbi-034"></a>[PBI-034](https://github.com/Farhad-V/Web-Resumefolio/issues/41) | Enforce storage reservations and bounded Git/media admission | PBI-002, PBI-030 | AFO / QSR / GIT; G2; G5 |

[Recorded package details and deferred work](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/Project-Management/product-backlog.md).

## Readiness and evidence

A work item is ready to select when its expected outcome, acceptance checks, prerequisites and owning design are clear. If the work is too broad to demonstrate, split by observable user outcome. Capture actual results and follow-up on the existing issue. Keep deferred work out of the selected sprint scope unless the scope decision is updated.

## Task Slices, Order and Completion

The [Sprint Delivery Plan](../05-Agile-Iterative-Development/03-Sprint-Delivery-Plan.md) and development-plan section on each current MVP issue define the ordered task slices, observable results, verification and preliminary estimates. Existing 28 MVP issue identities are preserved; task checklists refine them without creating duplicate backlog items. Six deferred issues remain after MVP. Planning completion does not close any execution or acceptance item.

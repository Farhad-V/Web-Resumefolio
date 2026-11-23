
<a id="requirements-specification-requirements-priority-and-readiness"></a>

<a id="requirements-specification-requirements-priority-and-readiness--heading-requirement-priority-and-readiness"></a>
# Requirement Priority and Readiness

Use the [157-row requirement register](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/requirement-register.csv) and [470-row criterion register](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/criterion-dispositions.csv) as the current scope/priority records. Original IDs and criterion wording are preserved; a mixed requirement selects only its explicit MVP slice. [Criterion guide](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/criterion-dispositions.md).

| Classification | Meaning |
| --- | --- |
| Must within MVP slice | Required for the selected Core/basic ProjectForge outcome, subject to its exact criterion constraint |
| Later | After MVP; not a current Release prerequisite |

Priority is not a completed test or an implementation order. [Technical and policy decisions](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/README.md) are selected; [implementation gates](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/implementation-sequence.md) identify unexecuted environment, security, actor, operational and quality checks. [Backlog dependencies](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/Project-Management/product-backlog.md) and GitHub track actual execution.

Do not infer that all criteria of a selected parent are accepted, or require future mail/calendar/review/Sprint/runner behavior merely because a shared access or recovery rule names it. Do not keep a second proposed-priority table that contradicts the selected registers.

## Current record rules

The selected baseline BL-MVP-2026-11-04.1 supersedes the November 1 proposals within the MVP slice. The [decision index](../07-Change-And-Baseline/03-Requirements-Questions-And-Decisions.md#change-and-baseline-open-questions-and-decisions--heading-current-dispositions) owns question dispositions; the linked baseline registers own exact scope and priority. Domain documents own behavior and acceptance wording.

| Term in a source record | How to read it now |
| --- | --- |
| Proposed, provisional, unassigned or an open policy question | Original drafting status. Check the selected decision and criterion disposition before treating it as an unresolved MVP choice. |
| Selected MVP slice / Must within MVP slice | Required only within the stated criterion boundary; future clauses of a mixed record remain excluded. |
| Later / deferred | Preserved for future work; not an MVP implementation or release prerequisite. |
| Not executed / evidence pending | The policy can be selected while its implementation, measurement, actor validation or restore remains unproven. |
| Historical M-01/M-02 or owner-review statement | Applies to the named source revision. Editorial reconciliation neither invents personal owner review nor changes runtime or release acceptance. |

Source refinement notes and dated observations remain for provenance. Use the current decision when it resolves the same question; retain genuinely unresolved evidence gates. A source date or requested delivery date is not a current forecast.

## Scope and priority by domain

This is a summary of the selected 157-row register, not a second editable priority register. Reconcile it from that source when scope changes.

| Domain | Must within MVP slice | Later |
| --- | ---: | ---: |
| [ACC](01-Accounts-Authentication-And-Permissions.md) | 12 | 0 |
| [AFO](02-Administration-Files-And-Operational-Behavior.md) | 12 | 0 |
| [BIZ](03-Business-Requirements.md) | 5 | 0 |
| [BRL](04-Business-Rules-And-Data-Lifecycle.md) | 9 | 1 |
| [DOM](05-Domain-Requirements-And-Constraints.md) | 8 | 0 |
| [EGC](06-Email-Calendar-And-Google-Integration.md) | 0 | 12 |
| [EIF](07-External-Interface-Requirements.md) | 8 | 2 |
| [GIT](08-Git-Hosting-And-Collaboration.md) | 6 | 4 |
| [APP](09-Manual-Application-Management.md) | 9 | 0 |
| [PDF](11-Pdf-And-Controlled-Sharing.md) | 10 | 0 |
| [PRP](12-Profiles-Resumes-And-Portfolio.md) | 10 | 0 |
| [PKS](13-Projects-Kanban-And-Sprints.md) | 5 | 6 |
| [QSR](14-Quality-Security-And-Recovery-Requirements.md) | 14 | 0 |
| [USR](18-User-Requirements.md) | 10 | 2 |
| [YML](19-Yaml-Workflows-And-Cicd.md) | 0 | 12 |
| **Total** | **118** | **39** |

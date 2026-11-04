# Resumefolio — Scenarios and Models Guide

Current implementation choices and scope: [Baseline](../../../baseline/README.md). Runtime verification remains subject to its gates.

| Item | Current position |
| --- | --- |
| Purpose | Navigate actor stories, goal-based use cases, scenario paths and visual models |
| Owner | Farhad |
| Status | Proposed documentation set — owner review, policy refinement and execution pending |
| Inventory | 12 use-case bundles, 12 stories and 60 path drafts in one primary document; four diagrams including this guide |
| Revision | October 31, 2026 |

**Start with [User Stories and Scenarios](user-stories-and-scenarios.md).** Use the
catalog to find an actor goal, then read its conditions, normal steps, alternative,
denied, failure and recovery/correction paths. These are reviewable examples,
not an approved baseline, exhaustive use-case model or completed test suite.

[Reading routes](#1-reading-routes) · [Documents](#documents)
· [Coverage](#3-coverage-and-boundaries) · [Roadmap](#4-refinement-roadmap)
· [Diagrams](#5-diagram-catalog) · [Maintenance](#6-maintenance)

## 1. Reading Routes

| Your question | Suggested route |
| --- | --- |
| What goal/path should I review? | [Goal catalog](user-stories-and-scenarios.md#2-use-case-and-story-catalog) → selected UC/ST bundle → N/A/D/F/R path |
| Where do the stories come from? | [Actors](../02-stakeholders-and-elicitation/actors-and-system-context.md) → [User Requirements](../03-requirements-specification/user-requirements.md) → linked story/source |
| Which detailed rule decides the outcome? | Bundle trace references → [primary specifications](../03-requirements-specification/README.md) → exact obligation/criterion and open policy |
| Can I treat this as an executable test? | [Refinement/evidence contract](user-stories-and-scenarios.md#5-refinement-and-later-execution-evidence) → resolve conditions → later authorized checks and separate evidence |
| What must be consistent across scenarios? | [Dictionary](../05-data-definitions/data-dictionary.md) → [Lifecycle](../03-requirements-specification/business-rules-and-data-lifecycle.md) → [Accounts](../03-requirements-specification/accounts-authentication-and-permissions.md) → [Quality](../03-requirements-specification/quality-security-and-recovery-requirements.md) |

## Documents

| Document | Primary responsibility | Current content / limitation |
| --- | --- | --- |
| [User Stories and Scenarios](user-stories-and-scenarios.md) | Sourced actor goals, preconditions, interactions, observable outcomes, variants and open review gates | 12 proposed UC bundles / 12 ST stories / 60 SCN path drafts; no actual user validation or product results recorded |

The folder keeps related small records together for review. It does not decide a
permanent one-file storage strategy. Split individual use cases/scenarios when
needed, preserve references and update this guide. UC-D/ST-D/SCN-D references are
provisional local navigation, not allocated final global identifiers or approved priorities.

## 3. Coverage and Boundaries

| Goal group | Bundle links | Main review concern |
| --- | --- | --- |
| Professional tailoring | [UC-D01](user-stories-and-scenarios.md#uc-d01) | Independent resumes, selected evidence and explicit shared-source updates |
| Owner/employer sharing | [UC-D02](user-stories-and-scenarios.md#uc-d02), [UC-D03](user-stories-and-scenarios.md#uc-d03) | PDF/language availability, passwords, direct paths and changed access |
| Applications/history | [UC-D04](user-stories-and-scenarios.md#uc-d04), [UC-D05](user-stories-and-scenarios.md#uc-d05) | Manual progress versus actual submitted copies, capture failure and correction |
| Correspondence/calendar | [UC-D06](user-stories-and-scenarios.md#uc-d06) | Account/grants, actual provider conditions, conflict and uncertain external effects  **After MVP.** |
| Work/collaboration | [UC-D07](user-stories-and-scenarios.md#uc-d07), [UC-D08](user-stories-and-scenarios.md#uc-d08) | Items/tasks/Sprint Backlog, invitations and scoped membership |
| Real Git | [UC-D09](user-stories-and-scenarios.md#uc-d09) | Actual client operations, current source/target, denied actions and merge conflict |
| Conditional execution | [UC-D10](user-stories-and-scenarios.md#uc-d10) | Isolation/resources, secret scope, actual run outcomes and separate deployment approval  **After MVP.** |
| Administration/recovery | [UC-D11](user-stories-and-scenarios.md#uc-d11), [UC-D12](user-stories-and-scenarios.md#uc-d12) | Effective limits/powers, reference-aware cleanup and consistent safely authorized restoration |

Each bundle has five path drafts; categories do not prove exhaustive coverage.
Complex mail/calendar, Git, Sprint and execution interactions still need more
operation-specific cases as their policies stabilize. Quantitative performance,
availability, accessibility and recovery targets require separate decided
measurement contracts in QSR-D; these narratives do not set those values.

**Keep these distinctions visible:** source versus live share versus actual
submitted copy; downloaded copy versus future retrieval; item/task versus accepted
work; scoped membership versus unrelated private access; Git transfer versus job
execution; Push/merge versus deployment authority; backup existence versus demonstrated recovery.

## 4. Refinement Roadmap

![Source a goal, define paths, resolve policies and record later actual evidence](../diagrams/scenario-refinement-map.png)

[Scalable SVG](../diagrams/scenario-refinement-map.svg) ·
[Editable Graphviz](../diagrams/scenario-refinement-map.dot)

Arrows describe review/refinement relationships, not a dated schedule, software
architecture or a completed evidence chain. Colors supplement labels.

1. Confirm the scope-derived actor goal and identify its primary domain/criteria.
2. Review each path's conditions, allowed/denied actions and observable state/effect.
3. Resolve policy, input/state, dependency and measurement gaps at their existing gates.
4. Split complex paths, allocate final IDs and concrete data, then maintain actual trace links and review findings.
5. Later run only authorized controlled checks; record candidate/environment, actual results and limitations separately from the proposed path.

Use [Questions and Decisions](../07-change-and-baseline/open-questions-and-decisions.md),
[Traceability](../06-validation-and-traceability/requirements-traceability.md),
[Review Findings](../06-validation-and-traceability/review-plan-and-findings.md) and
[Baseline Criteria](../07-change-and-baseline/requirements-review-and-baseline-criteria.md).
The model does not populate these registers or resolve their acceptance conditions.

M-02 remains pending. Scope interpretation, owner review, feasibility, later product
verification and release acceptance are separate outcomes. The agreed wider
pre-implementation baseline still precedes product coding. No scenario draft
authorizes real email/job submissions, live resource mutation, job execution or production recovery.

## 5. Diagram Catalog

| Diagram | Purpose | Editable source | SVG | PNG |
| --- | --- | --- | --- | --- |
| Scenario refinement roadmap | This folder's review/evidence route | [DOT](../diagrams/scenario-refinement-map.dot) | [SVG](../diagrams/scenario-refinement-map.svg) | [PNG](../diagrams/scenario-refinement-map.png) |
| Story/scenario relationships | Sources, goals and the five path categories | [DOT](../diagrams/story-scenario-relationships.dot) | [SVG](../diagrams/story-scenario-relationships.svg) | [PNG](../diagrams/story-scenario-relationships.png) |
| Protected sharing sequence | UC-D03's viewer/direct-file boundary | [PlantUML](../diagrams/protected-sharing-sequence.puml) | [SVG](../diagrams/protected-sharing-sequence.svg) | [PNG](../diagrams/protected-sharing-sequence.png) |
| Submitted-history scenario | UC-D05's actual-material capture and later source edits | [PlantUML](../diagrams/submission-history-scenario.puml) | [SVG](../diagrams/submission-history-scenario.svg) | [PNG](../diagrams/submission-history-scenario.png) |

## 6. Maintenance

- Keep the catalog, local references and path counts synchronized with the primary document.
- Preserve the legacy protected-resume walkthrough anchor retained at UC-D03 for existing method links.
- Link primary obligations instead of creating competing copies of permission/lifecycle policies.
- Distinguish actual review/execution from planned paths, including exact revisions and limits.
- Keep editable diagrams and PNG/SVG renders together; inspect labels/arrows and local links after changes.

Follow the [diagram guide](../diagrams/README.md). From the repository root:

```powershell
$diagramFolder = 'docs\SDLC\02-requirements-engineering\diagrams'
$graphvizExe = 'C:\Program Files\Graphviz\bin\dot.exe'
$plantUmlJar = 'C:\Users\fvali\AppData\Local\Resumefolio\DiagramTools\plantuml.jar'
foreach ($format in 'svg', 'png') {
    foreach ($stem in 'scenario-refinement-map', 'story-scenario-relationships') {
        & $graphvizExe "-T$format" -Gdpi=140 "$diagramFolder\$stem.dot" -o "$diagramFolder\$stem.$format"
        if ($LASTEXITCODE -ne 0) { throw "Graphviz failed: $stem / $format" }
    }
    foreach ($stem in 'protected-sharing-sequence', 'submission-history-scenario') {
        java '-Djava.awt.headless=true' -jar $plantUmlJar -charset UTF-8 "-t$format" "$diagramFolder\$stem.puml"
        if ($LASTEXITCODE -ne 0) { throw "PlantUML failed: $stem / $format" }
    }
}
```

Use actual installed tool paths elsewhere; save UTF-8 without BOM. A readable
render and working link establish document quality, not a modeled product result.

[Requirements index](../README.md) · [Specification guide](../03-requirements-specification/README.md)

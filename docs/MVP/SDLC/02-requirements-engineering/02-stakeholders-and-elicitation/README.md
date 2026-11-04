# Resumefolio — Stakeholders and Elicitation

Current implementation choices and scope: [Baseline](../../../baseline/README.md). Runtime verification remains subject to its gates.

| Item | Current position |
| --- | --- |
| Folder purpose | Identify actor goals and system context, plan elicitation and preserve actual source/activity evidence |
| Responsible person | Farhad; sole delivery and operations owner |
| Document coverage | Three expanded working documents with editable diagrams |
| Actual activity | LOG-001 document analysis with EXT-001–EXT-003 recorded; interpretations pending owner review |
| Acceptance boundary | No new interview, detailed permission approval or M-02 baseline acceptance is established here |
| Index revision | October 31, 2026 |

**Start with [Actors and System Context](actors-and-system-context.md)** to
understand who interacts with the product and where its boundaries lie. Read the
plan for proposed next activities and the log for what actually happened. Keep
accepted source decisions, extracted interpretations and future requirements distinct.

[Overview](#1-folder-overview) · [Documents](#documents) · [Reading routes](#3-find-the-right-record)
· [Evidence status](#4-current-evidence-and-next-work) · [Handoff](#5-connections-to-the-rest-of-requirements-engineering)
· [Diagrams](#6-diagram-catalog) · [Maintenance](#7-maintaining-this-folder)

## 1. Folder Overview

![Actors, planned activities, actual evidence and downstream handoff](../diagrams/stakeholders-elicitation-overview.png)

[Scalable SVG](../diagrams/stakeholders-elicitation-overview.svg) ·
[Editable Graphviz](../diagrams/stakeholders-elicitation-overview.dot)

Blue identifies actor/source context, purple identifies planning, amber identifies
actual records and pending interpretation, and green identifies the downstream
handoff. Arrows show information relationships, not completed activities, staffing,
runtime data flow or automatic acceptance.

Use the three documents together: actor/context questions guide activity selection;
the plan explains what to explore and how; the log preserves actual sources,
activities and feedback. Analysis/review can expose gaps that require further
elicitation. A planned topic becomes an actual log activity only when performed.

## Documents

| Document | Main question | Contents and boundary |
| --- | --- | --- |
| [Actors and System Context](actors-and-system-context.md) | Who needs what, and what lies inside/outside the product? | Actor/stakeholder goals, resource-owner contexts, external services/dependencies, access boundaries and open questions; not a complete permission grant or architecture |
| [Elicitation Plan and Techniques](elicitation-plan-and-techniques.md) | What genuine gaps should be explored next, using which method? | Scope-based topic coverage, selection guidance, preparation, neutral prompts and an undated roadmap; no session dates or participant commitments invented |
| [Elicitation Log](elicitation-log.md) | What material was inspected or activity actually performed, and what was learned? | SRC register, actual LOG-001/EXT records, separate interpretations, source hash, review state and recording template; no invented interviews or detailed policy acceptance |

For a first reading, follow the table order. When checking an evidence claim,
start in the log and follow its exact source/revision rather than relying only on
this overview.

## 3. Find the Right Record

| If you need to… | Open | What to inspect next |
| --- | --- | --- |
| Understand a role or external interaction | [Actor catalog](actors-and-system-context.md#3-human-actor-and-stakeholder-catalog) | Its goal, existing boundary, unresolved rules and source DEC references |
| Clarify who may perform an operation | [Accounts/Permissions matrix](../03-requirements-specification/accounts-authentication-and-permissions.md#7-role-resource-and-operation-matrix) | Relevant resource/action/state rules and allowed/denied scenarios; role names alone grant no access |
| Select the next clarification group | [Proposed work plan](elicitation-plan-and-techniques.md#2-proposed-elicitation-work-plan) | Existing extracts, dependencies, method and expected handoff |
| Choose a suitable technique | [Technique selection](elicitation-plan-and-techniques.md#technique-selection) | Question, available material/participants and evidence limits |
| Prepare an actual activity | [Preparation and conduct](elicitation-plan-and-techniques.md#4-activity-preparation-and-conduct) | Bounded question, sources, fictional/sanitized examples, permissions and expected records |
| Find existing sources | [Source register](elicitation-log.md#source-register) | Exact section/turn/version when used; broad discovery pointers are not precise extraction evidence |
| Review the performed documentary work | [LOG-001](elicitation-log.md#log-001-scope-decision-extraction) | Actual coverage, source hash, paraphrases, interpretation status and limitations |
| Record a new activity | [Recording guide](elicitation-log.md#5-recording-new-activities) | Actual date/method/participants or inspected material, raw evidence, interpretation and follow-up |
| Resolve a conflict or material new choice | [Analysis and Negotiation](../01-process-and-approach/04-analysis-and-negotiation.md) | Exact competing statements, impacts/options and actual owner decision where needed |

## 4. Current Evidence and Next Work

### What is recorded

| Record | Actual content | Remaining limit |
| --- | --- | --- |
| SRC-01–SRC-06 | Index of planning, prior discussion and reference-project material | Discovery pointers require exact locators/revisions when extracted; not an exhaustive source review |
| LOG-001 | Document analysis performed October 31, 2026 against DEC-024, DEC-023 and DEC-028 in the identified Scope working copy | No interview participants, server/provider checks, product execution or complete-scope extraction |
| [EXT-001](elicitation-log.md#ext-001-controlled-employer-access) | Protected employer access and selected-content boundary | Interpretation pending; session/revocation and detailed criteria still need definition |
| [EXT-002](elicitation-log.md#ext-002-manual-applications-and-preserved-submissions) | Manual applications and preservation of actual submitted material | Interpretation pending; capture, progress and lifecycle detail still need definition |
| [EXT-003](elicitation-log.md#ext-003-unified-sign-in-and-resource-permissions) | Unified sign-in with resource-specific permissions | Interpretation pending; detailed role/account/authentication rules still need definition |

The three paraphrases were checked against the inspected source sections; this
does not constitute owner validation of their detailed interpretations. Source
decisions retain their original accepted scope authority. No interview, workshop,
observation, prototype-feedback session or survey has been recorded in this log.

### Practical next work

1. Review the existing extracts and their genuine missing-detail questions without re-approving accepted scope inclusion.
2. Select a coherent actor goal using the proposed work plan and relevant feasibility/dependency gates.
3. Prepare and conduct an appropriate activity only with actual available material/participants and needed access.
4. Record actual evidence and feedback, keeping interpretation and unresolved detail separate.
5. Hand off reviewed needs and explicit gaps to analysis/specification and maintain source-to-record links.

Farhad coordinates the work in the current solo arrangement. Missing stakeholder
perspectives remain visible; owner representation is not evidence of research
with actual employers or collaborators. No dates, durations or research population
are assumed by this index.

## 5. Connections to the Rest of Requirements Engineering

| Related record | Relationship to this folder |
| --- | --- |
| [Scope](../../01-project-planning/02-scope.md) / [Planning Decision Register](../../01-project-planning/decision-register.md) | Source of accepted boundaries and rationale; material changes follow actual decision control |
| [Requirements Approach](../01-process-and-approach/01-requirements-approach.md) / [Elicitation Process](../01-process-and-approach/03-requirements-elicitation.md) | Overall method, iterative work and evidence expectations |
| [Feasibility Study](../01-process-and-approach/02-feasibility-study.md) | Investigations needed where user expectations do not establish actual technical/provider/resource suitability |
| [Analysis](../01-process-and-approach/04-analysis-and-negotiation.md) / [SRS](../03-requirements-specification/requirements-specification.md) | Clarification/classification/conflict handling and authoritative detailed requirement records |
| [Scenarios and Models](../04-scenarios-and-models/user-stories-and-scenarios.md) | Actor journeys, alternatives, denied/failure paths and use-case detail |
| [Data Definitions](../05-data-definitions/README.md) | Consistent terms and conceptual information meaning |
| [Traceability](../06-validation-and-traceability/requirements-traceability.md) / [Review Findings](../06-validation-and-traceability/review-plan-and-findings.md) | Source-to-requirement links and actual review evidence/rechecks |
| [Open Questions](../07-change-and-baseline/open-questions-and-decisions.md) / [Change Control](../07-change-and-baseline/change-control.md) | Unresolved matters, owner/actions/gates and actual material decisions |

Do not copy full requirement text, live delivery status or review findings into
this README. Link the authoritative home and summarize only the evidence needed
for navigation. Source extraction, requirement acceptance, implementation progress
and executed verification results are distinct facts.

Preserve all agreed Version 1 scope, including manual job application management. Product AI,
automatic translation and automatic demo migration remain excluded. The wider
pre-implementation baseline and M-02 review remain separate gates; documentation
or elicitation completion alone does not authorize product coding.

## 6. Diagram Catalog

This catalog covers **seven supporting diagram sources**: the new folder overview
and two diagrams for each of the three documents. Sources and SVG/PNG outputs
live in the shared `diagrams` folder. See the wider
[Requirements Diagram Index](../diagrams/README.md) for other phase diagrams.

| Topic / diagram | Preview | Scalable | Editable source |
| --- | --- | --- | --- |
| This index — folder overview | [PNG](../diagrams/stakeholders-elicitation-overview.png) | [SVG](../diagrams/stakeholders-elicitation-overview.svg) | [DOT](../diagrams/stakeholders-elicitation-overview.dot) |
| Actors — system context | [PNG](../../04-system-design/01-software-architecture/diagrams/logical-component-ownership.png) | [SVG](../../04-system-design/01-software-architecture/diagrams/logical-component-ownership.svg) | [DOT](../../04-system-design/01-software-architecture/diagrams/logical-component-ownership.dot) |
| Actors — goal overview | [PNG](../diagrams/actors-goal-overview.png) | [SVG](../diagrams/actors-goal-overview.svg) | [PlantUML](../diagrams/actors-goal-overview.puml) |
| Log — provenance | [PNG](../diagrams/elicitation-log-provenance.png) | [SVG](../diagrams/elicitation-log-provenance.svg) | [DOT](../diagrams/elicitation-log-provenance.dot) |
| Log — recording/review cycle | [PNG](../diagrams/elicitation-log-recording-cycle.png) | [SVG](../diagrams/elicitation-log-recording-cycle.svg) | [PlantUML](../diagrams/elicitation-log-recording-cycle.puml) |
| Plan — technique selection | [PNG](../diagrams/elicitation-technique-selection.png) | [SVG](../diagrams/elicitation-technique-selection.svg) | [DOT](../diagrams/elicitation-technique-selection.dot) |
| Plan — adaptive roadmap | [PNG](../diagrams/elicitation-plan-roadmap.png) | [SVG](../diagrams/elicitation-plan-roadmap.svg) | [PlantUML](../diagrams/elicitation-plan-roadmap.puml) |

PNG is the quick preview, SVG supports zooming, and DOT/PlantUML is editable.
Read each image with its source document's meaning and limits. No diagram is a
permission grant, live schedule or proof of technical feasibility.

## 7. Maintaining This Folder

| Change | Keep consistent |
| --- | --- |
| Actor, interaction or boundary changes | Actor document, relevant permission/scenario records, models and source rationale |
| New planned activity | Work plan, technique rationale, expected output and dependent gate |
| Activity actually performed | Log date/source/participants or material, extracts, actual feedback and follow-up; update summary here if material |
| Source changes | Preserve historic extraction locator; add explicit new evidence/review rather than silently rewriting old observations |
| Diagram/document moved or revised | Catalog, incoming links, editable sources, renders, captions and affected record references |
| Actual decision or requirement allocated | Authoritative record first, then source/extract-to-requirement traceability and any relevant summary |

Regeneration commands for each document's diagrams are in that document. For the
folder overview, run from the repository root:

```powershell
$diagramFolder = 'docs\SDLC\02-requirements-engineering\diagrams'
$graphvizExe = 'C:\Program Files\Graphviz\bin\dot.exe'
foreach ($format in 'svg', 'png') {
    & $graphvizExe "-T$format" -Gdpi=140 `
        "$diagramFolder\stakeholders-elicitation-overview.dot" `
        -o "$diagramFolder\stakeholders-elicitation-overview.$format"
    if ($LASTEXITCODE -ne 0) { throw "Graphviz failed: $format" }
}
```

Use UTF-8 without BOM and retain source/SVG/PNG files together in version control.
Inspect rendered labels/arrows and verify file/section links after edits. Color
supports labels/shapes; meaning must remain understandable without color alone.
Keep secrets and unnecessary private material out of repository examples/evidence.

**Revision note — October 31, 2026:** Reorganized the folder guide with reading
routes, actual evidence status, authoritative handoff locations and a complete
seven-diagram catalog. Added the folder overview. No new activity, permission,
source extraction, requirement acceptance or baseline decision is recorded.

[Requirements Engineering index](../README.md) · [Process and Approach](../01-process-and-approach/README.md)

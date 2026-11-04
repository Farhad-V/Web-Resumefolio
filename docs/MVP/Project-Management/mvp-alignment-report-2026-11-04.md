# MVP Documentation Alignment — November 4, 2026

Status: documentation synchronization to the accepted owner scope/system-boundary decision. This records documentation work, not product implementation, deployment or a newly accepted requirements/design baseline.

## Current source of truth

[OWNER-MVP-2026-11-04](../SDLC/01-project-planning/owner-mvp-decision-2026-11-04.md) defines Version 1 as the MVP. [Scope](../SDLC/01-project-planning/02-scope.md), the [157-candidate release allocation](../SDLC/02-requirements-engineering/03-requirements-specification/mvp-release-allocation.md) and [ADR-005](../SDLC/04-system-design/07-design-decisions/ADR-005-owner-mvp-system-boundaries.md) carry that decision into the current project documentation.

## Changed surfaces and outcome

| Surface | Result |
| --- | --- |
| Root README and planning | Coherent current entry point; scope, purpose, constraints, assumptions/risks, deliverables, milestones, capacity and decision authority aligned |
| Requirements | All 157 candidate IDs retained with explicit release allocation; mixed issues/milestones, Kanban/Sprints, follow-up/provider and safe-content/execution records separated; primary account/media/application criteria refined |
| Scenarios, dictionary and trace/review inventories | Core/future paths distinguished; library/selected-media/application follow-up information added; earlier coverage evidence kept dated |
| Analysis | Existing seven-folder relocation preserved; context/domain/data/function/state/rules/contracts/interfaces/security/handoff allocated to MVP versus future |
| Architecture/components/data/API/security/UI/recovery | Core and separate user-scoped API ProjectForge; private same-server library and selected/range delivery; invited admission; manual follow-up; future independent communications |
| ADRs | ADR-004 added to the formerly incomplete index; ADR-005 records accepted owner boundary; ADR-001's common-application extent superseded, original proposal retained |
| Delivery/backlog/sprints | Local MVP/deferred/split allocation, historical dates retained; no GitHub issue/board changed |
| Diagrams | 151 edited/new source files; SVG/PNG exports regenerated. Current boundary/media figures, future/historical/mixed applicability and catalogs aligned. Five original shared-stem DOT/PlantUML pairs now have separate Graphviz exports |

The exact file inventory and pre/post SHA-256 values accompany the work in the local `output/mvp-alignment-2026-11-04` review package. Every existing file to be written was checked against its captured pre-edit bytes before publication; no reset, deletion or Git HEAD restoration was used.

## Verification and limits

- Local file/heading-link comparison: zero broken local targets or anchors introduced; baseline also had zero findings. Fresh exact counts are in the accompanying verification record.
- Candidate identity: 157 before/after, no duplicate primary IDs; every primary candidate keeps a release allocation. All twelve EGC and twelve YML candidates are after MVP.
- Historical planning: original accepted decision/review blocks retained verbatim in ten planning documents; older dates and estimates remain historical.
- Diagram generation: edited PlantUML/Graphviz sources rendered successfully to SVG/PNG; XML/image signatures/dimensions checked, no error diagrams accepted. Current system-boundary and private-media figures visually inspected for readable layout.
- Write integrity: source and destination bytes checked with SHA-256; existing modifications and relocated/untracked analysis/design are preserved. `index.html` and product code are outside this change.

These are document/link/source/export checks. They do not demonstrate real API interoperability, Git transfer, private range serving, security/capacity or successful restoration; those remain implementation/release verification work. Historical November 1 reviews and the old full-scope 675–1350 hour scenario were not rerun or recast as MVP results. No commit, push, purchase or live configuration is performed.

## Remaining engineering decisions

1. ProjectForge engine, physical deployment, database and supported native Git transport/client contract.
2. Core–ProjectForge API authentication/subject mapping, revocation, version/error/repetition mechanisms.
3. Supported upload/playback formats, validated type/size/quota values, safe preview/direct/range delivery behavior.
4. Backup destination, coverage/retention/recovery targets and actual isolated restore evidence.
5. Evidence-based MVP task estimates and schedule at 20 total project hours/week; no new delivery deadline inferred.

Future planning retains mail/calendar account/provider mechanisms, other provider support, advanced Git/work/execution and AI. Settled owner choices about MVP scope, invited admission, same-server media and private-mail authority are not open again.

# ADR 005 Owner Mvp System Boundaries

<a id="design-record-07-design-decisions-adr-005-owner-mvp-system-boundaries-md"></a>

<details>
<summary>ADR-005 — Owner MVP System Boundaries</summary>

<a id="design-record-07-design-decisions-adr-005-owner-mvp-system-boundaries-md--heading-adr-005--owner-mvp-system-boundaries"></a>

### ADR-005 — Owner MVP System Boundaries

Current implementation choices and scope: [Baseline](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/README.md). Runtime verification remains subject to its gates.

Status: **Accepted owner product/system boundary; physical mechanisms undecided**. Recorded November 4, 2026. Authority: Farhad through [OWNER-MVP-2026-11-04](../../01-Project-Planning/01-Project-Charter.md#release-decision).

<a id="design-record-07-design-decisions-adr-005-owner-mvp-system-boundaries-md--heading-context-and-decision"></a>

#### Context and decision

The owner defined Version 1 as the MVP and required a unified experience across a Resumefolio core and a **separate ProjectForge system joined by an authenticated user-scoped API**. This replaces ADR-001's proposed common trusted application for all nine owners. It does not reject explicit modular ownership within each system.

Core owns dashboard, invited accounts, profile/resumes/portfolio/cover letters/manual applications, protected PDFs/sharing and private My Files & Media on the same server. ProjectForge MVP owns real Git repositories/transfers/permissions/file-history, issues/simple Kanban. Commits normally occur in clients. Advanced review/merge/releases, backlog/Sprints and YAML execution/deployment are future stages.

Future communications is an independent private API system with user-consented personal Gmail/Google Calendar accounts, potentially multiple. Owner/admin has no mail-reading authority. Other providers are undecided. AI is future/Version 2 discussion.

<a id="design-record-07-design-decisions-adr-005-owner-mvp-system-boundaries-md--heading-alternatives-and-provenance"></a>

#### Alternatives and provenance

ADR-001 retains the November 2 alternatives and rationale as a historical proposal. A single trusted application spanning all nine owners no longer matches the owner's selected boundary. A forced microservice/database split for every logical owner was not selected either. This record implements a settled owner choice; it is not a newly benchmarked architecture recommendation.

<a id="design-record-07-design-decisions-adr-005-owner-mvp-system-boundaries-md--heading-consequences-and-open-engineering-decisions"></a>

#### Consequences and open engineering decisions

Core/ProjectForge API contracts must enforce current subject/resource/action scope and revocation; internal references cannot grant authority. Do not assume a shared database, cross-system transaction or physical co-deployment. ProjectForge engine, database, physical deployment, Git transport and API credential mechanism remain open. Same-server core media is settled; separate media infrastructure is future only with evidence. File policy, safe range serving, backup destination and recovery targets still need specification and verification.

<a id="design-record-07-design-decisions-adr-005-owner-mvp-system-boundaries-md--heading-verification-and-acceptance-limits"></a>

#### Verification and acceptance limits

Documentation synchronization does not implement or demonstrate API interoperability, real Git transfer, private playback, capacity, least privilege or restoration. Future verification must cover allowed/denied cross-user API/Git calls, changed grants, client-created commits, selected protected media/direct/range retrieval, independent submitted history and isolated recovery. No new delivery deadline, spending, live configuration or whole-design acceptance is authorized.

</details>

# Owner Decision — Version 1 Is the MVP

Decision key: OWNER-MVP-2026-11-04. Status: **Accepted product scope and system boundaries**. Decision authority: Farhad. Recorded November 4, 2026 (Europe/Berlin).

## Provenance and precedence

The owner explicitly requested alignment of the entire project to the final MVP decisions in the planning chat, handed off to this documentation task on November 4, 2026. This is the recorded owner decision, not an assistant proposal or a new technical baseline acceptance. It supersedes the broader October 29–November 2 Version 1 allocation where incompatible. Original DEC, candidate, scenario, PBI and ADR identifiers and dated evidence remain available. Detailed numerical policies remain proposed unless separately accepted.

## Accepted release allocation

| Area | Version 1 = MVP | Deferred / boundary |
| --- | --- | --- |
| Resumefolio core | Main dashboard, private professional profile, multiple tailored resumes and portfolios, manually authored cover letters and job applications | ApplyFlow is a former name, not a separate branded platform |
| Applications | Company/opportunity, selected resume, actual submitted materials, status, next action and follow-up date; manual submission recording | Mail/calendar connections and automatic external submission are not required for manual tracking |
| Identity | Owner/admin creates or invites initial users; scoped authentication and permissions | No open public self-registration; authentication factors/session details remain engineering decisions |
| Presentation | Explicit preview/select/apply from profile, independent resume overrides, separate publication confirmation, generated/uploaded PDFs, protected employer sharing | Profile edits cannot mutate existing resumes, publication or actual submitted history automatically |
| My Files & Media | Private user library of supported video, audio, images, text/documents and external YouTube links; optional selection per resume | Upload does not publish; no new editor or heavyweight transcoding; private uploads are not placed on YouTube |
| Media storage | Private directories on the same server as Resumefolio; validated types/sizes/quotas, safe delivery, backups and demonstrated recovery | No separate media platform/server/object-storage purchase; later separation only with justified need |
| Employer delivery | Link/password-scoped resume authorization without owner-account login; only selected media/PDFs | Direct URLs, thumbnails/previews and byte-range requests cannot bypass current authorization |
| ProjectForge | Separate system connected to core through an authenticated user-scoped API; real repositories, clone/fetch/pull/push, repository permissions, files/history, issues and simple Kanban | Full advanced review/merge/releases, advanced Product Backlog/Sprint functions and YAML execution/deployment deferred; no GitHub parity promise |
| Git semantics | Normal commits occur in the client; transfer and server-side repository access honor actual grants | No automatic server-side commit creation implied by Push or application UI |
| Communications | After MVP: independent private communications system through API, Gmail and Google Calendar connections | Explicit per-user/per-account consent and authority, potentially multiple personal Google accounts; owner/admin has no mail-reading privilege; other providers unresolved |
| AI | Future / Version 2 discussion only | No AI implementation in MVP |
| Operations | Least privilege, audit, enforceable file limits, backups, demonstrated recovery, relevant verification and operating guidance | Documentation and diagrams do not prove runtime security, capacity or recovery |

## System and responsibility boundaries

Unified user experience does not mean one trusted application containing every responsibility. The Resumefolio core and ProjectForge are distinct systems. ProjectForge's engine, physical deployment, database, transport and API credential mechanism remain undecided. Internal core modules may retain explicit logical ownership; no nine-service mandate or shared ProjectForge database/transaction is adopted. The future communications system is independently private and API connected. Cross-system references never convey authority by themselves.

## Capacity and delivery

The owner has **20 total project hours/week**, including learning, documentation, testing and operations. The November 8, 2026 target is a historical unverified target. The older 675–1350 hour / approximately 34–68 week full-scope scenario is historical, not an MVP forecast. Re-estimate the actual MVP after task decomposition and engineering evidence; this decision sets no new deadline.

## Reconciliation and acceptance

The [scope catalog](02-scope.md) allocates current and deferred capabilities. The [candidate release register](../02-requirements-engineering/03-requirements-specification/mvp-release-allocation.md) preserves candidate IDs and splits mixed criteria. [ADR-005](../04-system-design/07-design-decisions/ADR-005-owner-mvp-system-boundaries.md) records the accepted boundaries and the superseded portion of ADR-001. Historical findings/counts are dated observations; they are not fresh MVP coverage passes.

Before implementation: refine API/identity exchange and revocation, Git engine/transport/deployment/database, allowed file formats/quotas/byte-range serving, and backup destination/recovery targets. Do not reopen the owner's settled release scope, same-server media choice, private-mail authority or registration policy as open questions.

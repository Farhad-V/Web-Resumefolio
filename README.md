# Web Resumefolio

Resumefolio is a private workspace for professional profiles, tailored resumes/portfolios, cover letters and manual job applications. **Version 1 is the MVP.** Product implementation is not established by these design documents; the existing welcome page remains unchanged.

- Core: dashboard, invited accounts, explicit resume updates/publication, PDF/protected employer sharing, submitted-material history, next actions/follow-up, and private same-server My Files & Media.
- ProjectForge: separate system connected through authenticated user-scoped API; real repositories, clone/fetch/pull/push, permissions, file/history browsing, issues and simple Kanban. Git commits normally occur in the client.
- Future: independent private Gmail/Calendar communications, AI, advanced review/merge/releases, backlog/Sprints and YAML execution/deployment.

[Accepted MVP decision](docs/MVP/SDLC/01-project-planning/owner-mvp-decision-2026-11-04.md) · [Scope](docs/MVP/SDLC/01-project-planning/02-scope.md) · [Planning](docs/MVP/SDLC/01-project-planning/README.md) · [Requirements](docs/MVP/SDLC/02-requirements-engineering/README.md) · [Candidate release allocation](docs/MVP/SDLC/02-requirements-engineering/03-requirements-specification/mvp-release-allocation.md) · [Analysis](docs/MVP/SDLC/03-system-analysis/README.md) · [Design](docs/MVP/SDLC/04-system-design/README.md) · [Delivery/backlog](docs/MVP/Project-Management/product-backlog.md)

Uploads are private by default; only selected resume material is exposed through protected authorization, including direct and byte-range retrieval. Owner/admin roles never authorize reading users' future mail. Security, file limits, audit, backups and demonstrated recovery remain MVP obligations.

Capacity: 20 total project hours/week, including learning/docs/testing/operations. Historical November 8, 2026 dates and earlier full-scope estimates are not a current MVP forecast. ProjectForge engine/deployment/database, API mechanisms, numerical file policies and backup/recovery targets remain engineering decisions.

[Complete diagram alignment and inventory](docs/MVP/SDLC/diagram-alignment-review-2026-11-04.md).

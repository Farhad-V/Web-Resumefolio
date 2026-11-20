# Project Charter

## Purpose and success

Resumefolio gives invited users a private workspace to maintain a professional profile, tailor resumes and portfolios, prepare cover letters and track applications. An employer can view the specifically shared material through a protected link. The MVP succeeds when those journeys work and the applicable security, compatibility and recovery checks pass on the same release candidate.

## MVP scope

The MVP is the first planned stable release, version 1.0.0.

- **Resumefolio Core** provides a dashboard, private profiles, tailored resumes and portfolios, manually authored cover letters, private files and media, generated or uploaded PDFs, protected employer sharing and manual application tracking.
- **Accounts and sharing** use owner/admin-created or invited accounts. Employers access the selected shared material under link-scoped authorization without an owner account. Direct file access must respect the same permissions.
- **Publication and application history** require explicit preview, selection and confirmation. Profile edits do not overwrite independent resumes, published versions or the exact materials previously submitted. Each application records status, next action and follow-up.
- **ProjectForge** is a separate system linked through an authenticated, user-scoped API. It supports real Git transfers, repository permissions, file history, issues and a simple Kanban board.
- **After MVP** covers personal mail and calendar integration, AI, advanced Git review and releases, advanced ProjectForge backlog and sprint features, and user workflow execution.

## Responsibilities

Farhad owns scope decisions, development and operations. Invited account holders manage their own private materials. Employers receive only the access granted for the shared resume. Repository collaborators act within their ProjectForge grants.

See the [project management plan](02-Project-Management-Plan.md), [feasibility and risk assessment](03-Feasibility-And-Risk-Assessment.md) and [release criteria](../06-Deployment-Release/01-Deployment-Plan.md).

## Release decision

Farhad approved the MVP scope with Resumefolio Core and a separate ProjectForge system. Core owns private professional materials, controlled sharing and manual applications. ProjectForge owns Git repositories, grants, issues and a simple board. Media stays private on the Resumefolio server, and employer access covers the explicitly selected materials. The first stable MVP is planned as version 1.0.0.

The high-level requirements are invited access, creation and protected sharing of tailored presentation materials, preservation of submitted application history and grant-based ProjectForge collaboration. The [requirements specification](../02-Requirements-Engineering/01-Software-Requirements-Specification.md#requirements-specification-requirements-specification) defines the detailed behavior and acceptance criteria.

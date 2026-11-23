# Software Requirements Specification (SRS)

## Introduction

This is the requirements entry point for Resumefolio. It serves the project owner, implementation and test work. The [project charter](../../01-Project-Planning/01-Project-Charter.md#mvp-scope) defines the MVP release boundary. The [detailed specification](03-Requirements-Specification/17-Software-Requirements-Specification.md#requirements-specification-requirements-specification) and its domain documents own the individual requirement wording and acceptance criteria.

## Overall description

Resumefolio Core provides the private workspace. ProjectForge is a separate system connected through scoped authorization. The principal users are invited account holders, an owner or administrator, employers with a protected share and repository collaborators with assigned permissions. The [operating constraints](../../01-Project-Planning/03-Feasibility-And-Risk-Assessment.md#resource-constraints) cover the host, separate databases and private storage. Setup and runtime assumptions still require verification.

## Functional requirements

| Capability | Detailed requirements |
| --- | --- |
| Invited identity and resource access | [Accounts and permissions](03-Requirements-Specification/01-Accounts-Authentication-And-Permissions.md#requirements-specification-accounts-authentication-and-permissions) |
| Professional profile, independent resumes and portfolio | [Professional presentation](03-Requirements-Specification/12-Profiles-Resumes-And-Portfolio.md#requirements-specification-profiles-resumes-and-portfolio) |
| Private files, generated or uploaded PDFs and controlled employer sharing | [Files and operations](03-Requirements-Specification/02-Administration-Files-And-Operational-Behavior.md#requirements-specification-administration-files-and-operational-behavior) and [PDF and sharing](03-Requirements-Specification/11-Pdf-And-Controlled-Sharing.md#requirements-specification-pdf-and-controlled-sharing) |
| Manual applications and immutable submitted history | [Application management](03-Requirements-Specification/09-Manual-Application-Management.md#requirements-specification-manual-application-management) and [business rules](03-Requirements-Specification/04-Business-Rules-And-Data-Lifecycle.md#requirements-specification-business-rules-and-data-lifecycle) |
| Scoped ProjectForge repositories, issues and simple Kanban | [Git collaboration](03-Requirements-Specification/08-Git-Hosting-And-Collaboration.md#requirements-specification-git-hosting-and-collaboration) and [work management](03-Requirements-Specification/13-Projects-Kanban-And-Sprints.md#requirements-specification-projects-kanban-and-sprints) |

## Non-functional requirements

Use the [quality, security and recovery requirements](03-Requirements-Specification/14-Quality-Security-And-Recovery-Requirements.md#requirements-specification-quality-security-and-recovery-requirements) for authorization, performance, accessibility, availability, resilience and operational checks. Preserve the recorded status of any proposed thresholds or compliance targets. Verification applies to the actual release candidate.

## External interfaces

The [interface requirements](03-Requirements-Specification/07-External-Interface-Requirements.md#requirements-specification-external-interface-requirements) cover user-facing interactions, service boundaries, supported communication and integration behavior. Technical details are in the [system design](../../01-Project-Planning/02-Project-Management-Plan.md#stage-4-system-design).

## Supporting evidence and changes

- [Business goals](03-Requirements-Specification/03-Business-Requirements.md#requirements-specification-business-requirements) and [stakeholder needs](02-Stakeholders-And-Elicitation/04-Stakeholders-And-Elicitation.md#stakeholders-and-elicitation-stakeholders-and-elicitation)
- [User stories and scenarios](04-Scenarios-And-Models/02-User-Stories-And-Scenarios.md#scenarios-and-models-user-stories-and-scenarios) and [analysis models](../../03-System-Analysis/01-System-Context-And-Gap-Analysis.md)
- [Glossary](05-Data-Definitions/03-Requirements-Glossary.md#data-definitions-glossary) and [data dictionary](05-Data-Definitions/02-Data-Dictionary.md#data-definitions-data-dictionary)
- [Decisions and open issues](07-Change-And-Baseline/03-Requirements-Questions-And-Decisions.md#change-and-baseline-open-questions-and-decisions), [review and evidence](06-Validation-And-Traceability/07-Validation-And-Traceability.md#validation-and-traceability-validation-and-traceability) and [change control](07-Change-And-Baseline/02-Requirements-Change-Control.md#change-and-baseline-change-control)
- [Product backlog](../02-Product-Backlog/README.md) and [requirements traceability matrix](../03-Requirements-Traceability-Matrix/README.md)

## Topic files

- [Process and Approach](01-Process-And-Approach/README.md)
- [Stakeholders and Elicitation](02-Stakeholders-And-Elicitation/README.md)
- [Requirements Specification](03-Requirements-Specification/README.md)
- [Scenarios and Models](04-Scenarios-And-Models/README.md)
- [Data Definitions](05-Data-Definitions/README.md)
- [Validation and Traceability](06-Validation-And-Traceability/README.md)
- [Change and Baseline](07-Change-And-Baseline/README.md)
- [Working agreement for requirement changes](08-Working-Agreement-For-Requirement-Changes.md)

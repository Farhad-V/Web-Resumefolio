# Resumefolio — Version 1 Scope

| Item | Current position |
|---|---|
| Project owner | Farhad Valizadegan; sole project delivery and operations owner |
| Document status | Scope boundaries accepted; detailed behavior and technical feasibility remain under investigation |
| Original decisions | DEC-009 through DEC-028, accepted October 29–30, 2026 |
| Planning baseline | Accepted with tracked follow-up under [DEC-116](10-planning-completion-criteria.md#dec-116) |
| Presentation revision | October 31, 2026; existing decisions and conditions retained |

**At a glance:** Version 1 brings professional presentation, manual job
application management, work management, and real Git collaboration into one
controlled-access environment. AI features, automatic translation, and legacy
demo migration are outside this release.

**Use this document to answer:** What is included? What is excluded? Which
conditions and unresolved details must be addressed before delivery decisions?
Inclusion is a product commitment, not proof of implementation or feasibility.

[Overview](#1-scope-overview) · [Included capabilities](#2-in-scope-capability-catalog)
· [Exclusions](#3-out-of-scope-for-version-1) · [Boundaries](#4-planning-boundaries)
· [Open definitions](#5-open-definitions-and-review-gates) · [Decision records](#6-accepted-scope-decision-records)

## 1. Scope Overview

![Version 1 inclusions, exclusions, and conditions](diagrams/scope-boundaries.png)

[Open scalable diagram](diagrams/scope-boundaries.svg) ·
[Editable Graphviz source](diagrams/scope-boundaries.dot)

The diagram groups the agreed boundaries. Its arrows describe classification,
not software architecture, data flow, delivery order, or completed capabilities.
The catalog below is the detailed planning reference.

## 2. In-Scope Capability Catalog

SCP references are navigation labels for this catalog, not new requirements.
Each row links to the original decision and its rationale. Detailed fields,
behavior, and testable acceptance criteria belong in Requirements Engineering.

| Ref. | Included capability | Boundary that must be preserved | Decision |
|---|---|---|---|
| SCP-01 | Individual accounts, roles, permissions, and unified sign-in | Sign-in does not grant access to unrelated private data or operations | [DEC-028](#dec-028) |
| SCP-02 | Professional profiles and opportunity-specific resumes | Reuse shared information while preserving independent resume selections, presentation, and overrides | [DEC-027](#dec-027) |
| SCP-03 | Portfolio and supporting evidence for skills/projects | Add, organize, and display externally created text, media, files, diagrams, and links; select evidence per resume | [DEC-026](#dec-026) |
| SCP-04 | Generated resume PDFs and uploaded PDFs | Per-resume download selection: generated, uploaded, both, or neither; separate English/German uploaded PDFs with language-specific availability | [DEC-025](#dec-025) |
| SCP-05 | Password-protected employer sharing without a viewer account | Share only the intended resume and selected content; protect direct file/PDF retrieval; owner can change password or disable link | [DEC-024](#dec-024) |
| SCP-06 | Manual ApplyFlow | Record company/position, associate resume, manually write cover letter, track progress, and preserve the materials actually submitted | [DEC-023](#dec-023) |
| SCP-07 | Gmail and calendar capabilities with Google Calendar integration | Read, compose, send, and reply; coordinate interviews, deadlines, follow-ups, and other agreed activities under explicit synchronization rules | [DEC-022](#dec-022) |
| SCP-08 | Projects, Kanban, boards, tasks, authorized collaboration, Product Backlogs, Backlog Items, Sprints, and Sprint Backlogs | A backlog item may be refined into tasks; one Sprint Backlog combines the Sprint Goal, selected items, and delivery plan | [DEC-021](#dec-021) |
| SCP-09 | Real Git hosting and collaboration | Create repositories; Clone/Fetch/Pull/Push; branches, file/history browsing; Fork, PR, comments, review and Merge; Issues, Milestones, Tags and Releases | [DEC-020](#dec-020) |
| SCP-10 | Real YAML workflow and CI/CD execution | Subject to early feasibility, security and resource analysis; define isolation, permissions, secrets, cleanup, limits and deployment approvals | [DEC-019](#dec-019) |
| SCP-11 | Owner-configurable upload and storage limits | Administration policies must respect actual infrastructure and processing capacity | [DEC-018](#dec-018) |
| SCP-12 | Deployment and operational readiness | Setup/maintenance guidance, backups, demonstrated restoration, and verification of agreed core workflows | [DEC-017](#dec-017) |

### Important distinctions

- **Application history versus live sharing:** Submitted resume/cover-letter copies remain preserved; a live employer view can reflect later saved changes according to explicit requirements.
- **Product capability versus development tool:** Resumefolio's Kanban and Git hosting are product features. The GitHub board and repository used to build the product do not demonstrate those features are implemented.
- **Backlog item versus task:** Product Backlog Items can represent features, defects, improvements, or investigations; they are not necessarily single implementation tasks.
- **Unified sign-in versus permission:** A collaborator invited to a board must not gain access to private email, unrelated resumes, or repositories merely through that invitation.
- **Access revocation versus downloaded copies:** Download controls govern product retrieval; disabling a link cannot remove a copy already legitimately downloaded.

## 3. Out of Scope for Version 1

| Exclusion | What remains supported | Reason / decision |
|---|---|---|
| AI-assisted analysis, recommendations, and content generation | Users analyze opportunities and prepare application content manually | Focus on core workflows and reduce additional dependencies; [DEC-016](#dec-016) |
| Automatic translation of resume content | Manually entered and reviewed English and German content | Keep professional wording under user control; [DEC-015](#dec-015) |
| Automatic migration of old demo accounts and data | Enter required information through normal new-product workflows; preserve the existing demo | Avoid legacy mapping/validation work in this release; [DEC-014](#dec-014) |

Additional limits of the accepted inclusions:
- Adding video or diagrams does not include building an in-product video editor or diagram-authoring tool.
- Recording an application as submitted does not add automatic submission to external job platforms.
- YAML workflows do not imply compatibility with every GitHub Actions workflow.
- Using reference projects does not automatically include every feature found in them.

These clarifications preserve the recorded decisions; they do not remove an
agreed capability. Later inclusion of an excluded feature needs its own scope decision.

## 4. Planning Boundaries

| Boundary | Agreed position | Source decision |
|---|---|---|
| Initial deployment | Target 10 users on the existing server; workload, concurrency and capacity require evidence | [DEC-013](#dec-013) |
| Future growth | Consider growth toward approximately 1,000 users without claiming that capacity is supported by the initial infrastructure | [DEC-013](#dec-013) |
| Budget | Use existing resources; do not assume paid services, paid APIs, or extra infrastructure. Document need, alternatives, costs and consequences for an owner decision | [DEC-012](#dec-012) |
| Reference projects | MultiResume Manager, Git Hosting Platform, OmniDesk, and KanbanFlow remain unchanged; treat them as references, not automatic specifications | [DEC-011](#dec-011) |
| Requirements detail | Scope states inclusions/exclusions; Requirements Engineering defines behavior and acceptance criteria | [DEC-010](#dec-010) |
| Delivery and change | Milestones/Sprints organize delivery without silently removing scope; material changes require rationale, impact assessment and owner decision | [DEC-010](#dec-010) |

Technical constraints such as Laravel and object-oriented development remain in
[Resources and Constraints](05-resources-and-constraints.md). This document does
not select the final architecture, frontend, database, Git engine, or runner.

## 5. Open Definitions and Review Gates

The following accepted follow-up remains open. The project owner coordinates
all items. A pending definition neither excludes its capability nor establishes
that it is technically feasible.

| Open topic | Required next step | Review gate | Existing tracking |
|---|---|---|---|
| Email and calendar operations | Define operations, views, account selection, synchronization, conflicts, reminders and disconnection behavior; validate provider access | Before accepting related requirements; validate access before dependent development | PBI-004, PBI-017, PBI-018; M-02/M-03; GAP-D02 |
| Kanban behavior, reporting, and automation | Specify item/task relationships, workflows and completion conditions; evaluate design | Requirements review, then analysis/design before dependent commitments | PBI-008, PBI-019; M-02/M-03; GAP-D06 |
| YAML syntax and CI/CD limits | Investigate execution feasibility early; define supported behavior, isolation, secret handling and limits | Before accepting execution design or enabling execution; verify controls before acceptance | PBI-003, PBI-023; M-03/M-08; GAP-D09 |
| File types, upload limits, and quotas | Define policy; inspect actual capacity and verify enforcement | Requirements and design; verify before affected capability acceptance | PBI-002, PBI-013; M-02/M-03; GAP-D01/GAP-D10 |
| Performance, backup, recovery, and availability targets | Define measurable targets; justify design against resources and retain actual verification/restoration evidence | Requirements and design, with evidence before release | PBI-002, PBI-006, PBI-026, PBI-027; M-02/M-03/M-09; GAP-D04/GAP-D10 |

The original assignment and rationale are preserved under [DEC-009](#dec-009).
The accepted GAP follow-up is in
[Planning Completion Criteria](10-planning-completion-criteria.md).

### How inclusion becomes an accepted capability

![Review gates between scope inclusion and capability acceptance](diagrams/scope-review-gates.png)

[Open scalable diagram](diagrams/scope-review-gates.svg) ·
[Editable Graphviz source](diagrams/scope-review-gates.dot)

This is a gate overview, not a dated roadmap or an instruction to finish all
investigations sequentially. Investigate high-impact feasibility questions early,
use feedback to revise affected documents, and keep scope changes explicit.
The agreed initial SDLC documentation, delivery-plan reconciliation, and
pre-implementation baseline precede product coding.

Scheduling and milestone definitions remain in
[Roadmap and Milestones](08-roadmap-and-milestones.md). Current dates are
provisional; this revision does not change GitHub assignments or dates.

## 6. Accepted Scope Decision Records

The expandable record below preserves the original twenty decision sections,
their identifiers, acceptance dates, rationale, detailed limits, and follow-up.
The short tables above are a reading aid; these records retain the detailed
accepted wording. References in the [Planning Decision Register](decision-register.md)
continue to point to their stable anchors.

Some original entries say overall baseline acceptance is separate. They record
the review stage at that time; the later planning-only acceptance is DEC-116.
Neither that acceptance nor this presentation revision claims technical delivery.

<details>
<summary>Original accepted scope decisions — expand or collapse</summary>

### Accounts, Roles, Permissions, and Unified Sign-in Review

Decision ID: DEC-028
<a id="dec-028"></a>

Status: Accepted by the project owner as included in Version 1
Review date: October 29, 2026

Decision: Include individual user accounts, application roles,
resource and operation permissions, and unified sign-in across
authorized product sections.

Rationale: Private workflows depend on identifiable users and
controlled access. Unified sign-in reduces repeated authentication
without granting unrestricted access to other users' information.

For example, a collaborator invited to a Kanban board must not gain
access to the owner's private email or resumes through that invitation.

Detailed role rules, account lifecycle, authentication flows, and
acceptance criteria will be defined in Requirements Engineering.
This decision confirms scope inclusion only; it does not establish
implementation or acceptance of the whole scope document or baseline.

### Professional Profiles and Tailored Resumes Review

Decision ID: DEC-027
<a id="dec-027"></a>

Status: Accepted by the project owner as included in Version 1
Review date: October 29, 2026

Decision: Include professional profiles containing experience,
education, skills, and other agreed professional information.
Allow users to create tailored resumes for individual job
opportunities by selecting relevant information and adjusting
presentation without repeatedly entering shared information.

Resume-specific selections, layouts, and content overrides remain
independent. Intended updates from shared profile information must
follow explicit requirements and preserve resume-specific overrides.

Rationale: Support professional, opportunity-specific applications
while reducing duplicated data entry and unintended cross-resume
changes.

Detailed fields, editing workflows, propagation rules, and acceptance
criteria will be specified in Requirements Engineering. This review
confirms inclusion, not implementation or overall baseline acceptance.

### Portfolio and Supporting Evidence Review

Decision ID: DEC-026
<a id="dec-026"></a>

Status: Accepted by the project owner as included in Version 1
Review date: October 29, 2026

Decision: Allow users to add, organize, and display supporting
content associated with individual skills and projects, including
explanatory text, images, video, files, diagrams, and repository or
other relevant links. Users select which evidence appears in each
tailored resume and is available through its controlled sharing.

Rationale: Help employers assess concrete examples of professional
work and understand the user's contribution, rather than relying
only on a list of claimed skills. Per-resume selection keeps the
presentation relevant to the specific opportunity.

This inclusion covers adding and displaying content created using
external tools. Building an in-product video editor or diagram
authoring tool is not included by this decision.

Supported formats, storage and upload limits, rendering behavior,
and access-control acceptance criteria will be defined in
Requirements Engineering and System Design.

### Generated and Uploaded Resume PDFs Review

Decision ID: DEC-025
<a id="dec-025"></a>

Status: Accepted by the project owner as included in Version 1
Review date: October 29, 2026

Decision: Support PDF generation from an authored resume and upload
of a separately prepared resume PDF. For each resume, the owner can
make the generated PDF, uploaded PDF, both, or neither available
for employer download. English and German uploaded PDFs can be
provided separately, with availability controlled by language.

Rationale: Provide a portable, printable resume while allowing the
user to offer an externally prepared document when preferred.
Per-resume and language-specific download controls support tailored
presentation without requiring every available PDF to be shared.

PDF retrieval must follow the resume's access-control rules;
a direct file URL must not bypass authorization. Download controls
apply to retrieval through the product and do not revoke copies
already legitimately downloaded by an employer.

Template, formatting, pagination, language fallback, and generation
acceptance criteria will be defined in Requirements Engineering.
This decision confirms scope inclusion, not implementation.

### Password-Protected Resume Sharing Review

Decision ID: DEC-024
<a id="dec-024"></a>

Status: Accepted by the project owner as included in Version 1
Review date: October 29, 2026

Decision: Provide a password-protected link for a resume tailored
to a specific job opportunity. An employer does not need a user
account and may access only that resume and the content selected
for sharing. The resume owner can change the password or disable
the link to stop subsequent access through it.

Rationale: Make employer access straightforward while retaining
owner control over which professional information is shared.
An employer link must not grant access to the private workspace
or unrelated resumes, files, email, or collaboration resources.

Shared files and PDFs follow the same authorization boundary.
Disabling access does not remove copies already legitimately
downloaded. Detailed password-change, active-session revocation,
and link lifecycle behavior will be specified and tested through
Requirements Engineering.

This decision confirms inclusion in scope, not implementation
or acceptance of the overall planning baseline.

### Manual ApplyFlow Review

Decision ID: DEC-023
<a id="dec-023"></a>

Status: Accepted by the project owner as included in Version 1
Review date: October 29, 2026

Decision: Allow users to record the company and job position for
an application, associate the relevant resume, manually write the
cover letter, and track application progress through agreed
statuses such as preparation, submission, interview, and outcome.
Preserve the resume and cover letter actually submitted so later
source edits do not overwrite application history.

Rationale: Maintain a clear, traceable record of each application,
its materials, progress, and outcome. Analysis and decisions remain
with the user in Version 1; AI-assisted analysis and drafting are
outside this release's scope.

Detailed fields, status transitions, submission-recording workflows,
and archive behavior will be defined in Requirements Engineering.
Recording an application as submitted does not itself establish
an automated submission integration.

This decision confirms scope inclusion, not implementation.

### Email and Calendar Review

Decision ID: DEC-022
<a id="dec-022"></a>

Status: Accepted by the project owner as included in Version 1
Review date: October 30, 2026

Decision: Allow users to connect their Gmail accounts and read,
compose, send, and reply to email within Resumefolio. Provide a
calendar for interviews, deadlines, follow-ups, personal activities,
and project-related schedules, with Google Calendar integration
according to explicitly defined synchronization rules.

Users can relate relevant correspondence and scheduled activities
to their job-application work. Classification and decisions remain
user-directed in Version 1; AI analysis is not included.

Rationale: Reduce switching between tools and support coherent
tracking of professional communications, dates, and follow-up actions.
Email and calendar data remain subject to the user's permissions
and must not become accessible merely through a collaboration invite.

Detailed email operations, calendar views, account-selection rules,
reminders, synchronization, conflicts, disconnection behavior, and
acceptance criteria will be specified in Requirements Engineering.
Provider access, quotas, delivery behavior, and infrastructure
requirements still require validation.

This decision confirms scope inclusion, not implementation or
acceptance of the overall planning baseline.

### Kanban and Work Management Review

Decision ID: DEC-021
<a id="dec-021"></a>

Status: Accepted by the project owner as included in Version 1
Review date: October 30, 2026

Decision: Provide projects, boards, configurable columns, tasks,
assignments, priorities, due dates, authorized collaboration,
Product Backlogs, Backlog Items, Sprints, and Sprint Backlogs
within the Resumefolio product.

A Product Backlog is a list of Backlog Items. Items may represent
features, defects, technical improvements, or investigations and
may be refined into smaller implementation tasks. A Backlog Item
and a task are not necessarily the same thing.

For each Sprint, selected Backlog Items, the Sprint Goal, and the
plan for delivering them form one Sprint Backlog. Detailed item
relationships, workflow rules, and completion criteria will be
specified in Requirements Engineering.

Rationale: Turn planned outcomes into traceable work, support
prioritization and incremental delivery, and coordinate collaboration
while limiting each participant to authorized resources.

This is a capability of the Resumefolio application. The GitHub
project currently used to build Resumefolio is a separate delivery
tracking tool and does not establish that this capability exists.

This decision confirms scope inclusion, not implementation or
acceptance of the overall planning baseline.

### Real Git Hosting and Collaboration Review

Decision ID: DEC-020
<a id="dec-020"></a>

Status: Accepted by the project owner as included in Version 1
Review date: October 30, 2026

Decision: Provide actual Git repository hosting within Resumefolio,
including repository creation, Clone, Fetch, Pull, Push, branches,
file and history browsing, Fork, Pull Requests, review, comments,
and Merge. Include repository Issues, Milestones, Tags, and Releases.

Rationale: Support storage, presentation, and collaboration on real
project code in the unified product rather than merely displaying
links to repositories hosted elsewhere.

This product capability is distinct from using GitHub to develop
Resumefolio. CI/CD execution is a separate scope item and is not
established by accepting Git hosting.

Repository visibility, permissions, access credentials, collaboration
rules, merge conflicts, release assets, storage limits, and
acceptance criteria will be specified in Requirements Engineering.
Implementation and infrastructure choices require subsequent
analysis and design; this decision does not select a Git engine.

This review confirms inclusion, not implementation or acceptance
of the overall planning baseline.

### YAML Workflows and CI/CD Review

Decision ID: DEC-019
<a id="dec-019"></a>

Status: Accepted by the project owner as included in Version 1,
subject to security and resource analysis before implementation
Review date: October 30, 2026

Decision: Provide YAML-defined workflows for repeatable project
checks, test execution, builds, and execution results and logs.
Deployment can be a separate, explicitly controlled workflow stage;
a code Push must not inherently authorize production deployment.

Rationale: Make verification and release preparation repeatable
and traceable rather than relying solely on ad hoc manual steps.
Actual workflow execution is distinct from Git integrity checks.

Before implementation, analyze execution isolation, authorization,
secret protection, cleanup, and resource limits against the existing
infrastructure. Supported YAML syntax, triggers, runner behavior,
artifacts, and deployment approvals require explicit requirements
and design. Compatibility with all GitHub Actions workflows is not
implied by this scope decision.

This decision confirms the intended release scope, not demonstrated
feasibility, implementation, or permission to execute arbitrary
project workloads on the production server. Any feasibility conflict
must be documented and reviewed without silently reducing scope.

### Owner-Configurable File Limits Review

Decision ID: DEC-018
<a id="dec-018"></a>

Status: Accepted by the project owner as included in Version 1
Review date: October 30, 2026

Decision: Allow the platform owner to configure maximum upload
sizes and storage consumption limits through the administration
interface rather than fixing these policy values in application
code. Effective limits must respect actual infrastructure capacity.

Rationale: Adapt storage policy as needs and available resources
change while reducing the risk of exhausting shared server storage.
Configuration does not create additional physical storage or remove
infrastructure and processing constraints.

Numerical defaults, quota scope, file-type rules, validation,
behavior when limits are changed, and acceptance criteria will be
defined in Requirements Engineering and System Design. No specific
upload size or storage capacity is promised by this decision.

This review confirms scope inclusion, not implementation or
acceptance of the overall planning baseline.

### Deployment and Operational Readiness Review

Decision ID: DEC-017
<a id="dec-017"></a>

Status: Accepted by the project owner as included in Version 1
Review date: October 30, 2026

Decision: Include deployment on the target server, setup and
maintenance guidance, backup procedures, demonstrated restoration,
and verification of agreed core product workflows as release work.

Rationale: Source code alone does not establish a usable delivery.
The application must be operable, maintainable, and recoverable,
with reviewable evidence rather than untested procedures alone.

Deployment, Testing, and Maintenance documentation will define
procedures and measurable readiness criteria. Infrastructure and
recovery assumptions still require validation. Acceptance of this
scope item does not establish that deployment, verification, or
restoration has already been executed successfully.

This review confirms scope inclusion. All inclusion decisions have
now been reviewed individually; exclusions, planning boundaries,
open definitions, and overall baseline acceptance remain separate.

### AI Capabilities Exclusion Review

Decision ID: DEC-016
<a id="dec-016"></a>

Status: Accepted by the project owner as excluded from Version 1
Review date: October 30, 2026

Decision: Defer AI-assisted job-ad analysis, recommendations,
and resume or cover-letter content generation to a later version.
In Version 1, users perform the analysis, make decisions, and
prepare their application content manually.

Rationale: Focus on the core product workflows while reducing
additional technical, infrastructure, integration, and cost
dependencies. Manual ApplyFlow remains included in Version 1.

This exclusion concerns AI features in the delivered application.
A later AI release requires its own requirements, feasibility,
resource, privacy, and acceptance analysis. No AI delivery date,
model, or deployment arrangement is established by this decision.

### Automatic Translation Exclusion Review

Decision ID: DEC-015
<a id="dec-015"></a>

Status: Accepted by the project owner as excluded from Version 1
Review date: October 30, 2026

Decision: Retain English and German resume content, with users
manually entering and reviewing each language version. Automatic
translation of resume content is not included in Version 1.

Rationale: Keep users in control of the accuracy of professional
content while avoiding an additional translation-service dependency.
Multilingual content support and automatic translation are separate
capabilities; excluding translation does not remove language support.

Detailed language selection, missing-content behavior, and
language-specific PDF rules remain subject to Requirements
Engineering. This review does not add translation in a later release
without a separate scope decision.

### Existing Demo Migration Exclusion Review

Decision ID: DEC-014
<a id="dec-014"></a>

Status: Accepted by the project owner as excluded from Version 1
Review date: October 30, 2026

Decision: Do not require automatic migration of accounts or data
from the existing demo into the new Version 1 application. Required
information can be entered into the new product through its normal
workflows.

Rationale: Allow the new data model and rules to be established
without adding legacy migration mapping and validation work to
this release.

This exclusion does not authorize deletion, modification, or
shutdown of the existing demo or its data. Any later migration or
retirement decision requires separate analysis and authorization.

This entry records the exclusion review. See the Scope Document
Review Summary for the current overall document review status.

### Initial Capacity and Growth Boundary Review

Decision ID: DEC-013
<a id="dec-013"></a>

Status: Accepted by the project owner as a planning boundary
Review date: October 30, 2026

Decision: Target initial deployment for 10 users on the existing
server. Consider gradual growth toward approximately 1,000 users
in design, without asserting that the initial infrastructure has
been verified to support that larger capacity.

Rationale: Align near-term delivery with current needs and budget
while retaining a deliberate growth direction. Design intent and
verified operational capacity are different claims.

The user count does not by itself define simultaneous load.
Workload assumptions, performance targets, resource inspection,
and capacity-test evidence must be established before accepting
operational capacity. Future growth may require further tuning,
resources, and explicit decisions; it is not promised by this review.

### Budget and Additional Spending Boundary Review

Decision ID: DEC-012
<a id="dec-012"></a>

Status: Accepted by the project owner as a planning boundary
Review date: October 30, 2026

Decision: Plan against the existing server and currently available
resources. Do not assume additional servers, paid services, or
paid APIs as available project resources.

If technical analysis identifies a need for additional spending,
document the need, alternatives, expected costs, and effects on
scope, quality, and delivery. The project owner decides whether
to authorize the proposed expenditure or another response.

Rationale: Keep architecture and delivery planning aligned with
actual financial capacity rather than relying on unapproved costs.
This boundary does not establish that every agreed capability is
feasible at the current budget; conflicts require explicit review
and must not cause silent scope reduction.

### Existing Reference Projects Boundary Review

Decision ID: DEC-011
<a id="dec-011"></a>

Status: Accepted by the project owner as a planning boundary
Review date: October 30, 2026

Decision: Use the earlier MultiResume Manager, Git Hosting Platform,
OmniDesk, and KanbanFlow projects as references for understanding
capabilities and prior experience. Do not modify those projects
as part of developing Resumefolio.

The presence of a feature in a reference project does not
automatically include it in Resumefolio. Select capabilities through
explicit product requirements and scope decisions, distinguishing
implemented behavior from documented proposals.

Rationale: Preserve existing projects and make deliberate choices
based on the new product's needs rather than importing prior
assumptions or treating sample behavior as an approved specification.

This review records a working boundary; it does not establish that
all reference code has been reviewed, tested, or selected for reuse.

### Requirements Detail and Controlled Scope Change Review

Decision ID: DEC-010
<a id="dec-010"></a>

Status: Accepted by the project owner as planning boundaries
Review date: October 30, 2026

Decision: Use Scope to identify Version 1 inclusions and exclusions.
Define detailed behavior and testable acceptance criteria in
Requirements Engineering, maintaining traceability to scope.

Milestones and Sprints organize delivery rather than silently
removing agreed capabilities. Significant scope changes require
a documented rationale, impact assessment, and project-owner decision.

Rationale: Separate product boundaries from detailed specifications
while allowing controlled revision as understanding improves.
Delivery sequencing must not conceal changes to the agreed product.

This entry records the planning-boundary review. See the Open
Definitions and Follow-up Review and Scope Document Review Summary
for the current status. Overall baseline acceptance is separate.

### Open Definitions and Follow-up Review

Decision ID: DEC-009
<a id="dec-009"></a>

Status: Follow-up approach accepted by the project owner;
detailed definitions and feasibility remain open
Review date: October 30, 2026

Decision: Track the following unresolved details with a responsible
person and review point. Deferral does not exclude the capability
or demonstrate its feasibility. The project owner coordinates each
item.

| Open topic | Responsible person | Review point | Related tracking |
|---|---|---|---|
| Detailed email and calendar operations | Project owner | Define during Requirements Engineering before accepting the related requirements; validate provider access before dependent implementation | PBI-004, PBI-017, PBI-018; M-02 and M-03 |
| Kanban workflows, reporting, and automation | Project owner | Define and review behavior during Requirements Engineering; assess implementation approach during System Analysis and System Design | PBI-008, PBI-019; M-02 and M-03 |
| Supported YAML syntax and CI/CD execution limits | Project owner | Investigate feasibility early; agree supported behavior and isolation before accepting CI/CD design or enabling execution | PBI-003, PBI-023; M-03 and M-08 |
| File types, upload limits, and storage quotas | Project owner | Define policy during Requirements Engineering; validate capacity and enforcement during System Design and before capability acceptance | PBI-002, PBI-013; M-02 and M-03 |
| Performance, backup, recovery, and availability targets | Project owner | Define measurable targets during Requirements Engineering; validate design against resources and record verification evidence before release | PBI-002, PBI-006, PBI-026, PBI-027; M-02, M-03 and M-09 |

Rationale: Keep unresolved details visible and owned without
pretending they are settled or silently reducing agreed scope.
Record findings, evidence, and any resulting decisions in the
relevant authoritative documents and linked work items.

</details>

## 7. Document Review and Revision Summary

The project owner accepted the inclusions, exclusions, planning boundaries,
and follow-up approach on October 29–30, 2026. Planning baseline acceptance
was recorded separately under [DEC-116](10-planning-completion-criteria.md#dec-116).
Detailed requirements and technical validation remain open at their assigned gates.

**Editorial revision — October 31, 2026:** Replaced inherited section numbering
with a local document structure, added a capability catalog and clear boundary
tables, and embedded two Graphviz diagrams. The twenty original decision records
are preserved below the reading summary. No accepted capability, exclusion,
resource constraint, or provisional delivery date was changed. Earlier hashes
and baseline evidence continue to identify their original snapshots.

## 8. Diagram Sources and Regeneration

The two diagrams added to this document use Graphviz. Each has an editable
`.dot` source, a scalable `.svg`, and a `.png` preview in `diagrams/`.
The earlier `version-1-scope.puml` and its image remain unchanged as the original
planning mind map linked from the planning index; the catalog and accepted
records here explain its summarized capability groups and conditions.

Run from the repository root in PowerShell:

```powershell
$diagramFolder = 'docs\SDLC\01-project-planning\diagrams'
$graphvizExe = 'C:\Program Files\Graphviz\bin\dot.exe'

foreach ($name in 'scope-boundaries', 'scope-review-gates') {
    foreach ($format in 'svg', 'png') {
        & $graphvizExe "-T$format" -Gdpi=140 `
            "$diagramFolder\$name.dot" -o "$diagramFolder\$name.$format"
        if ($LASTEXITCODE -ne 0) {
            throw "Graphviz failed: $name ($format)"
        }
    }
}
```

Save DOT sources as UTF-8 without BOM. Review images and related text together
whenever a boundary, label, or condition changes.

# Stakeholders and Responsibilities

## 7. Stakeholders and Responsibilities

Status: Reviewed - accepted planning-level direction

### 7.1 Stakeholders

| Stakeholder | Main interest |
|---|---|
| Project owner: Farhad Valizadegan | Product direction, delivery, budget, and long-term operation |
| Platform owner | Overall administration and operational control |
| Administrators | Account management and authorized content administration |
| Registered users | Professional presentation, applications, and related work |
| Invited collaborators | Authorized collaboration on projects, boards, and repositories |
| Employers and resume viewers | Access to the specific resume and evidence shared with them |

One person may hold multiple roles.
Project ownership and platform permissions are distinct concepts.

External dependencies include the hosting provider, Google
integrations, and email delivery services. Their availability,
limits, and connection requirements must be considered.

### 7.2 Project Responsibilities

| Activity | Responsibility |
|---|---|
| Product goals and business decisions | Project owner |
| Scope, priorities, and budget decisions | Project owner, supported by analysis and recommendations |
| Planning and requirements documentation | Developed with the project owner through guided, reviewable steps |
| Technical analysis and design | Prepared by the project owner and evaluated against requirements, resources, and constraints |
| Implementation | Project owner |
| Verification | Project owner; review requirements, run relevant checks, and retain evidence |
| Deployment and operation | Project owner; no separate operations person is currently assigned |
| Release decisions | Project owner, informed by verification and operational readiness |

No separate staffed team or continuous monitoring of the deployed
product is assumed.

### 7.3 Working Agreement

- Progress step by step through PowerShell.
- Explain each command and its expected result.
- Review actual output before dependent steps.
- Keep confirmed decisions, proposals, assumptions, and
  unresolved matters clearly distinguished.
- Record important decisions, their rationale, alternatives where
  material, and their impact. Preserve reasons for later revisions.
- Do not repeatedly request content approval already given.
  Tool-required file-access approvals are distinct from content review.
- Keep planning documents and diagrams consistent.
- Include readable diagrams alongside written explanations in analysis
  and design documentation. Preserve editable Graphviz or PlantUML
  sources and rendered images, and revise both when decisions change.
- Preserve project progress through focused Git commits.
- Group related questions and discuss significant decisions.
- Reflect the project owner's ownership in project materials.

### 7.4 Boundary with Requirements Engineering

This section identifies stakeholders and delivery responsibilities.
Detailed permissions, role restrictions, invitation behavior,
and account lifecycle rules belong in Requirements Engineering.

## Review Decisions

### Stakeholder Classification Review

Decision ID: DEC-032
<a id="dec-032"></a>

Status: Accepted by the project owner for this section
Review date: October 30, 2026

Decision: Identify the project owner, platform owner,
administrators, registered users, invited collaborators, and
employers or resume viewers as stakeholder groups.

Project ownership covers product direction, budget, and delivery
decisions. Platform ownership is an administrative role within
the application. One person may hold both roles.

Rationale: Distinguish responsibility for creating and delivering
the product from permissions for operating and using it. Clarifying
these perspectives supports subsequent responsibility assignments
and requirements without treating project ownership itself as a
complete application permission specification.

Detailed roles and access rules remain in Requirements Engineering.
This entry records the stakeholder decision. See the Document Review
Summary for current document status; overall baseline acceptance
requires a separate review.

### Current Solo Delivery Arrangement

Decision ID: DEC-031
<a id="dec-031"></a>

Status: Current arrangement confirmed by the project owner
Review date: October 30, 2026

The project owner is the sole person advancing the project.
There is currently no separate delivery team, developer, tester,
or operations person. Planning, requirements, analysis, design,
implementation, verification, deployment, and maintenance are
responsibilities carried by the same person.

Role names describe responsibilities, not additional staff.
Stakeholder and application-role groups do not imply that those
positions are currently staffed by other people.

Rationale: Keep responsibility assignments, workload planning,
and operational expectations aligned with actual staffing.
No independent review team or continuous operational coverage is assumed. Any future staffing change
must be reflected explicitly in these assignments.

### Working Agreement Review

Decision ID: DEC-030
<a id="dec-030"></a>

Status: Accepted by the project owner for this section
Review date: October 30, 2026

Decision: Work step by step through PowerShell and review actual
outputs. Keep confirmed decisions, proposals, assumptions, and
verified results distinct. Record the rationale for significant
decisions and revisions, keep related documents consistent, and
avoid asking again for content approval already provided.

Rationale: Support a traceable, understandable solo-development
process with reviewable evidence and less repetitive interruption.
System-required access approvals, if any, are separate from approval
of the document's content and must be explained as such.

Review all Project Planning documents in order. Analyze and plan
all eight SDLC phases before starting product implementation,
using appropriate initial detail for later phases. Reconcile the
backlog, Sprints, and milestones with the reviewed documentation
and agreed baseline before coding. Subsequent evidence can drive
controlled revisions; baseline acceptance does not prohibit change.

This entry records the working agreement. It does not approve
unreviewed documents, establish implementation, or accept the
overall planning baseline.

### Requirements Engineering Boundary Review

Decision ID: DEC-029
<a id="dec-029"></a>

Status: Accepted by the project owner for this section
Review date: October 30, 2026

Decision: Keep stakeholder identification and project delivery
responsibilities in this planning document. Maintain authoritative
detailed application permissions, role restrictions, invitations,
and account lifecycle behavior in Requirements Engineering.

Rationale: Avoid duplicating detailed authorization rules across
planning and requirements documents, reducing inconsistency while
preserving clear ownership and traceability.

## Document Review Summary

The project owner reviewed the stakeholder classification,
confirmed solo delivery, accepted the working agreement, and
accepted the boundary with Requirements Engineering.

Current staffing: one project owner advancing the project; no separate
delivery or operations team.

This document is accepted as planning-level direction. Detailed
requirements, remaining Project Planning documents, and acceptance
of the overall planning baseline require their own reviews.

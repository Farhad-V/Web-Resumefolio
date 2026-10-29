# Assumptions and Dependencies

Status: Draft for review

## 1. Planning Assumptions

These are provisional assumptions, not verified facts.

| ID | Assumption | How to validate | Needed before |
|---|---|---|---|
| ASM-01 | The existing server can support the initial application workload within the budget | Inspect server resources and workloads; evaluate representative application loads | Finalizing deployment design |
| ASM-02 | Required Google integrations are available under acceptable access conditions and costs | Check current provider requirements and test the required operations | Committing to integration details |
| ASM-03 | A suitable email delivery arrangement can support authentication and notifications | Verify configuration, delivery behavior, limits, and costs | Releasing email-dependent workflows |
| ASM-04 | Suitable backup storage is available within the budget | Identify storage location, capacity, access, and restoration procedure | Approving operational readiness |
| ASM-05 | Development time is sufficient for the agreed scope | Establish available hours, estimate work, and review progress | Setting delivery dates |

If an assumption proves false, record its impact and discuss
options with the project owner. Do not silently change scope
or assume additional spending.

## 2. External Dependencies

| ID | Dependency | What depends on it | Verification needed |
|---|---|---|---|
| DEP-01 | Hosting server and network | Application availability, storage, Git hosting, and background processing | Resource inventory, access, limits, and current workloads |
| DEP-02 | Domain, DNS, and TLS | Access through Resumefolio.de and secure browser connections | Domain control, configuration, and certificate arrangements |
| DEP-03 | Google services | Agreed Gmail and Google Calendar operations | Required permissions, provider conditions, quotas, and failure behavior |
| DEP-04 | Email delivery | Email-based authentication, notifications, and relevant recovery workflows | Delivery configuration and operational verification |
| DEP-05 | Backup storage | Recovery after data loss or server failure | Storage separation, access, retention, and restoration checks |
| DEP-06 | Software packages and development tools | Building, running, and maintaining the application | Compatibility, licenses, maintenance status, and supported versions |

Provider-specific requirements must be checked when selecting
and implementing integrations. This document does not claim
that access, approval, or capacity has already been secured.

## 3. Internal Dependencies

- Detailed requirements and scenarios inform system analysis.
- Analysis and resource findings inform architecture decisions.
- Identity and permissions support protected workflows.
- Data ownership and lifecycle rules inform sharing,
  collaboration, deletion, and recovery.
- Git CI/CD execution depends on an agreed security model,
  resource limits, and execution isolation.
- Release readiness depends on verification evidence,
  deployment procedures, and demonstrated restoration.

These relationships guide sequencing.
They do not require every activity to finish before related
work can begin; documents and decisions can evolve iteratively.

## 4. Tracking and Review

- The project owner coordinates validation with assistant support.
- Record each validation result and its supporting evidence.
- Mark assumptions as unverified, confirmed, or invalidated.
- Mark dependencies as unverified, available, or blocked.
- Review affected items when scope, infrastructure, or
  provider conditions change.
- Link unresolved consequences to the risk register.
- Never record passwords, tokens, or other secrets as evidence.

Current status: all assumptions and external dependency
arrangements listed here require validation.

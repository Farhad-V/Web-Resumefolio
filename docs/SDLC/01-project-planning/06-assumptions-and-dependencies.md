# Assumptions and Dependencies

Status: Reviewed - planning methods accepted; technical validation remains open

## 1. Planning Assumptions

These are provisional assumptions, not verified facts.

| ID | Assumption | How to validate | Needed before |
|---|---|---|---|
| ASM-01 | The existing server can support the initial application workload within the budget | Inspect server resources and workloads; evaluate representative application loads | Finalizing deployment design |
| ASM-02 | Required Google integrations are available under acceptable access conditions and costs | Check current provider requirements and test the required operations | Committing to integration details |
| ASM-03 | A suitable email delivery arrangement can support authentication and notifications | Verify configuration, delivery behavior, limits, and costs | Releasing email-dependent workflows |
| ASM-04 | Suitable backup storage is available within the budget | Identify storage location, capacity, access, and restoration procedure | Approving operational readiness |
| ASM-05 | Development time is sufficient for the agreed scope | Break down and estimate work after analysis/design; include dependencies and all engineering activities; compare with capacity and actual progress | Accepting a delivery forecast; subsequent milestone and Sprint reviews |
| ASM-06 | Information needed from users is sufficiently complete and timely for planned workflows | Define inputs and walk through a representative scenario; examine incomplete or delayed information | Accepting affected workflows and schedules |

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

- The project owner coordinates validation.
- Record each validation result and its supporting evidence.
- Mark assumptions as unverified, confirmed, or invalidated.
- Mark dependencies as unverified, available, or blocked.
- Review affected items when scope, infrastructure, or
  provider conditions change.
- Link unresolved consequences to the risk register.
- Never record passwords, tokens, or other secrets as evidence.

Current status: all assumptions and external dependency
arrangements listed here require validation.

## 5. Validation Assignments

Status: Responsibility assignments and review points accepted; validation outcomes remain open

The project owner coordinates these investigations. Findings must include evidence and be
reviewed before the dependent commitment.

| Items | Responsible person | Review point | Current status |
|---|---|---|---|
| ASM-01, DEP-01 | Project owner | Before accepting the deployment design in M-03 | Unverified |
| ASM-02, DEP-03 | Project owner | Before accepting integration requirements in M-02; verify implementation access before dependent development | Unverified |
| ASM-03, DEP-04 | Project owner | Before accepting authentication delivery design in M-03; verify delivery before release | Unverified |
| ASM-04, DEP-05 | Project owner | Before accepting recovery design in M-03; demonstrate restoration before M-09 acceptance | Unverified |
| ASM-05 | Project owner | After analysis/design and before accepting a delivery forecast; revisit with actual progress at milestone and Sprint reviews | Unverified: full-time availability stated, sufficiency not demonstrated |
| ASM-06 | Project owner | During Requirements Engineering before accepting affected workflows; review schedule implications before dependent commitments | Unverified |
| DEP-02 | Project owner | Before accepting deployment configuration in M-03; verify live configuration before M-10 | Unverified |
| DEP-06 | Project owner | At relevant technical selection decisions in M-03 and before dependent implementation | Partially verified: Git and diagram tools demonstrated; application dependencies remain open |

Record results against the existing ASM and DEP identifiers.
Completion of an investigation does not automatically mean
the assumption is confirmed or the dependency is available.

## Review Decisions

### ASM-01 Server Capacity Assumption Review

Decision ID: DEC-061
<a id="dec-061"></a>

Status: Assumption treatment and validation approach accepted;
server capacity remains unverified
Review date: October 30, 2026

Decision: Treat sufficient capacity of the existing server for the
initial application workload within budget as a provisional
assumption, not an established technical fact.

Validation: Inspect resources and current workloads, define a
representative workload, and evaluate it against explicit capacity
and performance criteria. Record evidence and whether the assumption
is confirmed, invalidated, or remains unresolved before finalizing
the deployment design. The project owner coordinates this work.

Rationale: Make a material infrastructure assumption explicit so
architecture and deployment decisions do not rest on a hidden guess.
If invalidated, record the impact and options for the project owner's
decision without silently changing scope or assuming new spending.

This review does not access or modify the server, execute load
tests, or establish capacity for either 10 or 1,000 users.

### ASM-02 Google Integration Access Review

Decision ID: DEC-060
<a id="dec-060"></a>

Status: Assumption and validation approach accepted for tracking;
provider access and suitability remain unverified
Review date: October 30, 2026

Decision: Provisionally assume required Gmail and Google Calendar
operations can be supported under acceptable access conditions,
limits, and costs. Check current provider documentation, required
permissions, API access, quotas, and costs, and test the required
operations before committing to dependent integration details.

Rationale: Avoid designing workflows around unavailable permissions
or unsuitable provider conditions. The project owner coordinates
validation; link findings to ASM-02 and DEP-03.
No provider investigation or integration test has yet been demonstrated
by this review.

### ASM-03 Email Delivery Review

Decision ID: DEC-059
<a id="dec-059"></a>

Status: Assumption and validation approach accepted for tracking;
email delivery remains unverified
Review date: October 30, 2026

Decision: Provisionally assume suitable, affordable email delivery
can support authentication and notifications. Investigate available
arrangements, required configuration, access, quotas, costs, and
failure behavior; validate actual delivery before releasing dependent
workflows and before committing to the dependent technical design.

Rationale: Authentication and notification workflows depend on
working delivery, not merely on having an email address or account.
The project owner coordinates validation;
record findings against ASM-03 and DEP-04. This does not introduce
public self-registration or a new application-submission integration.
No successful delivery test is claimed by this review.

### ASM-06 User Input Availability Review

Decision ID: DEC-058
<a id="dec-058"></a>

Status: New provisional assumption and validation approach accepted
for tracking; actual input availability remains unverified
Review date: October 30, 2026

Decision: Record the provisional expectation that information needed
from users for planned workflows is available with sufficient
completeness and timeliness. Do not treat this as a guarantee of
future user behavior or as a verified delivery dependency.

Validation: Define required inputs, forms, and intake workflows in
Requirements Engineering. Walk through a representative scenario
with suitable sample information and identify missing, delayed,
or incomplete inputs and their effects. Define handling of those
cases before accepting the affected workflows and schedules.

Rationale: Make information needs visible rather than silently
assuming all input will arrive complete and on time. The project
owner coordinates this work. This review
does not claim forms are implemented or a scenario test has run.

### ASM-04 Backup Storage Assumption Review

Decision ID: DEC-057
<a id="dec-057"></a>

Status: Assumption treatment and validation approach accepted;
storage suitability and restoration remain unverified
Review date: October 30, 2026

Decision: Treat suitable backup storage within budget as provisional.
Inspect its location, available capacity, separation from the primary
server, access arrangements, and restoration options. Record findings
before accepting recovery design; demonstrate restoration before
accepting operational readiness.

Rationale: A copy on the same primary server may not cover complete
server loss. Do not infer independent recovery capability merely
from backup-file existence. The project owner coordinates the
investigation; link evidence to ASM-04,
DEP-05, and the backup investigation work item.

This review does not establish available storage, run restoration,
or authorize purchasing services or modifying server data.

### External Google and Email Provider Dependency Review

Decision ID: DEC-056
<a id="dec-056"></a>

Status: Dependency treatment and validation approach accepted;
provider access and operating conditions remain unverified
Review date: October 30, 2026

Decision: Track Gmail and Google Calendar under DEP-03 and email
delivery under DEP-04 as external dependencies. Required access,
provider-condition changes, limits, and service interruption can
affect dependent workflows and must be addressed explicitly.

Validation: Consult current official provider sources, identify
required operations, permissions, limits, and costs, and define
appropriate operation and failure-behavior checks. Record sources,
findings, and limitations before dependent commitments, with the
project owner coordinating validation.

Rationale: Keep dependence on external services visible and testable
rather than assuming uninterrupted availability or unchanged access.
Link findings to ASM-02 and ASM-03 and the existing validation
assignments. This review does not claim provider research or
successful integration tests have already been performed.

### ASM-05 Development Time Assumption Review

Decision ID: DEC-055
<a id="dec-055"></a>

Status: Validation approach accepted by the project owner;
time sufficiency and delivery forecast remain unverified
Review date: October 31, 2026

Decision: Treat sufficient development time for the complete agreed
scope as a provisional assumption. Full-time solo availability is
confirmed, but does not establish numerical throughput or prove
that the requested delivery target is achievable.

Validation: After the initial analysis and design review, break down
work into estimable items, identify dependencies, and include learning,
implementation, testing, documentation, integration, and rework.
Compare effort ranges with available capacity, then reconcile Sprints
and milestones. During execution, revise forecasts against observed
progress and record the reasons and effects of changes.

Review point: Before accepting a schedule as a credible delivery
forecast, and again at relevant milestone and Sprint reviews. An
already recorded target date is not evidence validating the schedule.
The project owner coordinates estimation.

Rationale: Distinguish the requested target from an evidence-based
forecast and make scope/time conflicts explicit. If the assumption
is invalidated, document options for the project owner's decision;
do not silently reduce scope or claim that Agile guarantees the date.

This review records the validation method only. It does not estimate
all remaining work, revise live GitHub dates, accept the overall
planning baseline, or authorize starting implementation now.

### DEP-01 Hosting Server and Network Dependency Review

Decision ID: DEC-054
<a id="dec-054"></a>

Status: Dependency treatment and validation approach accepted;
technical characteristics and failure behavior remain unverified
Review date: October 31, 2026

Decision: Track the hosting server and network as external
infrastructure dependencies for application operation, storage,
Git hosting, and background processing. This dependency is distinct
from ASM-01, which provisionally assumes sufficient capacity.

Validation: Inspect available resources, existing workloads,
network and storage limits, and relevant access arrangements.
Define and document expected behavior during interruption or
failure, then verify relevant recovery and error-handling scenarios
before accepting dependent operational capabilities.

Review point: Evaluate findings before accepting deployment design
and dependent capacity commitments; verify operational behavior
before release. The project owner coordinates the investigation, linking findings to DEP-01 and ASM-01.

Rationale: Make reliance on infrastructure explicit and distinguish
its existence from evidence of adequate capacity and resilience.
Record limitations and unresolved findings rather than assuming
uninterrupted operation or sufficient resources.

This review does not inspect or modify the server, run load or
failure tests, or establish availability or recovery guarantees.

### DEP-02 Domain DNS and TLS Dependency Review

Decision ID: DEC-053
<a id="dec-053"></a>

Status: Dependency treatment and validation approach accepted;
current configuration and certificate arrangements remain unverified
Review date: October 31, 2026

Decision: Track the domain, DNS, and TLS arrangements as dependencies
for reaching Resumefolio.de through the intended secure connection.
Domain availability alone does not establish correct routing or
valid HTTPS configuration.

Validation: Verify administrative access to domain configuration,
relevant DNS records and their intended server destination, and
TLS certificate validity, coverage, configuration, and renewal
arrangements. Record findings without exposing credentials.

Review point: Review configuration findings before accepting the
deployment design and verify the live domain and HTTPS behavior
before deployment acceptance. The project owner coordinates this
work, recording evidence against DEP-02.

Rationale: Ensure that a deployed application can be reached through
the intended address with an appropriately configured secure
connection rather than assuming server deployment alone provides it.

This acceptance records the investigation approach. It does not
inspect or change DNS, issue or renew a certificate, access domain
administration, or establish that HTTPS currently works correctly.

### DEP-06 Software Packages and Development Tools Review

Decision ID: DEC-052
<a id="dec-052"></a>

Status: Dependency treatment and evaluation approach accepted;
individual application dependency selections remain open
Review date: October 31, 2026

Decision: Evaluate software packages and development tools against
required behavior, version compatibility, usage licenses,
maintenance and support status, and runtime and infrastructure
requirements. Document significant selection decisions, alternatives,
rationale, and material limitations.

Validation: Check current primary project or vendor documentation
and relevant release and license information when selecting a
component. Verify compatibility through appropriate checks in the
intended environment rather than relying on package availability
or prior use alone.

Review point: Evaluate before accepting the related technical
selection during analysis and design, and validate required
compatibility before dependent implementation and release.
The project owner coordinates this work.

Rationale: Reduce unsupported or unsuitable technical dependencies
and make choices defensible against actual product and resource
constraints. Reassess selections when relevant versions, requirements,
or maintenance conditions change.

Previously demonstrated Git and diagram tooling remain distinct
from unselected and unverified application dependencies. This review
does not select, install, update, or validate a new package.

### Internal Dependencies Review

Decision ID: DEC-051
<a id="dec-051"></a>

Status: Dependency relationships and their planning use accepted
by the project owner
Review date: October 31, 2026

Decision: Use requirements and scenarios as the basis for analysis
and design. Treat identity and permissions as prerequisites for
protected behavior; data ownership and lifecycle rules as inputs
to sharing, deletion, and restoration; and CI/CD security and
resource boundaries as prerequisites for enabling workflow execution.
Release readiness depends on actual verification evidence,
deployment readiness, and demonstrated recovery.

Rationale: Make the sequence of dependent decisions and the effects
of change explicit. Link the affected requirements, design decisions,
work items, and verification evidence so changes can be evaluated
across the relevant product areas.

These relationships guide work sequencing without prohibiting
feedback, iterative review, or incremental delivery. Preserve the
agreed initial documentation and baseline process before product
coding, then revise affected artifacts as evidence emerges.

This review does not claim prerequisites are already satisfied,
accept the overall planning baseline, or authorize release.

### Tracking and Review Method Acceptance

Decision ID: DEC-050
<a id="dec-050"></a>

Status: Tracking and review method accepted by the project owner;
individual validation outcomes remain unchanged
Review date: October 31, 2026

Decision: Track assumptions as unverified, confirmed, or invalidated,
and dependencies as unverified, available, or blocked. Support status
changes with evidence and a recorded responsible person and review
point. The project owner coordinates this work.

Review affected items when requirements, infrastructure, or provider
conditions change. Link unresolved consequences to the risk register
and affected work items. Never include credentials or other secrets
in repository evidence.

Rationale: Distinguish acceptance of an investigation method from
confirmation of its outcome, and keep changes traceable rather than
allowing unverified assumptions to become implicit facts.

This acceptance does not confirm a resource, complete an investigation,
change an item's technical validation status, or approve the overall
planning baseline.

### Validation Assignments Review

Decision ID: DEC-049
<a id="dec-049"></a>

Status: Responsibility assignments and review points accepted;
technical validation outcomes remain unchanged
Review date: October 31, 2026

Decision: The project owner coordinates the listed investigations.
Review Google access before committing to integration details;
server and CI/CD resources before accepting dependent designs;
backup arrangements before accepting recovery design, with actual
restoration evidence before release; time sufficiency after analysis
and design and against observed progress; and software dependencies
at selection and before dependent implementation.

Rationale: Give open questions accountable ownership and a review
point before their results are needed. Acceptance of assignments
does not confirm assumptions, complete tests, or establish resources.

## Document Review Summary

The project owner reviewed the assumption treatment, external and
internal dependencies, evidence-based status tracking, responsibility
assignments, and review points. Review date: October 31, 2026.

These planning methods are accepted. Actual technical investigations,
provider validation, capacity checks, and restoration evidence remain
open as identified in this document. This review does not accept the
overall planning baseline or begin product implementation.

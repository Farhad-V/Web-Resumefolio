# Risk Register

Status: Reviewed - risk definitions and management approach accepted; risks remain open

## 1. Initial Risks

The risks below identify possible problems.
They do not claim that failures have already occurred.

| ID | Risk and potential impact | Proposed response | Related items |
|---|---|---|---|
| RSK-01 | Scope exceeds available development time, delaying delivery or reducing verification quality | Estimate work incrementally, review progress, and discuss scope or schedule conflicts explicitly | ASM-05 |
| RSK-02 | Server resources are insufficient for the combined application, media, Git, and CI/CD workloads | Inspect capacity, evaluate representative loads, and define resource limits before finalizing deployment design | ASM-01, DEP-01 |
| RSK-03 | CI/CD execution exposes the host, secrets, or other users' data | Define execution isolation, permissions, secret handling, and resource limits; verify controls before enabling execution | DEP-01 |
| RSK-04 | Access-control errors expose private resumes, files, email, or collaboration resources | Define a permission matrix and test authorized and unauthorized paths, including direct file access | Requirements specification |
| RSK-05 | Server failure, deletion, or an unsuccessful update causes unrecoverable data loss | Establish backup arrangements, retention, restoration checks, and update recovery procedures | ASM-04, DEP-05 |
| RSK-06 | Google integration restrictions or service failures interrupt agreed workflows | Verify required operations and access conditions early; define disconnection, retry, and failure behavior | ASM-02, DEP-03 |
| RSK-07 | Delayed or failed email delivery prevents email-dependent login or notifications | Verify delivery arrangements and define rate limits, retry behavior, and permitted recovery paths | ASM-03, DEP-04 |
| RSK-08 | Large uploads or accumulated data exhaust storage or processing capacity | Define owner-configurable limits, capacity checks, and storage monitoring | ASM-01, DEP-01 |
| RSK-09 | Unclear cross-module lifecycle rules cause inconsistent or unexpectedly deleted data | Specify ownership, synchronization, archival, deletion, and recovery scenarios before implementation | Requirements specification |
| RSK-10 | Limited maintenance time leaves defects, dependencies, or operational failures unattended | Define realistic maintenance responsibilities, update procedures, and operational checks | DEP-06 |

## 2. Assessment Status

All listed risks are open for assessment.

Likelihood remains unassessed. Preliminary impact judgments and response priorities are proposed in Section 6.
Ratings must be justified using available evidence rather
than presented as measured facts.

Security boundaries, recovery arrangements, and infrastructure
feasibility require early investigation because they can affect
architecture and delivery sequencing.

## 3. Ownership and Review

The project owner coordinates risk review and response.

For each assessed risk, record:
- Likelihood and impact, with the reason for each rating.
- The agreed response and responsible person.
- A review milestone or date.
- Warning signs that require action.
- Current status and supporting evidence.
- Remaining risk after the response is implemented.

Review risks at milestone checkpoints and when assumptions,
requirements, infrastructure, or provider conditions change.

## 4. Handling Problems

If a risk occurs, record the actual problem as an issue
and link it to the originating risk.

Responses that change agreed scope, spending, or delivery
commitments require an explicit project-owner decision.

A risk is not closed merely because a response is documented.
Closure requires evidence or a recorded decision accepting
the remaining risk.

## 5. References

- [Assumptions and Dependencies](06-assumptions-and-dependencies.md)
- [Resources and Constraints](05-resources-and-constraints.md)
- [Version 1 Scope](02-scope.md)

## 6. Initial Assessment and Review Assignments

Status: Reviewed - preliminary assessment approach accepted; judgments remain evidence-dependent

These are preliminary planning judgments, not measured
probabilities or findings from a security or capacity test.

### Assessment Terms

- Likelihood: Unknown until sufficient evidence is available.
- High impact: Could expose private data, cause unrecoverable
  loss, prevent essential workflows, or materially disrupt delivery.
- Medium impact: Could degrade service or increase maintenance
  effort without necessarily preventing the entire release.
- P1: Investigate early because findings can affect feasibility,
  architecture, or major delivery commitments.
- P2: Address during relevant design and implementation work,
  before accepting the affected capability.

All risks remain open. The project owner coordinates responses.

| Risk | Likelihood | Potential impact | Priority | Reason for initial assessment | Review point |
|---|---|---|---|---|---|
| RSK-01 | Unknown | High | P1 | Broad scope and unverified effort/capacity make delivery forecasts uncertain despite stated full-time availability | Before accepting a delivery forecast; revisit milestone and Sprint reviews |
| RSK-02 | Unknown | High | P1 | Server capacity for combined workloads has not been verified | M-03, before accepting deployment design |
| RSK-03 | Unknown | High | P1 | Executing project code could compromise the host or other data if isolation fails | M-03 security design; controls verified before M-08 acceptance |
| RSK-04 | Unknown | High | P1 | Permission failures could expose private information across users or sharing boundaries | M-02 permission requirements; verify each affected increment and M-09 |
| RSK-05 | Unknown | High | P1 | Backup arrangements and recoverability are not yet demonstrated | M-03 recovery design; restoration evidence before M-09 acceptance |
| RSK-06 | Unknown | High | P1 | Unverified integration access could prevent agreed email or calendar workflows | M-02 integration requirements; verify before dependent development |
| RSK-07 | Unknown | High | P1 | Email delivery failure could prevent email-dependent authentication | M-03 authentication design; delivery checks before release |
| RSK-08 | Unknown | High | P1 | Storage exhaustion could affect uploads and other services sharing the server | M-03 storage design; verify limits before affected capability acceptance |
| RSK-09 | Unknown | High | P1 | Ambiguous deletion and synchronization rules could cause inconsistent or lost data | M-02 lifecycle requirements; M-03 data design |
| RSK-10 | Unknown | Medium | P2 | Unconfirmed maintenance capacity could delay updates and operational responses | Before M-09 acceptance; review during operation |

High impact does not imply high likelihood.
Priorities may change when evidence becomes available.

These assignments identify review points; they do not claim
that responses have been implemented or that risks are resolved.

## Risk Review Decisions

### RSK-01 Scope and Development Time Review

Decision ID: DEC-074
<a id="dec-074"></a>

Status: Risk definition and response approach accepted;
risk remains open and likelihood remains unassessed
Review date: October 31, 2026

Risk: The agreed scope may exceed available development time,
causing delayed delivery or reduced verification quality.
Potential impact: High, because the complete release can be affected.
Response priority: P1, to inform delivery commitments early.

Response: Break down and estimate work after initial analysis and
design, including dependencies, learning, testing, documentation,
integration, and rework. Review actual progress and revise forecasts.
Record scope/time conflicts explicitly for the project owner's
decision rather than silently omitting capabilities or bypassing
necessary verification to satisfy a target date.

Owner: Project owner.
Review point: Before accepting a delivery forecast and at subsequent
milestone and Sprint reviews. Link findings to ASM-05 and relevant
backlog and schedule records.
Warning signs: Estimated effort exceeds available capacity,
prerequisites remain unresolved at planned start points, or
verification work is repeatedly deferred to preserve target dates.

Rationale: Prevent schedule pressure from being hidden in incomplete
scope or unsupported quality claims. Full-time availability alone
is not evidence of sufficient capacity for the requested deadline.

This acceptance does not resolve the risk, revise live delivery
dates, or establish that the complete scope is feasible in the
requested period. Residual risk must be reassessed with evidence.

### RSK-02 Combined Server Workload Review

Decision ID: DEC-073
<a id="dec-073"></a>

Status: Risk definition and response approach accepted;
risk remains open and likelihood remains unassessed
Review date: October 31, 2026

Risk: Server resources may be insufficient for the combined
application, media storage and processing, Git hosting, background
jobs, and CI/CD execution workloads, degrading performance or
causing operations to fail.
Potential impact: High, because shared resource exhaustion can
affect multiple essential workflows.
Response priority: P1, before dependent deployment commitments.

Response: Inspect current capacity and existing workloads. Define
representative usage scenarios, evaluate resource demand for the
combined workload, and establish appropriate resource limits before
accepting deployment design. Assess concurrency and storage growth
rather than assuming low per-feature usage proves total capacity.

Owner: Project owner.
Review point: Before accepting the deployment design in M-03;
verify relevant capacity behavior before release acceptance.
Related items: ASM-01, DEP-01, and the server investigation backlog item.
Warning signs: Sustained resource pressure, insufficient free storage,
queue accumulation, or repeated operation failures in representative
checks. Define measurable thresholds in later requirements and design.

Rationale: Shared infrastructure must be evaluated as a combined
system, not as isolated features. If resources cannot support the
agreed scope, document evidence, alternatives, costs, and delivery
implications for the project owner's decision; do not assume new
spending or silently remove capabilities.

This review does not inspect the server, execute load tests,
choose infrastructure changes, or establish verified capacity.

### RSK-03 CI/CD Execution Security Review

Decision ID: DEC-072
<a id="dec-072"></a>

Status: Risk definition and response approach accepted;
risk remains open and likelihood remains unassessed
Review date: October 31, 2026

Risk: CI/CD job execution may gain unauthorized access to the host,
secrets, or other users' information if execution boundaries fail.
Repository content must not be assumed trustworthy merely because
it is stored in a project repository.
Potential impact: High, because a boundary failure can compromise
private information and shared infrastructure.
Response priority: P1, before accepting execution design or enabling jobs.

Response: Define isolated job execution, explicit permissions,
secret-handling boundaries, resource limits, and appropriate cleanup.
Evaluate and test relevant controls before enabling CI/CD execution.
Select the technical isolation approach during System Design,
documenting alternatives, rationale, constraints, and residual risks.

Owner: Project owner.
Review point: During M-03 security and execution design, with control
verification required before M-08 acceptance and release readiness.
Related items: DEP-01, the CI/CD feasibility investigation, and the
CI/CD implementation work package.
Warning signs: A job can access unrelated files or credentials,
affect other workloads, or exceed its intended privileges or limits
in controlled verification. Record failures and stop dependent
execution acceptance until addressed.

Rationale: Running project code introduces an execution trust boundary
that repository storage and ordinary Git checks do not provide.
Documented intentions alone are insufficient evidence of containment.

This review records the risk response, not a selected isolation
technology, completed security test, or permission to run arbitrary
workloads on the production server.

### RSK-04 Authorization and Private Data Exposure Review

Decision ID: DEC-071
<a id="dec-071"></a>

Status: Risk definition and response approach accepted;
risk remains open and likelihood remains unassessed
Review date: October 31, 2026

Risk: Authorization errors may allow a person to view or modify
another user's private resumes, files, email, or collaboration
resources outside the permissions granted to that person.
Potential impact: High, because private information and operations
across multiple product areas can be affected.
Response priority: P1, beginning with permission requirements.

Response: Define role, resource, and operation permissions explicitly.
Verify permitted and denied paths, including cross-user requests,
limited collaboration invitations, employer sharing, and direct
file retrieval. Enforce authorization at relevant request boundaries;
hidden interface controls or successful login alone are not proof
that the requested operation is authorized.

Owner: Project owner.
Review point: Define permission rules during M-02; review relevant
design boundaries in M-03; verify each affected increment and the
integrated release candidate before acceptance.
Warning signs: Requests succeed outside granted permissions,
shared links expose unrelated content, or authorization checks rely
only on navigation restrictions. Record findings and reassess related
workflows before accepting the affected capability.

Rationale: Private data protection requires enforced authorization
and actual evidence across retrieval and modification paths, rather
than assuming a login page or interface restriction is sufficient.

This review does not select the complete permission implementation,
claim that controls are implemented or tested, or resolve the risk.

### RSK-05 Data Loss and Unrecoverable Failure Review

Decision ID: DEC-070
<a id="dec-070"></a>

Status: Risk definition and response approach accepted;
risk remains open and likelihood remains unassessed
Review date: October 31, 2026

Risk: Server failure, accidental deletion, or an unsuccessful update
may cause data loss that cannot be recovered with the available
backup and recovery arrangements.
Potential impact: High, because professional information, application
history, repositories, and other important product data may be lost.
Response priority: P1, beginning with recovery requirements and feasibility.

Response: Define backup coverage, storage and retention, restoration,
and recovery from unsuccessful updates. Demonstrate restoration in
a separate environment and check restored data integrity and
consistency. Verify relevant rollback and migration recovery steps;
do not assume application-code rollback restores data automatically.

Owner: Project owner.
Review point: Review recovery requirements and design before M-03
acceptance; retain restoration and update-recovery evidence before
M-09 and the release decision. Link findings to ASM-04 and DEP-05.
Warning signs: Missing or failed backups, inaccessible backup storage,
failed restoration, or inconsistent restored data. Investigate findings
before accepting operational readiness.

Rationale: Backup existence alone does not demonstrate recoverability.
Define recovery-time and recovery-point targets against actual
resources and record achieved results and remaining limitations.
Do not imply that zero data loss or a particular recovery time has
been demonstrated before appropriate evidence exists.

This review does not create a backup, restore data, modify the server,
authorize destructive testing, or close the risk.

### RSK-06 Google Integration Restrictions and Failure Review

Decision ID: DEC-069
<a id="dec-069"></a>

Status: Risk definition and response approach accepted;
risk remains open and likelihood remains unassessed
Review date: October 31, 2026

Risk: Access restrictions, changed provider conditions, or service
interruption may prevent agreed Gmail and Google Calendar workflows
from operating correctly.
Potential impact: High, because required communication and scheduling
workflows may become unavailable or inconsistent.
Response priority: P1, beginning with integration feasibility.

Response: Investigate required operations, access conditions, and
limits early. Define and test behavior for disconnection, failures,
retry, and reconnection. Make failures visible and design safeguards
against inconsistent records and duplicated operations when retries
or synchronization resume.

Owner: Project owner.
Review point: Before accepting dependent integration requirements
and design; validate access before dependent development and verify
relevant failure scenarios before capability and release acceptance.
Related items: ASM-02, DEP-03, and the Google integration investigation.
Warning signs: Required operations are unavailable, authorization
is revoked, provider errors persist, or reconnection/retry produces
inconsistent or duplicate records. Record evidence and reassess the
affected workflow and delivery plan.

Rationale: External service behavior is outside the project's direct
control. Define bounded, observable failure and recovery behavior
rather than assuming provider availability or unchanged conditions.

This review does not check current provider policy, authorize new
account permissions, connect a Google account, execute integration
tests, or establish that a failure-handling mechanism is implemented.

### RSK-07 Email Delivery Delay and Failure Review

Decision ID: DEC-068
<a id="dec-068"></a>

Status: Risk definition and response approach accepted;
risk remains open and likelihood remains unassessed
Review date: October 31, 2026

Risk: Delayed or failed email delivery may prevent email-dependent
login or interrupt notifications and activity follow-up.
Potential impact: High, because essential authentication paths
can depend on successful receipt of an email.
Response priority: P1, before accepting email-dependent capabilities.

Response: Investigate and test actual delivery arrangements.
Define resend behavior, request limits, code validity, and permitted
recovery paths in the authentication requirements. Make relevant
failures observable without exposing credentials or login codes.
Delivery failure must not become a reason to bypass authentication.

Owner: Project owner.
Review point: During authentication and delivery design in M-03;
verify relevant delivery, failure, resend, and recovery behavior
before accepting dependent capabilities and release readiness.
Related items: ASM-03, DEP-04, and the email-delivery investigation.
Warning signs: Delivery errors, repeated delays, or reports of
missing login messages. Record evidence and distinguish application
submission to the delivery provider from actual recipient receipt.

Rationale: Application-side send success alone does not establish
that the user received a message. Maintain security boundaries while
providing explicit handling of unavailable or delayed delivery.

This review does not send email, select a provider, implement a
recovery mechanism, demonstrate delivery, or close the risk.

### RSK-08 Upload and Storage Exhaustion Review

Decision ID: DEC-067
<a id="dec-067"></a>

Status: Risk definition and response approach accepted;
risk remains open and likelihood remains unassessed
Review date: October 31, 2026

Risk: Large uploads or accumulated data may exhaust storage or
processing capacity and disrupt the application or other workloads
sharing the server.
Potential impact: High, because resource exhaustion can affect
multiple essential operations beyond the upload itself.
Response priority: P1, before accepting dependent storage capabilities.

Response: Define and verify owner-configurable upload limits and
storage quotas, capacity checks, and warnings as resource thresholds
are approached. Specify behavior during insufficient capacity,
interrupted uploads, and failed processing; do not treat a failed
operation as successfully stored content.

Owner: Project owner.
Review point: During storage and resource design in M-03; verify
limits, failure behavior, and relevant warnings before capability
acceptance and release readiness.
Related items: ASM-01, DEP-01, server resource investigation, and
media/storage implementation work.
Warning signs: Declining free capacity, quota overruns, interrupted
uploads, growing processing queues, or capacity-related failures.
Set measurable thresholds after inspecting actual infrastructure.

Rationale: Configurable policy limits do not create unlimited
physical storage or processing capacity. Enforce the intended
policy within real resource constraints and make capacity failures
visible and reviewable.

This review does not set numerical quotas, implement monitoring,
change server limits, or establish successful capacity testing.

### RSK-09 Cross-Module Data Lifecycle Review

Decision ID: DEC-066
<a id="dec-066"></a>

Status: Risk definition and response approach accepted;
risk remains open and likelihood remains unassessed
Review date: October 31, 2026

Risk: Unclear rules for modification, deletion, synchronization,
archival, and restoration across product areas may cause inconsistent
information or unintended data loss.
Potential impact: High, because one operation can affect records
and evidence used by multiple workflows.
Response priority: P1, before accepting dependent lifecycle design.

Response: Specify ownership and lifecycle rules in Requirements
Engineering, including the effects of each operation on related
resources and preserved submission records. Analyze the relationships
in System Analysis and System Design, then verify the relevant
cross-module success, failure, deletion, and restoration scenarios.

For example, deleting a source resume must not silently delete an
archived submitted copy. Keep live editable information distinct
from preserved application-history evidence under explicit rules.

Owner: Project owner.
Review point: During M-02 lifecycle requirements and M-03 data design;
verify affected behavior before capability and integrated release
acceptance. Link rules and scenarios to the relevant requirements,
data model, work items, and test evidence.
Warning signs: An operation changes or removes unrelated records,
reconnection produces contradictory data, or restoration does not
respect the agreed relationship and access rules.

Rationale: Make cross-module consequences deliberate and testable
rather than leaving hidden side effects to implementation assumptions.
Record material changes and their impact on dependent workflows.

This review does not define every lifecycle rule, modify stored data,
implement synchronization, or establish that scenario tests passed.

### RSK-10 Solo Maintenance Capacity Review

Decision ID: DEC-065
<a id="dec-065"></a>

Status: Risk definition and response approach accepted;
risk remains open and likelihood remains unassessed
Review date: October 31, 2026

Risk: Limited maintenance time in the current solo arrangement may
delay defect investigation, dependency updates, or responses to
operational problems after deployment.
Potential impact: Medium as an initial general assessment; reassess
upward where a specific incident affects critical data, security,
or essential availability.
Response priority: P2 for planning the operating approach; urgent
findings require priority based on their actual consequences.

Response: Define recurring maintenance, health checks,
troubleshooting, and update procedures against the project owner's
actual available time. Prioritize significant defects and operational
issues explicitly. Keep instructions, evidence, and remaining
limitations documented rather than assuming additional personnel
or continuous operational coverage.

Owner: Project owner.
Review point: Before M-09 acceptance and the release decision,
then during operation and when available capacity or incident
severity changes. Relate the response to DEP-06 and the Maintenance
and Operations Guide.
Warning signs: Repeatedly deferred critical updates, unresolved
significant defects, unreviewed operational failures, or recurring
checks exceeding available maintenance time.

Rationale: Keep the operating plan feasible for one person and
avoid depending on a team or monitoring arrangement that does not
exist. Record any staffing, spending, or service changes explicitly.

This review does not configure monitoring, schedule unattended
work, execute updates, demonstrate response coverage, or close
the risk. See the Document Review Summary for the current review
status; risk outcomes and technical evidence remain separate.

### Shared Risk Assessment Rules Review

Decision ID: DEC-064
<a id="dec-064"></a>

Status: Assessment method accepted by the project owner;
individual risk status and unassessed likelihood remain unchanged
Review date: October 31, 2026

Decision: Keep likelihood, potential impact, and response priority
separate. Likelihood remains unknown where evidence is insufficient.
Impact judgments describe possible consequences and require a
recorded reason. Priority identifies the urgency of investigation
or response and is not a measured probability.

Review preliminary judgments as evidence and circumstances change.
Record the rationale, evidence, and implications of reassessment.
High impact alone does not establish high likelihood. Acceptance
of a documented response does not close or resolve the risk.

Rationale: Make risk evaluation understandable and evidence-based
without presenting preliminary judgments as measured facts or
confusing planned controls with demonstrated effectiveness.

These rules apply across the register. They do not change a risk
rating, implement a control, execute a test, or accept residual risk
on the project owner's behalf.

### Risk Ownership and Review Method Acceptance

Decision ID: DEC-063
<a id="dec-063"></a>

Status: Ownership and review method accepted by the project owner;
actual response effectiveness remains unverified
Review date: October 31, 2026

Decision: The project owner coordinates each risk in the current
solo delivery arrangement. Maintain a next action, review point,
warning signs, current status with evidence, and remaining risk
after responses are implemented. Keep assessment reasons and
response responsibilities explicit.

Review relevant risks at milestone checkpoints and whenever material
requirements, infrastructure, assumptions, or provider conditions
change. Connect risk actions to the relevant work items and preserve
rationale when assessments or responses are revised.

Rationale: Make the register actionable and traceable rather than
a static list of concerns. Recorded ownership and checkpoints support
follow-up without assuming a separate team or continuous monitoring.

This review defines the management method. It does not perform
ongoing monitoring, demonstrate control effectiveness, change risk
status, or accept residual risks without a recorded owner decision.

### Issue Handling and Risk Closure Review

Decision ID: DEC-062
<a id="dec-062"></a>

Status: Handling and closure method accepted by the project owner;
individual risk status remains unchanged
Review date: October 31, 2026

Decision: When a risk materializes, record the actual problem as an
issue linked to its originating risk. Record the evidence, effects,
next action, and responsible person. Responses that materially change
scope, cost, or delivery commitments require a documented project-owner
decision.

Do not close a risk merely because a response has been written.
Closure requires appropriate evidence or an explicit, recorded
project-owner decision accepting the remaining risk, with its limits
and implications stated. Reopen or reassess when relevant conditions
or evidence change.

Rationale: Distinguish planned work from effective response and
actual issues from possible future events. Keep unresolved exposure
visible rather than reporting a documented intention as a resolution.

## Document Review Summary

The project owner reviewed the definitions and response approaches
for all ten risks, the separate treatment of likelihood, impact,
and priority, ownership and review rules, and issue handling and
closure criteria. Review date: October 31, 2026.

Acceptance concerns the register and management approach. All ten
risks remain open; likelihoods remain unassessed and impact and
priority judgments are preliminary. Technical investigation, response
implementation, and verification evidence are still required.
This review does not accept the overall planning baseline or authorize
product implementation or release.

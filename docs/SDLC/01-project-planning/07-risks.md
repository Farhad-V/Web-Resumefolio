# Risk Register

Status: Proposed draft for review

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

The project owner coordinates risk review and response,
with assistant support during project work.

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

Status: Proposed for review

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

All risks remain open. The project owner coordinates responses
with assistant support.

| Risk | Likelihood | Potential impact | Priority | Reason for initial assessment | Review point |
|---|---|---|---|---|---|
| RSK-01 | Unknown | High | P1 | Broad scope and unconfirmed development hours make delivery commitments uncertain | Before agreeing delivery dates; revisit each milestone |
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

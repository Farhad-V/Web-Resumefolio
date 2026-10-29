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

Likelihood and impact ratings have not yet been assigned.
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

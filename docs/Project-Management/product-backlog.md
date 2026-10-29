# Product Backlog

Status: Proposed initial backlog for review

## Working Rules

This file is the initial work-tracking location.
Requirements and acceptance criteria remain authoritative
in Requirements Engineering; backlog items link to them.

Item order below is a proposed investigation sequence.
Dependencies and findings may change that order.

Statuses: Proposed, Ready, In Progress, Blocked, Done.
No item is currently assigned to a sprint.

The project owner coordinates these items with assistant support.
Done requires the completion evidence stated for the item.

## Initial Work Items

| ID | Work item | Priority | Status | Completion evidence | Related items |
|---|---|---|---|---|---|
| PBI-001 | Establish development availability and estimation approach | P1 | Proposed | Available time or explicit uncertainty recorded; estimation review point agreed | ASM-05, M-01 |
| PBI-002 | Inspect existing server resources and workloads | P1 | Proposed | Sanitized resource inventory and capacity questions recorded | ASM-01, DEP-01, RSK-02 |
| PBI-003 | Investigate Git CI/CD feasibility | P1 | Proposed | Options, isolation needs, resource constraints, and unresolved questions documented | RSK-03, M-03 |
| PBI-004 | Verify required Google integration access | P1 | Proposed | Required operations, access conditions, costs, and limitations documented from current evidence | ASM-02, DEP-03 |
| PBI-005 | Investigate email delivery arrangements | P1 | Proposed | Delivery options, configuration needs, costs, and validation plan recorded | ASM-03, DEP-04 |
| PBI-006 | Investigate backup and restoration arrangements | P1 | Proposed | Storage options, separation, constraints, and restoration validation plan documented | ASM-04, DEP-05 |
| PBI-007 | Review the planning baseline | P1 | Proposed | Completion checklist reviewed; blocking and deferred items recorded; owner decision identifies reviewed revision | M-01 |
| PBI-008 | Develop version 1 requirements incrementally | P1 | Proposed | Reviewed requirements, scenarios, permissions, lifecycle rules, and acceptance criteria linked from this backlog | M-02 |

## Sequencing Notes

- PBI-001 informs scheduling and planning review.
- PBI-002 informs CI/CD and deployment feasibility.
- Investigations may proceed alongside requirements discovery.
- PBI-007 must explicitly assess unresolved investigations.
- PBI-008 is a broad work item to refine into smaller items;
  it is not a single-sprint commitment.
- These investigation items do not replace the full version 1
  feature backlog, which will evolve with requirements.

## References

- [Planning Index](../SDLC/01-project-planning/README.md)
- [Assumptions and Dependencies](../SDLC/01-project-planning/06-assumptions-and-dependencies.md)
- [Risk Register](../SDLC/01-project-planning/07-risks.md)
- [Planning Completion Criteria](../SDLC/01-project-planning/10-planning-completion-criteria.md)

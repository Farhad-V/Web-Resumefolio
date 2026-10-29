# Planning Completion Criteria

Status: Proposed draft for review

## 1. Purpose

Define the conditions for accepting M-01: Planning baseline.

An accepted baseline is a reviewed starting point.
It can evolve through the documented change-control process.

Planning acceptance does not mean that requirements,
architecture, implementation, or release readiness are complete.

## 2. Review Checklist

All items remain pending until reviewed with supporting evidence.

- [ ] PC-01: Purpose, problem statement, intended value, and
  initial objectives are understood and accepted.
- [ ] PC-02: Version 1 inclusions, exclusions, and unresolved
  feature boundaries are explicitly recorded.
- [ ] PC-03: Stakeholders, delivery responsibilities, and
  decision authority are agreed.
- [ ] PC-04: Expected deliverables and their completion evidence
  are reviewed.
- [ ] PC-05: Available resources and constraints are recorded;
  unverified resource details are clearly distinguished.
- [ ] PC-06: Significant assumptions and dependencies have
  validation actions, responsible people, and review points.
- [ ] PC-07: Initial risks have reasoned assessments, response
  priorities, responsible people, and review points.
- [ ] PC-08: The proposed milestone sequence and dependencies
  are reviewed for consistency with scope and resources.
- [ ] PC-09: Available development time and the approach to
  estimates are recorded. Any deferred estimates have an
  assigned investigation and review point.
- [ ] PC-10: The initial work-tracking approach and next set of
  planning or requirements activities are agreed.
- [ ] PC-11: Documents and diagrams are consistent, local links
  resolve, and no known contradictory decisions remain unaddressed.
- [ ] PC-12: Remaining gaps are explicitly classified as
  blocking or deferred, with reasons and follow-up actions.
- [ ] PC-13: The project owner records the review outcome
  against an identifiable Git revision.

## 3. Handling Open Questions

Not every technical detail must be resolved during planning.

A question may be deferred when:
- Its impact and uncertainty are understood sufficiently.
- A responsible person and validation action are recorded.
- A review milestone is assigned before dependent commitments.
- The project owner accepts the proposed deferral.

Do not defer a known feasibility conflict without an agreed
investigation or response.

Server capacity, integration access, backup arrangements,
and safe CI/CD execution require explicit follow-up.
Deferring them does not establish their feasibility.

## 4. Review Outcomes

Choose and record one outcome:
- Pending: the review has not finished.
- Rework required: blocking gaps must be addressed.
- Accepted with tracked follow-up: the baseline is accepted
  and specific non-blocking gaps are assigned.
- Accepted: all planning criteria are satisfied.

A Git commit or push preserves work.
It does not by itself record acceptance.

## 5. Baseline Review Record

- Milestone: M-01
- Outcome: Pending
- Reviewed Git revision: Not yet recorded
- Review date: Not yet recorded
- Decision-maker: Project owner
- Blocking gaps: To be assessed
- Deferred items and follow-up: To be assessed
- Next agreed activities: To be recorded

Update this record after the review.
Do not mark checklist items complete without evidence.

## 6. References

- [Planning Index](README.md)
- [Assumptions and Dependencies](06-assumptions-and-dependencies.md)
- [Risk Register](07-risks.md)
- [Roadmap and Milestones](08-roadmap-and-milestones.md)
- [Working Method and Change Control](09-working-method-and-change-control.md)

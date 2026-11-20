# 6. Algorithms And Business Rules

[Low-Level Design index](03-Low-Level-Design.md)

## 6.1 Operation Flows
For publishing: verify current authorization and draft version; validate selected artifact references; reserve necessary immutable references; commit the publication and live pointer together; finalize pending work and report the recorded outcome.

## 6.2 Validation Rules
Validate identifiers, expected versions, lifecycle transitions, lengths and supported formats at the entry point. Enforce ownership and invariants in the owning application service.

## 6.3 Edge Cases
A stale draft never overrides newer content. A revoked share denies new access. A repeated submission returns the same recorded outcome for an identical request. Missing or uncertain material remains pending for reconciliation.

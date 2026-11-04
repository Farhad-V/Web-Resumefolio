# Architecture Decision Records

The [Baseline](../../../baseline/README.md) and ADR-006 select the current MVP technical design under Farhad's delegated authority. Product/runtime acceptance remains subject to the named gates.

| Record | Decision / status |
| --- | --- |
| [ADR-001 — Modular boundaries](ADR-001-modular-application-boundaries.md) | Internal ownership rationale retained; combined-system proposal superseded by ADR-005 |
| [ADR-002 — Publication and history](ADR-002-explicit-publication-and-history.md) | Selected for MVP through ADR-006/T05; deferred-domain clauses excluded |
| [ADR-003 — Durable external attempts](ADR-003-durable-external-attempts.md) | Selected MVP outbox, idempotency and truthful outcome rules; provider/runner details deferred |
| [ADR-004 — Compatible evolution](ADR-004-compatible-incremental-design-evolution.md) | Selected MVP evolution/compatibility principles |
| [ADR-005 — Owner system boundaries](ADR-005-owner-mvp-system-boundaries.md) | Accepted Core / independent ProjectForge / private media scope |
| [ADR-006 — Implementation baseline](ADR-006-selected-mvp-implementation-baseline.md) | Selected mechanisms, alternatives, consequences and evidence gates |
| [ADR-007 — React and Inertia frontend](ADR-007-react-inertia-frontend.md) | Selected by Farhad; replaces interactive Blade/Alpine, retains Blade PDF templates |

Use the existing records as examples when a consequential design choice needs a new ADR. Record context/source, alternatives, selected behavior, rationale, impacts, authority/date, verification and revisit conditions. A later material decision supersedes rather than erases the earlier rationale. No new choice or runtime Pass is established by editing this index.

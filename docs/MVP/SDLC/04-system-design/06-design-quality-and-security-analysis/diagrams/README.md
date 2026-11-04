# Quality and Security — Diagram Catalog

Keep editable sources and SVG/PNG exports synchronized. These are proposed quality/design evaluation views, not product-test evidence.

## MVP system allocation and design status

The accepted system boundary separates the Resumefolio core from ProjectForge, joined by an authenticated user-scoped API. Logical responsibilities remain useful within each system; they do not authorize a shared core/ProjectForge process, database or transaction. Core owns dashboard, invited accounts, professional presentation, protected sharing, manual applications and same-server private My Files & Media. ProjectForge MVP owns real repositories/transfers/permissions, file/history browsing, issues and simple Kanban. Its engine, deployment and database remain open. The future communications system is independently private and API connected. Advanced Git review/releases, backlog/Sprints and execution/deployment remain deferred. Keep source, independent resume draft, explicit publication and actual submitted material identities distinct. Profile changes require preview/select/apply and cannot mutate publication or submitted history. Manual applications include status, next action and follow-up date without mail/calendar dependencies.

Authority: [OWNER-MVP-2026-11-04](../../../01-project-planning/owner-mvp-decision-2026-11-04.md).

## Quality attributes and design trade-offs

- [Quality scenarios and required evidence](quality-scenario-evidence-map.svg) · [PlantUML](quality-scenario-evidence-map.puml) · [PNG](quality-scenario-evidence-map.png)
- [Scenario-based trade-off evaluation](quality-tradeoff-evaluation-route.svg) · [PlantUML](quality-tradeoff-evaluation-route.puml) · [PNG](quality-tradeoff-evaluation-route.png)

[Owning document](../01-quality-attributes-and-design-trade-offs.md). Proposed evaluation coverage and procedure; targets, actual measurements and scoped acceptance remain pending.

## Security threat model and trust boundaries

- [Logical trust boundaries](security-trust-boundaries.svg) · [PlantUML](security-trust-boundaries.puml) · [PNG](security-trust-boundaries.png)
- [Current scoped authority and consequential admission](security-current-authority-sequence.svg) · [PlantUML](security-current-authority-sequence.puml) · [PNG](security-current-authority-sequence.png)

[Owning document](../02-security-threat-modeling-and-trust-boundaries.md). Proposed bounded threat/control views; actual policy reconciliation, mechanisms and security verification remain pending.

## Operations, backup and recovery

- [Recoverable set and independent protected copy](operations-recovery-coverage.svg) · [PlantUML](operations-recovery-coverage.puml) · [PNG](operations-recovery-coverage.png)
- [Isolated restore and guarded resumption](operations-isolated-restore-route.svg) · [PlantUML](operations-isolated-restore-route.puml) · [PNG](operations-isolated-restore-route.png)

[Owning document](../03-operations-backup-recovery-and-resilience.md). Proposed operating/recovery procedures. Actual facilities, backup setup, targets and usable restoration evidence remain pending.

## User interface and accessibility

- [Explicit review, draft save and publication](ui-source-apply-publication.svg) · [PlantUML](ui-source-apply-publication.puml) · [PNG](ui-source-apply-publication.png)
- [Truthful outcomes and safe recovery actions](ui-outcome-recovery-route.svg) · [PlantUML](ui-outcome-recovery-route.puml) · [PNG](ui-outcome-recovery-route.png)

[Owning document](../04-user-interface-accessibility-and-interaction-quality.md). Proposed interaction behavior, not screen prototypes or conformance evidence. Actual widgets, client compatibility and accessibility validation remain pending.

## Design review, traceability and handoff

- [Exact criterion to design and evidence trace chain](review-trace-chain.svg) · [PlantUML](review-trace-chain.puml) · [PNG](review-trace-chain.png)
- [Scoped candidate and implementation handoff gates](review-handoff-gates.svg) · [PlantUML](review-handoff-gates.puml) · [PNG](review-handoff-gates.png)

[Owning document](../05-design-review-traceability-and-handoff.md). Review procedure views, not performed criterion comparisons, product-test results or owner baseline disposition.

## Essential quality and trade-off views

- [Concrete quality scenario and evidence contract](quality-essential-scenario.svg) · [PlantUML](quality-essential-scenario.puml) · [PNG](quality-essential-scenario.png)
- [Quality trade-off hypotheses and non-negotiable invariants](quality-essential-conflicts.svg) · [PlantUML](quality-essential-conflicts.puml) · [PNG](quality-essential-conflicts.png)
- [Candidate tactics mapped to scenario responsibilities](quality-essential-tactics.svg) · [PlantUML](quality-essential-tactics.puml) · [PNG](quality-essential-tactics.png)

[Owning quality evaluation guide](../01-quality-attributes-and-design-trade-offs.md#6-essential-quality-and-trade-off-views). Utility tree/radar and evaluation route reused; no measured improvement or accepted ranking implied.

## November 4 release applicability

Current MVP figures replace the former common-product boundary. Future and historical figures retain their details without committing them to MVP.

| Editable source | Current applicability |
| --- | --- |
| [security-trust-boundaries.puml](security-trust-boundaries.puml) | MVP systems|

## Complete diagram alignment — November 4

[Full project inventory and verification limits](../../../diagram-alignment-review-2026-11-04.md). This current disposition supersedes earlier partial diagram-allocation lists.

| Editable source or visual | Current applicability | Matching exports |
| --- | --- | --- |
| [operations-isolated-restore-route.puml](operations-isolated-restore-route.puml) | MVP core / cross-cutting| [SVG](operations-isolated-restore-route.svg) · [PNG](operations-isolated-restore-route.png) |
| [operations-recovery-coverage.puml](operations-recovery-coverage.puml) | MVP core / cross-cutting| [SVG](operations-recovery-coverage.svg) · [PNG](operations-recovery-coverage.png) |
| [quality-essential-conflicts.puml](quality-essential-conflicts.puml) | MVP core / cross-cutting| [SVG](quality-essential-conflicts.svg) · [PNG](quality-essential-conflicts.png) |
| [quality-essential-scenario.puml](quality-essential-scenario.puml) | MVP core / cross-cutting| [SVG](quality-essential-scenario.svg) · [PNG](quality-essential-scenario.png) |
| [quality-essential-tactics.puml](quality-essential-tactics.puml) | MVP core / cross-cutting| [SVG](quality-essential-tactics.svg) · [PNG](quality-essential-tactics.png) |
| [quality-scenario-evidence-map.puml](quality-scenario-evidence-map.puml) | Method / document navigation| [SVG](quality-scenario-evidence-map.svg) · [PNG](quality-scenario-evidence-map.png) |
| [quality-tradeoff-evaluation-route.puml](quality-tradeoff-evaluation-route.puml) | MVP core / cross-cutting| [SVG](quality-tradeoff-evaluation-route.svg) · [PNG](quality-tradeoff-evaluation-route.png) |
| [review-handoff-gates.puml](review-handoff-gates.puml) | MVP core / cross-cutting| [SVG](review-handoff-gates.svg) · [PNG](review-handoff-gates.png) |
| [review-trace-chain.puml](review-trace-chain.puml) | MVP core / cross-cutting| [SVG](review-trace-chain.svg) · [PNG](review-trace-chain.png) |
| [security-current-authority-sequence.puml](security-current-authority-sequence.puml) | MVP core / cross-cutting| [SVG](security-current-authority-sequence.svg) · [PNG](security-current-authority-sequence.png) |
| [security-trust-boundaries.puml](security-trust-boundaries.puml) | MVP systems| [SVG](security-trust-boundaries.svg) · [PNG](security-trust-boundaries.png) |
| [ui-outcome-recovery-route.puml](ui-outcome-recovery-route.puml) | MVP core / cross-cutting| [SVG](ui-outcome-recovery-route.svg) · [PNG](ui-outcome-recovery-route.png) |
| [ui-source-apply-publication.puml](ui-source-apply-publication.puml) | MVP core / cross-cutting| [SVG](ui-source-apply-publication.svg) · [PNG](ui-source-apply-publication.png) |

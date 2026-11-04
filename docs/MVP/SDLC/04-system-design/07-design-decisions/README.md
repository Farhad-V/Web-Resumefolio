# Resumefolio â€” Design Decisions

## Current implementation baseline â€” November 4, 2026

[BL-MVP-2026-11-04.1](../../../baseline/README.md) selects the MVP technical mechanisms, numerical policies, priorities and requirement/criterion dispositions under Farhadâ€™s explicit delegation. It supersedes earlier Proposed/pending mechanism and whole-baseline statements below for MVP design input. Future clauses and dated evidence remain separate. Runtime/actor validation, credentials, Git isolation, capacity and backup/restore still require the named implementation/Release gates; this update reports no product test Pass.

### Prior source material and rationale (superseded where this Baseline selects a different MVP choice)

**Use this folder to understand consequential technical choices, their alternatives, rationale, consequences and actual status.** Architecture Decision Records (ADRs) link the detailed owning designs; they do not replace requirements, component specifications or verification evidence.

Owner and decision authority: Farhad. Updated November 4, 2026.

**Current position:** five concrete ADRs and the reusable template are populated. ADR-005 records the accepted owner system boundary; ADR-001 is superseded in part; ADR-002â€“004 retain their proposed technical status. Updating the records does not accept a baseline, authorize implementation/spending or establish product readiness.

[Records](#1-decision-register) Â· [Reading route](#2-reading-route-and-relationships) Â· [Status](#3-status-and-authority) Â· [Maintenance](#4-adding-and-evolving-records) Â· [Review](#5-review-and-current-limits)

## MVP system allocation and design status

The accepted system boundary separates the Resumefolio core from ProjectForge, joined by an authenticated user-scoped API. Logical responsibilities remain useful within each system; they do not authorize a shared core/ProjectForge process, database or transaction. Core owns dashboard, invited accounts, professional presentation, protected sharing, manual applications and same-server private My Files & Media. ProjectForge MVP owns real repositories/transfers/permissions, file/history browsing, issues and simple Kanban. Its selected engine is native Git Smart HTTP behind the independent Laravel ProjectForge service, with its own MySQL 8.4 database and OS/storage boundaries on the existing host; BL-MVP-2026-11-04.1 governs implementation and evidence gates. The future communications system is independently private and API connected. Advanced Git review/releases, backlog/Sprints and execution/deployment remain deferred. Keep source, independent resume draft, explicit publication and actual submitted material identities distinct. Profile changes require preview/select/apply and cannot mutate publication or submitted history. Manual applications include status, next action and follow-up date without mail/calendar dependencies.

Authority: [OWNER-MVP-2026-11-04](../../01-project-planning/owner-mvp-decision-2026-11-04.md).

## 1. Decision register

| Record | Proposed technical direction | Status |
| --- | --- | --- |
| [ADR-001 â€” Modular Application Boundaries](ADR-001-modular-application-boundaries.md) | Historical common-application proposal; logical ownership retained | Superseded in part by ADR-005 |
| [ADR-002 â€” Explicit Publication and Historical Material Identity](ADR-002-explicit-publication-and-history.md) | Distinct source, independent draft, immutable publication and actual-material contexts with protected references | Proposed technical realization |
| [ADR-003 â€” Durable External Attempts and Reconciliation](ADR-003-durable-external-attempts.md) | Durable intent, attributable attempts, guarded dispatch and reconciliation of uncertain effects | Proposed |
| [ADR-004 â€” Compatible Incremental Design Evolution](ADR-004-compatible-incremental-design-evolution.md) | Compatibility, refactoring and evidence-guided evolution | Proposed |
| [ADR-005 â€” Owner MVP System Boundaries](ADR-005-owner-mvp-system-boundaries.md) | Core / separate ProjectForge API; same-server private media; future communications | Accepted owner boundary; mechanisms open |

[ADR template](ADR-template.md) provides authoring instructions, a reusable record structure and checks. It allocates no identifier or decision of its own.

## 2. Reading route and relationships

1. Start with [architecture drivers/options](../01-software-architecture/01-design-drivers-and-solution-options.md) and the relevant [source decisions](../../02-requirements-engineering/07-change-and-baseline/open-questions-and-decisions.md).
2. Read ADR-005 for the accepted system boundary and ADR-001 for its historical proposal and surviving internal ownership rationale. Follow its links to architecture/component/data/interface records for concrete realization.
3. Read ADR-002 for publication/history identities and reference obligations. Its accepted product basis is separate from the proposed storage/transaction mechanism.
4. Read ADR-003 for effects outside local transactions, including dispatch ownership, stale workers, unknown results and safe repetition limits.
5. Use [review/handoff](../06-design-quality-and-security-analysis/05-design-review-traceability-and-handoff.md) to assess the exact candidate and record actual findings/disposition.

The records complement each other: ownership defines who admits an operation; publication/history defines which content is meant; durable attempts preserve intended versus observed consequential effects. None alone specifies a final schema, selected provider, queue, runner or deployment facility.

Each ADR reuses an existing owning diagram: logical component ownership, revision/protected-reference relationships, or durable-attempt protocol. Follow the record's editable-source/export links rather than maintain a competing diagram set here.

## 3. Status and authority

| Status | Meaning and required provenance |
| --- | --- |
| Proposed | A reviewable technical recommendation; assumptions and dependent evidence remain visible |
| Accepted | An actual authorized disposition for an identified candidate/scope, with date, conditions and evidence reference |
| Rejected | The actual disposition rejects the proposal; retain its alternatives and rationale |
| Superseded | A later identified decision replaces an accepted choice; link both records and preserve history |

Do not infer acceptance from a populated file, successful link check, assistant recommendation or index entry. Record conditional disposition with its exact permitted/blocked scope rather than hide unresolved commitments under a bare Accepted label.

The [owner-accepted update/publication policy](../../02-requirements-engineering/07-change-and-baseline/open-questions-and-decisions.md#owner-accepted-profile-update-policy) remains settled product behavior. ADR-002's Proposed status does not reopen it. Conversely, an accepted product obligation does not automatically accept a particular schema, renderer, storage mechanism or numerical target.

## 4. Adding and evolving records

Create an ADR for a concrete consequential choice with meaningful alternatives or lasting implications. Routine formatting, settled-plan synchronization and every implementation detail need not become separate decisions.

Check the current register/files, allocate the next unused sequential identifier and copy the template to `ADR-[number]-[descriptive-title].md`. Do not preallocate IDs for hypothetical work or reuse a rejected/superseded identity. Add the actual title/status here and link affected source/owner records.

Include exact context/source/candidate, comparable options, rationale, consequences, unresolved conditions, verification and revisit triggers. Preserve current authority, independent publication/history, protected references and truthful external outcomes where applicable. Separate expected benefits from actual measurements.

Correct factual/documentary mistakes with attributable revision history. If an accepted choice materially changes, create a superseding record and retain the original rationale/disposition; do not rewrite history as though the new choice was always accepted. Follow [design evolution](../02-detailed-and-object-oriented-design/05-design-evolution-refactoring-and-technical-debt.md) for compatibility, migration and recovery consequences.

## 5. Review and current limits

Before relying on a decision, identify its exact source/design revisions and assess affected criteria, owner contracts, data/runtime boundaries, resource/operating costs and applicable compatibility/security/recovery evidence. Keep actual sanitized findings/results under [review evidence guidance](../06-design-quality-and-security-analysis/review-and-traceability/evidence/README.md).

Final physical mechanisms, exact criterion closure and dependent provider/Git/execution/recovery facilities remain pending at their affected gates. Existing OAuth-not-created and backups-not-configured facts do not become resolved through an ADR. No universal exactly-once effect, safe containment, redundant availability or usable restoration is established by these proposals.

Changes to scope/resources/targets and actual disposition follow existing authority and the agreed pre-implementation baseline sequence. Reconcile delivery/operations with the sole owner's total 20 project hours/week. This index records no new purchase, live change, test Pass, baseline acceptance or coding authorization.

The ADR organization is a project decision-record convention, not a university-mandated file tree. See the [reference map](../01-reference-and-coverage-map.md).

[System Design home](../README.md) Â· [ADR template](ADR-template.md) Â· [Review/handoff](../06-design-quality-and-security-analysis/05-design-review-traceability-and-handoff.md)

## Proposed evolution procedure

[ADR-004 â€” Compatible incremental design evolution](ADR-004-compatible-incremental-design-evolution.md) records a proposed procedure, not an accepted debt item or authorized migration.

## Current selected decision

[ADR-006 — Selected MVP implementation baseline](ADR-006-selected-mvp-implementation-baseline.md) records the delegated selection and exact relationship to ADR-001–005. The older counts/status discussion above describes its earlier register revision.

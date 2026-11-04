# ADR-006 — Selected MVP implementation baseline

Status: Selected under delegated authority, November 4, 2026. Supersedes open mechanism choices for the MVP; preserves OWNER-MVP-2026-11-04 system/scope decisions. [Baseline](../../../baseline/README.md).

## Context and decision

Farhad explicitly delegated completion of technical decisions and the Baseline. Select [T01–T10](../../../baseline/technical-decisions.md) and [Q-D01–28 dispositions](../../../baseline/policy-decisions.md). The frozen manifest identifies exact documentary inputs. Core and ProjectForge remain independent systems; the future communications platform remains deferred.

ADR-002’s explicit publication/history realization, ADR-003’s durable/outcome-truthful effects and ADR-004’s compatible incremental evolution are selected for MVP implementation subject to T05’s concrete transactions, protected artifact references, idempotency and outbox rules. Provider/workflow-specific portions remain deferred. ADR-001 cannot override the separate-system boundary already selected by ADR-005.

## Alternatives, consequences and validation

[Technical decisions](../../../baseline/technical-decisions.md) records the SPA/database/Git-platform alternatives, selected mechanisms and revisit triggers. The principal cost/risk is the independent identity/API/native Git boundary; G2 is mandatory before enabling it. Same-host operation remains a shared failure domain. No feature scope is removed to hide that risk.

Package patch resolution, target capacity, actor validation, SMTP, backup destination and demonstrated restore remain evidence/input gates, not undecided stack choices. No current runtime test is claimed. Changes require a revised ADR/Baseline, impacted criterion/test review, compatibility and recovery assessment. Documentation completion does not authorize deployment or implementation in this task.

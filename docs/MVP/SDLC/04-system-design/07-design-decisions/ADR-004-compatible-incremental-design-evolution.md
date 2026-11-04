# ADR-004 â€” Compatible Incremental Design Evolution

Current implementation choices and scope: [Baseline](../../../baseline/README.md). Runtime verification remains subject to its gates.

- Status: **Proposed**
- Date: November 2, 2026
- Decision authority: Farhad
- Scope: proposed engineering procedure; no migration or implementation authorized by this record

## Context

The modular application proposal must preserve current private authority, explicit source application/publication, independent actual submission materials and attributable external effects during structural change. This documentation update establishes no inspected implementation deficiency or running legacy baseline.

## Proposed decision

Prefer the smallest compatible, evidence-led change. Identify the exact baseline and affected contracts; establish focused checks; extract one responsibility or introduce a justified abstraction; verify behavior, real persistence/concurrency and affected adapters; switch one authoritative route; retire obsolete paths only when old consumers, pending work and recovery conditions permit.

Use branch by abstraction or a strangler facade only when an actual replacement need is established. Define per-operation/cohort authority, old/new contract compatibility, command/attempt identity, protected references, reconciliation and stop conditions. Avoid uncontrolled dual writes and shadow execution of sends, Git mutations, workflows or deployments.

## Alternatives

| Option | Consequence |
| --- | --- |
| Leave unchanged | Reasonable when no evidenced deficiency/value exists; record actual implications if a finding exists |
| Incremental compatible change | Smaller assessable steps; requires temporary compatibility and disciplined retirement |
| Broad rewrite / immediate extraction | Potential structural freedom, with larger verification, migration, distributed-failure and operating burden; requires separate justification |

## Consequences and limits

Temporary adapters and coexistence add maintenance work within the total 20 project hours/week. Refactoring preserves applicable behavior; source-policy or API behavior changes need separate disposition. Reverting code cannot undo irreversible data changes or remote effects. Stop, preserve evidence and select compatible rollback, reviewed forward repair or scoped recovery according to actual state.

## Validation and disposition

Before applying to real work, identify the exact candidate, observed finding, alternatives, full effort, affected criteria, checks, compatibility/recovery route and authorized scope. Close only with actual candidate-specific results and owner disposition. This proposal has no live test, migration result or acceptance evidence.

[Owning evolution procedure](../02-detailed-and-object-oriented-design/05-design-evolution-refactoring-and-technical-debt.md) Â· [ADR index](README.md) Â· [ADR-001 modular boundaries](ADR-001-modular-application-boundaries.md) Â· [ADR-002 publication/history](ADR-002-explicit-publication-and-history.md) Â· [ADR-003 external attempts](ADR-003-durable-external-attempts.md)

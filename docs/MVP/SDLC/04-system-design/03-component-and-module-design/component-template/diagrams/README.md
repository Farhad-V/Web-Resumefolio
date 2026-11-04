# Resumefolio — Component Template Diagram Catalog

**Status: five reusable illustrative views, November 2, 2026.** These diagrams accompany template guidance; they are not allocated actual component models, final types/schemas or executed tests.

## Examples and owning records

### Generic contract and ownership roles

[SVG preview](component-interface-realization-template.svg) · [Editable PlantUML](component-interface-realization-template.puml) · [PNG](component-interface-realization-template.png) · [Owning template](../01-responsibilities-and-interface-realization.md)

### Draft publication and actual-material identities

[SVG preview](component-data-class-template.svg) · [Editable PlantUML](component-data-class-template.puml) · [PNG](component-data-class-template.png) · [Owning template](../02-data-model-and-class-structure.md)

### Separate publication algorithm

[SVG preview](component-publication-algorithm-template.svg) · [Editable PlantUML](component-publication-algorithm-template.puml) · [PNG](component-publication-algorithm-template.png) · [Owning template](../03-detailed-behavior-and-algorithms.md)

### Uncertain-effect reconciliation

[SVG preview](component-failure-reconciliation-template.svg) · [Editable PlantUML](component-failure-reconciliation-template.puml) · [PNG](component-failure-reconciliation-template.png) · [Owning template](../04-technical-scenarios-and-failure-handling.md)

### Pattern selection and implementation constraints

[SVG preview](component-pattern-selection-template.svg) · [Editable PlantUML](component-pattern-selection-template.puml) · [PNG](component-pattern-selection-template.png) · [Owning template](../05-design-patterns-and-coding-constraints.md)

## Copying and maintenance

Replace generic/example roles with the actual component identity and source behavior when copied. Adjust backlinks for the actual package location. Keep editable source and SVG/PNG exports together, regenerate after semantic changes and inspect readability. Use notation/legend and explicit proposal/evidence labels; do not infer permission, cardinality, physical deployment or test success from an arrow.

These examples are optional supporting illustrations; a component may need different class, sequence, activity, state or data views. Link shared diagrams rather than maintaining competing architectural truth. Preserve original source/evidence status and record actual candidate review separately.

[Component template guide](../README.md) · [Component and Module Design](../../README.md)

## Responsibilities and interface contract package

- [Component: provided lollipop and required socket](contract-provided-required.svg) · [PlantUML](contract-provided-required.puml) · [PNG](contract-provided-required.png)
- [Realization: contract to implementation](contract-realization.svg) · [PlantUML](contract-realization.puml) · [PNG](contract-realization.png)
- [Component context and neighbors](contract-context.svg) · [PlantUML](contract-context.puml) · [PNG](contract-context.png)
- [Composite structure: ports and connectors](contract-ports-connectors.svg) · [PlantUML](contract-ports-connectors.puml) · [PNG](contract-ports-connectors.png)
- [Internal structure and responsibility allocation](contract-internal-parts.svg) · [PlantUML](contract-internal-parts.puml) · [PNG](contract-internal-parts.png)
- [Classes realizing the provided command](contract-class-realization.svg) · [PlantUML](contract-class-realization.puml) · [PNG](contract-class-realization.png)
- [Inbound and outbound dependencies](contract-dependencies.svg) · [PlantUML](contract-dependencies.puml) · [PNG](contract-dependencies.png)
- [Client calls the publication interface](contract-command-sequence.svg) · [PlantUML](contract-command-sequence.puml) · [PNG](contract-command-sequence.png)
- [Optional interface segregation: before and after](contract-segregation.svg) · [PlantUML](contract-segregation.puml) · [PNG](contract-segregation.png)

[Owning interface template and CRC/specification/contract/traceability tables](../01-responsibilities-and-interface-realization.md#9-visual-contract-and-responsibility-package). Replace example roles and source prompts before component-specific review.

## Data and class structure model package

- [Class structure: visibility, types and operations](model-classes.svg) · [PlantUML](model-classes.puml) · [PNG](model-classes.png)
- [ERD: selected persisted relationships](model-erd.svg) · [PlantUML](model-erd.puml) · [PNG](model-erd.png)
- [Logical model: identity and independent history](model-logical.svg) · [PlantUML](model-logical.puml) · [PNG](model-logical.png)
- [Physical schema example: keys and candidate indexes](model-physical.svg) · [PlantUML](model-physical.puml) · [PNG](model-physical.png)
- [Domain model: entities, values and aggregate candidates](model-domain.svg) · [PlantUML](model-domain.puml) · [PNG](model-domain.png)
- [Aggregate boundary: root, members and invariant](model-aggregate.svg) · [PlantUML](model-aggregate.puml) · [PNG](model-aggregate.png)
- [Relationship notation and multiplicity](model-multiplicity.svg) · [PlantUML](model-multiplicity.puml) · [PNG](model-multiplicity.png)
- [Object diagram: proposed sample instances](model-objects.svg) · [PlantUML](model-objects.puml) · [PNG](model-objects.png)
- [Inheritance hierarchy: justified alternative results](model-inheritance.svg) · [PlantUML](model-inheritance.puml) · [PNG](model-inheritance.png)
- [Publication revision lifecycle and observation](model-lifecycle.svg) · [PlantUML](model-lifecycle.puml) · [PNG](model-lifecycle.png)
- [DTO versus entity versus value object mapping](model-dto-values.svg) · [PlantUML](model-dto-values.puml) · [PNG](model-dto-values.png)

[Owning data/class template and mapping/dictionary/invariant tables](../02-data-model-and-class-structure.md#9-data-and-class-model-package). Conceptual, logical, physical and runtime examples are distinct; no schema or migration is allocated.

## Detailed behavior and algorithm package

- [Publication collaboration: alt, opt and loop](behavior-sequence.svg) · [PlantUML](behavior-sequence.puml) · [PNG](behavior-sequence.png)
- [Activity: guarded work and post-commit fork/join](behavior-activity.svg) · [PlantUML](behavior-activity.puml) · [PNG](behavior-activity.png)
- [Step-by-step publication algorithm](behavior-flowchart.svg) · [PlantUML](behavior-flowchart.puml) · [PNG](behavior-flowchart.png)
- [Event-driven command knowledge states](behavior-state.svg) · [PlantUML](behavior-state.puml) · [PNG](behavior-state.png)
- [Branching decision tree with precedence](behavior-decision-tree.svg) · [PlantUML](behavior-decision-tree.puml) · [PNG](behavior-decision-tree.png)
- [Communication diagram: numbered object messages](behavior-communication.svg) · [PlantUML](behavior-communication.puml) · [PNG](behavior-communication.png)
- [Optional timing: commit and lost response](behavior-timing.svg) · [PlantUML](behavior-timing.puml) · [PNG](behavior-timing.png)
- [Algorithm data structures and identities](behavior-structures.svg) · [PlantUML](behavior-structures.puml) · [PNG](behavior-structures.png)
- [Error and exception handling](behavior-errors.svg) · [PlantUML](behavior-errors.puml) · [PNG](behavior-errors.png)
- [Optional concurrency: guarded competing publications](behavior-concurrency.svg) · [PlantUML](behavior-concurrency.puml) · [PNG](behavior-concurrency.png)

[Owning behavior template, pseudocode and decision/trace/complexity/comparison tables](../03-detailed-behavior-and-algorithms.md#9-behavior-and-algorithm-visual-package). Synthetic timings and analytical costs are not runtime policies or measurements.

## Technical failure and resilience package

- [Happy and failure paths for one external attempt](failure-sequence.svg) · [PlantUML](failure-sequence.puml) · [PNG](failure-sequence.png)
- [Failure classification and safe next action](failure-error-flow.svg) · [PlantUML](failure-error-flow.puml) · [PNG](failure-error-flow.png)
- [Proposed error vocabulary hierarchy](failure-exception-types.svg) · [PlantUML](failure-exception-types.puml) · [PNG](failure-exception-types.png)
- [Conditional retry and backoff timeline](failure-retry-backoff.svg) · [PlantUML](failure-retry-backoff.puml) · [PNG](failure-retry-backoff.png)
- [Optional circuit breaker state machine](failure-circuit-breaker.svg) · [PlantUML](failure-circuit-breaker.puml) · [PNG](failure-circuit-breaker.png)
- [Deadline and remaining-budget propagation](failure-deadlines.svg) · [PlantUML](failure-deadlines.puml) · [PNG](failure-deadlines.png)
- [Optional resilience controls at admission boundaries](failure-resilience.svg) · [PlantUML](failure-resilience.puml) · [PNG](failure-resilience.png)
- [Identity binding and deduplication flow](failure-idempotency.svg) · [PlantUML](failure-idempotency.puml) · [PNG](failure-idempotency.png)
- [Conditional saga compensation and irreversible limits](failure-compensation.svg) · [PlantUML](failure-compensation.puml) · [PNG](failure-compensation.png)
- [Local transaction versus external consistency](failure-transactions.svg) · [PlantUML](failure-transactions.puml) · [PNG](failure-transactions.png)
- [Capability degraded, recovering and failed states](failure-service-states.svg) · [PlantUML](failure-service-states.puml) · [PNG](failure-service-states.png)
- [Dependency failure and affected capability](failure-dependency-impact.svg) · [PlantUML](failure-dependency-impact.puml) · [PNG](failure-dependency-impact.png)
- [Optional race: expired claim and stale completion](failure-claim-race.svg) · [PlantUML](failure-claim-race.puml) · [PNG](failure-claim-race.png)
- [Optional corruption detection and isolated recovery](failure-corruption.svg) · [PlantUML](failure-corruption.puml) · [PNG](failure-corruption.png)
- [Optional fault tree: duplicate consequential effect](failure-fault-tree.svg) · [PlantUML](failure-fault-tree.puml) · [PNG](failure-fault-tree.png)

[Owning technical scenario template and six failure/quality/observability tables](../04-technical-scenarios-and-failure-handling.md#9-failure-and-resilience-visual-package). Optional controls, symbolic delays and error vocabulary are not selected implementation or verified facilities.

## Pattern participants and coding rules package

- [Strategy participants](pattern-strategy.svg) · [PlantUML](pattern-strategy.puml) · [PNG](pattern-strategy.png)
- [Adapter participants](pattern-adapter.svg) · [PlantUML](pattern-adapter.puml) · [PNG](pattern-adapter.png)
- [Factory participants](pattern-factory.svg) · [PlantUML](pattern-factory.puml) · [PNG](pattern-factory.png)
- [Facade participants](pattern-facade.svg) · [PlantUML](pattern-facade.puml) · [PNG](pattern-facade.png)
- [Optional Repository-like persistence port](pattern-repository.svg) · [PlantUML](pattern-repository.puml) · [PNG](pattern-repository.png)
- [Without versus with justified Strategy](pattern-before-after.svg) · [PlantUML](pattern-before-after.puml) · [PNG](pattern-before-after.png)
- [Strategy runtime collaboration](pattern-sequence.svg) · [PlantUML](pattern-sequence.puml) · [PNG](pattern-sequence.png)
- [Patterns across logical component roles](pattern-components.svg) · [PlantUML](pattern-components.puml) · [PNG](pattern-components.png)
- [Optional Strategy object instances](pattern-objects.svg) · [PlantUML](pattern-objects.puml) · [PNG](pattern-objects.png)
- [Optional State pattern evaluation](pattern-state-option.svg) · [PlantUML](pattern-state-option.puml) · [PNG](pattern-state-option.png)
- [Dependency inversion through the adapter seam](pattern-dependency-inversion.svg) · [PlantUML](pattern-dependency-inversion.puml) · [PNG](pattern-dependency-inversion.png)
- [Allowed versus forbidden dependencies](pattern-layers.svg) · [PlantUML](pattern-layers.puml) · [PNG](pattern-layers.png)
- [Illustrative package and folder conventions](pattern-packages.svg) · [PlantUML](pattern-packages.puml) · [PNG](pattern-packages.png)

[Owning patterns template, selection/rule tables, checklist, pseudocode and unallocated ADR form](../05-design-patterns-and-coding-constraints.md#8-pattern-and-coding-rule-package). Candidate roles are not implemented classes or adopted tool/version policies.

## Complete diagram alignment — November 4

[Full project inventory and verification limits](../../../../diagram-alignment-review-2026-11-04.md). This current disposition supersedes earlier partial diagram-allocation lists.

| Editable source or visual | Current applicability | Matching exports |
| --- | --- | --- |
| [behavior-activity.puml](behavior-activity.puml) | Reference / reusable template| [SVG](behavior-activity.svg) · [PNG](behavior-activity.png) |
| [behavior-communication.puml](behavior-communication.puml) | Reference / reusable template| [SVG](behavior-communication.svg) · [PNG](behavior-communication.png) |
| [behavior-concurrency.puml](behavior-concurrency.puml) | Reference / reusable template| [SVG](behavior-concurrency.svg) · [PNG](behavior-concurrency.png) |
| [behavior-decision-tree.puml](behavior-decision-tree.puml) | Reference / reusable template| [SVG](behavior-decision-tree.svg) · [PNG](behavior-decision-tree.png) |
| [behavior-errors.puml](behavior-errors.puml) | Reference / reusable template| [SVG](behavior-errors.svg) · [PNG](behavior-errors.png) |
| [behavior-flowchart.puml](behavior-flowchart.puml) | Reference / reusable template| [SVG](behavior-flowchart.svg) · [PNG](behavior-flowchart.png) |
| [behavior-sequence.puml](behavior-sequence.puml) | Reference / reusable template| [SVG](behavior-sequence.svg) · [PNG](behavior-sequence.png) |
| [behavior-state.puml](behavior-state.puml) | Reference / reusable template| [SVG](behavior-state.svg) · [PNG](behavior-state.png) |
| [behavior-structures.puml](behavior-structures.puml) | Reference / reusable template| [SVG](behavior-structures.svg) · [PNG](behavior-structures.png) |
| [behavior-timing.puml](behavior-timing.puml) | Reference / reusable template| [SVG](behavior-timing.svg) · [PNG](behavior-timing.png) |
| [component-data-class-template.puml](component-data-class-template.puml) | Reference / reusable template| [SVG](component-data-class-template.svg) · [PNG](component-data-class-template.png) |
| [component-failure-reconciliation-template.puml](component-failure-reconciliation-template.puml) | Reference / reusable template| [SVG](component-failure-reconciliation-template.svg) · [PNG](component-failure-reconciliation-template.png) |
| [component-interface-realization-template.puml](component-interface-realization-template.puml) | Reference / reusable template| [SVG](component-interface-realization-template.svg) · [PNG](component-interface-realization-template.png) |
| [component-pattern-selection-template.puml](component-pattern-selection-template.puml) | Reference / reusable template| [SVG](component-pattern-selection-template.svg) · [PNG](component-pattern-selection-template.png) |
| [component-publication-algorithm-template.puml](component-publication-algorithm-template.puml) | Reference / reusable template| [SVG](component-publication-algorithm-template.svg) · [PNG](component-publication-algorithm-template.png) |
| [contract-class-realization.puml](contract-class-realization.puml) | Reference / reusable template| [SVG](contract-class-realization.svg) · [PNG](contract-class-realization.png) |
| [contract-command-sequence.puml](contract-command-sequence.puml) | Reference / reusable template| [SVG](contract-command-sequence.svg) · [PNG](contract-command-sequence.png) |
| [contract-context.puml](contract-context.puml) | Reference / reusable template| [SVG](contract-context.svg) · [PNG](contract-context.png) |
| [contract-dependencies.puml](contract-dependencies.puml) | Reference / reusable template| [SVG](contract-dependencies.svg) · [PNG](contract-dependencies.png) |
| [contract-internal-parts.puml](contract-internal-parts.puml) | Reference / reusable template| [SVG](contract-internal-parts.svg) · [PNG](contract-internal-parts.png) |
| [contract-ports-connectors.puml](contract-ports-connectors.puml) | Reference / reusable template| [SVG](contract-ports-connectors.svg) · [PNG](contract-ports-connectors.png) |
| [contract-provided-required.puml](contract-provided-required.puml) | Reference / reusable template| [SVG](contract-provided-required.svg) · [PNG](contract-provided-required.png) |
| [contract-realization.puml](contract-realization.puml) | Reference / reusable template| [SVG](contract-realization.svg) · [PNG](contract-realization.png) |
| [contract-segregation.puml](contract-segregation.puml) | Reference / reusable template| [SVG](contract-segregation.svg) · [PNG](contract-segregation.png) |
| [failure-circuit-breaker.puml](failure-circuit-breaker.puml) | Reference / reusable template| [SVG](failure-circuit-breaker.svg) · [PNG](failure-circuit-breaker.png) |
| [failure-claim-race.puml](failure-claim-race.puml) | Reference / reusable template| [SVG](failure-claim-race.svg) · [PNG](failure-claim-race.png) |
| [failure-compensation.puml](failure-compensation.puml) | Reference / reusable template| [SVG](failure-compensation.svg) · [PNG](failure-compensation.png) |
| [failure-corruption.puml](failure-corruption.puml) | Reference / reusable template| [SVG](failure-corruption.svg) · [PNG](failure-corruption.png) |
| [failure-deadlines.puml](failure-deadlines.puml) | Reference / reusable template| [SVG](failure-deadlines.svg) · [PNG](failure-deadlines.png) |
| [failure-dependency-impact.puml](failure-dependency-impact.puml) | Reference / reusable template| [SVG](failure-dependency-impact.svg) · [PNG](failure-dependency-impact.png) |
| [failure-error-flow.puml](failure-error-flow.puml) | Reference / reusable template| [SVG](failure-error-flow.svg) · [PNG](failure-error-flow.png) |
| [failure-exception-types.puml](failure-exception-types.puml) | Reference / reusable template| [SVG](failure-exception-types.svg) · [PNG](failure-exception-types.png) |
| [failure-fault-tree.puml](failure-fault-tree.puml) | Reference / reusable template| [SVG](failure-fault-tree.svg) · [PNG](failure-fault-tree.png) |
| [failure-idempotency.puml](failure-idempotency.puml) | Reference / reusable template| [SVG](failure-idempotency.svg) · [PNG](failure-idempotency.png) |
| [failure-resilience.puml](failure-resilience.puml) | Reference / reusable template| [SVG](failure-resilience.svg) · [PNG](failure-resilience.png) |
| [failure-retry-backoff.puml](failure-retry-backoff.puml) | Reference / reusable template| [SVG](failure-retry-backoff.svg) · [PNG](failure-retry-backoff.png) |
| [failure-sequence.puml](failure-sequence.puml) | Reference / reusable template| [SVG](failure-sequence.svg) · [PNG](failure-sequence.png) |
| [failure-service-states.puml](failure-service-states.puml) | Reference / reusable template| [SVG](failure-service-states.svg) · [PNG](failure-service-states.png) |
| [failure-transactions.puml](failure-transactions.puml) | Reference / reusable template| [SVG](failure-transactions.svg) · [PNG](failure-transactions.png) |
| [model-aggregate.puml](model-aggregate.puml) | Reference / reusable template| [SVG](model-aggregate.svg) · [PNG](model-aggregate.png) |
| [model-classes.puml](model-classes.puml) | Reference / reusable template| [SVG](model-classes.svg) · [PNG](model-classes.png) |
| [model-domain.puml](model-domain.puml) | Reference / reusable template| [SVG](model-domain.svg) · [PNG](model-domain.png) |
| [model-dto-values.puml](model-dto-values.puml) | Reference / reusable template| [SVG](model-dto-values.svg) · [PNG](model-dto-values.png) |
| [model-erd.puml](model-erd.puml) | Reference / reusable template| [SVG](model-erd.svg) · [PNG](model-erd.png) |
| [model-inheritance.puml](model-inheritance.puml) | Reference / reusable template| [SVG](model-inheritance.svg) · [PNG](model-inheritance.png) |
| [model-lifecycle.puml](model-lifecycle.puml) | Reference / reusable template| [SVG](model-lifecycle.svg) · [PNG](model-lifecycle.png) |
| [model-logical.puml](model-logical.puml) | Reference / reusable template| [SVG](model-logical.svg) · [PNG](model-logical.png) |
| [model-multiplicity.puml](model-multiplicity.puml) | Reference / reusable template| [SVG](model-multiplicity.svg) · [PNG](model-multiplicity.png) |
| [model-objects.puml](model-objects.puml) | Reference / reusable template| [SVG](model-objects.svg) · [PNG](model-objects.png) |
| [model-physical.puml](model-physical.puml) | Reference / reusable template| [SVG](model-physical.svg) · [PNG](model-physical.png) |
| [pattern-adapter.puml](pattern-adapter.puml) | Reference / reusable template| [SVG](pattern-adapter.svg) · [PNG](pattern-adapter.png) |
| [pattern-before-after.puml](pattern-before-after.puml) | Reference / reusable template| [SVG](pattern-before-after.svg) · [PNG](pattern-before-after.png) |
| [pattern-components.puml](pattern-components.puml) | Reference / reusable template| [SVG](pattern-components.svg) · [PNG](pattern-components.png) |
| [pattern-dependency-inversion.puml](pattern-dependency-inversion.puml) | Reference / reusable template| [SVG](pattern-dependency-inversion.svg) · [PNG](pattern-dependency-inversion.png) |
| [pattern-facade.puml](pattern-facade.puml) | Reference / reusable template| [SVG](pattern-facade.svg) · [PNG](pattern-facade.png) |
| [pattern-factory.puml](pattern-factory.puml) | Reference / reusable template| [SVG](pattern-factory.svg) · [PNG](pattern-factory.png) |
| [pattern-layers.puml](pattern-layers.puml) | Reference / reusable template| [SVG](pattern-layers.svg) · [PNG](pattern-layers.png) |
| [pattern-objects.puml](pattern-objects.puml) | Reference / reusable template| [SVG](pattern-objects.svg) · [PNG](pattern-objects.png) |
| [pattern-packages.puml](pattern-packages.puml) | Reference / reusable template| [SVG](pattern-packages.svg) · [PNG](pattern-packages.png) |
| [pattern-repository.puml](pattern-repository.puml) | Reference / reusable template| [SVG](pattern-repository.svg) · [PNG](pattern-repository.png) |
| [pattern-sequence.puml](pattern-sequence.puml) | Reference / reusable template| [SVG](pattern-sequence.svg) · [PNG](pattern-sequence.png) |
| [pattern-state-option.puml](pattern-state-option.puml) | Reference / reusable template| [SVG](pattern-state-option.svg) · [PNG](pattern-state-option.png) |
| [pattern-strategy.puml](pattern-strategy.puml) | Reference / reusable template| [SVG](pattern-strategy.svg) · [PNG](pattern-strategy.png) |

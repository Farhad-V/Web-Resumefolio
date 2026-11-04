# Interface and API Design — Diagram Catalog

Keep editable sources and SVG/PNG exports synchronized. These are proposed technical interaction and compatibility views.

Current MVP scope and selected mechanisms: [Baseline](../../../../baseline/README.md). Deferred provider, advanced collaboration and workflow-execution designs are not MVP prerequisites.

## API protocols, contracts and compatibility

- [Identified command and actual outcome contract](api-command-outcome-sequence.svg) · [PlantUML](api-command-outcome-sequence.puml) · [PNG](api-command-outcome-sequence.png)
- [Contract evolution and compatibility](api-contract-evolution.svg) · [PlantUML](api-contract-evolution.puml) · [PNG](api-contract-evolution.png)

[Owning document](../01-api-protocols-contracts-and-compatibility.md). Proposed shared contract behavior. Exact routes/types, framework and external compatibility, dispatch and transition mechanisms remain implementation work.

## Use-case realizations and interactions

- [Independent Git, execution and deployment admission](interaction-git-execution-deployment.svg) · [PlantUML](interaction-git-execution-deployment.puml) · [PNG](interaction-git-execution-deployment.png)
- [Isolated recovery and resumption gate](interaction-isolated-recovery.svg) · [PlantUML](interaction-isolated-recovery.puml) · [PNG](interaction-isolated-recovery.png)

[Owning document](../03-use-case-realizations-and-interactions.md). Cross-component responsibility overviews complement detailed component-owned sequences; exact synchronization, compatibility and operating evidence remain pending.

## Essential API and contract views

- [Consumers, owner contracts and external adapters](api-essential-boundaries.svg) · [PlantUML](api-essential-boundaries.puml) · [PNG](api-essential-boundaries.png)
- [Protocol selection by actual boundary need](api-essential-selection.svg) · [PlantUML](api-essential-selection.puml) · [PNG](api-essential-selection.png)
- [Contract-first refinement without mandatory code generation](api-essential-contract-workflow.svg) · [PlantUML](api-essential-contract-workflow.puml) · [PNG](api-essential-contract-workflow.png)
- [Consumer expectations and provider verification](api-essential-consumer-verification.svg) · [PlantUML](api-essential-consumer-verification.puml) · [PNG](api-essential-consumer-verification.png)

[Owning API contract guide](../01-api-protocols-contracts-and-compatibility.md#9-essential-api-and-contract-views). Existing evolution/interaction views reused; no protocol, gateway, schema tooling or endpoint allocated.

## Essential use-case realization views

- [Selected actors and use-case boundaries](interaction-essential-use-cases.svg) · [PlantUML](interaction-essential-use-cases.puml) · [PNG](interaction-essential-use-cases.png)
- [Use-case realization through owner contracts](interaction-essential-realization.svg) · [PlantUML](interaction-essential-realization.puml) · [PNG](interaction-essential-realization.png)
- [Separate owner commands across the content journey](interaction-essential-end-to-end.svg) · [PlantUML](interaction-essential-end-to-end.puml) · [PNG](interaction-essential-end-to-end.png)
- [Alternate paths, duplicate commands and uncertain effects](interaction-essential-alternates.svg) · [PlantUML](interaction-essential-alternates.puml) · [PNG](interaction-essential-alternates.png)

[Owning interaction guide](../03-use-case-realizations-and-interactions.md#8-essential-use-case-realization-views). Existing detailed component sequences reused; no new source use cases, API payloads or execution evidence allocated.

## November 4 release applicability

Current MVP figures replace the former common-product boundary. Future and historical figures retain their details without committing them to MVP.

| Editable source | Current applicability |
| --- | --- |
| [api-essential-contract-workflow.puml](api-essential-contract-workflow.puml) | Method / document navigation|
| [interaction-git-execution-deployment.puml](interaction-git-execution-deployment.puml) | Future after MVP|

## Complete diagram alignment — November 4

[Full project inventory and verification limits](../../01-software-architecture/diagrams/README.md). This current disposition supersedes earlier partial diagram-allocation lists.

| Editable source or visual | Current applicability | Matching exports |
| --- | --- | --- |
| [api-command-outcome-sequence.puml](api-command-outcome-sequence.puml) | MVP core / cross-cutting| [SVG](api-command-outcome-sequence.svg) · [PNG](api-command-outcome-sequence.png) |
| [api-contract-evolution.puml](api-contract-evolution.puml) | MVP core / cross-cutting| [SVG](api-contract-evolution.svg) · [PNG](api-contract-evolution.png) |
| [api-essential-boundaries.puml](api-essential-boundaries.puml) | Mixed MVP / future| [SVG](api-essential-boundaries.svg) · [PNG](api-essential-boundaries.png) |
| [api-essential-consumer-verification.puml](api-essential-consumer-verification.puml) | MVP core / cross-cutting| [SVG](api-essential-consumer-verification.svg) · [PNG](api-essential-consumer-verification.png) |
| [api-essential-contract-workflow.puml](api-essential-contract-workflow.puml) | Method / document navigation| [SVG](api-essential-contract-workflow.svg) · [PNG](api-essential-contract-workflow.png) |
| [api-essential-selection.puml](api-essential-selection.puml) | Mixed MVP / future| [SVG](api-essential-selection.svg) · [PNG](api-essential-selection.png) |
| [interaction-essential-alternates.puml](interaction-essential-alternates.puml) | MVP core / cross-cutting| [SVG](interaction-essential-alternates.svg) · [PNG](interaction-essential-alternates.png) |
| [interaction-essential-end-to-end.puml](interaction-essential-end-to-end.puml) | MVP core / cross-cutting| [SVG](interaction-essential-end-to-end.svg) · [PNG](interaction-essential-end-to-end.png) |
| [interaction-essential-realization.puml](interaction-essential-realization.puml) | MVP core / cross-cutting| [SVG](interaction-essential-realization.svg) · [PNG](interaction-essential-realization.png) |
| [interaction-essential-use-cases.puml](interaction-essential-use-cases.puml) | MVP core / cross-cutting| [SVG](interaction-essential-use-cases.svg) · [PNG](interaction-essential-use-cases.png) |
| [interaction-git-execution-deployment.puml](interaction-git-execution-deployment.puml) | Future after MVP| [SVG](interaction-git-execution-deployment.svg) · [PNG](interaction-git-execution-deployment.png) |
| [interaction-isolated-recovery.puml](interaction-isolated-recovery.puml) | Mixed MVP / future| [SVG](interaction-isolated-recovery.svg) · [PNG](interaction-isolated-recovery.png) |

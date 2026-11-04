# Resumefolio — Detailed and OO Design Diagrams

These are proposed technical illustrations, not implemented classes or complete component models. Read each with the owning document and refine exact signatures/types in the actual component package.

- [Responsibilities and dependency direction](oo-responsibility-direction.svg) · [Editable source](oo-responsibility-direction.dot) · [PNG](oo-responsibility-direction.png)
- [Selected publication class design](publication-use-case-classes.svg) · [Editable source](publication-use-case-classes.puml) · [PNG](publication-use-case-classes.png)
- [Pattern selection and review](pattern-selection-route.svg) · [Editable source](pattern-selection-route.dot) · [PNG](pattern-selection-route.png)

[Owning principles document](../01-design-principles-and-object-oriented-approach.md) · [Detailed Design index](../README.md)

Current MVP scope and selected mechanisms: [Baseline](../../../../baseline/README.md). Deferred provider, advanced collaboration and workflow-execution designs are not MVP prerequisites.

## Design evolution and debt

- [Finding classification](design-finding-classification.svg) · [DOT](design-finding-classification.dot) · [PNG](design-finding-classification.png)
- [Change impact and verification](design-change-impact-route.svg) · [DOT](design-change-impact-route.dot) · [PNG](design-change-impact-route.png)
- [Compatible data and contract evolution](compatible-design-evolution.svg) · [DOT](compatible-design-evolution.dot) · [PNG](compatible-design-evolution.png)

[Owning evolution procedure](../05-design-evolution-refactoring-and-technical-debt.md). Proposed procedures; no actual code debt finding or performed migration/refactoring is implied.

## Expanded OO principles package

- [Before and after: separate reasons to change](oo-before-after.svg) · [PlantUML](oo-before-after.puml) · [PNG](oo-before-after.png)
- [Object diagram: one illustrative publication collaboration](oo-runtime-objects.svg) · [PlantUML](oo-runtime-objects.puml) · [PNG](oo-runtime-objects.png)
- [Package diagram: acyclic source dependencies](oo-packages.svg) · [PlantUML](oo-packages.puml) · [PNG](oo-packages.png)
- [Dependency inversion at the persistence boundary](oo-dependency-inversion.svg) · [PlantUML](oo-dependency-inversion.puml) · [PNG](oo-dependency-inversion.png)
- [Inheritance versus composition: rendition variation](oo-composition.svg) · [PlantUML](oo-composition.puml) · [PNG](oo-composition.png)
- [Interface realization and narrow consumer access](oo-realization.svg) · [PlantUML](oo-realization.puml) · [PNG](oo-realization.png)
- [Coupling and cohesion: compare responsibility shapes](oo-coupling-cohesion.svg) · [PlantUML](oo-coupling-cohesion.puml) · [PNG](oo-coupling-cohesion.png)
- [Sequence: explicit publication object collaboration](oo-publication-sequence.svg) · [PlantUML](oo-publication-sequence.puml) · [PNG](oo-publication-sequence.png)
- [Conceptual domain model: independent identities](oo-conceptual-domain.svg) · [PlantUML](oo-conceptual-domain.puml) · [PNG](oo-conceptual-domain.png)
- [Law of Demeter: request an intention, avoid navigation chains](oo-demeter.svg) · [PlantUML](oo-demeter.puml) · [PNG](oo-demeter.png)
- [Optional Strategy preview: exact representation resolution](oo-strategy-preview.svg) · [PlantUML](oo-strategy-preview.puml) · [PNG](oo-strategy-preview.png)

[Owning principles document, CRC/SOLID/scenario tables](../01-design-principles-and-object-oriented-approach.md#8-object-oriented-visual-and-responsibility-package). Proposed illustrations; counterexamples are not observed defects.

## Expanded evolution and debt package

- [Before/after class responsibilities](evolution-class-change.svg) · [PlantUML](evolution-class-change.puml) · [PNG](evolution-class-change.png)
- [Step-by-step transformation and verification](evolution-refactoring-sequence.svg) · [PlantUML](evolution-refactoring-sequence.puml) · [PNG](evolution-refactoring-sequence.png)
- [Hypothetical dependency cycle and hotspot](evolution-dependency-hotspots.svg) · [PlantUML](evolution-dependency-hotspots.puml) · [PNG](evolution-dependency-hotspots.png)
- [Before/after package dependency direction](evolution-package-direction.svg) · [PlantUML](evolution-package-direction.puml) · [PNG](evolution-package-direction.png)
- [Intended versus eroded architecture](evolution-erosion.svg) · [PlantUML](evolution-erosion.puml) · [PNG](evolution-erosion.png)
- [Design evolution timeline and ADR history](evolution-history.svg) · [PlantUML](evolution-history.puml) · [PNG](evolution-history.png)
- [Strangler facade: conditional future replacement](evolution-strangler.svg) · [PlantUML](evolution-strangler.puml) · [PNG](evolution-strangler.png)
- [Branch by abstraction inside one application](evolution-branch-abstraction.svg) · [PlantUML](evolution-branch-abstraction.puml) · [PNG](evolution-branch-abstraction.png)
- [Legacy-shaped versus target component state](evolution-component-target.svg) · [PlantUML](evolution-component-target.puml) · [PNG](evolution-component-target.png)
- [Refactoring/migration work lifecycle](evolution-lifecycle.svg) · [PlantUML](evolution-lifecycle.puml) · [PNG](evolution-lifecycle.png)
- [Contract-oriented verification safety net](evolution-safety-net.svg) · [PlantUML](evolution-safety-net.puml) · [PNG](evolution-safety-net.png)
- [Technical debt quadrant](evolution-debt-quadrant.svg) · [PNG](evolution-debt-quadrant.png)
- [Impact versus effort matrix](evolution-impact-effort.svg) · [PNG](evolution-impact-effort.png)
- [Conceptual debt interest curve](evolution-interest-curve.svg) · [PNG](evolution-interest-curve.png)
- [Illustrative churn versus complexity hotspot chart](evolution-churn-complexity.svg) · [PNG](evolution-churn-complexity.png)

[Generator](evolution-visuals-generator.py) · [Synthetic chart data](evolution-chart-data.json) · [Owning procedure and tables](../05-design-evolution-refactoring-and-technical-debt.md#8-evolution-and-debt-visual-package). All counterexamples/measurements are illustrative, not observed findings.

## Section orientation and learning maps

- [Section learning path](oo-index-reading-path.svg) · [PlantUML](oo-index-reading-path.puml) · [PNG](oo-index-reading-path.png)
- [Principles, patterns and refactoring](oo-index-concept-map.svg) · [PlantUML](oo-index-concept-map.puml) · [PNG](oo-index-concept-map.png)
- [Prerequisites and reading dependencies](oo-index-prerequisites.svg) · [PlantUML](oo-index-prerequisites.puml) · [PNG](oo-index-prerequisites.png)
- [Architecture-to-detailed-design bridge](oo-index-architecture-bridge.svg) · [PlantUML](oo-index-architecture-bridge.puml) · [PNG](oo-index-architecture-bridge.png)
- [Levels of abstraction](oo-index-abstraction-levels.svg) · [PlantUML](oo-index-abstraction-levels.puml) · [PNG](oo-index-abstraction-levels.png)
- [Design lifecycle and feedback](oo-index-design-lifecycle.svg) · [PlantUML](oo-index-design-lifecycle.puml) · [PNG](oo-index-design-lifecycle.png)
- [Topic mind map](oo-index-topic-mindmap.svg) · [PlantUML](oo-index-topic-mindmap.puml) · [PNG](oo-index-topic-mindmap.png)

[Owning section index, glossary and cheat sheet](../README.md). Reading paths are guidance, not runtime dependencies or evidence of implemented design.

## Complete diagram alignment — November 4

[Full project inventory and verification limits](../../01-software-architecture/diagrams/README.md). This current disposition supersedes earlier partial diagram-allocation lists.

| Editable source or visual | Current applicability | Matching exports |
| --- | --- | --- |
| [compatible-design-evolution.dot](compatible-design-evolution.dot) | MVP core / cross-cutting| [SVG](compatible-design-evolution.svg) · [PNG](compatible-design-evolution.png) |
| [design-change-impact-route.dot](design-change-impact-route.dot) | MVP core / cross-cutting| [SVG](design-change-impact-route.svg) · [PNG](design-change-impact-route.png) |
| [design-finding-classification.dot](design-finding-classification.dot) | MVP core / cross-cutting| [SVG](design-finding-classification.svg) · [PNG](design-finding-classification.png) |
| [evolution-branch-abstraction.puml](evolution-branch-abstraction.puml) | Reference / design method| [SVG](evolution-branch-abstraction.svg) · [PNG](evolution-branch-abstraction.png) |
| [evolution-churn-complexity.svg](evolution-churn-complexity.svg) | Reference / illustrative chart | [SVG](evolution-churn-complexity.svg) · [PNG](evolution-churn-complexity.png) |
| [evolution-class-change.puml](evolution-class-change.puml) | Reference / design method| [SVG](evolution-class-change.svg) · [PNG](evolution-class-change.png) |
| [evolution-component-target.puml](evolution-component-target.puml) | Reference / design method| [SVG](evolution-component-target.svg) · [PNG](evolution-component-target.png) |
| [evolution-debt-quadrant.svg](evolution-debt-quadrant.svg) | Reference / illustrative chart | [SVG](evolution-debt-quadrant.svg) · [PNG](evolution-debt-quadrant.png) |
| [evolution-dependency-hotspots.puml](evolution-dependency-hotspots.puml) | Reference / design method| [SVG](evolution-dependency-hotspots.svg) · [PNG](evolution-dependency-hotspots.png) |
| [evolution-erosion.puml](evolution-erosion.puml) | Reference / design method| [SVG](evolution-erosion.svg) · [PNG](evolution-erosion.png) |
| [evolution-history.puml](evolution-history.puml) | Historical / alternative| [SVG](evolution-history.svg) · [PNG](evolution-history.png) |
| [evolution-impact-effort.svg](evolution-impact-effort.svg) | Reference / illustrative chart | [SVG](evolution-impact-effort.svg) · [PNG](evolution-impact-effort.png) |
| [evolution-interest-curve.svg](evolution-interest-curve.svg) | Reference / illustrative chart | [SVG](evolution-interest-curve.svg) · [PNG](evolution-interest-curve.png) |
| [evolution-lifecycle.puml](evolution-lifecycle.puml) | Reference / design method| [SVG](evolution-lifecycle.svg) · [PNG](evolution-lifecycle.png) |
| [evolution-package-direction.puml](evolution-package-direction.puml) | Reference / design method| [SVG](evolution-package-direction.svg) · [PNG](evolution-package-direction.png) |
| [evolution-refactoring-sequence.puml](evolution-refactoring-sequence.puml) | Reference / design method| [SVG](evolution-refactoring-sequence.svg) · [PNG](evolution-refactoring-sequence.png) |
| [evolution-safety-net.puml](evolution-safety-net.puml) | Reference / design method| [SVG](evolution-safety-net.svg) · [PNG](evolution-safety-net.png) |
| [evolution-strangler.puml](evolution-strangler.puml) | Reference / design method| [SVG](evolution-strangler.svg) · [PNG](evolution-strangler.png) |
| [oo-before-after.puml](oo-before-after.puml) | Reference / design method| [SVG](oo-before-after.svg) · [PNG](oo-before-after.png) |
| [oo-composition.puml](oo-composition.puml) | Reference / design method| [SVG](oo-composition.svg) · [PNG](oo-composition.png) |
| [oo-conceptual-domain.puml](oo-conceptual-domain.puml) | Reference / design method| [SVG](oo-conceptual-domain.svg) · [PNG](oo-conceptual-domain.png) |
| [oo-coupling-cohesion.puml](oo-coupling-cohesion.puml) | Reference / design method| [SVG](oo-coupling-cohesion.svg) · [PNG](oo-coupling-cohesion.png) |
| [oo-demeter.puml](oo-demeter.puml) | Reference / design method| [SVG](oo-demeter.svg) · [PNG](oo-demeter.png) |
| [oo-dependency-inversion.puml](oo-dependency-inversion.puml) | Reference / design method| [SVG](oo-dependency-inversion.svg) · [PNG](oo-dependency-inversion.png) |
| [oo-index-abstraction-levels.puml](oo-index-abstraction-levels.puml) | Reference / design method| [SVG](oo-index-abstraction-levels.svg) · [PNG](oo-index-abstraction-levels.png) |
| [oo-index-architecture-bridge.puml](oo-index-architecture-bridge.puml) | Reference / design method| [SVG](oo-index-architecture-bridge.svg) · [PNG](oo-index-architecture-bridge.png) |
| [oo-index-concept-map.puml](oo-index-concept-map.puml) | Reference / design method| [SVG](oo-index-concept-map.svg) · [PNG](oo-index-concept-map.png) |
| [oo-index-design-lifecycle.puml](oo-index-design-lifecycle.puml) | Reference / design method| [SVG](oo-index-design-lifecycle.svg) · [PNG](oo-index-design-lifecycle.png) |
| [oo-index-prerequisites.puml](oo-index-prerequisites.puml) | Reference / design method| [SVG](oo-index-prerequisites.svg) · [PNG](oo-index-prerequisites.png) |
| [oo-index-reading-path.puml](oo-index-reading-path.puml) | Reference / design method| [SVG](oo-index-reading-path.svg) · [PNG](oo-index-reading-path.png) |
| [oo-index-topic-mindmap.puml](oo-index-topic-mindmap.puml) | Reference / design method| [SVG](oo-index-topic-mindmap.svg) · [PNG](oo-index-topic-mindmap.png) |
| [oo-packages.puml](oo-packages.puml) | Reference / design method| [SVG](oo-packages.svg) · [PNG](oo-packages.png) |
| [oo-publication-sequence.puml](oo-publication-sequence.puml) | Reference / design method| [SVG](oo-publication-sequence.svg) · [PNG](oo-publication-sequence.png) |
| [oo-realization.puml](oo-realization.puml) | Reference / design method| [SVG](oo-realization.svg) · [PNG](oo-realization.png) |
| [oo-responsibility-direction.dot](oo-responsibility-direction.dot) | Reference / design method| [SVG](oo-responsibility-direction.svg) · [PNG](oo-responsibility-direction.png) |
| [oo-runtime-objects.puml](oo-runtime-objects.puml) | Reference / design method| [SVG](oo-runtime-objects.svg) · [PNG](oo-runtime-objects.png) |
| [oo-strategy-preview.puml](oo-strategy-preview.puml) | Reference / design method| [SVG](oo-strategy-preview.svg) · [PNG](oo-strategy-preview.png) |
| [pattern-selection-route.dot](pattern-selection-route.dot) | Reference / design method| [SVG](pattern-selection-route.svg) · [PNG](pattern-selection-route.png) |
| [publication-use-case-classes.puml](publication-use-case-classes.puml) | Reference / design method| [SVG](publication-use-case-classes.svg) · [PNG](publication-use-case-classes.png) |

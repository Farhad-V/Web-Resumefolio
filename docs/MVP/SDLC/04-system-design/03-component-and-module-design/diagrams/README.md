# Resumefolio — Component and Module Design Diagrams

Proposed technical ownership/dependency views; not implemented module enforcement.

Current MVP scope and selected mechanisms: [Baseline](../../../../baseline/README.md). Deferred provider, advanced collaboration and workflow-execution designs are not MVP prerequisites.

## Modularity dependencies and encapsulation

- [Public and private module boundary](module-public-and-private-boundary.svg) · [DOT](module-public-and-private-boundary.dot) · [PNG](module-public-and-private-boundary.png)
- [Dependency and adapter direction](module-dependency-direction.svg) · [DOT](module-dependency-direction.dot) · [PNG](module-dependency-direction.png)
- [Composition and operation lifetimes](module-composition-and-lifetimes.svg) · [DOT](module-composition-and-lifetimes.dot) · [PNG](module-composition-and-lifetimes.png)

[Owning module guide](../01-modularity-dependencies-and-encapsulation.md) · [Component index](../README.md). Diagrams show relationships rather than execution order.

## Implementation view and artifacts

- [Proposed source responsibility layout](implementation-source-structure.svg) · [DOT](implementation-source-structure.dot) · [PNG](implementation-source-structure.png)
- [Component artifact and placement mapping](component-artifact-placement.svg) · [DOT](component-artifact-placement.dot) · [PNG](component-artifact-placement.png)
- [Build and release evidence route](implementation-release-route.svg) · [DOT](implementation-release-route.dot) · [PNG](implementation-release-route.png)

[Owning implementation view](../02-implementation-view-and-artifacts.md). Proposed organization and evidence route, not existing built software.

## Essential modularity and encapsulation views

- [Owner packages and source dependency direction](modularity-essential-packages.svg) · [PlantUML](modularity-essential-packages.puml) · [PNG](modularity-essential-packages.png)
- [Allowed layers and forbidden bypasses](modularity-essential-layers.svg) · [PlantUML](modularity-essential-layers.puml) · [PNG](modularity-essential-layers.png)
- [Public contract and hidden implementation](modularity-essential-encapsulation.svg) · [PlantUML](modularity-essential-encapsulation.puml) · [PNG](modularity-essential-encapsulation.png)
- [Tangled versus owner-controlled dependencies](modularity-essential-before-after.svg) · [PlantUML](modularity-essential-before-after.puml) · [PNG](modularity-essential-before-after.png)

[Owning modularity guide and four boundary/dependency/fitness tables](../01-modularity-dependencies-and-encapsulation.md#8-essential-modularity-and-encapsulation-views). Intended edges/counterexamples are not measured imports or actual hotspot findings.

## Essential implementation and artifact views

- [Implementation view: logical owners to physical outputs](implementation-essential-overview.svg) · [PlantUML](implementation-essential-overview.puml) · [PNG](implementation-essential-overview.png)
- [UML-style artifacts and manifestation boundaries](implementation-essential-overview.svg) · [PlantUML](implementation-essential-overview.puml) · [PNG](implementation-essential-overview.png)
- [Build dependency order and candidate evidence](implementation-essential-build-order.svg) · [PlantUML](implementation-essential-build-order.puml) · [PNG](implementation-essential-build-order.png)

[Owning implementation view](../02-implementation-view-and-artifacts.md#8-essential-implementation-and-artifact-views). Three complementary views only; existing source/artifact/deployment diagrams reused.

## November 4 release applicability

Current MVP figures replace the former common-product boundary. Future and historical figures retain their details without committing them to MVP.

| Editable source | Current applicability |
| --- | --- |
| [component-artifact-placement.dot](component-artifact-placement.dot) | MVP systems|
| [module-dependency-direction.dot](module-dependency-direction.dot) | Method / document navigation|

## Complete diagram alignment — November 4

[Full project inventory and verification limits](../../01-software-architecture/diagrams/README.md). This current disposition supersedes earlier partial diagram-allocation lists.

| Editable source or visual | Current applicability | Matching exports |
| --- | --- | --- |
| [component-artifact-placement.dot](component-artifact-placement.dot) | MVP systems| [SVG](component-artifact-placement.svg) · [PNG](component-artifact-placement.png) |
| [implementation-essential-artifacts.puml](implementation-essential-overview.puml) | MVP systems| [SVG](implementation-essential-overview.svg) · [PNG](implementation-essential-overview.png) |
| [implementation-essential-build-order.puml](implementation-essential-build-order.puml) | MVP core / cross-cutting| [SVG](implementation-essential-build-order.svg) · [PNG](implementation-essential-build-order.png) |
| [implementation-essential-overview.puml](implementation-essential-overview.puml) | MVP systems| [SVG](implementation-essential-overview.svg) · [PNG](implementation-essential-overview.png) |
| [implementation-release-route.dot](implementation-release-route.dot) | MVP core / cross-cutting| [SVG](implementation-release-route.svg) · [PNG](implementation-release-route.png) |
| [implementation-source-structure.dot](implementation-source-structure.dot) | MVP core / cross-cutting| [SVG](implementation-source-structure.svg) · [PNG](implementation-source-structure.png) |
| [modularity-essential-before-after.puml](modularity-essential-before-after.puml) | Reference / design method| [SVG](modularity-essential-before-after.svg) · [PNG](modularity-essential-before-after.png) |
| [modularity-essential-encapsulation.puml](modularity-essential-encapsulation.puml) | MVP core / cross-cutting| [SVG](modularity-essential-encapsulation.svg) · [PNG](modularity-essential-encapsulation.png) |
| [modularity-essential-layers.puml](modularity-essential-layers.puml) | MVP core / cross-cutting| [SVG](modularity-essential-layers.svg) · [PNG](modularity-essential-layers.png) |
| [modularity-essential-packages.puml](modularity-essential-packages.puml) | MVP core / cross-cutting| [SVG](modularity-essential-packages.svg) · [PNG](modularity-essential-packages.png) |
| [module-composition-and-lifetimes.dot](module-composition-and-lifetimes.dot) | MVP core / cross-cutting| [SVG](module-composition-and-lifetimes.svg) · [PNG](module-composition-and-lifetimes.png) |
| [module-dependency-direction.dot](module-dependency-direction.dot) | Method / document navigation| [SVG](module-dependency-direction.svg) · [PNG](module-dependency-direction.png) |
| [module-public-and-private-boundary.dot](module-public-and-private-boundary.dot) | MVP core / cross-cutting| [SVG](module-public-and-private-boundary.svg) · [PNG](module-public-and-private-boundary.png) |

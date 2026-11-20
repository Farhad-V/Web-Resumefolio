# Software Design Document (SDD)

This document defines how the Resumefolio MVP will be built. The [SRS](02-Requirements-engineering/01-Software-requirements-specification.md) owns required behavior, the [analysis document](03-System-analysis/System-analysis.md) explains domain meaning, and the [requirements traceability matrix](02-Requirements-engineering/03-Requirements-traceability-matrix.md) connects requirements with their design records and verification. The three design sections follow the SDLC Complete Engineering Guide.

- [High-Level Design](#high-level-design)
- [UI/UX Design](#ui-ux-design)
- [Low-Level Design](#low-level-design)

<a id="high-level-design"></a>

## High-Level Design (HLD)

Architecture, system boundaries, technology, deployment, security and operating decisions. [Open High-Level Design (HLD)](04-System-design/01-High-level-design/High-level-design.md).

<a id="ui-ux-design"></a>

## UI/UX Design

User journeys, screen states, interaction behavior and accessibility. [Open UI/UX Design](04-System-design/02-Ui-ux-design/Ui-ux-design.md).

<a id="low-level-design"></a>

## Low-Level Design (LLD)

Component behavior, data models, API contracts and failure handling. [Open Low-Level Design (LLD)](04-System-design/03-Low-level-design/Low-level-design.md).

## Implementation design references

- [MVP wireframes](04-System-design/02-Ui-ux-design/Ui-ux-design.md#mvp-wireframes)
- [MVP physical schema design](04-System-design/03-Low-level-design/Low-level-design.md#mvp-physical-schema-design)
- [MVP API contracts](04-System-design/03-Low-level-design/Low-level-design.md#mvp-api-contracts)
- [Criterion-level design and test trace](02-Requirements-engineering/03-Requirements-traceability-matrix.md#criterion-level-design-and-test-trace)

## Design review and implementation handoff

Set shared boundaries and consequential choices early. During [Development](Sdlc-guide.md#stage-5-agile-iterative-development), refine only the design needed for the selected capability, update the relevant design records and diagrams, and use the traceability matrix to link the affected requirement and acceptance criterion. Record consequential changes in an architecture decision record.

Use the [design scope](04-System-design/01-High-level-design/High-level-design.md#design-record-design-scope-and-approach-md), [reference and coverage map](04-System-design/01-High-level-design/High-level-design.md#design-record-design-references-and-coverage-md) and [review and handoff](04-System-design/01-High-level-design/High-level-design.md#design-record-06-design-quality-and-security-analysis-05-design-review-traceability-and-handoff-md) to track unresolved choices and evidence. Record verified code, tests and release readiness in their respective stages.

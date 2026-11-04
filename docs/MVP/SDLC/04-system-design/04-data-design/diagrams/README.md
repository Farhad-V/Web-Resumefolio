# Data Design — Diagram Catalog

Keep editable sources and SVG/PNG exports synchronized. These are proposed technical views, not final physical schemas.

## MVP system allocation and design status

MVP data ownership follows distinct core and ProjectForge systems; do not infer a common database or cross-system ACID transaction. Core retains private library metadata, protected artifacts, selected resume media, application status/next action/follow-up and immutable submitted manifests. ProjectForge owns basic repositories/issues/Kanban; its database is undecided. Mail/account/provider, advanced Sprint/review/release and runner tables below are future models. My Files & Media is a core private library with optional per-resume selection. Supported uploads remain in private directories on the same Resumefolio server, with type/size/quota enforcement, safe serving and backup/recovery. Direct, preview and byte-range requests use current owner or selected-resume/viewer authority. Upload does not publish. External YouTube links use simple embedded playback; private uploads are not sent to YouTube. No extra media platform or heavyweight editor/transcoding is selected.

Authority: [OWNER-MVP-2026-11-04](../../../01-project-planning/owner-mvp-decision-2026-11-04.md).

## Logical and physical data-model refinement

- [Logical revisions and protected references](data-logical-revisions-and-references.svg) · [PlantUML](data-logical-revisions-and-references.puml) · [PNG](data-logical-revisions-and-references.png)
- [Invariant enforcement and physical mapping](data-physical-enforcement-map.svg) · [PlantUML](data-physical-enforcement-map.puml) · [PNG](data-physical-enforcement-map.png)

[Owning document](../01-analysis-to-logical-and-physical-data-models.md). Candidate logical relationships and physical enforcement allocation. Final types, constraints, engine, policy-dependent cardinalities and coordination mechanisms remain gated.

## Persistence, caching and lifecycle

- [Current eligibility before private cache delivery](persistence-protected-cache-flow.svg) · [PlantUML](persistence-protected-cache-flow.puml) · [PNG](persistence-protected-cache-flow.png)
- [Artifact protection and physical reclamation](persistence-artifact-lifecycle.svg) · [PlantUML](persistence-artifact-lifecycle.puml) · [PNG](persistence-artifact-lifecycle.png)

[Owning document](../03-persistence-caching-and-data-lifecycle.md). Proposed persistence and lifecycle protocols. Actual storage/cache facilities, freshness/guard mechanisms, retention and recovery evidence remain pending.

## Essential conceptual, logical and physical model views

- [Conceptual identities: no attributes or physical choices](data-essential-conceptual.svg) · [PlantUML](data-essential-conceptual.puml) · [PNG](data-essential-conceptual.png)
- [Logical ERD: exact publication and live selection](data-essential-logical.svg) · [PlantUML](data-essential-logical.puml) · [PNG](data-essential-logical.png)
- [Physical schema illustration: types, scoped keys and indexes](data-essential-physical.svg) · [PlantUML](data-essential-physical.puml) · [PNG](data-essential-physical.png)
- [Conceptual to logical to physical refinement](data-essential-levels.svg) · [PlantUML](data-essential-levels.puml) · [PNG](data-essential-levels.png)
- [Normalization walkthrough with explicit example dependencies](data-essential-normalization.svg) · [PlantUML](data-essential-normalization.puml) · [PNG](data-essential-normalization.png)

[Owning data model document](../01-analysis-to-logical-and-physical-data-models.md#essential-data-model-diagrams). Selected examples and normalization dependencies are illustrative, not accepted schema or migrations.

## Essential persistence, cache and recovery views

- [Persistence responsibilities and authoritative stores](persistence-essential-architecture.svg) · [PlantUML](persistence-essential-architecture.puml) · [PNG](persistence-essential-architecture.png)
- [Guarded write and post-commit cache coherence](persistence-essential-write.svg) · [PlantUML](persistence-essential-write.puml) · [PNG](persistence-essential-write.png)
- [Authorized cache-aside read: hit, miss and outage](persistence-essential-read.svg) · [PlantUML](persistence-essential-read.puml) · [PNG](persistence-essential-read.png)
- [Versioned invalidation and concurrent-fill safety](persistence-essential-invalidation.svg) · [PlantUML](persistence-essential-invalidation.puml) · [PNG](persistence-essential-invalidation.png)
- [Logical retirement, policy assessment and physical deletion](persistence-essential-deletion.svg) · [PlantUML](persistence-essential-deletion.puml) · [PNG](persistence-essential-deletion.png)
- [Consistent backup set and isolated usable restore](persistence-essential-recovery.svg) · [PlantUML](persistence-essential-recovery.puml) · [PNG](persistence-essential-recovery.png)

[Owning persistence document](../03-persistence-caching-and-data-lifecycle.md#7-essential-persistence-cache-and-recovery-views). Existing cache/lifecycle views reused; no replica/cache/backend/backup facility selected.

## Complete diagram alignment — November 4

[Full project inventory and verification limits](../../../diagram-alignment-review-2026-11-04.md). This current disposition supersedes earlier partial diagram-allocation lists.

| Editable source or visual | Current applicability | Matching exports |
| --- | --- | --- |
| [data-essential-conceptual.puml](data-essential-conceptual.puml) | MVP core / cross-cutting| [SVG](data-essential-conceptual.svg) · [PNG](data-essential-conceptual.png) |
| [data-essential-levels.puml](data-essential-levels.puml) | MVP core / cross-cutting| [SVG](data-essential-levels.svg) · [PNG](data-essential-levels.png) |
| [data-essential-logical.puml](data-essential-logical.puml) | MVP core / cross-cutting| [SVG](data-essential-logical.svg) · [PNG](data-essential-logical.png) |
| [data-essential-normalization.puml](data-essential-normalization.puml) | Reference / design method| [SVG](data-essential-normalization.svg) · [PNG](data-essential-normalization.png) |
| [data-essential-physical.puml](data-essential-physical.puml) | MVP core / cross-cutting| [SVG](data-essential-physical.svg) · [PNG](data-essential-physical.png) |
| [data-logical-revisions-and-references.puml](data-logical-revisions-and-references.puml) | MVP core / cross-cutting| [SVG](data-logical-revisions-and-references.svg) · [PNG](data-logical-revisions-and-references.png) |
| [data-physical-enforcement-map.puml](data-physical-enforcement-map.puml) | MVP core / cross-cutting| [SVG](data-physical-enforcement-map.svg) · [PNG](data-physical-enforcement-map.png) |
| [persistence-artifact-lifecycle.puml](persistence-artifact-lifecycle.puml) | MVP core / cross-cutting| [SVG](persistence-artifact-lifecycle.svg) · [PNG](persistence-artifact-lifecycle.png) |
| [persistence-essential-architecture.puml](persistence-essential-architecture.puml) | Mixed MVP / future| [SVG](persistence-essential-architecture.svg) · [PNG](persistence-essential-architecture.png) |
| [persistence-essential-deletion.puml](persistence-essential-deletion.puml) | MVP core / cross-cutting| [SVG](persistence-essential-deletion.svg) · [PNG](persistence-essential-deletion.png) |
| [persistence-essential-invalidation.puml](persistence-essential-invalidation.puml) | MVP core / cross-cutting| [SVG](persistence-essential-invalidation.svg) · [PNG](persistence-essential-invalidation.png) |
| [persistence-essential-read.puml](persistence-essential-read.puml) | MVP core / cross-cutting| [SVG](persistence-essential-read.svg) · [PNG](persistence-essential-read.png) |
| [persistence-essential-recovery.puml](persistence-essential-recovery.puml) | MVP core / cross-cutting| [SVG](persistence-essential-recovery.svg) · [PNG](persistence-essential-recovery.png) |
| [persistence-essential-write.puml](persistence-essential-write.puml) | MVP core / cross-cutting| [SVG](persistence-essential-write.svg) · [PNG](persistence-essential-write.png) |
| [persistence-protected-cache-flow.puml](persistence-protected-cache-flow.puml) | MVP core / cross-cutting| [SVG](persistence-protected-cache-flow.svg) · [PNG](persistence-protected-cache-flow.png) |

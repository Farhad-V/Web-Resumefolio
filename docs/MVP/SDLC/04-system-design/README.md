# System Design

Use this SDD to understand the selected design and its owning component, data, API and security records. The [Baseline](../../baseline/README.md) identifies the applicable choices; its runtime gates remain unexecuted.

## Reading route

| Topic | Purpose |
| --- | --- |
| [Architecture](01-software-architecture/README.md) | Core / separate ProjectForge boundaries, runtime and deployment |
| [Detailed and OO Design](02-detailed-and-object-oriented-design/README.md) | Responsibilities, dependencies, patterns and evolution |
| [Components](03-component-and-module-design/README.md) | Project-specific operation, data and failure behavior |
| [Data Design](04-data-design/README.md) | Revisions, persistence, transactions, history and lifecycle |
| [Interface and API Design](05-interface-and-api-design/README.md) | User-scoped contracts, authorization and failure semantics |
| [Quality and Security](06-design-quality-and-security-analysis/README.md) | Threats, accessibility, capacity, backup and restore |
| [Architecture Decisions](07-design-decisions/README.md) | Selected decisions, alternatives and consequences |

Start with the [architecture decomposition](01-software-architecture/02-system-decomposition-and-boundaries.md), then read the affected component and shared data/API/security rules. [Purpose](00-design-purpose-scope-and-approach.md), [source coverage](01-reference-and-coverage-map.md) and [review/handoff](06-design-quality-and-security-analysis/05-design-review-traceability-and-handoff.md) provide supporting context.

## Current boundaries

Core owns invited identity, dashboard, profile/resumes, private media, PDFs/sharing and manual applications. ProjectForge is a separate Laravel/native Git system with its own MySQL database, OS/storage boundaries and current user-scoped authorization. Both initially share the existing host's failure domain. The [dark architecture overview](../../baseline/diagrams/selected-architecture.svg) shows the selected topology.

Mail/calendar and user workflow execution are future component designs. Work management and Git collaboration records contain explicit MVP slices; advanced Sprints/review/releases are deferred. Required access isolation, publication/history consistency and operational recovery remain in scope. A design description is not evidence of working code or a passing test.

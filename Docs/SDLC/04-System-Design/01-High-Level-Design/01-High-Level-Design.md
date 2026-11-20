# High-Level Design (HLD)

Part of the [Software Design Document](../../01-Project-Planning/02-Project-Management-Plan.md#stage-4-system-design).

| Design concern | Resumefolio design |
| --- | --- |
| Architecture and ownership | Core owns invited identity, professional presentation, private files and application tracking. ProjectForge owns repositories, Git operations, issues and basic Kanban. A scoped API connects the systems. See [architecture and system boundaries](14-Appendices.md#design-record-01-software-architecture-software-architecture-md). |
| Technology | Separate Laravel applications use React and Inertia for interactive pages; Core keeps Blade for trusted PDF templates. ProjectForge uses native Git. See the [frontend decision](../ADR/ADR-007-React-Inertia-Frontend.md#design-record-07-design-decisions-adr-007-react-inertia-frontend-md) and [selected implementation decisions](../ADR/ADR-006-Selected-Mvp-Implementation-Baseline.md#design-record-07-design-decisions-adr-006-selected-mvp-implementation-baseline-md). |
| Deployment | The applications have separate database credentials, sessions, keys and private storage boundaries. Initial placement on a shared host carries a shared failure domain. See the [deployment topology](14-Appendices.md#design-record-01-software-architecture-04-deployment-topology-nodes-and-networks-md). |
| Security and operations | Enforce current actor and resource authorization at each entry point, including direct media retrieval and Git operations. Design for protected backups and an isolated restore. See [security and trust boundaries](14-Appendices.md#design-record-06-design-quality-and-security-analysis-02-security-threat-modeling-and-trust-boundaries-md), [recovery](14-Appendices.md#design-record-06-design-quality-and-security-analysis-03-operations-backup-recovery-and-resilience-md), and [quality trade-offs](14-Appendices.md#design-record-06-design-quality-and-security-analysis-01-quality-attributes-and-design-trade-offs-md). |

The [architecture decisions](../ADR/Decision-Index.md#design-record-07-design-decisions-design-decisions-md) record alternatives, rationale and status. Personal mail and calendar, advanced repository collaboration and user workflow execution remain outside the MVP.

## Sections

1. [Introduction](01-Introduction.md)
2. [Architectural Goals & Constraints](02-Architectural-Goals-And-Constraints.md)
3. [System Context](03-System-Context.md)
4. [Architecture Overview](04-Architecture-Overview.md)
5. [Components](05-Components.md)
6. [Data Architecture](06-Data-Architecture.md)
7. [Integration & Interfaces](07-Integration-And-Interfaces.md)
8. [Technology Stack](08-Technology-Stack.md)
9. [Deployment Architecture](09-Deployment-Architecture.md)
10. [Security Architecture](10-Security-Architecture.md)
11. [Non-Functional Strategy](11-Non-Functional-Strategy.md)
12. [Risks & Key Decisions](12-Risks-And-Key-Decisions.md)
13. [Traceability](13-Traceability.md)
14. [Appendices](14-Appendices.md)

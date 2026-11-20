# Resumefolio software development life cycle

The reference for this documentation is *SDLC Complete Engineering Guide EN*, sections 1, 8–13 and 15. Its **Agile with Upfront Architecture** model guides the seven stages below. Design decisions and acceptance criteria are revisited as implementation and verification produce evidence.

| Stage | Project documentation |
| --- | --- |
| 1. Project Planning / Initiation | [Project charter](01-Project-planning/01-Project-charter.md), [management plan](01-Project-planning/02-Project-management-plan.md) and [feasibility and risks](01-Project-planning/03-Feasibility-and-risk-assessment.md) |
| 2. Requirements Engineering | [SRS](02-Requirements-engineering/01-Software-requirements-specification.md), [product backlog](02-Requirements-engineering/02-Product-backlog.md) and [traceability matrix](02-Requirements-engineering/03-Requirements-traceability-matrix.md) |
| 3. System Analysis | [System analysis](03-System-analysis/System-analysis.md) |
| 4. System Design | [Software Design Document](System-design-guide.md) |
| 5. Agile Iterative Development | [Agile Iterative Development](#stage-5-agile-iterative-development) and [test plan and results](05-Agile-iterative-development/05-Testing.md) |
| 6. Deployment / Release | [Release preparation and evidence](06-Deployment-release/Deployment-release.md) |
| 7. Maintenance & Evolution | [Operations and maintenance](07-Maintenance-evolution/Maintenance-evolution.md) |

## Stage 5: Agile Iterative Development

Begin with [Project Setup](05-Agile-iterative-development/00-Project-setup.md). Section 6 of the PDF guides each development cycle. Refinement continues as new information arrives, and testing runs throughout the cycle.

1. [Sprint Planning](05-Agile-iterative-development/01-Sprint-planning.md)
2. [Backlog Refinement](05-Agile-iterative-development/02-Backlog-refinement.md)
3. [Detailed Analysis & Design](05-Agile-iterative-development/03-Detailed-analysis-and-design.md)
4. [Implementation](05-Agile-iterative-development/04-Implementation.md)
5. [Testing](05-Agile-iterative-development/05-Testing.md)
6. [Sprint Review](05-Agile-iterative-development/06-Sprint-review.md)
7. [Sprint Retrospective](05-Agile-iterative-development/07-Sprint-retrospective.md)

Run the ProjectForge identity and Git security checks before dependent Git integration.

## Documentation deliverables

The guide identifies 15 deliverable types. These links point to the owning documents and their supporting records.

| Deliverable | Project source |
| --- | --- |
| 1. Project Charter | [Project charter](01-Project-planning/01-Project-charter.md) |
| 2. Project Management Plan | [Project management plan](01-Project-planning/02-Project-management-plan.md) |
| 3. Feasibility & Risk Assessment | [Feasibility and risk assessment](01-Project-planning/03-Feasibility-and-risk-assessment.md) |
| 4. Software Requirements Specification | [SRS](02-Requirements-engineering/01-Software-requirements-specification.md) |
| 5. Product Backlog | [Product backlog](02-Requirements-engineering/02-Product-backlog.md) |
| 6. Requirements Traceability Matrix | [Requirements traceability matrix](02-Requirements-engineering/03-Requirements-traceability-matrix.md) |
| 7. System Analysis Document | [Actors, scenarios, models and rules](03-System-analysis/System-analysis.md) |
| 8. Software Architecture Document | [Architecture](04-System-design/01-High-level-design/High-level-design.md#design-record-01-software-architecture-software-architecture-md) and [architecture decisions](04-System-design/01-High-level-design/High-level-design.md#design-record-07-design-decisions-design-decisions-md) |
| 9. UI/UX Design Specification | [Interaction and accessibility design](04-System-design/02-Ui-ux-design/Ui-ux-design.md). Record screen-level details with the relevant implementation package. |
| 10. Database Design Document | [Data design](04-System-design/03-Low-level-design/Low-level-design.md#design-record-04-data-design-data-design-md) |
| 11. Low-Level Design | [Detailed design](04-System-design/03-Low-level-design/Low-level-design.md#design-record-02-detailed-and-object-oriented-design-detailed-and-object-oriented-design-md) and [component design](04-System-design/03-Low-level-design/Low-level-design.md#design-record-03-component-and-module-design-component-and-module-design-md) |
| 12. API Specification | [Interface and API design](04-System-design/03-Low-level-design/Low-level-design.md#design-record-05-interface-and-api-design-interface-and-api-design-md). Verify contracts against the implemented interfaces during development. |
| 13. Test Strategy & Test Plan | [Test plan](05-Agile-iterative-development/05-Testing.md) and [verification gates](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/implementation-sequence.md) |
| 14. Test Cases & Test Reports | [Acceptance criteria](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/criterion-dispositions.md) and [test evidence record](05-Agile-iterative-development/05-Testing.md). Execution is pending. |
| 15. Deployment & Operations Documentation | [Release preparation](06-Deployment-release/Deployment-release.md) and [maintenance](07-Maintenance-evolution/Maintenance-evolution.md) |

The selected MVP baseline and design are documented. Begin stage 5 with [isolated project setup](05-Agile-iterative-development/00-Project-setup.md). As work lands, connect requirements and acceptance criteria to analysis and design, the implementation revision, test results and the release record.

# Diagram notation alignment review — November 1, 2026

Scope: files 00–15 and README, compared with the requested notation mapping. Existing valid models were retained; missing views were added. This is documentary alignment, not architecture acceptance, product testing or measured user research.

| File | Diagram family | Interpretation |
| --- | --- | --- |
| [00-start-here.md](../01-foundations-and-system-context/00-start-here.md) | Navigation graph | See the document's Diagram Types and Reading Guide; file 04 has its own notation/level rules. |
| [01-analysis-purpose-scope-and-approach.md](../01-foundations-and-system-context/01-analysis-purpose-scope-and-approach.md) | Stakeholder/scope map | See the document's Diagram Types and Reading Guide; file 04 has its own notation/level rules. |
| [02-system-context-and-boundaries.md](../01-foundations-and-system-context/02-system-context-and-boundaries.md) | C4 Level 1; evidence-bounded C4 Level 2 | See the document's Diagram Types and Reading Guide; file 04 has its own notation/level rules. |
| [03-domain-model-and-object-oriented-view.md](../02-domain-and-information-analysis/03-domain-model-and-object-oriented-view.md) | UML class and package | See the document's Diagram Types and Reading Guide; file 04 has its own notation/level rules. |
| [04-function-oriented-view.md](../03-functional-and-process-analysis/04-function-oriented-view.md) | Functional tree; DFD context/Level 1/selected Level 2 | See the document's Diagram Types and Reading Guide; file 04 has its own notation/level rules. |
| [05-data-oriented-view.md](../02-domain-and-information-analysis/05-data-oriented-view.md) | Conceptual ERD | See the document's Diagram Types and Reading Guide; file 04 has its own notation/level rules. |
| [06-scenario-based-view.md](../04-behavioral-and-scenario-analysis/06-scenario-based-view.md) | UML use case and sequence | See the document's Diagram Types and Reading Guide; file 04 has its own notation/level rules. |
| [07-state-based-view.md](../04-behavioral-and-scenario-analysis/07-state-based-view.md) | UML state machine | See the document's Diagram Types and Reading Guide; file 04 has its own notation/level rules. |
| [08-control-flow-based-view.md](../03-functional-and-process-analysis/08-control-flow-based-view.md) | UML activity | See the document's Diagram Types and Reading Guide; file 04 has its own notation/level rules. |
| [09-rule-based-view.md](../05-business-rules-and-operation-contracts/09-rule-based-view.md) | Decision tables and decision trees | See the document's Diagram Types and Reading Guide; file 04 has its own notation/level rules. |
| [10-domain-constraints-and-operation-contracts.md](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md) | Contract boundary graphs and UML object snapshots | See the document's Diagram Types and Reading Guide; file 04 has its own notation/level rules. |
| [11-model-consistency-traceability-and-review.md](../07-review-and-design-handoff/11-model-consistency-traceability-and-review.md) | RTM / matrix graphic | See the document's Diagram Types and Reading Guide; file 04 has its own notation/level rules. |
| [12-interfaces-and-external-interactions.md](../06-interfaces-security-and-quality-analysis/12-interfaces-and-external-interactions.md) | UML interface component and request/response sequence | See the document's Diagram Types and Reading Guide; file 04 has its own notation/level rules. |
| [13-security-quality-and-operational-analysis.md](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md) | Trust-boundary DFD and UML deployment | See the document's Diagram Types and Reading Guide; file 04 has its own notation/level rules. |
| [14-feasibility-dependencies-and-design-handoff.md](../07-review-and-design-handoff/14-feasibility-dependencies-and-design-handoff.md) | Dependency network | See the document's Diagram Types and Reading Guide; file 04 has its own notation/level rules. |
| [15-current-processes-and-bottleneck-analysis.md](../03-functional-and-process-analysis/15-current-processes-and-bottleneck-analysis.md) | BPMN As-Is boundary and To-Be swimlanes | See the document's Diagram Types and Reading Guide; file 04 has its own notation/level rules. |
| [README.md](../README.md) | High-level ecosystem banner | See the document's Diagram Types and Reading Guide; file 04 has its own notation/level rules. |

## Important boundaries

- C4 Level 1 models target scope. Level 2 records a partial historical demo inventory; final target containers and technology choices remain design work.

- ER models are conceptual; no physical schema or database choice is falsely accepted.

- HTTP/gRPC details remain unselected; request/response diagrams specify logical contracts.

- Trust boundaries are obligations; the deployment diagram is historical inventory, not proof of configured firewall/HA/DR.

- Dependency graphs are not promised dates or accepted schedules.

- BPMN As-Is is an explicit black-box evidence boundary; target swimlanes do not fabricate current practice or measured bottlenecks.

- Existing matrices remain historical. Source associations and render checks are not complete criterion coverage or test-case execution.

## Verification record

See [machine-readable review](notation-alignment-review-2026-11-01.json) for source hashes, flow catalog, diagram inventory and performed artifact checks. Earlier handoff/review fingerprints remain historical; this file does not silently reissue their acceptance.

## Notation references

- [C4 container diagram](https://c4model.com/diagrams/container): application/data-store architecture; deployment is separate.

- [PlantUML activities](https://plantuml.com/activity-diagram-beta): workflow notation, distinct from BPMN.

- [OMG BPMN 2.0.2](https://www.omg.org/spec/BPMN/2.0.2/About-BPMN): native BPMN model/diagram interchange basis.

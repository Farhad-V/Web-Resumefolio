# Four-Document Review — Diagram Meaning and Readability

Date: November 1, 2026. Scope: System Analysis documents 00–03 and their referenced figures. This is a documentation/model review, not product testing or baseline acceptance.

| Finding | Correction | Limit |
|---|---|---|
| Wide Graphviz concept cards combined property and action detail, making associations difficult to scan | Replace with focused PlantUML class views; keep action descriptions in authoritative tables; split presentation/evidence and application/provider views | Exact non-established multiplicities still require policy review |
| Similar arrows were used for document influence, control flow, conceptual links and authority | Use activity notation for workflows, class associations for domain structure and separately explained context/dependency conventions | Logical relationships do not select protocols or physical architecture |
| Profile workflow could imply that every edit automatically starts preview/apply | Add an explicit owner choice to review; keep selected apply and publication as separate decisions | Denied/failed/conflicting outcomes still need their detailed contracts |
| Full-product context had compressed request/response wording on ambiguous lines | Use actor/context associations and retain explicit directional information in the interface table | Lines are not grants or verified integrations |
| Start Here still described document 03 as a partial textual model | Update current state to populated domain model and identify data/behavior reconciliation as next work | Population is not complete cross-view acceptance |
| All domain relationship counts were omitted, including the established Sprint Backlog meaning | Show Sprint–Sprint Backlog 1:1; explain omitted bounds and retain their proposal status | Do not manufacture counts for other relations |
| Some class drawings mixed independent application preparation with provider access | Separate actual-history and provider-communication figures while preserving concept IDs and explicit application associations | Linking does not transfer authority or imply external submission |

## Preserved Meaning

The owner-accepted profile rule is unchanged: no automatic resume/live update; preview and explicitly selected application; separate publication confirmation; preservation of independent content and actual submitted material. The 53 local concept IDs and primary requirement text/IDs remain intact. Detailed proposals are not promoted to acceptance. Actual OAuth, isolation, backup and recovery gates remain in force.

## Verification

Validation checks: PlantUML renders without syntax-error pages; diagram/Markdown links resolve; local concept IDs match the tables; all original concepts are represented; accepted source decisions are unchanged; source hashes prevent unnoticed concurrent edits; saved outputs are byte-checked. Visual inspection checks labels, crossings, cropping and layout. Counts and final results are recorded in the companion JSON after validation.

[Diagram catalog](../diagrams/README.md) · [System Analysis index](../README.md)

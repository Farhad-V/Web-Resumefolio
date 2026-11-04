# Change and Baseline

The [current Baseline](../../../baseline/README.md) identifies the selected documentary revision and its exact files. It is the implementation input, not evidence that the application or its Release gates have passed.

## Documents

| Read | For |
| --- | --- |
| [Questions and decisions](open-questions-and-decisions.md) | Q-D01–28 current dispositions and settled owner policy |
| [Selected answers](../../../baseline/policy-decisions.md) | Concrete policies and MVP/future boundaries |
| [Change control](change-control.md) | Impact, authority, decision, changed records and recheck |
| [Review criteria](requirements-review-and-baseline-criteria.md) | Conditions and evidence for requirement review |
| [Answer review](requirements-answer-review.md) | Source/scenario/finding review route |
| [Implementation gates](../../../baseline/implementation-sequence.md) | Remaining environment, security, operational, actor and Release evidence |

## Authority and maintenance

Requirements, decisions, review findings and actual test results are distinct records. A later material change identifies the affected scope/criteria/design, alternatives, compatibility/recovery impact, authority and new revision. Update the current manifest after review; the previous snapshot remains available in Git history. No silence, diagram count or file creation is treated as acceptance of unimplemented behavior.

Keep established planning acceptance and actual source evidence intact. Do not reopen already selected technical/policy choices as generic missing decisions, and do not close outstanding runtime/actor/restore checks merely because their Design exists.

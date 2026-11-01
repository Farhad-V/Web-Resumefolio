# Resumefolio — Confirmed Capacity and Preliminary Sizing

Date: November 1, 2026. Owner: Farhad Valizadegan. Status: actual capacity input plus low-confidence engineering estimate; not a committed schedule, accepted baseline or completed design.

## 1. Confirmed Capacity and Authority

The owner answered **20 hours per week**, explicitly including learning, documentation and testing. Use 20 total project hours, not 20 coding hours plus uncounted supporting work. This supersedes the unspecified “full time” assumption for current working forecasts; historical accepted planning snapshots/decisions are preserved unchanged. This observation does not promise that every future week is uninterrupted.

## 2. Preliminary Work-Package Estimate

These are Codex's order-of-magnitude engineering estimates of remaining work, derived from the local 29-item backlog and current incomplete analysis/design. They are judgments, not measured productivity, quotes, owner-approved estimates or GitHub live status. Component ranges include development, local component checks and documentation; the integrated row addresses cross-module verification. A separate 25% planning allowance below covers learning/rework uncertainty without representing additional availability. Results depend strongly on component reuse, owner decisions and provider/runner/storage feasibility.

| Remaining work | Existing local work references | Low hours | High hours | Basis |
|---|---|---:|---:|---|
| Requirements refinement and actual owner review | PBI-008 | 12 | 24 | Complete policy/criterion reconciliation and review records |
| System Analysis models | PBI-008/PBI-009 | 20 | 40 | Populate context, domain/data, interactions, states, rules and consistency |
| Design and decisive feasibility | PBI-002–006/PBI-009 | 24 | 48 | Evaluate architecture, dependencies, isolation, storage and recovery options |
| Identity, access and shell | PBI-010/PBI-011 | 24 | 48 | Normal/denied/revoked access and responsive navigation |
| Profiles and tailored resumes | PBI-012 | 40 | 80 | Reusable sources, independent overrides, revision/publication workflow |
| Evidence and quotas | PBI-013 | 16 | 32 | Safe admission, per-resume disclosure, concurrent accounting |
| PDF representations | PBI-014 | 24 | 48 | Generation/upload, language, revision, rendering and failure paths |
| Protected sharing | PBI-015 | 20 | 40 | Scoped links, passwords, direct retrieval and revocation |
| Applications and submitted history | PBI-016 | 32 | 64 | Manual progress, exact materials, correction and retained history |
| Gmail operations | PBI-017 | 32 | 64 | OAuth integration, private read/draft/send, unknown-result reconciliation |
| Calendar and reminders | PBI-018 | 24 | 48 | Time zones, selected sync, conflicts and reconnect |
| Work management and Sprints | PBI-019 | 32 | 64 | Items/tasks/boards, permissions, Sprint state and incomplete outcomes |
| Real Git hosting/transports | PBI-020 | 32 | 64 | Integrate an evaluated engine, grants, client interoperability and resource limits |
| Git collaboration/tracking/releases | PBI-021/PBI-022 | 48 | 96 | Fork/review/merge state, current revisions and release assets |
| Isolated execution and deployment control | PBI-003/PBI-023 | 64 | 128 | Integrate and validate an evaluated runner/control design; feasibility may require revision |
| Administration and lifecycle | PBI-024 | 24 | 48 | Suspension, trash/restore, retention/reference effects and audit |
| Integrated quality/security checks | PBI-025/PBI-026 | 40 | 80 | Cross-module failures, permission regression, capacity and accessibility |
| Recovery, operating guidance and deployment | PBI-006/PBI-027–029 | 32 | 64 | Consistent restore drill, data-compatible recovery, runbooks and live readiness |

Base range: **540–1080 hours**. Explicit 25% planning allowance: **135–270 hours**. Scenario total: **675–1350 hours**, or **33.75–67.5 project weeks at 20 hours/week**. Round outward to approximately **34–68 weeks** for this sizing scenario. This is an uncertainty illustration for the full agreed scope, not a promised finish window or a conclusion that a particular architecture can be built within it. External waits, holidays or failed feasibility can extend elapsed time; successful reuse can change the estimate. Do not add per-row high values and describe the result as a probability/confidence interval.

## 3. Target Conflict and Decisions

The historical requested target November 8, 2026 is one week from the assessment date. One week supplies about 20 stated project hours, far below this preliminary full-scope range. There is no evidence-based basis to promise the complete agreed product by that date. Do not silently narrow scope, skip recovery/isolation evidence or count unbuilt features complete. Retain the historical target and make an explicit owner decision on delivery horizon, scope or resources after design/feasibility refinement.

The next committed work should be a short requirements/modeling iteration with a bounded review outcome, not the old Sprint table treated as an executable forecast. Confirmed capacity alone does not justify an invented completion date.

## 4. Live Tracking Limitation and Re-estimation Gate

Local PBI links 1–29 were inspected. GitHub connector search returned 422 (repository unavailable/not permitted), and direct issue-8 retrieval returned no usable issue data. Thus only the local index was used; live issue state, board fields, assignments and estimates were not verified or changed. No message, issue comment or board update was sent.

Before accepting a forecast: finish initial analysis/design; choose justified components; decompose large packages into criteria-bearing work; confirm provider/storage/runner prerequisites; inspect actual tracking; estimate by dependency and risk; then compare early measured progress with these ranges. Record the owner decision against an identified candidate. Q-D28 has a capacity answer and preliminary sizing now, but its final forecast/baseline gate remains pending.

[Resource authority](05-resources-and-constraints.md) · [Roadmap](08-roadmap-and-milestones.md) · [Local backlog](../../Project-Management/product-backlog.md)


<a id="requirements-specification-yaml-workflows-and-cicd"></a>

<a id="requirements-specification-yaml-workflows-and-cicd--heading-resumefolio--yaml-workflows-and-cicd"></a>
# Resumefolio — YAML Workflows and CI/CD

**Quick read — Deferred: workflow execution.** YAML workflow execution and deployment are after MVP. Keep these proposals separate from the current delivery path.

[3. Proposed Requirements](#requirements-specification-yaml-workflows-and-cicd--heading-3-proposed-requirements) · [6. Open Decisions and Gates](#requirements-specification-yaml-workflows-and-cicd--heading-6-open-decisions-and-gates) · [Selected Policies and Future Proposals](#requirements-specification-yaml-workflows-and-cicd--heading-selected-policies-and-future-proposals)

[Domain index](README.md) · [Acceptance trace](../../03-Requirements-Traceability-Matrix/README.md)


Current implementation choices and scope: [Baseline](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/README.md). Runtime verification remains subject to its gates.

| Item | Current position |
| --- | --- |
| Owner | Farhad; sole delivery and operations owner |
| Status | Deferred after MVP; source proposals retained for future review; see [current record rules](15-Requirement-Priority-And-Readiness.md#current-record-rules) |
| Planning basis | DEC-019/028/018/017; GAP-D09 and resource follow-up |
| Candidate references | YML-D01–YML-D12: retained stable source IDs; criterion scope follows [current record rules](15-Requirement-Priority-And-Readiness.md#current-record-rules) |
| Priority | [current record rules](15-Requirement-Priority-And-Readiness.md#current-record-rules) define Must within MVP slice / Later; file order is not execution order |
| Source record date | October 31, 2026 |

**At a glance:** Provide agreed real workflow execution, not only YAML validation or Git integrity checks. Define supported behavior, untrusted-code isolation, secrets, limits and outputs; deployment authority stays separate. Execution remains conditional on evidence-based feasibility/security gates.

[Basis](#requirements-specification-yaml-workflows-and-cicd--heading-1-purpose-and-accepted-boundary) · [Inventory](#requirements-specification-yaml-workflows-and-cicd--heading-2-capability-and-information-inventory)
· [Requirements](#requirements-specification-yaml-workflows-and-cicd--heading-3-proposed-requirements) · [Models](#requirements-specification-yaml-workflows-and-cicd--heading-4-behavior-and-boundary-models)
· [Scenarios](#requirements-specification-yaml-workflows-and-cicd--heading-5-planned-verification) · [Decisions](#requirements-specification-yaml-workflows-and-cicd--heading-6-open-decisions-and-gates)
· [Review](#requirements-specification-yaml-workflows-and-cicd--heading-7-traceability-and-review-readiness)

<a id="requirements-specification-yaml-workflows-and-cicd--heading-deferred-execution-and-deployment"></a>
## Deferred execution and deployment

All YAML workflow execution, runners and product deployment automation are after MVP. Retain isolation, scoped secrets, approvals, resource limits, durable effects and cleanup/recovery requirements for later planning. None is an MVP implementation commitment or a reason to run untrusted code in the core or ProjectForge MVP. Operating/deploying Resumefolio itself and demonstrating backups/recovery remain MVP obligations.

Authority: [OWNER-MVP-2026-11-04](../../../01-Project-Planning/01-Project-Charter.md#release-decision). [Candidate allocation](10-Mvp-Candidate-Release-Allocation.md#requirements-specification-mvp-release-allocation).

<a id="requirements-specification-yaml-workflows-and-cicd--heading-1-purpose-and-accepted-boundary"></a>
## 1. Purpose and Accepted Boundary

The older inclusion references in this section are historical. Every product obligation in this document is deferred after MVP; the new allocation supersedes its old Version 1 commitment.

[Scope DEC-019](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/01-project-planning/02-scope.md#dec-019) includes YAML-defined
repeatable checks, tests, builds and actual results/logs, with deployment as a
separately controlled stage where defined. It requires isolation, authorization,
secrets, cleanup and resource analysis before implementation. Compatibility with
every GitHub Actions workflow is not implied.

The capability is part of Resumefolio; using CI to build Resumefolio elsewhere
does not demonstrate it. [Git Hosting](08-Git-Hosting-And-Collaboration.md#requirements-specification-git-hosting-and-collaboration) is a separate
capability, and Push/merge/release does not inherently authorize production deployment.
No workflow engine, runner, container/VM, command syntax, event trigger or public
interface is selected. No actual job/deployment is launched by this revision.

Use [Accounts](01-Accounts-Authentication-And-Permissions.md#requirements-specification-accounts-authentication-and-permissions),
[Interfaces](07-External-Interface-Requirements.md#requirements-specification-external-interface-requirements),
[Files/Operations](02-Administration-Files-And-Operational-Behavior.md#requirements-specification-administration-files-and-operational-behavior),
[Quality/Recovery](14-Quality-Security-And-Recovery-Requirements.md#requirements-specification-quality-security-and-recovery-requirements) and
[Business Lifecycle](04-Business-Rules-And-Data-Lifecycle.md#requirements-specification-business-rules-and-data-lifecycle) for cross-module invariants.

<a id="requirements-specification-yaml-workflows-and-cicd--heading-2-capability-and-information-inventory"></a>
## 2. Capability and Information Inventory

| Subject | Required contract | Open selection |
| --- | --- | --- |
| Definition | Supported syntax, inputs, actions/steps, version and validation | No arbitrary YAML or ecosystem compatibility assumed |
| Trigger/run | Eligible initiator/event, code/definition revision, authority and attempt | Trigger types, state model, deduplication and concurrency |
| Execution | Isolated work context, allowed identity/network/resources and secret scope | Runner mechanism, environment/dependencies and limits |
| Results | Step/run outcomes, permitted logs and any agreed artifacts | Aggregation, safe display, retention and unknown outcomes |
| Deployment | Explicit target authority/approval, artifact/revision and verification | Targets, approver rules, failure and data-compatible recovery |
| Operations | Cancellation, runner loss, cleanup/accounting, guidance and restoration | Exact procedures and actual control/resource evidence |

For each supported action, specify inputs, permissions, preconditions, allowed
effects, output/result meaning, limits, failure/repetition and evidence. Treat
repository code, definitions and outputs as untrusted within the reviewed threat
model. Authorized authorship does not grant host, other-tenant or arbitrary network access.

<a id="requirements-specification-yaml-workflows-and-cicd--heading-3-proposed-requirements"></a>
## 3. Proposed Requirements

Farhad owns these records. Read their retained IDs and original criteria using the [current record rules](15-Requirement-Priority-And-Readiness.md#current-record-rules). This domain is deferred after MVP. Planned checks do not establish executed results or personal owner acceptance.

<a id="requirements-specification-yaml-workflows-and-cicd--heading-yml-d01-defined-supported-workflow-contract"></a>
### YML-D01: Defined Supported Workflow Contract

**Release allocation (owner decision, November 4):** Deferred after MVP.

**Source / rationale:** DEC-019; YAML definitions need an explicit supported meaning.

**Actor / conditions:** Authorized author supplies a workflow definition for an eligible repository/context.

**Proposed obligation:** The product shall validate agreed workflow syntax/structure and supported behavior before it is eligible for execution.

**Acceptance criteria**
- Supported examples identify intended checks/build steps, inputs and relevant configuration.
- Malformed/unsupported definitions produce defined validation feedback rather than silently executing unrecognized behavior.
- The effective definition/version is distinguishable from an arbitrary unreviewed latest file.

**Planned verification:** Later supported/unsupported/invalid examples and definition-version inspection.

**Open detail:** YAML subset/schema, file location, actions/commands/dependencies, expressions, step ordering, inputs and compatibility/version policy; no GitHub Actions parity or unrestricted command model selected.

<a id="requirements-specification-yaml-workflows-and-cicd--heading-yml-d02-explicit-triggers-and-run-authority"></a>
### YML-D02: Explicit Triggers and Run Authority

**Release allocation (owner decision, November 4):** Deferred after MVP.

**Source / rationale:** DEC-019/028; a code event is not inherently unlimited execution authority.

**Actor / conditions:** User or selected event requests a run.

**Proposed obligation:** Only agreed eligible triggers and actors shall create execution work under the applicable repository/workflow/run authority.

**Acceptance criteria**
- Selected trigger examples create only the intended permitted work.
- Unauthorized actors, altered repository references and ineligible events cannot start protected execution.
- Repeated/concurrent trigger events follow explicit deduplication/admission rules with distinguishable results.

**Planned verification:** Later controlled allowed/denied/manual/event cases after trigger selection.

**Open detail:** Manual/event triggers, branch/fork policy, webhook if selected, scheduling, re-runs and duplicate semantics; no event type or unattended job configured here.

<a id="requirements-specification-yaml-workflows-and-cicd--heading-yml-d03-run-identity-and-reproducible-context"></a>
### YML-D03: Run Identity and Reproducible Context

**Release allocation (owner decision, November 4):** Deferred after MVP.

**Source / rationale:** DEC-019 and proposed traceability refinement; results must relate to the evaluated code/definition.

**Actor / conditions:** An eligible run is accepted or inspected.

**Proposed obligation:** Each run shall identify its repository/ref resolution, evaluated revision, effective definition and relevant non-secret execution context.

**Acceptance criteria**
- A later branch change does not silently relabel an existing run as having evaluated different code.
- Permitted result inspection distinguishes separate attempts and their defined relationship to a rerun.
- Evidence identifies environment/input limits without exposing secret values.

**Planned verification:** Later fixed-revision, changed-ref and rerun context comparisons.

**Open detail:** Ref resolution point, environment/dependency capture, run/attempt identifiers and reproducibility scope; no byte-identical build guarantee.

<a id="requirements-specification-yaml-workflows-and-cicd--heading-yml-d04-isolation-and-untrusted-code-boundary"></a>
### YML-D04: Isolation and Untrusted-code Boundary

**Release allocation (owner decision, November 4):** Deferred after MVP.

**Source / rationale:** DEC-019/GAP-D09; hosted code and workflow definitions can act with unintended authority.

**Actor / conditions:** A run is prepared/executed in the selected isolated environment after feasibility review.

**Proposed obligation:** Execution shall enforce reviewed filesystem/process/network/identity boundaries protecting the host, unrelated tenants/resources and operational control plane.

**Acceptance criteria**
- Later controlled attempts cannot access unrelated private repository/user/host data beyond permitted inputs.
- Allowed execution cannot gain administrative/host authority merely through crafted code or definition inputs.
- Isolation failure or inability to establish required controls blocks enabling the affected execution capability.

**Planned verification:** Later bounded isolated security checks in an authorized environment.

**Open detail:** Threat scenarios, runner/isolation mechanism, privilege/network policy, workspace/dependency handling and control evidence; no container/VM or safe-host result selected/claimed.

<a id="requirements-specification-yaml-workflows-and-cicd--heading-yml-d05-scoped-secrets-and-credentials"></a>
### YML-D05: Scoped Secrets and Credentials

**Release allocation (owner decision, November 4):** Deferred after MVP.

**Source / rationale:** DEC-019/028 and resource credential constraints; a run grant is not a grant to every secret.

**Actor / conditions:** Run requires an explicitly permitted secret/credential or produces output.

**Proposed obligation:** Secret access shall be scoped to reviewed actor/repository/event/target conditions with protected handling and output rules.

**Acceptance criteria**
- An ineligible run/fork/event cannot obtain a protected secret through normal or altered requests.
- Ordinary log/artifact/status examples do not expose secret values under the defined handling policy.
- Credential change/revocation and failed secret availability have explicit outcomes rather than an authorization bypass.

**Planned verification:** Later controlled synthetic-secret allowed/denied/output/revocation cases.

**Open detail:** Secret creation/view/update authority, storage/injection/lifetime, output protection, untrusted forks, rotation and deployment credentials; no universal perfect redaction guarantee.

<a id="requirements-specification-yaml-workflows-and-cicd--heading-yml-d06-resource-admission-and-limits"></a>
### YML-D06: Resource Admission and Limits

**Release allocation (owner decision, November 4):** Deferred after MVP.

**Source / rationale:** DEC-019/018 and existing-server constraints; execution competes with the product workload.

**Actor / conditions:** A run requests execution/storage/network resources.

**Proposed obligation:** Run admission and execution shall respect explicit effective resource/concurrency/time/output limits justified against actual combined capacity.

**Acceptance criteria**
- Defined eligible/over-limit requests produce reviewed admitted/pending/rejected outcomes.
- Later controlled limit-exceeding runs have distinguishable terminated/failed outcomes and defined cleanup/accounting.
- Combined-workload findings evaluate impact on other required workflows; a user count alone is not execution capacity evidence.

**Planned verification:** Later bounded resource/admission/combined-load cases.

**Open detail:** CPU/memory/storage/network, concurrency/queue/time/output limits, fair use, warning thresholds and reservations; no numerical limits or extra runner server assumed.

<a id="requirements-specification-yaml-workflows-and-cicd--heading-yml-d07-truthful-run-and-step-outcomes"></a>
### YML-D07: Truthful Run and Step Outcomes

**Release allocation (owner decision, November 4):** Deferred after MVP.

**Source / rationale:** DEC-019 and proposed reliability refinement; queued work or a partial build is not successful completion.

**Actor / conditions:** An authorized user monitors a run/check/build and its permitted outputs.

**Proposed obligation:** The product shall expose reviewed run/step state and completion semantics tied to actual execution outcomes.

**Acceptance criteria**
- Pending/running/completed/failed/cancelled or equivalent selected states are distinguishable under the final state model.
- A required step failure, missing output or interrupted execution cannot produce a false successful overall result.
- Unavailable/unknown runner state is reported/reconciled under the defined policy rather than invented success.

**Planned verification:** Later controlled success/failure/interruption and required-step aggregation cases.

**Open detail:** Final state machine, dependency/skip/continue behavior, exit/result meaning, timing and detection; example states do not establish the final model.

<a id="requirements-specification-yaml-workflows-and-cicd--heading-yml-d08-restricted-logs-and-artifacts"></a>
### YML-D08: Restricted Logs and Artifacts

**Release allocation (owner decision, November 4):** Deferred after MVP.

**Source / rationale:** DEC-019 with proposed output/interface refinement; execution outputs can carry private or unsafe data.

**Actor / conditions:** Actor requests run logs/results or agreed artifacts.

**Proposed obligation:** Outputs shall retain run/revision context and follow reviewed access, content, size and lifecycle policies across UI/direct retrieval.

**Acceptance criteria**
- Authorized inspection shows intended run/attempt output without mixing another user/repository context.
- Unauthorized direct log/artifact requests cannot bypass repository/run/output authority.
- Partial/truncated/unavailable outputs are distinguishable; defined active/unsafe content is not served contrary to reviewed policy.

**Planned verification:** Later run-context/direct access/unsafe-output and incomplete-output cases.

**Open detail:** Artifact support/types, access after repository changes, retention, truncation, safe serving, download, size and deletion; no unlimited logs or universal upload policy assumed.

<a id="requirements-specification-yaml-workflows-and-cicd--heading-yml-d09-cancellation-retry-and-runner-loss-recovery"></a>
### YML-D09: Cancellation, Retry and Runner-loss Recovery

**Release allocation (owner decision, November 4):** Deferred after MVP.

**Source / rationale:** Proposed reliability detail for DEC-019; repetition may repeat external effects.

**Actor / conditions:** Authorized actor cancels/retries, or a runner fails/disconnects.

**Proposed obligation:** Cancellation, retry and orphaned-run reconciliation shall have explicit authority, actual-state and side-effect policies.

**Acceptance criteria**
- Cancellation request and confirmed execution termination are distinguishable under the reviewed state rules.
- Runner loss leaves an observable unresolved/failed state with defined reconciliation, not false success.
- Rerunning a deployment/send/other consequential step follows its explicit approval/reconciliation policy rather than blind automatic replay.

**Planned verification:** Later isolated cancellation/runner-loss/retry and ambiguous-effect cases.

**Open detail:** Cancellation scope, cleanup timing, orphan detection, retry eligibility, duplicate handling and confirmed termination evidence; no exactly-once promise.

<a id="requirements-specification-yaml-workflows-and-cicd--heading-yml-d10-separate-controlled-deployment-stage"></a>
### YML-D10: Separate Controlled Deployment Stage

**Release allocation (owner decision, November 4):** Deferred after MVP.

**Source / rationale:** DEC-019; Push does not inherently authorize production deployment.

**Actor / conditions:** A workflow proposes a change to an explicitly permitted deployment target.

**Proposed obligation:** Deployment shall require reviewed target authority/approval and conditions separate from code Push, merge or check success.

**Acceptance criteria**
- A Push/merge/successful check alone cannot use an otherwise unauthorized deployment target/credential.
- A permitted deployment identifies intended code/artifact revision, target and applicable approval context.
- Rejected/failed/unknown target outcomes are distinguishable from successful usable deployment; recovery follows reviewed version/data compatibility rules.

**Planned verification:** Later isolated authorized/denied target, changed revision and failure/recovery cases.

**Open detail:** Targets, approver identity/action/effective revision, environment restrictions, verification, rollback/forward recovery and migration consequences; no live deployment authorized here.

<a id="requirements-specification-yaml-workflows-and-cicd--heading-yml-d11-workspace-cleanup-and-retained-evidence"></a>
### YML-D11: Workspace Cleanup and Retained Evidence

**Release allocation (owner decision, November 4):** Deferred after MVP.

**Source / rationale:** DEC-019/018/017 and proposed lifecycle refinement; leftovers can leak secrets or exhaust storage.

**Actor / conditions:** Run completes/fails/is cancelled or retained execution material becomes eligible for removal.

**Proposed obligation:** Workspace/temporary/output cleanup shall follow explicit eligibility/reference/retention rules with secret protection and truthful accounting.

**Acceptance criteria**
- A later run cannot read a prior run's protected workspace/secret residue contrary to isolation policy.
- Required retained evidence/artifacts are not deleted merely because temporary work is eligible for cleanup.
- Partial cleanup or accounting failure is distinguishable from complete reclamation and does not silently remove unrelated data.

**Planned verification:** Later isolated successive-run, eligible/ineligible cleanup and failure cases.

**Open detail:** Timing, manual/automatic procedure, cache reuse, artifact/log retention, quarantine/recovery and quota release; no cleanup schedule or retention period set.

<a id="requirements-specification-yaml-workflows-and-cicd--heading-yml-d12-feasibility-operational-guidance-and-enabling-gate"></a>
### YML-D12: Feasibility, Operational Guidance and Enabling Gate

**Release allocation (owner decision, November 4):** Deferred after MVP.

**Source / rationale:** DEC-019/017, GAP-D09/D01/D08; inclusion does not prove executable infrastructure.

**Actor / conditions:** Owner evaluates execution design or enables/accepts the capability.

**Proposed obligation:** Dependent execution commitments shall retain actual isolation/resource/access findings, supported-contract decisions, operational guidance and later control evidence before enabling/acceptance.

**Acceptance criteria**
- The evaluation identifies selected environment, combined workload, supported operations, control checks, costs and unresolved blockers.
- Required security/resource blockers prevent treating execution as enabled/accepted merely because YAML parsing or Git hosting works.
- Guidance covers versioned setup, failure/cancellation/cleanup, updates and recovery without replaying stale work or exposing secrets.

**Planned verification:** Later evidence/design/procedure review and controlled end-to-end run checks before relevant acceptance.

**Open detail:** Actual infrastructure/configuration, mechanism/licensing, targets, solo workload, backup/restore and costs; no feasibility conclusion or successful run recorded.

<a id="requirements-specification-yaml-workflows-and-cicd--heading-4-behavior-and-boundary-models"></a>
## 4. Behavior and Boundary Models

![After MVP — Definition, run, isolation, output and separately controlled target boundaries](../../Diagrams/Workflow-Execution-Boundaries.png)

[Scalable SVG](../../Diagrams/Workflow-Execution-Boundaries.svg) · [Graphviz source](../../Diagrams/Workflow-Execution-Boundaries.dot)

Connections express requirements relationships, not selected services or network
topology. Secrets, output retrieval and deployment targets have distinct authority.

![After MVP — Enabling gate, authorized bounded run and separate deployment decision](../../Diagrams/Workflow-Run-Control-Flow.png)

[Scalable SVG](../../Diagrams/Workflow-Run-Control-Flow.svg) · [PlantUML source](../../Diagrams/Workflow-Run-Control-Flow.puml)

The flow is conceptual, not a final run state machine or a live command sequence.
Re-evaluate mutable grants, code/definition revisions and target conditions as
required by later design. Colors supplement labels; no automatic deployment is implied.

<a id="requirements-specification-yaml-workflows-and-cicd--heading-5-planned-verification"></a>
## 5. Planned Verification

| Family | Candidates | Cases to develop |
| --- | --- | --- |
| Definition/authority | YML-D01–D03 | Supported/invalid definitions, denied triggers, fixed code/revision and reruns  **After MVP.** |
| Trust/resources | YML-D04–D06 | Isolated cross-context attempts, synthetic-secret scope, saturation and admission  **After MVP.** |
| Outcome/output | YML-D07/D08 | Required step failure, unknown state, direct protected output and unsafe/partial artifact  **After MVP.** |
| Recovery/side effects | YML-D09/D10 | Cancel versus termination, runner loss, changed target/revision, approval and failed deployment  **After MVP.** |
| Lifecycle/readiness | YML-D11/D12 | Successive-run residue, reference-aware cleanup, procedure and actual enabling evidence  **After MVP.** |

Later checks use authorized isolated infrastructure, synthetic secrets and controlled
targets. Record candidate/configuration, code/definition/attempt, grants, input,
limits, expected/actual effects, evidence and cleanup outcome. Never expose real
secrets or execute unbounded hostile workloads against existing services. These
are evidence-plan constraints, not authorization for operations in this documentation task.

<a id="requirements-specification-yaml-workflows-and-cicd--heading-6-open-decisions-and-gates"></a>
## 6. Open Decisions and Gates

| Topic | Decisions/evidence needed | Gate |
| --- | --- | --- |
| Execution feasibility | Combined server demand, isolation/control findings, actual access and solo operation | GAP-D09/D01; before execution design acceptance/enabling |
| Syntax/triggers | Supported definition contract, versioned ref resolution, event/manual rules and duplicates | Affected M-02 acceptance and M-03 design |
| Trust/secrets | Actor/ref/fork scope, identity, filesystem/process/network, credentials and protected output | Before dependent implementation/enabling; actual control evidence before M-08 |
| Resource/outcome | Effective limits, admission, state/aggregation, cancel/loss/retry and output access | Before accepting detailed behavior/design |
| Target deployment | Target approval, revision/artifact, permission changes, verification and recovery | Before enabling any deployment stage |
| Lifecycle/operation | Workspace/cache/output retention, accounting, cleanup, update and safe restored state | Design/readiness; relevant actual evidence for M-08/M-09 |

Farhad coordinates [Questions](../07-Change-And-Baseline/03-Requirements-Questions-And-Decisions.md#change-and-baseline-open-questions-and-decisions)
and [Feasibility](../01-Process-And-Approach/01-Feasibility-Study.md#process-and-approach-02-feasibility-study). Preserve
[Planning Gates](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/01-project-planning/10-planning-completion-criteria.md) and
explicit [Change Control](../07-Change-And-Baseline/02-Requirements-Change-Control.md#change-and-baseline-change-control). A blocker
does not silently remove accepted scope or authorize buying another runner/service.

<a id="requirements-specification-yaml-workflows-and-cicd--heading-7-traceability-and-review-readiness"></a>
## 7. Traceability and Review Readiness

YML-D01–D12 derive from DEC-019 and explicitly proposed detailed control/lifecycle
refinements. Reconcile GIT-D real repository context, ACC-D grants, EIF-D07
execution interfaces, AFO-D accounting/cleanup, BRL-D recovery and QSR-D07/D12
untrusted execution/restored external-state rules. Actual M-08 acceptance is separate.

Use the [requirement template](17-Software-Requirements-Specification.md#requirements-specification-requirements-specification) when allocating
final IDs. Link allocated records/scenarios and actual evidence in
[Traceability](../06-Validation-And-Traceability/07-Validation-And-Traceability.md#validation-and-traceability-validation-and-traceability--heading-traceability).
Record actual inspection outcomes in [Review Findings](../06-Validation-And-Traceability/07-Validation-And-Traceability.md#validation-and-traceability-validation-and-traceability--heading-review-findings).

- [ ] Reconcile provisional YML-D references and assign justified priorities.
- [ ] Review source-derived boundaries separately from proposed supporting detail.
- [ ] Resolve policy/state/permission questions blocking affected acceptance.
- [ ] Reconcile dictionary, lifecycle, interface and related domain specifications.
- [ ] Complete normal, denied, failure, concurrent and recovery scenarios where applicable.
- [ ] Record actual owner decision, reviewed revision, evidence and remaining blockers.

**Current outcome:** Proposed specification; no candidate is accepted and no product
test result is recorded. Conditional criteria are not acceptance-ready until their
referenced policies are decided. M-02 and the wider pre-implementation agreement
remain pending. This revision changes no accepted scope and performs no live
repository, application-submission, sharing, file or provider operation.

<a id="requirements-specification-yaml-workflows-and-cicd--heading-8-diagram-maintenance"></a>
<details>
<summary>Supporting reference: 8. Diagram Maintenance</summary>

## 8. Diagram Maintenance

| Diagram | Source | SVG | PNG |
| --- | --- | --- | --- |
| Execution boundaries | [Graphviz](../../Diagrams/Workflow-Execution-Boundaries.dot) | [SVG](../../Diagrams/Workflow-Execution-Boundaries.svg) | ![workflow execution boundaries](../../Diagrams/Workflow-Execution-Boundaries.png) |
| Controlled run flow | [PlantUML](../../Diagrams/Workflow-Run-Control-Flow.puml) | [SVG](../../Diagrams/Workflow-Run-Control-Flow.svg) | ![workflow run control flow](../../Diagrams/Workflow-Run-Control-Flow.png) |

Keep sources, captions and renders synchronized. Colors supplement labels. Follow
the [diagram guide](../../Diagrams/Diagram-Catalog.md); inspect readable arrows/labels and check
file/section links after changes. From repository root:

```powershell
$diagramFolder = 'docs\MVP\SDLC\02-requirements-engineering\diagrams'
$graphvizExe = 'C:\Program Files\Graphviz\bin\dot.exe'
$plantUmlJar = 'C:\Users\fvali\AppData\Local\Resumefolio\DiagramTools\plantuml.jar'
foreach ($format in 'svg', 'png') {
    & $graphvizExe "-T$format" -Gdpi=140 "$diagramFolder\workflow-execution-boundaries.dot" -o "$diagramFolder\workflow-execution-boundaries.$format"
    if ($LASTEXITCODE -ne 0) { throw "Graphviz failed: $format" }
    java '-Djava.awt.headless=true' -jar $plantUmlJar -charset UTF-8 "-t$format" "$diagramFolder\workflow-run-control-flow.puml"
    if ($LASTEXITCODE -ne 0) { throw "PlantUML failed: $format" }
}
```

Use actual tool paths on other machines; save UTF-8 without BOM.

[Specification index](16-Requirements-Specification-Guide.md#requirements-specification-requirements-specification-overview) · [SRS entry point](17-Software-Requirements-Specification.md#requirements-specification-requirements-specification)
· [Requirements index]()

</details>



<a id="requirements-specification-yaml-workflows-and-cicd--heading-selected-policies-and-future-proposals"></a>
## Selected Policies and Future Proposals

Use the [current record rules](15-Requirement-Priority-And-Readiness.md#current-record-rules) and the [decision index](../07-Change-And-Baseline/03-Requirements-Questions-And-Decisions.md#change-and-baseline-open-questions-and-decisions--heading-current-dispositions) to distinguish selected MVP policies, deferred proposals and remaining evidence.

<a id="requirements-specification-yaml-workflows-and-cicd--id-resolution-q-d23"></a>
<a id="requirements-specification-yaml-workflows-and-cicd--heading-proposed-answer-q-d23-workflow-contract-and-enabling-gate"></a>
### Proposed answer Q-D23: Workflow contract and enabling gate

**Affected records:** YML-D01–YML-D12; QSR-D07/D12; GAP-D09. **Current disposition: Deferred after MVP.** The following investigation and proposal are future work; they do not block the current MVP.

1. Propose versioned YAML contract: schema_version, workflow name, allowed triggers, repository revision, jobs, ordered command steps, per-step/job timeout and declared artifact paths. Reject unknown executable keys/unsupported expressions. Initial triggers are explicit manual run and authorized push; never silently claim GitHub Actions parity.

2. Each run/attempt binds immutable code/definition revision, initiator, granted resources and result states Queued/Running/Succeeded/Failed/Cancelled/Unknown. Retry is a new attempt with explicit authority; runner loss is Unknown until reconciled. Logs/artifacts are scoped private outputs with secret redaction and HTML-safe display.

3. Execution environment must prevent access to host/admin interfaces, production data/credentials, other users/jobs and unauthorized network destinations; no privileged mode, host paths or Docker socket exposure. Dependency/network access is explicitly allowlisted. Destruction/recreation between jobs and denial/escape/resource tests are evidence gates, not assumed properties of using containers.

4. Propose one job at a time, 512 MiB job memory, 0.5 vCPU budget, 1 GiB temporary workspace, 10-minute job timeout, 1 MiB log output and 20 MiB artifact cap as evaluation candidates only. These are not a claim that required builds fit or isolation is safe on the shared 4-GB server. If evidence cannot support agreed real execution within resources/budget, escalate the conflict; do not silently drop execution or add a paid server.

5. Deployment is a separately approved stage naming target, exact artifact/revision, authority and compatible data/recovery plan. Untrusted job code cannot receive production secrets or approve its own deployment. The product may record/validate definitions while execution remains disabled pending controls, but validation alone cannot satisfy the agreed execution capability.

**Assessable review cases:** [RC-Q23-01 through RC-Q23-03](../04-Scenarios-And-Models/02-User-Stories-And-Scenarios.md#scenarios-and-models-user-stories-and-scenarios--id-review-q-d23). These are planned checks, not executed results.

**Remaining evidence / acceptance condition:** Actual isolation mechanism, capacity fit, budget-compatible option, cleanup and escape/control evidence are missing. This is a hard dependent-design/enabling gate, not completed feasibility.



<a id="scenarios-and-models"></a>

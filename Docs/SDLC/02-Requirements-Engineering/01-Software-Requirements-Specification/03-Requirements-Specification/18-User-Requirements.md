
<a id="requirements-specification-user-requirements"></a>

<a id="requirements-specification-user-requirements--heading-resumefolio--user-requirements"></a>
# Resumefolio — User Requirements

**Quick read — User needs.** Explains user-level outcomes. Follow the domain links for exact behavior, conditions and acceptance criteria.

[3. Proposed Requirements](#requirements-specification-user-requirements--heading-3-proposed-requirements) · [6. Open Decisions and Gates](#requirements-specification-user-requirements--heading-6-open-decisions-and-gates) · [Selected Policies and Future Proposals](#requirements-specification-user-requirements--heading-selected-policies-and-future-proposals)

[Domain index](README.md) · [Acceptance trace](../../03-Requirements-Traceability-Matrix/README.md)


Current implementation choices and scope: [Baseline](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/README.md). Runtime verification remains subject to its gates.

| Item | Current position |
| --- | --- |
| Owner | Farhad; sole delivery and operations owner |
| Status | Selected MVP slice; future clauses remain deferred; implementation and acceptance evidence remain required; see [current record rules](15-Requirement-Priority-And-Readiness.md#current-record-rules) |
| Planning basis | Accepted scope DEC-028–DEC-017 and stakeholder perspectives |
| Candidate references | USR-D01–USR-D12: retained stable source IDs; criterion scope follows [current record rules](15-Requirement-Priority-And-Readiness.md#current-record-rules) |
| Priority | [current record rules](15-Requirement-Priority-And-Readiness.md#current-record-rules) define Must within MVP slice / Later; file order is not execution order |
| Source record date | October 31, 2026 |

**At a glance:** Describe what each actor needs to achieve in user language. These goals are derived from planning sources, not new interviews or universal permission grants. Detailed behavior stays in domain specifications; quality and exceptional paths apply across journeys.

[Basis](#requirements-specification-user-requirements--heading-1-purpose-and-accepted-boundary) · [Inventory](#requirements-specification-user-requirements--heading-2-capability-and-information-inventory)
· [Requirements](#requirements-specification-user-requirements--heading-3-proposed-requirements) · [Models](#requirements-specification-user-requirements--heading-4-behavior-and-boundary-models)
· [Scenarios](#requirements-specification-user-requirements--heading-5-planned-verification) · [Decisions](#requirements-specification-user-requirements--heading-6-open-decisions-and-gates)
· [Review](#requirements-specification-user-requirements--heading-7-traceability-and-review-readiness)

<a id="requirements-specification-user-requirements--heading-1-purpose-and-accepted-boundary"></a>
## 1. Purpose and Accepted Boundary

Use [Actors and Context](../02-Stakeholders-And-Elicitation/01-Actors-And-System-Context.md#stakeholders-and-elicitation-actors-and-system-context)
and [Stakeholders](../../../01-Project-Planning/01-Project-Charter.md#responsibilities)
for perspectives, and [Scope](../../../01-Project-Planning/01-Project-Charter.md#mvp-scope) for accepted
inclusions/exclusions. A person may act as applicant, resource owner and collaborator
in different contexts; this is not a hierarchy of inherited permissions.

No new user research, stakeholder answers or detailed policy acceptance is recorded.
The [elicitation log](../02-Stakeholders-And-Elicitation/02-Elicitation-Log.md#stakeholders-and-elicitation-elicitation-log) distinguishes
actual documentary extraction from interpretation. No outcome implies AI, automatic
translation or automatic legacy migration, which remain excluded in Version 1.

<a id="requirements-specification-user-requirements--heading-2-capability-and-information-inventory"></a>
## 2. Capability and Information Inventory

| Perspective | Intended outcome | Primary detail owner |
| --- | --- | --- |
| Registered applicant / resume owner | Reuse, tailor, disclose deliberately and preserve actual application materials | PRP-D, PDF-D, APP-D, EGC-D |
| Employer viewer | Understand intended professional material without an account | PDF-D, ACC-D, EIF-D |
| Invited work/code collaborator | Perform permitted work and repository actions | PKS-D, GIT-D, ACC-D |
| Workflow author / deployment authority | Run supported work and control consequential targets separately | YML-D, EIF-D, QSR-D |
| Administrator / platform owner | Configure explicitly permitted policy and inspect authorized outcomes | AFO-D, ACC-D |
| Project owner / operator | Make commitments and operate a maintainable recoverable release | QSR-D, AFO-D, planning decisions |

The [account permission matrix](01-Accounts-Authentication-And-Permissions.md#requirements-specification-accounts-authentication-and-permissions--heading-7-role-resource-and-operation-matrix)
owns detailed grants. A role name or user goal does not authorize all possible
view/edit/delete/restore actions. Supported client/accessibility/language criteria
remain in the interface and quality specifications, not assumptions about users.

<a id="requirements-specification-user-requirements--heading-3-proposed-requirements"></a>
## 3. Proposed Requirements

Farhad owns these records. Read their retained IDs and original criteria using the [current record rules](15-Requirement-Priority-And-Readiness.md#current-record-rules). Only the selected MVP criteria are current delivery obligations. Planned checks do not establish executed results or personal owner acceptance.

<a id="requirements-specification-user-requirements--heading-usr-d01-reuse-and-tailor-professional-information"></a>
### USR-D01: Reuse and Tailor Professional Information

**Release allocation (owner decision, November 4):** MVP — Resumefolio core.

**Source / rationale:** DEC-027/026; derived applicant goal, not a newly conducted interview.

**Actor / conditions:** Registered user preparing resumes for different opportunities.

**Proposed obligation:** The user shall be able to maintain reusable professional information and create independently tailored resumes with relevant selected evidence.

**Acceptance criteria**
- A representative user can select shared information without re-entering it for every resume.
- Two opportunity-specific resumes retain their independent selections, layouts and overrides after changes under the agreed source-update policy.
- The user can select evidence for each resume without exposing their entire private evidence collection.

**Planned verification:** Later two-opportunity task walkthrough; PRP-D01–D06 and related scenarios.

**Open detail:** Required fields, propagation triggers, override precedence, supported evidence and presentation rules; no productivity benefit has been measured.

<a id="requirements-specification-user-requirements--heading-usr-d02-control-pdf-and-employer-sharing"></a>
### USR-D02: Control PDF and Employer Sharing

**Release allocation (owner decision, November 4):** MVP — Resumefolio core.

**Source / rationale:** DEC-025/024; derived resume-owner goal and documentary EXT-001.

**Actor / conditions:** Resume owner chooses what a particular employer may view/download.

**Proposed obligation:** The owner shall be able to control selected shared content, permitted generated/uploaded PDF variants and language-specific uploaded availability through protected links.

**Acceptance criteria**
- The owner can configure generated, uploaded, both or neither for each resume and the permitted uploaded language variants.
- Only the intended selected material is retrievable in the employer context, including direct file/PDF paths.
- The owner can change the sharing password or disable the link under the reviewed access-change policy.

**Planned verification:** Later owner configuration and allowed/denied retrieval walkthrough; PDF-D and ACC-D.

**Open detail:** Link/session lifecycle, missing-language behavior, active/cached/in-flight access and owner preview; disabling retrieval cannot recall a downloaded copy.

<a id="requirements-specification-user-requirements--heading-usr-d03-view-intended-professional-material-without-an-account"></a>
### USR-D03: View Intended Professional Material Without an Account

**Release allocation (owner decision, November 4):** MVP — Resumefolio core.

**Source / rationale:** DEC-024/025/026; derived employer-viewer perspective, not employer research.

**Actor / conditions:** Employer viewer receives an eligible password-protected link.

**Proposed obligation:** The viewer shall be able to view the intended shared resume/evidence and retrieve permitted available PDFs without registering a product account.

**Acceptance criteria**
- A fresh viewer with the correct password can reach eligible selected content without product registration.
- Wrong/missing password, disabled link and unselected/disabled file requests do not disclose protected material.
- Language/variant unavailability and relevant access failure have defined understandable outcomes rather than unrelated private content.

**Planned verification:** Later viewer valid/invalid/missing-variant/direct-request examples; PDF-D04–D06 and EIF-D02.

**Open detail:** Supported clients, accessibility, wording, session lifetime and language fallback; possession of a password does not prove employer identity.

<a id="requirements-specification-user-requirements--heading-usr-d04-prepare-and-track-applications-manually"></a>
### USR-D04: Prepare and Track Applications Manually

**Release allocation (owner decision, November 4):** MVP — Resumefolio core.

**Source / rationale:** DEC-023/016; applicant retains analysis and authorship.

**Actor / conditions:** Registered applicant prepares and tracks a job application.

**Proposed obligation:** The applicant shall be able to record company/position, associate a relevant resume, manually write a cover letter and record progress under explicit state rules.

**Acceptance criteria**
- A representative application retains the intended company/position and allowed resume association.
- The applicant can prepare cover-letter content manually and distinguish save failure from completed persistence.
- Progress follows reviewed transitions without implying automatic external submission or employer receipt.

**Planned verification:** Later preparation/state/validation walkthrough; APP-D01–D05.

**Open detail:** Fields, statuses, corrections, dates and incomplete records; no AI drafting or automatic external application submission is added.

<a id="requirements-specification-user-requirements--heading-usr-d05-keep-a-trustworthy-record-of-actual-submitted-materials"></a>
### USR-D05: Keep a Trustworthy Record of Actual Submitted Materials

**Release allocation (owner decision, November 4):** MVP — Resumefolio core.

**Source / rationale:** DEC-023 and EXT-002; later edits must not rewrite what the applicant recorded as sent.

**Actor / conditions:** Applicant records actual submitted resume and cover-letter material, then changes sources.

**Proposed obligation:** The applicant shall be able to identify and retain actual submitted materials separately from current editable content and live sharing.

**Acceptance criteria**
- Captured actual submitted material remains distinguishable after later source edits/replacement.
- Incomplete/failed preservation is distinguishable from a completed historical set.
- Corrections/resubmissions follow a reviewed policy rather than silently substituting a new set for the original.

**Planned verification:** Later actual-material/capture/source-edit comparison; APP-D05–D09 and BRL-D05.

**Open detail:** Capture trigger/artifact/provenance, repeated sets, deletion and retention; history is neither an indefinite archive nor a backup guarantee.

<a id="requirements-specification-user-requirements--heading-usr-d06-coordinate-correspondence-and-activities"></a>
### USR-D06: Coordinate Correspondence and Activities

**Release allocation (owner decision, November 4):** Deferred after MVP.

**Source / rationale:** DEC-022/028; user-controlled communication in an authorized context.

**Actor / conditions:** Connected user works with Gmail and relevant calendar activities.

**Proposed obligation:** The user shall be able to read, compose, send and reply in the intended Gmail context and coordinate agreed activities with Google Calendar integration under explicit rules.

**Acceptance criteria**
- Representative permitted mail operations use the intended selected account and expose truthful outcomes.
- Agreed activities and application relationships preserve intended time/context and independent private access.
- Access loss, conflict, unavailable data and uncertain outbound effects are distinguishable with defined next actions.

**Planned verification:** Later controlled account/activity/denial/failure walkthrough; EGC-D.

**Open detail:** Actual provider access, permissions, views, synchronization, reminders and delivery limits; no operation has been proven or sent here.

<a id="requirements-specification-user-requirements--heading-usr-d07-plan-and-adapt-authorized-work"></a>
### USR-D07: Plan and Adapt Authorized Work

**Release allocation (owner decision, November 4):** Split — MVP ProjectForge basic capability; advanced workflows deferred.

**Source / rationale:** DEC-021; project/work participant goal.

**Actor / conditions:** Authorized user organizes work through projects, boards, backlogs and Sprints.

**Proposed obligation:** The user shall be able to organize and prioritize work, refine items into tasks and maintain a Sprint Backlog comprising goal, selected items and delivery plan.

**Acceptance criteria**
- Representative work retains distinct Backlog Item/task meanings and valid assignment/priority/due dates.
- The Sprint view/plan identifies goal, selected work and delivery plan together under reviewed change rules.
- Incomplete work remains identifiable at Sprint end; board movement alone is not item acceptance.

**Planned verification:** Later planning/refinement/Sprint-end task walkthrough; PKS-D.

**Open detail:** Relationships, workflow/roles, completion and carry-over, reporting/automation scope; no mandatory ceremonies or additional staff assumed.

<a id="requirements-specification-user-requirements--heading-usr-d08-collaborate-within-invited-resource-boundaries"></a>
### USR-D08: Collaborate Within Invited Resource Boundaries

**Release allocation (owner decision, November 4):** MVP — Resumefolio core.

**Source / rationale:** DEC-028/021/020; collaborator goals differ from owner privileges.

**Actor / conditions:** Invited collaborator participates in a specific authorized board/project/repository.

**Proposed obligation:** The collaborator shall be able to perform granted work/repository actions while remaining outside unrelated private contexts.

**Acceptance criteria**
- An accepted applicable grant permits only the reviewed actions on its intended resources.
- An invitation or board membership alone does not expose private mail, unrelated resumes or repositories.
- Changed/revoked membership has the defined subsequent operation outcome and cannot be bypassed by direct references.

**Planned verification:** Later invited/denied/revoked context walkthrough; ACC-D, PKS-D06 and GIT-D02.

**Open detail:** Invitation states, role/action matrix, resource scope, existing sessions and ownership transfer; actor labels are not universal grants.

<a id="requirements-specification-user-requirements--heading-usr-d09-use-real-repository-collaboration"></a>
### USR-D09: Use Real Repository Collaboration

**Release allocation (owner decision, November 4):** Split — MVP ProjectForge basic capability; advanced workflows deferred.

**Source / rationale:** DEC-020; code contributor/reviewer goal.

**Actor / conditions:** Authorized repository user/client performs agreed Git and collaboration work.

**Proposed obligation:** The user shall be able to work with actual hosted repositories through real Git clients and agreed branch, history, fork, request, review, merge and tracking/release capabilities.

**Acceptance criteria**
- Supported real-client examples demonstrate intended Clone/Fetch/Pull/Push outcomes in the authorized repository.
- A review/merge example identifies source/target revisions and handles conflicts or changed state under reviewed rules.
- Repository issues/milestones/tags/releases retain their intended context without implying deployment.

**Planned verification:** Later real-client and review/release journeys; GIT-D and EIF-D06.

**Open detail:** Client/transports, credentials, grants, merge/release/lifecycle policy; development GitHub is not evidence of product hosting.

<a id="requirements-specification-user-requirements--heading-usr-d10-run-agreed-checks-and-control-deployment-separately"></a>
### USR-D10: Run Agreed Checks and Control Deployment Separately

**Release allocation (owner decision, November 4):** Deferred after MVP.

**Source / rationale:** DEC-019; conditional workflow-author/operator goal.

**Actor / conditions:** Authorized actor uses a reviewed supported workflow after feasibility/security gates.

**Proposed obligation:** The actor shall be able to request agreed repeatable checks/builds and inspect permitted results, with separately controlled deployment authority.

**Acceptance criteria**
- Supported/unsupported definitions have explicit validation outcomes.
- Authorized runs have identifiable definitions/revisions and truthful result/log/artifact access.
- Push/merge/run success does not inherently authorize a protected deployment target or unrelated secrets.

**Planned verification:** Later isolated supported-workflow, denied action and controlled target journeys; YML-D.

**Open detail:** Execution feasibility, syntax/triggers, isolation, limits, approvals and actual evidence; no general GitHub Actions compatibility promised.

<a id="requirements-specification-user-requirements--heading-usr-d11-administer-explicit-policy-and-understand-failures"></a>
### USR-D11: Administer Explicit Policy and Understand Failures

**Release allocation (owner decision, November 4):** MVP — Resumefolio core.

**Source / rationale:** DEC-018/028 and stakeholder responsibilities; platform-owner/admin perspective.

**Actor / conditions:** Actor with defined administrative authority configures policy or investigates an operation.

**Proposed obligation:** The actor shall be able to manage agreed effective policies and inspect permitted operational outcomes without inferring unrestricted access to user content.

**Acceptance criteria**
- A permitted policy edit follows explicit ranges/infrastructure limits and reports the effective outcome.
- Unauthorized policy/content/audit operations are denied across direct paths.
- Relevant incomplete/failed/quota outcomes are distinguishable without exposing secrets/unrelated private data.

**Planned verification:** Later allowed/denied policy and output walkthrough; AFO-D and ACC-D09.

**Open detail:** Exact administrative actions, audit visibility, thresholds and sensitive-operation rules; project governance alone grants no product superuser power.

<a id="requirements-specification-user-requirements--heading-usr-d12-operate-and-recover-an-identified-release"></a>
### USR-D12: Operate and Recover an Identified Release

**Release allocation (owner decision, November 4):** MVP — Resumefolio core.

**Source / rationale:** DEC-017 and sole-owner resources; operator goal rather than a claim of an additional team.

**Actor / conditions:** Farhad operates, maintains or later restores the product using authorized procedures.

**Proposed obligation:** The operator shall have version/environment-specific guidance and evidence to deploy, maintain, diagnose and recover the required workflows within agreed constraints.

**Acceptance criteria**
- Guidance identifies dependencies, non-secret configuration, responsibility and actual checked versus unperformed steps.
- Later isolated restoration checks required artifacts/relationships/workflows and safe restored access against decided targets.
- Failures, limitations and pending external actions remain explicit rather than an untested successful recovery or rollback claim.

**Planned verification:** Later procedure walkthrough and isolated recovery evidence; QSR-D10–D14 and AFO-D12.

**Open detail:** Actual infrastructure/storage, workload, targets, maintenance effort, keys/access and upgrade recovery; no successful deployment or recovery recorded.

<a id="requirements-specification-user-requirements--heading-4-behavior-and-boundary-models"></a>
## 4. Behavior and Boundary Models

![Actor perspectives and scoped user outcomes](../../Diagrams/User-Goal-Map.png)

[Scalable SVG](../../Diagrams/User-Goal-Map.svg) · [Graphviz source](../../Diagrams/User-Goal-Map.dot)

Connections group goals, not role inheritance or technical services. External
systems are dependencies/interfaces, not substitutes for the human outcomes.

![Turn a sourced actor goal into reviewed scenarios and detailed criteria](../../Diagrams/User-Requirement-Review.png)

[Scalable SVG](../../Diagrams/User-Requirement-Review.svg) · [PlantUML source](../../Diagrams/User-Requirement-Review.puml)

The flow is a review roadmap, not evidence that users have validated the goals.
Colors supplement labels. Resolve normal, alternative, denied, failure and recovery
paths in the relevant domain/scenario records, without duplicating competing rules.

<a id="requirements-specification-user-requirements--heading-5-planned-verification"></a>
## 5. Planned Verification

| Journey family | Candidates | Normal and exceptional examples |
| --- | --- | --- |
| Presentation/sharing | USR-D01–D03 | Two resumes, language/variant availability, selected evidence and denied direct requests |
| Applications/communication | USR-D04–D06 | Manual preparation, actual materials, later source edits, provider rejection/disconnect |
| Work/repository | USR-D07–D09 | Item/task distinction, incomplete Sprint work, revoked invite, real client and conflicting merge |
| Execution/administration | USR-D10/D11 | Unsupported definition, unauthorized target/secret/policy action and truthful failed outcome |
| Operation/recovery | USR-D12 | Versioned procedure, incomplete backup/restore, old access and pending external effects |

Before later walkthroughs, record the actor, context/grants, initial data, intent,
steps, expected observable outcome and relevant criteria. Retain actual participant,
candidate/environment, result and limits only when a real activity occurs. No
scenarios or interviews above have been executed in the product.

<a id="requirements-specification-user-requirements--heading-6-open-decisions-and-gates"></a>
## 6. Open Decisions and Gates

| Topic | Definition/evidence needed | Gate |
| --- | --- | --- |
| Goal validation | Review derived goals, missing perspectives, priorities and actual research needs | Before accepting affected user requirements |
| Journeys | Required inputs, states, language/accessibility, normal/denied/failure/recovery paths | Affected M-02 acceptance |
| Grants and lifecycle | Roles/actions, active/revoked contexts, source/history and deletion effects | Related domain/security design |
| Dependencies | Actual provider access, combined resource and execution safety findings | Existing planning gates before dependent commitments/development |
| Evidence | Actual review, traceability, measurable criteria and later operation/recovery results | M-02 versus later separate capability/readiness gates |

Farhad coordinates clarification in [Questions](../07-Change-And-Baseline/03-Requirements-Questions-And-Decisions.md#change-and-baseline-open-questions-and-decisions)
and [Scenarios](../04-Scenarios-And-Models/02-User-Stories-And-Scenarios.md#scenarios-and-models-user-stories-and-scenarios). Local topics
are not newly allocated shared decisions. Preserve [Planning Gates](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/01-project-planning/10-planning-completion-criteria.md)
and [Change Control](../07-Change-And-Baseline/02-Requirements-Change-Control.md#change-and-baseline-change-control) for material impacts.

<a id="requirements-specification-user-requirements--heading-7-traceability-and-review-readiness"></a>
## 7. Traceability and Review Readiness

USR-D01–D12 link the scope-derived actor goals to the domain prefixes listed
in section 2 and in each verification plan. The [SRS](17-Software-Requirements-Specification.md#requirements-specification-requirements-specification)
coordinates levels; user outcomes complement detailed functional, interface,
quality and lifecycle criteria rather than replacing them.

Use the [requirement template](17-Software-Requirements-Specification.md#requirements-specification-requirements-specification) when allocating
final IDs. Link allocated records/scenarios and actual evidence in
[Traceability](../06-Validation-And-Traceability/07-Validation-And-Traceability.md#validation-and-traceability-validation-and-traceability--heading-traceability).
Record actual inspection outcomes in [Review Findings](../06-Validation-And-Traceability/07-Validation-And-Traceability.md#validation-and-traceability-validation-and-traceability--heading-review-findings).

- [ ] Reconcile provisional USR-D references and assign justified priorities.
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

<a id="requirements-specification-user-requirements--heading-8-diagram-maintenance"></a>
<details>
<summary>Supporting reference: 8. Diagram Maintenance</summary>

## 8. Diagram Maintenance

| Diagram | Source | SVG | PNG |
| --- | --- | --- | --- |
| Actor goal map | [Graphviz](../../Diagrams/User-Goal-Map.dot) | [SVG](../../Diagrams/User-Goal-Map.svg) | ![user goal map](../../Diagrams/User-Goal-Map.png) |
| User requirement review | [PlantUML](../../Diagrams/User-Requirement-Review.puml) | [SVG](../../Diagrams/User-Requirement-Review.svg) | ![user requirement review](../../Diagrams/User-Requirement-Review.png) |

Keep sources, captions and renders synchronized. Colors supplement labels. Follow
the [diagram guide](../../Diagrams/Diagram-Catalog.md); inspect readable arrows/labels and check
file/section links after changes. From repository root:

```powershell
$diagramFolder = 'docs\MVP\SDLC\02-requirements-engineering\diagrams'
$graphvizExe = 'C:\Program Files\Graphviz\bin\dot.exe'
$plantUmlJar = 'C:\Users\fvali\AppData\Local\Resumefolio\DiagramTools\plantuml.jar'
foreach ($format in 'svg', 'png') {
    & $graphvizExe "-T$format" -Gdpi=140 "$diagramFolder\user-goal-map.dot" -o "$diagramFolder\user-goal-map.$format"
    if ($LASTEXITCODE -ne 0) { throw "Graphviz failed: $format" }
    java '-Djava.awt.headless=true' -jar $plantUmlJar -charset UTF-8 "-t$format" "$diagramFolder\user-requirement-review.puml"
    if ($LASTEXITCODE -ne 0) { throw "PlantUML failed: $format" }
}
```

Use actual tool paths on other machines; save UTF-8 without BOM.

[Specification index](16-Requirements-Specification-Guide.md#requirements-specification-requirements-specification-overview) · [SRS entry point](17-Software-Requirements-Specification.md#requirements-specification-requirements-specification)
· [Requirements index]()

</details>



<a id="requirements-specification-user-requirements--heading-selected-policies-and-future-proposals"></a>
## Selected Policies and Future Proposals

Use the [current record rules](15-Requirement-Priority-And-Readiness.md#current-record-rules) and the [decision index](../07-Change-And-Baseline/03-Requirements-Questions-And-Decisions.md#change-and-baseline-open-questions-and-decisions--heading-current-dispositions) to distinguish selected MVP policies, deferred proposals and remaining evidence.

<a id="requirements-specification-user-requirements--id-resolution-q-d02"></a>
<a id="requirements-specification-user-requirements--heading-q-d02-selected-policy"></a>
### Q-D02: Selected policy

[Selected answer and remaining evidence](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d02). Apply this policy to the MVP slice; the original criteria above remain subject to their [current dispositions](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/criterion-dispositions.csv).

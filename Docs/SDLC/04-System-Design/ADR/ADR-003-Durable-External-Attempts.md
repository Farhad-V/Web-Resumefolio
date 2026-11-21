# ADR-003 — Durable External Attempts

[Decision index](Decision-Index.md) · [ADR-005 boundaries](ADR-005-Owner-Mvp-System-Boundaries.md) · [ADR-006 baseline](ADR-006-Selected-Mvp-Implementation-Baseline.md)

## Current Status

**Selected MVP durable/outcome-truthful effects, idempotency and outbox rules through ADR-006/T05; provider/runner-specific details remain deferred.** Decision authority remains Farhad. No new approval or runtime evidence is recorded here.

## Decision and Invariants

Record required local intent/outcome durably and keep attributable operation/attempt identity when an effect crosses database, filesystem, Git, mail or service boundaries. A local commit or queue acknowledgment does not prove external completion. Distinguish definitive rejection, known partial work and unknown completion.

| Situation | Required response |
| --- | --- |
| Same actor/operation/key/payload | Resolve the recorded outcome under current authority; do not duplicate the effect |
| Same key with changed payload/scope | Conflict rather than reinterpret the original command |
| Response lost after possible effect | Preserve uncertainty and resolve the same operation before unsafe repeat |
| Worker interrupted | Resume/reconcile owner-local recorded work under the contract |
| Pending artifact finalization | Preserve still-required references/reservations until owner evidence permits release |
| Revoked/unavailable authority | Recheck current policy; no bypass through stale admission or broad worker credentials |

Each application commits locally. SQL rollback cannot undo an already changed Git ref, delivered bytes or a remote commit. Compensation must be an explicitly reviewed owning operation, not a generic erase-history strategy. This decision does not promise exactly-once delivery or select a universal queue/state enum.

## Alternatives and Consequences

Calling every external facility inside a SQL transaction does not make remote effects atomic. Fire-and-forget without durable attributable state loses recoverability. Selected owner-local durable intent/outcomes improve truthful recovery but add worker supervision, state handling, reference protection and reconciliation work.

Retry bounds, identity retention and late-retry behavior follow the actual selected contract; no arbitrary durations or unlimited retries are introduced here. Personal provider sends/calendar, workflow runners and target deployment remain deferred even where the retained record explains their possible future failure modes.

## Verification and Revisit

Exercise concurrent matching keys, inconsistent reuse, stale writes, unavailable/revoked authority, lost acknowledgment after commit, interrupted processing and restored pending work. Verify actual database/storage/Git/service behavior where fakes cannot establish the guarantee. Revisit a mechanism only with evidence of contract/resource limitations and a compatibility/recovery plan preserving attributable outcomes.

## Supporting Dark Diagram

![Durable External Attempts](../01-High-Level-Design/Diagrams/Appendix/runtime-attempt-state-machine.svg)

[PlantUML source](../01-High-Level-Design/Diagrams/Appendix/runtime-attempt-state-machine.puml) · [PNG](../01-High-Level-Design/Diagrams/Appendix/runtime-attempt-state-machine.png)

This canonical view illustrates the applicable current contracts; it does not convert retained proposal details or deferred features into MVP obligations.

## Sources, Evidence and Retained Rationale

Use [LLD contracts](../03-Low-Level-Design/03-Detailed-Module-Design.md), [Database Design](../03-Low-Level-Design/04-Database-Design.md), [API Specification](../03-Low-Level-Design/05-API-Specification.md) and the [RTM](../../02-Requirements-Engineering/03-Requirements-Traceability-Matrix.md) for exact implementation/criterion evidence. Preserve immutable baseline provenance links.

The record below retains original anchors, alternatives and context. Current status above and ADR-006/ADR-007 govern any older proposed/pending wording. Runtime setup, security, compatibility and recovery still require fresh evidence; documentation does not close those gates.

<a id="design-record-07-design-decisions-adr-003-durable-external-attempts-md"></a>

<details>
<summary>ADR-003 — Durable External Attempts and Reconciliation</summary>

<a id="design-record-07-design-decisions-adr-003-durable-external-attempts-md--heading-adr-003-â-durable-external-attempts-and-reconciliation"></a>

### ADR-003 — Durable External Attempts and Reconciliation

Current implementation choices and scope: [Baseline](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/README.md). Runtime verification remains subject to its gates.

| Item | Position |
| --- | --- |
| Status | **Selected MVP durable/outcome-truthful effects, idempotency and outbox rules through ADR-006/T05; provider/runner-specific details remain deferred.** |
| Decision authority | Farhad |
| Scope | Durable intent, attributable attempts, dispatch coordination and evidence-supported external outcomes |
| Implementation evidence | No queue, worker, provider idempotency facility, executor or target protocol is verified here |

[Context](#design-record-07-design-decisions-adr-003-durable-external-attempts-md--heading-1-context-and-source-authority) · [Options](#design-record-07-design-decisions-adr-003-durable-external-attempts-md--heading-2-options-considered) · [Proposal](#design-record-07-design-decisions-adr-003-durable-external-attempts-md--heading-3-proposed-decision) · [Application](#design-record-07-design-decisions-adr-003-durable-external-attempts-md--heading-4-operation-specific-application) · [Consequences](#design-record-07-design-decisions-adr-003-durable-external-attempts-md--heading-5-consequences-and-limits) · [Validation](#design-record-07-design-decisions-adr-003-durable-external-attempts-md--heading-6-validation-and-disposition) · [Evolution](#design-record-07-design-decisions-adr-003-durable-external-attempts-md--heading-7-revisit-and-evolution)

<a id="design-record-07-design-decisions-adr-003-durable-external-attempts-md--heading-1-context-and-source-authority"></a>

#### 1. Context and source authority

Provider sends/calendar changes, native Git mutations, artifact processing, execution and deployment can have effects outside the local relational transaction. A timeout, worker crash or lost acknowledgment can leave the effect unknown. Repeating a request after such ambiguity can duplicate a send, launch or target change; marking it failed can misrepresent actual state.

Use [runtime design](../01-High-Level-Design/14-Appendices.md#design-record-01-software-architecture-03-process-view-concurrency-and-runtime-behavior-md), [interface requirements](../../02-Requirements-Engineering/01-Software-Requirements-Specification.md#requirements-specification-external-interface-requirements), [provider requirements](../../02-Requirements-Engineering/01-Software-Requirements-Specification.md#requirements-specification-email-calendar-and-google-integration), [workflow requirements](../../02-Requirements-Engineering/01-Software-Requirements-Specification.md#requirements-specification-yaml-workflows-and-cicd), [quality/recovery requirements](../../02-Requirements-Engineering/01-Software-Requirements-Specification.md#requirements-specification-quality-security-and-recovery-requirements) and [source decisions](../../02-Requirements-Engineering/01-Software-Requirements-Specification.md#change-and-baseline-open-questions-and-decisions). Detailed retry, trigger, cancellation and provider policies retain their source status.

The [modular-boundary proposal](ADR-001-Modular-Application-Boundaries.md#design-record-07-design-decisions-adr-001-modular-application-boundaries-md) and [publication/history proposal](ADR-002-Explicit-Publication-And-History.md#design-record-07-design-decisions-adr-002-explicit-publication-and-history-md) require truthful outcomes and preserved identities across owners. This record proposes technical coordination, not a new product automation policy, universal queue requirement or exactly-once guarantee.

<a id="design-record-07-design-decisions-adr-003-durable-external-attempts-md--heading-2-options-considered"></a>

#### 2. Options considered

<a id="design-record-07-design-decisions-adr-003-durable-external-attempts-md--heading-a-â-call-an-external-facility-inside-the-local-transaction"></a>

##### A — Call an external facility inside the local transaction

Straightforward code can make the call appear coordinated with local state, but remote effects cannot generally be rolled back with SQL. Long transactions also retain local resources while waiting on the dependency. A crash after remote acceptance can still leave ambiguous local state. This is not a sufficient general correctness strategy.

<a id="design-record-07-design-decisions-adr-003-durable-external-attempts-md--heading-b-â-commit-local-state-then-issue-an-unrecorded-external-call"></a>

##### B — Commit local state, then issue an unrecorded external call

Shortens local transaction duration but risks losing required work if the process dies after commit and before dispatch. Adding a generic automatic retry can duplicate already accepted effects when the result is lost. Suitable only where the specific contract does not require durable effect coordination and its risks are explicit.

<a id="design-record-07-design-decisions-adr-003-durable-external-attempts-md--heading-c-â-durable-local-intent-and-identified-attempts-with-reconciliation"></a>

##### C — Durable local intent and identified attempts with reconciliation

Commit required local state and pending intent coherently; dispatch through scoped adapters with stable identities; retain attributable observations and reconcile ambiguity before consequential repeat. Adds operating and state-model complexity while making lost intent and unknown effects explicit. **This is the proposed shared direction.**

These are qualitative assessments. Actual transactional, queue and external capabilities need evaluation; using an outbox or broker alone does not solve remote duplicate effects.

<a id="design-record-07-design-decisions-adr-003-durable-external-attempts-md--heading-3-proposed-decision"></a>

#### 3. Proposed decision

Persist reviewed consequential intent and distinguish the business operation, local command, dispatch ownership and external attempt identities. Store immutable intended inputs/revisions or sufficient protected references, current eligibility requirements and actual observed outcomes. Avoid copying raw secrets/private payloads into ordinary diagnostic records.

[Proposed durable attempt and reconciliation protocol](../01-High-Level-Design/Diagrams/Appendix/durable-attempt-protocol.svg)

[Owning runtime protocol](../01-High-Level-Design/14-Appendices.md#design-record-01-software-architecture-03-process-view-concurrency-and-runtime-behavior-md--heading-4-durable-work-dispatch-and-reconciliation) · [Editable Graphviz](../01-High-Level-Design/Diagrams/Appendix/durable-attempt-protocol.dot) · ![durable attempt protocol](../01-High-Level-Design/Diagrams/Appendix/durable-attempt-protocol.png)

<a id="design-record-07-design-decisions-adr-003-durable-external-attempts-md--heading-local-commit-and-dispatch"></a>

##### Local commit and dispatch

Where a local operation requires later work, commit its owned state, attributable result and pending intent atomically through an evaluated outbox or equivalent mechanism. Dispatch only committed intent. Queue deliveries may duplicate; a delivery acknowledgment is neither business completion nor proof of external acceptance.

Scope command identity to its actual actor/resource/operation contract, compare intended payload/version context and reject changed intent under the same identity. Prior-result lookup still requires current authority. A missing HTTP response after commit is not evidence of rollback. Read-only operations need no mutation/outbox record merely for uniformity.

<a id="design-record-07-design-decisions-adr-003-durable-external-attempts-md--heading-claims-stale-workers-and-current-authority"></a>

##### Claims, stale workers and current authority

Use evaluated atomic claims with bounded ownership/lease and changing claim-generation/fencing identity. Local observation/result updates validate current claim ownership so stale workers cannot overwrite a successor's state. Persistent workers reconstruct current required authority and exact attempt context rather than reuse an evergreen serialized session.

A lease expiry does **not** stop a worker already sending or executing remotely. After possible dispatch, reclaiming local ownership cannot authorize blind resend. External fencing/idempotency must be supported and actually enforced by the relevant facility before relying on it; a local token has no such power automatically.

<a id="design-record-07-design-decisions-adr-003-durable-external-attempts-md--heading-evidence-and-repetition"></a>

##### Evidence and repetition

Record known pending, confirmed completion, confirmed no-effect failure, partial and unknown outcomes as applicable, with attempt identity, observation provenance and actual time. Keep request acceptance, business effect, output availability and cleanup as separate facts where their meanings differ.

After ambiguity, inspect the same attributable attempt/effect through the owning adapter's actual capabilities. If reconciliation cannot establish an outcome, retain Unknown/partial context and obtain the reviewed bounded disposition; do not fabricate safe retry from absent local evidence. A permitted new retry creates a distinct attempt linked to prior intent/outcomes. Duplicate delivery of the same work is not automatically a new authorized business operation.

If a provider supports idempotency, evaluate its actual key scope, retention, payload matching, concurrent behavior and result-lookup limits. No particular provider support is asserted here. Cancellation intent is separate from confirmed prevention/stop; completion can win the race and prior effects remain observable.

<a id="design-record-07-design-decisions-adr-003-durable-external-attempts-md--heading-4-operation-specific-application"></a>

#### 4. Operation-specific application

| Owner/boundary | Required specialization |
| --- | --- |
| [Communication/Calendar](../03-Low-Level-Design/03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-communication-and-calendar-md) | Preserve reviewed send/event context and provider identity; acceptance is not recipient receipt; ambiguous writes need actual reconciliation |
| [Git](../03-Low-Level-Design/03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-git-collaboration-md) | Guard exact native ref intent and retain observed ref outcomes; relational metadata rollback does not undo changed refs |
| [Workflow/Deployment](../03-Low-Level-Design/03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-workflow-and-deployment-md) | Bind exact code/definition/executor attempt; separate launch/stop/output/cleanup and target approval/effects; no automatic relaunch/redeploy |
| [Files](../03-Low-Level-Design/03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-files-and-operations-md) | Coordinate staged bytes, protected consumer references and actual reclamation; unknown acknowledgment/deletion retains appropriate protection/accounting |
| [Sharing](../03-Low-Level-Design/03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-representation-and-sharing-md) | Bind generation to exact publication/language/render inputs; an old worker cannot make stale output current |

These boundaries do not all require the same queue or retry policy. Native synchronous operations can use durable intent/observation without becoming broker jobs; exact local algorithm and result semantics remain component-owned.

<a id="design-record-07-design-decisions-adr-003-durable-external-attempts-md--heading-5-consequences-and-limits"></a>

#### 5. Consequences and limits

**Expected benefits:** required work remains discoverable after local commit; repeated local intent can resolve to one attributable result; uncertainty and recovery obligations remain visible. These are design rationale, not observed reliability results.

**Costs:** additional intent/attempt/claim/observation persistence, restricted status projections, worker supervision, queue-age/resource management and reconciliation procedures. Pending state consumes actual storage/operating capacity within the sole owner's total 20 project hours/week.

**Limits:** durable dispatch does not promise exactly-once execution, universal provider lookup, safe cancellation, automatic compensation or remote rollback. Backoff/circuit breaking reduces pressure but does not prove no effect. Compensation is a separate attributable authorized operation and may be impossible or irreversible.

Physical schemas, transaction/claim guards, queue/supervisor facilities, callback authentication, external duplicate/fencing semantics, retention and resumption procedures remain pending evaluation. Follow [data design](../03-Low-Level-Design/04-Database-Design.md#design-record-04-data-design-data-design-md), [API contracts](../03-Low-Level-Design/05-API-Specification.md#design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md), [security](../01-High-Level-Design/14-Appendices.md#design-record-06-design-quality-and-security-analysis-02-security-threat-modeling-and-trust-boundaries-md) and [operations/recovery](../01-High-Level-Design/14-Appendices.md#design-record-06-design-quality-and-security-analysis-03-operations-backup-recovery-and-resilience-md). A restored pending row cannot replay sends/jobs/deployments automatically.

<a id="design-record-07-design-decisions-adr-003-durable-external-attempts-md--heading-6-validation-and-disposition"></a>

#### 6. Validation and disposition

For an identified candidate, exercise interruptions before local commit, after commit/before dispatch, before known dispatch, and after possible external acceptance/before observation. Require evidence-supported results, preserved owned state and no blind consequential repetition.

Also check:

- Duplicate deliveries and reused command identities with changed intent.
- Concurrent claims, lease expiry and late stale-worker results, including an old worker still performing a remote action.
- Current authority changes while work waits or reaches a consequential stage.
- Lost launch/stop/target responses and cancellation racing completion.
- Actual protected output/reference/accounting state after partial/unknown work.
- Isolated coordinator restoration reconciled with current authority and actual external effects before resumption.

Use actual persistence/concurrency and authorized adapter/provider/executor/target evidence alongside deterministic state checks. A mock returning success cannot prove duplicate protection, termination or remote no-effect. Verify actual external compatibility at selection time rather than importing a generic retry assumption.

Record exact source/design revisions, findings, limitations and actual owner disposition through [review/handoff](../01-High-Level-Design/14-Appendices.md#design-record-06-design-quality-and-security-analysis-05-design-review-traceability-and-handoff-md). No test Pass, queue installation, execution enablement, purchase or acceptance is created by elaborating this proposed ADR.

<a id="design-record-07-design-decisions-adr-003-durable-external-attempts-md--heading-7-revisit-and-evolution"></a>

#### 7. Revisit and evolution

Reassess per-operation coordination when measured workload, external capabilities, latency/operating needs or new failure evidence change the trade-off. A simpler mechanism is acceptable only where it preserves the actual contract; a more complex broker does not justify weaker authority or effect semantics.

Schema/worker/adapter changes must preserve old pending intent and observation meaning, claim-generation safety and current authority. Define compatible migration/resumption before retiring an old format. If an accepted decision changes, add a superseding ADR and retain original rationale and actual disposition history.

[Decision index](Decision-Index.md#design-record-07-design-decisions-design-decisions-md) · [ADR-001: Boundaries](ADR-001-Modular-Application-Boundaries.md#design-record-07-design-decisions-adr-001-modular-application-boundaries-md) · [ADR-002: Publication/history](ADR-002-Explicit-Publication-And-History.md#design-record-07-design-decisions-adr-002-explicit-publication-and-history-md) · [ADR template](Decision-Index.md#design-record-07-design-decisions-design-decisions-md)

</details>

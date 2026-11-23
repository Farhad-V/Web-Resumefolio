
<a id="stakeholders-and-elicitation-elicitation-log"></a>

<a id="stakeholders-and-elicitation-elicitation-log--heading-resumefolio--elicitation-log"></a>
# Resumefolio — Elicitation Log

This log records where requirements came from and what the owner actually reported. Use the [decision index](../07-Change-And-Baseline/03-Requirements-Questions-And-Decisions.md#change-and-baseline-open-questions-and-decisions) for current policy and rationale.

<a id="stakeholders-and-elicitation-elicitation-log--heading-source-register"></a>
## Source register

| ID | Source |
| --- | --- |
| SRC-01 | [Purpose and objectives](../../../01-Project-Planning/01-Project-Charter.md#purpose-and-success), OBJ-01–05 and DEC-001–008 |
| SRC-02 | [Scope decisions](../../../01-Project-Planning/01-Project-Charter.md#mvp-scope), DEC-009–028 |
| SRC-03 | [Stakeholders and responsibilities](../../../01-Project-Planning/01-Project-Charter.md#responsibilities), DEC-029–032 |
| SRC-04 | [Planning decision register](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/01-project-planning/decision-register.md) and [accepted planning snapshot](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/01-project-planning/10-planning-completion-criteria.md#dec-116) |
| SRC-05 | Earlier project chats. Cite the specific turn when used. |
| SRC-06 | [Reference projects](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/01-project-planning/02-scope.md#dec-011). Cite the repository, file and revision when used. |

<a id="stakeholders-and-elicitation-elicitation-log--heading-log-001-scope-decision-extraction"></a>
### LOG-001: Scope Decision Extraction

Codex reviewed the three scope decisions below and recorded the corresponding needs. This was document analysis. Stakeholder validation is tracked separately.

Inspected working-copy SHA-256: `33b218141cef0799afe61adc098b7c42e6eb3ee9b1826c1b3d03f926b332dd82`.

<a id="stakeholders-and-elicitation-elicitation-log--heading-ext-001-controlled-employer-access"></a>
### EXT-001: Controlled Employer Access

Employers should see only the shared resume and permitted material. The same access boundary applies to direct file and PDF retrieval. [Source DEC-024](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/01-project-planning/02-scope.md#dec-024) · [Selected sharing policy](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d11)

<a id="stakeholders-and-elicitation-elicitation-log--heading-ext-002-manual-applications-and-preserved-submissions"></a>
### EXT-002: Manual Applications and Preserved Submissions

Users prepare applications, track their progress and preserve the exact materials they submitted. [Source DEC-023](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/01-project-planning/02-scope.md#dec-023) · [Submission history policy](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d13)

<a id="stakeholders-and-elicitation-elicitation-log--heading-ext-003-unified-sign-in-and-resource-permissions"></a>
### EXT-003: Unified Sign-in and Resource Permissions

Users sign in with individual accounts. Access depends on the current grant, resource and action. [Source DEC-028](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/01-project-planning/02-scope.md#dec-028) · [Resource grants policy](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d04)

<a id="stakeholders-and-elicitation-elicitation-log--id-log-002-owner-supplied-server-observation-record"></a>

<a id="stakeholders-and-elicitation-elicitation-log--heading-owner-inputs-and-follow-up--november-1-2026"></a>
## Owner inputs and follow-up — November 1, 2026

| Record | Input or observed activity |
| --- | --- |
| **LOG-002** | The owner supplied hosting screenshots and SSH output. See the [dated server inventory and limits](../01-Process-And-Approach/01-Feasibility-Study.md#process-and-approach-02-feasibility-study--id-server-observation-2026-11-01). |
| <a id="stakeholders-and-elicitation-elicitation-log--id-log-003"></a>**LOG-003** | The owner requested completion of the open questions. Codex drafted proposals and performed [bounded read-only checks](../06-Validation-And-Traceability/05-Server-Readonly-Check-2026-11-01json.md#validation-and-traceability-server-readonly-check-2026-11-01). Individual proposals awaited review. |
| <a id="stakeholders-and-elicitation-elicitation-log--id-log-004-capacity-answer-and-follow-up-observation"></a>**LOG-004** | Work follows the selected scope, dependencies and demonstrated outcomes. |
| <a id="stakeholders-and-elicitation-elicitation-log--id-log-005-actual-oauth-status-answer"></a>**LOG-005** | The owner reported that the intended Google OAuth project had not been created. Google integration is deferred. [Q-D15](../07-Change-And-Baseline/03-Requirements-Questions-And-Decisions.md#change-and-baseline-open-questions-and-decisions--id-q-d15) |
| <a id="stakeholders-and-elicitation-elicitation-log--id-log-006-actual-backup-setup-answer"></a>**LOG-006** | The owner reported that application backups had not been set up. The destination, coverage and isolated restore still require evidence. [Q-D26](../07-Change-And-Baseline/03-Requirements-Questions-And-Decisions.md#change-and-baseline-open-questions-and-decisions--id-q-d26) |

<a id="stakeholders-and-elicitation-elicitation-log--heading-5-recording-new-activities"></a>
## 5. Recording New Activities

Record the date, source, actor, need or observation, and the decision or open question it informs. Link the evidence and keep reported observations separate from verified results.

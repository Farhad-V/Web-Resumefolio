# Resumefolio — Requirements Answer Review Package

## Current implementation baseline — November 4, 2026

[BL-MVP-2026-11-04.1](../../../baseline/README.md) selects the MVP technical mechanisms, numerical policies, priorities and requirement/criterion dispositions under Farhad’s explicit delegation. It supersedes earlier Proposed/pending mechanism and whole-baseline statements below for MVP design input. Future clauses and dated evidence remain separate. Runtime/actor validation, credentials, Git isolation, capacity and backup/restore still require the named implementation/Release gates; this update reports no product test Pass.

### Prior source material and rationale (superseded where this Baseline selects a different MVP choice)

Date: November 1, 2026. Owner/reviewer: Farhad. Prepared by Codex in response to “fix them and complete them.” Status: core profile-update/publication policy owner-accepted; remaining proposal reviews and six evidence gates pending.

## MVP requirement applicability and remaining review

Apply the current candidate release register: retain core presentation/sharing/manual applications/private files and basic ProjectForge; defer mail/calendar, advanced Git review/releases, advanced backlog/Sprints and YAML execution/deployment. Candidate IDs and planned verification stay intact. Mixed criteria must be scoped individually; allocation does not approve proposed numbers, priority or a complete baseline. Older 157-candidate/470-criterion evidence is historical larger-product coverage, not an MVP pass. Keep source, independent resume draft, explicit publication and actual submitted material identities distinct. Profile changes require preview/select/apply and cannot mutate publication or submitted history. Manual applications include status, next action and follow-up date without mail/calendar dependencies.

Authority: [OWNER-MVP-2026-11-04](../../01-project-planning/owner-mvp-decision-2026-11-04.md). [Candidate allocation](../03-requirements-specification/mvp-release-allocation.md).

## 1. Authority and What Is Complete

Every Q-D question now has a substantive, assessable proposed answer in its primary specification, three planned review cases and an explicit remaining gate. This replaces blank policy prompts with a reviewable candidate. It does not accept a stakeholder choice, certify legal compliance, demonstrate product functionality or close external feasibility by assertion. Scope exclusions and conditional execution obligations remain intact. No account, mail send, calendar event, job, backup or production configuration was changed.

The proposal supplies 157 proposed priorities and [470 proposed criterion locators](../06-validation-and-traceability/evidence/proposed-criterion-locators.json), preserving all existing candidate IDs/criterion wording. Scope priority and implementation order remain different. [Fresh server evidence](../06-validation-and-traceability/evidence/server-readonly-check-2026-11-01.json) is bounded read-only evidence, not a load/recovery test.

## 2. Answers and Current Dispositions

| Question / source answer | Topic | Current disposition |
| --- | --- | --- |
| [Q-D01](../03-requirements-specification/requirements-specification.md#resolution-q-d01) | Identifiers, priorities and traceability | Answer proposed |
| [Q-D02](../03-requirements-specification/user-requirements.md#resolution-q-d02) | Actor outcomes and validation | Under investigation: external/review evidence |
| [Q-D03](../03-requirements-specification/accounts-authentication-and-permissions.md#resolution-q-d03) | Account lifecycle and authentication | Answer proposed |
| [Q-D04](../03-requirements-specification/accounts-authentication-and-permissions.md#resolution-q-d04) | Resource grants and administrative boundaries | Answer proposed |
| [Q-D05](../03-requirements-specification/accounts-authentication-and-permissions.md#resolution-q-d05) | Revocation and active access | Answer proposed |
| [Q-D06](../03-requirements-specification/profiles-resumes-and-portfolio.md#resolution-q-d06) | Profile fields and composition | Answer proposed |
| [Q-D07](../03-requirements-specification/profiles-resumes-and-portfolio.md#resolution-q-d07) | Shared updates, conflicts and publication | Core behavior owner-accepted; remaining source-removal/concurrency details pending |
| [Q-D08](../03-requirements-specification/profiles-resumes-and-portfolio.md#resolution-q-d08) | Evidence formats, display and references | Answer proposed |
| [Q-D09](../03-requirements-specification/profiles-resumes-and-portfolio.md#resolution-q-d09) | English/German variants and fallback | Answer proposed |
| [Q-D10](../03-requirements-specification/pdf-and-controlled-sharing.md#resolution-q-d10) | PDF representations and downloads | Answer proposed |
| [Q-D11](../03-requirements-specification/pdf-and-controlled-sharing.md#resolution-q-d11) | Employer links and password controls | Answer proposed |
| [Q-D12](../03-requirements-specification/manual-application-management.md#resolution-q-d12) | Application fields and progress | Answer proposed |
| [Q-D13](../03-requirements-specification/manual-application-management.md#resolution-q-d13) | Actual submitted materials | Answer proposed |
| [Q-D14](../03-requirements-specification/manual-application-management.md#resolution-q-d14) | Corrections, repeated submissions and retirement | Answer proposed |
| [Q-D15](../03-requirements-specification/email-calendar-and-google-integration.md#resolution-q-d15) | Google access and applicability | Under investigation: external/review evidence |
| [Q-D16](../03-requirements-specification/email-calendar-and-google-integration.md#resolution-q-d16) | Mail operations and uncertain outcomes | Answer proposed |
| [Q-D17](../03-requirements-specification/email-calendar-and-google-integration.md#resolution-q-d17) | Calendar authority, conflicts and disconnection | Answer proposed |
| [Q-D18](../03-requirements-specification/projects-kanban-and-sprints.md#resolution-q-d18) | Work structures and workflow | Answer proposed |
| [Q-D19](../03-requirements-specification/projects-kanban-and-sprints.md#resolution-q-d19) | Sprint Backlog and incomplete work | Answer proposed |
| [Q-D20](../03-requirements-specification/projects-kanban-and-sprints.md#resolution-q-d20) | Cross-module associations and bounded reporting | Answer proposed |
| [Q-D21](../03-requirements-specification/git-hosting-and-collaboration.md#resolution-q-d21) | Real Git clients and repository contract | Answer proposed |
| [Q-D22](../03-requirements-specification/git-hosting-and-collaboration.md#resolution-q-d22) | Review, merge and release semantics | Answer proposed |
| [Q-D23](../03-requirements-specification/yaml-workflows-and-cicd.md#resolution-q-d23) | Workflow contract and enabling gate | Under investigation: external/review evidence |
| [Q-D24](../03-requirements-specification/administration-files-and-operational-behavior.md#resolution-q-d24) | File formats, quotas and accounting | Answer proposed |
| [Q-D25](../03-requirements-specification/quality-security-and-recovery-requirements.md#resolution-q-d25) | Measurable quality and supported clients | Answer proposed |
| [Q-D26](../03-requirements-specification/quality-security-and-recovery-requirements.md#resolution-q-d26) | Backup, retention and recoverability | Under investigation: external/review evidence |
| [Q-D27](../03-requirements-specification/domain-requirements-and-constraints.md#resolution-q-d27) | Operating dependencies and maintainability | Under investigation: external/review evidence |
| [Q-D28](../03-requirements-specification/requirements-specification.md#resolution-q-d28) | Forecast, work mapping and baseline candidate | Under investigation: external/review evidence |

## 3. Material Policy Choices to Review

- Controlled initial onboarding, resource-specific grants and separate administrative powers; no default administrative access to private content.
- Explicit source-update preview/apply, independent overrides, draft save versus publication, and preserved actual submitted artifacts.
- No silent language/PDF substitution; each sharing request checks current access after revocation completes, with an honest already-emitted-bytes boundary.
- Conservative proposed upload/aggregate/repository/job limits, measurable quality/recovery targets and precise test conditions; none is measured capacity or an accepted service promise.
- Explicit manual send/progress/submission actions and conflict handling; no replay of uncertain sends or implicit work completion/deployment.
- Real Git and YAML execution remain agreed capabilities; actual unsafe/unverified execution cannot be enabled or silently replaced by YAML validation.

## 4. Remaining Evidence Gates and Exact Next Actions

| Gate | Evidence required | Next action / owner |
| --- | --- | --- |
| Q-D02 actor validation | Actual review of identified proposal/scenario revision and recorded responses | Farhad reviews this candidate; record corrections/acceptance and missing actor perspectives |
| Q-D15 Google | Actual OAuth project/audience, consent/scopes, applicable verification, quota/cost and controlled authorized operation results | Identify an existing permitted project/account; inspect sanitized settings; do not request secret values in documents |
| Q-D23 isolated execution | Budget-compatible isolation/resource option and actual bounded control/cleanup/denial checks | Analyze in System Design; no untrusted execution on the existing production host to manufacture evidence |
| Q-D26 recovery | Independent destination/keys/coverage, scheduled results and isolated consistent restoration with measured RPO/RTO | Identify actual backup storage; design then rehearse safely before release; no purchase or restore is authorized by this package |
| Q-D27 operation | Delivery/renewal/worker readiness, component applicability and operating demonstrations | Scoped read-only inventory completed in RV-D06; resolve declared log-mail/OAuth gaps and missing observed worker paths, then verify actual delivery/renewal/recovery |
| Q-D28 forecast/baseline | Refined analysis/design effort, actual tracking and identified owner-reviewed candidate | Owner supplied 20 hours/week; preliminary sizing/local work mapping recorded. Refine with completed design and live tracking before an accepted forecast |

These gates are not accepted deferrals and do not permit dependent acceptance by default. A complete draft answer is different from verified access, achieved quality or an accepted baseline.

## 5. Evidence and Review Method

Read [the current question register](open-questions-and-decisions.md), source answers above and [84 proposed review cases](../04-scenarios-and-models/user-stories-and-scenarios.md#proposed-question-resolution-review-cases--november-1-2026). For each group record the actual reviewed source hash/commit, owner outcome, rationale and any compatible explicit conditions. Before closing RF findings, verify criterion-level coverage and all affected views. Existing requirements/analysis diagrams are not claimed to depict every new proposed rule; update them after the choices are accepted and during model development.

Current root-owned document checks validate IDs, local links, 28 answer sections and 84 RC locators. Proposed checks are not executed product tests. Advisor preflight returned unavailable; no advisor recommendation is claimed. Fresh SSH evidence and public-source review are the actual research completed.

## 6. Official Sources Reviewed November 1, 2026

- [Google Gmail scopes](https://developers.google.com/workspace/gmail/api/auth/scopes)
- [Google Calendar scopes](https://developers.google.com/workspace/calendar/api/auth)
- [Hetzner backup coverage](https://docs.hetzner.com/cloud/servers/backups-snapshots/overview/)
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [Laravel 12 deployment](https://laravel.com/framework/docs/12.x/deployment)
- [Docker security boundaries](https://docs.docker.com/engine/security/)

Source limits: Google lists scopes and verification conditions; it does not confirm this product's access. Hetzner documents disk-snapshot coverage excluding attached Volumes; actual backup enablement/storage remains unknown. WCAG supplies testable web criteria, not a conformance result. Laravel/Docker documentation informs compatibility/security questions, not a final engine/runner decision. Proposed product rules and numerical targets are engineering recommendations requiring owner review, not facts attributed to these sources.

## Follow-up Gate Progress — November 1, 2026

The [actual gate assessment](../06-validation-and-traceability/remaining-gate-assessment.md) records new operating findings, exclusions, a bounded documentary walkthrough and phase-specific evidence requirements. [Capacity/sizing](../../01-project-planning/11-capacity-and-preliminary-sizing.md) uses the owner's actual 20-hour answer. Current certificate/timer state is established; mail is declared log-only in the inspected .env, Google keys are absent there and standard worker paths were not observed. These observations support specific fixes but are not a production-readiness Pass. Existing proposals still await owner review. Two factual owner questions (Google project/audience and existing independent backup storage) remain unanswered at preparation time.

## Subsequent Google OAuth Clarification — November 1, 2026

The owner confirmed no OAuth project has been created. The project-existence question is answered; Q-D15 now tracks missing setup and future access evidence rather than an unknown existing project ID. Intended audience is not inferred. Weekly capacity is answered (20 hours/week); independent backup-storage availability remains the outstanding factual owner input. No parent question, provider capability or baseline is marked accepted by this clarification.

## Subsequent Backup Clarification — November 1, 2026

The owner confirmed backups have not been set up. All three recent factual owner inputs are now recorded: 20 project hours/week, OAuth not created and backups not set up. Q-D15/Q-D26 retain setup/access/recovery tasks, not unanswered requests for existing project IDs or an existing backup service name. Proposed rules/targets still require review and actual dependent evidence. No parent question, recovery capability or baseline is marked accepted by these factual clarifications.

## Accepted Core Policy — November 1, 2026

The owner explicitly accepted no automatic profile-to-resume changes, preview/select/apply, separate publication confirmation and preservation of resume-specific text/actual submitted documents. [Decision](open-questions-and-decisions.md#owner-accepted-profile-update-policy). Do not request that approval again. Current question dispositions are 21 Answer proposed, one Partially resolved (this accepted core policy), six Under investigation. Earlier summaries are historical. No full baseline or unrelated proposal is accepted.


<a id="change-and-baseline-open-questions-and-decisions"></a>

<a id="change-and-baseline-open-questions-and-decisions--heading-requirements-questions-and-decisions"></a>
# Requirements Questions and Decisions

The [selected Baseline](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/README.md) owns the current answers. Technical/policy choices are selected for the applicable MVP slice; user validation, environment, native Git security, capacity and restore still need evidence. Future-only topics are deferred and do not block MVP.

For source-status labels, mixed criteria and Must/Later priority, use the [current record rules](../03-Requirements-Specification/15-Requirement-Priority-And-Readiness.md#current-record-rules). Dated proposals below the selected policy references do not reopen resolved MVP choices.

**Key decisions and why they matter**

| Decision | Reason |
| --- | --- |
| Invite-only access and resource-specific permissions | Limit admission and keep one user's private material inaccessible to other users. [Identity](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d03) · [Grants](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d04) |
| Independent resume drafts and explicit publication | Reuse shared profile data while protecting tailored edits and controlling what employers see. [Publication policy](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d07) |
| Protected sharing and preserved submitted materials | Control what a recipient can retrieve and retain the exact materials sent for an application. [Sharing](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d11) · [Submission history](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d13) |
| Basic ProjectForge with real Git | Deliver repository transfers and scoped collaboration in the MVP. Advanced review and release functions follow later. [Git](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d21) · [MVP allocation](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d22) |

<a id="change-and-baseline-open-questions-and-decisions--heading-current-dispositions"></a>
## Current dispositions

| Question | Subject | Current disposition / selected answer |
| --- | --- | --- |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d01"></a>Q-D01 | Identifiers, priorities and criterion-level traceability | [Selected](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d01) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d02"></a>Q-D02 | Actor outcomes and user validation | [Specification selected; user validation gate](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d02) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d03"></a>Q-D03 | Identity, onboarding and account lifecycle | [Selected](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d03) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d04"></a>Q-D04 | Resource grants and administration powers | [Selected](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d04) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d05"></a>Q-D05 | Active access, credentials and revocation | [Selected](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d05) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d06"></a>Q-D06 | Professional fields and resume composition | [Selected](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d06) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d07"></a>Q-D07 | Shared updates, overrides and publication | [Selected](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d07) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d08"></a>Q-D08 | Evidence, media and external-content handling | [Selected](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d08) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d09"></a>Q-D09 | Manual language variants and fallback | [Selected](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d09) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d10"></a>Q-D10 | PDF rendition and download contracts | [Selected](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d10) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d11"></a>Q-D11 | Employer link/password lifecycle | [Selected](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d11) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d12"></a>Q-D12 | Application fields and progress | [Selected](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d12) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d13"></a>Q-D13 | Actual submitted-set capture | [Selected](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d13) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d14"></a>Q-D14 | Correction, resubmission and retained history | [Selected](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d14) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d15"></a>Q-D15 | Google access and external conditions | [Deferred after MVP](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d15) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d16"></a>Q-D16 | Mail views, drafts, send and uncertain outcomes | [Deferred after MVP](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d16) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d17"></a>Q-D17 | Calendar, synchronization and disconnection | [Deferred after MVP](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d17) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d18"></a>Q-D18 | Work structures, fields and workflows | [Selected MVP slice](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d18) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d19"></a>Q-D19 | Sprint Backlog, completion and end behavior | [Deferred after MVP](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d19) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d20"></a>Q-D20 | Cross-module links, reporting and automation | [Selected MVP slice](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d20) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d21"></a>Q-D21 | Real Git clients, credentials and repository policy | [Selected design; capability gate](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d21) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d22"></a>Q-D22 | Git review, merge, tracking and releases | [Selected issues; advanced Git deferred](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d22) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d23"></a>Q-D23 | Workflow contract, isolation, secrets and target controls | [Deferred after MVP](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d23) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d24"></a>Q-D24 | Effective file policy, quotas and administrative evidence | [Selected; capacity gate](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d24) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d25"></a>Q-D25 | Quantitative quality, client and accessibility targets | [Selected targets; measurement gate](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d25) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d26"></a>Q-D26 | Backup, retention, consistent recovery and restored access | [Selected design; restore gate](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d26) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d27"></a>Q-D27 | Operating dependencies, applicability and maintenance | [Selected; operational inputs gate](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d27) |
| <a id="change-and-baseline-open-questions-and-decisions--id-q-d28"></a>Q-D28 | Forecast, downstream reconciliation and baseline candidate | [Selected Baseline; no delivery forecast](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md#q-d28) |

<a id="change-and-baseline-open-questions-and-decisions--id-owner-accepted-profile-update-policy"></a>
<a id="change-and-baseline-open-questions-and-decisions--heading-owner-accepted-profile-update-policy"></a>
## Owner-accepted Profile Update Policy

Farhad explicitly accepted this behavior on November 1, 2026: profile changes do not automatically alter existing resumes; preview/select/apply preserves independent overrides; publication requires a separate confirmation; actual previously submitted materials remain unchanged. This settled policy must not be reopened as a generic pending question. [Current realization](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/technical-decisions.md#t05--data-publication-and-durable-history).

<a id="change-and-baseline-open-questions-and-decisions--heading-known-setup-facts-and-remaining-evidence"></a>
## Known setup facts and remaining evidence

Do not repeatedly ask those same questions. Actual backup destination, consistent capture and demonstrated restore are still operational gates; personal Google integration is after MVP. Runtime compatibility and host capacity need actual checks. These facts do not assert product tests, actor acceptance or Release readiness.

[Gate definitions](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/implementation-sequence.md#gate-register) · [Review criteria](04-Requirements-Review-And-Baseline-Criteria.md#change-and-baseline-requirements-review-and-baseline-criteria) · [Change control](02-Requirements-Change-Control.md#change-and-baseline-change-control)

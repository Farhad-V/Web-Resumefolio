# Resumefolio — Remaining Gate Assessment

Date: November 1, 2026. Activity: RV-D06. Scope: requirements-stage clarification, bounded read-only operating checks, public-source investigation and preliminary capacity/sizing. No production configuration, installed packages, accounts, job execution or external messages changed.

## MVP requirement applicability and remaining review

Apply the current candidate release register: retain core presentation/sharing/manual applications/private files and basic ProjectForge; defer mail/calendar, advanced Git review/releases, advanced backlog/Sprints and YAML execution/deployment. Candidate IDs and planned verification stay intact. Mixed criteria must be scoped individually; allocation does not approve proposed numbers, priority or a complete baseline. Older 157-candidate/470-criterion evidence is historical larger-product coverage, not an MVP pass. Keep source, independent resume draft, explicit publication and actual submitted material identities distinct. Profile changes require preview/select/apply and cannot mutate publication or submitted history. Manual applications include status, next action and follow-up date without mail/calendar dependencies.

Authority: [OWNER-MVP-2026-11-04](../../01-project-planning/owner-mvp-decision-2026-11-04.md). [Candidate allocation](../03-requirements-specification/mvp-release-allocation.md).

## 1. What Was Answered

| Topic | Actual finding | What it establishes | Remaining limit |
| --- | --- | --- | --- |
| Weekly capacity | Owner stated 20 project hours/week | Numerical current planning input is answered | Final effort/forecast needs design and re-estimation |
| Mail declaration | Deployed .env declares log transport; no cached config file found; selected SMTP credentials absent | No SMTP delivery setup is evidenced by the inspected declarations | Process/service environment may differ; no mail sent or received |
| Google declaration | Selected GOOGLE_CLIENT_ID/SECRET/REDIRECT keys absent | This deployed .env does not supply that common OAuth configuration | External project/alternate config/account state unknown; owner question pending |
| Certificate | Live TLS verification succeeded; certificate ends January 7, 2027; certbot.timer enabled/active and one renewal definition found | Current certificate and automated-renewal configuration subset observed | No renewal challenge/reload/recovery test performed |
| Background processing | No matching artisan worker/scheduler processes at sample time; no schedule entries in root/www-data crontabs | These particular execution paths were not observed | Other users, timers, managers and external scheduling not excluded |
| Backup | No Restic/Borg executables found; selected timer match is dpkg-db-backup | That timer is not evidence of application backup coverage | Provider backups/Storage Box/other destinations unknown; owner question pending |
| Execution | Docker/Podman not found; /dev/kvm absent | No evaluated runner is currently established by these checks | Runtime installation, limits and safe execution remain design/control work |
| License inventory | Lock metadata identifies LGPL-family dompdf components and multi-license Nette declarations | Exact declared licenses can now be examined | License obligations, chosen licensing paths and all distribution/font/assets remain unreviewed |
| Tracking | Local PBI index available; GitHub read returned access/empty-data limitations | Actual existing local work references available | Live board/issue evidence not available through current connector |

Sanitized machine-readable evidence: [operating check](evidence/operating-check-2026-11-01.json). Password/token values, private key material, .env contents and private email addresses are not recorded.

## 2. Separate Requirements, Design and Release Evidence

My earlier six-gate summary did not make the stage distinction clear enough. A requirement can specify restoration/control outcomes before the product exists; it cannot claim those outcomes were achieved. Actual restore drills and implemented control checks are not prerequisites for merely drafting requirements. Existing mandatory gates still apply before the dependent commitment.

| Question | Requirements-stage outcome needed | Design / access prerequisite | Later verification |
| --- | --- | --- | --- |
| Q-D02 actor validation | Owner/actor disposition on the exact proposed workflows/criteria | Resolved inputs before accepting affected models | Usability/outcome verification of actual implementation |
| Q-D15 Google | Reviewed operation/privacy/scope and disconnected/unknown-outcome contracts | Actual app/audience/consent/applicable verification and access before dependent acceptance/development | Controlled authorized read/draft/send/calendar checks; no send performed now |
| Q-D23 isolated execution | Supported YAML/authority/result/limit requirements; real execution retained | Budget-compatible isolation/resource findings before dependent M-03 acceptance/enabling | Denial/resource/cleanup and actual job checks before M-08 |
| Q-D26 recovery | Reviewed coverage, proposed RPO/RTO/retention and restore semantics | Actual independent storage/key/consistency approach before recovery-design acceptance | Isolated usable restore and target measurement before M-09 |
| Q-D27 operation | Delivery, renewal, workers, maintenance and applicability obligations | Compatible actual arrangements/components before dependent design/deployment acceptance | Actual notification/renewal/maintenance/recovery checks at readiness |
| Q-D28 forecast | Confirmed 20-hour input and criteria/work linkage approach | Initial analysis/design and decisive feasibility before accepted forecast/coding | Re-estimate using actual execution outcomes; baseline owner decision remains distinct |

None of these rows is an automatically accepted deferral. Pending owner choices still require review, and a feasibility conflict cannot be waived by moving a label to a later phase.

## 3. CI/CD Options After the Infrastructure Check

Hetzner's [official Cloud FAQ](https://docs.hetzner.com/cloud/servers/faq/) states nested virtualization is not available on Cloud servers; the inspected guest has no /dev/kvm. Therefore nested KVM/microVM execution on this existing VPS is not a supported working assumption.

| Candidate | Disposition now | Evidence still needed |
| --- | --- | --- |
| Arbitrary host shell / privileged container / Docker socket exposed to jobs | Reject as a candidate for the stated untrusted-code boundary | It does not meet the proposed separation of production host/data/secrets |
| Nested KVM/microVM on the current Cloud VPS | Exclude from current candidate shortlist | Provider limitation and missing guest device do not support it |
| Userspace isolation such as gVisor with a non-KVM platform and scoped resource/network/filesystem controls | Research candidate only; no runtime selected or installed | Application/syscall compatibility, operating burden, quotas, policy enforcement, cross-job separation, cleanup and representative combined resource use |
| A separately isolated existing execution host/service | Conditional candidate if actually available within the owner's budget | Actual availability/access, cost, lifecycle, secret/data boundaries and job result integration |

gVisor's [project documentation](https://gvisor.dev/docs/) and [security model](https://gvisor.dev/docs/architecture_guide/security/) describe a userspace application-kernel approach and its threat boundaries. This is a feasibility lead, not proof of a secure/suitable configuration on the inspected server. Do not buy a host, install a runner or execute untrusted workloads on production without a justified design and applicable authorization. If no budget-compatible option meets the agreed requirement, expose the conflict for an actual owner decision; YAML validation is not completion of real execution.

## 4. Bounded Documentary Walkthrough

These are actual reasoned text comparisons by Codex, not product tests or stakeholder acceptance. Inputs are the proposed source answers already saved on November 1 and their linked existing scope/criteria.

| Compared proposed rules | Observed consistency | Remaining work |
| --- | --- | --- |
| Q-D05/Q-D11 revocation versus PDF-D06 | Subsequent authorization rejects a disabled/rotated context; already-emitted bytes are outside recall | Owner disposition and eventual enforcement checks |
| Q-D07/Q-D10 publication versus PRP-D03/D04 and PDF-D07 | Source edits do not silently publish; current generated artifact binds the intended revision | Complete source/reference retirement edge cases and cross-view models |
| Q-D09/Q-D10 language versus PRP-D07/PDF-D02/D03 | Missing/disabled variants do not silently substitute another language | Owner confirmation of fallback/completeness rules and actual UI checks |
| Q-D13/Q-D14 history versus APP-D05–D07 | Actual captured artifact identity survives live edits; missing captures remain incomplete | Retention/applicability review, model details and restore checks |
| Q-D04/Q-D18/Q-D21 resource grants | Project, repository and private mail/profile grants remain independent | Full action matrix and criterion-level negative-case mapping |
| Q-D19/Q-D20 Sprint/work versus PKS-D07–D11 | Item acceptance differs from task completion; links do not automatically send/merge/deploy | Owner workflow review and complete state/activity models  **Advanced paths after MVP; any retained core/basic path follows the release register.** |

No claim is made that all 470 criteria or 84 planned cases were semantically exhausted. RF-D01–RF-D05 remain open until their own evidence and review conditions are met.

## 5. Concrete Remaining Inputs

The owner has answered weekly capacity: **20 hours**. Two factual questions were submitted and had no answer at preparation time: the intended Google Cloud OAuth project/audience (or not created), and any existing independent backup storage (or none/unknown). Do not infer answers from silence or .env absence. Existing signed-in provider-console tabs were not available through browser inventory, so account-level inspection could not be completed here.

The 22 other question groups have substantive proposals in the [answer review package](../07-change-and-baseline/requirements-answer-review.md). Actual acceptance of those choices is still not recorded. Owner review of this specific candidate can record accept/correct per group; neither the request for assistance nor a documentary walkthrough silently accepts new security/retention/numerical policy.

## 6. Public Sources and Limits

- [Laravel mail log driver](https://laravel.com/framework/docs/12.x/mail#log-driver): explains the declared transport; does not independently verify all runtime configuration.
- [Laravel scheduler](https://laravel.com/framework/docs/12.x/scheduling#running-the-scheduler): explains a standard trigger path; other scheduling arrangements remain possible.
- [Laravel queue workers](https://laravel.com/framework/docs/12.x/queues#supervisor-configuration): explains sustained worker supervision; no manager installed by this review.
- [Hetzner Cloud FAQ](https://docs.hetzner.com/cloud/servers/faq/): shared resources and nested-virtualization limitation.
- [gVisor documentation](https://gvisor.dev/docs/): candidate mechanism characteristics; no actual suitability result.

Reviewed November 1, 2026. No legal compliance conclusion, resource purchase, integration capability Pass or completed restore is inferred. [Preliminary sizing](../../01-project-planning/11-capacity-and-preliminary-sizing.md) uses the new capacity input and explicitly retains uncertainty.

## Subsequent Actual Owner Answer — Google OAuth

November 1, 2026: the owner answered “I have not created OAuth.” The earlier preparation-time unknown is now answered: intended OAuth setup has not been created. This resolves the factual existence input, not Q-D15's complete access/feasibility gate. Next work is intended-audience definition and authorized setup, followed by applicable provider review and controlled operation checks. Backup-storage availability remains unanswered; do not infer none. No external configuration changed.

## Subsequent Actual Owner Answer — Backups

November 1, 2026: the owner stated “No, I haven’t set up backups.” The earlier unanswered setup question is now answered. Record an unmet application-backup prerequisite; do not claim configured/tested recovery. Actual provider backup enablement was not independently inspected. Destination availability, coverage, keys, scheduling, reviewed targets and later isolated restoration remain Q-D26/DEP-05 work. Both recent setup questions are answered: OAuth not created and backups not set up. The owner also confirmed 20 project hours/week. No setup operation was performed by this clarification.

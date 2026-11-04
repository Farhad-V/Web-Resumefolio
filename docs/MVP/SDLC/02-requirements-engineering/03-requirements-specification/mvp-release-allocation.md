# MVP Candidate Release Allocation

## Current implementation baseline — November 4, 2026

[BL-MVP-2026-11-04.1](../../../baseline/README.md) selects the MVP technical mechanisms, numerical policies, priorities and requirement/criterion dispositions under Farhad’s explicit delegation. It supersedes earlier Proposed/pending mechanism and whole-baseline statements below for MVP design input. Future clauses and dated evidence remain separate. Runtime/actor validation, credentials, Git isolation, capacity and backup/restore still require the named implementation/Release gates; this update reports no product test Pass.

### Prior source material and rationale (superseded where this Baseline selects a different MVP choice)

Updated November 4, 2026 from [OWNER-MVP-2026-11-04](../../01-project-planning/owner-mvp-decision-2026-11-04.md). This is release allocation, not priority approval or acceptance of all proposed numerical policies/criteria. Candidate IDs and original source criteria are preserved. Mixed records require criterion-level separation before implementation acceptance.

Core: dashboard, invited accounts, profile/resumes/portfolio, PDFs/protected sharing, manual applications and private same-server My Files & Media. ProjectForge: separate user-scoped API system, real Git transfers/permissions/file-history, issues/simple Kanban. No future requirement blocks MVP merely because it was formerly in Version 1.

| Candidate | Retained subject | Release allocation |
| --- | --- | --- |
| [ACC-D01](accounts-authentication-and-permissions.md#acc-d01-individual-account-context) | Individual Account Context | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [ACC-D02](accounts-authentication-and-permissions.md#acc-d02-unified-sign-in-across-authorized-sections) | Unified Sign-in Across Authorized Sections | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [ACC-D03](accounts-authentication-and-permissions.md#acc-d03-resource-and-operation-authorization) | Resource and Operation Authorization | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [ACC-D04](accounts-authentication-and-permissions.md#acc-d04-cross-user-private-data-isolation) | Cross-user Private-data Isolation | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [ACC-D05](accounts-authentication-and-permissions.md#acc-d05-limited-collaboration-authority) | Limited Collaboration Authority | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [ACC-D06](accounts-authentication-and-permissions.md#acc-d06-employer-access-without-a-viewer-account) | Employer Access Without a Viewer Account | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [ACC-D07](accounts-authentication-and-permissions.md#acc-d07-protected-shared-file-and-pdf-retrieval) | Protected Shared File and PDF Retrieval | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [ACC-D08](accounts-authentication-and-permissions.md#acc-d08-owner-control-of-employer-link-access) | Owner Control of Employer-link Access | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [ACC-D09](accounts-authentication-and-permissions.md#acc-d09-explicit-administrative-powers) | Explicit Administrative Powers | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [ACC-D10](accounts-authentication-and-permissions.md#acc-d10-authorization-of-access-grant-changes) | Authorization of Access-grant Changes | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [ACC-D11](accounts-authentication-and-permissions.md#acc-d11-no-authentication-bypass-on-deliveryprovider-failure) | No Authentication Bypass on Delivery/Provider Failure | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [ACC-D12](accounts-authentication-and-permissions.md#acc-d12-end-of-access-and-lifecycle-enforcement) | End-of-access and Lifecycle Enforcement | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [AFO-D01](administration-files-and-operational-behavior.md#afo-d01-owner-configurable-upload-and-storage-policy) | Owner-configurable Upload and Storage Policy | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [AFO-D02](administration-files-and-operational-behavior.md#afo-d02-policy-consistent-with-evaluated-infrastructure) | Policy Consistent with Evaluated Infrastructure | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [AFO-D03](administration-files-and-operational-behavior.md#afo-d03-per-file-admission-limit) | Per-file Admission Limit | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [AFO-D04](administration-files-and-operational-behavior.md#afo-d04-aggregate-quota-and-concurrent-admission) | Aggregate Quota and Concurrent Admission | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [AFO-D05](administration-files-and-operational-behavior.md#afo-d05-supported-content-and-validation) | Supported Content and Validation | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [AFO-D06](administration-files-and-operational-behavior.md#afo-d06-file-resource-authorization-and-isolation) | File-resource Authorization and Isolation | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [AFO-D07](administration-files-and-operational-behavior.md#afo-d07-truthful-completion-and-interrupted-operation-handling) | Truthful Completion and Interrupted-operation Handling | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [AFO-D08](administration-files-and-operational-behavior.md#afo-d08-safe-replacement-and-lifecycle-effects) | Safe Replacement and Lifecycle Effects | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [AFO-D09](administration-files-and-operational-behavior.md#afo-d09-operational-outcomes-and-capacity-warnings) | Operational Outcomes and Capacity Warnings | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [AFO-D10](administration-files-and-operational-behavior.md#afo-d10-administrative-operation-evidence) | Administrative Operation Evidence | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [AFO-D11](administration-files-and-operational-behavior.md#afo-d11-bounded-cleanup-and-storage-reclamation) | Bounded Cleanup and Storage Reclamation | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [AFO-D12](administration-files-and-operational-behavior.md#afo-d12-version-specific-operational-guidance-and-readiness) | Version-specific Operational Guidance and Readiness | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [BIZ-D01](business-requirements.md#biz-d01-reusable-information-and-relevant-professional-presentation) | Reusable Information and Relevant Professional Presentation | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [BIZ-D02](business-requirements.md#biz-d02-controlled-disclosure-of-professional-information) | Controlled Disclosure of Professional Information | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [BIZ-D03](business-requirements.md#biz-d03-traceable-manual-applications-and-preserved-submission-history) | Traceable Manual Applications and Preserved Submission History | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [BIZ-D04](business-requirements.md#biz-d04-coordinated-authorized-work-in-one-product-experience) | Coordinated Authorized Work in One Product Experience | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [BIZ-D05](business-requirements.md#biz-d05-usable-maintainable-and-recoverable-initial-operation) | Usable, Maintainable and Recoverable Initial Operation | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [BRL-D01](business-rules-and-data-lifecycle.md#brl-d01-resource-specific-authority) | Resource-specific Authority | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [BRL-D02](business-rules-and-data-lifecycle.md#brl-d02-shared-information-and-independent-tailoring) | Shared Information and Independent Tailoring | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [BRL-D03](business-rules-and-data-lifecycle.md#brl-d03-explicit-shared-content-and-download-availability) | Explicit Shared Content and Download Availability | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [BRL-D04](business-rules-and-data-lifecycle.md#brl-d04-access-changes-govern-subsequent-retrieval) | Access Changes Govern Subsequent Retrieval | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [BRL-D05](business-rules-and-data-lifecycle.md#brl-d05-preserve-actual-submitted-materials) | Preserve Actual Submitted Materials | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [BRL-D06](business-rules-and-data-lifecycle.md#brl-d06-validation-and-truthful-state-changes) | Validation and Truthful State Changes | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [BRL-D07](business-rules-and-data-lifecycle.md#brl-d07-explicit-provider-synchronization-authority) | Explicit Provider Synchronization Authority | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [BRL-D08](business-rules-and-data-lifecycle.md#brl-d08-reference-aware-retirement) | Reference-aware Retirement | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [BRL-D09](business-rules-and-data-lifecycle.md#brl-d09-recovery-preserves-defined-business-consistency) | Recovery Preserves Defined Business Consistency | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [BRL-D10](business-rules-and-data-lifecycle.md#brl-d10-defined-language-and-time-meaning) | Defined Language and Time Meaning | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [DOM-D01](domain-requirements-and-constraints.md#dom-d01-consistent-professional-information-meaning) | Consistent Professional-information Meaning | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [DOM-D02](domain-requirements-and-constraints.md#dom-d02-application-history-represents-actual-submitted-material) | Application History Represents Actual Submitted Material | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [DOM-D03](domain-requirements-and-constraints.md#dom-d03-authorization-follows-the-resource-and-operation) | Authorization Follows the Resource and Operation | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [DOM-D04](domain-requirements-and-constraints.md#dom-d04-explicit-human-authored-language-and-application-work) | Explicit Human-authored Language and Application Work | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [DOM-D05](domain-requirements-and-constraints.md#dom-d05-explicit-external-service-applicability) | Explicit External-service Applicability | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [DOM-D06](domain-requirements-and-constraints.md#dom-d06-establish-information-handling-applicability) | Establish Information-handling Applicability | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [DOM-D07](domain-requirements-and-constraints.md#dom-d07-verify-reuse-and-licensing-before-adoption) | Verify Reuse and Licensing Before Adoption | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [DOM-D08](domain-requirements-and-constraints.md#dom-d08-evidence-based-operation-within-constraints) | Evidence-based Operation Within Constraints | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [EGC-D01](email-calendar-and-google-integration.md#egc-d01-authorized-connection-and-account-context) | Authorized Connection and Account Context | Deferred after MVP |
| [EGC-D02](email-calendar-and-google-integration.md#egc-d02-justified-permissions-and-private-resource-isolation) | Justified Permissions and Private-resource Isolation | Deferred after MVP |
| [EGC-D03](email-calendar-and-google-integration.md#egc-d03-read-authorized-correspondence) | Read Authorized Correspondence | Deferred after MVP |
| [EGC-D04](email-calendar-and-google-integration.md#egc-d04-manual-compose-and-draft-handling) | Manual Compose and Draft Handling | Deferred after MVP |
| [EGC-D05](email-calendar-and-google-integration.md#egc-d05-deliberate-send-and-truthful-outcome) | Deliberate Send and Truthful Outcome | Deferred after MVP |
| [EGC-D06](email-calendar-and-google-integration.md#egc-d06-reply-context-and-conversation-association) | Reply Context and Conversation Association | Deferred after MVP |
| [EGC-D07](email-calendar-and-google-integration.md#egc-d07-calendar-activities-and-time-meaning) | Calendar Activities and Time Meaning | Deferred after MVP |
| [EGC-D08](email-calendar-and-google-integration.md#egc-d08-explicit-synchronization-contract) | Explicit Synchronization Contract | Deferred after MVP |
| [EGC-D09](email-calendar-and-google-integration.md#egc-d09-application-relationships-preserve-boundaries) | Application Relationships Preserve Boundaries | Deferred after MVP |
| [EGC-D10](email-calendar-and-google-integration.md#egc-d10-reminders-and-notification-outcomes) | Reminders and Notification Outcomes | Deferred after MVP |
| [EGC-D11](email-calendar-and-google-integration.md#egc-d11-disconnect-revocation-and-reconnect) | Disconnect, Revocation and Reconnect | Deferred after MVP |
| [EGC-D12](email-calendar-and-google-integration.md#egc-d12-bounded-failures-recovery-and-feasibility-evidence) | Bounded Failures, Recovery and Feasibility Evidence | Deferred after MVP |
| [EIF-D01](external-interface-requirements.md#eif-d01-reviewable-interface-contracts) | Reviewable Interface Contracts | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [EIF-D02](external-interface-requirements.md#eif-d02-clear-operable-user-interaction) | Clear, Operable User Interaction | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [EIF-D03](external-interface-requirements.md#eif-d03-consistent-authorization-across-entry-paths) | Consistent Authorization Across Entry Paths | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [EIF-D04](external-interface-requirements.md#eif-d04-protected-file-and-pdf-exchange) | Protected File and PDF Exchange | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [EIF-D05](external-interface-requirements.md#eif-d05-explicit-google-provider-contracts) | Explicit Google Provider Contracts | Deferred after MVP |
| [EIF-D06](external-interface-requirements.md#eif-d06-real-git-client-interoperability) | Real Git-client Interoperability | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [EIF-D07](external-interface-requirements.md#eif-d07-bounded-workflow-and-deployment-interfaces) | Bounded Workflow and Deployment Interfaces | Deferred after MVP |
| [EIF-D08](external-interface-requirements.md#eif-d08-operation-specific-failure-and-repetition-semantics) | Operation-specific Failure and Repetition Semantics | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [EIF-D09](external-interface-requirements.md#eif-d09-operational-configuration-and-recovery-boundaries) | Operational Configuration and Recovery Boundaries | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [EIF-D10](external-interface-requirements.md#eif-d10-consistent-exchange-meaning-and-lifecycle) | Consistent Exchange Meaning and Lifecycle | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [GIT-D01](git-hosting-and-collaboration.md#git-d01-repository-creation-and-ownership) | Repository Creation and Ownership | MVP — ProjectForge |
| [GIT-D02](git-hosting-and-collaboration.md#git-d02-repository-and-ref-authorization) | Repository and Ref Authorization | MVP — ProjectForge |
| [GIT-D03](git-hosting-and-collaboration.md#git-d03-real-clone-fetch-pull-and-push) | Real Clone, Fetch, Pull and Push | MVP — ProjectForge |
| [GIT-D04](git-hosting-and-collaboration.md#git-d04-branches-files-and-history-browsing) | Branches, Files and History Browsing | Split — MVP file/history browsing and normal Git refs; advanced branch management deferred |
| [GIT-D05](git-hosting-and-collaboration.md#git-d05-fork-provenance-and-permission-boundaries) | Fork Provenance and Permission Boundaries | Deferred after MVP — advanced Git collaboration |
| [GIT-D06](git-hosting-and-collaboration.md#git-d06-pull-requests-comments-and-review) | Pull Requests, Comments and Review | Deferred after MVP — advanced Git collaboration |
| [GIT-D07](git-hosting-and-collaboration.md#git-d07-controlled-merge-and-conflict-outcomes) | Controlled Merge and Conflict Outcomes | Deferred after MVP — advanced Git collaboration |
| [GIT-D08](git-hosting-and-collaboration.md#git-d08-issues-and-milestones) | Issues and Milestones | Split — MVP ProjectForge issues; milestones deferred |
| [GIT-D09](git-hosting-and-collaboration.md#git-d09-tags-and-releases) | Tags and Releases | Deferred after MVP — advanced Git collaboration |
| [GIT-D10](git-hosting-and-collaboration.md#git-d10-lifecycle-capacity-and-recovery) | Lifecycle, Capacity and Recovery | MVP — ProjectForge |
| [APP-D01](manual-application-management.md#app-d01-company-and-opportunity-context) | Company and Opportunity Context | MVP — Resumefolio core |
| [APP-D02](manual-application-management.md#app-d02-relevant-resume-association) | Relevant Resume Association | MVP — Resumefolio core |
| [APP-D03](manual-application-management.md#app-d03-manually-authored-cover-letter) | Manually Authored Cover Letter | MVP — Resumefolio core |
| [APP-D04](manual-application-management.md#app-d04-explicit-progress-states-and-transitions) | Explicit Progress States and Transitions | MVP — Resumefolio core |
| [APP-D05](manual-application-management.md#app-d05-user-directed-submission-recording) | User-directed Submission Recording | MVP — Resumefolio core |
| [APP-D06](manual-application-management.md#app-d06-preserved-actual-submitted-copies) | Preserved Actual Submitted Copies | MVP — Resumefolio core |
| [APP-D07](manual-application-management.md#app-d07-correction-and-repeated-submissions) | Correction and Repeated Submissions | MVP — Resumefolio core |
| [APP-D08](manual-application-management.md#app-d08-correspondence-calendar-and-follow-up-links) | Correspondence, Calendar and Follow-up Links | Split — MVP manual next action/follow-up date; mail/calendar association deferred |
| [APP-D09](manual-application-management.md#app-d09-private-access-archive-and-recovery) | Private Access, Archive and Recovery | MVP — Resumefolio core |
| [PDF-D01](pdf-and-controlled-sharing.md#pdf-d01-generated-resume-pdf) | Generated Resume PDF | MVP — Resumefolio core |
| [PDF-D02](pdf-and-controlled-sharing.md#pdf-d02-uploaded-pdf-and-language-identity) | Uploaded PDF and Language Identity | MVP — Resumefolio core |
| [PDF-D03](pdf-and-controlled-sharing.md#pdf-d03-per-resume-download-choices) | Per-resume Download Choices | MVP — Resumefolio core |
| [PDF-D04](pdf-and-controlled-sharing.md#pdf-d04-scoped-password-protected-employer-access) | Scoped Password-protected Employer Access | MVP — Resumefolio core |
| [PDF-D05](pdf-and-controlled-sharing.md#pdf-d05-direct-file-and-pdf-authorization) | Direct File and PDF Authorization | MVP — Resumefolio core |
| [PDF-D06](pdf-and-controlled-sharing.md#pdf-d06-owner-password-and-link-controls) | Owner Password and Link Controls | MVP — Resumefolio core |
| [PDF-D07](pdf-and-controlled-sharing.md#pdf-d07-explicit-live-revision-and-rendition-behavior) | Explicit Live-revision and Rendition Behavior | MVP — Resumefolio core |
| [PDF-D08](pdf-and-controlled-sharing.md#pdf-d08-downloaded-copy-and-submission-distinctions) | Downloaded-copy and Submission Distinctions | MVP — Resumefolio core |
| [PDF-D09](pdf-and-controlled-sharing.md#pdf-d09-failure-safe-processing-and-content-handling) | Failure-safe Processing and Content Handling | MVP — Resumefolio core |
| [PDF-D10](pdf-and-controlled-sharing.md#pdf-d10-reference-aware-retirement-and-recovery) | Reference-aware Retirement and Recovery | MVP — Resumefolio core |
| [PRP-D01](profiles-resumes-and-portfolio.md#prp-d01-reusable-professional-information) | Reusable Professional Information | MVP — Resumefolio core |
| [PRP-D02](profiles-resumes-and-portfolio.md#prp-d02-opportunity-specific-resume-composition) | Opportunity-specific Resume Composition | MVP — Resumefolio core |
| [PRP-D03](profiles-resumes-and-portfolio.md#prp-d03-independent-selections-layouts-and-overrides) | Independent Selections, Layouts and Overrides | MVP — Resumefolio core |
| [PRP-D04](profiles-resumes-and-portfolio.md#prp-d04-explicit-shared-source-update-rules) | Explicit Shared-source Update Rules | MVP — Resumefolio core |
| [PRP-D05](profiles-resumes-and-portfolio.md#prp-d05-skill-and-project-evidence-management) | Skill and Project Evidence Management | MVP — Resumefolio core |
| [PRP-D06](profiles-resumes-and-portfolio.md#prp-d06-per-resume-evidence-selection-and-disclosure) | Per-resume Evidence Selection and Disclosure | MVP — Resumefolio core |
| [PRP-D07](profiles-resumes-and-portfolio.md#prp-d07-manually-maintained-english-and-german-content) | Manually Maintained English and German Content | MVP — Resumefolio core |
| [PRP-D08](profiles-resumes-and-portfolio.md#prp-d08-clear-presentation-and-rendition-boundaries) | Clear Presentation and Rendition Boundaries | MVP — Resumefolio core |
| [PRP-D09](profiles-resumes-and-portfolio.md#prp-d09-safe-content-admission-and-truthful-save-outcomes) | Safe Content Admission and Truthful Save Outcomes | MVP — Resumefolio core |
| [PRP-D10](profiles-resumes-and-portfolio.md#prp-d10-reference-aware-retirement-and-historical-independence) | Reference-aware Retirement and Historical Independence | MVP — Resumefolio core |
| [PKS-D01](projects-kanban-and-sprints.md#pks-d01-project-and-board-context) | Project and Board Context | Split — MVP ProjectForge simple Kanban and necessary permissions/lifecycle; advanced configuration deferred |
| [PKS-D02](projects-kanban-and-sprints.md#pks-d02-configurable-columns-and-valid-work-movement) | Configurable Columns and Valid Work Movement | Split — MVP ProjectForge simple Kanban and necessary permissions/lifecycle; advanced configuration deferred |
| [PKS-D03](projects-kanban-and-sprints.md#pks-d03-product-backlog-and-item-definition) | Product Backlog and Item Definition | Deferred after MVP — advanced work planning/reporting |
| [PKS-D04](projects-kanban-and-sprints.md#pks-d04-item-refinement-and-task-relationships) | Item Refinement and Task Relationships | Deferred after MVP — advanced work planning/reporting |
| [PKS-D05](projects-kanban-and-sprints.md#pks-d05-assignment-priority-and-due-date-handling) | Assignment, Priority and Due-date Handling | Split — MVP ProjectForge simple Kanban and necessary permissions/lifecycle; advanced configuration deferred |
| [PKS-D06](projects-kanban-and-sprints.md#pks-d06-scoped-collaboration-and-membership-changes) | Scoped Collaboration and Membership Changes | Split — MVP ProjectForge simple Kanban and necessary permissions/lifecycle; advanced configuration deferred |
| [PKS-D07](projects-kanban-and-sprints.md#pks-d07-sprint-goal-and-selected-backlog-items) | Sprint Goal and Selected Backlog Items | Deferred after MVP — advanced work planning/reporting |
| [PKS-D08](projects-kanban-and-sprints.md#pks-d08-one-coherent-sprint-backlog) | One Coherent Sprint Backlog | Deferred after MVP — advanced work planning/reporting |
| [PKS-D09](projects-kanban-and-sprints.md#pks-d09-explicit-completion-and-sprint-end-outcomes) | Explicit Completion and Sprint-end Outcomes | Deferred after MVP — advanced work planning/reporting |
| [PKS-D10](projects-kanban-and-sprints.md#pks-d10-deliberate-cross-module-links-reports-and-automation) | Deliberate Cross-module Links, Reports and Automation | Deferred after MVP — advanced work planning/reporting |
| [PKS-D11](projects-kanban-and-sprints.md#pks-d11-truthful-changes-retirement-and-recovery) | Truthful Changes, Retirement and Recovery | Split — MVP ProjectForge simple Kanban and necessary permissions/lifecycle; advanced configuration deferred |
| [QSR-D01](quality-security-and-recovery-requirements.md#qsr-d01-response-performance-under-defined-workloads) | Response Performance Under Defined Workloads | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [QSR-D02](quality-security-and-recovery-requirements.md#qsr-d02-combined-capacity-and-bounded-resource-use) | Combined Capacity and Bounded Resource Use | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [QSR-D03](quality-security-and-recovery-requirements.md#qsr-d03-operable-accessible-and-compatible-interaction) | Operable, Accessible and Compatible Interaction | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [QSR-D04](quality-security-and-recovery-requirements.md#qsr-d04-observable-availability-and-controlled-degradation) | Observable Availability and Controlled Degradation | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [QSR-D05](quality-security-and-recovery-requirements.md#qsr-d05-identity-resource-isolation-and-changed-access) | Identity, Resource Isolation and Changed Access | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [QSR-D06](quality-security-and-recovery-requirements.md#qsr-d06-sensitive-information-and-secret-protection) | Sensitive Information and Secret Protection | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [QSR-D07](quality-security-and-recovery-requirements.md#qsr-d07-safe-content-and-untrusted-execution-boundaries) | Safe Content and Untrusted Execution Boundaries | Split — MVP safe content; untrusted workflow execution deferred |
| [QSR-D08](quality-security-and-recovery-requirements.md#qsr-d08-data-integrity-and-truthful-completion) | Data Integrity and Truthful Completion | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [QSR-D09](quality-security-and-recovery-requirements.md#qsr-d09-deliberate-retention-and-reference-aware-removal) | Deliberate Retention and Reference-aware Removal | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [QSR-D10](quality-security-and-recovery-requirements.md#qsr-d10-defined-protected-and-observable-backups) | Defined, Protected and Observable Backups | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [QSR-D11](quality-security-and-recovery-requirements.md#qsr-d11-demonstrated-restoration-and-recovery-targets) | Demonstrated Restoration and Recovery Targets | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [QSR-D12](quality-security-and-recovery-requirements.md#qsr-d12-safe-restored-access-and-external-state-reconciliation) | Safe Restored Access and External-state Reconciliation | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [QSR-D13](quality-security-and-recovery-requirements.md#qsr-d13-useful-restricted-operational-evidence) | Useful, Restricted Operational Evidence | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [QSR-D14](quality-security-and-recovery-requirements.md#qsr-d14-maintainable-verifiable-and-recoverable-changes) | Maintainable, Verifiable and Recoverable Changes | MVP foundation where used by core/basic ProjectForge; future-domain clauses deferred |
| [USR-D01](user-requirements.md#usr-d01-reuse-and-tailor-professional-information) | Reuse and Tailor Professional Information | MVP — Resumefolio core |
| [USR-D02](user-requirements.md#usr-d02-control-pdf-and-employer-sharing) | Control PDF and Employer Sharing | MVP — Resumefolio core |
| [USR-D03](user-requirements.md#usr-d03-view-intended-professional-material-without-an-account) | View Intended Professional Material Without an Account | MVP — Resumefolio core |
| [USR-D04](user-requirements.md#usr-d04-prepare-and-track-applications-manually) | Prepare and Track Applications Manually | MVP — Resumefolio core |
| [USR-D05](user-requirements.md#usr-d05-keep-a-trustworthy-record-of-actual-submitted-materials) | Keep a Trustworthy Record of Actual Submitted Materials | MVP — Resumefolio core |
| [USR-D06](user-requirements.md#usr-d06-coordinate-correspondence-and-activities) | Coordinate Correspondence and Activities | Deferred after MVP |
| [USR-D07](user-requirements.md#usr-d07-plan-and-adapt-authorized-work) | Plan and Adapt Authorized Work | Split — MVP ProjectForge basic capability; advanced workflows deferred |
| [USR-D08](user-requirements.md#usr-d08-collaborate-within-invited-resource-boundaries) | Collaborate Within Invited Resource Boundaries | MVP — Resumefolio core |
| [USR-D09](user-requirements.md#usr-d09-use-real-repository-collaboration) | Use Real Repository Collaboration | Split — MVP ProjectForge basic capability; advanced workflows deferred |
| [USR-D10](user-requirements.md#usr-d10-run-agreed-checks-and-control-deployment-separately) | Run Agreed Checks and Control Deployment Separately | Deferred after MVP |
| [USR-D11](user-requirements.md#usr-d11-administer-explicit-policy-and-understand-failures) | Administer Explicit Policy and Understand Failures | MVP — Resumefolio core |
| [USR-D12](user-requirements.md#usr-d12-operate-and-recover-an-identified-release) | Operate and Recover an Identified Release | MVP — Resumefolio core |
| [YML-D01](yaml-workflows-and-cicd.md#yml-d01-defined-supported-workflow-contract) | Defined Supported Workflow Contract | Deferred after MVP |
| [YML-D02](yaml-workflows-and-cicd.md#yml-d02-explicit-triggers-and-run-authority) | Explicit Triggers and Run Authority | Deferred after MVP |
| [YML-D03](yaml-workflows-and-cicd.md#yml-d03-run-identity-and-reproducible-context) | Run Identity and Reproducible Context | Deferred after MVP |
| [YML-D04](yaml-workflows-and-cicd.md#yml-d04-isolation-and-untrusted-code-boundary) | Isolation and Untrusted-code Boundary | Deferred after MVP |
| [YML-D05](yaml-workflows-and-cicd.md#yml-d05-scoped-secrets-and-credentials) | Scoped Secrets and Credentials | Deferred after MVP |
| [YML-D06](yaml-workflows-and-cicd.md#yml-d06-resource-admission-and-limits) | Resource Admission and Limits | Deferred after MVP |
| [YML-D07](yaml-workflows-and-cicd.md#yml-d07-truthful-run-and-step-outcomes) | Truthful Run and Step Outcomes | Deferred after MVP |
| [YML-D08](yaml-workflows-and-cicd.md#yml-d08-restricted-logs-and-artifacts) | Restricted Logs and Artifacts | Deferred after MVP |
| [YML-D09](yaml-workflows-and-cicd.md#yml-d09-cancellation-retry-and-runner-loss-recovery) | Cancellation, Retry and Runner-loss Recovery | Deferred after MVP |
| [YML-D10](yaml-workflows-and-cicd.md#yml-d10-separate-controlled-deployment-stage) | Separate Controlled Deployment Stage | Deferred after MVP |
| [YML-D11](yaml-workflows-and-cicd.md#yml-d11-workspace-cleanup-and-retained-evidence) | Workspace Cleanup and Retained Evidence | Deferred after MVP |
| [YML-D12](yaml-workflows-and-cicd.md#yml-d12-feasibility-operational-guidance-and-enabling-gate) | Feasibility, Operational Guidance and Enabling Gate | Deferred after MVP |

## Split-record interpretation

GIT-D08 keeps issues in MVP and milestones for later. GIT-D04 does not add an advanced browser branch-management feature. PKS-D01/02/05/06/11 support only simple Kanban plus necessary permissions and truthful lifecycle; advanced workflow configuration is not implicitly accepted. APP-D08 keeps manual next action and follow-up date without provider integration. USR-D07/09 preserve basic ProjectForge goals while advanced review/Sprint behavior is future. QSR-D07 keeps safe uploads/rendering in MVP; executable repository workloads are deferred.

For all shared ACC/AFO/EIF/QSR/lifecycle rules, evaluate the retained MVP path; provider, Sprint, review/release and runner-specific examples are future criteria. No shared rule becomes permission to enable a deferred capability. Planned verification is unexecuted until actual implementation evidence is recorded.

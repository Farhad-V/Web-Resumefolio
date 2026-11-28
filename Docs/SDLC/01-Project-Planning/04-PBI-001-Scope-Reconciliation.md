# PBI-001 Scope, Responsibilities and Planning Constraints

## Candidate and disposition

Review performed on 2026-11-28 against repository revision `f47086b241e545fa404ed07880c353cfe4dbe314`, the current body of [issue #1](https://github.com/Farhad-V/Web-Resumefolio/issues/1), and the documents linked below. This evidence document is a review candidate; publication does not imply owner acceptance of I1-T02. Farhad explicitly accepted the I1-T01 comparison in the Persian voice conversation on 2026-11-28: «بازبینی رو تأیید می‌کنم، بریم شروع کنیم». That acceptance applies to the previously presented scope/responsibility comparison only. I1-T02 is now documented and checked below; its owner review and final issue-level disposition remain pending. The appropriate board state is Review, not Done. No product criterion, readiness gate or release is marked passed.

## Controlling sources

- [Project Charter](01-Project-Charter.md): selected scope, exclusions, roles and release authority.
- [Current record rules](../02-Requirements-Engineering/01-Software-Requirements-Specification/03-Requirements-Specification/15-Requirement-Priority-And-Readiness.md#current-record-rules): interpretation of historical proposals and selected slices.
- [Decision dispositions](../02-Requirements-Engineering/01-Software-Requirements-Specification/07-Change-And-Baseline/03-Requirements-Questions-And-Decisions.md): Q-D01 through Q-D28 and accepted profile policy.
- [ADR register](../04-System-Design/ADR/Decision-Index.md): ADR-005 boundaries, ADR-006 implementation baseline and ADR-007 frontend amendment.
- [Manual status amendment](../02-Requirements-Engineering/01-Software-Requirements-Specification/03-Requirements-Specification/09-Manual-Application-Management.md#owner-selected-manual-application-status): current owner-selected status behavior.
- [Criterion register](../02-Requirements-Engineering/03-Requirements-Traceability-Matrix/02-Criterion-Coverage.md): exact criterion wording and retained gaps.
- [Sprint 01 slices](../05-Agile-Iterative-Development/03-Sprint-Delivery-Plan.md#issue-1): I1-T01 and separate I1-T02.

The frozen baseline was read from local Git object `1f2acaa351ac306cb57cbe4fe9742e8bd90720d9` (policy-decisions.md and Project-Management/product-backlog.md under docs/MVP). It retains provenance; later owner amendments control their stated subjects.

## Scope comparison and criterion trace

Each result below is a documentary match, not a functional test or acceptance of an entire criterion. Apply the individual criterion's MVP constraint; excluded clauses stay deferred.

| Selected boundary | Comparison result and controlling decision | Issue #1 criterion locators |
| --- | --- | --- |
| Invited private workspace; no public registration; admin has no implicit private-content access | Charter agrees with Q-D03/Q-D04 and ADR-005. Employer and collaborator authority remains limited to the selected resource. | BIZ-D04-AC01, BIZ-D04-AC02, BIZ-D04-AC03; DOM-D03-AC01, DOM-D03-AC02, DOM-D03-AC03 |
| Reusable profile, independent resume/portfolio drafts, manually authored cover letters, explicit publication | Charter agrees with Q-D06/Q-D07 and accepted profile policy. Preview/select/apply preserves overrides and never publishes automatically. | BIZ-D01-AC01, BIZ-D01-AC02, BIZ-D01-AC03; DOM-D01-AC01, DOM-D01-AC02, DOM-D01-AC03 |
| Private same-server media, generated/uploaded PDFs, password-protected employer access without an account | Charter agrees with Q-D08/Q-D10/Q-D11 and ADR-005. Only published and explicitly selected material is shared; direct retrieval and revocation still require runtime proof. | BIZ-D02-AC01, BIZ-D02-AC02, BIZ-D02-AC03; DOM-D03-AC02, DOM-D03-AC03 |
| Manual applications, exact submitted materials, status/next action/follow-up | Charter agrees with Q-D12/Q-D13/Q-D14 and the later manual-status amendment. Any existing MVP status can be selected from any status; no external send/receipt is implied. Later edits preserve submitted history. | BIZ-D03-AC01, BIZ-D03-AC02, BIZ-D03-AC03; DOM-D02-AC01, DOM-D02-AC02, DOM-D02-AC03 |
| English/German manually authored variants; no automatic translation | Q-D09 and Charter exclusions agree. An unavailable language is explicit; no implicit fallback or AI dependency. | DOM-D04-AC01, DOM-D04-AC02, DOM-D04-AC03 |
| Separate ProjectForge with scoped API, native Git, repository permissions, files/history, issues and fixed Kanban | Charter agrees with ADR-005 and Q-D18/Q-D21/Q-D22. No shared authority/database or simulated Git is selected. GitHub delivery Sprints do not add product Sprint functionality. | BIZ-D04-AC02, BIZ-D04-AC03; DOM-D03-AC01, DOM-D03-AC03; BIZ-D04-AC04 remains deferred |
| Runtime, capacity, recovery and evidence obligations | Charter retains actual candidate verification and isolated restore. Q-D24 through Q-D27 select obligations, not observed success. | BIZ-D05-AC01, BIZ-D05-AC02, BIZ-D05-AC03, BIZ-D05-AC04; DOM-D05-AC02, DOM-D05-AC03; DOM-D08-AC01, DOM-D08-AC02, DOM-D08-AC03 |
| Legal applicability and dependency/asset rights | RTM gaps remain explicit; neither this comparison nor Charter claims compliance or reuse approval. No demo migration/reference-project change is authorized. | DOM-D06-AC01, DOM-D06-AC02, DOM-D06-AC03; DOM-D07-AC01, DOM-D07-AC02, DOM-D07-AC03 |

Personal mail/calendar and Google integration, AI, automatic translation/submission, advanced Git review/merge/releases, general backlog/Sprints and user workflow/deployment execution remain after MVP (Q-D15–Q-D19, Q-D22/Q-D23 within their dispositions). Transactional invitation/recovery SMTP remains an MVP dependency; it is not deferred personal mail. DOM-D05-AC01 is deferred and is not added to issue #1 acceptance.

## Responsibilities

Farhad is the sole delivery and operations owner and the authority for scope changes and release decisions, as recorded in Charter and the current SRS. Codex prepares this evidence under the explicit instructions to execute I1-T01 and then I1-T02. Farhad's explicit I1-T01 acceptance is attributed above; acceptance of the later I1-T02 addition is not inferred. Product roles (administrator, invited account holder, employer viewer and ProjectForge collaborator) retain the Charter's resource-limited responsibilities. No additional staffing, reviewer approval or operational readiness is assumed.

## Differences resolved by existing authority

1. The frozen PBI-001 title includes an obsolete working-capacity assumption. Current issue #1 and scope-driven Sprint slices replace that planning basis. No working-hour estimate or schedule is adopted; the frozen record remains unchanged for provenance.
2. Frozen frontend wording is amended by owner-selected ADR-007: React/Inertia within each independent Laravel application; trusted Blade PDF templates remain. This is an existing amendment, not a new stack decision.
3. Earlier application-progress wording must be read under the owner-selected unrestricted manual-status amendment. No workflow lock or automatic submission is introduced.
4. Historical proposals and broad product examples do not reopen selected MVP policy or import deferred provider/Sprint/runner behavior. Current record rules and exact criterion dispositions govern.

No unresolved contradiction was found between Charter and the reviewed selected scope/responsibility records. This is a bounded comparison, not a review of every design contract or all 480 criteria; those walkthroughs belong to #8/#9.

## Open evidence and exit

| Remaining input | Owner / follow-up | Exit condition |
| --- | --- | --- |
| I1-T01 scope/responsibility review | Farhad; issue #1 | Accepted explicitly in the voice conversation on 2026-11-28; limited to the prior I1-T01 candidate. |
| I1-T02 planning constraints | Farhad; issue #1 | Documentary check complete below; owner review of this addition remains pending before final issue disposition. |
| Current host capacity/isolation and compatible setup targets | Farhad; #2, then #9/#37 | Actual sanitized host observations and safe setup prerequisite evidence. Historical observations are not current readiness. |
| Project-specific privacy applicability and component/asset licensing | Farhad; DOM-D06/DOM-D07 at applicable adoption gates | Record actual deployment facts, authoritative applicability assessment and resolved dependency/asset rights; hold affected adoption if unresolved. |
| Runtime, native Git, delivery, actor validation and restore | Owning delivery issues and gates | Identifiable candidate plus exact observed criterion results; no product test is executed by this document. |

Verification: compared the named sources and issue-specific BIZ/DOM locators, preserving deferred BIZ-D04-AC04 and excluding DOM-D05-AC01 as the current issue does. Local-link existence and whitespace checks are run on the resulting candidate. No production code, server or dependency change is part of this slice. Farhad separately authorized committing and pushing this report to GitHub; publication does not approve the pending review.

## I1-T02: Operating obligations, unresolved inputs and review owner

Prepared on 2026-11-28 against the same base revision and the live issue #1 acceptance wording. Sources: [management plan](02-Project-Management-Plan.md), [feasibility and risks](03-Feasibility-And-Risk-Assessment.md), [runbook](../06-Deployment-Release/02-Runbook.md), selected Q-D24–Q-D27 and the criterion trace above. The management plan responsibility table identifies Farhad for product decisions, execution, acceptance and release; no extra team or reviewer is assumed.

| Current obligation / constraint | Accountable owner | Unresolved input and affected boundary | Follow-up / completion evidence |
| --- | --- | --- | --- |
| Preserve independent Core/ProjectForge authority, private storage, keys, sessions and databases on the existing shared host | Farhad | Current workloads, resource headroom, separate identities/paths/DB grants and required Nginx capabilities are not freshly established | #2 inventory; #9 contracts; #37 isolated setup. Record actual observations and hold affected setup if targets/isolation are unsafe. DOM-D05-AC02/03; DOM-D08-AC01 |
| Preserve the existing hosted workload and isolate synthetic development/testing from real data | Farhad | Safe new target paths and compatibility with installed runtimes remain unverified | #2/#37; no demo migration, deployment or server change follows from #1. DOM-D07-AC03 |
| Deliver operational invitations/recovery through transactional SMTP | Farhad | Current configured delivery and actual receipt are unproven; secrets are not collected in this record | #5 controlled delivery evidence; hold operational onboarding/recovery until verified. Personal provider mail remains deferred |
| Maintain coherent backup, protected destination, recovery and revocation/deletion behavior | Farhad | Actual independent backup destination, capture consistency and isolated restore evidence are outstanding | #6 prerequisites and #27 restore demonstration; hold stable production release until required evidence exists. BIZ-D05-AC03; DOM-D08-AC03 |
| Check capacity, retained storage and supported workload before enabling dependent operations | Farhad | Actual quotas/headroom and workload results remain unmeasured; old low-load host observations are historical only | #2, #41 and #26 owning checks; record measured limits and an owner decision for any resource/cost conflict. BIZ-D05-AC02/04; DOM-D08-AC02 |
| Assess actual data use, recipients, retention and applicable privacy obligations | Farhad | Deployment-specific controller/processor, jurisdiction/contract facts and authoritative applicability assessment remain open | DOM-D06-AC01/02/03 retained RTM gaps; resolve before affected adoption, without claiming compliance or reopening settled scope |
| Review dependency/asset provenance, resolved versions and reuse rights before adoption | Farhad | Actual lockfiles/assets and license/terms dispositions do not yet exist for the new applications | #9/#37 and DOM-D07-AC01/02; unresolved rights block affected adoption; extra cost/tooling requires Farhad's decision |
| Keep evidence, monitoring, patching and operating guidance tied to the real candidate | Farhad | Executable setup, operating commands, incident/recovery rehearsals and actual candidate tests remain unexecuted | Owning implementation items, #28 and #29; preserve failures and sanitized results; release authority stays separate. BIZ-D05-AC01/03/04 |

**Review owner:** Farhad, per the existing management plan. Codex performed the documentary comparison and constraint inventory; Farhad reviews the resulting record. Participant feedback for future actor validation is obtained when relevant and available, not invented here. No new product decision is needed to finish this inventory. Missing operational facts are assigned to their owning items; documenting them does not establish feasibility or require solving later delivery items within #1.

### I1-T02 expected / actual checks

| Check | Expected | Actual documentary result |
| --- | --- | --- |
| I1-T02-C01 obligations | Existing host/data protection, isolation, mail, backup/recovery, capacity and maintenance duties are explicit | Recorded above from management plan, risk assessment and runbook; operational execution remains unverified |
| I1-T02-C02 unresolved inputs | Each material unknown has owner, affected boundary and exit evidence | Recorded above with owning items and exact applicable BIZ/DOM locators; no scope silently removed |
| I1-T02-C03 responsibility | Delivery, operations and review authority agree with Charter/management plan | Farhad retains those roles; no invented staffing or approval |
| I1-T02-C04 acceptance boundary | Historical/selected design, owner acceptance and runtime evidence are distinguished | I1-T01 acceptance explicitly attributed; I1-T02 owner review pending; all product tests and runtime gates remain unexecuted |

### Issue #1 completion assessment and next work

The selected scope, exclusions, responsibilities and planning constraints now have an identified document candidate, criterion trace and explicit limitations. #1 has no prerequisite package. Both documentary slices have been prepared and checked; only I1-T01 has received Farhad's explicit review acceptance. Keep #1 open in Review pending his disposition on I1-T02 and the combined outcome. The report was initially local and uncommitted. Farhad subsequently explicitly authorized its commit and push; the containing Git revision identifies the published candidate, and the issue evidence record links that exact revision after verification. This record does not mark functional BIZ/DOM criteria or G1–G6 passed, and does not re-accept the entire G0 baseline.

The next item in Sprint 01's reading/start order is #2: read-only inventory of the actual host and isolation prerequisites. It is independent of #1, but fresh observations/access and a safe target must be established before calling it verified. In parallel sequencing terms, #7 depends on accepted #1, then #8 depends on #7 and #9 depends on #8; no later item is executed by this record. No duration or working-capacity forecast is introduced.

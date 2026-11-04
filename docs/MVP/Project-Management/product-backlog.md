# Product Backlog

Updated November 4, 2026. This is the current scope and dependency index, not a duplicate live status database. [Baseline](../baseline/README.md) and [criterion dispositions](../baseline/criterion-dispositions.md) own requirement/policy applicability. [Roadmap and Milestones](../SDLC/01-project-planning/08-roadmap-and-milestones.md#2-milestone-catalog) owns outcome definitions and acceptance. Live task state, evidence and blockers belong in GitHub Issues and Kanban. No Sprint or delivery deadline is assigned.

## Current MVP work packages

Existing PBI-001–029 identities are preserved; PBI-030–034 isolate Setup, identity/Git feasibility, API, immutable history and quota risks already required by the Baseline. New packages refine existing scope and do not add capabilities. Prefix links mean the applicable selected criteria only; the original 470 plus 10 supplemental checks are not all MVP obligations.

| ID | Outcome | Milestone | Dependencies | Acceptance / gate |
| --- | --- | --- | --- | --- |
| <a id="pbi-001"></a>[PBI-001](https://github.com/Farhad-V/Web-Resumefolio/issues/1) | Record 20-hour capacity and MVP scope | M-01 | None | BIZ / DOM; G0 |
| <a id="pbi-002"></a>[PBI-002](https://github.com/Farhad-V/Web-Resumefolio/issues/2) | Verify shared-host capacity and isolation prerequisites | M-03 | None | AFO / QSR; G1; G5 |
| <a id="pbi-005"></a>[PBI-005](https://github.com/Farhad-V/Web-Resumefolio/issues/5) | Verify invitation and recovery SMTP delivery | M-03 | PBI-002 | ACC / EIF; G4 |
| <a id="pbi-006"></a>[PBI-006](https://github.com/Farhad-V/Web-Resumefolio/issues/6) | Verify independent backup destination and restore plan | M-03 | PBI-002 | QSR / AFO; G4 |
| <a id="pbi-007"></a>[PBI-007](https://github.com/Farhad-V/Web-Resumefolio/issues/7) | Review current planning allocation and tracked follow-ups | M-01 | PBI-001 | BIZ / DOM; G0 |
| <a id="pbi-008"></a>[PBI-008](https://github.com/Farhad-V/Web-Resumefolio/issues/8) | Validate MVP requirement and criterion coverage | M-02 | PBI-007 | USR / BIZ / DOM; G0 |
| <a id="pbi-009"></a>[PBI-009](https://github.com/Farhad-V/Web-Resumefolio/issues/9) | Reconcile selected Design and technical baseline | M-03 | PBI-008 | DOM / EIF / QSR; G0; G1 |
| <a id="pbi-010"></a>[PBI-010](https://github.com/Farhad-V/Web-Resumefolio/issues/10) | Implement invited identity and resource authorization | M-04 | PBI-030 | ACC; G3 |
| <a id="pbi-011"></a>[PBI-011](https://github.com/Farhad-V/Web-Resumefolio/issues/11) | Implement dashboard and responsive application shell | M-04 | PBI-010 | EIF / USR; G3; G5 |
| <a id="pbi-012"></a>[PBI-012](https://github.com/Farhad-V/Web-Resumefolio/issues/12) | Implement Profile and independent Resume drafts | M-05 | PBI-010 | PRP / BRL; G3 |
| <a id="pbi-013"></a>[PBI-013](https://github.com/Farhad-V/Web-Resumefolio/issues/13) | Implement private My Files and Media library | M-05 | PBI-010, PBI-002 | AFO / PRP; G3; G5 |
| <a id="pbi-014"></a>[PBI-014](https://github.com/Farhad-V/Web-Resumefolio/issues/14) | Implement generated and uploaded language-specific PDFs | M-05 | PBI-012, PBI-013 | PDF; G3; G5 |
| <a id="pbi-015"></a>[PBI-015](https://github.com/Farhad-V/Web-Resumefolio/issues/15) | Implement password links and protected selected-content retrieval | M-05 | PBI-012, PBI-013, PBI-014 | PDF / ACC; G3 |
| <a id="pbi-016"></a>[PBI-016](https://github.com/Farhad-V/Web-Resumefolio/issues/16) | Implement manual applications and actual submitted history | M-06 | PBI-012, PBI-014, PBI-033 | APP / BRL; G3 |
| <a id="pbi-019"></a>[PBI-019](https://github.com/Farhad-V/Web-Resumefolio/issues/19) | Implement ProjectForge fixed issue Kanban | M-07 | PBI-022 | PKS; G3 |
| <a id="pbi-020"></a>[PBI-020](https://github.com/Farhad-V/Web-Resumefolio/issues/20) | Implement native repositories and real Git transfers | M-07 | PBI-031, PBI-032, PBI-034 | GIT; G2; G3 |
| <a id="pbi-022"></a>[PBI-022](https://github.com/Farhad-V/Web-Resumefolio/issues/22) | Implement basic ProjectForge repository issues | M-07 | PBI-032, PBI-020 | GIT / PKS; G3 |
| <a id="pbi-024"></a>[PBI-024](https://github.com/Farhad-V/Web-Resumefolio/issues/24) | Implement account suspension, lifecycle and audit | M-09 | PBI-010, PBI-013, PBI-033 | ACC / AFO / BRL / QSR; G3; G4 |
| <a id="pbi-025"></a>[PBI-025](https://github.com/Farhad-V/Web-Resumefolio/issues/25) | Verify integrated MVP acceptance and authorization | M-09 | PBI-011, PBI-015, PBI-016, PBI-019, PBI-024, PBI-032 | ACC / PRP / PDF / APP / GIT / PKS; G3; G6 |
| <a id="pbi-026"></a>[PBI-026](https://github.com/Farhad-V/Web-Resumefolio/issues/26) | Measure capacity, browsers and accessibility | M-09 | PBI-025, PBI-034 | QSR / EIF; G5 |
| <a id="pbi-027"></a>[PBI-027](https://github.com/Farhad-V/Web-Resumefolio/issues/27) | Demonstrate coherent restore and deployment recovery | M-09 | PBI-006, PBI-024, PBI-020, PBI-033 | QSR / AFO; G4 |
| <a id="pbi-028"></a>[PBI-028](https://github.com/Farhad-V/Web-Resumefolio/issues/28) | Complete user, admin and operating guidance | M-09 | PBI-025, PBI-027 | EIF / QSR / USR; G4; G6 |
| <a id="pbi-029"></a>[PBI-029](https://github.com/Farhad-V/Web-Resumefolio/issues/29) | Review and deploy the initial MVP release | M-10 | PBI-025, PBI-026, PBI-027, PBI-028 | USR / QSR; G6 |
| <a id="pbi-030"></a>[PBI-030](https://github.com/Farhad-V/Web-Resumefolio/issues/37) | Create isolated Laravel applications and reproducible Setup | M-04 | PBI-009, PBI-002 | DOM / EIF; G1 |
| <a id="pbi-031"></a>[PBI-031](https://github.com/Farhad-V/Web-Resumefolio/issues/38) | Prove ProjectForge SSO and native Git security spike | M-07 | PBI-030, PBI-010, PBI-002 | ACC / GIT; G2 |
| <a id="pbi-032"></a>[PBI-032](https://github.com/Farhad-V/Web-Resumefolio/issues/39) | Implement Core and ProjectForge scoped identity/API | M-07 | PBI-031, PBI-010 | ACC / EIF; G2; G3 |
| <a id="pbi-033"></a>[PBI-033](https://github.com/Farhad-V/Web-Resumefolio/issues/40) | Implement atomic publication and protected artifact history | M-05 | PBI-012, PBI-013, PBI-014 | PRP / BRL / APP; G3 |
| <a id="pbi-034"></a>[PBI-034](https://github.com/Farhad-V/Web-Resumefolio/issues/41) | Enforce storage reservations and bounded Git/media admission | M-05 | PBI-002, PBI-030 | AFO / QSR / GIT; G2; G5 |

## Package completion conditions

### PBI-001 — Record 20-hour capacity and MVP scope

Record the actual 20 total project hours/week, including learning/docs/tests/operations. Preserve old dates only as historical; no new delivery deadline is promised.

### PBI-002 — Verify shared-host capacity and isolation prerequisites

Record sanitized actual host resources/workloads, disk reservation headroom, independent users/DB/storage and required Nginx modules. No infrastructure change is implied by this investigation.

### PBI-005 — Verify invitation and recovery SMTP delivery

Select actual operator SMTP configuration, demonstrate receipt with authorized test addresses, truthful outcomes, throttling and recovery. Never expose secrets or confuse log transport with delivery.

### PBI-006 — Verify independent backup destination and restore plan

Verify restic destination capacity/access, separate recovery keys, consistent Core/ProjectForge capture and 7 daily/4 weekly retention; prepare isolated restore procedure. Actual restore is PBI-027.

### PBI-007 — Review current planning allocation and tracked follow-ups

Review the current scope, dependencies, 20-hour capacity, risk and evidence gates. Preserve original M-01 acceptance without claiming later outcome acceptance.

### PBI-008 — Validate MVP requirement and criterion coverage

Review the selected Baseline, preserved criterion dispositions and 10 supplemental checks as an implementation input. Establish the applicable specification-to-test-plan mapping and requirements walkthrough; actual product results and actor acceptance remain PBI-025/G6, not prerequisites to Setup.

### PBI-009 — Reconcile selected Design and technical baseline

Use selected T01–T10 and Q-D decisions, separate Core/ProjectForge trust/storage, private media and recovery design. Resolve real compatibility/feasibility findings; selected documents are not installed runtime evidence. Setup is PBI-030.

### PBI-010 — Implement invited identity and resource authorization

Implement admin invitation, no public signup, Login/recovery/Admin TOTP, current-session revocation, explicit policies and private cross-user denial. SMTP acceptance depends on PBI-005.

### PBI-011 — Implement dashboard and responsive application shell

Provide authorized navigation and dashboard for Core/manual applications/basic ProjectForge. Keyboard/mobile/language/failure states must not imply unauthorized data or completed external actions.

### PBI-012 — Implement Profile and independent Resume drafts

Private Profile, multiple tailored resumes/portfolio, manual English/German variants, selected source preview/apply and independent overrides. Publishing is separately confirmed and stale edits conflict.

### PBI-013 — Implement private My Files and Media library

Same Core server outside public webroot, selected supported video/audio/image/text/PDF formats and safe YouTube embeds. Quarantine/type/dimension checks, private-by-default storage and per-resume selection; upload never publishes.

### PBI-014 — Implement generated and uploaded language-specific PDFs

Trusted-template Dompdf, EN/DE fonts/page flow, separate generated/uploaded modes and immutable private artifacts. Missing/failed language is explicit; remote resources and arbitrary user HTML are disabled.

### PBI-015 — Implement password links and protected selected-content retrieval

Employer views only the selected published resume/media/PDF without owner login. Link/password revocation applies to every future preview/direct/range request; no public storage URL or shared-cache bypass. Any access statistics must be minimal, private and avoid adding new analytics scope.

### PBI-016 — Implement manual applications and actual submitted history

Company/opportunity, authored cover letter, manual status, next action and follow-up date. Capture actual submitted immutable bytes/checksums and append corrections/resubmissions; no email/calendar dependency or invented send success.

### PBI-019 — Implement ProjectForge fixed issue Kanban

Fixed To do / In progress / Done board for authorized issues, explicit assignee/priority/due date, safe movement and membership changes. General backlog/Sprints/configurable column workflows are after MVP.

### PBI-020 — Implement native repositories and real Git transfers

Independent ProjectForge native bare Git/Smart HTTP with scoped expiring PATs, current Core status and repository grants; real clone/fetch/pull/push and safe file/history browsing. Dedicated process/path/hook/env isolation; no SSH/user workflow runner.

### PBI-022 — Implement basic ProjectForge repository issues

Authorized issue creation, updates, assignee and repository context. Basic issue access does not grant repository writes. Milestone/release management and advanced collaboration UI are outside product MVP; GitHub project Milestones used to manage this work are unrelated.

### PBI-024 — Implement account suspension, lifecycle and audit

Current account revocation, private-content policies, 30-day trash, reference-aware cleanup and bounded append-only audit metadata. Preserve actual history and reapply deletion/revocation after restore; no admin implicit content access.

### PBI-025 — Verify integrated MVP acceptance and authorization

Run requirement-linked positive/denied/stale/failure/regression journeys against the identified candidate; intended actor review and complete sanitized evidence. Deferred provider/review/runner paths are not release prerequisites.

### PBI-026 — Measure capacity, browsers and accessibility

Measure selected T09 workload, latency/error limits, browser/keyboard/zoom and WCAG target plus PDF bounds and disk quotas. Targets are not prior measurements and no 30-day availability result is invented.

### PBI-027 — Demonstrate coherent restore and deployment recovery

Timed isolated encrypted backup restore of both systems, immutable artifacts, Git refs, current grants/deletion/revocation and outbox without external replay. Test code rollback separately from data recovery.

### PBI-028 — Complete user, admin and operating guidance

Document real clean Setup/run/test, actual interfaces, user/admin flows, backup/restore, patching and operational response; link candidate-specific evidence. Keep documentation current with implementation.

### PBI-029 — Review and deploy the initial MVP release

Before any deployment confirm required gate evidence, actual candidate, credentials/TLS, compatible migrations, tested recovery and owner Release decision. Then execute the separately reviewed deployment procedure and record live checks. Creating this issue performs no deployment.

### PBI-030 — Create isolated Laravel applications and reproducible Setup

Create Core and independent ProjectForge scaffolds using selected maintained versions, isolated MySQL databases/users, lockfiles and clean build/test commands. No demo migration or live server change; document verified Setup.

### PBI-031 — Prove ProjectForge SSO and native Git security spike

Run real isolated clients plus OAuth state/PKCE/redirect, current-account revocation, forged/expired/wrong-repo credentials, dumb/anonymous transport denial, paths/header/env/hooks and quota/ref races. Failures require Design revision before enabling Git, never a fake pass.

### PBI-032 — Implement Core and ProjectForge scoped identity/API

OAuth authorization code + PKCE binds immutable Core identity; independent sessions/databases. Short-lived signed audience/scoped API tokens, local grants and fresh fail-closed Core status checks; correct timeout/retry behavior and no browser service-wide bearer.

### PBI-033 — Implement atomic publication and protected artifact history

Source/draft/publication/submission identities, optimistic versions, immutable bytes and protected reference reservations, short local transactions/outbox/idempotency and cleanup reconciliation. Interrupted capture cannot appear complete or delete referenced history.

### PBI-034 — Enforce storage reservations and bounded Git/media admission

Implement selected per-file/user/global quotas including temporary/quarantine bytes, disk reserve and concurrent reservations; bound Git requests/processes and deny exhaustion safely without losing committed data.

## Deferred after MVP

These original work items remain open future planning, not failed or completed MVP tasks. Remove obsolete MVP deadline/Sprint assignments. Keep their history and do not delete or mark them complete merely to improve the board.

| ID | Future outcome | Reference |
| --- | --- | --- |
| <a id="pbi-003"></a>[PBI-003](https://github.com/Farhad-V/Web-Resumefolio/issues/3) | Assess future isolated workflow execution | M-08 |
| <a id="pbi-004"></a>[PBI-004](https://github.com/Farhad-V/Web-Resumefolio/issues/4) | Assess future Gmail and Calendar provider access | Future planning; no MVP milestone |
| <a id="pbi-017"></a>[PBI-017](https://github.com/Farhad-V/Web-Resumefolio/issues/17) | Implement future personal Gmail client | Future planning; no MVP milestone |
| <a id="pbi-018"></a>[PBI-018](https://github.com/Farhad-V/Web-Resumefolio/issues/18) | Implement future Calendar and provider synchronization | Future planning; no MVP milestone |
| <a id="pbi-021"></a>[PBI-021](https://github.com/Farhad-V/Web-Resumefolio/issues/21) | Implement future advanced review and merge | Future planning; no MVP milestone |
| <a id="pbi-023"></a>[PBI-023](https://github.com/Farhad-V/Web-Resumefolio/issues/23) | Implement future user YAML execution and deployment | M-08 |

Advanced general backlog/Sprints/configurable boards and advanced Git milestones/releases formerly bundled into PBI-019/022 remain future specifications; those existing issue identities now track only their MVP slices. The product’s future milestone feature is distinct from GitHub Milestones used to manage development.

## Execution rules

Each GitHub issue has one stable PBI identity, outcome, dependencies, links to exact selected criteria and a verification checklist. Large packages may be decomposed into linked child tasks when execution begins. A broad issue title is not a completed plan or test result.

Use Backlog → In Progress → Done. All packages start in Backlog; move a package to In Progress only when work actually starts and its prerequisites are satisfied. Done requires verified completion criteria and linked evidence. Record blockers and review notes in the Issue without adding columns. Keep after-MVP work in the separate After MVP view using its scope label. Product Backlog is a table of the same MVP Issues shown on MVP Kanban, not a second task list. No active Sprint or completed implementation is asserted.

No implementation is started by reconciling this backlog. Estimates and delivery dates remain uncommitted; available capacity is 20 total project hours/week.

[Delivery workflow](version-1-delivery-plan.md) · [GitHub Issues](https://github.com/Farhad-V/Web-Resumefolio/issues)

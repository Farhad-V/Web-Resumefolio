# Sprint Delivery Plan

[Development overview](00-Agile-Iterative-Development.md) · [Product backlog](../02-Requirements-Engineering/02-Product-Backlog/README.md) · [Test strategy](02-Test-Strategy.md) · [RTM](../02-Requirements-Engineering/03-Requirements-Traceability-Matrix/README.md)

## Selection, Verification and Completion Rules

These are proposed development groups organized by dependencies. Select a demonstrable slice and split or carry work explicitly when needed. No iteration is started, no task completed and no test passed by this refinement.

**Ready to select:** exact issue/slice and applicable RTM criteria identified; earlier dependencies accepted for the required boundary; actual safe environment and input available; expected outcomes and denied/failure checks clear; task small enough to review. An unavailable host, service credential, backup destination or required legal/license disposition is a named gate/input, not silently assumed success. Independent settled work may proceed where that gate does not apply.

**Done for a slice:** attributable revision/document change; expected functional and relevant denied/stale/retry/concurrent/interrupted checks executed; actual evidence mapped to each applicable criterion; safe data/configuration/migration implications checked; affected guidance updated; review disposition recorded. No unresolved blocker may be relabeled passed. A checkbox, documentation link, mock or successful build cannot replace the required real boundary/byte/restore evidence. Production deployment and owner acceptance still require their actual separate authority.

**Tests and security belong in every implementation slice.** Sprint 10/11 are integrated/regression and workload/accessibility checkpoints, not the first time testing, isolation, revocation or accessibility is implemented. Restore primitives and capture safety begin in Sprint 02 and evolve with each data/artifact change; Sprint 10 proves the combined restored candidate.

**Task identity:** `I<number>-T<number>` below is a work locator under the existing issue, not a replacement requirement ID or a new backlog item. Preserve the issue's exact criterion register and scope constraints; map observed results to individual criteria. A task may need further splitting after the actual implementation seam is known. Deferred issues #3/#4/#17/#18/#21/#23 stay outside these groups and are not implemented by this plan.

Work locators define execution precedence. Refine later groups from implementation evidence before selecting their next demonstrable slice.

## Dependency-Ordered Allocation

| Group | Demonstrable goal | Execution sequence |
| --- | --- | --- |
| 01 | Reviewed scope, host prerequisites and implementation inputs | [#1](https://github.com/Farhad-V/Web-Resumefolio/issues/1) → [#2](https://github.com/Farhad-V/Web-Resumefolio/issues/2) → [#7](https://github.com/Farhad-V/Web-Resumefolio/issues/7) → [#8](https://github.com/Farhad-V/Web-Resumefolio/issues/8) → [#9](https://github.com/Farhad-V/Web-Resumefolio/issues/9) |
| 02 | Repeatable isolated applications, transactional SMTP and backup prerequisites | [#37](https://github.com/Farhad-V/Web-Resumefolio/issues/37) → [#5](https://github.com/Farhad-V/Web-Resumefolio/issues/5) → [#6](https://github.com/Farhad-V/Web-Resumefolio/issues/6) |
| 03 | Invited private access with current authorization | [#10](https://github.com/Farhad-V/Web-Resumefolio/issues/10) |
| 04 | Bounded admission and proven identity/native Git boundary | [#41](https://github.com/Farhad-V/Web-Resumefolio/issues/41) → [#38](https://github.com/Farhad-V/Web-Resumefolio/issues/38) |
| 05 | Usable private workspace, profile/resume drafts and media | [#11](https://github.com/Farhad-V/Web-Resumefolio/issues/11) → [#12](https://github.com/Farhad-V/Web-Resumefolio/issues/12) → [#13](https://github.com/Farhad-V/Web-Resumefolio/issues/13) |
| 06 | Exact PDF variants, atomic publication and protected history | [#14](https://github.com/Farhad-V/Web-Resumefolio/issues/14) → [#40](https://github.com/Farhad-V/Web-Resumefolio/issues/40) |
| 07 | Protected selected sharing and manual application history | [#15](https://github.com/Farhad-V/Web-Resumefolio/issues/15) → [#16](https://github.com/Farhad-V/Web-Resumefolio/issues/16) |
| 08 | Scoped production integration and real native Git | [#39](https://github.com/Farhad-V/Web-Resumefolio/issues/39) → [#20](https://github.com/Farhad-V/Web-Resumefolio/issues/20) |
| 09 | Repository issues/fixed board and account lifecycle | [#22](https://github.com/Farhad-V/Web-Resumefolio/issues/22) → [#19](https://github.com/Farhad-V/Web-Resumefolio/issues/19) → [#24](https://github.com/Farhad-V/Web-Resumefolio/issues/24) |
| 10 | Integrated criterion evidence and isolated restore | [#25](https://github.com/Farhad-V/Web-Resumefolio/issues/25) → [#27](https://github.com/Farhad-V/Web-Resumefolio/issues/27) |
| 11 | Measured quality and usable operating guidance | [#26](https://github.com/Farhad-V/Web-Resumefolio/issues/26) → [#28](https://github.com/Farhad-V/Web-Resumefolio/issues/28) |
| 12 | Reviewed release candidate and separately authorized deployment | [#29](https://github.com/Farhad-V/Web-Resumefolio/issues/29) |

The numeric Development order shown on the GitHub Sprint Backlog (when present) mirrors this sequence. It is a stable reading/start order, not an additional dependency between otherwise independent items. Dependency admission always takes precedence.

<a id="sprint-01"></a>

## Sprint 01: Reviewed scope, host prerequisites and implementation inputs

**Status:** proposed; all implementation checks not executed. Near-term task/check definitions are expanded below; current external evidence still determines readiness.

**Entry:** Start with existing owner scope/responsibilities decisions and safe read-only access to the actual host/prerequisite inventory.

**Exit/demonstration:** Reviewed scope, host prerequisites and implementation inputs, demonstrated by the item checks below and the common completion rules. Retain failures, unavailable inputs and remaining scope explicitly.

<a id="issue-1"></a>

### Development order 01: PBI-001 / #1

**Proposed group:** Sprint 01. **Owner:** Farhad. **Prerequisites:** None.

**Observable outcome:** Record the selected MVP scope, exclusions and delivery responsibilities.

**Implementation/checklist slices:**

- [ ] **I1-T01: Record scope and responsibilities.** Deliver: Document MVP/deferred boundaries and the responsible delivery owner. Acceptance/verification: Check against the owner's recorded scope decisions.
- [ ] **I1-T02: Record planning constraints.** Deliver: List current operating obligations, unresolved inputs and review owner. Acceptance/verification: No invented staffing or accepted outcomes.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="issue-2"></a>

### Development order 02: PBI-002 / #2

**Proposed group:** Sprint 01. **Owner:** Farhad. **Prerequisites:** None.

**Observable outcome:** Record sanitized actual host resources/workloads, disk reservation headroom, independent users/DB/storage and required Nginx modules. No infrastructure change is implied by this investigation.

**Implementation/checklist slices:**

- [ ] **I2-T01: Inventory actual host.** Deliver: Record sanitized CPU/RAM/disk/workloads and selected service prerequisites. Acceptance/verification: Use actual observations; identify unavailable values rather than assumed capacity.
- [ ] **I2-T02: Check isolation and reserve feasibility.** Deliver: Review separate app users, databases, sessions, private roots, native Git and Nginx capabilities. Acceptance/verification: Verify intended targets and headroom against selected quotas; record each unavailable prerequisite as a blocker, without changing infrastructure.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="issue-7"></a>

### Development order 03: PBI-007 / #7

**Proposed group:** Sprint 01. **Owner:** Farhad. **Prerequisites:** [#1](https://github.com/Farhad-V/Web-Resumefolio/issues/1).

**Observable outcome:** Review the current scope, dependencies, risk and evidence gates. Preserve original M-01 acceptance without claiming later outcome acceptance.

**Implementation/checklist slices:**

- [ ] **I7-T01: Reconcile planning records.** Deliver: Review scope, responsibilities, dependencies and risk follow-ups against #1 and selected baseline. Acceptance/verification: No conflicting scope or deferred feature in the MVP path.
- [ ] **I7-T02: Review evidence gates.** Deliver: Record exact required G0/G1 inputs, responsible follow-up and conditional blockers. Acceptance/verification: Planning acceptance does not claim setup, runtime or release acceptance.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="issue-8"></a>

### Development order 04: PBI-008 / #8

**Proposed group:** Sprint 01. **Owner:** Farhad. **Prerequisites:** [#7](https://github.com/Farhad-V/Web-Resumefolio/issues/7).

**Observable outcome:** Review the selected Baseline, preserved criterion dispositions and 10 supplemental checks as an implementation input. Establish the applicable specification-to-test-plan mapping and requirements walkthrough; actual product results and actor acceptance remain PBI-025/G6, not prerequisites to Setup.

**Implementation/checklist slices:**

- [ ] **I8-T01: Walk through requirements.** Deliver: Review the 480 criterion identities and selected/deferred dispositions against the current SRS and owner amendments. Acceptance/verification: Every selected criterion has an owning delivery item or explicit tracked gap; no silent scope change.
- [ ] **I8-T02: Map verification obligations.** Deliver: Link exact applicable criteria to planned checks and owning contracts. Acceptance/verification: Distinguish planned/not executed from passed; legal/license evidence gaps remain visible at their applicable gates.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="issue-9"></a>

### Development order 05: PBI-009 / #9

**Proposed group:** Sprint 01. **Owner:** Farhad. **Prerequisites:** [#8](https://github.com/Farhad-V/Web-Resumefolio/issues/8).

**Observable outcome:** Use selected T01–T10 and Q-D decisions, separate Core/ProjectForge trust/storage, private media and recovery design. Resolve real compatibility/feasibility findings; selected documents are not installed runtime evidence. Setup is PBI-030.

**Implementation/checklist slices:**

- [ ] **I9-T01: Reconcile implementation contracts.** Deliver: Review selected ADRs, runtime/frontend targets, Core/Forge boundaries and LLD contracts. Acceptance/verification: Database/API/security/history contracts agree with current owner decisions; no legacy proposal overrides them.
- [ ] **I9-T02: Prepare setup handoff.** Deliver: Record compatibility assumptions to verify in #37 and native-boundary risks to prove in #38. Acceptance/verification: Each unknown has an exit condition; design review is not installation or runtime proof.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="sprint-02"></a>

## Sprint 02: Repeatable isolated applications, transactional SMTP and backup prerequisites

**Status:** proposed; all implementation checks not executed. Near-term task/check definitions are expanded below; current external evidence still determines readiness.

**Entry:** [#2](https://github.com/Farhad-V/Web-Resumefolio/issues/2), [#9](https://github.com/Farhad-V/Web-Resumefolio/issues/9) supply the required accepted dependency evidence.

**Exit/demonstration:** Repeatable isolated applications, transactional SMTP and backup prerequisites, demonstrated by the item checks below and the common completion rules. Retain failures, unavailable inputs and remaining scope explicitly.

<a id="issue-37"></a>

### Development order 06: PBI-030 / #37

**Proposed group:** Sprint 02. **Owner:** Farhad. **Prerequisites:** [#2](https://github.com/Farhad-V/Web-Resumefolio/issues/2), [#9](https://github.com/Farhad-V/Web-Resumefolio/issues/9).

**Observable outcome:** Create Core and independent ProjectForge scaffolds using selected maintained versions, isolated MySQL databases/users, lockfiles and clean build/test commands. No demo migration or live server change; document verified Setup.

**Implementation/checklist slices:**

- [ ] **I37-T01: Verify tools and safe paths.** Deliver: Resolve actual compatible PHP/Composer/Node/database tooling and two independent application paths from the current checkout. Acceptance/verification: Record effective versions/extensions and ensure no existing demo or live store is targeted.
- [ ] **I37-T02: Scaffold both applications.** Deliver: Install independent Core and ProjectForge Laravel applications with the selected React/Inertia stack and dependency locks. Acceptance/verification: Both locked installs and production builds succeed; no shared app key, session or database credential.
- [ ] **I37-T03: Establish isolated persistence.** Deliver: Prepare separate development/test databases, private roots and safe example configuration. Acceptance/verification: Migrations/fixtures affect only intended synthetic stores; private files are not publicly served.
- [ ] **I37-T04: Establish repeatable checks.** Deliver: Record startup/shutdown, jobs/scheduler needs, basic automated checks and build/lint commands. Acceptance/verification: Both designated entry responses and basic checks succeed in the identified environment.
- [ ] **I37-T05: Reproduce clean checkout.** Deliver: Follow the setup record from a clean checkout and capture sanitized commands/results. Acceptance/verification: G1 evidence identifies revision, lockfiles, environment, successful commands and remaining limitations.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="issue-5"></a>

### Development order 07: PBI-005 / #5

**Proposed group:** Sprint 02. **Owner:** Farhad. **Prerequisites:** [#2](https://github.com/Farhad-V/Web-Resumefolio/issues/2).

**Observable outcome:** Select actual operator SMTP configuration, demonstrate receipt with authorized test addresses, truthful outcomes, throttling and recovery. Never expose secrets or confuse log transport with delivery.

**Implementation/checklist slices:**

- [ ] **I5-T01: Configure transactional mail safely.** Deliver: Record actual SMTP operator configuration names and authorized synthetic test recipients; provision secrets outside source. Acceptance/verification: No credential in repository, browser props or diagnostic evidence; log transport is not delivery.
- [ ] **I5-T02: Prove delivery and failure handling.** Deliver: Send controlled invitation/recovery-shaped test mail and inspect actual receipt, failed connection and throttled retry outcomes. Acceptance/verification: Record transport acceptance and recipient receipt separately; failure stays visible and retries do not invent duplicate business actions.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="issue-6"></a>

### Development order 08: PBI-006 / #6

**Proposed group:** Sprint 02. **Owner:** Farhad. **Prerequisites:** [#2](https://github.com/Farhad-V/Web-Resumefolio/issues/2).

**Observable outcome:** Verify restic destination capacity/access, separate recovery keys, consistent Core/ProjectForge capture and 7 daily/4 weekly retention; prepare isolated restore procedure. Actual restore is PBI-027.

**Implementation/checklist slices:**

- [ ] **I6-T01: Verify backup destination.** Deliver: Check independent restic destination access/capacity and separately protected recovery-key availability. Acceptance/verification: Destination and keys remain independent of application failure; no secret appears in evidence.
- [ ] **I6-T02: Prepare coherent capture.** Deliver: Document Core/Forge database, artifact and native Git capture consistency and selected 7 daily/4 weekly retention. Acceptance/verification: Controlled capture/inventory matches intended scope; cleanup cannot remove protected application history.
- [ ] **I6-T03: Prepare isolated recovery.** Deliver: Record restore target checks and safe restore procedure for #27. Acceptance/verification: No live overwrite; actual end-to-end restore acceptance remains #27.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="sprint-03"></a>

## Sprint 03: Invited private access with current authorization

**Status:** proposed; all implementation checks not executed. Candidate slices are defined below; refine exact fixtures, steps and calibrated scope before starting this group.

**Entry:** [#37](https://github.com/Farhad-V/Web-Resumefolio/issues/37), [#5](https://github.com/Farhad-V/Web-Resumefolio/issues/5) supply the required accepted dependency evidence.

**Exit/demonstration:** Invited private access with current authorization, demonstrated by the item checks below and the common completion rules. Retain failures, unavailable inputs and remaining scope explicitly.

<a id="issue-10"></a>

### Development order 09: PBI-010 / #10

**Proposed group:** Sprint 03. **Owner:** Farhad. **Prerequisites:** [#37](https://github.com/Farhad-V/Web-Resumefolio/issues/37), [#5](https://github.com/Farhad-V/Web-Resumefolio/issues/5).

**Observable outcome:** Implement admin invitation, no public signup, Login/recovery/Admin TOTP, current-session revocation, explicit policies and private cross-user denial. SMTP acceptance depends on PBI-005.

**Implementation/checklist slices:**

- [ ] **I10-T01: Invite and activate.** Deliver: Implement administrator invitation and one-use activation with public signup disabled. Acceptance/verification: Expired/reused/forged invitation is denied; first signup never grants administrator privilege.
- [ ] **I10-T02: Login, recovery and factors.** Deliver: Implement selected password/session recovery, administrator TOTP and recent authentication. Acceptance/verification: Allowed login/recovery plus invalid credentials, reused recovery, missing factor and expired recent authentication are tested; use #5 delivery evidence.
- [ ] **I10-T03: Enforce current ownership.** Deliver: Implement private profile/account policies, persisted Core admin authority and current-session revocation. Acceptance/verification: Cross-user IDs, suspended/revoked sessions and client-supplied role/owner fields are denied; administrator status alone grants no private content or Forge access.
- [ ] **I10-T04: Demonstrate authenticated journey.** Deliver: Exercise invitation through private workspace admission and recovery with synthetic accounts. Acceptance/verification: Record exact applicable ACC criteria, revision and observed allowed/denied outcomes; no fake SMTP receipt.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="sprint-04"></a>

## Sprint 04: Bounded admission and proven identity/native Git boundary

**Status:** proposed; all implementation checks not executed. Candidate slices are defined below; refine exact fixtures, steps and calibrated scope before starting this group.

**Entry:** [#2](https://github.com/Farhad-V/Web-Resumefolio/issues/2), [#37](https://github.com/Farhad-V/Web-Resumefolio/issues/37), [#10](https://github.com/Farhad-V/Web-Resumefolio/issues/10) supply the required accepted dependency evidence.

**Exit/demonstration:** Bounded admission and proven identity/native Git boundary, demonstrated by the item checks below and the common completion rules. Retain failures, unavailable inputs and remaining scope explicitly.

<a id="issue-41"></a>

### Development order 10: PBI-034 / #41

**Proposed group:** Sprint 04. **Owner:** Farhad. **Prerequisites:** [#2](https://github.com/Farhad-V/Web-Resumefolio/issues/2), [#37](https://github.com/Farhad-V/Web-Resumefolio/issues/37).

**Observable outcome:** Implement selected per-file/user/global quotas including temporary/quarantine bytes, disk reserve and concurrent reservations; bound Git requests/processes and deny exhaustion safely without losing committed data.

**Implementation/checklist slices:**

- [ ] **I41-T01: Implement atomic reservations.** Deliver: Persist selected file/user/global quotas, temporary/quarantine accounting and disk reserve under concurrent admission. Acceptance/verification: Boundary and concurrent requests cannot over-admit; failed work releases only its attributable unprotected reservation.
- [ ] **I41-T02: Bound expensive work.** Deliver: Apply selected Git/media process, request and resource limits at receiving boundaries. Acceptance/verification: Exhaustion is denied safely with no committed data loss or bypass through another entry.
- [ ] **I41-T03: Prove reconciliation.** Deliver: Reconcile interrupted reservations and protected references. Acceptance/verification: Retries/crashes do not double-count or delete retained bytes; recorded measurements distinguish assumptions from observed limits.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="issue-38"></a>

### Development order 11: PBI-031 / #38

**Proposed group:** Sprint 04. **Owner:** Farhad. **Prerequisites:** [#2](https://github.com/Farhad-V/Web-Resumefolio/issues/2), [#37](https://github.com/Farhad-V/Web-Resumefolio/issues/37), [#10](https://github.com/Farhad-V/Web-Resumefolio/issues/10).

**Observable outcome:** Run real isolated clients plus OAuth state/PKCE/redirect, current-account revocation, forged/expired/wrong-repo credentials, dumb/anonymous transport denial, paths/header/env/hooks and quota/ref races. Failures require Design revision before enabling Git, never a fake pass.

**Implementation/checklist slices:**

- [ ] **I38-T01: Prove independent identity seam.** Deliver: Build a bounded synthetic Core/Forge SSO/status/API spike under selected issuer/audience/PKCE/current-status contracts. Acceptance/verification: Wrong/reused/expired identity, missing scope, revoked entitlement and unavailable status fail closed.
- [ ] **I38-T02: Prove real native Git.** Deliver: Exercise actual HTTPS Smart HTTP/PAT clone/fetch/push against private test repositories. Acceptance/verification: Verify read/write separation, ref restrictions, no anonymous/dumb HTTP and denied non-fast-forward/deletion cases.
- [ ] **I38-T03: Record G2 disposition.** Deliver: Capture exact configuration, commands, allowed/denied evidence and compatibility findings. Acceptance/verification: Dependent Forge enablement is blocked until mandatory G2 is satisfied; a mock cannot pass this gate.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="sprint-05"></a>

## Sprint 05: Usable private workspace, profile/resume drafts and media

**Status:** proposed; all implementation checks not executed. Candidate slices are defined below; refine exact fixtures, steps and calibrated scope before starting this group.

**Entry:** [#2](https://github.com/Farhad-V/Web-Resumefolio/issues/2), [#10](https://github.com/Farhad-V/Web-Resumefolio/issues/10), [#41](https://github.com/Farhad-V/Web-Resumefolio/issues/41) supply the required accepted dependency evidence.

**Exit/demonstration:** Usable private workspace, profile/resume drafts and media, demonstrated by the item checks below and the common completion rules. Retain failures, unavailable inputs and remaining scope explicitly.

<a id="issue-11"></a>

### Development order 12: PBI-011 / #11

**Proposed group:** Sprint 05. **Owner:** Farhad. **Prerequisites:** [#10](https://github.com/Farhad-V/Web-Resumefolio/issues/10).

**Observable outcome:** Provide authorized navigation and dashboard for Core/manual applications/basic ProjectForge. Keyboard/mobile/language/failure states must not imply unauthorized data or completed external actions.

**Implementation/checklist slices:**

- [ ] **I11-T01: Build authenticated shell.** Deliver: Implement responsive Core navigation and dashboard from selected UI contracts. Acceptance/verification: Anonymous/cross-user entry is denied and empty/loading/error states are truthful.
- [ ] **I11-T02: Verify usable navigation.** Deliver: Check keyboard focus, narrow layouts, zoom and explicit Core/Forge navigation behavior. Acceptance/verification: No private data in client props or accidental shared session; navigation does not imply Forge entitlement.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="issue-12"></a>

### Development order 13: PBI-012 / #12

**Proposed group:** Sprint 05. **Owner:** Farhad. **Prerequisites:** [#10](https://github.com/Farhad-V/Web-Resumefolio/issues/10).

**Observable outcome:** Private Profile, multiple tailored resumes/portfolio, manual English/German variants, selected source preview/apply and independent overrides. Publishing is separately confirmed and stale edits conflict.

**Implementation/checklist slices:**

- [ ] **I12-T01: Edit private profile.** Deliver: Implement validated owner-scoped profile edits with stale-write protection. Acceptance/verification: Cross-user changes and stale saves are denied without overwriting newer content.
- [ ] **I12-T02: Create independent resume drafts.** Deliver: Implement language-specific drafts and selected preview/apply of source changes. Acceptance/verification: Unselected fields and independent draft edits remain intact; source edits do not silently publish.
- [ ] **I12-T03: Verify draft lifecycle.** Deliver: Exercise valid/invalid edits, explicit apply and separate publication intent. Acceptance/verification: Map applicable PRP/BRL criteria; #40 owns atomic publication/history realization.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="issue-13"></a>

### Development order 14: PBI-013 / #13

**Proposed group:** Sprint 05. **Owner:** Farhad. **Prerequisites:** [#2](https://github.com/Farhad-V/Web-Resumefolio/issues/2), [#10](https://github.com/Farhad-V/Web-Resumefolio/issues/10), [#41](https://github.com/Farhad-V/Web-Resumefolio/issues/41).

**Observable outcome:** Same Core server outside public webroot, selected supported video/audio/image/text/PDF formats and safe YouTube embeds. Quarantine/type/dimension checks, private-by-default storage and per-resume selection; upload never publishes.

**Implementation/checklist slices:**

- [ ] **I13-T01: Admit private media.** Deliver: Implement validated owner-scoped upload/quarantine using #41 reservations. Acceptance/verification: Detected type/size, concurrent quotas and unusable incomplete uploads are enforced.
- [ ] **I13-T02: Protect retrieval and association.** Deliver: Implement authorized file association, direct/range delivery and private metadata. Acceptance/verification: Substituted IDs, public paths and another user's artifacts reveal no private bytes.
- [ ] **I13-T03: Retire safely.** Deliver: Implement reference-aware retirement and failure reconciliation. Acceptance/verification: Referenced submitted/publication artifacts remain protected; interrupted/retried operations do not lose committed content.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="sprint-06"></a>

## Sprint 06: Exact PDF variants, atomic publication and protected history

**Status:** proposed; all implementation checks not executed. Candidate slices are defined below; refine exact fixtures, steps and calibrated scope before starting this group.

**Entry:** [#12](https://github.com/Farhad-V/Web-Resumefolio/issues/12), [#13](https://github.com/Farhad-V/Web-Resumefolio/issues/13) supply the required accepted dependency evidence.

**Exit/demonstration:** Exact PDF variants, atomic publication and protected history, demonstrated by the item checks below and the common completion rules. Retain failures, unavailable inputs and remaining scope explicitly.

<a id="issue-14"></a>

### Development order 15: PBI-014 / #14

**Proposed group:** Sprint 06. **Owner:** Farhad. **Prerequisites:** [#12](https://github.com/Farhad-V/Web-Resumefolio/issues/12), [#13](https://github.com/Farhad-V/Web-Resumefolio/issues/13).

**Observable outcome:** Trusted-template Dompdf, EN/DE fonts/page flow, separate generated/uploaded modes and immutable private artifacts. Missing/failed language is explicit; remote resources and arbitrary user HTML are disabled.

**Implementation/checklist slices:**

- [ ] **I14-T01: Generate selected PDFs.** Deliver: Render a selected resume revision/language using trusted Blade templates. Acceptance/verification: Content matches the chosen revision; untrusted content cannot execute; bounded rendering failures are explicit.
- [ ] **I14-T02: Admit uploaded PDFs.** Deliver: Implement private validated uploaded variants and safe replacement. Acceptance/verification: Wrong type/size/language, incomplete processing and quota denial preserve the previous usable artifact.
- [ ] **I14-T03: Verify protected output.** Deliver: Check exact variant availability and private authorized retrieval. Acceptance/verification: No unrelated-language fallback, public artifact leak or silent replacement of historical material.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="issue-40"></a>

### Development order 16: PBI-033 / #40

**Proposed group:** Sprint 06. **Owner:** Farhad. **Prerequisites:** [#12](https://github.com/Farhad-V/Web-Resumefolio/issues/12), [#13](https://github.com/Farhad-V/Web-Resumefolio/issues/13), [#14](https://github.com/Farhad-V/Web-Resumefolio/issues/14).

**Observable outcome:** Source/draft/publication/submission identities, optimistic versions, immutable bytes and protected reference reservations, short local transactions/outbox/idempotency and cleanup reconciliation. Interrupted capture cannot appear complete or delete referenced history.

**Implementation/checklist slices:**

- [ ] **I40-T01: Publish atomically.** Deliver: Implement explicit publication of an exact selected draft/revision and artifact set. Acceptance/verification: Stale/concurrent or interrupted publication cannot expose a partially mixed representation.
- [ ] **I40-T02: Protect historical references.** Deliver: Persist immutable attributable material references and selected history rules. Acceptance/verification: Later profile/PDF edits or retirement do not mutate protected submitted material.
- [ ] **I40-T03: Reconcile uncertain effects.** Deliver: Implement selected version/idempotency/outbox and cleanup rules. Acceptance/verification: Lost responses/retries/crashes do not duplicate effects or prematurely remove protected bytes.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="sprint-07"></a>

## Sprint 07: Protected selected sharing and manual application history

**Status:** proposed; all implementation checks not executed. Candidate slices are defined below; refine exact fixtures, steps and calibrated scope before starting this group.

**Entry:** [#12](https://github.com/Farhad-V/Web-Resumefolio/issues/12), [#13](https://github.com/Farhad-V/Web-Resumefolio/issues/13), [#14](https://github.com/Farhad-V/Web-Resumefolio/issues/14), [#40](https://github.com/Farhad-V/Web-Resumefolio/issues/40) supply the required accepted dependency evidence.

**Exit/demonstration:** Protected selected sharing and manual application history, demonstrated by the item checks below and the common completion rules. Retain failures, unavailable inputs and remaining scope explicitly.

<a id="issue-15"></a>

### Development order 17: PBI-015 / #15

**Proposed group:** Sprint 07. **Owner:** Farhad. **Prerequisites:** [#12](https://github.com/Farhad-V/Web-Resumefolio/issues/12), [#13](https://github.com/Farhad-V/Web-Resumefolio/issues/13), [#14](https://github.com/Farhad-V/Web-Resumefolio/issues/14), [#40](https://github.com/Farhad-V/Web-Resumefolio/issues/40).

**Observable outcome:** Employer views only the selected published resume/media/PDF without owner login. Link/password revocation applies to every future preview/direct/range request; no public storage URL or shared-cache bypass. Any access statistics must be minimal, private and avoid adding new analytics scope.

**Implementation/checklist slices:**

- [ ] **I15-T01: Create protected share.** Deliver: Implement owner-selected published content/language, password and download eligibility. Acceptance/verification: A viewer needs only the selected link/password; no implicit owner or verified-employer identity.
- [ ] **I15-T02: Enforce every delivery path.** Deliver: Apply current share/generation and artifact policy to page/direct/range retrieval. Acceptance/verification: Wrong password, revoked link, changed IDs and forbidden downloads reveal no unauthorized representation.
- [ ] **I15-T03: Verify change and revocation.** Deliver: Exercise owner changes, unavailable variants and subsequent access after revocation. Acceptance/verification: No cross-language fallback; explain that already downloaded bytes cannot be recalled.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="issue-16"></a>

### Development order 18: PBI-016 / #16

**Proposed group:** Sprint 07. **Owner:** Farhad. **Prerequisites:** [#12](https://github.com/Farhad-V/Web-Resumefolio/issues/12), [#14](https://github.com/Farhad-V/Web-Resumefolio/issues/14), [#40](https://github.com/Farhad-V/Web-Resumefolio/issues/40).

**Observable outcome:** Company/opportunity, authored cover letter, manual status, next action and follow-up date. Capture actual submitted immutable bytes/checksums and append corrections/resubmissions; no email/calendar dependency or invented send success.

**Implementation/checklist slices:**

- [ ] **I16-T01: Create private applications.** Deliver: Implement manual job/application data, cover letters, next actions and follow-up dates. Acceptance/verification: Owner-scoped validation and stale-write checks protect another user's records.
- [ ] **I16-T02: Record manual progress.** Deliver: Allow every pair of existing statuses, backward/reopen moves and deliberate same-status events; reason optional. Acceptance/verification: Only explicit authorized action appends immutable actor/old/new/effective/recorded history; stale writes conflict and leaving Offer preserves historical outcome.
- [ ] **I16-T03: Capture actual submitted materials.** Deliver: Associate exact actual artifacts separately from manual status selection. Acceptance/verification: Missing capture is explicitly incomplete without blocking Submitted; no send/receipt claim, and later edits do not change captured materials.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="sprint-08"></a>

## Sprint 08: Scoped production integration and real native Git

**Status:** proposed; all implementation checks not executed. Candidate slices are defined below; refine exact fixtures, steps and calibrated scope before starting this group.

**Entry:** [#10](https://github.com/Farhad-V/Web-Resumefolio/issues/10), [#41](https://github.com/Farhad-V/Web-Resumefolio/issues/41), [#38](https://github.com/Farhad-V/Web-Resumefolio/issues/38) supply the required accepted dependency evidence.

**Exit/demonstration:** Scoped production integration and real native Git, demonstrated by the item checks below and the common completion rules. Retain failures, unavailable inputs and remaining scope explicitly.

<a id="issue-39"></a>

### Development order 19: PBI-032 / #39

**Proposed group:** Sprint 08. **Owner:** Farhad. **Prerequisites:** [#10](https://github.com/Farhad-V/Web-Resumefolio/issues/10), [#38](https://github.com/Farhad-V/Web-Resumefolio/issues/38).

**Observable outcome:** OAuth authorization code + PKCE binds immutable Core identity; independent sessions/databases. Short-lived signed audience/scoped API tokens, local grants and fresh fail-closed Core status checks; correct timeout/retry behavior and no browser service-wide bearer.

**Implementation/checklist slices:**

- [ ] **I39-T01: Implement receiving identity.** Deliver: Replace bounded spike code with selected production-shaped SSO, actor/status and independent-session adapters. Acceptance/verification: Issuer/audience/scope/expiry/PKCE and current active/entitled status are checked at every receiving admission.
- [ ] **I39-T02: Implement scoped API contracts.** Deliver: Implement documented JSON schemas, bounded file metadata/preview/history, errors and idempotency. Acceptance/verification: Validate forbidden fields, stale versions, cursor binding, 8 MiB serialized response budget and unavailable dependencies.
- [ ] **I39-T03: Verify cross-system isolation.** Deliver: Exercise allowed/denied Core-to-Forge operations with real adapters. Acceptance/verification: No direct database shortcut, private-content service scope or positive entitlement cache bypass; retain G2 proof.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="issue-20"></a>

### Development order 20: PBI-020 / #20

**Proposed group:** Sprint 08. **Owner:** Farhad. **Prerequisites:** [#41](https://github.com/Farhad-V/Web-Resumefolio/issues/41), [#38](https://github.com/Farhad-V/Web-Resumefolio/issues/38), [#39](https://github.com/Farhad-V/Web-Resumefolio/issues/39).

**Observable outcome:** Independent ProjectForge native bare Git/Smart HTTP with scoped expiring PATs, current Core status and repository grants; real clone/fetch/pull/push and safe file/history browsing. Dedicated process/path/hook/env isolation; no SSH/user workflow runner.

**Implementation/checklist slices:**

- [ ] **I20-T01: Provision private repositories.** Deliver: Implement native repository ownership, local grants and scoped credentials. Acceptance/verification: Issue write never grants Git write; provisioning failure and revoked grants remain explicit.
- [ ] **I20-T02: Enable real transfers.** Deliver: Implement allowed native clone/fetch/push with selected process/ref/resource policies. Acceptance/verification: Exercise real clients, read-only/write cases, forbidden refs/deletion/force pushes and interrupted operations.
- [ ] **I20-T03: Expose safe file/history views.** Deliver: Implement immutable revision/path browsing and bounded metadata/preview/history. Acceptance/verification: Traversal, symlink/submodule dereference, cross-repository access and oversized/unrepresentable output are safely denied.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="sprint-09"></a>

## Sprint 09: Repository issues/fixed board and account lifecycle

**Status:** proposed; all implementation checks not executed. Candidate slices are defined below; refine exact fixtures, steps and calibrated scope before starting this group.

**Entry:** [#10](https://github.com/Farhad-V/Web-Resumefolio/issues/10), [#13](https://github.com/Farhad-V/Web-Resumefolio/issues/13), [#40](https://github.com/Farhad-V/Web-Resumefolio/issues/40), [#39](https://github.com/Farhad-V/Web-Resumefolio/issues/39), [#20](https://github.com/Farhad-V/Web-Resumefolio/issues/20) supply the required accepted dependency evidence.

**Exit/demonstration:** Repository issues/fixed board and account lifecycle, demonstrated by the item checks below and the common completion rules. Retain failures, unavailable inputs and remaining scope explicitly.

<a id="issue-22"></a>

### Development order 21: PBI-022 / #22

**Proposed group:** Sprint 09. **Owner:** Farhad. **Prerequisites:** [#39](https://github.com/Farhad-V/Web-Resumefolio/issues/39), [#20](https://github.com/Farhad-V/Web-Resumefolio/issues/20).

**Observable outcome:** Authorized issue creation, updates, assignee and repository context. Basic issue access does not grant repository writes. Milestone/release management and advanced collaboration UI are outside product MVP; GitHub project Milestones used to manage this work are unrelated.

**Implementation/checklist slices:**

- [ ] **I22-T01: Create repository issues.** Deliver: Persist fixed-schema issue fields and repository-local numbering. Acceptance/verification: Validate title/body, assignee eligibility, priority and paired due date/timezone; repository authority is current.
- [ ] **I22-T02: Update and list safely.** Deliver: Implement versioned/idempotent updates and bounded cursor lists. Acceptance/verification: Concurrent creates/updates, retries and cross-repository substituted IDs cannot duplicate or overwrite unauthorized work.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="issue-19"></a>

### Development order 22: PBI-019 / #19

**Proposed group:** Sprint 09. **Owner:** Farhad. **Prerequisites:** [#22](https://github.com/Farhad-V/Web-Resumefolio/issues/22).

**Observable outcome:** Fixed To do / In progress / Done board for authorized issues, explicit assignee/priority/due date, safe movement and membership changes. General backlog/Sprints/configurable column workflows are after MVP.

**Implementation/checklist slices:**

- [ ] **I19-T01: Project issues onto fixed board.** Deliver: Implement To do/In progress/Done using the same repository issue objects. Acceptance/verification: A move changes issue state only; no duplicate task, custom column, Sprint product feature or new Git permission.
- [ ] **I19-T02: Verify board interaction.** Deliver: Implement accessible move controls and stale/denied/error recovery. Acceptance/verification: Keyboard move and cross-user/concurrent cases preserve the persisted issue and truthful UI state.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="issue-24"></a>

### Development order 23: PBI-024 / #24

**Proposed group:** Sprint 09. **Owner:** Farhad. **Prerequisites:** [#10](https://github.com/Farhad-V/Web-Resumefolio/issues/10), [#13](https://github.com/Farhad-V/Web-Resumefolio/issues/13), [#40](https://github.com/Farhad-V/Web-Resumefolio/issues/40).

**Observable outcome:** Current account revocation, private-content policies, 30-day trash, reference-aware cleanup and bounded append-only audit metadata. Preserve actual history and reapply deletion/revocation after restore; no admin implicit content access.

**Implementation/checklist slices:**

- [ ] **I24-T01: Complete account lifecycle.** Deliver: Implement selected suspension/disable/retirement behavior and current Core/Forge admission revocation. Acceptance/verification: Earlier session/page/queued work cannot bypass current account or entitlement state.
- [ ] **I24-T02: Enforce retention and retirement.** Deliver: Implement selected content/reference lifecycle with protected history and compatible recovery. Acceptance/verification: Retirement cannot remove protected bytes or silently grant administrative content access.
- [ ] **I24-T03: Record safe audit.** Deliver: Persist attributable administrative/lifecycle outcomes and failure diagnostics. Acceptance/verification: Allowed/denied actions have safe evidence without tokens/private payloads; retry/concurrency preserves one attributable effect.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="sprint-10"></a>

## Sprint 10: Integrated criterion evidence and isolated restore

**Status:** proposed; all implementation checks not executed. Candidate slices are defined below; refine exact fixtures, steps and calibrated scope before starting this group.

**Entry:** [#6](https://github.com/Farhad-V/Web-Resumefolio/issues/6), [#11](https://github.com/Farhad-V/Web-Resumefolio/issues/11), [#40](https://github.com/Farhad-V/Web-Resumefolio/issues/40), [#15](https://github.com/Farhad-V/Web-Resumefolio/issues/15), [#16](https://github.com/Farhad-V/Web-Resumefolio/issues/16), [#39](https://github.com/Farhad-V/Web-Resumefolio/issues/39), [#20](https://github.com/Farhad-V/Web-Resumefolio/issues/20), [#19](https://github.com/Farhad-V/Web-Resumefolio/issues/19), [#24](https://github.com/Farhad-V/Web-Resumefolio/issues/24) supply the required accepted dependency evidence.

**Exit/demonstration:** Integrated criterion evidence and isolated restore, demonstrated by the item checks below and the common completion rules. Retain failures, unavailable inputs and remaining scope explicitly.

<a id="issue-25"></a>

### Development order 24: PBI-025 / #25

**Proposed group:** Sprint 10. **Owner:** Farhad. **Prerequisites:** [#11](https://github.com/Farhad-V/Web-Resumefolio/issues/11), [#15](https://github.com/Farhad-V/Web-Resumefolio/issues/15), [#16](https://github.com/Farhad-V/Web-Resumefolio/issues/16), [#39](https://github.com/Farhad-V/Web-Resumefolio/issues/39), [#19](https://github.com/Farhad-V/Web-Resumefolio/issues/19), [#24](https://github.com/Farhad-V/Web-Resumefolio/issues/24).

**Observable outcome:** Run requirement-linked positive/denied/stale/failure/regression journeys against the identified candidate; intended actor review and complete sanitized evidence. Deferred provider/review/runner paths are not release prerequisites.

**Implementation/checklist slices:**

- [ ] **I25-T01: Run integrated journeys.** Deliver: Execute selected invited access, profile/resume/PDF/share/application and Forge Git/issue journeys. Acceptance/verification: Map each actual result to exact applicable RTM criterion, candidate and environment; mocks are explicitly limited.
- [ ] **I25-T02: Run adversarial/regression cases.** Deliver: Exercise cross-user/direct-byte denial, stale/retry/concurrent/interrupt cases and manual history policy. Acceptance/verification: Failures remain blockers/follow-ups; no broad family-level pass replaces criterion evidence.
- [ ] **I25-T03: Review acceptance evidence.** Deliver: Walk through demonstrated scope with the owner and record disposition. Acceptance/verification: Do not invent owner acceptance, legal compliance or release approval; independently authorized review remains required.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="issue-27"></a>

### Development order 25: PBI-027 / #27

**Proposed group:** Sprint 10. **Owner:** Farhad. **Prerequisites:** [#6](https://github.com/Farhad-V/Web-Resumefolio/issues/6), [#40](https://github.com/Farhad-V/Web-Resumefolio/issues/40), [#20](https://github.com/Farhad-V/Web-Resumefolio/issues/20), [#24](https://github.com/Farhad-V/Web-Resumefolio/issues/24).

**Observable outcome:** Timed isolated encrypted backup restore of both systems, immutable artifacts, Git refs, current grants/deletion/revocation and outbox without external replay. Test code rollback separately from data recovery.

**Implementation/checklist slices:**

- [ ] **I27-T01: Capture coherent candidate.** Deliver: Back up identified Core/Forge databases, artifacts and native Git with independently protected keys. Acceptance/verification: Inventory and capture consistency identify one restorable candidate; no real private data in shared proof.
- [ ] **I27-T02: Restore in isolation.** Deliver: Verify resolved target, restore into isolated stores and run access/history/Git integrity checks. Acceptance/verification: No production overwrite; restored protected artifacts and revoked/allowed access behave consistently.
- [ ] **I27-T03: Exercise recovery.** Deliver: Demonstrate selected rollout/rollback or recovery procedure and record limitations. Acceptance/verification: Actual recovery results meet selected policy or remain explicit failed/unverified gates.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="sprint-11"></a>

## Sprint 11: Measured quality and usable operating guidance

**Status:** proposed; all implementation checks not executed. Candidate slices are defined below; refine exact fixtures, steps and calibrated scope before starting this group.

**Entry:** [#41](https://github.com/Farhad-V/Web-Resumefolio/issues/41), [#25](https://github.com/Farhad-V/Web-Resumefolio/issues/25), [#27](https://github.com/Farhad-V/Web-Resumefolio/issues/27) supply the required accepted dependency evidence.

**Exit/demonstration:** Measured quality and usable operating guidance, demonstrated by the item checks below and the common completion rules. Retain failures, unavailable inputs and remaining scope explicitly.

<a id="issue-26"></a>

### Development order 26: PBI-026 / #26

**Proposed group:** Sprint 11. **Owner:** Farhad. **Prerequisites:** [#41](https://github.com/Farhad-V/Web-Resumefolio/issues/41), [#25](https://github.com/Farhad-V/Web-Resumefolio/issues/25).

**Observable outcome:** Measure selected T09 workload, latency/error limits, browser/keyboard/zoom and WCAG target plus PDF bounds and disk quotas. Targets are not prior measurements and no 30-day availability result is invented.

**Implementation/checklist slices:**

- [ ] **I26-T01: Measure selected workload.** Deliver: Run T09 workload/latency/error, PDF and storage-admission scenarios on an identified candidate. Acceptance/verification: Record actual measurements versus selected thresholds, concurrent/exhaustion behavior and environment limits.
- [ ] **I26-T02: Verify browser/accessibility matrix.** Deliver: Run selected browser, keyboard, focus, zoom and accessibility checks across implemented journeys. Acceptance/verification: Defects have reproduction and follow-up; automated scanning alone does not establish the whole target.
- [ ] **I26-T03: Review quality gates.** Deliver: Summarize actual G5 evidence and blockers. Acceptance/verification: No invented availability history or claim that late integrated checks replace tests within each feature.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="issue-28"></a>

### Development order 27: PBI-028 / #28

**Proposed group:** Sprint 11. **Owner:** Farhad. **Prerequisites:** [#25](https://github.com/Farhad-V/Web-Resumefolio/issues/25), [#27](https://github.com/Farhad-V/Web-Resumefolio/issues/27).

**Observable outcome:** Document real clean Setup/run/test, actual interfaces, user/admin flows, backup/restore, patching and operational response; link candidate-specific evidence. Keep documentation current with implementation.

**Implementation/checklist slices:**

- [ ] **I28-T01: Write from observed behavior.** Deliver: Align user/admin/setup/operating guidance with the verified candidate and actual commands. Acceptance/verification: Walk through safe examples against the candidate; no secret, unsupported feature or unexecuted command is called verified.
- [ ] **I28-T02: Exercise operating guidance.** Deliver: Check incident, backup, recovery and lifecycle instructions against #27 evidence. Acceptance/verification: Document exact limitations and unresolved actions; another clean checkout/operator walkthrough finds no contradictory route or prerequisite.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

<a id="sprint-12"></a>

## Sprint 12: Reviewed release candidate and separately authorized deployment

**Status:** proposed; all implementation checks not executed. Candidate slices are defined below; refine exact fixtures, steps and calibrated scope before starting this group.

**Entry:** [#25](https://github.com/Farhad-V/Web-Resumefolio/issues/25), [#27](https://github.com/Farhad-V/Web-Resumefolio/issues/27), [#26](https://github.com/Farhad-V/Web-Resumefolio/issues/26), [#28](https://github.com/Farhad-V/Web-Resumefolio/issues/28) supply the required accepted dependency evidence.

**Exit/demonstration:** Reviewed release candidate and separately authorized deployment, demonstrated by the item checks below and the common completion rules. Retain failures, unavailable inputs and remaining scope explicitly.

<a id="issue-29"></a>

### Development order 28: PBI-029 / #29

**Proposed group:** Sprint 12. **Owner:** Farhad. **Prerequisites:** [#25](https://github.com/Farhad-V/Web-Resumefolio/issues/25), [#27](https://github.com/Farhad-V/Web-Resumefolio/issues/27), [#26](https://github.com/Farhad-V/Web-Resumefolio/issues/26), [#28](https://github.com/Farhad-V/Web-Resumefolio/issues/28).

**Observable outcome:** Before any deployment confirm required gate evidence, actual candidate, credentials/TLS, compatible migrations, tested recovery and owner Release decision. Then execute the separately reviewed deployment procedure and record live checks. Creating this issue performs no deployment.

**Implementation/checklist slices:**

- [ ] **I29-T01: Prepare release decision.** Deliver: Assemble exact scope, all applicable gate evidence, license/privacy adoption dispositions and known blockers. Acceptance/verification: Candidate/revision and compatible rollout/recovery plan are identified; unmet required gates prevent release.
- [ ] **I29-T02: Deploy only under explicit authorization.** Deliver: Execute the separately authorized initial rollout with safe configuration and recovery readiness. Acceptance/verification: Record real deployment revision, live smoke results and rollback/recovery disposition; planning this task does not authorize deployment.
- [ ] **I29-T03: Handover observed operations.** Deliver: Record release decision, limitations, operating guidance and maintenance follow-ups. Acceptance/verification: No invented approval, release success or closed incident; only demonstrated outcomes are accepted.

**Evidence/exit:** apply the common completion rules and the exact applicable criteria already retained on this issue. Each executed check records criterion, candidate revision, environment, expected/actual outcome and sanitized evidence. All checkboxes remain pending until demonstrated.

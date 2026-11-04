# Requirements and policy decisions

**BL-MVP-2026-11-04.1 — November 4, 2026.** Selected on November 4, 2026 by Codex under Farhad’s explicit instruction to complete technical decisions and establish the Baseline. This is delegated design authority; no personal owner review, running implementation, deployment or product test is fabricated.

These dispositions supersede the November 1 proposed answers only within MVP. Selected specification is distinct from demonstrated user validation, runtime capability and Release acceptance. [Implementation gates](implementation-sequence.md) assign those obligations.

<a id="q-d01"></a>
## Q-D01 — Identifiers, priorities and criterion-level traceability

**Disposition: Selected.** Retain all 157 candidate IDs and 470 criterion locators. The two Baseline CSV registers define current applicability and Must-within-MVP / Later priority; no ID is renumbered. Record test IDs/results per criterion during implementation. Mixed criteria are explicitly narrowed; excluded domains are never implicitly accepted.

<a id="q-d02"></a>
## Q-D02 — Actor outcomes and user validation

**Disposition: Specification selected; user validation gate.** Select the existing Core/basic ProjectForge actor journeys including denial/failure/recovery. Employer uses a password link without an account; only invited users enter private areas. Intended actor walkthrough remains G6; no user validation is asserted.

<a id="q-d03"></a>
## Q-D03 — Identity, onboarding and account lifecycle

**Disposition: Selected.** T02 fixes onboarding, factors, password/session/recovery timings. Operator SMTP is required for system invitations/recovery and is independent of deferred personal Gmail; use Laravel Mail with authenticated SMTP, local log transport only in development. Verify actual receipt at G4.

<a id="q-d04"></a>
## Q-D04 — Resource grants and administration powers

**Disposition: Selected.** T02/T03/T04 default-deny resource grants. Core private data belongs to its user; Admin has no implicit content access. Repo owner manages grants; writer pushes; reader fetches/browses; issue access does not imply repo write. Account disable terminates new admissions; resource transfer requires current owner confirmation and explicit grant re-evaluation.

<a id="q-d05"></a>
## Q-D05 — Active access, credentials and revocation

**Disposition: Selected.** Every new protected request checks current subject/resource/link generation; Core invalidates sessions on reset/disable. ProjectForge checks Core status for browser/API/Git access. Deny stale credentials. Already delivered bytes cannot be recalled. No shared public download/cache bypass.

<a id="q-d06"></a>
## Q-D06 — Professional fields and resume composition

**Disposition: Selected.** Allow incomplete private drafts. Publishing requires a display name, a contact method and one selected resume section with meaningful content. Preserve ordered section entries, explicit selected profile values and independent per-resume overrides. No mandatory sensitive demographic fields.

<a id="q-d07"></a>
## Q-D07 — Shared updates, overrides and publication

**Disposition: Selected.** Source, independent resume draft, immutable publication and actual submission are separate identities. Preview/select/apply never publishes automatically. Use T05 optimistic versions, transactions, protected artifact references and outbox.

<a id="q-d08"></a>
## Q-D08 — Evidence, media and external-content handling

**Disposition: Selected.** T06 selects private supported files, no automatic publication, per-resume selection and explicit YouTube embed contact. Validate/canonicalize known YouTube IDs; never fetch arbitrary external URLs. Unsupported formats/codecs are rejected, not silently converted.

<a id="q-d09"></a>
## Q-D09 — Manual language variants and fallback

**Disposition: Selected.** English and German are manually authored variants. Store language on draft/publication/PDF. Missing requested language is explicitly unavailable; no silent fallback or automatic translation. Store timestamps in UTC with explicit user timezone rendering; follow-up date stays a date in that timezone.

<a id="q-d10"></a>
## Q-D10 — PDF rendition and download contracts

**Disposition: Selected.** T06 selects Dompdf and immutable generated artifacts. Keep generated versus uploaded PDF mode and language explicit per resume; absent/failed rendition is unavailable, never substituted silently. No arbitrary template HTML or remote rendering.

<a id="q-d11"></a>
## Q-D11 — Employer link/password lifecycle

**Disposition: Selected.** Use at least 32 random bytes for opaque employer link identity and hashed password under T02 policy. Viewer session is scoped to one resume/link generation for 30 minutes idle / 8 hours absolute. Password change/disable bumps generation and invalidates future requests. Rate limit 5 failed attempts per link/IP per 15 minutes plus 30 per IP globally. Links remain active until owner disables them; optional expiry must be enforced if set. Never leak token/password in logs/referrers.

<a id="q-d12"></a>
## Q-D12 — Application fields and progress

**Disposition: Selected.** Manual states: Preparing, Ready, Submitted, Interview, Offer, Rejected, Withdrawn. Offer outcome may be accepted/declined. Record company/opportunity/title, selected resume, authored cover letter, status, next action and follow-up date. Warn on potential duplicate; do not forbid legitimate resubmission. External send is not implied by a state edit.

<a id="q-d13"></a>
## Q-D13 — Actual submitted-set capture

**Disposition: Selected.** Capture actual selected submitted bytes plus SHA-256, language/mode and submission context. T05 reservation/commit/outbox preserves consistency. If capture fails, do not report a completed submitted set; retain a recoverable draft/failure record.

<a id="q-d14"></a>
## Q-D14 — Correction, resubmission and retained history

**Disposition: Selected.** Corrections append attributed history rather than overwriting actual prior submitted material. Archive is reversible. Soft-delete private drafts/application records for 30 days, then delete only unreferenced eligible data; explicit permanent account/content erasure removes owned live copies and respects other owners’ independent copies. Do not promise erasure from existing encrypted backups before their retention expiry; restored systems must reapply deletion/revocation records before access.

<a id="q-d15"></a>
## Q-D15 — Google access and external conditions

**Disposition: Deferred after MVP.** No Gmail/Calendar connection is required for MVP. Future independent communications service requires per-user/account consent and least scopes, no admin private mail access. Actual provider verification/credentials remain future gates.

<a id="q-d16"></a>
## Q-D16 — Mail views, drafts, send and uncertain outcomes

**Disposition: Deferred after MVP.** Personal mail views/drafts/send and uncertain provider outcomes remain future communications work. MVP cover letters/submission history are manual and never claim an email was sent.

<a id="q-d17"></a>
## Q-D17 — Calendar, synchronization and disconnection

**Disposition: Deferred after MVP.** Provider calendar synchronization/disconnection is deferred. MVP manual follow-up dates require no provider connection.

<a id="q-d18"></a>
## Q-D18 — Work structures, fields and workflows

**Disposition: Selected MVP slice.** ProjectForge issues with title, description, assignee, explicit repo reference when authorized and To do / In progress / Done board. No general advanced backlog or customizable Sprint workflow in MVP.

<a id="q-d19"></a>
## Q-D19 — Sprint Backlog, completion and end behavior

**Disposition: Deferred after MVP.** Sprint Backlog, Sprint-end semantics and advanced work planning are preserved as future specifications.

<a id="q-d20"></a>
## Q-D20 — Cross-module links, reporting and automation

**Disposition: Selected MVP slice.** Core dashboard shows only authorized Core/manual-application and basic ProjectForge information through user-scoped API. Provider reporting, cross-module automation and advanced Sprint reporting are deferred. No shared database or implicit grant propagation.

<a id="q-d21"></a>
## Q-D21 — Real Git clients, credentials and repository policy

**Disposition: Selected design; capability gate.** T03/T04 select native Smart HTTP, PATs, current account checks and separate process boundaries. G2 must demonstrate real transfers and denial/isolation. Engine choice is complete; capability evidence remains unexecuted.

<a id="q-d22"></a>
## Q-D22 — Git review, merge, tracking and releases

**Disposition: Selected issues; advanced Git deferred.** Basic issues/simple Kanban are MVP. Fork/review/merge/milestone/release UI and advanced policies are deferred. Normal Git refs required for client transfers remain subject to MVP authorization and protected-ref rules.

<a id="q-d23"></a>
## Q-D23 — Workflow contract, isolation, secrets and target controls

**Disposition: Deferred after MVP.** No user YAML workflow execution, deployment agent, user code runner or secret injection in MVP. Future sandbox/target/provider decisions remain open only for that later scope.

<a id="q-d24"></a>
## Q-D24 — Effective file policy, quotas and administrative evidence

**Disposition: Selected; capacity gate.** T06 selects file types, exact per-file/user/global limits, reservations and disk reserve. T07 audit/rotation bounds apply. Test effective enforcement and actual target headroom at G2/G5 before admitting production data.

<a id="q-d25"></a>
## Q-D25 — Quantitative quality, client and accessibility targets

**Disposition: Selected targets; measurement gate.** T09 selects browsers, WCAG target, load mix and numerical performance/PDF/SLO thresholds. Collect actual results at G5; targets are not measurements.

<a id="q-d26"></a>
## Q-D26 — Backup, retention, consistent recovery and restored access

**Disposition: Selected design; restore gate.** T08 selects encrypted independent workstation restic backups, coordinated capture, 7 daily/4 weekly retention, RPO 24h and RTO 8 operator working hours. Actual destination/key/schedule/isolated restore are G4, not a documentation Pass.

<a id="q-d27"></a>
## Q-D27 — Operating dependencies, applicability and maintenance

**Disposition: Selected; operational inputs gate.** T01/T07/T08 select runtime, queues, SMTP and same-host independent service topology. Actual domain/TLS/SMTP/backup destination secrets and host capacity are operational inputs at G1/G4/G5. Review dependencies monthly; pin supported patches and licenses. Future providers do not block Setup.

<a id="q-d28"></a>
## Q-D28 — Forecast, downstream reconciliation and baseline candidate

**Disposition: Selected Baseline; no delivery forecast.** Baseline BL-MVP-2026-11-04.1 selects scope/policies/technical choices and task sequence. Keep 20 total project hours/week. Estimate work packages after Setup/Git spike evidence; historical larger-scope estimates and dates are not current MVP commitments. User validation and runtime/release gates remain visible.

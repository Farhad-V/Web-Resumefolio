# Deployment Runbook

[Deployment Plan](01-Deployment-Plan.md) · [Release Notes](03-Release-Notes.md)

**Draft / not rehearsed.** Actual host-specific commands, paths, service identities, backup set and verified operating results remain unrecorded. This is a reviewable procedure with stop conditions, not an executable production script. Add commands only after successful authorized rehearsal in the identified environment.

## Execution Record and Preconditions

| Input | Required value before rollout | Current record |
| --- | --- | --- |
| Authority / target | Actual authorized executor and intended environment | Pending |
| Candidate | Approved exact revision/build, locks and artifact identity | Pending |
| Configuration | Reviewed non-secret identity plus independently supplied secrets | Pending |
| Storage / database | Verified owner-local schema/users/private roots and permissions | Pending |
| Migration | Reviewed set, code/data compatibility and observed rehearsal result | Pending |
| Backup | Protected usable coherent backup and actual isolated restore evidence | Pending |
| Recovery | Compatible code rollback or approved data recovery with explicit stop rules | Pending |
| Work/traffic handling | Verified in-flight requests, writes, workers/scheduler and pending-effect policy | Pending |
| Smoke checks | Actual executable cases/fixtures and expected results | Pending |

Do not target production/demo data implicitly. Confirm resolved paths/users/databases before migration, reset, move or restore. Keep secret values out of shell/evidence output. A missing critical prerequisite stops execution.

## Step 1 — Identify and Verify the Candidate

Confirm exact source/build and dependency/configuration/migration identity against release approval. Check required criterion/gate evidence and known limitations. Verify the intended previous known-good revision and whether it remains compatible with the candidate schema/data/pending work.

Record actual working directory, command, target, expected response and observed rehearsal result for every executable step. Do not paste generic framework commands and label them tested.

## Step 2 — Prepare Environment and Recovery

Verify independent Core/ProjectForge keys, sessions, database credentials and private paths, intended service scopes, TLS/routing and real process privileges. Confirm protected backup coverage of records, exact artifacts, native repositories and required operating secrets/configuration.

Validate isolated restore and relevant integrity/access checks before relying on the backup. Establish actual traffic/write/worker pause/drain/restart behavior; avoid replaying effects or running incompatible jobs against changed data. Required numeric settings/targets follow governing criteria, not invented runbook defaults.

## Step 3 — Apply Reviewed Rollout

Follow the rehearsed ordering for migrations, application activation, built frontend assets and owner-local process configuration. Check actual result at each checkpoint. Do not infer rollback safety from a successful DDL command or silently continue through partial migration failure.

If a command targets the wrong environment, integrity becomes uncertain or an unexpected effect appears, stop affected activity and preserve necessary evidence. Diagnose before retrying. Local transaction failure does not prove filesystem/Git/remote rollback.

## Step 4 — Verify Revision and Essential Journeys

| Smoke area | Required outcome |
| --- | --- |
| Identity / routing | Intended apps/revision/assets and receiving-session behavior |
| Private authority | Wrong-owner/direct paths denied; allowed content remains available |
| Professional materials | Applicable explicit draft/publication distinction and exact submitted history |
| Sharing/files | Current selected content/language/download eligibility; private roots not exposed |
| ProjectForge | Required scoped API/status, current grants and evaluated native Git behavior |
| Workers/mail | Correct owner/revision/configuration, visible processing/failure and controlled actual delivery where applicable |
| Persistence/resources | Intended database/private storage, migration state and selected disk/resource controls |
| Diagnostics | Bounded health/correlation/failure signals without secret/private payloads |

Select concrete synthetic fixtures and executable checks in rehearsal. Avoid casually altering real user content to obtain a smoke result. Record actual case, revision, environment and observation, not only a checklist tick.

## Deployment and Rollback Decision Points

| Checkpoint | Continue when | Stop / recover when |
| --- | --- | --- |
| Before rollout | Candidate approved, targets correct and recovery prerequisites usable | Required input, evidence or authorization missing |
| After migration | Actual migration succeeded and required code/data/work compatibility holds | Failure, partial state, integrity uncertainty or unsafe prior-code compatibility |
| After promotion | Intended revision, health and essential journeys pass | Authentication, private access, data/history or other essential checks fail |

## Step 5 — Contain and Recover When Required

| Recovery path | Preconditions / action | Required verification |
| --- | --- | --- |
| Code rollback | Previous revision compatible with current schema/data/pending work; authorized runbook procedure | Repeat revision, health and essential journey checks |
| Data restore | Recovery necessary; affected writes paused; incident evidence preserved; approved isolated-tested procedure | Consistent records/private bytes/digests/Git, intended access and safe pending work before resumption |
| Owner reconciliation | Recorded outcome differs from actual file/Git/remote state or remains uncertain | Resolve same operation identity without duplicate effect or premature reference release |

Do not restore production data automatically or infer permission from this draft. A restore can discard later writes. Code rollback cannot recall bytes/mail or undo every Git/remote effect. Account for changed/revoked authority and pending jobs before replay or cleanup.

## Step 6 — Record Outcome and Handoff

Record trigger, actual revision/configuration/environment, commands/results, smoke observations, failure/containment, recovery decision and verified outcome. Keep unresolved issues/gates visible and link the owning work item/RTM. Exclude secrets and unnecessary private data.

Use the [release/deployment gate view](01-Deployment-Plan.md#release-and-deployment-decision-flow) and [Release Notes](03-Release-Notes.md) for the separate product/publication record. Carry verified procedures and remaining operating issues into Maintenance. No rollout, rollback, restore or release publication has been performed by writing this runbook.

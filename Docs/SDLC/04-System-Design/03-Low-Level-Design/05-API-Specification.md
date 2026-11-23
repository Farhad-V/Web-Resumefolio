# 5. API Specification

[Previous: Database Design](04-Database-Design.md) · [Low-Level Design introduction](01-Introduction.md) · [Next: Algorithms and Business Rules](06-Algorithms-And-Business-Rules.md)

<a id="api-specification"></a>

## Contract Coverage

The MVP contract section lists routes, request and response fields, status codes and caller authority. Keep the endpoint-specific checks with the work item.

## MVP API contracts

The versioned JSON interface is server-to-server. Browser UI uses each application's Laravel session and Inertia; native Git uses its separate authorized transport. Core signs scoped calls to ProjectForge. On every protected call, ProjectForge verifies the current Core entitlement and the local resource grant. Service credentials for Core identity status grant access only to status, never content. The paths below are proposed implementation names.

| Operation | Request | Success response and obligations |
| --- | --- | --- |
| GET /internal/v1/accounts/{userId}/projectforge-status | Status-only service credential; Core subject UUID | 200 with userId, active and entitled. Use the bounded status timeout and fail closed when the service is unavailable. |
| GET /api/v1/repositories | Scoped actor token and optional opaque cursor | 200 with permitted repository summaries and nextCursor. Stable cursor ordering; never return unauthorized repositories. |
| GET /api/v1/repositories/{repositoryId}/files | Scoped read token, immutable revision and optional repository-relative path | 200 with authorized entries and resolved revision; results contain no host path. |
| GET /api/v1/repositories/{repositoryId}/history | Scoped read token, revision and optional cursor | 200 with commit summaries for the permitted repository, resolved revision and nextCursor. |
| GET /api/v1/repositories/{repositoryId}/issues | Scoped issue-read token, optional state and cursor | 200 with repository-scoped issues, their versions and nextCursor. |
| POST /api/v1/repositories/{repositoryId}/issues | Scoped issue-write token, Idempotency-Key, title, body and optional priority, assignee and due date | 201 with stable issue ID, repository issue number and version. Issue authority does not grant Git write. |
| PATCH /api/v1/repositories/{repositoryId}/issues/{issueId} | Scoped issue-write token, Idempotency-Key, expectedVersion and changed fields | 200 with updated issue and version. Supports a fixed board move using state. A stale version produces a conflict without overwriting the later change. |

Issue states are todo, in_progress and done. Priorities are low, normal and high. An issue response contains id, number, title, state, priority, assigneeId, dueDate and version. A repository summary contains id and display name. History returns immutable revision identifiers. Dates carried as local dates include their time-zone context where applicable.

Return 401 for invalid identity, 403 for a forbidden visible action, 404 for missing or hidden resources, 409 for stale writes or mismatched idempotency payloads, 422 for invalid input and 503 when required authority cannot be checked. Errors expose a stable code and correlation ID. Do not include private content or storage paths. Bind write keys to actor, operation and payload and return the stored outcome for a matching retry. Reconcile uncertain outcomes before any repeat that could duplicate effects. Verify these contracts with allowed, denied, invalid, stale and interrupted requests.

## 5.1 Interface Scope and Authority

The route table above is the selected MVP contract direction with proposed implementation names. It is not a deployed route inventory or an executed compatibility result. Internal module operations need not become HTTP endpoints. Browser/Inertia, protected file delivery, scoped JSON and native Git retain distinct authentication and response contracts.

| Interface | Caller context | Required receiving checks |
| --- | --- | --- |
| Core entitlement status | Narrow service credential and Core issuer/subject identity | Authenticate permitted service access; disclose only current account/entitlement status |
| ProjectForge JSON | Signed scoped actor request from Core | Caller/token scope, current Core entitlement and local repository/action authority |
| Browser workspace | Receiving Laravel session | Current account/resource/action policy, validated inputs and applicable state-change protection |
| Protected recipient/file | Current link/viewer context | Selected publication/content/language, eligible download and current direct-delivery policy |
| Native Git | Evaluated transport credential and repository/action scope | Current entitlement and local grants for the actual native operation |

A scoped service credential is not universal human authority. Status access cannot read professional content. Issue-write permission does not authorize Git push. Required current authority unavailable returns the documented safe unavailable outcome instead of permission inferred from previous access.

## 5.2 Request and Response Field Contract

| Field / concept | Meaning and validation |
| --- | --- |
| Actor and scope | Bind to the authenticated caller's permitted context; never trust an arbitrary payload user identifier as authority |
| Repository / issue ID | Public stable resource identity with current visibility/action policy; no host storage path |
| Immutable revision | Resolve the exact requested repository revision for files/history; response identifies the resolved content context |
| Repository-relative path | Validate relative-path semantics and permitted repository content; reject traversal/out-of-scope access |
| Opaque cursor | Preserve documented stable ordering and authorized result scope; client does not manufacture a database offset contract |
| `Idempotency-Key` | Required for listed writes; bind actor/operation/payload and resolve matching recorded outcome |
| `expectedVersion` | Required for listed mutable issue update; compare within owning write transaction |
| Issue fields | Validate selected state/priority values, field limits, assignee eligibility and temporal meaning under the owning contract |
| Correlation ID / stable error code | Bounded diagnostic linkage, not an access credential or sensitive payload |

The [concrete MVP schemas](#mvp-json-schemas) specify required/optional/null fields, types, bounds, unknown-field policy and PATCH clearing. The [error and retry contract](#mvp-json-errors-and-retries) fixes the JSON error shape, recorded-result semantics and synthetic examples. Implement and verify these contracts rather than inferring behavior from UI appearance.

Issue creation/update returns only permitted fields. Preserve stable issue identity and repository issue number through board moves. Dates that are local/date-only retain their intended meaning and applicable context; do not convert them arbitrarily into instants. The database design governs storage, not an unreviewed JSON serialization guess.

## 5.3 Error Mapping and Information Hiding

| JSON status | Contract use | Client behavior |
| --- | --- | --- |
| `401` | Invalid identity | Establish the permitted receiving context; no business mutation assumed |
| `403` | Forbidden visible action | Explain bounded restriction without offering a bypass |
| `404` | Missing or hidden resource | Do not disclose private existence through alternate wording/payload |
| `409` | Stale write or mismatched repeated payload | Review current state or correct request-identity misuse; no blind overwrite |
| `422` | Invalid input | Correct field/selection using permitted validation details |
| `503` | Required authority cannot be checked | Safe unavailable outcome; do not use stale/broad authority |

These are the documented categories, not a full enumeration of every possible infrastructure response. Define transport/body-size/rate-limit behavior in actual endpoint configuration when applicable; do not fabricate guarantees or status mappings here. Native Git and file/browser entry paths use their own protocol behavior.

A rejection has no unauthorized business effect; necessary bounded audit metadata may still be recorded. Network failure/lost response is not a definitive business rejection and may follow a remote commit. Exclude secrets, private bytes, stack traces and host paths from client errors.

## 5.4 Idempotency, Concurrency and Uncertain Completion

For listed writes, validate current authority and bind stable request identity to actor, operation and payload. A matching retry resolves the stored outcome under that contract; a different payload reusing the key conflicts. Concurrent same-key requests must not both create independent effects. Expected-version checks protect mutable state separately from request identity.

Retain recorded outcomes and related protection through pending/uncertain work. If a response disappears, resolve the same operation before a repeat that could duplicate an issue or other effect. Do not infer remote rollback from a local exception or automatically replay every error. T05 selects seven-day outcome retention; pending/uncertain protection and late retries follow the [concrete retry contract](#mvp-json-errors-and-retries).

Each application commits locally. Durable work/outbox supports attributable asynchronous effects where selected; queue acceptance does not prove completion. Current authority and preserved separately recorded outcomes remain required on recovery. Filesystem/Git/mail effects do not become atomic with local SQL.

## 5.5 Pagination, Revision and Content Delivery

Repository/issue list results contain only permitted resources with stable contract-defined order/cursor behavior. Validate filters and cursor context and document invalid/stale cursor behavior in the concrete schema. Apply current authority to subsequent pages; a previous cursor cannot confer access after revocation.

File/history queries distinguish immutable revision identity from mutable branch/head selection. Return the resolved revision and permitted repository-relative data without exposing host paths. Protected Core media/PDF delivery resolves current link/viewer policy, selected material/language and byte eligibility even for direct/alternate/range/cache paths. Cached content is not a substitute for current authority.

Native Git uses actual client-compatible transfer semantics, not a JSON CRUD envelope. Ordinary commits are client-created under the native workflow; no API command is introduced merely to fake a Git transfer. Advanced fork/review/merge/releases and user execution remain deferred even where retained interaction examples discuss them.

## 5.6 Representative Command and Outcome Sequence

![Dark-mode PlantUML command outcome and recorded identity](Diagrams/API/api-command-outcome-sequence.svg)

[PlantUML source](Diagrams/API/api-command-outcome-sequence.puml) · [PNG](Diagrams/API/api-command-outcome-sequence.png)

This retained sequence illustrates stable command/outcome reasoning; read its proposal details with selected MVP scope. Exact route payloads, transaction boundaries and status mappings follow the contract table and owning operation. A diagram is not a deployed endpoint or a client interoperability test.

## 5.7 Compatibility, Security and Configuration

Version the service contract deliberately and review existing consumers when changing identity, scope, fields, errors, pagination or request-key behavior. Permission/visibility changes are compatibility changes even if the JSON shape stays the same. Do not repurpose stable IDs or remove information needed to resolve recorded outcomes silently.

Protect intended transport with TLS and restricted service access. Keep independent application keys/sessions and secrets out of source/frontend output/logs. Actual signing/token format, key lifecycle, timeout values, field bounds and host bindings must follow selected decisions and verified setup; proposed names alone do not specify them.

For cookie-authenticated browser state changes, retain selected Laravel anti-forgery/session protections; CORS or same-origin placement does not replace authorization. Content validation, private artifact handling and safe rendering remain the owners' obligations. No new API gateway, identity provider, broker or browser authentication layer is selected by this chapter.

## 5.8 Endpoint Verification and Handoff

| Contract | Required checks |
| --- | --- |
| Entitlement status | Correct/invalid service identity, status-only data, changed account/entitlement and unavailable bounded check |
| Repository summaries | Authorized set, hidden resources, stable pagination and revoked access |
| Files/history | Exact resolved revision, allowed relative path, invalid traversal/revision and no host-path leakage |
| Issue list | Repository scoping, filter/cursor validation and local grant changes |
| Issue create | Valid fields, permitted assignee, stable created identity, repeated key and concurrent same-key execution |
| Issue update/board move | Expected-version conflict, same issue identity, mismatched key payload and distinct Git authority |
| Direct/browser/Git paths | Applicable receiving session/viewer/transport checks independent of JSON success |
| Partial failure | Lost response after commit, interrupted durable work and safe owner-controlled result resolution |
| Evolution | Concrete schema examples, consumer compatibility and actual candidate/configuration evidence |

Use real server/persistence/concurrency checks where guarantees depend on them, plus actual Git-client and protected-delivery interoperability. Mocks support limited contract isolation but cannot establish native transport, permission or recovery behavior.

For each endpoint record actual method/path/schema, actor/scopes, preconditions, response/error examples, timeout/retry/cursor rules, implementation revision, exact criteria and executed results. Link [Detailed Module Design](03-Detailed-Module-Design.md), [Database Design](04-Database-Design.md), [Unit Test Design](10-Unit-Test-Design.md) and [Traceability](11-Traceability.md) / [RTM](../../02-Requirements-Engineering/03-Requirements-Traceability-Matrix/README.md).

The retained records below preserve original anchors and alternatives. Deferred provider/runner and advanced collaboration examples do not create MVP routes. This update implements no endpoint, installs no dependency and claims no runtime pass. Embedded UML is maintained locally in dark-mode PlantUML.

<a id="mvp-json-schemas"></a>

## 5.9 Concrete MVP JSON Schemas

This section refines the proposed routes above for implementation. It selects serialization and validation details, not new product capabilities or deployed endpoints. It takes precedence over abbreviated field lists and retained broad-product examples. T02–T07 and Q-D04/Q-D09/Q-D18 remain the governing security, policy and temporal decisions in the [selected technical baseline](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/technical-decisions.md) and [policy baseline](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/policy-decisions.md).

### Common Representation and Validation

- JSON bodies are UTF-8 objects with unique member names. Reject unknown input members, duplicate members, wrong types and invalid enum values; do not coerce numeric strings, booleans or nulls. Reject malformed JSON with `400`, unsupported request media type with `415`, and schema-invalid JSON with `422`. Authentication/visibility guards still apply before disclosing resource-specific validation.
- Public IDs are canonical UUID strings; resolve them to the owning database's `BINARY(16)` identities. UUID possession conveys no authority. Versions are integers from 1 through 9,007,199,254,740,991, incremented once per successful mutation; reject overflow rather than wrap or lose JSON precision.
- Dates are valid Gregorian `YYYY-MM-DD` strings. A non-null local date is paired with an IANA `dueTimezone`; it remains a date in that zone, not an implicit midnight UTC instant. UTC instants use RFC 3339 strings ending in `Z`. Reject impossible dates and unknown zones. No language fallback is introduced.
- The JSON field bounds below are technical validation bounds, not increases to the selected storage/admission ceilings. Lengths count Unicode code points, without silently truncating content. A required title/name must contain a non-whitespace character; trim title edges, preserve body text. Issue title: 1–255 characters; body: 0–65,535 characters; repository display name: 1–255 characters; timezone: 1–64 ASCII characters.
- Reject actor/owner/repository/version/event fields supplied outside the allowlisted operation schema. The route fixes repository and issue identity. `assigneeId` never grants membership or Git authority; a non-null assignee must currently be eligible in that repository.
- List input permits `limit` (integer 1–100, default 25) and `cursor` (opaque string, maximum 2,048 ASCII characters). These bound a response page, not total permitted data. Unknown query parameters are invalid. List responses are `{ "data": [...], "nextCursor": null }`, with `nextCursor` a string when more results exist. Singleton success responses are `{ "data": {...} }`. Success has no error member.

### Request Objects and Response Objects

| Operation | Exact permitted input | Response `data` |
| --- | --- | --- |
| Account status | Required path `userId`; no query or body. Authenticate the status-only service identity. | `{userId: UUID, active: boolean, entitled: boolean}`. An authenticated unknown subject returns `404`; inactive or unentitled existing subjects return their current false flags, without account content. |
| Repository list | Optional `limit`, `cursor`; no body. | Array of `{id: UUID, displayName: string}`. |
| Repository files | Required query `revision`; optional `path` (default root), `limit`, `cursor`; no body. | `{repositoryId: UUID, revision: string, path: string, kind: "file" or "directory", entries: [...]}` as defined below. |
| Repository history | Required query `revision`; optional `limit`, `cursor`; no body. | `{repositoryId: UUID, revision: string, commits: [...]}`; `nextCursor` is a sibling of `data`. Each commit is `{id: string, parentIds: string[], subject: string, authoredAt: UTC instant or null}`. Missing/invalid Git author dates are null, not invented instants. |
| Issue list | Optional `state` (`todo`, `in_progress`, `done`), `limit`, `cursor`; no body. | Array of Issue objects below. |
| Issue create | Required JSON `title`, `body`; optional `priority`, `assigneeId`, `dueDate`, `dueTimezone`. Required `Idempotency-Key`. | One Issue object, status `201`. Initial `state` is `todo`, `priority` defaults to `normal`, `assigneeId` and date pair default to null, version is 1. |
| Issue update / board move | Required JSON `expectedVersion`; at least one of `title`, `body`, `state`, `priority`, `assigneeId`, `dueDate`, `dueTimezone`. Required `Idempotency-Key`. | One Issue object, status `200`, with the resulting version. No arbitrary field, repository move or grant update. |

An **Issue** is exactly `{id, repositoryId, number, title, body, state, priority, assigneeId, dueDate, dueTimezone, version}`. IDs are UUIDs, `number` is a repository-local positive safe integer, enums are the values above (`priority`: `low`, `normal`, `high`), and only `assigneeId`, `dueDate` and `dueTimezone` are nullable. All response members are present. Issue bodies are untrusted plain text for this interface; render as text, never executable HTML. The database uses the same character/value bounds. Authorization can deny the entire object; the server must not return another repository's issue under a substituted route ID.

The MVP board is a projection of these same issues with fixed columns in order `todo`, `in_progress`, `done`. A board move updates `state` through the issue PATCH contract; it never creates a second task or grants repository write. Custom columns/order, independent Backlog Item/task hierarchies and Sprint planning are deferred by Q-D18/Q-D19.

### PATCH Omission and Clearing

An omitted field retains its existing value. Explicit null clears `assigneeId`. Explicit null for `dueDate` clears both date and zone; omit `dueTimezone` or send it as null in that case. Setting/changing a non-null date requires a non-null zone in the same request. A zone-only change requires an existing date and a non-null zone. `dueTimezone: null` with a retained/non-null date is invalid. Creation requires both non-null date/zone or both null/omitted. Null title, body, state, priority or expectedVersion is invalid; `body: ""` explicitly clears body text. Validate the resulting complete object before committing. A PATCH containing no mutable field is `422`; a valid no-op with matching expected version records the successful outcome and increments version once, so retries remain unambiguous.

### Serialized Response Budget

The complete uncompressed UTF-8 JSON response, including envelope, escaped values and cursor, must not exceed **8 MiB (8,388,608 bytes)**. Enforce this bound during bounded serialization before sending any success bytes; compression does not increase it. List `limit` is a maximum, not a promise of that many results. Return fewer entries when needed and a cursor that resumes at the first omitted entry, without skipping it or falsely claiming exhaustion. If even one permitted item/projection plus envelope cannot fit, return `422 representation_too_large` with no partial success; do not loop with an empty page and unchanged cursor. Admission/resource limits still apply independently.

Planned contract checks (not executed): list 100 one-MiB text files and verify metadata-only results; request one file and verify its preview ceiling; measure escaped UTF-8 serialized bytes at/beyond the total budget; traverse reduced pages without omissions/duplicates; verify an unrepresentable singleton gives the stable error.

### Revision, Path and Cursor Semantics

`revision` is a complete immutable Git object ID (40 or 64 hexadecimal characters, matching the repository's configured object format); files accept a readable commit/tree, history requires a readable commit under the repository policy. Responses return canonical lower-case resolved identity. Do not silently replace a missing revision with HEAD. `path` is a UTF-8 repository-relative path of at most 4,096 bytes: no absolute prefix, drive prefix, backslash, NUL, `.`/`..` segment or decoded traversal. Decode the HTTP query once before validating. Empty path means root. Git entries that cannot be represented safely in this API receive an explicit unsupported-path outcome; do not reinterpret them as host paths.

File `entries` contain `{path, name, kind, objectId, sizeBytes, text, contentState}`. Kinds are `file`, `directory`, `symlink`, `submodule`; sizes are nonnegative safe integers for blobs and null otherwise. Directory results contain one page of immediate children, with optional `limit`/`cursor` using the common bounds; file results contain only the requested entry. A sibling `nextCursor` is present and null for a single file or exhausted directory. A requested symlink/submodule has result `kind: "file"` as a non-directory entry and its precise kind in `entries[0]`; never dereference it. Directory listings always return metadata only: every entry has `text: null` and `contentState: metadata_only`, including regular files. Inline text is available only when requesting one specific regular UTF-8 file no larger than 1 MiB; otherwise `text` is null. `contentState` is `inline`, `binary`, `too_large` or `metadata_only`; never call a binary/large file empty or fetch a symlink/submodule target. This preview ceiling changes no Git transfer or repository quota. The UI escapes inline content. File entries sort by raw Git path bytes; the cursor is bound to repository, immutable revision, path and page order.

Repository lists sort by public UUID bytes; issues sort by ascending repository-local issue number. History traverses parents from the resolved start commit in a deterministic order (parents sorted by object ID, depth-first, each commit once), preserving the traversal frontier in a server-validated cursor. Cursors bind the authenticated actor, operation, resource, filters and order; they never convey permission. Invalid/tampered or wrong-context cursors return `422` with `invalid_cursor`. If a cursor's retained traversal context is unavailable, return `409` with `cursor_unavailable` and require a fresh list. Recheck authority on every page. Lists are not a cross-request database snapshot: concurrent creation may appear on a later page; revoked objects are omitted. Do not manufacture empty results from a dependency/read failure.

<a id="mvp-json-errors-and-retries"></a>

## 5.10 Error, Retry and Security Contract

JSON errors are exactly `{ "error": { "code": "stable_code", "message": "Safe user-facing description", "fields": {} }, "correlationId": "opaque-diagnostic-id" }`. `fields` is an object mapping allowlisted input field names to arrays of safe validation codes; it is empty outside field-validation errors. Never echo request secrets, private bodies, host paths or stack traces. The correlation ID is server-generated or validated bounded diagnostic text, not an authorization token. Error messages may be localized; clients branch on codes. Unknown/missing/hidden resources all use the same `404 resource_not_found` shape.

| Status | Stable codes / use |
| --- | --- |
| 400 | `invalid_json` |
| 401 | `invalid_identity`; missing/invalid/expired credential |
| 403 | `forbidden`; visible but unauthorized action |
| 404 | `resource_not_found`; hidden/missing subject/resource/revision/path |
| 409 | `version_conflict`, `idempotency_conflict`, `operation_pending`, `cursor_unavailable` |
| 413 | `payload_too_large`; enforced receiving body bound |
| 415 | `unsupported_media_type` |
| 422 | `validation_failed`, `invalid_cursor`, `unsupported_path`, `representation_too_large` |
| 429 | `rate_limited`; enforced receiving admission limit |
| 500 | `internal_error`; bounded diagnostic, not proof of rollback |
| 503 | `authority_unavailable`, `dependency_unavailable` |

Status/codes do not certify whether an earlier attempt committed. For issue writes use an opaque, case-sensitive `Idempotency-Key` of 1–128 printable ASCII characters (no whitespace/control characters). Key identity is actor + operation + key; operation includes method and canonical repository/issue route IDs. Canonical payload hash includes validated input, defaults, explicit field presence/clearing and expectedVersion; JSON property order is irrelevant. Reject conflicting reuse with `409 idempotency_conflict`. Recheck current authority before disclosing a recorded result. A matching completed retry returns the original allowed status/body without another version change/event. An in-progress/uncertain attempt returns `409 operation_pending`; reconcile that operation, never create a second effect. A definitive rejected transaction produces no business mutation.

T05 retains outcome protection for **7 days**; compute expiry from terminal completion, and retain the claim while attributable work remains pending/uncertain. Expiry alone never releases protected bytes. After a completed key's retained record is purged, deduplication is no longer guaranteed: do not automatically resend an old create; inspect current issue state or use owner reconciliation. A stale update remains subject to expectedVersion. No unbounded forever-replay guarantee is made.

T03 actor JWT validation pins RS256, issuer, `projectforge-api` audience, immutable Core UUID subject, allowlisted action scope and a maximum five-minute lifetime. The status-only credential grants no content scope. On every new protected request, including browser and native Git admission, verify Core active/entitled status and local grants; no positive entitlement cache. T07 sets status timeout to **2 seconds**, API connect timeout **2 seconds** and response timeout **10 seconds**. A timeout is an unknown outcome until reconciled. Retry only classified safe/idempotent work under the same operation identity; T07's **1/5/30-minute** backoff then manual recovery applies to durable retryable work, not automatic blind retries of all HTTP writes. Package settings, actual credentials and interoperability remain setup evidence gates.

### Synthetic Examples

Create input: `{"title":"Review resume","body":"","priority":"normal","assigneeId":null,"dueDate":"2026-12-01","dueTimezone":"Europe/Berlin"}` plus a fresh key. Success: `{"data":{"id":"11111111-1111-4111-8111-111111111111","repositoryId":"22222222-2222-4222-8222-222222222222","number":1,"title":"Review resume","body":"","state":"todo","priority":"normal","assigneeId":null,"dueDate":"2026-12-01","dueTimezone":"Europe/Berlin","version":1}}`.

Clear-date PATCH: `{"expectedVersion":1,"dueDate":null}` retains other fields and returns both date fields null at version 2. A different write using expectedVersion 1 then receives `409` with `{"error":{"code":"version_conflict","message":"Review the current issue before saving.","fields":{}},"correlationId":"example-only"}`. None of these examples is an executed result.

<a id="mvp-browser-and-native-interface-contracts"></a>

## 5.11 Browser SSO and Non-JSON Receiving Contracts

### Independent Sessions and OAuth Admission

T03 selects Core Passport authorization-code SSO with PKCE S256 and ProjectForge's League OAuth2 Client GenericProvider. Navigation between sections of an already authenticated receiving application retains its valid Laravel session. Entering ProjectForge without a valid local session starts the explicit Core authorization flow; a still-valid Core session permits reauthorization without asking for the password merely because the section changed. Independent app sessions are never a shared session table or a grant to all repositories.

Bind the authorization attempt to the initiating ProjectForge browser context with a cryptographically random one-use state and a PKCE verifier; exact registered redirect URI, pinned Core issuer and five-minute callback deadline must match. Reject missing, mismatched, expired or reused state/code; do not provision an actor from caller-supplied email/UUID. Exchange the code server-side and obtain the immutable Core UUID through the protected user-info contract. Provision/bind `(pinned issuer, Core UUID)` only after current invited/active account and explicit ProjectForge entitlement checks. No refresh tokens in MVP; OAuth access lifetime is five minutes. Store tokens server-side encrypted at rest; never expose them in Inertia props. Failed admission leaves no authenticated Forge context. Current Core status and local grants are rechecked on every later protected Forge browser/API/Git admission.

The user-info receiver authenticates the short-lived Core OAuth access token, derives the subject from it, and returns only `{userId: UUID, active: boolean, entitled: boolean}` for that subject. It accepts no caller-selected subject override. The status-only service endpoint remains separate and can query a specified UUID only with its restricted service credential. Concrete Passport/SSO/user-info route names and package interoperability are Setup/G2 records; this contract defines identity/result semantics without inventing deployed routes or an OpenID Connect implementation.

### Applicable Interface Inventory

| Receiving path | Owning contract and bounded result |
| --- | --- |
| IF-01 workspace/browser | Receiving Laravel session plus current owner policy; Inertia validation errors retain the user's input, stale writes require review, and denied actions do not commit. See [screen forms and recovery](../02-UI-UX-Design/08-Screen-Specifications.md#4-forms-feedback-and-recovery). |
| IF-02 protected employer/file/PDF | Link-scoped viewer identity, current generation and selected resume/language/artifact; no owner account required. Direct/range access uses the same decision, Nginx internal delivery, no-store/nosniff and safe disposition. Missing or unauthorized content never falls back to unrelated content. See [retrieval/revocation](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-representation-and-sharing-md--heading-4-protected-retrieval-and-revocation-protocol). |
| IF-03 private file input/output | Owner admission, detected type/actual size and concurrent selected quotas; incomplete/failed validation is not usable content. Exact artifacts and protected references follow [database write protocols](04-Database-Design.md#mvp-protected-foreign-keys). |
| IF-04/IF-05 personal mail/calendar | Deferred after MVP. Transactional invitation/recovery SMTP is an operating dependency, not a personal mail/calendar connection. Record actual delivery/failure independently; SMTP acceptance is not recipient receipt/read. |
| IF-06 native Git | T04 HTTPS Smart HTTP/PAT and per-operation/ref policy; clone/fetch/push remain native protocol exchanges. Discovery and service method must match read/write authority; deny dumb HTTP, anonymous access, force/non-fast-forward pushes and ref deletion. See [native transfer contract](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-git-collaboration-md--heading-transfergitcontext-repositoryid-transportoperation-refintent). Client pull includes local integration, not a server JSON command. |
| IF-07 user workflow/deployment targets | Deferred after MVP; a push or issue event cannot admit user code execution or deployment. Developer release operations remain separately authorized. |
| IF-08 external/operating failures | Scoped Core/Forge JSON uses sections 5.9–5.10; actual SMTP and backup/restore use their owner-local durable result and [operating procedure](../../06-Deployment-Release/02-Runbook.md). Unknown completion requires reconciliation, not false success or blind repetition. |

IF labels retain the SRS's interface families; the scoped Core/ProjectForge seam is an MVP refinement, not a replacement for those families. Exact native/browser/SMTP/backup runtime configuration and real-client/delivery/restore results remain mandatory evidence gates.


<a id="design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md"></a>

<details>
<summary>Resumefolio — API Protocols, Contracts and Compatibility</summary>

<a id="design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-resumefolio--api-protocols-contracts-and-compatibility"></a>

### Resumefolio — API Protocols, Contracts and Compatibility

Current implementation choices and scope: [Baseline](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/README.md). Runtime verification remains subject to its gates.

**Purpose:** define shared communication choices, contract contents, result semantics and compatibility rules for browser, component and external integration boundaries.

**Status:** proposed technical design. This is a shared contract specification, not an implemented route catalog, adopted frontend stack or verified provider/client compatibility matrix. Concrete signatures and payload schemas remain with their owning components.

[Scope](#design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-1-sources-and-interface-ownership) · [Protocols](#design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-2-protocol-choices-by-consumer) · [Contracts](#design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-3-required-contract-record) · [HTTP](#design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-4-http-results-and-concurrency) · [Repetition](#design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-5-command-identity-and-asynchronous-effects) · [Boundaries](#design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-6-external-and-protected-exchanges) · [Evolution](#design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-7-versioning-and-compatibility) · [Review](#design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-8-verification-and-handoff) · [Essential views](#design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-9-essential-api-and-contract-views)

<a id="design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-1-sources-and-interface-ownership"></a>

#### 1. Sources and interface ownership

Use [EIF-D01–EIF-D10 and IF-01–IF-08](../../02-Requirements-Engineering/01-Software-Requirements-Specification/03-Requirements-Specification/07-External-Interface-Requirements.md#requirements-specification-external-interface-requirements), [analysis interfaces](../../03-System-Analysis/04-Interfaces-Security-And-Quality.md#analysis-interfaces-security-and-quality-analysis--12-interfaces-and-external-interactions), the [dictionary](../../02-Requirements-Engineering/01-Software-Requirements-Specification/05-Data-Definitions/02-Data-Dictionary.md#data-definitions-data-dictionary) and [architecture boundaries](../01-High-Level-Design/14-Appendices.md#design-record-01-software-architecture-02-system-decomposition-and-boundaries-md). Inventory labels identify source boundaries, not new API endpoint IDs or selected transports.

The resource-owning component provides the contract and enforces its invariants. Consumers use explicit permitted identities/projections and cannot mutate private records through a shared ORM model. This folder owns shared conventions; [component designs](02-Module-Breakdown.md#design-record-03-component-and-module-design-component-and-module-design-md) own exact operations/types, [interaction realizations](#design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md) own selected collaborations, and [runtime design](../01-High-Level-Design/14-Appendices.md#design-record-01-software-architecture-03-process-view-concurrency-and-runtime-behavior-md) owns concurrency/reconciliation behavior.

Accepted publication/history behavior remains binding: preview/select/apply changes only the intended draft, publication needs separate owner confirmation, and actual submitted materials remain independent. API convenience cannot combine these into an implicit publish or submission action.

<a id="design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-2-protocol-choices-by-consumer"></a>

#### 2. Protocol choices by consumer

| Boundary | Candidate communication and rationale |
| --- | --- |
| Private browser UI | Same-origin HTTPS with server-side authorization; server-rendered/progressively enhanced views and HTTP/JSON commands where useful |
| Employer viewing / file retrieval | Protected HTTPS projection/controlled byte delivery, with separate viewer/link scope and exact variant eligibility |
| In-process components | Explicit language-level interfaces/value types; no HTTP hop solely to connect modules in one application |
| Background effects | Durable identified intent and scoped worker/adapter dispatch; transport remains evaluated rather than implying exactly-once messaging |
| Google provider integrations | Evaluated official provider APIs/consent/capabilities through adapters; current scopes/version/quotas require selection-time evidence |
| Git clients | Evaluated native Git-compatible transport and client credentials; browser session/JSON endpoints do not establish clone/fetch/push interoperability |
| Executor / deployment target | Authenticated attempt-scoped control/observation and separate target authority across evaluated trust boundaries |

HTTP/JSON is the current interactive-command proposal, not a mandate to expose a public REST API. GraphQL can be evaluated for evidenced client/query needs; gRPC for an evidenced separately deployed consumer and compatibility needs. Neither is needed merely because the application has components. Do not add a broker, public API, mobile client or service split without a justified requirement/decision. Actual browser support, frontend framework and transport products remain pending evaluation.

<a id="design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-3-required-contract-record"></a>

#### 3. Required contract record

Before implementation, record each provided/required operation with:

- **Identity and trace:** contract owner, consumer, source IF/EIF/domain criteria, scenario and contract revision.
- **Invocation:** operation purpose, transport/method/path or in-process signature, media type, input schema and bounded payload rules.
- **Authority:** caller/context, resource/action scope, current eligibility/revocation checks, anti-forgery mechanism where applicable and safe denial disclosure.
- **Meaning:** required/optional/nullable fields, identifiers/units, dates/instants/time zones, language/revision provenance and enum/unknown-value handling.
- **Consistency:** expected versions, command/attempt identity, transaction/admission boundary and which external effects can remain unknown.
- **Results:** actual outcome variants, permitted response projection, HTTP mapping where relevant, field errors, operation lookup and repetition/reconciliation behavior.
- **Lifecycle:** pagination/filter/order, cancellation/expiry/retention where relevant, compatibility/deprecation and verification evidence.

Validate transport shape at the boundary and domain invariants at the owner. Distinguish omitted from intentional empty/null values, especially resume overrides, patch-like updates and optional provider mappings. Do not accept arbitrary fields for mass assignment. Exposed IDs identify resources; they do not establish permission.

Pagination needs bounded page size, deterministic ordering with a stable tie-breaker and documented cursor/filter semantics. Re-evaluate authority on each page and cursor use; define concurrent-change/completeness behavior. A cursor must not grant access or reveal another user's private query. Numerical limits require reviewed resource policy.

<a id="design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-4-http-results-and-concurrency"></a>

#### 4. HTTP results and concurrency

Apply [RFC 9110 HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110.html) rather than using transport success as proof of domain completion. Read-only retrieval must not trigger publication, send, deployment or other business mutations. Protocol idempotence concerns repeated intended server effect, not identical response bodies or a guarantee about remote provider behavior.

| Condition | Candidate HTTP mapping and qualification |
| --- | --- |
| Completed permitted read/command | 200 with the actual result; 201 only when its creation semantics apply; 204 only when no response content is needed |
| Accepted but incomplete operation | 202 with permitted operation reference/status lookup; acceptance does not prove eventual success |
| Malformed / unsupported / semantically invalid input | 400 / 415 / 422 as applicable, with stable safe field/problem details |
| Missing/invalid authentication or insufficient authority | 401 / 403 where applicable; 401 includes the required challenge semantics; reviewed 404 concealment may protect private existence |
| Stale conditional request / domain conflict | 412 for a failed applicable HTTP precondition; 409 for the defined state/intent conflict |
| Resource/abuse pressure | 429 or 503 where appropriate; any retry advice must not authorize blind repetition of uncertain effects |
| Internal/transport uncertainty | Appropriate 5xx/transport failure plus safe operation reconciliation; never invent an HTTP status meaning “definitely not sent” |

Final endpoint mappings and disclosure rules belong in each exact contract. Domain outcomes include confirmed, pending, denied, invalid, conflict, unavailable, partial and unknown where meaningful; they are not a mandatory universal envelope or eight new status codes. A successful operation-status lookup can return 200 while describing a failed or unresolved underlying attempt.

Use an evaluated expected-version field or applicable ETag/If-Match precondition to prevent stale writes. If using HTTP validators, scope them to the actual representation and implement their comparison semantics correctly; an arbitrary domain revision is not automatically a compliant ETag. A single resource validator may not guard a cross-record Sprint or grant-change race. Exact locking/admission remains [data/runtime design](04-Database-Design.md#design-record-04-data-design-01-analysis-to-logical-and-physical-data-models-md).

For HTTP error representations, evaluate [RFC 9457 Problem Details](https://www.rfc-editor.org/rfc/rfc9457.html): stable problem type/title/status semantics with safe instance/field extensions where useful. Do not expose stack traces, storage paths, secrets or private target existence. Display text may be localized; machine codes and field identities remain stable. These standards were consulted; framework/route compatibility is not verified here.

<a id="design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-5-command-identity-and-asynchronous-effects"></a>

#### 5. Command identity and asynchronous effects

[Identified command, guarded owner mutation and safe outcome lookup](Diagrams/API/api-command-outcome-sequence.svg)

[Editable PlantUML](Diagrams/API/api-command-outcome-sequence.puml) · ![api command outcome sequence](Diagrams/API/api-command-outcome-sequence.svg)

Consequential commands use a documented stable command identity scoped to the actual operation/actor/resource contract. Validate current authority before returning a prior result. Compare attributable intended payload/version context so reuse with changed intent conflicts instead of executing new work. Storage/expiry and secret-safe intent representation are explicit implementation decisions; no idempotency-header standard or infinite retention is assumed.

Commit the owned local change, result and required durable external intent coherently. A worker uses current required authority, immutable inputs and stable attempt identity; it does not carry an evergreen privileged session. Operation lookup identifies the actual command/attempt and returns only permitted bounded evidence. Polling, push feedback or callbacks need explicit ownership and compatibility; no realtime protocol is selected here.

A lost response prompts lookup/reconciliation of the same operation. A local deduplication key cannot prove a provider accepted a send, a runner did not start or a target rolled back. Do not repeat such effects blindly. Fresh retries/new attempts require explicit operation policy, current authority and known effect boundaries. Cancellation request and confirmed stop are distinct results; completion can win a race.

<a id="design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-6-external-and-protected-exchanges"></a>

#### 6. External and protected exchanges

<a id="design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-browser-and-employer-entry-paths"></a>

##### Browser and employer entry paths

Use evaluated transport/session controls and state-change protection for cookie-authenticated requests. [OWASP CSRF guidance](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) informs anti-forgery evaluation; same-origin deployment alone is not a complete CSRF mechanism. CORS configuration does not replace authentication, resource authorization or applicable CSRF controls. Exact framework/session/cookie compatibility remains pending.

Employer viewer context remains link-scoped and is not proof of a named employer identity. Resolve current link generation, selected content, publication/language and download eligibility before protected delivery. Apply current checks to direct paths, range/cache requests and alternate endpoints. Already emitted/downloaded bytes cannot be recalled. See [Sharing](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-representation-and-sharing-md).

<a id="design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-files-and-provider-adapters"></a>

##### Files and provider adapters

Uploads distinguish transfer, admitted usable artifact and consumer association. Specify supported media, bounded streaming, replacement and unavailable/error behavior through [Files](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-files-and-operations-md); do not expose raw private paths or execute uploaded previews.

Provider adapters map actual capabilities/results into local contracts without losing pending/partial/unknown meaning. Provider acceptance is not recipient delivery/reading. Consent changes, disconnect/reconnect, external IDs, time-zone mappings, throttling and reconciliation stay explicit. See [Communication](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-communication-and-calendar-md). Current Google API/scopes/quotas must be verified against official sources when selecting the adapter; none is certified here.

<a id="design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-git-executor-and-target-interfaces"></a>

##### Git, executor and target interfaces

**After MVP.** Shared operating and recovery controls still apply where relevant.

Native Git clients use evaluated transport/credential/ref rules and actual client interoperability evidence; do not wrap every exchange in a JSON result envelope. See [Git](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-git-collaboration-md).

Executor callbacks must be authenticated and bound to the exact attempt/generation, with stale/duplicate observation handling. Deployment approval names exact artifact/target/configuration and separate current authority. A callback, merge or run success cannot approve deployment. Actual containment and execution-enabling evidence remain gates in [Workflow and Deployment](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-workflow-and-deployment-md).

<a id="design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-7-versioning-and-compatibility"></a>

#### 7. Versioning and compatibility

[Contract change, consumer compatibility and safe retirement](Diagrams/API/api-contract-evolution.svg)

[Editable PlantUML](Diagrams/API/api-contract-evolution.puml) · ![api contract evolution](Diagrams/API/api-contract-evolution.svg)

Version externally consumed contracts deliberately. Select path/header/media-type or another explicit scheme only for actual consumers; do not create an arbitrary `/v1` public API solely for internal modularity. In-process interfaces also need consumer coordination, and queued payloads may outlive the deployment that produced them.

An additive field is compatible only if actual consumers tolerate it. Changed requiredness, enum values, defaults, units, ordering, permission scope, side effects and result meaning can break consumers even when JSON shape looks similar. Do not weaken privacy or grant broader permissions to preserve an old client's convenience.

For a change, identify active browsers/clients, workers, stored pending payloads, callbacks and adapters; classify shape and semantic impact; define old/new reader-writer compatibility; migrate/backfill where needed; verify coexistence; then retire only with actual disposition. No default deprecation period or perpetual old-version support is invented. Preserve exact historical publication/submission and pending external-attempt meaning through schema/job/API changes.

<a id="design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-8-verification-and-handoff"></a>

#### 8. Verification and handoff

| Source group | Shared contract responsibility |
| --- | --- |
| EIF-D01/D02 | Reviewable operation record and clear input/feedback semantics |
| EIF-D03/D04 | Consistent authority across entry paths and protected byte exchange |
| EIF-D05–D07 | Explicit provider, native Git and executor/target boundaries |
| EIF-D08 | Operation-specific conflict, repetition, cancellation and uncertain effects |
| EIF-D09/D10 | Operating/recovery boundaries and consistent identity/time/language/lifecycle meaning |

<a id="design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-planned-focused-checks"></a>

##### Planned focused checks

- Schema/requiredness/unknown-field/media-type behavior, safe errors and exact status/precondition semantics.
- Direct wrong-owner requests, employer scope, anti-forgery paths and current permission/revocation checks.
- Stale versions, duplicate command identities, changed intent and lost responses without duplicate external effects.
- Pending-result lookup under current authority, cancellation races and authenticated stale/duplicate callbacks.
- Bounded deterministic pagination, concurrent changes, time/language/revision and private projection isolation.
- Actual Git-client/provider/serving interoperability once facilities are selected; mock success is insufficient.
- Old/new client/worker/payload coexistence, semantic compatibility and safe retirement.

Use contract tests plus actual framework/persistence/concurrency and authorized integration evidence. No live route, provider send, Git transfer, executor action, deployment or product compatibility test is performed by this update.

**Remaining prescriptions:** specify exact route/signature and payload/result schemas per owner; choose client/framework/session/security facilities; fix endpoint status/precondition/repetition contracts, resource limits and pagination; evaluate actual external versions/capabilities and callback authentication; record compatibility/migration evidence. The shared design is populated, not a complete API implementation or accepted baseline.

The FAU component-interface/use-case realization concerns inform this design; protocol conventions and this document layout are project adaptations. See the [reference map](../01-High-Level-Design/14-Appendices.md#design-record-design-references-and-coverage-md) and [review/handoff](../01-High-Level-Design/14-Appendices.md#design-record-06-design-quality-and-security-analysis-05-design-review-traceability-and-handoff-md).

[Interface and API Design](#design-record-05-interface-and-api-design-interface-and-api-design-md) · [Interaction realizations](#design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md) · [Diagram catalog](#design-record-05-interface-and-api-design-diagrams-diagram-catalog-md)

<a id="design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-9-essential-api-and-contract-views"></a>

#### 9. Essential API and contract views

Only **four complementary diagrams** are added; no new tables, endpoints or schema excerpts. Reuse the existing [contract evolution diagram](#design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-7-versioning-and-compatibility) and the [interaction realization document](#design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md) for detailed collaborations. Diagrams express candidate boundaries and engineering workflow, not selected protocols/services or tested client compatibility.

<a id="design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-91-consumers-owner-contracts-and-external-adapters"></a>

##### 9.1 Consumers, owner contracts and external adapters

[MVP with explicitly deferred paths — Consumers, owner contracts and external adapters](Diagrams/API/api-essential-boundaries.svg)

[Editable PlantUML](Diagrams/API/api-essential-boundaries.puml) · ![api essential boundaries](Diagrams/API/api-essential-boundaries.svg)

Essential interface landscape and provider/consumer boundary in one view. Actual authentication, anti-forgery and resource checks remain required at all applicable entry paths. Adapters preserve denied/conflict/pending/partial/unknown outcomes; a reachable technical credential is not human authority.

<a id="design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-92-protocol-selection-by-actual-boundary-need"></a>

##### 9.2 Protocol selection by actual boundary need

[MVP with explicitly deferred paths — Protocol selection by actual boundary need](Diagrams/API/api-essential-selection.svg)

[Editable PlantUML](Diagrams/API/api-essential-selection.puml) · ![api essential selection](Diagrams/API/api-essential-selection.svg)

Decision aid, not a product-selection benchmark. GraphQL/gRPC/WebSocket/async transport require an actual justified need, supported consumers and operating compatibility. Durable asynchronous intent is a semantic requirement where needed, not automatic selection of a messaging broker or exactly-once delivery.

<a id="design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-93-contract-first-refinement-without-mandatory-code-generation"></a>

##### 9.3 Contract-first refinement without mandatory code generation

[Contract-first refinement without mandatory code generation](Diagrams/API/api-essential-contract-workflow.svg)

[Editable PlantUML](Diagrams/API/api-essential-contract-workflow.puml) · ![api essential contract workflow](Diagrams/API/api-essential-contract-workflow.svg)

OpenAPI, AsyncAPI, protobuf and GraphQL schemas are alternative representations for actual selected protocols, not four required artifacts. Mock/codegen is optional and cannot prove real authorization, external idempotency or runtime interoperability. No spec file, toolchain or production implementation is generated here.

<a id="design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-94-consumer-expectations-and-provider-verification"></a>

##### 9.4 Consumer expectations and provider verification

[Consumer expectations and provider verification](Diagrams/API/api-essential-consumer-verification.svg)

[Editable PlantUML](Diagrams/API/api-essential-consumer-verification.puml) · ![api essential consumer verification](Diagrams/API/api-essential-consumer-verification.svg)

Compact consumer-driven contract-testing concept, not an installed test platform. Actual consumers must tolerate additive fields/enums where claimed; changed defaults, permission scope, effects or ordering can break compatibility even with unchanged schema. Required live/controlled evidence remains separately scoped.

<a id="design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-essential-scope-and-evolution-limits"></a>

##### Essential scope and evolution limits

No separate API landscape, HTTP-version/TLS stack or URI resource graph is added before actual transport, routes and clients are selected. A conceptual resource identity does not allocate a public URL. In-process modularity does not mandate HTTP, a gateway or `/v1` routing. HTTP/JSON remains the interactive-command proposal; native Git, protected files and external control/provider exchanges preserve their own contracts.

The existing compatibility/evolution view already owns change classification, consumer coordination and safe retirement. A real deprecation process must identify active client/worker/persisted-payload versions, truthful migration guidance, actual observation and explicit removal disposition; no calendar dates, sunset headers, universal migration window or perpetual old-version support are invented. Public API scheme, rate limits and service targets remain actual selection/source decisions.

Concrete payload/endpoint/error/repetition prescriptions belong in each owning component, preserving separate draft apply, publication and actual history. Old/new consumer coexistence must not weaken current authority, drop unresolved effects or silently reinterpret language/time/version meaning. No route/spec generation, contract test, codegen, protocol upgrade, deprecation notice or provider/native-client operation is executed by this documentation update.

<a id="design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-mvp-coreprojectforge-api-contract-refinement"></a>

#### MVP core–ProjectForge API contract refinement

The API is the integration seam between distinct systems, not an internal module call or shared database. The following are required contract subjects; endpoint paths, transport credentials, token format, versions, timeout values and error codes remain design decisions.

| Contract subject | Required observable behavior | Verification still required |
| --- | --- | --- |
| Authenticated actor and resource | Bind the actual user, action and target resource; reject impersonation, unrelated grants and universal admin bypass | Two-user allowed/denied and forged-subject cases |
| Current authority and revocation | Re-evaluate applicable account/repository/board grants; API access does not itself confer native Git credentials | Changed grant/account state and separate Git transport checks |
| Repository / file / history projection | Return only the permitted repository/revision projection; no private core library paths or unrestricted mutable models | Cross-user/private-path and exact revision checks |
| Issues and simple Kanban | Own state in ProjectForge, preserve attributable changes and truthful failures; no advanced Sprint/review/release promise | Intended issue/board flow plus stale/denied/failure cases |
| Unknown or failed result | Preserve actual local intent/observed remote outcome; reconcile before repeating a consequential request | Interrupted response and duplicate-request cases with selected mechanism |
| Independent storage/recovery | Cross-system IDs carry no shared transaction assumption; restore must reconcile references and current authority | Isolated restore and stale-reference walkthrough |

Native Git clone/fetch/pull/push is a separate ProjectForge entry contract; ordinary commits are client-created. No API method is required to create a server-side commit merely to save core data. Mail/calendar API contracts below are future-only and preserve per-user/account consent; administrator role grants no mail-reading authority.

</details>

<a id="design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md"></a>

<details>
<summary>Resumefolio — Use-Case Realizations and Interactions</summary>

<a id="design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-resumefolio--use-case-realizations-and-interactions"></a>

### Resumefolio — Use-Case Realizations and Interactions

Current implementation choices and scope: [Baseline](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/README.md). Runtime verification remains subject to its gates.

**Purpose:** show how technical components collaborate to realize existing analysis scenarios without changing their goals or accepted behavior.

**Status:** proposed technical realizations. The routes and diagrams specify responsibilities and consistency obligations, not implemented endpoints, proven atomicity or executed scenario tests. Exact signatures and mechanisms remain with component owners.

[Sources](#design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-1-source-and-realization-conventions) · [Coverage](#design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-2-scenario-to-component-map) · [Content](#design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-3-content-sharing-and-actual-material) · [Providers](#design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-4-provider-interactions) · [Work and execution](#design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-5-work-git-execution-and-deployment) · [Recovery](#design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-6-policy-admission-and-recovery) · [Review](#design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-7-verification-and-completion-boundary) · [Essential views](#design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-8-essential-use-case-realization-views)

<a id="design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-1-source-and-realization-conventions"></a>

#### 1. Source and realization conventions

Use the existing [use-case/scenario catalog](../../02-Requirements-Engineering/01-Software-Requirements-Specification/04-Scenarios-And-Models/02-User-Stories-And-Scenarios.md#scenarios-and-models-user-stories-and-scenarios), [scenario-based analysis](../../03-System-Analysis/03-Processes-Scenarios-And-Business-Rules.md#analysis-behavioral-and-scenario-analysis--06-scenario-based-view), [state-based analysis](../../03-System-Analysis/03-Processes-Scenarios-And-Business-Rules.md#analysis-behavioral-and-scenario-analysis--07-state-based-view) and [operation contracts](../../03-System-Analysis/03-Processes-Scenarios-And-Business-Rules.md#analysis-business-rules-and-operation-contracts--10-domain-constraints-and-operation-contracts). UC-D and SB-M references retain those sources' status; this document allocates no new primary use cases or acceptance.

Follow [shared API contracts](#design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md), [runtime coordination](../01-High-Level-Design/14-Appendices.md#design-record-01-software-architecture-03-process-view-concurrency-and-runtime-behavior-md) and [data integrity](04-Database-Design.md#design-record-04-data-design-01-analysis-to-logical-and-physical-data-models-md). Each protected operation resolves current actor/resource authority, expected versions and attributable intent before its owner admits effects. An arrow denotes a responsibility exchange, not a remote service, database transaction or automatic trigger.

Existing component diagrams remain the detailed owning views. The new overview and recovery view below connect them rather than replacing their contracts. Unspecified lock ordering, dispatch fencing, provider compatibility and reference/deletion guards remain implementation work.

<a id="design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-2-scenario-to-component-map"></a>

#### 2. Scenario-to-component map

All SB-M identifiers below resolve in the linked [scenario analysis](../../03-System-Analysis/03-Processes-Scenarios-And-Business-Rules.md#analysis-behavioral-and-scenario-analysis--06-scenario-based-view). This is responsibility coverage, not criterion closure or a claim that every alternative path has an implementation sequence.

| Existing scenario family | Technical owner and detailed realization |
| --- | --- |
| UC-D01 / SB-M01 | [Presentation](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-professional-presentation-md): compare/select/apply; separately confirmed publication |
| UC-D02 / SB-M02–03 | [Sharing](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-representation-and-sharing-md): independent PDF configuration and link/password management |
| UC-D03 / SB-M04 | Sharing with Presentation/Files: selected, current protected representation retrieval |
| UC-D04–05 / SB-M05–06 | [Applications](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-applications-md): manual preparation/progress and separate actual-material capture |
| UC-D06 / SB-M07–08 | [Communication/Calendar](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-communication-and-calendar-md): read/send and explicit local/provider synchronization  **After MVP.** |
| UC-D07 / SB-M09 | [Work](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-work-management-md): refinement, coherent Sprint planning and actual period outcomes |
| UC-D08 / SB-M10 | [Identity](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-identity-and-access-md) with resource owner: effective membership, scoped grants and revocation |
| UC-D09 / SB-M11–12 | [Git](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-git-collaboration-md): native transfers, revision-bound review and guarded ref update |
| UC-D10 / SB-M13–14 | [Workflow/Deployment](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-workflow-and-deployment-md): gated execution and separate target-authorized deployment  **After MVP.** |
| UC-D11 / SB-M15 | [Files/Operations](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-files-and-operations-md): effective policy, admission/accounting and restricted evidence |
| UC-D12 / SB-M16 | Files/Operations with affected owners: isolated restore, current authority and external-state reconciliation |

<a id="design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-3-content-sharing-and-actual-material"></a>

#### 3. Content, sharing and actual material

<a id="design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-source-update-and-separate-publication"></a>

##### Source update and separate publication

Presentation resolves authorized source/draft versions and returns read-only differences. Explicit selected apply rechecks those versions and saves only intended draft changes, preserving unrelated overrides and other resumes. Separate owner confirmation names the reviewed candidate; Presentation protects exact evidence references through Files and commits the publication manifest/live pointer/result within its defined consistency boundary.

[Selected apply and separately confirmed publication](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/03-component-and-module-design/components/diagrams/presentation-update-publication.svg)

[Owning design and editable exports](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-professional-presentation-md--heading-4-update-and-publication-protocol).

Stale comparisons conflict/recompare; denied operations do not mutate. Lost save/publish responses resolve the same command outcome. Failed/unknown reference finalization retains protection until consumer evidence permits release. Draft save, publication, PDF availability and employer access remain distinct outcomes under the [accepted policy](../../02-Requirements-Engineering/01-Software-Requirements-Specification/07-Change-And-Baseline/03-Requirements-Questions-And-Decisions.md#change-and-baseline-open-questions-and-decisions--id-owner-accepted-profile-update-policy).

<a id="design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-pdflink-management-and-protected-retrieval"></a>

##### PDF/link management and protected retrieval

Sharing authorizes owner-side configuration against exact versions. Download mode changes neither rotate passwords nor disable links implicitly. Viewer context is independently link-scoped; it proves password possession under reviewed policy, not named employer identity.

At retrieval, Sharing resolves current link/viewer generation, selected publication/content, language/mode and exact matching rendition. Files supplies actual usable identity and controlled delivery. The evaluated admission protocol must cover revocation/configuration/publication races; direct paths, caches and range requests cannot bypass applicable checks. Missing variants return their permitted actual state without draft/old-language fallback. Already emitted bytes cannot be recalled.

[Protected retrieval sequence and failure cases](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-representation-and-sharing-md--heading-4-protected-retrieval-and-revocation-protocol) own the detailed diagram and unresolved serving mechanism.

<a id="design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-manual-application-and-actual-capture"></a>

##### Manual application and actual capture

Applications owns preparation/progress without implicit sending. An explicit actual-event/material command resolves exact admitted artifacts, protects references through Files and commits attributable submission/material completeness. Finalization reconciles actual committed consumer evidence. Capture does not publish, change a sharing link or certify provider receipt. Incomplete material stays labeled incomplete; later profile/publication edits cannot rewrite actual submitted material.

[Actual-material capture sequence](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/03-component-and-module-design/components/diagrams/applications-capture-sequence.svg) and [Applications design](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-applications-md) define duplicate/lost-response/reference failure behavior.

<a id="design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-4-provider-interactions"></a>

#### 4. Provider interactions

<a id="design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-deliberate-send"></a>

##### Deliberate send

Communication validates current account/provider capability and reviewed recipient/content/attachment intent, then records durable send attempt context. The scoped worker dispatches the same attempt under the actual provider contract and records observed acceptance/failure/unknown state. Provider acceptance is not recipient delivery or reading, and does not automatically create a complete application-history capture.

On timeout/lost response, reconcile the existing attempt before any consequential repeat. An expired local worker lease or generic queue retry cannot prove no send occurred. Read-only mail access creates no send intent. [Send sequence](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/03-component-and-module-design/components/diagrams/communication-send-sequence.svg) and the [owning component](03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-communication-and-calendar-md) hold exact responsibilities and provider gates.

<a id="design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-local-activity-and-selected-calendar-synchronization"></a>

##### Local activity and selected calendar synchronization

**After MVP.** Shared operating and recovery controls still apply where relevant.

Communication distinguishes locally owned event intent, provider identity/mapping and actual synchronization observations. Explicitly selected synchronization rechecks current capability, field authority, versions/time meaning and actual provider state. Local save does not imply provider success. Conflicts, disconnect/reconnect, deleted targets and ambiguous writes retain real outcomes instead of inventing agreement or repeating effects blindly.

[Calendar reconciliation route](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/03-component-and-module-design/components/diagrams/calendar-reconciliation-route.svg) is the owning view. Actual provider versions/scopes/quotas and source synchronization policies remain pending evaluation/disposition.

<a id="design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-5-work-git-execution-and-deployment"></a>

#### 5. Work, Git, execution and deployment

**After MVP.** Shared operating and recovery controls still apply where relevant.

[After MVP — Guarded handoffs without inherited authority](Diagrams/API/interaction-git-execution-deployment.svg)

[Editable PlantUML](Diagrams/API/interaction-git-execution-deployment.puml) · ![interaction git execution deployment](Diagrams/API/interaction-git-execution-deployment.svg)

<a id="design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-work-and-changed-collaboration"></a>

##### Work and changed collaboration

Work validates current project/action authority, coherent item/task/board/plan relationships and relevant versions before committing. Goal, selected items and delivery plan remain one Sprint Backlog. Period-end records actual context/outcomes; task completion, item acceptance and goal achievement do not follow automatically from a column move or elapsed date.

Identity and the resource owner coordinate effective membership/grant changes and assignment consequences under reviewed policy. Invitation alone is not effective membership, and project access does not grant repository/private-mail authority. Stale contexts and grant changes racing operations need concrete synchronization. See [work mutation/Sprint-close sequence](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/03-component-and-module-design/components/diagrams/work-mutation-sprint-close.svg) and [Identity authorization sequence](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/03-component-and-module-design/components/diagrams/identity-authorization-sequence.svg).

<a id="design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-native-git-and-revision-bound-review"></a>

##### Native Git and revision-bound review

Git authenticates actual client credentials and repository/ref scope for native transfer. Review/merge resolves exact current source/target revisions, current authority and required review/check policy. A guarded native ref update is coordinated with durable metadata observations; SQL rollback cannot undo an already changed ref. Stale revision/review produces conflict/re-evaluation, not a blind merge repeat. See [Git merge sequence](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/03-component-and-module-design/components/diagrams/git-merge-sequence.svg).

<a id="design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-conditional-execution-and-separate-target-stage"></a>

##### Conditional execution and separate target stage

**After MVP.** Shared operating and recovery controls still apply where relevant.

A Git event may produce workflow intent only under an explicit supported authorized trigger. Workflow separately validates immutable code/definition context and actual isolation/resource/secret-enabling evidence before admission. Run identity, launch acknowledgment, terminal outcome, cancellation request, output availability and cleanup remain distinct.

Run success supplies no deployment permission. The target stage separately binds current approval to exact artifact/revision/target/configuration and recovery compatibility. Unknown executor/target effects require same-attempt reconciliation; do not relaunch/redeploy automatically. [Workflow boundaries](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/03-component-and-module-design/components/diagrams/workflow-trust-model.svg) and [deployment sequence](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/03-component-and-module-design/components/diagrams/workflow-deployment-sequence.svg) own detailed mechanisms/gates.

<a id="design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-6-policy-admission-and-recovery"></a>

#### 6. Policy, admission and recovery

Files/Operations authorizes effective policy changes, atomically reserves concurrent growth, validates actual usable artifacts and records true accounting. Protected consumer references exclude reclamation; retiring a record or a finished workflow does not prove bytes/workspace were reclaimed. Partial/unknown storage outcomes retain evidence and applicable protection/accounting for reconciliation. See [admission sequence](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/03-component-and-module-design/components/diagrams/files-admission-sequence.svg) and [reclamation route](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/03-component-and-module-design/components/diagrams/files-reclamation-route.svg).

[MVP with explicitly deferred paths — Isolated restoration and explicit resumption gate](Diagrams/API/interaction-isolated-recovery.svg)

[Editable PlantUML](Diagrams/API/interaction-isolated-recovery.puml) · ![interaction isolated recovery](Diagrams/API/interaction-isolated-recovery.svg)

For UC-D12, the authorized operator identifies source/version and intended scope; Operations coordinates isolated restoration with outbound actions disabled. Affected owners verify schema/content manifests, bytes/native repositories, keys, protected references and actual current authority. Reconcile provider/executor/target effects before resuming work. Missing bytes/keys, inconsistent references or unresolved dangerous effects remain findings, not a successful usable-state claim.

Backup coverage/destination, recovery targets and promotion disposition remain in [Operations/Recovery](../01-High-Level-Design/14-Appendices.md#design-record-06-design-quality-and-security-analysis-03-operations-backup-recovery-and-resilience-md). Restoration does not re-enable historical grants/links or replay pending remote actions automatically. No backup or recovery capability is established by this sequence.

<a id="design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-7-verification-and-completion-boundary"></a>

#### 7. Verification and completion boundary

For each realization, record the exact source scenario/criterion, owner/consumer, candidate/environment, actor and current grants, input/state versions, command/attempt identity, expected effects and unchanged protected state, observed result and remaining limits. Cover normal, denied, invalid, conflict, partial, uncertain and recovery branches where applicable. Diagram coverage is not executed verification.

Focused preservation checks:

- Separate source apply/publication and independent actual material across later changes.
- Current authority on all entry/follow-through paths and no permission inherited from associations/events.
- Protected-reference coordination before consumer commit and safe reconciliation before release.
- Actual provider/native-ref/executor/target observations without false atomicity or blind repeat.
- Coherent work/Sprint history and recovery without access resurrection or remote replay.

Use component policy tests plus actual persistence/concurrency and authorized integration evidence. Remaining work includes exact signatures/types, synchronization/fencing, selected external compatibility, full criterion mapping and implementation-specific scenario sequences. No live product action, acceptance test, baseline approval or new policy selection is performed here.

These technical interaction views adapt FAU's use-case realization/component-collaboration approach; source goals remain in requirements/analysis. Use the [reference map](../01-High-Level-Design/14-Appendices.md#design-record-design-references-and-coverage-md) and [review/handoff](../01-High-Level-Design/14-Appendices.md#design-record-06-design-quality-and-security-analysis-05-design-review-traceability-and-handoff-md).

[Interface and API Design](#design-record-05-interface-and-api-design-interface-and-api-design-md) · [Contract conventions](#design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md) · [Diagram catalog](#design-record-05-interface-and-api-design-diagrams-diagram-catalog-md)

<a id="design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-8-essential-use-case-realization-views"></a>

#### 8. Essential use-case realization views

Only **four complementary diagrams** are added; no new tables, payloads or use-case IDs. Reuse the detailed source/apply/publication, actual-material capture, provider send/calendar, Work/Identity, native Git, execution/deployment and recovery sequences already linked in sections 3–6. This prevents a second competing definition of the same collaboration.

<a id="design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-81-selected-actors-and-use-case-boundaries"></a>

##### 8.1 Selected actors and use-case boundaries

[Selected actors and use-case boundaries](Diagrams/API/interaction-essential-use-cases.svg)

[Editable PlantUML](Diagrams/API/interaction-essential-use-cases.puml) · ![interaction essential use cases](Diagrams/API/interaction-essential-use-cases.svg)

Selected existing source-family summary, not new use-case allocation or complete system coverage. No include/extend arrow joins apply, publish or capture: they are distinct deliberate goals/actions, not automatically executed substeps. Other source families remain mapped in section 2.

<a id="design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-82-use-case-realization-through-owner-contracts"></a>

##### 8.2 Use-case realization through owner contracts

[Use-case realization through owner contracts](Diagrams/API/interaction-essential-realization.svg)

[Editable PlantUML](Diagrams/API/interaction-essential-realization.puml) · ![interaction essential realization](Diagrams/API/interaction-essential-realization.svg)

UML-style realization overview, not a claim that every arrow is a network API call. The existing Sharing retrieval sequence owns detailed ordering. Concrete revocation/admission/reference synchronization must still be designed and verified.

<a id="design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-83-separate-owner-commands-across-the-content-journey"></a>

##### 8.3 Separate owner commands across the content journey

[Separate owner commands across the content journey](Diagrams/API/interaction-essential-end-to-end.svg)

[Editable PlantUML](Diagrams/API/interaction-essential-end-to-end.puml) · ![interaction essential end to end](Diagrams/API/interaction-essential-end-to-end.svg)

End-to-end activity spans separate commands and user decisions, not one atomic API transaction or mandatory sequence for every user. Recording a manual submission does not require this exact publication journey; actual submitted material can come from the source-permitted real route. Provider acceptance alone is not an actual submission claim.

<a id="design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-84-alternate-paths-duplicate-commands-and-uncertain-effects"></a>

##### 8.4 Alternate paths, duplicate commands and uncertain effects

[Alternate paths, duplicate commands and uncertain effects](Diagrams/API/interaction-essential-alternates.svg)

[Editable PlantUML](Diagrams/API/interaction-essential-alternates.puml) · ![interaction essential alternates](Diagrams/API/interaction-essential-alternates.svg)

Generic exception interaction complements rather than replaces operation-specific sequences. Local commit response loss uses same-command local reconciliation; remote effects require actual adapter evidence and cannot be inferred from SQL rollback, lease expiry or timeout. No observation API, retry count or automatic effect replay is invented.

<a id="design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-reading-and-coverage-limits"></a>

##### Reading and coverage limits

The existing scenario-to-component map owns source-family references; it is not exact criterion closure. Use-case summaries show goals, realization views show participating contracts, activity views show control flow, and sequences show message ordering/evidence. None proves a selected locking scheme, remote service deployment or atomic transaction across owners and facilities.

No generic orchestration engine, choreography bus, gateway, boundary/control/entity hierarchy or additional interaction state model is introduced solely to satisfy a diagram taxonomy. Actual operations remain owner-coordinated; events carry provenance without granting permission. Optional state/communication diagrams belong with a concrete component when they resolve a real question.

Before implementation, refine exact signatures, permitted inputs/projections, authority/version ordering, actual external capabilities and safe repetition/cancellation behavior. Validate normal/denied/conflict/partial/unknown paths and protected state against an identified candidate; numerical timeout, latency or retry budgets remain actual design decisions. No request, provider operation, ref update, workflow, deployment or live scenario test is executed by this update.

</details>

<a id="design-record-05-interface-and-api-design-diagrams-diagram-catalog-md"></a>

<details>
<summary>Interface and API Design — Diagram Catalog</summary>

<a id="design-record-05-interface-and-api-design-diagrams-diagram-catalog-md--heading-interface-and-api-design--diagram-catalog"></a>

### Interface and API Design — Diagram Catalog

Keep editable sources and SVG/PNG exports synchronized. These are proposed technical interaction and compatibility views.

Current MVP scope and selected mechanisms: [Baseline](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/README.md). Deferred provider, advanced collaboration and workflow-execution designs are not MVP prerequisites.

<a id="design-record-05-interface-and-api-design-diagrams-diagram-catalog-md--heading-api-protocols-contracts-and-compatibility"></a>

#### API protocols, contracts and compatibility

- [Identified command and actual outcome contract](Diagrams/API/api-command-outcome-sequence.svg) · [PlantUML](Diagrams/API/api-command-outcome-sequence.puml) · ![api command outcome sequence](Diagrams/API/api-command-outcome-sequence.svg)
- [Contract evolution and compatibility](Diagrams/API/api-contract-evolution.svg) · [PlantUML](Diagrams/API/api-contract-evolution.puml) · ![api contract evolution](Diagrams/API/api-contract-evolution.svg)

[Owning document](#design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md). Proposed shared contract behavior. Exact routes/types, framework and external compatibility, dispatch and transition mechanisms remain implementation work.

<a id="design-record-05-interface-and-api-design-diagrams-diagram-catalog-md--heading-use-case-realizations-and-interactions"></a>

#### Use-case realizations and interactions

- [Independent Git, execution and deployment admission](Diagrams/API/interaction-git-execution-deployment.svg) · [PlantUML](Diagrams/API/interaction-git-execution-deployment.puml) · ![interaction git execution deployment](Diagrams/API/interaction-git-execution-deployment.svg)
- [Isolated recovery and resumption gate](Diagrams/API/interaction-isolated-recovery.svg) · [PlantUML](Diagrams/API/interaction-isolated-recovery.puml) · ![interaction isolated recovery](Diagrams/API/interaction-isolated-recovery.svg)

[Owning document](#design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md). Cross-component responsibility overviews complement detailed component-owned sequences; exact synchronization, compatibility and operating evidence remain pending.

<a id="design-record-05-interface-and-api-design-diagrams-diagram-catalog-md--heading-essential-api-and-contract-views"></a>

#### Essential API and contract views

- [Consumers, owner contracts and external adapters](Diagrams/API/api-essential-boundaries.svg) · [PlantUML](Diagrams/API/api-essential-boundaries.puml) · ![api essential boundaries](Diagrams/API/api-essential-boundaries.svg)
- [Protocol selection by actual boundary need](Diagrams/API/api-essential-selection.svg) · [PlantUML](Diagrams/API/api-essential-selection.puml) · ![api essential selection](Diagrams/API/api-essential-selection.svg)
- [Contract-first refinement without mandatory code generation](Diagrams/API/api-essential-contract-workflow.svg) · [PlantUML](Diagrams/API/api-essential-contract-workflow.puml) · ![api essential contract workflow](Diagrams/API/api-essential-contract-workflow.svg)
- [Consumer expectations and provider verification](Diagrams/API/api-essential-consumer-verification.svg) · [PlantUML](Diagrams/API/api-essential-consumer-verification.puml) · ![api essential consumer verification](Diagrams/API/api-essential-consumer-verification.svg)

[Owning API contract guide](#design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-9-essential-api-and-contract-views). Existing evolution/interaction views reused; no protocol, gateway, schema tooling or endpoint allocated.

<a id="design-record-05-interface-and-api-design-diagrams-diagram-catalog-md--heading-essential-use-case-realization-views"></a>

#### Essential use-case realization views

- [Selected actors and use-case boundaries](Diagrams/API/interaction-essential-use-cases.svg) · [PlantUML](Diagrams/API/interaction-essential-use-cases.puml) · ![interaction essential use cases](Diagrams/API/interaction-essential-use-cases.svg)
- [Use-case realization through owner contracts](Diagrams/API/interaction-essential-realization.svg) · [PlantUML](Diagrams/API/interaction-essential-realization.puml) · ![interaction essential realization](Diagrams/API/interaction-essential-realization.svg)
- [Separate owner commands across the content journey](Diagrams/API/interaction-essential-end-to-end.svg) · [PlantUML](Diagrams/API/interaction-essential-end-to-end.puml) · ![interaction essential end to end](Diagrams/API/interaction-essential-end-to-end.svg)
- [Alternate paths, duplicate commands and uncertain effects](Diagrams/API/interaction-essential-alternates.svg) · [PlantUML](Diagrams/API/interaction-essential-alternates.puml) · ![interaction essential alternates](Diagrams/API/interaction-essential-alternates.svg)

[Owning interaction guide](#design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-8-essential-use-case-realization-views). Existing detailed component sequences reused; no new source use cases, API payloads or execution evidence allocated.

<a id="design-record-05-interface-and-api-design-diagrams-diagram-catalog-md--heading-november-4-release-applicability"></a>

#### November 4 release applicability

Current MVP figures replace the former common-product boundary. Future and historical figures retain their details without committing them to MVP.

| Editable source | Current applicability |
| --- | --- |
| [api-essential-contract-workflow.puml](Diagrams/API/api-essential-contract-workflow.puml) | Method / document navigation|
| [interaction-git-execution-deployment.puml](Diagrams/API/interaction-git-execution-deployment.puml) | Future after MVP|

<a id="design-record-05-interface-and-api-design-diagrams-diagram-catalog-md--heading-complete-diagram-alignment--november-4"></a>

#### Complete diagram alignment — November 4

[Full project inventory and verification limits](../01-High-Level-Design/14-Appendices.md#design-record-01-software-architecture-diagrams-diagram-catalog-md). This current disposition supersedes earlier partial diagram-allocation lists.

| Editable source or visual | Current applicability | Matching exports |
| --- | --- | --- |
| [api-command-outcome-sequence.puml](Diagrams/API/api-command-outcome-sequence.puml) | MVP core / cross-cutting| [SVG](Diagrams/API/api-command-outcome-sequence.svg) · ![api command outcome sequence](Diagrams/API/api-command-outcome-sequence.svg) |
| [api-contract-evolution.puml](Diagrams/API/api-contract-evolution.puml) | MVP core / cross-cutting| [SVG](Diagrams/API/api-contract-evolution.svg) · ![api contract evolution](Diagrams/API/api-contract-evolution.svg) |
| [api-essential-boundaries.puml](Diagrams/API/api-essential-boundaries.puml) | Mixed MVP / future| [SVG](Diagrams/API/api-essential-boundaries.svg) · ![api essential boundaries](Diagrams/API/api-essential-boundaries.svg) |
| [api-essential-consumer-verification.puml](Diagrams/API/api-essential-consumer-verification.puml) | MVP core / cross-cutting| [SVG](Diagrams/API/api-essential-consumer-verification.svg) · ![api essential consumer verification](Diagrams/API/api-essential-consumer-verification.svg) |
| [api-essential-contract-workflow.puml](Diagrams/API/api-essential-contract-workflow.puml) | Method / document navigation| [SVG](Diagrams/API/api-essential-contract-workflow.svg) · ![api essential contract workflow](Diagrams/API/api-essential-contract-workflow.svg) |
| [api-essential-selection.puml](Diagrams/API/api-essential-selection.puml) | Mixed MVP / future| [SVG](Diagrams/API/api-essential-selection.svg) · ![api essential selection](Diagrams/API/api-essential-selection.svg) |
| [interaction-essential-alternates.puml](Diagrams/API/interaction-essential-alternates.puml) | MVP core / cross-cutting| [SVG](Diagrams/API/interaction-essential-alternates.svg) · ![interaction essential alternates](Diagrams/API/interaction-essential-alternates.svg) |
| [interaction-essential-end-to-end.puml](Diagrams/API/interaction-essential-end-to-end.puml) | MVP core / cross-cutting| [SVG](Diagrams/API/interaction-essential-end-to-end.svg) · ![interaction essential end to end](Diagrams/API/interaction-essential-end-to-end.svg) |
| [interaction-essential-realization.puml](Diagrams/API/interaction-essential-realization.puml) | MVP core / cross-cutting| [SVG](Diagrams/API/interaction-essential-realization.svg) · ![interaction essential realization](Diagrams/API/interaction-essential-realization.svg) |
| [interaction-essential-use-cases.puml](Diagrams/API/interaction-essential-use-cases.puml) | MVP core / cross-cutting| [SVG](Diagrams/API/interaction-essential-use-cases.svg) · ![interaction essential use cases](Diagrams/API/interaction-essential-use-cases.svg) |
| [interaction-git-execution-deployment.puml](Diagrams/API/interaction-git-execution-deployment.puml) | Future after MVP| [SVG](Diagrams/API/interaction-git-execution-deployment.svg) · ![interaction git execution deployment](Diagrams/API/interaction-git-execution-deployment.svg) |
| [interaction-isolated-recovery.puml](Diagrams/API/interaction-isolated-recovery.puml) | Mixed MVP / future| [SVG](Diagrams/API/interaction-isolated-recovery.svg) · ![interaction isolated recovery](Diagrams/API/interaction-isolated-recovery.svg) |

</details>

<a id="design-record-05-interface-and-api-design-interface-and-api-design-md"></a>

<details>
<summary>Resumefolio — Interface and API Design</summary>

<a id="design-record-05-interface-and-api-design-interface-and-api-design-md--heading-resumefolio--interface-and-api-design"></a>

### Resumefolio — Interface and API Design

Current implementation choices and scope: [Baseline](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/README.md). Runtime verification remains subject to its gates.

**Use this folder to understand communication contracts and how components collaborate to realize existing scenarios.** Shared protocol/result/compatibility conventions belong here; exact signatures and domain invariants remain with their owning components.

Owner and decision authority: Farhad. **Current position:** both documents are populated with project-specific proposed design. **Twelve local diagrams** illustrate contracts, protocol selection, consumer verification, use-case realization and safe interactions; detailed component diagrams are linked at their owning locations. No implemented route catalog, adopted frontend/API stack, verified external integration or accepted baseline is claimed.

[Reading route](#design-record-05-interface-and-api-design-interface-and-api-design-md--heading-1-reading-route) · [Document guide](#design-record-05-interface-and-api-design-interface-and-api-design-md--heading-2-find-the-right-record) · [Diagrams](#design-record-05-interface-and-api-design-interface-and-api-design-md--heading-3-diagrams-and-owning-views) · [Boundaries](#design-record-05-interface-and-api-design-interface-and-api-design-md--heading-4-ownership-and-preservation-rules) · [Readiness](#design-record-05-interface-and-api-design-interface-and-api-design-md--heading-5-review-and-current-limits)

<a id="design-record-05-interface-and-api-design-interface-and-api-design-md--heading-1-reading-route"></a>

#### 1. Reading route

1. Read [interface requirements](../../02-Requirements-Engineering/01-Software-Requirements-Specification/03-Requirements-Specification/07-External-Interface-Requirements.md#requirements-specification-external-interface-requirements) and [analysis interfaces](../../03-System-Analysis/04-Interfaces-Security-And-Quality.md#analysis-interfaces-security-and-quality-analysis--12-interfaces-and-external-interactions) for existing boundary meanings and source status.
2. Read [API Protocols, Contracts and Compatibility](#design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md) for protocol options, required contract records, HTTP/result semantics, expected versions, command identity, protected/external exchanges and compatibility.
3. Read [Use-Case Realizations and Interactions](#design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md) for UC-D01–UC-D12/SB-M01–SB-M16 responsibility coverage, technical routes, failure boundaries and linked component sequences.
4. Follow the [component catalog](02-Module-Breakdown.md#design-record-03-component-and-module-design-component-and-module-design-md) for concrete operations/types and the [runtime design](../01-High-Level-Design/14-Appendices.md#design-record-01-software-architecture-03-process-view-concurrency-and-runtime-behavior-md) for concurrency and reconciliation obligations.
5. Record consequential choices in [ADRs](../ADR/Decision-Index.md#design-record-07-design-decisions-design-decisions-md) and actual criterion/evidence disposition in [review/handoff](../01-High-Level-Design/14-Appendices.md#design-record-06-design-quality-and-security-analysis-05-design-review-traceability-and-handoff-md).

The retained numbers are stable document locators. Component/external integration guidance is included in document 01; no separate file 02 is required merely to close the numbering gap.

<a id="design-record-05-interface-and-api-design-interface-and-api-design-md--heading-2-find-the-right-record"></a>

#### 2. Find the right record

| Question | Owning location |
| --- | --- |
| Which transport fits browser, local component, Git or external consumers? | [01 — Protocol choices](#design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-2-protocol-choices-by-consumer) |
| What must each operation contract specify? | [01 — Required contract record](#design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-3-required-contract-record) |
| How do HTTP results, stale writes and uncertain effects differ? | [01 — Results and repetition](#design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md) |
| How are clients, workers and stored payloads kept compatible? | [01 — Compatibility](#design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-7-versioning-and-compatibility) |
| Which components realize each existing source scenario? | [03 — Scenario map](#design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-2-scenario-to-component-map) |
| Where are detailed publication, send, Git, work and target sequences? | [03 — Owning component links](#design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md) |
| Where do schema/storage and threat/operating details belong? | [Data](04-Database-Design.md#design-record-04-data-design-data-design-md) and [Quality/Security](../01-High-Level-Design/14-Appendices.md#design-record-06-design-quality-and-security-analysis-design-quality-and-security-analysis-md) |

<a id="design-record-05-interface-and-api-design-interface-and-api-design-md--heading-3-diagrams-and-owning-views"></a>

#### 3. Diagrams and owning views

<a id="design-record-05-interface-and-api-design-interface-and-api-design-md--heading-identified-command-and-actual-outcome"></a>

##### Identified command and actual outcome

[Command handling and permitted outcome lookup](Diagrams/API/api-command-outcome-sequence.svg)

[Owning contract document](#design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md) · [PlantUML](Diagrams/API/api-command-outcome-sequence.puml) · ![api command outcome sequence](Diagrams/API/api-command-outcome-sequence.svg)

Transport acceptance and a local commit do not certify remote completion. Lost responses resolve the same attributable operation before a consequential repeat.

<a id="design-record-05-interface-and-api-design-interface-and-api-design-md--heading-independent-git-execution-and-target-admission"></a>

##### Independent Git, execution and target admission

**After MVP.** Shared operating and recovery controls still apply where relevant.

[After MVP — Independent authority at Git, execution and deployment boundaries](Diagrams/API/interaction-git-execution-deployment.svg)

[Owning realizations document](#design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md) · [PlantUML](Diagrams/API/interaction-git-execution-deployment.puml) · ![interaction git execution deployment](Diagrams/API/interaction-git-execution-deployment.svg)

The overview does not prescribe automatic execution or deployment. Explicit trigger policy, actual execution-enabling evidence and separate target approval remain necessary.

<a id="design-record-05-interface-and-api-design-interface-and-api-design-md--heading-contract-guide--six-local-views"></a>

##### Contract guide — six local views

The [essential API package](#design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md--heading-9-essential-api-and-contract-views) adds four views to the existing command/outcome sequence and contract-evolution diagram:

- [Consumer/provider boundaries](Diagrams/API/api-essential-boundaries.svg) · [PlantUML](Diagrams/API/api-essential-boundaries.puml) · ![api essential boundaries](Diagrams/API/api-essential-boundaries.svg)
- [Protocol selection by actual consumer need](Diagrams/API/api-essential-selection.svg) · [PlantUML](Diagrams/API/api-essential-selection.puml) · ![api essential selection](Diagrams/API/api-essential-selection.svg)
- [Contract-first refinement](Diagrams/API/api-essential-contract-workflow.svg) · [PlantUML](Diagrams/API/api-essential-contract-workflow.puml) · ![api essential contract workflow](Diagrams/API/api-essential-contract-workflow.svg)
- [Consumer expectations and provider verification](Diagrams/API/api-essential-consumer-verification.svg) · [PlantUML](Diagrams/API/api-essential-consumer-verification.puml) · ![api essential consumer verification](Diagrams/API/api-essential-consumer-verification.svg)

These views select no public REST API, gateway, GraphQL/gRPC/broker, code-generation tool or versioned endpoint scheme. Module contracts can remain in-process; native Git and protected-byte/provider/control exchanges retain their actual distinct contracts. Consumer expectations cannot override accepted behavior or privacy.

<a id="design-record-05-interface-and-api-design-interface-and-api-design-md--heading-interaction-guide--six-local-views"></a>

##### Interaction guide — six local views

The [essential realization package](#design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md--heading-8-essential-use-case-realization-views) adds four views to the existing Git/execution/deployment overview and isolated-recovery sequence:

- [Selected actors and existing use-case families](Diagrams/API/interaction-essential-use-cases.svg) · [PlantUML](Diagrams/API/interaction-essential-use-cases.puml) · ![interaction essential use cases](Diagrams/API/interaction-essential-use-cases.svg)
- [Protected retrieval realized through owner contracts](Diagrams/API/interaction-essential-realization.svg) · [PlantUML](Diagrams/API/interaction-essential-realization.puml) · ![interaction essential realization](Diagrams/API/interaction-essential-realization.svg)
- [Separate commands across the content journey](Diagrams/API/interaction-essential-end-to-end.svg) · [PlantUML](Diagrams/API/interaction-essential-end-to-end.puml) · ![interaction essential end to end](Diagrams/API/interaction-essential-end-to-end.svg)
- [Alternate paths and uncertain effects](Diagrams/API/interaction-essential-alternates.svg) · [PlantUML](Diagrams/API/interaction-essential-alternates.puml) · ![interaction essential alternates](Diagrams/API/interaction-essential-alternates.svg)

Document 03 reuses the detailed component-owned publication/retrieval/capture/send/calendar/work/Git/executor/file sequences. Its scenario map describes responsibility, not exact criterion closure. The content journey spans deliberate separate actions, not one automatic publish/send/submit transaction. Generic alternate paths complement, rather than replace, each operation's actual contract.

The [complete diagram catalog](#design-record-05-interface-and-api-design-diagrams-diagram-catalog-md) contains **12 PlantUML sources, 12 SVGs and 12 PNGs**. Counts refer to distinct local views, not repeated links or component diagrams maintained elsewhere. Read captions at the stated abstraction level: arrows are not proof of remote-service deployment, automatic permission, atomicity or runtime behavior. This README update adds no table or diagram.

<a id="design-record-05-interface-and-api-design-interface-and-api-design-md--heading-4-ownership-and-preservation-rules"></a>

#### 4. Ownership and preservation rules

Requirements/analysis retain source goals and scenario meaning. This folder refines provided/required contracts and collaborations; resource owners enforce actual operations. Data design owns schema/reference integrity, runtime owns concurrency/reconciliation, security owns threat controls and Operations owns the actual recovery procedure.

Preserve these shared rules:

- Current actor/resource/action authority applies across browser, native-client, file, background and callback entry paths.
- Source preview/apply, separately confirmed publication and actual submitted material remain independent.
- Private cached/direct/range retrieval cannot silently bypass current eligibility or substitute another revision/language.
- Command identity prevents defined duplicate local intent; it does not prove remote exactly-once execution.
- Provider acceptance is not recipient receipt; cancellation request is not confirmed stop; terminal execution is not cleanup; run success is not target approval.
- Membership, resource association and emitted events convey no unrelated permissions or automatic side effects.
- Recovery reconciles current authority and actual external state before resumption, without replaying uncertain actions.

<a id="design-record-05-interface-and-api-design-interface-and-api-design-md--heading-5-review-and-current-limits"></a>

#### 5. Review and current limits

Before implementation handoff, specify exact signatures/routes and payload/result schemas, requiredness/units/language/time/revision conventions, authority and anti-forgery controls, status/precondition/error mappings, pagination/resource bounds, command/attempt repetition semantics and compatibility behavior. Each realization needs source/criterion links, current context/version checks, consistency boundary, external effects and applicable failure/recovery branches.

Verify actual framework, persistence/concurrency, protected serving and selected provider/Git/executor compatibility using suitable authorized evidence. Mock results and diagram/link checks do not establish interoperability, safe remote retries, isolation or recovery readiness. Final transport/client/framework facilities, external capabilities, synchronization and exact criterion closure remain pending.

No endpoint, provider send, repository transfer, execution, deployment, account/link change or acceptance test is performed by this documentation. Scope and baseline acceptance remain with their source authorities.

<a id="design-record-05-interface-and-api-design-interface-and-api-design-md--heading-6-fau-basis-and-maintenance"></a>

#### 6. FAU basis and maintenance

FAU's component interfaces and use-case realization views inform these documents. HTTP conventions, compatibility records and this folder structure are project adaptations, not a university-mandated API style. See the [reference map](../01-High-Level-Design/14-Appendices.md#design-record-design-references-and-coverage-md).

When changing a contract, identify consumers and stored pending payloads, reconcile source/owner/data/runtime/security consequences, update the owning realization and ADR, regenerate affected diagrams and check local links. Preserve historical evidence and distinguish documentation checks from product verification.

[System Design home](../../01-Project-Planning/02-Project-Management-Plan.md#stage-4-system-design) · [Component Design](02-Module-Breakdown.md#design-record-03-component-and-module-design-component-and-module-design-md) · [Diagram catalog](#design-record-05-interface-and-api-design-diagrams-diagram-catalog-md)

</details>

## Endpoint readiness checklist

For every implemented endpoint, record the supported request and response shapes, actor and scope, relevant status codes and compatibility policy. Link contract tests for valid, unauthorized, invalid and conflicting requests. Confirm implementation-specific routes against the candidate before marking the contract stable.

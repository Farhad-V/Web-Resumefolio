# Implementation

Status: Not started. The responsibilities below are selected Design, not claims that modules or endpoints exist.

[Implementation index](../Sdlc-guide.md#stage-5-agile-iterative-development) · [SDD](../System-design-guide.md) · [Technical decisions](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/technical-decisions.md)

## Build the selected capability

Start with the selected backlog item, its acceptance criteria and the relevant [analysis and design](03-Detailed-analysis-and-design.md). Build a usable slice through the affected layers. Link the actual code and interface changes to the work item and its [iteration tests](05-Testing.md#test-within-the-iteration). If the work changes an accepted design decision, record the reason and consequence in the [design deviation log](06-Sprint-review.md#design-deviation-log).

## Responsibilities to map to actual code

| System / responsibility | Actual source paths | Implementation status |
| --- | --- | --- |
| Core — invited accounts, authentication and policies | Not created | Not started |
| Core — profile, independent resume drafts and explicit publication | Not created | Not started |
| Core — private library, PDFs and protected employer sharing | Not created | Not started |
| Core — manual applications and actual submitted artifacts | Not created | Not started |
| Core — dashboard and user-scoped ProjectForge client | Not created | Not started |
| ProjectForge — SSO, grants, native Git, files/history and issues/board | Not created | Not started |
| Each system — local persistence, outbox, jobs and audit | Not created | Not started |

React pages and reusable components belong to each Laravel application through Inertia. Laravel routes/controllers and policies retain server-side authority; client-side visibility is not authorization. Keep trusted Blade PDF templates separate from interactive React pages. No source paths or installed adapters are asserted before scaffolding.

Map responsibilities to actual namespaces/directories after scaffolding. Keep Core and ProjectForge databases, keys, sessions and private storage separate; do not introduce a shared process/database to make this table easier to fill.

## Record database changes when implemented

For each migration record its real path, owning system, affected tables/indexes/constraints, requirement links, compatibility/data-loss implications, execution evidence and rollback or recovery procedure. No implemented schema or migration is recorded yet.

## Record API and UI entry points when implemented

For each real entry point record route/method, owning system, actor and resource authority, request/response/error contract, version/idempotency rules and contract-test evidence. Link handlers, application services and persistence responsibilities. Never publish tokens, private keys or actual user content. No implemented endpoint is recorded yet.

## Record operational code when implemented

Link real job handlers, scheduled tasks, immutable artifact lifecycle, quota enforcement, audit events and configuration examples. Record trust-boundary/failure behavior and verification alongside each implementation; the Design description alone is not execution evidence.

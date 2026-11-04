# Code Structure and Implemented Interfaces

Status: Not started. The responsibilities below are selected Design, not claims that modules or endpoints exist.

[Implementation index](README.md) · [SDD](../04-system-design/README.md) · [Technical decisions](../../baseline/technical-decisions.md)

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

Map responsibilities to actual namespaces/directories after scaffolding. Keep Core and ProjectForge databases, keys, sessions and private storage separate; do not introduce a shared process/database to make this table easier to fill.

## Record database changes when implemented

For each migration record its real path, owning system, affected tables/indexes/constraints, requirement links, compatibility/data-loss implications, execution evidence and rollback or recovery procedure. No implemented schema or migration is recorded yet.

## Record API and UI entry points when implemented

For each real entry point record route/method, owning system, actor and resource authority, request/response/error contract, version/idempotency rules and contract-test evidence. Link handlers, application services and persistence responsibilities. Never publish tokens, private keys or actual user content. No implemented endpoint is recorded yet.

## Record operational code when implemented

Link real job handlers, scheduled tasks, immutable artifact lifecycle, quota enforcement, audit events and configuration examples. Record trust-boundary/failure behavior and verification alongside each implementation; the Design description alone is not execution evidence.

# Project Setup

Status: Not started. This is a checklist for recording verified Setup, not a runnable installation guide yet.

[Implementation index](../Sdlc-guide.md#stage-5-agile-iterative-development) · [Selected stack](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/technical-decisions.md#t01--runtime-frontend-and-persistence) · [G1 requirements](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/implementation-sequence.md#gate-register)

## Iteration outcome

The first iteration establishes a repeatable local environment for both applications. Start from the [setup work item](https://github.com/Farhad-V/Web-Resumefolio/issues/37), confirm its acceptance checks, then build and verify a clean setup. Review the results before selecting a dependent feature. Record the outcome and any follow-up in the [iteration review](06-Sprint-review.md#iteration-review).

## Selected targets versus verified environment

| Item | Selected target | Verified project value |
| --- | --- | --- |
| Framework / runtime | Laravel 13 / maintained PHP 8.4 patch | Not recorded |
| Dependency management | Composer 2; compatible pinned dependencies | No project lockfile recorded |
| Database | Isolated MySQL 8.4 LTS / InnoDB / utf8mb4 | Not created or verified |
| Frontend | React 19 / Inertia 3 / Tailwind 4 / Vite; Blade for PDF templates | Not installed |
| Build runtime | Node 24 LTS | Project build not verified |
| Core / ProjectForge | Separate applications, DB users, keys, sessions and storage | No working application setup recorded |

## Complete during Project Setup

- Record OS, actual maintained versions and required PHP extensions from the resolved dependencies.
- Record the actual application paths and clean install/build commands after executing them successfully.
- Commit appropriate dependency lockfiles during the separately authorized implementation workflow.
- Create a safe example configuration containing names and non-secret examples only; document how local secrets are supplied.
- Record isolated database creation, migration and fixture/seed commands; never target the existing demo database implicitly.
- Record local app, queue and scheduler startup/shutdown commands, ports and expected health responses.
- Record test database isolation and actual test/lint/build commands with their results.
- Document SMTP test delivery separately from development log output; never put credentials into this guide.
- Verify a clean checkout can follow the guide before marking Setup complete.

## Execution record

No Setup commands have been executed for the MVP implementation. Replace this statement with dated evidence when Setup is authorized and completed. Local tools existing on a workstation do not establish a working project environment.

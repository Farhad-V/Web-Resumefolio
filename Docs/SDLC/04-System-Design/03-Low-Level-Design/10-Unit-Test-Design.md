# 10. Unit Test Design

[Low-Level Design index](03-Low-Level-Design.md)

## 10.1 Cases by Module

| Module | Unit-level cases |
| --- | --- |
| Identity and Access | Expired invitation, disabled account and resource policy decisions |
| Professional Presentation | Selected apply, stale draft, immutable publication |
| Files and Sharing | Validation, referenced-artifact retention and revoked access |
| Applications | Identical retry, changed-payload conflict and intact submitted history |
| Git and Work Management | Role and scope decisions, permitted transitions and stale issue versions |

## 10.2 Mocks and Test Data
Use deterministic clocks, synthetic accounts and fake adapter outcomes for unit tests. Verify MySQL behavior, native Git, browser flows and restore through the matching integration or release checks in the [Test Strategy](../../05-Agile-Iterative-Development/02-Test-Strategy.md). These cases are designed and pending execution.

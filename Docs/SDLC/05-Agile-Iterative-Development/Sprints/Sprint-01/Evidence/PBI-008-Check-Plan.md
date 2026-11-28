# PBI-008: Planned Criterion Checks

[Coverage review](PBI-008.md) · [Exact RTM checks/contracts](../../../../02-Requirements-Engineering/03-Requirements-Traceability-Matrix/02-Criterion-Coverage.md) · [Existing unit/boundary cases](../../../../04-System-Design/03-Low-Level-Design/10-Unit-Test-Design.md)

**Planned, not executed.** Each non-deferred criterion is its check identity; its RTM Observable check is the oracle and Design reference is the owning contract. Preserve its [source verification method/gate](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/criterion-dispositions.csv). Select the action/environment below, arrange the criterion's actor/state/input and compare actual output/state/bytes with that oracle. Include denied/stale/interrupted/concurrent cases where specified; protect unrelated data. Resolve executable fixtures/commands during implementation.

| Criterion prefix | Planned exercise / minimum evidence |
| --- | --- |
| ACC | Owner/other-user/admin/viewer/grant/expiry/revocation matrix; real browser/service authorization; UT-01/02 companions. |
| AFO | Policy, formats, limits, competing quota, interruption/cleanup, audit and guidance; MySQL/filesystem; UT-04/06/15/16. |
| BIZ | Selected actor journeys; identified-candidate workload and recovery evidence for D05. |
| BRL | Independent resumes, protected bytes/references, lifecycle/time, crash/retry/restore; persistence/storage; UT-03–06/08/11/12/16. |
| DOM | Terminology/scope/provenance walkthrough; D06/D07 actual applicability/license evidence; D08 measured workload/recovery later. |
| EIF | Valid/denied/invalid/unavailable interface requests; real transport/storage/browser/recovery as specified; UT-10/14/15 companions. |
| GIT | Real-client transfers/refs/history, denied grants, issue context and restore; UT-10/13 companions. |
| APP | Manual status independent of capture, exact history/correction/retry/restore; browser/MySQL/filesystem; UT-04/05/11/12. |
| PDF | Modes/languages/revisions, direct/range authorization, rendering failures/retention/restore; real renderer/storage; UT-08/09/12/16. |
| PRP | Two-resume preview/select/apply/publication, manual variants/evidence/display; browser/storage; UT-03/04/08/09. |
| PKS | Fixed board, allowed/denied/stale moves, assignee/priority/date/timezone and restore; MySQL/browser; UT-07/13. |
| QSR | Each row's workload/accessibility/security/integrity/audit/recovery scenario; measured bounds, candidate and limitations. |
| USR | Corresponding actor journey including denial/incomplete outcomes; actual actor acceptance remains G6. |
| MVP-AC01–10 | Exact supplemental outcomes and delivery owners in coverage review; real identity/Git/PDF/concurrency/recovery boundaries. |

Exclude all 129 Deferred rows from MVP execution. Unit cases do not prove real-boundary guarantees. Record revision/environment, expected/actual result and sanitized evidence through the [RTM procedure](../../../../02-Requirements-Engineering/03-Requirements-Traceability-Matrix/03-Recording-Verified-Evidence.md). No runtime result or new requirement is created here.

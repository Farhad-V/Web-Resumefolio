
<a id="process-and-approach-02-feasibility-study"></a>

<a id="process-and-approach-02-feasibility-study--heading-resumefolio--feasibility-study"></a>
# Resumefolio — Feasibility Study

**Assessment:** The existing host has been inventoried. Its ability to run the new MVP alongside the existing application still needs to be verified. Start by checking capacity and isolation, then use the [MVP verification gates](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/implementation-sequence.md#gate-register) to decide when each dependent activity can proceed.

<a id="process-and-approach-02-feasibility-study--heading-what-needs-to-be-proven"></a>
## What needs to be proven

| Area | Next check |
| --- | --- |
| **Host capacity and isolation** | Measure CPU, memory and disk headroom with the existing application and representative Core, MySQL, media and ProjectForge Git workloads. Verify that the two new applications can use separate accounts, databases and storage. [Host assessment](https://github.com/Farhad-V/Web-Resumefolio/issues/2) |
| **Environment compatibility** | Verify maintained runtime versions, dependencies and isolated MySQL for the selected stack. Demonstrate a clean install, build and test before closing Setup. [Project Setup](https://github.com/Farhad-V/Web-Resumefolio/issues/37) |
| **Identity and Git** | Prove scoped sign-in, real Git transfers, revocation and denial with two users. Resolve isolation or capacity failures before enabling dependent Git features. [Git security test](https://github.com/Farhad-V/Web-Resumefolio/issues/38) |
| **Operations and recovery** | Demonstrate delivery of invitation and recovery emails, verify TLS renewal and background processing, and test an independent backup and isolated restore. [Email delivery](https://github.com/Farhad-V/Web-Resumefolio/issues/5) · [Restore drill](https://github.com/Farhad-V/Web-Resumefolio/issues/27) |

<a id="process-and-approach-02-feasibility-study--heading-budget-schedule-and-licenses"></a>
## Budget, schedule and licenses

Use the [planning capacity and sizing record](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/01-project-planning/11-capacity-and-preliminary-sizing.md) and [resource constraints](../../../01-Project-Planning/03-Feasibility-And-Risk-Assessment.md#resource-constraints) as inputs. Check how setup effort, license obligations and any additional infrastructure affect feasibility before estimating delivery.

<a id="process-and-approach-02-feasibility-study--id-server-observation-2026-11-01"></a>

<a id="process-and-approach-02-feasibility-study--heading-server-evidence--november-1-2026"></a>
## Server evidence — November 1, 2026

| Observed | What it tells us |
| --- | --- |
| Hetzner CX23, 2 vCPU, 4 GB RAM and 40 GB disk allocation | Starting point for capacity checks. A low-load sample showed about 2.8 GiB memory and 30 G root filesystem space available. |
| Existing Laravel site with Nginx, PHP 8.3 and MySQL 8.0 | The host already carries application traffic. The observed stack belongs to that deployment. Verify the selected MVP stack separately. |
| HTTPS login returned HTTP 200 and passed TLS verification | HTTPS worked during the check. Renewal and recovery still need their own evidence. |
| Application backup and queue or scheduler operation were not established by the checks | Confirm coverage and configuration before relying on them. The owner subsequently reported that application backups had not been set up. |

The first inventory came from owner-supplied observations. A follow-up read-only inspection confirmed selected versions and HTTPS behavior. The samples establish what was observed on that date. See the [server inventory](../06-Validation-And-Traceability/04-Server-Observation-2026-11-01json.md#validation-and-traceability-server-observation-2026-11-01), [read-only checks](../06-Validation-And-Traceability/05-Server-Readonly-Check-2026-11-01json.md#validation-and-traceability-server-readonly-check-2026-11-01) and [operating evidence](../06-Validation-And-Traceability/02-Operating-Check-2026-11-01json.md#validation-and-traceability-operating-check-2026-11-01).

<a id="process-and-approach-02-feasibility-study--heading-after-mvp"></a>
## After MVP

Google mail and calendar integration and user-controlled workflow execution are deferred. Revisit provider access and runner isolation when those capabilities enter scope. See [requirements decisions](../07-Change-And-Baseline/03-Requirements-Questions-And-Decisions.md#change-and-baseline-open-questions-and-decisions).

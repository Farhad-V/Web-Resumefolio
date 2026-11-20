# Deployment Plan

**Status** Version `1.0.0` is the planned first stable Resumefolio release and delivers the MVP. A release candidate and production deployment have yet to be recorded.

## Stable MVP release

1. Verify the selected MVP acceptance criteria on a specific candidate. Record the supported interfaces users and integrations can rely on, the compatibility policy for those interfaces, and any known limitations.
2. Complete the applicable security and operational release gates, including an isolated restore and rollback verification.
3. Tag the verified revision as `v1.0.0` and publish the GitHub release **Resumefolio MVP** from that tag. Include the delivered scope, verification summary, and known limitations.
4. Record deployment separately, including the deployed revision and smoke-check results.

## Release evidence

- Build an identifiable candidate and record its source revision, dependency versions and build verification.
- Verify environment configuration, secret handling, storage permissions, migrations and compatibility. Document the rollout and rollback procedure.
- Record applicable acceptance, security and operational results, including an isolated restore demonstration, before deployment.
- Record the rollout outcome, smoke checks, outstanding issues and any rollback in the release evidence.

Use the [release gates](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/implementation-sequence.md), [deployment topology](../04-System-Design/01-High-Level-Design/14-Appendices.md#design-record-01-software-architecture-04-deployment-topology-nodes-and-networks-md) and [operations and recovery design](../04-System-Design/01-High-Level-Design/14-Appendices.md#design-record-06-design-quality-and-security-analysis-03-operations-backup-recovery-and-resilience-md) as inputs. Carry operating procedures and known issues into [maintenance](../07-Maintenance-Evolution/01-Maintenance-Plan.md).

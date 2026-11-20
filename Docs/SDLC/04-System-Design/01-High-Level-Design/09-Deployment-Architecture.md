<a id="9-deployment-architecture"></a>

# 9. Deployment Architecture

[High-Level Design index](01-High-Level-Design.md)

### 9.1 Environments
Use isolated development and test environments. Validate deployment and recovery in a non-production rehearsal before promoting the verified candidate.

### 9.2 Infrastructure & Networking
Separate process identities, database credentials and storage paths. Restrict internal service endpoints to their intended callers. See the [deployment topology](14-Appendices.md#design-record-01-software-architecture-04-deployment-topology-nodes-and-networks-md).

### 9.3 CI/CD Overview
Build and test an identifiable revision, record the evidence, and deploy through the [runbook](../../06-Deployment-Release/02-Runbook.md). Verify migrations, smoke checks and rollback readiness on the candidate. Developer build and test automation is separate from the deferred product workflow feature.

<a id="11-non-functional-strategy"></a>

# 11. Non-Functional Strategy

[High-Level Design index](01-High-Level-Design.md)

### 11.1 Scalability
Keep ownership and resource limits explicit. Check host headroom and measure workload before changing placement or increasing limits.

### 11.2 Performance
Measure representative view and save workloads. Track bulk uploads, PDF generation and Git operations separately against their applicable bounds.

### 11.3 Availability & Reliability
Supervise workers, retain durable work records and verify coordinated backups and isolated recovery. See the [operations and recovery design](14-Appendices.md#design-record-06-design-quality-and-security-analysis-03-operations-backup-recovery-and-resilience-md).

### 11.4 Observability
Use correlation IDs, bounded structured logging, health and readiness checks, and monitoring of storage, job failures and backup freshness.

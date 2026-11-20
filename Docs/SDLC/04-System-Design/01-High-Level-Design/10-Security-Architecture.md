<a id="10-security-architecture"></a>

# 10. Security Architecture

[High-Level Design index](01-High-Level-Design.md)

### 10.1 Authentication & Authorization
Limit admission to invited users, require the selected administrator controls and resolve current actor, resource and action authority on each protected request.

### 10.2 Data Protection
Use TLS and private storage, restrict access to shared materials, keep secrets out of logs and protect backup copies with encryption and isolated restore checks.

### 10.3 Threats & Mitigations
Review cross-user exposure, revoked access, unsafe file handling, over-allocation and loss of retained artifacts. See the [threat model](14-Appendices.md#design-record-06-design-quality-and-security-analysis-02-security-threat-modeling-and-trust-boundaries-md).

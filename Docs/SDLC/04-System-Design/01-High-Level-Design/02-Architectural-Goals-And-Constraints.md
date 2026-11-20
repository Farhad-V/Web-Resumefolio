<a id="2-architectural-goals--constraints"></a>

# 2. Architectural Goals & Constraints

[High-Level Design index](01-High-Level-Design.md)

### 2.1 Business Drivers
Enable invited users to tailor professional materials, share them privately and retain what they submitted. Provide Git collaboration through a separately authorized service.

### 2.2 Key Quality Attributes
Prioritize authorization, data integrity, recoverability, accessibility and maintainability. Use the [quality design](14-Appendices.md#design-record-06-design-quality-and-security-analysis-01-quality-attributes-and-design-trade-offs-md) and requirement-linked checks for measurable targets.

### 2.3 Constraints & Assumptions
Use isolated applications, databases, credentials and private storage on the planned host. Verify host and dependency compatibility during setup. Initial colocation creates a shared host failure domain.

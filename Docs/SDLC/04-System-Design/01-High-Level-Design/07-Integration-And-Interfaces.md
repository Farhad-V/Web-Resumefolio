<a id="7-integration--interfaces"></a>

# 7. Integration & Interfaces

[High-Level Design index](01-High-Level-Design.md)

### 7.1 External Interfaces
Provide authenticated browser workspaces, protected employer views, system mail and authorized HTTPS Git operations.

### 7.2 Internal Communication
Use synchronous scoped JSON requests for Core-to-ProjectForge interactions. Use local outboxes and background jobs for durable asynchronous work. Reconcile uncertain outcomes within their owners.

### 7.3 API Overview
The [API specification](../03-Low-Level-Design/05-API-Specification.md) defines endpoint shapes, authorization, errors and retry behavior. Browser sessions and native Git credentials have separate responsibilities.

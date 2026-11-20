<a id="4-architecture-overview"></a>

# 4. Architecture Overview

[High-Level Design index](01-High-Level-Design.md)

### 4.1 Architectural Style & Rationale
Use independent Laravel applications with explicit internal module ownership. A scoped API connects Core and ProjectForge so each system retains authority over its own data and operations.

### 4.2 Design Principles
Separate mutable drafts from published and submitted records. Check current authorization at every protected entry point. Keep writes local to the owning system and make pending effects visible.

### 4.3 Container Diagram (C4 Level 2)
![C4 application containers](../Diagrams/Archived-Png/Boundaries-C4-Containers.png)

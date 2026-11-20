<a id="8-technology-stack"></a>

# 8. Technology Stack

[High-Level Design index](01-High-Level-Design.md)

### 8.1 Languages & Frameworks
Use PHP and Laravel with React and Inertia for the web applications. Retain Blade for trusted PDF templates. See the [frontend ADR](../ADR/ADR-007-React-Inertia-Frontend.md).

### 8.2 Databases & Infrastructure
Use MySQL with separate credentials and storage, Nginx and TLS on the planned Linux deployment, and native Git for ProjectForge.

### 8.3 Tools & Justification
Use Composer and Vite for repeatable builds. Use the maintained system Git engine for repository operations. Resolve compatible versions and verify both builds during [project setup](../../05-Agile-Iterative-Development/01-Project-Setup.md).

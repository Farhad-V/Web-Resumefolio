<a id="6-data-architecture"></a>

# 6. Data Architecture

[High-Level Design index](01-High-Level-Design.md)

### 6.1 Conceptual Data Model
An account owns profile content, resumes, artifacts and applications. Resumes have drafts and immutable published revisions. Applications retain immutable submission events and referenced artifacts. ProjectForge separately owns repositories, grants and issues.

### 6.2 Data Storage Strategy
Use separate MySQL databases and private storage roots. Keep binary media and native Git objects in the owning system's filesystem. Maintain hashes and authorized references in the application records. See [Database Design](../03-Low-Level-Design/04-Database-Design.md).

### 6.3 Data Flow
Users edit private source data and select revisions or files explicitly. Publication exposes only the allowed selection through protected access. Submission captures the exact materials. Cross-system requests carry only identifiers and data permitted by the scoped contract.

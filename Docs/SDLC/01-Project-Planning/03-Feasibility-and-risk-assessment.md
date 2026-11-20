# Feasibility & Risk Assessment

The proposed stack and separate application boundaries are documented. Setup, native Git integration and release safeguards still require verification on a project candidate.

## Assumptions and dependencies

- The two applications can run with isolated databases, credentials, sessions and private storage on the selected host. Validate the host and reproducible setup before relying on either environment.
- Invite and recovery flows depend on working system mail. Verify actual delivery using controlled test accounts before relying on email for access.
- ProjectForge integration depends on verifying real Git operations and the user-scoped authorization boundary. Verify these before building features that depend on that boundary.
- Private files are stored on the Resumefolio server. Verify authorization, storage limits and recovery before accepting production data.
- Personal mail and calendar providers are outside the MVP dependency chain.

## Resource constraints

Use the existing Resumefolio server for private MVP media. Keep the two applications' databases, credentials, sessions and storage boundaries isolated. Before relying on the host, verify dependency compatibility, available disk space, enforceable limits and a usable restore. Use measured operating evidence when deciding whether the existing resources are sufficient.

## Risks and verification

| Risk | Mitigation and evidence |
| --- | --- |
| Environment or storage isolation fails | Verify a clean dependency install, build, isolated migrations and basic tests for both applications. |
| Repository authority allows unauthorized access | Test supported Git operations with distinct grants and verify that expired or unauthorized access is denied. |
| Shared materials expose private data | Verify successful and denied access to selected documents, direct file URLs and revoked shares. |
| A publication or retry changes submitted history | Check that previously submitted materials remain available and unmodified after profile edits and recovery. |
| A backup cannot be restored safely | Demonstrate an isolated restore and verify data integrity and access controls before release. |

Farhad owns risk follow-up. Record the work item, evidence and residual risk for each unresolved issue. Use the [feasibility study](../02-Requirements-engineering/01-Software-requirements-specification.md#process-and-approach-02-feasibility-study) for the underlying assessment.

## Feasibility and risk tracking

- **Technical viability:** verify that the supported stack, isolated databases, private storage and standard Git clients work with the available environment.
- **Economic viability:** first test the existing host and development tools. If evidence points to additional tooling, licensing or hosting, assess the cost and obtain the owner's decision before committing.
- **Operational viability:** verify invitation delivery, permissions, logs, backups and an isolated restore. Record who owns each open issue and what evidence closes it.

| Risk | Likelihood | Impact | State |
| --- | --- | --- | --- |
| Host or storage isolation is inadequate | To assess during setup | High | Open |
| Repository or shared file access crosses its intended boundary | To assess during integration | High | Open |
| Submitted history changes during publication or retry | To assess during feature testing | High | Open |
| Backup cannot be restored with intact data and permissions | To assess in an isolated restore | High | Open |

Update likelihood and impact when evidence supports a rating. Keep the mitigation and result with the issue.


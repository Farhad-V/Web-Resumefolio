# Resources and Constraints

Status: Draft for review

## 1. Available Resources

| Resource | Current understanding | Verification status |
|---|---|---|
| Project owner | Farhad Valizadegan leads the project and development with assistant support | Confirmed working arrangement |
| Development environment | Windows and PowerShell; project located under the local XAMPP directory | Location confirmed; application runtime not yet verified |
| Version control | Git and a private GitHub repository | Commit and push workflow demonstrated |
| Diagram tools | Graphviz and PlantUML with Java | Diagram generation demonstrated |
| Hosting | Existing Hetzner server in Germany | Previously stated; specifications and current configuration not yet inspected |
| Domain | Resumefolio.de | Previously stated; current domain configuration not yet inspected |
| Reference projects | MultiResume Manager, Git Hosting Platform, OmniDesk, and KanbanFlow | Previously reviewed as references; remain unchanged |

## 2. Confirmed Constraints

- Use the existing server as the initial deployment resource.
- Work within the available budget.
- Do not assume additional servers or paid services.
- Paid AI APIs are not part of the version 1 plan.
- Use Laravel and object-oriented development.
- Support an initial deployment target of 10 users.
- Consider future growth toward approximately 1,000 users
  without claiming that the initial server supports that capacity.
- Make file limits configurable by the platform owner,
  within actual storage and processing capacity.
- Preserve existing reference projects.
- Keep credentials and private operational data out of Git.

## 3. Delivery Resources

Development proceeds through guided, reviewable steps.
There is no separately staffed delivery or operations team
assumed in this plan.

Available development hours and a target delivery date
have not yet been established. Estimates must account for
learning, implementation, verification, documentation,
and operational preparation.

## 4. Resource Details Still to Verify

- Server CPU, memory, storage, operating system, and free capacity.
- Existing workloads sharing the server.
- Available backup storage and its separation from the server.
- Hosting costs and available spending allowance.
- Network, upload, and storage limitations.
- Development runtime versions and required tools.
- Google integration access and email delivery arrangements.
- Resource requirements and isolation options for Git CI/CD.

## 5. Planning Implications

The scope is broad relative to the known delivery resources.
Effort and feasibility must be assessed before setting dates.

Technical choices must be justified against actual resources.
If a requirement cannot fit the available resources, record
the conflict and discuss options with the project owner.

Do not silently remove agreed scope or assume extra spending.
Unknown resource details remain open until verified.

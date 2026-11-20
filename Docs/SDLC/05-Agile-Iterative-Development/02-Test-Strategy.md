# Test Strategy

The [implementation sequence](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/implementation-sequence.md) defines the verification gates. The [criterion register](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/criterion-dispositions.csv) and [supplemental acceptance criteria](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/supplemental-acceptance.md) define the applicable outcomes. Record test cases alongside the feature or suite that implements them and link them to those criteria.

## Test within the iteration

Before building the slice, turn its acceptance criteria into concrete checks for the main user path and relevant denied or failure paths. Run the checks against the implemented slice and add regression checks for affected behavior. Bring the actual results to the [iteration review](Sprints/Sprint-01/02-Sprint-Review.md#iteration-review). Record further work against any failing or deferred check.

## Verification across iterations

- **Setup** Verify a clean dependency install, build, migrations and a basic automated check for each application, using isolated databases.
- **Integration** Verify the Core and ProjectForge identity boundary and real Git client behavior before dependent integration. Use distinct test accounts and verify access denial as well as success.
- **Acceptance** Exercise the invited user and employer journeys, private sharing and submitted-application history. Link successful, denied and interrupted paths to the applicable criteria.
- **Release verification** Record supported-browser, accessibility, operational and recovery checks against the release candidate. Use isolated test data and identify the environment and tested revision.

For each recorded case, include the criterion, prerequisites and test data, steps or automated test reference, and expected result. For each execution, include the tested revision, environment, observed result, evidence, and any unresolved failure. Record unexecuted cases as pending.

**Execution status** Product tests have yet to run. See [implementation progress](Sprints/Sprint-01/02-Sprint-Review.md) for package-level evidence.

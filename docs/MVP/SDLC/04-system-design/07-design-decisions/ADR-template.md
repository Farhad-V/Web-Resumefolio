# Architecture Decision Record Template

## Current implementation baseline — November 4, 2026

[BL-MVP-2026-11-04.1](../../../baseline/README.md) selects the MVP technical mechanisms, numerical policies, priorities and requirement/criterion dispositions under Farhad’s explicit delegation. It supersedes earlier Proposed/pending mechanism and whole-baseline statements below for MVP design input. Future clauses and dated evidence remain separate. Runtime/actor validation, credentials, Git isolation, capacity and backup/restore still require the named implementation/Release gates; this update reports no product test Pass.

### Prior source material and rationale (superseded where this Baseline selects a different MVP choice)

**Purpose:** provide a reusable structure for one consequential technical decision and its actual status, rationale, evidence and evolution.

**Template status:** guidance only, updated November 2, 2026. No ADR identifier, technical selection, reviewer, acceptance or product result is allocated by this file. Square-bracket fields below are placeholders; replace them with actual information or an explicit unresolved condition.

## How to use

1. Create a concrete record only when there is an identifiable technical decision. Allocate the next unused sequential identifier after checking the [decision index](README.md); use `ADR-[number]-[descriptive-title].md` and add its actual status to the index.
2. Copy the record structure below and replace placeholders. Scale detail to the decision; mark genuinely inapplicable topics with a reason rather than inventing material.
3. Preserve source acceptance. An accepted product rule can require a still-proposed technical realization; a technical ADR cannot silently change that rule.
4. Compare relevant options using the same criteria and identified evidence. Proposed benefits and estimates are not measured results.
5. Record owner/reviewer disposition only when actually made. Preserve original rationale and link later corrections or superseding decisions.

Keep diagrams at their owning architecture/component/data location and link them when sufficient. Create a new diagram only when it explains a material decision boundary. Keep planned verification in the record and link actual sanitized results through [evidence guidance](../06-design-quality-and-security-analysis/review-and-traceability/evidence/README.md).

---

# ADR-[number] — [Concrete Technical Decision Title]

| Item | Actual record value |
| --- | --- |
| Status | [Proposed / Accepted / Rejected / Superseded; actual scope and conditions] |
| Prepared / updated | [Actual dates; preserve decision history] |
| Author / decision authority | [Actual author and authorized decision-maker] |
| Candidate | [Exact source/design/code/configuration revisions or hashes being considered] |
| Decision scope | [What this choice determines and which commitments it affects] |
| Evidence boundary | [Actual inspected/tested scope and important unverified claims] |

## 1. Context and source authority

[State the concrete problem, trigger and why a decision is needed. Identify relevant source criteria/scenarios, analysis elements, drivers, constraints and prior decisions with exact links/revisions. Distinguish accepted behavior from proposals and unresolved policy.]

[Describe actual consumers, operating context, authority/trust boundaries, resource/cost/capacity constraints and deadline/trigger if one exists. State assumptions and missing evidence without turning them into facts. Do not reopen a settled source answer solely to approve this ADR.]

## 2. Options and decision criteria

[List the criteria used to compare relevant alternatives: behavior/integrity, compatibility, quality, security/privacy, implementation/operating cost, migration and recovery where applicable. Identify which criteria are mandatory and their actual source status.]

### Option A — [Name]

[Mechanism, fit to criteria, benefits, disadvantages, assumptions and evidence.]

### Option B — [Name]

[Comparable explanation; add other viable options when material. Include retaining the current approach only if it is a real option.]

[Identify the strongest objection to the preferred option and evidence that would change the recommendation. Avoid invented numerical scores, unsupported prices or false compatibility claims.]

## 3. Proposed or accepted decision and rationale

[State the exact proposed choice, or the actual accepted choice with its disposition reference. Explain why it fits the criteria better in this context.]

[Specify affected owners, contracts, data identities, consistency/transaction boundaries, runtime/artifacts, deployment and operating obligations as applicable. Explain what is genuinely selected and what remains a prerequisite. Link owning details rather than duplicate them.]

[Preserve applicable current authority, independent publication/history, protected references and truthful external outcomes. Do not imply remote atomicity, safe retry, rollback or execution isolation merely from a pattern name.]

## 4. Consequences, risks and unresolved mechanisms

[Record expected benefits separately from actual measurements. Describe costs, adverse effects, trade-offs, residual uncertainty and mitigation owners. Classify actual debt/findings using the evolution procedure rather than labeling every open decision as debt.]

[Document compatibility/migration and recovery limits, including old clients/workers/pending payloads and irreversible state/effects where relevant. State remaining technology/policy/resource/evidence decisions and the exact commitment each blocks.]

## 5. Verification and disposition

[Define scenario/criterion-specific acceptance checks, candidate/environment/fixtures, current actor/grants, relevant versions, expected effects and unchanged protected state. Cover applicable denied, concurrent, uncertain and recovery paths.]

[Separate planned checks from executed observations. Link actual method/results/limitations when available; explain what mocks or documentation checks cannot establish.]

[Record actual reviewer, date, identified candidate, finding/evidence references, decision authority and scoped disposition only when performed. Until then say “Owner disposition pending” or the precise unresolved status. Do not infer whole-phase acceptance, implementation authorization, spending approval or release readiness.]

## 6. Revisit and evolution

[Identify concrete events/measurements that would justify reconsideration. Describe compatibility and migration obligations if the choice changes.]

[Link preceding/superseding records where they actually exist. Retain historical rationale and status/disposition provenance; do not silently rewrite an accepted decision into a different one.]

[Decision index](README.md) · [Review/handoff](../06-design-quality-and-security-analysis/05-design-review-traceability-and-handoff.md)

---

## Authoring checks

- The record addresses one identifiable choice with exact source/candidate scope.
- Alternatives are comparable, rationale is concrete and unverified assumptions remain visible.
- Product-source acceptance and technical decision status are distinguished.
- Consequences include relevant authority, consistency, compatibility, operating and recovery limits.
- Planned verification and actual evidence/disposition are separate.
- Links resolve and no placeholders remain except deliberately unresolved fields with owners/gates.
- No credentials/private operational data, fabricated reviewer/result or unapproved purchase is recorded.

These checks help author a reviewable record; completing them is not acceptance. Use [design evolution](../02-detailed-and-object-oriented-design/05-design-evolution-refactoring-and-technical-debt.md) and the [review procedure](../06-design-quality-and-security-analysis/05-design-review-traceability-and-handoff.md) for subsequent changes and disposition.

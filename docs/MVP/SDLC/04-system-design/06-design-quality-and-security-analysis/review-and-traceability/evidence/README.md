# Resumefolio — Design Review Evidence

**Purpose:** store actual, attributable design inspections, option evaluations, findings and measured verification results for identified candidates.

Owner: Farhad. Updated November 2, 2026.

**Current position:** this directory contains this guidance README only. No review report, product-test result, benchmark, security assessment or restoration evidence is added by this update. Documentation checks reported elsewhere retain their original scope and location.

[Evidence types](#1-what-belongs-here) · [Required metadata](#2-required-evidence-record) · [Organization](#3-naming-and-package-organization) · [Handling](#4-sensitive-information-and-history) · [Review use](#5-using-evidence-in-review-and-handoff)

## 1. What belongs here

| Evidence type | What it can establish within its stated limits |
| --- | --- |
| Documentary inspection | Exact source/design comparison, cross-view finding or option assessment for the inspected revision |
| Compatibility investigation | Actual facility/version/client/configuration observations and bounded interoperability results |
| Executed verification | Actual component/integration/system outcome for identified code, environment, data and method |
| Quality/accessibility evaluation | Actual workload/task/criterion observations with measurement boundaries and limitations |
| Security/operating/recovery assessment | Authorized observed control behavior, consistent capture or usable restoration within the tested scope |
| Review/disposition record | Who reviewed or decided what, against which candidate, with actual conditions and remaining gaps |

Keep planned checks in the [owning design documents](../../README.md) and [review procedure](../../05-design-review-traceability-and-handoff.md). A prepared template or proposed result is not execution evidence. Imported historical results must preserve their original date, candidate, method and scope; do not label them as newly performed.

## 2. Required evidence record

Every actual record needs:

- **Identity:** descriptive local reference/title, evidence type, actual observation date/time and reviewer/operator or tool identity; do not invent independent review.
- **Candidate:** exact source/design/code revisions or hashes, relevant ADR status and configuration/facility versions. A filename or mutable branch alone is insufficient provenance.
- **Scope and trace:** exact requirement/criterion locator, analysis/design element, scenario/threat/operation and the question being evaluated.
- **Method and authority:** inspection/test/measurement procedure, authorized target/effects, environment, controlled fixtures, actor/grants and relevant versions or workload.
- **Expected versus observed:** actual outcomes, protected state, sanitized supporting output, measurement boundaries/denominators and anomalous or unknown effects.
- **Assessment:** specific finding, limitations, missing prerequisites, affected commitment, responsible owner and actual disposition if made.
- **Reproduction and relationships:** safe prerequisites/steps, links to supporting artifacts and earlier/superseding records; keep secrets out of instructions.

Not-applicable fields need a short rationale. For documentary inspection, identify inspected files/sections and exact comparison scope rather than inventing a runtime environment. For timed evidence, record the time zone/offset and actual start/end events. For quality/recovery objectives, identify whether the target is proposed or accepted before comparing results.

## 3. Naming and package organization

Choose a descriptive filename such as `YYYY-MM-DD-<subject>-<evidence-type>.md` using the actual observation date. Add a suffix or directory when multiple distinct runs exist; do not overwrite an earlier run to make it appear current. These are naming examples, not existing evidence files or allocated global IDs.

Use Markdown for readable method/findings, JSON/CSV for structured metadata or measured observations, and supporting screenshots/log excerpts only where they add actual evidence. A larger assessment can use a dated subject directory with an index linking its manifest, observations, findings and sanitized supporting files. Create that structure only when actual evidence exists; no empty Pass reports are required.

Hashes identify the bytes captured, not their semantic correctness, trusted origin or owner approval. Do not regenerate historical hashes against later files and retain the old review date. If evidence moves or is redacted, document the change and preserve appropriate original provenance in restricted storage where necessary.

## 4. Sensitive information and history

Use synthetic identities/content and controlled fixtures whenever possible. Exclude passwords, tokens, raw session/link/reset values, private keys, private correspondence and unnecessary personal/operational data. Check screenshots, URLs, headers, command output and attachments before repository inclusion. Redacted output must remain understandable and explicitly labeled as such.

When the actual underlying artifact cannot be stored safely here, record a sanitized summary and a permitted restricted-storage reference with access responsibility and limitations. Do not copy sensitive artifacts into Git for convenience. This guide sets no new retention period, legal policy, storage service or access privilege.

Preserve original records and their limitations. A later result can supersede an earlier conclusion for a new candidate, but does not turn the earlier observation into a different event. Add actual correction/supersession provenance rather than silently changing a historical Failed/Unknown into Pass. Distinguish inconclusive, blocked, not run and observed failure in plain language; none implies success.

## 5. Using evidence in review and handoff

Link evidence from the exact trace/finding record in [Design Review, Traceability and Implementation Handoff](../../05-design-review-traceability-and-handoff.md). Keep source identity aligned with the [requirements traceability authority](../../../../02-requirements-engineering/06-validation-and-traceability/requirements-traceability.md) and preserve the limits of the [analysis review](../../../../03-system-analysis/07-review-and-design-handoff/11-model-consistency-traceability-and-review.md).

Before relying on a record, check that its candidate/environment/method covers the present claim, protected state and relevant failure/concurrency/recovery paths. An old result may inform a change without verifying it. A mock success cannot prove provider delivery, native transfer, isolation or usable restoration. Rendering diagrams and resolving links verify documentation only.

Actual owner disposition, design acceptance, implementation readiness and product release remain separate claims requiring their own identified authority and evidence. Do not infer any of them from a nonempty folder, a manifest, a completed template or a collection of successful file checks.

[Quality and Security home](../../README.md) · [Review and handoff](../../05-design-review-traceability-and-handoff.md) · [System Design home](../../../README.md)

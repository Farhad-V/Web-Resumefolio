# SA-RV03 — selected exact-criterion comparisons

Thirty-nine current documentary comparisons. No entry is a full semantic-coverage or product-test Pass. Original criterion wording is preserved verbatim.

<a id="acc-d03-ac01"></a>
## ACC-D03-AC01

**Exact criterion:** Given an actor with read permission but no modification permission in the agreed matrix, a direct modification request does not change the protected resource.

**Current model locations:** [13-security-quality-and-operational-analysis.md#sq-a04](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-a04), [13-security-quality-and-operational-analysis.md#sq-t01](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-t01), [12-interfaces-and-external-interactions.md#if-01](../06-interfaces-security-and-quality-analysis/12-interfaces-and-external-interactions.md#if-01)

**Documentary finding:** Read authority is explicitly distinct from mutation authority.

**Residual:** A complete actor/action/state matrix and concrete read-only actor mutation cases remain unaccepted.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="acc-d03-ac02"></a>
## ACC-D03-AC02

**Exact criterion:** Given no permission to a private resource, direct read/list/download requests do not disclose its protected content.

**Current model locations:** [13-security-quality-and-operational-analysis.md#sq-a04](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-a04), [13-security-quality-and-operational-analysis.md#sq-t01](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-t01), [12-interfaces-and-external-interactions.md#if-01](../06-interfaces-security-and-quality-analysis/12-interfaces-and-external-interactions.md#if-01)

**Documentary finding:** Direct access and private-content non-disclosure are modeled at the resource boundary.

**Residual:** Confirm concrete read/list/download response and metadata cases for each protected subject.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="acc-d03-ac03"></a>
## ACC-D03-AC03

**Exact criterion:** Hiding a control or changing a request's resource identifier does not substitute for authorization of the requested operation.

**Current model locations:** [13-security-quality-and-operational-analysis.md#sq-a04](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-a04), [13-security-quality-and-operational-analysis.md#sq-t01](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-t01), [12-interfaces-and-external-interactions.md#if-01](../06-interfaces-security-and-quality-analysis/12-interfaces-and-external-interactions.md#if-01)

**Documentary finding:** Identifier substitution and hidden controls are explicitly not authorization.

**Residual:** Complete entry-point-specific negative cases and later enforcement evidence.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="acc-d04-ac01"></a>
## ACC-D04-AC01

**Exact criterion:** Given A and B with separate private resumes/email/application records and no grant between them, A cannot retrieve or modify B's protected content through direct requests.

**Current model locations:** [13-security-quality-and-operational-analysis.md#sq-a04](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-a04), [13-security-quality-and-operational-analysis.md#sq-a05](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-a05), [13-security-quality-and-operational-analysis.md#sq-t01](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-t01)

**Documentary finding:** Cross-user private resume, email and application access is explicitly prohibited without a relevant grant.

**Residual:** Exact grant matrix and per-resource direct read/write cases remain.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="acc-d04-ac02"></a>
## ACC-D04-AC02

**Exact criterion:** List/search/navigation in A's private context does not expose B's protected content merely because B's identifiers are supplied or guessed.

**Current model locations:** [13-security-quality-and-operational-analysis.md#sq-a04](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-a04), [13-security-quality-and-operational-analysis.md#sq-a05](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-a05), [13-security-quality-and-operational-analysis.md#sq-t01](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-t01)

**Documentary finding:** List/search/navigation are included in the protected-scope analysis.

**Residual:** Concrete filtered result, count and error-disclosure cases require review.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="acc-d04-ac03"></a>
## ACC-D04-AC03

**Exact criterion:** A legitimate collaboration or employer-sharing grant exposes only its defined scope, not unrelated resources.

**Current model locations:** [13-security-quality-and-operational-analysis.md#sq-a04](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-a04), [13-security-quality-and-operational-analysis.md#sq-a05](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-a05), [13-security-quality-and-operational-analysis.md#sq-t01](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-t01)

**Documentary finding:** Employer/collaboration scope is explicitly limited and does not grant unrelated private access.

**Residual:** Confirm all grant/action combinations and changed-grant effects.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="afo-d04-ac01"></a>
## AFO-D04-AC01

**Exact criterion:** An admission that exceeds the available allowance under the agreed accounting rule is not reported as successful usable content.

**Current model locations:** [10-domain-constraints-and-operation-contracts.md#dc-o32](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o32), [13-security-quality-and-operational-analysis.md#sq-t07](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-t07)

**Documentary finding:** Admission and usable completion are separate; effective limits constrain eligibility.

**Residual:** Accounting units, included subjects and actual quota values remain proposed.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="afo-d04-ac02"></a>
## AFO-D04-AC02

**Exact criterion:** Concurrent controlled requests that individually appear to fit but jointly exceed that allowance cannot all succeed in violation of the defined quota.

**Current model locations:** [10-domain-constraints-and-operation-contracts.md#dc-o32](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o32), [13-security-quality-and-operational-analysis.md#sq-t07](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-t07)

**Documentary finding:** Stale capacity/reference state and concurrent admissions are identified explicitly.

**Residual:** The detailed competing-request interleaving and chosen atomic admission mechanism are not yet established.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="afo-d04-ac03"></a>
## AFO-D04-AC03

**Exact criterion:** Accounted usage after successful/failed operations matches the agreed inclusion and release rules; failed work is not silently counted as permanent successful content.

**Current model locations:** [10-domain-constraints-and-operation-contracts.md#dc-o32](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o32), [13-security-quality-and-operational-analysis.md#sq-t07](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-t07)

**Documentary finding:** Failure does not justify reporting usable content or releasing retained references.

**Residual:** Exact temporary/failed/retained usage inclusion and release rules remain required.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="afo-d07-ac01"></a>
## AFO-D07-AC01

**Exact criterion:** Interrupted upload or required processing failure does not leave the file presented as complete usable content.

**Current model locations:** [10-domain-constraints-and-operation-contracts.md#dc-o32](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o32), [10-domain-constraints-and-operation-contracts.md#dc-o38](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o38), [13-security-quality-and-operational-analysis.md#sq-t07](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-t07)

**Documentary finding:** Interrupted upload or processing is not usable-file success.

**Residual:** Later controlled interruption/processing-failure evidence remains unperformed.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="afo-d07-ac02"></a>
## AFO-D07-AC02

**Exact criterion:** A completed operation exposes only the content/result associated with its successful request and allowed resource context.

**Current model locations:** [10-domain-constraints-and-operation-contracts.md#dc-o32](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o32), [10-domain-constraints-and-operation-contracts.md#dc-o38](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o38), [13-security-quality-and-operational-analysis.md#sq-t07](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-t07)

**Documentary finding:** The successful file result is bound to intended resource/association and current authority.

**Residual:** Check exact request-to-result identity for all upload/replacement paths.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="afo-d07-ac03"></a>
## AFO-D07-AC03

**Exact criterion:** Failure handling does not silently damage unrelated existing content or release quota still needed by retained material.

**Current model locations:** [10-domain-constraints-and-operation-contracts.md#dc-o32](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o32), [10-domain-constraints-and-operation-contracts.md#dc-o38](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o38), [13-security-quality-and-operational-analysis.md#sq-t07](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-t07)

**Documentary finding:** Replacement and cleanup preserve unrelated content and protected references.

**Residual:** Detailed failed-replacement/accounting interleavings and applicable policies remain.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="dom-d06-ac01"></a>
## DOM-D06-AC01

**Exact criterion:** The assessment identifies data categories, purpose, access recipients, provider/hosting flows, retention/deletion questions and backup implications.

**Current model locations:** [13-security-quality-and-operational-analysis.md#information-handling-applicability-status](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#information-handling-applicability-status)

**Documentary finding:** The security view now identifies intended data categories, purposes, recipient boundaries and provider/hosting/backup questions in an explicit assessment entry point.

**Residual:** Verify actual operating flows and retention/deletion/backup disposition before accepting affected operating requirements.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="dom-d06-ac02"></a>
## DOM-D06-AC02

**Exact criterion:** Each asserted external obligation identifies an authoritative source, date, applicability rationale and affected requirement.

**Current model locations:** [13-security-quality-and-operational-analysis.md#information-handling-applicability-status](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#information-handling-applicability-status)

**Documentary finding:** The assessment requires source/date/applicability/affected-requirement evidence for each asserted external obligation; none is asserted without it.

**Residual:** Actual authoritative external-obligation research has not been performed by this documentary update.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="dom-d06-ac03"></a>
## DOM-D06-AC03

**Exact criterion:** Unknown controller/processor, user-location, contractual or legal questions remain explicit rather than becoming an unsupported compliance statement.

**Current model locations:** [13-security-quality-and-operational-analysis.md#information-handling-applicability-status](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#information-handling-applicability-status)

**Documentary finding:** Controller/processor, user-location, contractual and legal questions remain explicit rather than inferred from hosting location.

**Residual:** Resolve actual roles and applicable arrangements through scoped investigation; no compliance conclusion is made.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="git-d03-ac01"></a>
## GIT-D03-AC01

**Exact criterion:** Later supported-client checks retrieve the expected repository content and history through real Clone/Fetch operations.

**Current model locations:** [12-interfaces-and-external-interactions.md#if-06](../06-interfaces-security-and-quality-analysis/12-interfaces-and-external-interactions.md#if-06), [10-domain-constraints-and-operation-contracts.md#dc-o22](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o22), [10-domain-constraints-and-operation-contracts.md#dc-o23](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o23)

**Documentary finding:** Real authorized content/history transfer is required rather than browser simulation.

**Residual:** Supported client/transport choices and interoperability evidence remain.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="git-d03-ac02"></a>
## GIT-D03-AC02

**Exact criterion:** Client Pull integrates fetched data according to the reviewed supported-client scenarios; client conflicts are not mislabeled server success.

**Current model locations:** [12-interfaces-and-external-interactions.md#if-06](../06-interfaces-security-and-quality-analysis/12-interfaces-and-external-interactions.md#if-06), [10-domain-constraints-and-operation-contracts.md#dc-o22](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o22), [10-domain-constraints-and-operation-contracts.md#dc-o23](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o23)

**Documentary finding:** Client Pull integration and server transfer/result meaning remain distinguishable in IF-06.

**Residual:** Specific supported-client integration/conflict scenarios are not fully modeled or executed.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="git-d03-ac03"></a>
## GIT-D03-AC03

**Exact criterion:** Authorized Push updates the intended allowed refs; denied/rejected/interrupted operations expose truthful outcomes under defined integrity rules.

**Current model locations:** [12-interfaces-and-external-interactions.md#if-06](../06-interfaces-security-and-quality-analysis/12-interfaces-and-external-interactions.md#if-06), [10-domain-constraints-and-operation-contracts.md#dc-o22](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o22), [10-domain-constraints-and-operation-contracts.md#dc-o23](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o23)

**Documentary finding:** Push success requires attributable intended ref effect; denial/conflict/unknown are distinct.

**Residual:** Exact ref protection and interrupted multi-ref behavior require scoped design and cases.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="pdf-d03-ac01"></a>
## PDF-D03-AC01

**Exact criterion:** Generated-only, uploaded-only, both and neither cases expose only the permitted available variants.

**Current model locations:** [10-domain-constraints-and-operation-contracts.md#dc-o04](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o04), [10-domain-constraints-and-operation-contracts.md#dc-o06](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o06), [09-rule-based-view.md#rb-d03](../05-business-rules-and-operation-contracts/09-rule-based-view.md#rb-d03), [09-rule-based-view.md#rb-d04](../05-business-rules-and-operation-contracts/09-rule-based-view.md#rb-d04)

**Documentary finding:** Mode eligibility and actual generated/uploaded availability are separate rule conditions.

**Residual:** Confirm concrete mode/availability combinations and their selected response behavior.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="pdf-d03-ac02"></a>
## PDF-D03-AC02

**Exact criterion:** English/German uploaded availability is respected without silently substituting a disabled/unavailable language.

**Current model locations:** [10-domain-constraints-and-operation-contracts.md#dc-o04](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o04), [10-domain-constraints-and-operation-contracts.md#dc-o06](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o06), [09-rule-based-view.md#rb-d03](../05-business-rules-and-operation-contracts/09-rule-based-view.md#rb-d03), [09-rule-based-view.md#rb-d04](../05-business-rules-and-operation-contracts/09-rule-based-view.md#rb-d04)

**Documentary finding:** Requested language/representation must be eligible and available; unrelated fallback is not permitted.

**Residual:** Review missing English/German rendition cases and actual generation/upload evidence.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="pdf-d03-ac03"></a>
## PDF-D03-AC03

**Exact criterion:** Changes for one resume do not silently alter another resume or bypass retrieval authorization.

**Current model locations:** [10-domain-constraints-and-operation-contracts.md#dc-o04](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o04), [10-domain-constraints-and-operation-contracts.md#dc-o06](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o06), [09-rule-based-view.md#rb-d03](../05-business-rules-and-operation-contracts/09-rule-based-view.md#rb-d03), [09-rule-based-view.md#rb-d04](../05-business-rules-and-operation-contracts/09-rule-based-view.md#rb-d04)

**Documentary finding:** Configuration is scoped to the intended resume and does not bypass retrieval authority.

**Residual:** Check simultaneous edits and cross-resume direct request cases.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="pdf-d06-ac01"></a>
## PDF-D06-AC01

**Exact criterion:** An unrelated actor cannot change another owner's password/link state through direct requests.

**Current model locations:** [10-domain-constraints-and-operation-contracts.md#dc-o05](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o05), [10-domain-constraints-and-operation-contracts.md#dc-o06](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o06), [13-security-quality-and-operational-analysis.md#sq-t02](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-t02)

**Documentary finding:** Changing a specific link requires current owner/resource authority.

**Residual:** Password-rotation operation details and unrelated actor attempts need a dedicated complete path.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="pdf-d06-ac02"></a>
## PDF-D06-AC02

**Exact criterion:** After disabling, a fresh viewer context cannot obtain protected content through the link.

**Current model locations:** [10-domain-constraints-and-operation-contracts.md#dc-o05](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o05), [10-domain-constraints-and-operation-contracts.md#dc-o06](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o06), [13-security-quality-and-operational-analysis.md#sq-t02](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-t02)

**Documentary finding:** Confirmed effective link disablement denies fresh protected access.

**Residual:** Concrete effective-change timing and fresh retrieval tests remain unperformed.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="pdf-d06-ac03"></a>
## PDF-D06-AC03

**Exact criterion:** After a password change, the old password does not newly authorize a fresh viewer; the current password works only for an eligible link.

**Current model locations:** [10-domain-constraints-and-operation-contracts.md#dc-o05](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o05), [10-domain-constraints-and-operation-contracts.md#dc-o06](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o06), [13-security-quality-and-operational-analysis.md#sq-t02](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-t02)

**Documentary finding:** SQ-T02 identifies password/grant change and separates fresh from already-open requests.

**Residual:** Gap: no dedicated password-rotation contract fully specifies fresh old/current password behavior; in-flight/session policy also remains open.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="prp-d04-ac01"></a>
## PRP-D04-AC01

**Exact criterion:** Editing shared profile information does not automatically change an existing resume draft or published view; the owner previews the changes, explicitly applies selected source changes without overwriting resume-specific overrides, and separately confirms publication.

**Current model locations:** [04-function-oriented-view.md#4-process-and-data-flow-models](../03-functional-and-process-analysis/04-function-oriented-view.md#4-process-and-data-flow-models), [10-domain-constraints-and-operation-contracts.md#dc-o01](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o01), [10-domain-constraints-and-operation-contracts.md#dc-o02](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o02), [10-domain-constraints-and-operation-contracts.md#dc-o03](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o03)

**Documentary finding:** F02.1/2/3 and DC-O01/02/03 distinguish source edit, selected apply and separately confirmed publication.

**Residual:** Accepted core is preserved; detailed stale-context/source-removal policy and execution evidence remain.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="prp-d04-ac02"></a>
## PRP-D04-AC02

**Exact criterion:** An overridden field retains its independent meaning under the reviewed precedence rules rather than being silently replaced by the source change.

**Current model locations:** [04-function-oriented-view.md#4-process-and-data-flow-models](../03-functional-and-process-analysis/04-function-oriented-view.md#4-process-and-data-flow-models), [10-domain-constraints-and-operation-contracts.md#dc-o01](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o01), [10-domain-constraints-and-operation-contracts.md#dc-o02](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o02), [10-domain-constraints-and-operation-contracts.md#dc-o03](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o03)

**Documentary finding:** DC-O02 explicitly preserves independent overrides under selected apply.

**Residual:** Exact field precedence/conflict rules beyond accepted preservation must be reviewed.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="prp-d04-ac03"></a>
## PRP-D04-AC03

**Exact criterion:** Omitted content is not silently added to a resume, and source updates do not overwrite preserved actual submitted copies.

**Current model locations:** [04-function-oriented-view.md#4-process-and-data-flow-models](../03-functional-and-process-analysis/04-function-oriented-view.md#4-process-and-data-flow-models), [10-domain-constraints-and-operation-contracts.md#dc-o01](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o01), [10-domain-constraints-and-operation-contracts.md#dc-o02](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o02), [10-domain-constraints-and-operation-contracts.md#dc-o03](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o03)

**Documentary finding:** Source-only edits cannot add omitted resume content or rewrite actual submitted history.

**Residual:** Review intentional re-inclusion and category-specific correction/retention exceptions separately.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="qsr-d10-ac01"></a>
## QSR-D10-AC01

**Exact criterion:** The coverage record includes or explicitly disposes of each subject in section 4 with dependencies and known exclusions.

**Current model locations:** [13-security-quality-and-operational-analysis.md#sq-q10](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-q10), [13-security-quality-and-operational-analysis.md#4-recovery-and-operation](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#4-recovery-and-operation)

**Documentary finding:** The recovery catalog identifies nine dependent subjects and requires include/reconstruct/exclude disposition.

**Residual:** Concrete per-subject backup coverage choices/exclusions and actual consistent source remain unestablished.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="qsr-d10-ac02"></a>
## QSR-D10-AC02

**Exact criterion:** Later backup evidence identifies candidate/environment, included recovery point/material, actual outcome and access without exposing secrets.

**Current model locations:** [13-security-quality-and-operational-analysis.md#sq-q10](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-q10), [13-security-quality-and-operational-analysis.md#4-recovery-and-operation](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#4-recovery-and-operation)

**Documentary finding:** Backup scenario defines candidate/environment/material/outcome/access evidence without secrets.

**Residual:** Backups are not configured; no successful creation evidence exists in this analysis.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="qsr-d10-ac03"></a>
## QSR-D10-AC03

**Exact criterion:** Missed/failed/incomplete backup work is distinguishable from successful covered backup creation under the reviewed operational policy.

**Current model locations:** [13-security-quality-and-operational-analysis.md#sq-q10](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-q10), [13-security-quality-and-operational-analysis.md#4-recovery-and-operation](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#4-recovery-and-operation)

**Documentary finding:** Failure/incomplete observations must not be reported as successful covered backup.

**Residual:** Actual schedule, failure detection and reporting procedures remain to be chosen and demonstrated.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="qsr-d11-ac01"></a>
## QSR-D11-AC01

**Exact criterion:** Before target acceptance, each scenario defines loss event, chosen recovery point, tolerable data loss, timing start/end boundaries and usable-state criteria.

**Current model locations:** [13-security-quality-and-operational-analysis.md#sq-q11](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-q11), [13-security-quality-and-operational-analysis.md#availability-disaster-recovery-and-failover-views](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#availability-disaster-recovery-and-failover-views), [10-domain-constraints-and-operation-contracts.md#dc-o37](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o37)

**Documentary finding:** DR view requires loss event, recovery point, timing and usable-state definitions.

**Residual:** RPO/RTO values and scenario-specific tolerable loss remain undecided.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="qsr-d11-ac02"></a>
## QSR-D11-AC02

**Exact criterion:** Later restoration verifies required records/artifacts/references and actual core workflow outcomes, not only extraction or process startup.

**Current model locations:** [13-security-quality-and-operational-analysis.md#sq-q11](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-q11), [13-security-quality-and-operational-analysis.md#availability-disaster-recovery-and-failover-views](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#availability-disaster-recovery-and-failover-views), [10-domain-constraints-and-operation-contracts.md#dc-o37](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o37)

**Documentary finding:** Restore must validate records/artifacts/references, current access and critical workflows.

**Residual:** Actual protected source, isolated drill and workflow restoration evidence remain absent.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="qsr-d11-ac03"></a>
## QSR-D11-AC03

**Exact criterion:** Measured loss/time and incomplete coverage are compared with the agreed RPO/RTO and limitations; unavailable evidence is not labeled Pass.

**Current model locations:** [13-security-quality-and-operational-analysis.md#sq-q11](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-q11), [13-security-quality-and-operational-analysis.md#availability-disaster-recovery-and-failover-views](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#availability-disaster-recovery-and-failover-views), [10-domain-constraints-and-operation-contracts.md#dc-o37](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o37)

**Documentary finding:** Measured loss/time must be compared with agreed objectives; absent evidence is not Pass.

**Residual:** No measured drill or agreed numerical objectives exist; diagram generation supplies neither.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="qsr-d12-ac01"></a>
## QSR-D12-AC01

**Exact criterion:** Restored sharing links/password contexts, memberships and credentials follow the agreed treatment of later revocation rather than being blindly reactivated.

**Current model locations:** [13-security-quality-and-operational-analysis.md#sq-q12](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-q12), [13-security-quality-and-operational-analysis.md#sq-t10](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-t10), [10-domain-constraints-and-operation-contracts.md#dc-o37](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o37)

**Documentary finding:** Restored grants and credentials require current-authority review, not blind resurrection.

**Residual:** The treatment of revocations after a recovery point needs explicit per-category policy and cases.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="qsr-d12-ac02"></a>
## QSR-D12-AC02

**Exact criterion:** Provider/Git/run mappings and pending send/deployment/reminder work are reconciled under defined authority/outcome rules before automatic continuation, if any.

**Current model locations:** [13-security-quality-and-operational-analysis.md#sq-q12](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-q12), [13-security-quality-and-operational-analysis.md#sq-t10](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-t10), [10-domain-constraints-and-operation-contracts.md#dc-o37](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o37)

**Documentary finding:** DR sequence reconciles pending external effects and prohibits automatic replay by assumption.

**Residual:** Provider/Git/run/deployment reconciliation procedures and attributable evidence remain required.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="qsr-d12-ac03"></a>
## QSR-D12-AC03

**Exact criterion:** Known deleted-data reappearance or missing newer external changes is handled and disclosed as the reviewed recovery limitation, not silently accepted as current truth.

**Current model locations:** [13-security-quality-and-operational-analysis.md#sq-q12](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-q12), [13-security-quality-and-operational-analysis.md#sq-t10](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-t10), [10-domain-constraints-and-operation-contracts.md#dc-o37](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o37)

**Documentary finding:** Recovered state must disclose missing/newer external information and deleted-data reappearance limits.

**Residual:** Concrete deletion/retention and external-change reconciliation decisions remain open.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="yml-d04-ac01"></a>
## YML-D04-AC01

**Exact criterion:** Later controlled attempts cannot access unrelated private repository/user/host data beyond permitted inputs.

**Current model locations:** [13-security-quality-and-operational-analysis.md#sq-t04](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-t04), [13-security-quality-and-operational-analysis.md#sq-q07](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-q07), [10-domain-constraints-and-operation-contracts.md#dc-o27](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o27)

**Documentary finding:** Unrelated host/user/repository data is outside permitted execution inputs.

**Residual:** A suitable isolated execution environment and controlled access tests are not established.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="yml-d04-ac02"></a>
## YML-D04-AC02

**Exact criterion:** Allowed execution cannot gain administrative/host authority merely through crafted code or definition inputs.

**Current model locations:** [13-security-quality-and-operational-analysis.md#sq-t04](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-t04), [13-security-quality-and-operational-analysis.md#sq-q07](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-q07), [10-domain-constraints-and-operation-contracts.md#dc-o27](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o27)

**Documentary finding:** Crafted code/definitions must not confer host or administrator powers.

**Residual:** Isolation/credential/network design and actual escape-resistance evidence remain at the enabling gate.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.

<a id="yml-d04-ac03"></a>
## YML-D04-AC03

**Exact criterion:** Isolation failure or inability to establish required controls blocks enabling the affected execution capability.

**Current model locations:** [13-security-quality-and-operational-analysis.md#sq-t04](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-t04), [13-security-quality-and-operational-analysis.md#sq-q07](../06-interfaces-security-and-quality-analysis/13-security-quality-and-operational-analysis.md#sq-q07), [10-domain-constraints-and-operation-contracts.md#dc-o27](../05-business-rules-and-operation-contracts/10-domain-constraints-and-operation-contracts.md#dc-o27)

**Documentary finding:** Missing required controls prevents enabling affected execution.

**Residual:** Record the eventual enabling evidence and disposition; none is supplied by diagram generation.

**Disposition:** Bounded documentary comparison; not product-tested or fully closed.


<a id="data-definitions-data-definitions"></a>

<a id="data-definitions-data-definitions--heading-resumefolio--data-definitions-guide"></a>
# Resumefolio — Data Definitions Guide

**Scope and status:** Interpret this supporting view using the [current record rules](../03-Requirements-Specification/15-Requirement-Priority-And-Readiness.md#current-record-rules). Original open fields do not override selected policies. Personal Google integration, advanced Sprint/review features and YAML execution remain after MVP; only the selected criteria apply to current work.

Current implementation choices and scope: [Baseline](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/README.md). Runtime verification remains subject to its gates.

| Item | Current position |
| --- | --- |
| Purpose | Coordinate terminology, conceptual information meaning, authority and lifecycle questions |
| Owner | Farhad; sole delivery and operations owner |
| Status | Proposed definitions — detailed constraints, policy and owner acceptance pending |
| Inventory | Two primary documents; 34 conceptual subject groups, 24 proposed semantic elements and four diagrams |
| Design boundary | No database schema, mandatory field set, physical representation, endpoint or implementation cardinality selected |
| Revision | October 31, 2026 |

**Start with the [Glossary](03-Requirements-Glossary.md#data-definitions-glossary)** for preferred terms, then the
[Data Dictionary](02-Data-Dictionary.md#data-definitions-data-dictionary) for information meaning, conceptual forms,
authority/access, lifecycle questions and requirement/scenario links. A proposed
definition is not an accepted product rule or proof that storage exists.

[Reading routes](#data-definitions-data-definitions--heading-1-reading-routes) · [Documents](#data-definitions-data-definitions--heading-documents)
· [Models](#data-definitions-data-definitions--heading-3-conceptual-models-and-boundaries) · [Open definitions](#data-definitions-data-definitions--heading-4-review-gates-and-evidence)
· [Diagrams](#data-definitions-data-definitions--id-5-diagram-catalog-and-regeneration) · [Maintenance](#data-definitions-data-definitions--heading-6-maintenance)

<a id="data-definitions-data-definitions--heading-1-reading-routes"></a>
## 1. Reading Routes
<a id="data-definitions-data-definitions--id-1-documents-and-reading-route"></a>

| Your question | Suggested route |
| --- | --- |
| What does a term mean? | [Glossary](03-Requirements-Glossary.md#data-definitions-glossary) → relevant domain source; qualify overloaded terms rather than inventing synonyms |
| What information does this feature use? | [Dictionary subjects](02-Data-Dictionary.md#data-definitions-data-dictionary--heading-2-accounts-and-access) → [semantic elements](02-Data-Dictionary.md#data-definitions-data-dictionary--heading-10-cross-cutting-element-definitions) → primary requirement |
| Who controls it and what happens when it changes? | Subject's authority/open questions → [Lifecycle](../03-Requirements-Specification/04-Business-Rules-And-Data-Lifecycle.md#requirements-specification-business-rules-and-data-lifecycle) → exact domain grant/state policy |
| Which requirement/path uses this concept? | [Dictionary trace links](02-Data-Dictionary.md#data-definitions-data-dictionary--heading-11-requirement-and-scenario-cross-references) → [specification guide](../03-Requirements-Specification/16-Requirements-Specification-Guide.md#requirements-specification-requirements-specification-overview) → [scenario catalog](../04-Scenarios-And-Models/02-User-Stories-And-Scenarios.md#scenarios-and-models-user-stories-and-scenarios--heading-2-use-case-and-story-catalog) |
| Is it ready to become a committed data rule? | [Review roadmap](#data-definitions-data-definitions--heading-4-review-gates-and-evidence) → resolve validation/authority/lifecycle questions → record actual owner decision |

<a id="data-definitions-data-definitions--heading-documents"></a>
## Documents

| Document | Primary responsibility | Current content / limitation |
| --- | --- | --- |
| [Glossary](03-Requirements-Glossary.md#data-definitions-glossary) | Preferred terminology and context distinctions | Actors/access, professional content, applications/providers, work/Git/execution and engineering/recovery; no universal grants or compliance finding |
| [Data Dictionary](02-Data-Dictionary.md#data-definitions-data-dictionary) | Conceptual subjects, semantic elements, responsibility and unresolved constraints | All 34 existing subject keys retained with stable anchors; 24 proposed element definitions; exact fields/requiredness/cardinalities/policies pending |

The subject keys and E01–E24 references are local navigation, not final FR/NFR/SCN
identifiers or implementation names. Subject groups may combine concepts for
review; they do not prescribe one table/object per row. The dictionary retains
its existing section anchors, and the glossary retains its original sections/terms.

<a id="data-definitions-data-definitions--heading-3-conceptual-models-and-boundaries"></a>
## 3. Conceptual Models and Boundaries
<a id="data-definitions-data-definitions--id-2-conceptual-information-map"></a>

![MVP with explicitly deferred paths — Product information groups and conceptual relationships](../../Diagrams/Data-Definitions-Map.png)

[Scalable SVG](../../Diagrams/Data-Definitions-Map.svg) ·
[Editable Graphviz](../../Diagrams/Data-Definitions-Map.dot)

The map groups information, not physical stores, foreign keys, counts, automatic
propagation or access grants. Product data differs from the development GitHub
board/repository. Colors supplement labels.

![Editable/live presentation versus actual submitted materials](../../Diagrams/Data-Submission-Boundaries.png)

[Scalable SVG](../../Diagrams/Data-Submission-Boundaries.svg) ·
[Editable PlantUML](../../Diagrams/Data-Submission-Boundaries.puml)

Keep editable sources, live employer views, generated/uploaded artifacts, actual
submitted copies and backups distinct. The capture policy must identify what was
actually submitted; the current live source is not proof it was the material sent.
Later source edits do not overwrite required preserved actual materials.

Other distinctions that must remain explicit:

- Authentication versus resource/action authorization; membership versus unrelated private access.
- Resume-specific override/selection versus shared source and its propagation policy.
- Portfolio project versus work-management project versus repository.
- Backlog Item versus task; board position versus completion/acceptance; Sprint Goal/items/plan as a composite Sprint Backlog.
- Provider/local authority and accepted send versus delivery/read confirmation; unknown external outcome requires safe reconciliation.
- Code/ref/review/run attempt versus separate target approval; Git hosting does not establish execution safety.
- Archive/unlink/deletion/reclamation versus retention/reference policy; quota does not prove resource capacity.
- Backup/recovery point versus actual usable restoration and safe restored access; no target is assigned by a term alone.

<a id="data-definitions-data-definitions--heading-4-review-gates-and-evidence"></a>
## 4. Review Gates and Evidence
<a id="data-definitions-data-definitions--id-3-how-to-use-and-maintain-definitions"></a>
<a id="data-definitions-data-definitions--id-4-current-coverage-and-review"></a>

![Sourced meaning, authority, validation and lifecycle before a committed data rule](../../Diagrams/Data-Definition-Review-Flow.png)

[Scalable SVG](../../Diagrams/Data-Definition-Review-Flow.svg) ·
[Editable PlantUML](../../Diagrams/Data-Definition-Review-Flow.puml)

| Definition group | Decisions/evidence still needed | Dependent gate |
| --- | --- | --- |
| Identity/requiredness | Exact fields, conditions, values/formats, uniqueness, examples/counterexamples and invalid/missing input | Affected M-02 requirements; GAP-D06 where applicable |
| Authority/relationships | Source of truth per property/action, grants/state, counts, overrides and reference consequences | Before dependent data/security design acceptance |
| Representations | Language/time/revision/units, provider mappings and interface compatibility | Domain/interface requirements then justified design |
| Resource quantities | Limits/accounting pools/concurrency and actual capacity | AFO/QSR policies; GAP-D01/D10 findings |
| Retirement/recovery | Per-category retention/eligibility, consistent coverage, old grants/deleted data and provider effects | BRL/QSR policy; GAP-D04 design and later actual restoration |
| Applicability | Current relevant provider/licensing/privacy obligations and operating facts | DOM/EGC review before dependent commitments; no compliance conclusion assumed |

Farhad coordinates [Questions and Decisions](../07-Change-And-Baseline/03-Requirements-Questions-And-Decisions.md#change-and-baseline-open-questions-and-decisions).
Link actual records in [Traceability](../06-Validation-And-Traceability/07-Validation-And-Traceability.md#validation-and-traceability-validation-and-traceability--heading-traceability)
and real inspection results in [Review Findings](../06-Validation-And-Traceability/07-Validation-And-Traceability.md#validation-and-traceability-validation-and-traceability--heading-review-findings).
Local open topics do not claim new shared IDs or resolved decisions. Material
meaning/scope changes follow [Change Control](../07-Change-And-Baseline/02-Requirements-Change-Control.md#change-and-baseline-change-control).

- [ ] Review shared terms/elements against the current primary requirement revision.
- [ ] Resolve acceptance-blocking validation, authority, relationship and lifecycle questions.
- [ ] Keep requirement/scenario links and worked examples semantically consistent.
- [ ] Confirm diagrams explain conceptual meaning without implying schema or grants.
- [ ] Record actual owner review and identified revision before changing definition/baseline status.

**Current outcome:** Proposed working definitions, not an accepted dictionary or
schema baseline. No product storage, integration, access control or recovery result
is demonstrated. M-02 and the wider pre-implementation agreement remain pending.

<a id="data-definitions-data-definitions--heading-5-diagram-catalog-and-regeneration"></a>
## 5. Diagram Catalog and Regeneration
<a id="data-definitions-data-definitions--id-5-diagram-catalog-and-regeneration"></a>

| Diagram | Purpose | Source | SVG | PNG |
| --- | --- | --- | --- | --- |
| Conceptual information map | Information groups and scoped relationships | [DOT](../../Diagrams/Data-Definitions-Map.dot) | [SVG](../../Diagrams/Data-Definitions-Map.svg) | ![data definitions map](../../Diagrams/Data-Definitions-Map.png) |
| Live/submitted boundaries | Editable/live versus actual historical material | [PlantUML](../../Diagrams/Data-Submission-Boundaries.puml) | [SVG](../../Diagrams/Data-Submission-Boundaries.svg) | ![data submission boundaries](../../Diagrams/Data-Submission-Boundaries.png) |
| Terminology boundaries | Similar terms with different context/authority | [DOT](../../Diagrams/Data-Terminology-Boundaries.dot) | [SVG](../../Diagrams/Data-Terminology-Boundaries.svg) | ![data terminology boundaries](../../Diagrams/Data-Terminology-Boundaries.png) |
| Definition review | Meaning, validation, authority and lifecycle refinement | [PlantUML](../../Diagrams/Data-Definition-Review-Flow.puml) | [SVG](../../Diagrams/Data-Definition-Review-Flow.svg) | ![data definition review flow](../../Diagrams/Data-Definition-Review-Flow.png) |

Keep sources/captions/renders synchronized; inspect labels/arrows and file/section
links. Follow the [shared diagram guide](../../Diagrams/Diagram-Catalog.md). From repository root:

```powershell
$diagramFolder = 'docs\SDLC\02-requirements-engineering\diagrams'
$graphvizExe = 'C:\Program Files\Graphviz\bin\dot.exe'
$plantUmlJar = 'C:\Users\fvali\AppData\Local\Resumefolio\DiagramTools\plantuml.jar'
foreach ($format in 'svg', 'png') {
    foreach ($stem in 'data-definitions-map', 'data-terminology-boundaries') {
        & $graphvizExe "-T$format" -Gdpi=140 "$diagramFolder\$stem.dot" -o "$diagramFolder\$stem.$format"
        if ($LASTEXITCODE -ne 0) { throw "Graphviz failed: $stem / $format" }
    }
    foreach ($stem in 'data-submission-boundaries', 'data-definition-review-flow') {
        java '-Djava.awt.headless=true' -jar $plantUmlJar -charset UTF-8 "-t$format" "$diagramFolder\$stem.puml"
        if ($LASTEXITCODE -ne 0) { throw "PlantUML failed: $stem / $format" }
    }
}
```

<a id="data-definitions-data-definitions--heading-6-maintenance"></a>
## 6. Maintenance

Use fictional/sanitized examples. Keep real application documents, private emails,
passwords/tokens/keys and confidential operational values out of repository examples.
Refine semantic rules here and link primary behavior; do not copy competing policy
wording across files. Add schema/types/indexes/storage choices only in later design
with traceability to reviewed requirements.

Preserve stable keys/section anchors when reorganizing. Update subject/element
counts, preferred terms, examples, models, requirement/scenario links and actual
review status together. Use installed tool paths applicable to the machine and
save UTF-8 without BOM; retain editable source and SVG/PNG outputs in version control.

[Requirements index]() · [Specification guide](../03-Requirements-Specification/16-Requirements-Specification-Guide.md#requirements-specification-requirements-specification-overview)
· [Scenarios guide](../04-Scenarios-And-Models/01-Scenarios-And-Models-Guide.md#scenarios-and-models-scenarios-and-models)

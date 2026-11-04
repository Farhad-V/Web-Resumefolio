# Historical package-generation snapshot, November 2, 2026.
# Current UML source files and the complete diagram alignment index are authoritative.
# This legacy script also stages old document text; do not use it to republish current diagrams/docs.
# Its four generic illustrative chart definitions remain unchanged and carry no release commitment.
from pathlib import Path
import subprocess,hashlib,json,re,sys
ROOT=Path('C:/xampp/htdocs/PROJECTs/Web/Web-Resumefolio/docs/MVP/SDLC/04-system-design/02-detailed-and-object-oriented-design')
OUT=Path('output/evolution-visual-package');(OUT/'diagrams').mkdir(parents=True,exist_ok=True)
DOC='05-design-evolution-refactoring-and-technical-debt.md'
views={}
def add(n,t,c,caption):views['evolution-'+n]=(t,c,caption)
add('class-change','Before/after class responsibilities',r'''
package "Before: hypothetical broad class" {
 class ResumeManager {
  +editSource()
  +publish()
  +captureActualMaterials()
 }
}
package "After: candidate cohesive roles" {
 class ApplySelectionHandler
 class PublishRevisionHandler
 class CaptureActualMaterialsHandler
 interface PublicationStore
 PublishRevisionHandler --> PublicationStore
}
ResumeManager ..> ApplySelectionHandler : extract explicit source application
ResumeManager ..> PublishRevisionHandler : retain explicit confirmation
ResumeManager ..> CaptureActualMaterialsHandler : independent history owner
''','A hypothetical original, not a detected code smell. Extracting roles must preserve observable contracts; changing publication or history behavior is a separate behavioral decision.')
add('refactoring-sequence','Step-by-step transformation and verification',r'''
actor Engineer
participant "Current candidate" as C
participant "Contract checks" as T
participant "Adapter seam" as S
Engineer -> C : identify exact baseline and invariants
Engineer -> T : establish focused observed behavior + source obligations
T --> Engineer : results / known defects / limitations
Engineer -> C : extract smallest cohesive handler
Engineer -> T : compare normal / denied / conflict / unknown outcomes
T --> Engineer : pass or stop and correct
Engineer -> S : introduce bounded abstraction if justified
Engineer -> C : wire one compatible implementation
Engineer -> T : verify persistence races + affected integration
T --> Engineer : candidate-specific evidence
Engineer -> C : remove obsolete path only after compatibility gate
note over Engineer,T
 Proposed engineering sequence, not runtime product messages
 or evidence that a refactoring has been executed.
end note
''','Each step has a reviewable candidate and a stop/correct route. Characterization does not legitimize known requirement violations; code reversal remains conditional on data and effect compatibility.')
add('dependency-hotspots','Hypothetical dependency cycle and hotspot',r'''
component "Presentation internals" as P
component "Applications internals" as A
component "Universal helper\nbroad fan-in / policy coupling" as H #FFE0CC
component "Communication" as C
P -[#red]-> A : forbidden internal dependency
A -[#red]-> P : cycle
P --> H
A --> H
C --> H
note bottom of H
 Teaching example only. No source imports,
 fan-in counts or actual hotspot measured.
end note
''','Red edges depict an invented cycle to investigate, not actual repository dependencies. A central technical utility is not automatically debt; shared mutable business authority and change propagation require concrete evidence.')
add('package-direction','Before/after package dependency direction',r'''
package "Before: illustrative cycle" {
 package "Presentation internal" as P1
 package "Applications internal" as A1
 P1 ..> A1
 A1 ..> P1
}
package "After: candidate dependency boundary" {
 package "Applications use case" as A2
 package "Presentation public contract" as PC
 package "Presentation implementation" as P2
 A2 ..> PC : permitted projection
 P2 ..> PC : realizes contract
}
''','The target removes this selected source cycle through an owner-controlled public contract. It does not permit cross-module writes or prove that the entire application is acyclic. Runtime requests and source dependency arrows must be reviewed separately.')
add('erosion','Intended versus eroded architecture',r'''
package "Intended: owner boundary" {
 component "Consumer" as C
 interface "Public owner contract" as P
 component "Owner implementation" as O
 database "Owner state" as D
 C --> P
 O ..|> P
 O --> D
}
package "Hypothetical erosion, not observed actual state" {
 component "Consumer shortcut" as X
 database "Other owner's tables" as Y
 component "Hidden save observer" as H
 cloud "External effect" as E
 X -[#red]-> Y : bypass owner invariant
 Y -[#red]-> H
 H -[#red]-> E : implicit send / publish
}
''','An actual-versus-intended comparison requires an identified source candidate and inspected imports/effects. No actual architecture audit is asserted here; the erosion half shows the kinds of divergence to look for.')
add('history','Design evolution timeline and ADR history',r'''
rectangle "Existing proposal records\nADR-001 modular boundaries\nADR-002 publication / history\nADR-003 durable external attempts" as A
rectangle "Current documentation package\nNovember 2, 2026\nExamples and engineering procedure" as B
rectangle "Proposed evolution decision\nADR-004 compatible incremental change\nStatus: Proposed" as C
rectangle "Future candidate-specific work\nEvidence -> owner disposition\nimplementation -> verification" as D
A --> B : context, not acceptance
B --> C : records recommendation
C --> D : conditional next steps
''','This is a documentation/proposal sequence, not a fabricated release/version history. Existing ADRs remain Proposed. Future implementation and acceptance have no invented date.')
add('strangler','Strangler facade: conditional future replacement',r'''
actor Caller
component "Compatibility facade\nCurrent authority + exact routing" as F
component "Old implementation\nif an actual one is established" as O
component "New owner implementation" as N
database "Authoritative state\nidentity / history / references" as D
Caller --> F
F --> O : unchanged cohorts / operations
F --> N : explicitly migrated scope
O --> D : designated writer only
N --> D : designated writer only
note bottom of D
 One authoritative write route per operation/cohort.
 No uncontrolled dual writes or duplicated remote effects.
end note
''','A conditional pattern, not a new legacy-migration feature or authorized migration. Define routing, compatible contracts, pending work, reference protection, reconciliation and cutover evidence before any real use. Do not shadow consequential sends or deployments.')
add('branch-abstraction','Branch by abstraction inside one application',r'''
component "Unchanged caller" as C
interface "Stable bounded contract" as P
component "Old adapter" as O
component "New adapter" as N
component "Composition-root selection\nreviewed version / operation scope" as S
C --> P
O ..|> P
N ..|> P
S ..> O : first retain
S ..> N : switch after evidence gate
note bottom of S
 Selection is not permission. Resolve current authority
 and preserve command/attempt identity across coexistence.
end note
''','Introduce abstraction, retain behavior through the old adapter, verify the new adapter, switch the designated route, then retire only when old consumers/pending work permit. This is independent of creating a long-lived source-control branch.')
add('component-target','Legacy-shaped versus target component state',r'''
package "Hypothetical existing shape" {
 component "Broad resume manager\ntransport + policy + storage + effects" as M
}
package "Candidate target within modular app" {
 component "Transport" as T
 component "Presentation use cases" as P
 component "Applications capture use case" as A
 interface "Presentation projection contract" as PC
 component "Persistence / artifact adapters" as I
 T --> P
 T --> A
 A --> PC
 P ..|> PC
 P --> I
}
M ..> P : bounded extraction
M ..> A : retain actual-material ownership
''','Legacy-shaped is a hypothetical structural comparison, not an established running legacy system. The target remains a modular application; this view neither selects microservices nor authorizes moving private data.')
add('lifecycle','Refactoring/migration work lifecycle',r'''
[*] --> Identified
Identified --> Assessed : baseline + source impact
Assessed --> Planned : remedy / compatibility / evidence plan
Planned --> Changing : authorized bounded scope
Changing --> Verifying : candidate ready
Verifying --> Changing : failed checks; correct
Verifying --> Ready : required checks pass
Ready --> Closed : actual disposition + retained evidence
Changing --> Stopped : unsafe or incompatible result
Stopped --> Assessed : assess actual effects / recovery
Closed --> [*]
note right of Ready
 Not product state enums.
 Ready is not owner acceptance
 or deployment authorization.
end note
''','Proposed engineering-work states, not implementation enums. Stopping work cannot undo irreversible data or remote effects; reassess before compatible rollback, forward repair or recovery.')
add('safety-net','Contract-oriented verification safety net',r'''
rectangle "Exact candidate + source invariants\nCurrent behavior / known violations" as C
rectangle "Focused domain / handler checks\nNormal, denied, conflict, repeat, unknown" as U
rectangle "Real persistence + concurrency\nGuard ordering / revision / references" as D
rectangle "Controlled boundary integration\nProvider / Git / executor where changed" as I
rectangle "Compatibility / recovery checks\nOld-new workers, schema, pending effects" as O
rectangle "Disposition\nResults + limitations + protected state" as R
C --> U
C --> D
C --> I
C --> O
U --> R
D --> R
I --> R
O --> R
''','A coverage plan rather than a measured coverage percentage. Choose checks for affected risks; unit mocks alone do not establish persistence races, actual external idempotency, executor isolation or usable recovery.')

style='skinparam backgroundColor white\nskinparam shadowing false\nskinparam defaultFontName Arial\nskinparam classAttributeIconSize 0\n'
for n,(title,code,_) in views.items():
 mix='' if n.endswith(('sequence','lifecycle')) else 'allowmixing\n'
 (OUT/'diagrams'/f'{n}.puml').write_text('@startuml\n'+mix+'title Proposed — '+title+'\n'+style+code+'\n@enduml',encoding='utf-8')
for fmt in ('svg','png'):
 r=subprocess.run(['C:/Program Files/Eclipse Adoptium/jdk-25.0.3.9-hotspot/bin/java.exe','-DGRAPHVIZ_DOT=C:/Program Files/Graphviz/bin/dot.exe','-jar','C:/Users/fvali/AppData/Local/Resumefolio/DiagramTools/plantuml.jar','-charset','UTF-8','-t'+fmt,str((OUT/'diagrams').resolve()/'*.puml')],capture_output=True,text=True)
 assert r.returncode==0,r.stderr

# Chart data is deliberately synthetic; never infer actual debt from these examples.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
chart_titles={}
def save(n,title):
 n='evolution-'+n;chart_titles[n]=title
 plt.gcf().text(.5,.015,'Illustrative only — no project measurement or accepted prioritization',ha='center',fontsize=9)
 plt.tight_layout(rect=(0,.05,1,1))
 for ext in ('svg','png'):plt.savefig(OUT/'diagrams'/f'{n}.{ext}',dpi=160)
 plt.close()
fig,ax=plt.subplots(figsize=(9,5));ax.set(xlim=(0,2),ylim=(0,2),xticks=[.5,1.5],xticklabels=['Reckless','Prudent'],yticks=[.5,1.5],yticklabels=['Inadvertent','Deliberate'],title='Technical debt quadrant — classification examples')
ax.axhline(1,color='gray');ax.axvline(1,color='gray')
for x,y,t in [(.5,1.5,'Skip owner boundaries\nwithout consequence review'),(1.5,1.5,'Bounded shortcut with\nactual recorded trade-off'),(.5,.5,'Unrecognized coupling\nfrom missing design knowledge'),(1.5,.5,'New understanding reveals\na better decomposition')]:ax.text(x,y,t,ha='center',va='center',fontsize=10)
save('debt-quadrant','Technical debt quadrant')
fig,ax=plt.subplots(figsize=(8,5));ax.set(xlim=(0,2),ylim=(0,2),xticks=[.5,1.5],xticklabels=['Lower effort','Higher effort'],yticks=[.5,1.5],yticklabels=['Lower impact','Higher impact'],title='Debt impact versus effort — qualitative decision aid');ax.axhline(1,color='gray');ax.axvline(1,color='gray')
for x,y,t in [(.5,1.5,'Investigate early action'),(1.5,1.5,'Plan staged remediation'),(.5,.5,'Fit when justified'),(1.5,.5,'Challenge value / defer only\nwith actual disposition')]:ax.text(x,y,t,ha='center',va='center')
save('impact-effort','Impact versus effort matrix')
fig,ax=plt.subplots(figsize=(8,5));x=list(range(7));ax.plot(x,[1,1.3,1.8,2.5,3.5,4.8,6.5],label='Possible compounding change friction');ax.plot(x,[1,1.2,1.4,1.6,1.8,2,2.2],label='Possible bounded friction');ax.set(xlabel='Illustrative change cycles (not calendar dates)',ylabel='Relative friction (synthetic units)',title='Possible debt interest — conceptual, not a forecast');ax.legend()
save('interest-curve','Conceptual debt interest curve')
data={'status':'synthetic teaching data, not repository metrics','points':[{'label':'Example A','churn':8,'complexity':8},{'label':'Example B','churn':8,'complexity':2},{'label':'Example C','churn':2,'complexity':8},{'label':'Example D','churn':2,'complexity':2}],'interest_compounding':[1,1.3,1.8,2.5,3.5,4.8,6.5],'interest_bounded':[1,1.2,1.4,1.6,1.8,2,2.2]}
fig,ax=plt.subplots(figsize=(8,5));ax.set(xlim=(0,10),ylim=(0,10),xlabel='Synthetic relative churn',ylabel='Synthetic relative complexity',title='Churn versus complexity — how to read a hotspot chart');ax.axhline(5,color='gray',ls='--');ax.axvline(5,color='gray',ls='--')
for p in data['points']:ax.scatter(p['churn'],p['complexity'],s=90);ax.annotate(p['label'],(p['churn']+.2,p['complexity']+.2))
save('churn-complexity','Illustrative churn versus complexity hotspot chart')
(OUT/'diagrams/evolution-chart-data.json').write_text(json.dumps(data,indent=2))
# Keep the exact reproducible generator alongside its charts.
(OUT/'diagrams/evolution-visuals-generator.py').write_bytes(Path(__file__).read_bytes())

body=(ROOT/DOC).read_text(encoding='utf-8-sig')
body=body.replace('· [Evidence](#6-verification-and-completion)','· [Evidence](#6-verification-and-completion) · [Visual package](#8-evolution-and-debt-visual-package)',1)
body+='\n## 8. Evolution and debt visual package\n\nAll comparisons below are **hypothetical design examples** unless an exact inspected candidate is explicitly identified. No implementation debt, actual architecture erosion, migration, measured hotspot or completed release is established. Legacy replacement is a conditional engineering pattern, not added product scope.\n\n'
for i,(n,(title,code,caption)) in enumerate(views.items(),1):body+=f'### 8.{i} {title}\n\n![{title}](diagrams/{n}.svg)\n\n[PlantUML](diagrams/{n}.puml) · [PNG](diagrams/{n}.png)\n\n{caption}\n\n'
body+='''### 8.12 Smell-to-refactoring mapping

| Indicator to investigate | Candidate remedy | Evidence and preservation check |
| --- | --- | --- |
| Broad manager with unrelated reasons to change | Extract cohesive handlers | Inspect actual callers; preserve explicit confirmation and owned invariants |
| Cyclic internal imports / cross-owner table access | Introduce owner public contract; relocate misplaced responsibility | Inspect actual import/write graph; prevent mutation bypass |
| Repeated authority logic diverges | Consolidate rule at authoritative owner | Compare exact semantics; do not merge distinct grant/consent rules |
| Long navigation chains expose private internals | Intention-revealing owner operation | Preserve exact eligibility and protected reference lifetime |
| Network call inside local transaction | Separate durable intent and attributable effect attempt | Review atomicity changes; reconcile uncertain results before repetition |
| Mutable actor/session retained in shared service | Bound context lifetime and reconstruct current authority | Exercise concurrent callers and revocation; no stale privileged identity |
| Oversized adapter interface | Split consumer-specific ports | Preserve capability and failure semantics for all affected consumers |

### 8.13 Technical debt register format and current position

This is a register **template**, not a second live backlog. No evidenced implementation debt item is allocated here. Link real future entries to the authoritative tracker and review record; open feasibility/design work remains in its owning record.

| Item / evidence | Impact if retained | Full cost to fix | Priority / disposition | Owner / closure |
| --- | --- | --- | --- | --- |
| No actual debt item established by this update | Not assessed | Not estimated | Unassigned; no accepted deferral | Farhad; requires actual finding and evidence |
| Template: stable ID + candidate + code/model locator + observed deficiency | Source criteria, exposure, recurrence and uncertainty | Analysis, implementation, migration, verification, docs and operations; estimate only after inspection | Actual urgency, rationale, authority and review trigger; link tracker/ADR | Responsible owner; exact remedied candidate, checks and remaining limits |

### 8.14 Classification, prioritization and measurement aids

'''
for n,title in chart_titles.items():body+=f'![{title}](diagrams/{n}.svg)\n\n[SVG](diagrams/{n}.svg) · [PNG](diagrams/{n}.png)\n\n'
body+='''Quadrant labels classify how a deficiency arose, not whether it is acceptable. Impact/effort is qualitative: source violations and commitment-blocking security, privacy, history or recovery gates take precedence over convenience. Neither chart allocates work or authorizes deferral.

The interest curves show possible maintenance-friction shapes, not forecast hours, money, deadlines or a claim that all debt compounds. The hotspot chart contains **four invented points**, not file names or project measurements. For a real chart, fix the candidate/history window, define churn (including rename/generated-file handling), choose a compatible complexity measure and inspect the high-churn/high-complexity candidates before recording findings. High values alone do not establish debt; small frequently changed files and complex stable algorithms can be legitimate.

[Synthetic chart data](diagrams/evolution-chart-data.json) · [Reproducible package generator](diagrams/evolution-visuals-generator.py). The generator defaults to staging; its explicit publish option checks saved target hashes before writing. No measurement collection or product execution occurs.

### 8.15 Evolution decision record

See [ADR-004 — Compatible incremental design evolution](../07-design-decisions/ADR-004-compatible-incremental-design-evolution.md). **Status: Proposed.** It records the recommended procedure and alternatives; it does not accept a debt item, authorize a migration, change product behavior or establish owner approval.
'''
adr='''# ADR-004 — Compatible Incremental Design Evolution

- Status: **Proposed**
- Date: November 2, 2026
- Decision authority: Farhad
- Scope: proposed engineering procedure; no migration or implementation authorized by this record

## Context

The modular application proposal must preserve current private authority, explicit source application/publication, independent actual submission materials and attributable external effects during structural change. This documentation update establishes no inspected implementation deficiency or running legacy baseline.

## Proposed decision

Prefer the smallest compatible, evidence-led change. Identify the exact baseline and affected contracts; establish focused checks; extract one responsibility or introduce a justified abstraction; verify behavior, real persistence/concurrency and affected adapters; switch one authoritative route; retire obsolete paths only when old consumers, pending work and recovery conditions permit.

Use branch by abstraction or a strangler facade only when an actual replacement need is established. Define per-operation/cohort authority, old/new contract compatibility, command/attempt identity, protected references, reconciliation and stop conditions. Avoid uncontrolled dual writes and shadow execution of sends, Git mutations, workflows or deployments.

## Alternatives

| Option | Consequence |
| --- | --- |
| Leave unchanged | Reasonable when no evidenced deficiency/value exists; record actual implications if a finding exists |
| Incremental compatible change | Smaller assessable steps; requires temporary compatibility and disciplined retirement |
| Broad rewrite / immediate extraction | Potential structural freedom, with larger verification, migration, distributed-failure and operating burden; requires separate justification |

## Consequences and limits

Temporary adapters and coexistence add maintenance work within the total 20 project hours/week. Refactoring preserves applicable behavior; source-policy or API behavior changes need separate disposition. Reverting code cannot undo irreversible data changes or remote effects. Stop, preserve evidence and select compatible rollback, reviewed forward repair or scoped recovery according to actual state.

## Validation and disposition

Before applying to real work, identify the exact candidate, observed finding, alternatives, full effort, affected criteria, checks, compatibility/recovery route and authorized scope. Close only with actual candidate-specific results and owner disposition. This proposal has no live test, migration result or acceptance evidence.

[Owning evolution procedure](../02-detailed-and-object-oriented-design/05-design-evolution-refactoring-and-technical-debt.md) · [ADR index](README.md) · [ADR-001 modular boundaries](ADR-001-modular-application-boundaries.md) · [ADR-002 publication/history](ADR-002-explicit-publication-and-history.md) · [ADR-003 external attempts](ADR-003-durable-external-attempts.md)
'''
catalog=(ROOT/'diagrams/README.md').read_text(encoding='utf-8-sig')+'\n## Expanded evolution and debt package\n\n'
for n,(title,_,_) in views.items():catalog+=f'- [{title}]({n}.svg) · [PlantUML]({n}.puml) · [PNG]({n}.png)\n'
for n,title in chart_titles.items():catalog+=f'- [{title}]({n}.svg) · [PNG]({n}.png)\n'
catalog+='\n[Generator](evolution-visuals-generator.py) · [Synthetic chart data](evolution-chart-data.json) · [Owning procedure and tables](../05-design-evolution-refactoring-and-technical-debt.md#8-evolution-and-debt-visual-package). All counterexamples/measurements are illustrative, not observed findings.\n'
ADRROOT=ROOT.parent/'07-design-decisions';adrname='ADR-004-compatible-incremental-design-evolution.md'
index=(ADRROOT/'README.md').read_text(encoding='utf-8-sig')+'\n## Proposed evolution procedure\n\n[ADR-004 — Compatible incremental design evolution](ADR-004-compatible-incremental-design-evolution.md) records a proposed procedure, not an accepted debt item or authorized migration.\n'
files={ROOT/DOC:body,ROOT/'diagrams/README.md':catalog,ADRROOT/adrname:adr,ADRROOT/'README.md':index}
manifest={}
for target,text in files.items():
 rel=target.relative_to(ROOT.parent).as_posix();p=OUT/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8');manifest[str(target)]=str(p)
for p in (OUT/'diagrams').iterdir():manifest[str(ROOT/'diagrams'/p.name)]=str(p)
count=0
for target,s in files.items():
 for link in re.findall(r'\]\(([^)]+)\)',s):
  if link.startswith('#') or '://' in link:continue
  p=(target.parent/link.split('#')[0]).resolve()
  assert str(p) in {str(Path(x).resolve()) for x in manifest} or p.exists(),link
  count+=1
if '--publish' not in sys.argv:
 baseline={}
 for t in manifest:
  p=Path(t);baseline[t]=hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None
  if p.exists():
   b=OUT/'previous'/p.relative_to(ROOT.parent);b.parent.mkdir(parents=True,exist_ok=True);b.write_bytes(p.read_bytes())
 (OUT/'baseline.json').write_text(json.dumps(baseline,indent=2))
else:
 for t,h in json.loads((OUT/'baseline.json').read_text()).items():
  p=Path(t);assert (hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None)==h,t
 for t,src in manifest.items():
  p=Path(t);p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(Path(src).read_bytes());assert p.read_bytes()==Path(src).read_bytes()
print(('Published' if '--publish' in sys.argv else 'Prepared'),len(manifest),'files;',count,'local links; 11 UML views, 4 charts, 2 tables and proposed ADR-004.')

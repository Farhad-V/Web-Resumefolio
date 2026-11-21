from pathlib import Path
import json
OUT=Path(__file__).resolve().parent
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.style.use('dark_background')
plt.rcParams.update({'figure.facecolor':'#111827','axes.facecolor':'#111827','text.color':'#F3F4F6','axes.labelcolor':'#F3F4F6','xtick.color':'#F3F4F6','ytick.color':'#CBD5E1'})
chart_titles={}
def save(n,title):
 n='evolution-'+n;chart_titles[n]=title
 plt.gcf().text(.5,.015,'Illustrative only — no project measurement or accepted prioritization',ha='center',fontsize=9)
 plt.tight_layout(rect=(0,.05,1,1))
 for ext in ('svg','png'):plt.savefig(OUT/f'{n}.{ext}',dpi=160)
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
(OUT/'evolution-chart-data.json').write_text(json.dumps(data,indent=2))

from pathlib import Path
import json,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=Path(__file__).resolve().parent
d=json.loads((p/'drivers-options-radar.json').read_text())
angles=[i*2*math.pi/len(d['axes']) for i in range(len(d['axes']))]
fig,ax=plt.subplots(figsize=(10,8),subplot_kw={'projection':'polar'})
ax.set_theta_offset(math.pi/2);ax.set_theta_direction(-1)
labels=['Initial delivery\nsimplicity','Ownership\nclarity','Local\nconsistency','Independent release\npotential','Failure separation\npotential','Solo operations\nfit']
ax.set_xticks(angles,labels,fontsize=11);ax.tick_params(axis='x',pad=18)
ax.set_ylim(0,5);ax.set_yticks([1,2,3,4,5]);ax.set_yticklabels(['1','2','3','4','5'],fontsize=9,color='#596472')
for (name,vals),color,ls in zip(d['options'].items(),['#a64b38','#2563a6','#34734d'],['--','-','-.']):
 ax.plot(angles+[angles[0]],vals+[vals[0]],label={'A':'A — weak internal boundaries','B':'B — modular monolith','C':'C — initial microservices'}[name],color=color,linewidth=2,linestyle=ls,marker='o')
ax.grid(color='#d8dee6');fig.suptitle('Historical options — November 2 comparison',fontsize=17,y=.97)
fig.text(.5,.91,'1 = least favorable · 5 = most favorable for this criterion / project context',ha='center',fontsize=10)
fig.legend(loc='lower center',bbox_to_anchor=(.5,.06),ncol=1,frameon=False,fontsize=10)
fig.text(.5,.025,'Historical comparison; ADR-005 supersedes the common-application boundary. Not current architecture scores.',ha='center',fontsize=9,color='#4b5563')
fig.subplots_adjust(top=.80,bottom=.23,left=.16,right=.84)
for ext in ['svg','png']:fig.savefig(p/('drivers-options-radar.'+ext),dpi=160,facecolor='white')

import pathlib,json,csv,math,collections,hashlib,shutil,datetime,statistics
R=pathlib.Path(r'F:\Research\PACT\Gate11'); P=R/'01_inputs/S008/PACT'; G=P/'reports/gate10a'
a=json.load(open(R/'06_causality/base_analysis.json')); rows=a['results']; pp=a['native_power_components']
prim=[x for x in rows if x['configuration']=='CS_C1']; candidates=[x for x in rows if x['configuration'].startswith('CS_') and 'dynamic_w' in x]
def corr(xs,ys):
 xm=statistics.mean(xs);ym=statistics.mean(ys)
 den=math.sqrt(sum((x-xm)**2 for x in xs)*sum((y-ym)**2 for y in ys))
 return sum((x-xm)*(y-ym) for x,y in zip(xs,ys))/den if den else None
cor=[]
for metric in ['E_delta_percent','H8_delta_percent']:
 for target in ['scan_FF_Q_transitions_delta_percent','combinational_transitions_delta_percent','total_data_transitions_delta_percent','dynamic_w_delta_percent']:
  cor.append({'predictor':metric,'response':target,'pearson_r':corr([r[metric] for r in candidates],[r[target] for r in candidates]),'n_rows':len(candidates),'independent_families':2,'status':'DESCRIPTIVE_DEPENDENT_DELTAS_NO_INFERENCE'})
controls=[]
for attempt in ['smoke_density0','smoke_nominal_attempt6','smoke_nominal_repeat1','smoke_density2']:
 run=G/'runs/b14_opt/B3T'/attempt; power=json.load(open(run/'power_report.json')); receipt=json.load(open(run/'receipt.json'))
 for x in receipt['outputs']:
  p=P/x['path'].replace('repo://','').replace('\\','/'); assert hashlib.sha256(p.read_bytes()).hexdigest()==x['sha256']
 controls.append({'attempt':attempt,'dynamic_w':power['Total']['internal']+power['Total']['switching'],'receipt_sha256':hashlib.sha256((run/'receipt.json').read_bytes()).hexdigest(),'historical_control_only':True})
floor=controls[0]['dynamic_w']/controls[1]['dynamic_w']; linear_residual=controls[3]['dynamic_w']-(2*controls[1]['dynamic_w']-controls[0]['dynamic_w'])
s=list(csv.DictReader(open(R/'06_causality/spatial_budget.csv'))); budgets=[]
for x in prim:
 ref=next(r for r in rows if r['design']==x['design'] and r['configuration']==x['baseline']); binid=ref['H8_peak_bin']; b=next(r for r in s if r['design']==x['design'] and r['configuration']==x['baseline'] and r['grid']=='8' and int(r['bin'])==binid); c=next(r for r in s if r['design']==x['design'] and r['configuration']=='CS_C1' and r['grid']=='8' and int(r['bin'])==binid)
 budgets.append({'design':x['design'],'reference_H8_bin':binid,'reference_bin_average_dynamic_fraction':float(b['dynamic_fraction']),'reference_bin_average_E_fraction':float(b['activity_fraction']),'same_bin_average_dynamic_delta_percent':100*(float(c['dynamic_w'])/float(b['dynamic_w'])-1),'same_bin_average_E_delta_percent':100*(float(c['weighted_activity'])/float(b['weighted_activity'])-1),'H8_peak_delta_percent':x['H8_delta_percent'],'same_peak_bin':x['H8_peak_bin']==binid})
resources=list(csv.DictReader(open(G/'runtime_resources.csv')))
status=collections.Counter(r['status'] for r in resources)
summary={'descriptive_correlations':cor,'historical_controls':controls,'density0_fixed_dynamic_fraction':floor,'density_control_linear_residual_w':linear_residual,'peak_bin_budgets':budgets,'historical_power_attempts_status_counts':dict(status),'historical_power_attempts_total':len(resources),'historical_selected_power_runs':sum(r['selected_scientific_record']=='True' for r in resources),'extra_optional_experiments':0}
(R/'06_causality/diagnostic_summary.json').write_text(json.dumps(summary,indent=2))
shutil.copyfile(G/'runtime_resources.csv',R/'10_logs/historical_Gate10A_all_attempts.csv')
shutil.copyfile(r'F:\Research_Archives\AUDIT_REPORTS\git_audit\G005.json',R/'00_audit/archived_source_git_audit_G005.json')
print(json.dumps(summary,indent=2))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size':9,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,3,figsize=(14,4.3),layout='constrained')
labels=[r['design'].split('_')[0]+' '+r['configuration'].replace('CS_','') for r in candidates]; y=np.arange(len(candidates))
for i,(k,label,color) in enumerate([('E_delta_percent','E','#247b99'),('H8_delta_percent','H8','#ba7841'),('dynamic_w_delta_percent','Dynamic power estimate','#51644d')]):
 axes[0].barh(y+(i-1)*.23,[r[k] for r in candidates],height=.21,label=label,color=color)
axes[0].set_yticks(y,labels); axes[0].axvline(0,color='0.5',lw=.7); axes[0].set_xlabel('Change versus frozen reference (%)');axes[0].set_title('Peak proxy and average power diverge'); axes[0].legend(frameon=False,fontsize=8)
refs=[next(r for r in rows if r['design']==d and r['configuration']==b) for d,b in [('b14_opt','B3T'),('b15_opt','B2')]]; bottom=np.zeros(2)
for cat,col in [('Combinational','#247b99'),('Sequential','#ba7841'),('Clock','#87997c')]:
 vals=[100*next(p for p in pp if p['design']==r['design'] and p['configuration']==r['configuration'] and p['native_category']==cat)['dynamic_w']/r['dynamic_w'] for r in refs]
 axes[1].bar(['b14 B3T','b15 B2'],vals,bottom=bottom,label=cat,color=col);bottom+=vals
axes[1].set_ylim(0,110);axes[1].set_ylabel('Share of reference dynamic estimate (%)');axes[1].set_title('Clock and sequential budgets persist');axes[1].legend(frameon=False,fontsize=8)
f=json.load(open(R/'06_causality/followup_01_results.json')); sel=[r for r in f if r['candidate']=='CS_C1'];xx=np.arange(2)
axes[2].bar(xx-.17,[r['activity_component_percent_baseline_E'] for r in sel],width=.32,label='Activity term',color='#247b99');axes[2].bar(xx+.17,[r['capacitance_component_percent_baseline_E'] for r in sel],width=.32,label='Capacitance term',color='#ba7841');axes[2].set_xticks(xx,['b14 C1','b15 C1']);axes[2].axhline(0,color='0.5',lw=.7);axes[2].set_ylabel('Contribution relative to reference E (%)');axes[2].set_title('Capacitance is a small offset on b15');axes[2].legend(frameon=False,fontsize=8)
fig.suptitle('PACT Gate 11: frozen seed-11 evidence and new accounting',fontsize=14)
fig.text(.5,-.02,'Historical zero-delay activity and fixed-duty routed Liberty estimates; no transient or signoff claim. All variants shown where power exports exist.',ha='center',fontsize=8)
fig.savefig(R/'08_reports/PACT_GATE11_CAUSAL_SUMMARY.png',dpi=180,bbox_inches='tight');fig.savefig(R/'08_reports/PACT_GATE11_CAUSAL_SUMMARY.pdf',bbox_inches='tight');plt.close(fig)

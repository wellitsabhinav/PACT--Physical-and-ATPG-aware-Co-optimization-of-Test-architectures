import json,pathlib,collections,hashlib
R=pathlib.Path(r'F:\Research\PACT\Gate11'); P=R/'01_inputs/S008/PACT'
inv=json.loads((R/'00_audit/archive_inventory.json').read_text()); index=collections.defaultdict(list)
for x in inv: index[x['SHA256']].append(x)
s=json.load(open(P/'reports/gate10a/selected_architectures.json')); machine=json.load(open(P/'reports/gate10a/machine_summary.json'))
binds=[]
def walk(x):
 if isinstance(x,dict):
  if 'path' in x and 'sha256' in x: binds.append(x)
  for v in x.values(): walk(v)
 elif isinstance(x,list):
  for v in x: walk(v)
walk(s); walk(json.load(open(P/'reports/gate10a/tool_provenance.json')))
for x in machine['architectures']:
 path=P/x['run_receipt']['path'].replace('repo://','')
 walk(json.load(open(path)))
found=[]; missing=[]
for x in {b['sha256']:b for b in binds}.values():
 candidates=[i for i in index[x['sha256']] if i['Kind']=='file' and i['ArchivePath'] and i['ArchiveMember']!='[entire copied archive]']
 if candidates:
  candidates.sort(key=lambda i:(i['SourceID']!='S008',i['SourceID']!='S002',i['RelativePath']))
  i=candidates[0]; target=R/'01_inputs'/i['SourceID']/pathlib.Path(i['RelativePath'])
  found.append(dict(binding=x,entry=i,staged=target.exists()))
 else: missing.append(x)
(R/'00_audit/required_binding_recovery.json').write_text(json.dumps({'recoverable':found,'not_in_archive_inventory':missing},indent=2))
freeze={'question':'Why do E/H8 gains weakly transfer to physical shift power, and is a distinct DAC mechanism demonstrated?','designs':['b14_opt','b15_opt'],'seed':11,'K':2,'reference':{'b14_opt':'B3T','b15_opt':'B2'},'selected_architectures':s['selection'],'include_all_Gate09_methods_in_historical_table':True,'primary':'CS_C1','power_selection':'unchanged Gate10A selected earliest admissible nominal run','clock_period_ns':10,'VDD_V':1.1,'nonclock_duty':0.5,'analysis':['recalculate frozen per-net totals','classify transitions by source Liberty master','recalculate saved per-instance power by cell class','analyze spatial and saved temporal summaries'],'new_simulation':'blocked pending exact qualified workload/netlist recovery','no_optimizer_changes':True,'post_outcome_thresholds':False,'optional_followup':'not yet admitted','limits':'one serial process; no install/build/download; no reroute; no GPU'}
(R/'02_reproduction/frozen_comparisons.json').write_text(json.dumps(freeze,indent=2))
print('Bindings',len(binds),'unique',len(found)+len(missing),'recoverable',len(found),'not staged',sum(not x['staged'] for x in found),'missing',len(missing))
print('Additional recoverable',[(x['entry']['SourceID'],x['entry']['RelativePath'],x['entry']['LogicalBytes']) for x in found if not x['staged']][:30])
print('Missing raw',[(x['path'],x.get('bytes')) for x in missing if any(t in x['path'] for t in ['counts','spef','patterns','routed.v','compatible.v'])][:25])
print('G005',json.dumps({k:v for k,v in json.load(open(r'F:\Research_Archives\AUDIT_REPORTS\git_audit\G005.json')).items() if k not in ['results']})[:1000])

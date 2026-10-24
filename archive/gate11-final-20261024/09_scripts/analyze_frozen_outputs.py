"""Gate11 accounting of frozen outputs; no simulation, search, power-tool or causal intervention."""
import pathlib,json,csv,math,hashlib,collections,re
R=pathlib.Path(r'F:\Research\PACT\Gate11'); P=R/'01_inputs/S008/PACT'; G=P/'reports/gate10a'
def read(p): return json.loads(pathlib.Path(p).read_text(encoding='utf-8-sig'))
def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def csvread(p): return list(csv.DictReader(open(p,encoding='utf-8-sig',newline='')))
def writecsv(p,rows):
 fields=list(dict.fromkeys(k for row in rows for k in row))
 with open(p,'w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
def bindpath(p):
 p=p.replace('repo://','').replace('\\','/')
 return P/p
checks=[]
normal=read(P/'reports/repository_cleanup/path_metadata_normalization.json')['files']
for rel,expected in read(P/'reports/repository_cleanup/retained_evidence_sha256.json').items():
 if rel in normal: assert expected==normal[rel]['original_sha256']; expected=normal[rel]['public_sha256']
 actual=sha(P/rel); assert actual==expected,(rel,actual,expected)
 checks.append({'path':rel,'sha256':actual,'status':'PASS','binding':'audited_export' if rel in normal else 'original'})
for rel,expected in read(P/'results/stage_a/checksums.json').items():
 assert sha(P/'results/stage_a'/rel)==expected
 a=csvread(P/'results/stage_a'/rel); b=csvread(P/'results/pact_oss_benchmark/topology_recovery_20261004/stage_a'/rel)
 assert a==[{k:r[k] for k in a[0]} for r in b]
for x in read(G/'machine_summary.json')['architectures']:
 b=x['run_receipt']; path=bindpath(b['path']); assert sha(path)==b['sha256']
 for output in read(path)['outputs']:
  path2=bindpath(output['path'])
  assert path2.is_file(),str(path2)
  assert sha(path2)==output['sha256'],str(path2)
  checks.append({'path':str(path2.relative_to(P)),'sha256':sha(path2),'status':'PASS','binding':'selected_power_run_output'})
(R/'00_audit/retained_hash_verification.json').write_text(json.dumps({'status':'PASS','checks':checks,'scope':'674 retained bindings + StageA projections + all selected Gate10A raw outputs; numerical State replay blocked by absent Numba'},indent=2))
lib=P/'external/OpenROAD-flow-scripts/flow/platforms/nangate45/lib/NangateOpenCellLibrary_typical.lib'
text=lib.read_text(); seq=set()
for m in re.finditer(r'\bcell\s*\(\s*([^\s)]+)\s*\)\s*\{',text):
 depth=1; i=m.end()
 while depth and i<len(text):
  if text[i]=='{': depth+=1
  elif text[i]=='}': depth-=1
  i+=1
 if re.search(r'\b(?:ff|latch)\s*\(',text[m.end():i]): seq.add(m.group(1))
assert 'SDFF_X1' in seq
selected={(x['design'],x['architecture']):x for x in read(G/'selected_architectures.json')['architectures']}
machine={(x['design'],x['architecture']):x for x in read(G/'machine_summary.json')['architectures']}
allrows=[]; powerparts=[]; actparts=[]; spatial=[]; netrows=[]; distr=[]; evidence=[]
for design in ['b14_opt','b15_opt']:
 comp=read(P/f'results/pact_gate09_open_source_20261005/final/{design}/comparison.json'); assert comp['fairness']['status']=='PASS'
 ref=comp['reference_method']; assert len(comp['rows'])==9
 for row in comp['rows']:
  method=row['role'] if row['method']=='PACT' else row['method']; item={'design':design,'configuration':method,'baseline':ref,'comparison_role':'primary' if method=='CS_C1' else ('reference' if method==ref else 'secondary'),'seed':row['seed'],'K':row['chain_count'],'FF_count':row['ff_count'],'chain_lengths':json.dumps(row['chain_lengths']),'patterns':row['patterns'],'shift_cycles':row['cycles'],'scan_period_ns':10,'voltage_v':1.1,'duty_model':0.5,'E_ff_transitions':row['E'],'H4_ff_transitions':row['H4'],'H8_ff_transitions':row['H8'],'activity_status':'HISTORICAL_ZERO_DELAY_SETTLED_MEASUREMENT','routed_scan_path_um':row['routed_scan_wirelength_um'],'total_route_wire_um':None,'route_metric_scope':'connected scan path nets including functional branches; total route wire unavailable','wns_global_route_ns':row['WNS'],'hold_wns_global_route_ns':row['hold_WNS'],'detailed_route_DRC':row['DRC'],'fault_coverage_percent':row['fault_coverage'],'pattern_sha256':row['common_inputs']['patterns']['sha256'],'placement_sha256':row['common_inputs']['placement']['sha256'],'source_netlist_sha256':row['source_netlist']['sha256'],'architecture_sha256':row['architecture_hash'],'qualification_status':row['qualification_status'],'E_delta_percent':row['delta_E_percent'],'H8_delta_percent':row['delta_H8_percent'],'WL_delta_percent':row['delta_routed_WL_percent'],'provenance_path':str(P/f'results/pact_gate09_open_source_20261005/final/{design}/comparison.json'),'new_simulation_status':'BLOCKED_RAW_INPUTS_MISSING','peak_power_status':'MISSING_NO_TIME_RESOLVED_LIBERTY_POWER','parasitic_status':'HISTORICAL_OPENRCX_GROUND_PLUS_PIN; RAW_SPEF_NOT_RECOVERED'}
  hits=[x for x in (P/'results/pact_gate09_open_source_20261005/repair_attempts').rglob('activity_summary.json') if design in x.parts and method in x.parts and 'GATE09_PRIMARY' in x.parts]
  assert len(hits)==1,(design,method,hits)
  summary=read(hits[0]); a=summary['scopes']['all_data']; item.update(total_data_transitions=int(a['transitions']['total']),scan_scope_transitions=int(summary['scopes']['scan_data']['transitions']['total']),max_cycle_weighted_activity=a['cap_weighted_ff_transitions']['maximum'],p99_cycle_weighted_activity=a['cap_weighted_ff_transitions']['p99'],mean_cycle_weighted_activity=a['cap_weighted_ff_transitions']['mean'],H8_peak_cycle=a['grids']['8']['max_cap_cycle'],H8_peak_bin=a['grids']['8']['max_cap_bin'])
  assert math.isclose(row['E'],a['cap_weighted_ff_transitions']['total'],rel_tol=1e-12)
  if (design,method) not in selected:
   item.update(power_status='MISSING_NOT_IN_FROZEN_GATE10A_SET',net_class_activity_status='MISSING_NO_RECOVERED_PER_NET_EXPORT')
   allrows.append(item); continue
  sel=selected[design,method]; ma=machine[design,method]
  run=bindpath(ma['run_receipt']['path']).parent; instances=csvread(run/'instance_power.csv'); imap={x['instance']:x for x in instances}
  nets=csvread(G/f'inputs/{design}/{method}/net_activity_capacitance.csv'); receipt=read(G/f'inputs/{design}/{method}/activity_export_receipt.json')
  assert sha(G/f'inputs/{design}/{method}/net_activity_capacitance.csv')==receipt['output']['sha256']
  groups=collections.defaultdict(list); classified=[]
  for net in nets:
   inst=net['source'].rsplit('/',1)[0] if '/' in net['source'] else None
   source=imap.get(inst); master=source['master'] if source else ''
   if source:
    cls='scan_FF_Q' if master in seq and net['source'].rsplit('/',1)[1] in ['Q','QN'] and inst.startswith('U_SCAN_') else ('other_sequential' if master in seq else 'combinational')
   else: cls='external_input' if net['source'].startswith('PORT/') else 'UNMAPPED_SOURCE'
   count=int(net['transitions']); cap=float(net['ground_pin_ff']); w=cap*count
   record={**net,'design':design,'configuration':method,'source_instance':inst,'source_master':master,'source_class':cls,'weighted_ff_transitions':w}
   groups[cls].append(record); classified.append(record); netrows.append(record)
  assert 'UNMAPPED_SOURCE' not in groups,[(x['source'],x['net']) for x in groups['UNMAPPED_SOURCE']]
  assert len(groups['scan_FF_Q'])==sel['ff_count'],(design,method,len(groups['scan_FF_Q']))
  assert sum(int(x['transitions']) for x in nets)==int(a['transitions']['total'])
  E=math.fsum(x['weighted_ff_transitions'] for x in classified); assert math.isclose(E,row['E'],rel_tol=1e-12)
  for cls,xs in groups.items():
   actparts.append({'design':design,'configuration':method,'source_class':cls,'nets':len(xs),'transitions':sum(int(x['transitions']) for x in xs),'weighted_ff_transitions':math.fsum(x['weighted_ff_transitions'] for x in xs),'ground_ff':math.fsum(float(x['ground_ff']) for x in xs),'pin_ff':math.fsum(float(x['pin_ff']) for x in xs),'incident_coupling_ff':math.fsum(float(x['incident_coupling_ff']) for x in xs),'status':'NEW_AGGREGATION_OF_HISTORICAL_EXPORT'})
  ptotal={k:math.fsum(float(x[k]) for x in instances) for k in ['internal_w','switching_w','leakage_w','total_w']}; ptotal['dynamic_w']=ptotal['internal_w']+ptotal['switching_w']
  for k,v in ptotal.items(): assert math.isclose(v,ma['power'][k],rel_tol=1e-12,abs_tol=1e-18),(k,v,ma['power'][k])
  native=read(run/'power_report.json')
  for cls,values in native.items():
   powerparts.append({'design':design,'configuration':method,'native_category':cls,**{k+'_w':v for k,v in values.items()},'dynamic_w':values['internal']+values['switching'],'status':'HISTORICAL_LIBERTY_ESTIMATE_NATIVE_BINARY32_AGGREGATION'})
  for frac in [0.01,0.1]:
   n=math.ceil(len(classified)*frac); m=math.ceil(len(instances)*frac)
   distr.append({'design':design,'configuration':method,'rank_fraction':frac,'top_net_E_share':math.fsum(sorted((x['weighted_ff_transitions'] for x in classified),reverse=True)[:n])/E,'top_instance_dynamic_share':math.fsum(sorted((float(x['internal_w'])+float(x['switching_w']) for x in instances),reverse=True)[:m])/ptotal['dynamic_w']})
  bounds=sel['bounds_um']
  def binid(x,y,n): return min(n-1,max(0,int((y-bounds[1])/(bounds[3]-bounds[1])*n)))*n+min(n-1,max(0,int((x-bounds[0])/(bounds[2]-bounds[0])*n)))
  for n in [4,8]:
   for b in range(n*n):
    ne=[x for x in classified if binid(float(x['x_um']),float(x['y_um']),n)==b]
    ins=[x for x in instances if binid(float(x['x_um']),float(x['y_um']),n)==b]
    spatial.append({'design':design,'configuration':method,'grid':n,'bin':b,'weighted_activity':math.fsum(x['weighted_ff_transitions'] for x in ne),'activity_fraction':math.fsum(x['weighted_ff_transitions'] for x in ne)/E,'dynamic_w':math.fsum(float(x['internal_w'])+float(x['switching_w']) for x in ins),'dynamic_fraction':math.fsum(float(x['internal_w'])+float(x['switching_w']) for x in ins)/ptotal['dynamic_w'],'cell_count':len(ins),'is_H8_winning_bin':n==8 and b==item['H8_peak_bin']})
  item.update(**ptotal,power_status='HISTORICAL_ROUTED_LIBERTY_ESTIMATE_REAGGREGATED',net_class_activity_status='NEW_AGGREGATION_OF_HISTORICAL_EXPORT',scan_FF_Q_transitions=sum(int(x['transitions']) for x in groups['scan_FF_Q']),combinational_transitions=sum(int(x['transitions']) for x in groups['combinational']),external_input_transitions=sum(int(x['transitions']) for x in groups['external_input']),ground_ff=math.fsum(float(x['ground_ff']) for x in nets),pin_ff=math.fsum(float(x['pin_ff']) for x in nets),scan_scope_ground_pin_ff=math.fsum(float(x['ground_pin_ff']) for x in nets if x['scope_scan_data']=='True'),clock_dynamic_w=ma['power']['clock_dynamic_w'],shift_dynamic_energy_j=ptotal['dynamic_w']*sel['cycles']*1e-8,shift_total_energy_j=ptotal['total_w']*sel['cycles']*1e-8,power_run_receipt_path=str(run/'receipt.json'),power_run_receipt_sha256=ma['run_receipt']['sha256'],activity_export_path=str(G/f'inputs/{design}/{method}/net_activity_capacitance.csv'),activity_export_sha256=receipt['output']['sha256'])
  allrows.append(item)
for row in allrows:
 ref=next(x for x in allrows if x['design']==row['design'] and x['configuration']==row['baseline'])
 for col in ['total_data_transitions','scan_scope_transitions','scan_FF_Q_transitions','combinational_transitions','dynamic_w','switching_w','internal_w','clock_dynamic_w','ground_ff','scan_scope_ground_pin_ff','max_cycle_weighted_activity','p99_cycle_weighted_activity','shift_dynamic_energy_j']:
  if col in row and col in ref:
   row[col+'_absolute_delta']=row[col]-ref[col]; row[col+'_delta_percent']=100*(row[col]/ref[col]-1) if ref[col] else None
writecsv(R/'08_reports/PACT_GATE11_RESULTS.csv',allrows)
writecsv(R/'03_activity/source_class_activity.csv',actparts)
writecsv(R/'03_activity/per_net_classified.csv',netrows)
writecsv(R/'04_power/native_power_components.csv',powerparts)
writecsv(R/'06_causality/spatial_budget.csv',spatial)
writecsv(R/'06_causality/activity_power_concentration.csv',distr)
(R/'06_causality/base_analysis.json').write_text(json.dumps({'results':allrows,'native_power_components':powerparts,'source_class_activity':actparts,'concentration':distr,'cell_classification':'Liberty ff/latch membership and source instance/pin; Q/QN outputs explicitly checked; scan_scope also contains buffers/ports','sequential_Liberty_masters':sorted(seq),'new_scientific_stage':'reanalysis only'},indent=2))
print('PASS hashes',len(checks),'historical rows',len(allrows),'per-net and power rows',len(selected))
for row in allrows:
 if row['configuration'] in ['CS_C1','CS_C2','CS_C3','B5']:
  print(row['design'],row['configuration'],{k:row.get(k) for k in ['E_delta_percent','H8_delta_percent','total_data_transitions_delta_percent','scan_FF_Q_transitions_delta_percent','combinational_transitions_delta_percent','dynamic_w_delta_percent','ground_ff_delta_percent','scan_scope_ground_pin_ff_delta_percent']})
for design in ['b14_opt','b15_opt']:
 ref='B3T' if design=='b14_opt' else 'B2'; pp=[x for x in powerparts if x['design']==design and x['configuration']==ref]; print('POWER_BUDGET',design,pp)



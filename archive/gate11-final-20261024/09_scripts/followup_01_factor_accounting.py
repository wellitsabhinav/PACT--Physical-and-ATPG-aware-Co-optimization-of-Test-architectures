import pathlib,json,csv,math,collections,hashlib
R=pathlib.Path(r'F:\Research\PACT\Gate11'); protocol=R/'07_hypothesis/followup_01_preregistration.md'
base=json.load(open(R/'06_causality/base_analysis.json')); results=base['results']; nets=list(csv.DictReader(open(R/'03_activity/per_net_classified.csv',newline='')))
def key(x): return x['net'],x['source'],x['source_master'],float(x['x_um']),float(x['y_um'])
def cap(x): return float(x['ground_pin_ff'])
def n(x): return int(x['transitions'])
def E(xs): return math.fsum(cap(x)*n(x) for x in xs)
out=[]; details=[]
for row in results:
 if row['configuration']==row['baseline'] or 'dynamic_w' not in row: continue
 d,c,b=row['design'],row['configuration'],row['baseline']; bn={key(x):x for x in nets if x['design']==d and x['configuration']==b}; cn={key(x):x for x in nets if x['design']==d and x['configuration']==c}; common=bn.keys()&cn.keys(); added=cn.keys()-bn.keys(); removed=bn.keys()-cn.keys()
 bb=E([bn[k] for k in common]); cc=E([cn[k] for k in common]); cb=math.fsum(cap(bn[k])*n(cn[k]) for k in common); bc=math.fsum(cap(cn[k])*n(bn[k]) for k in common)
 da=math.fsum((cap(bn[k])+cap(cn[k]))*.5*(n(cn[k])-n(bn[k])) for k in common)
 dc=math.fsum((n(bn[k])+n(cn[k]))*.5*(cap(cn[k])-cap(bn[k])) for k in common)
 du=E([cn[k] for k in added])-E([bn[k] for k in removed]); delta=E(cn.values())-E(bn.values()); residual=da+dc+du-delta
 assert abs(residual)<1e-6,(d,c,residual)
 rec={'design':d,'candidate':c,'reference':b,'common_nets':len(common),'candidate_only_nets':len(added),'reference_only_nets':len(removed),'baseline_common_E_share':bb/E(bn.values()),'candidate_common_E_share':cc/E(cn.values()),'E_bb_common':bb,'E_cb_candidate_counts_baseline_caps':cb,'E_bc_baseline_counts_candidate_caps':bc,'E_cc_common':cc,'activity_component_ff_transitions':da,'capacitance_component_ff_transitions':dc,'unmatched_component_ff_transitions':du,'E_delta_ff_transitions':delta,'identity_residual_ff_transitions':residual,'activity_component_percent_baseline_E':100*da/E(bn.values()),'capacitance_component_percent_baseline_E':100*dc/E(bn.values()),'cap_offset_fraction_of_activity_saving':dc/(-da) if da<0 else None,'H2_direction':'SUPPORTING_SMALL_OFFSET' if dc>0 and da<0 else 'CONTRADICTORY_OFFSET_DIRECTION','physical_causality_status':'MODEL_ACCOUNTING_ONLY_RAW_SPEF_NOT_RECOVERED','protocol_sha256':hashlib.sha256(protocol.read_bytes()).hexdigest()}
 for cls in sorted({bn[k]['source_class'] for k in common}|{cn[k]['source_class'] for k in common}):
  ks=[k for k in common if bn[k]['source_class']==cls and cn[k]['source_class']==cls]
  details.append({'design':d,'candidate':c,'reference':b,'source_class':cls,'matched_nets':len(ks),'activity_component':math.fsum((cap(bn[k])+cap(cn[k]))*.5*(n(cn[k])-n(bn[k])) for k in ks),'capacitance_component':math.fsum((n(bn[k])+n(cn[k]))*.5*(cap(cn[k])-cap(bn[k])) for k in ks)})
 duration=row['shift_cycles']*1e-8; rec['analytical_data_switching_w']=.5*1.1**2*row['E_ff_transitions']*1e-15/duration; rec['analytical_data_switching_energy_j']=.5*1.1**2*row['E_ff_transitions']*1e-15
 out.append(rec)
for filename,rs in [('followup_01_factor_accounting.csv',out),('followup_01_by_source_class.csv',details)]:
 with open(R/'06_causality'/filename,'w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rs[0]));w.writeheader();w.writerows(rs)
(R/'06_causality/followup_01_results.json').write_text(json.dumps(out,indent=2))
for r in out: print(r['design'],r['candidate'],{k:r[k] for k in ['common_nets','baseline_common_E_share','activity_component_percent_baseline_E','capacitance_component_percent_baseline_E','unmatched_component_ff_transitions','cap_offset_fraction_of_activity_saving','H2_direction']})

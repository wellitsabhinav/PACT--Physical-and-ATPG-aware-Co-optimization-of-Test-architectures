import pathlib,json,csv,math
R=pathlib.Path(r'F:\Research\PACT\Gate11');P=R/'01_inputs/S008/PACT'; rows=json.load(open(R/'06_causality/base_analysis.json'))['results']; transfer=[]
for design,folder in [('b14_opt','python_transport'),('b15_opt','metadata_registration_b15_opt')]:
 cohort=P/'results/pact_gate09_open_source_20261005'; comp=json.load(open(cohort/f'final/{design}/comparison.json')); sel=json.load(open(cohort/f'repair_attempts/{folder}/selections/{design}/preselected_candidates.json'))
 for row,raw in zip([r for r in rows if r['design']==design],comp['rows']):
  assert row['architecture_sha256']==raw['architecture_hash']
  row['total_route_wire_um']=raw['total_routed_WL_um'];row['route_metric_scope']='separate connected scan-path upper bound and detailed-route total wire';row['total_route_wire_status']='HISTORICAL_DETAILED_ROUTE_MEASUREMENT'
  ref=next(r for r in comp['rows'] if r['method']==row['baseline']); row['total_route_wire_delta_percent']=100*(raw['total_routed_WL_um']/ref['total_routed_WL_um']-1)
  if raw['method']=='PACT':
   rec=next(x for x in sel['records'] if x['candidate']==row['configuration']);s=json.load(open(P/rec['search_receipt']['path'].replace('repo://','')))
   score=s['reference_score']; est=raw['search_estimates']; row.update(search_E_ff_transitions=est['E_stateful_ff'],search_H4_ff_transitions=est['H4_stateful_ff'],search_H8_ff_transitions=est['H8_stateful_ff'],search_proxy_wire_um=est['wire_um'],search_E_delta_percent=100*(est['E_stateful_ff']/score[1]-1),search_H4_delta_percent=100*(est['H4_stateful_ff']/score[4]-1),search_H8_delta_percent=100*(est['H8_stateful_ff']/score[2]-1),search_estimate_status='HISTORICAL_DEPTH3_CANDIDATE_CAPACITANCE_SURROGATE',search_receipt_path=str(P/rec['search_receipt']['path'].replace('repo://','')))
   transfer.append({k:row[k] for k in ['design','configuration','search_E_ff_transitions','search_H8_ff_transitions','search_E_delta_percent','search_H4_delta_percent','search_H8_delta_percent','E_delta_percent','H8_delta_percent','total_route_wire_delta_percent']})
  else: row['search_estimate_status']='NOT_APPLICABLE_COMPETITOR'
fields=list(dict.fromkeys(k for r in rows for k in r))
with open(R/'08_reports/PACT_GATE11_RESULTS.csv','w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
(R/'06_causality/enriched_results.json').write_text(json.dumps(rows,indent=2))
with open(R/'03_activity/predictor_implemented_transfer.csv','w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(transfer[0]));w.writeheader();w.writerows(transfer)
print(json.dumps(transfer,indent=2))

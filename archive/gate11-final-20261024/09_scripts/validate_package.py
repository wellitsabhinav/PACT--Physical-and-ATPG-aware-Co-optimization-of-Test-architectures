import pathlib,json,csv,math,hashlib,ast,datetime,collections
R=pathlib.Path(r'F:\Research\PACT\Gate11');P=R/'01_inputs/S008/PACT'
def sha(p):return hashlib.file_digest(open(p,'rb'),'sha256').hexdigest()
selected=json.load(open(R/'00_audit/selected_inputs_manifest.json'));extra=json.load(open(R/'00_audit/additional_extraction_receipts.json'))
for x in selected:
 p=R/'01_inputs'/x['SourceID']/pathlib.Path(x['RelativePath']);assert sha(p)==x['SHA256'],str(p)
for x in extra:assert sha(pathlib.Path(x['path']))==x['sha256']
container_checks=[]
for x in json.load(open(R/'00_audit/extraction_receipts.json')):
 actual=sha(pathlib.Path(x['archive']));assert actual==x['sha256'];container_checks.append({'path':x['archive'],'sha256':actual,'unchanged':True})
(R/'00_audit/input_integrity_final.json').write_text(json.dumps({'status':'PASS','staged_member_hashes':len(selected)+len(extra),'containers':container_checks},indent=2))
rows=list(csv.DictReader(open(R/'08_reports/PACT_GATE11_RESULTS.csv',newline='')));assert len(rows)==18
assert len({(x['design'],x['configuration']) for x in rows})==18
assert sum(bool(x['dynamic_w']) for x in rows)==9
source=list(csv.DictReader(open(R/'03_activity/source_class_activity.csv')))
for r in rows:
 assert r['seed']=='11' and r['K']=='2' and r['detailed_route_DRC']=='0'
 if not r['dynamic_w']:continue
 xs=[x for x in source if x['design']==r['design'] and x['configuration']==r['configuration']]
 assert sum(int(x['transitions']) for x in xs)==int(r['total_data_transitions'])
 assert math.isclose(math.fsum(float(x['weighted_ff_transitions']) for x in xs),float(r['E_ff_transitions']),rel_tol=1e-12)
 assert math.isclose(float(r['internal_w'])+float(r['switching_w']),float(r['dynamic_w']),rel_tol=1e-12)
 assert math.isclose(float(r['dynamic_w'])*int(r['shift_cycles'])*1e-8,float(r['shift_dynamic_energy_j']),rel_tol=1e-12)
factors=json.load(open(R/'06_causality/followup_01_results.json'));assert len(factors)==7
for r in factors:assert abs(r['activity_component_ff_transitions']+r['capacitance_component_ff_transitions']+r['unmatched_component_ff_transitions']-r['E_delta_ff_transitions'])<1e-6
required=['PACT_GATE11_PHYSICAL_POWER_CAUSALITY.md','PACT_GATE11_RESULTS.csv','PACT_GATE11_CAUSAL_FINDINGS.md','PACT_GATE11_DAC_NOVELTY.md','PACT_GATE11_DECISION.md','PACT_GATE11_REPRODUCIBILITY.md']
for name in required:assert (R/'08_reports'/name).stat().st_size>100
assert 'Classification: **NO-GO**' in (R/'08_reports/PACT_GATE11_DECISION.md').read_text(encoding='utf-8-sig')
report=(R/'08_reports/PACT_GATE11_PHYSICAL_POWER_CAUSALITY.md').read_text(encoding='utf-8-sig')
for n in range(1,15):assert f'## {n}. ' in report,n
for script in (R/'09_scripts').glob('*.py'):ast.parse(script.read_text(encoding='utf-8-sig'))
# Static validation of every future root/input transformation; do not execute a second experiment.
for name in ['run_manifest.py','analyze_frozen_outputs.py','followup_01_factor_accounting.py','derive_diagnostics.py','enrich_predicted_transfer.py']:
 t=(R/'09_scripts'/name).read_text(encoding='utf-8-sig');assert "pathlib.Path(r'F:\\Research\\PACT\\Gate11')" in t,name
 t=t.replace("pathlib.Path(r'F:\\Research\\PACT\\Gate11')","pathlib.Path(r'F:\\Research\\PACT\\Gate11\\02_reproduction\\validation_only')").replace("P=R/'01_inputs/S008/PACT'","P=pathlib.Path(r'F:\\Research\\PACT\\Gate11\\01_inputs\\S008\\PACT')")
 ast.parse(t)
run=json.load(open(R/'10_logs/followup_01.manifest.json'));assert run['status']=='PASS' and run['wall_seconds']<=120 and run['peak_working_set_bytes']<512*2**20 and run['disk_after_bytes']-run['disk_before_bytes']<20*2**20
completion={'schema':'PACT_GATE11_FOLLOWUP01_COMPLETION','status':'PASS','protocol_sha256':sha(R/'07_hypothesis/followup_01_preregistration.md'),'execution_manifest':'10_logs/followup_01.manifest.json','comparisons':7,'optional_experiments_executed':1,'no_scan_order_changes':True,'measured_resources':run}
(R/'07_hypothesis/followup_01_completion.json').write_text(json.dumps(completion,indent=2))
validation={'status':'PASS','validated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'staged_member_hashes':len(selected)+len(extra),'original_container_post_hashes':container_checks,'all18_rows_retained':True,'nine_power_exports':True,'seven_factor_comparisons':True,'source_class_and_energy_identities':True,'report_sections':14,'reproducer_syntax_and_path_transformations':'PASS_STATIC_ONLY_NOT_EXECUTED','historical_end_to_end':'PASS_12_RECORDS','historical_optimizer_numerical_replay':'BLOCKED_NUMBA','fresh_physical_replay':'BLOCKED_RAW_INPUTS_AND_WSL_DISK','optional_experiments':1,'known_new_failures':['WSL failed before Linux start','retained verifier missing Numba','first accounting PORT source parser assertion','second accounting method/role parser assertion','report command line OS206 before process creation','initial package validation Windows cp1252 decode failure; corrected explicit UTF8']}
(R/'00_audit/package_validation.json').write_text(json.dumps(validation,indent=2));print(json.dumps(validation,indent=2))


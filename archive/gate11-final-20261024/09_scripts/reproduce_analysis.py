"""Reproduce saved-output accounting in a fresh F-only child; never edit frozen inputs."""
import pathlib,os,json,datetime,hashlib,subprocess,sys,csv
ROOT=pathlib.Path(__file__).resolve().parents[1]
assert str(ROOT.resolve()).lower().startswith('f:\\research\\pact\\gate11'),str(ROOT)
assert (ROOT/'01_inputs/S008/PACT').is_dir()
tag=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S_%fZ')
DEST=ROOT/'02_reproduction'/('rerun_'+tag)
DEST.mkdir(exist_ok=False)
for d in ['00_audit','01_inputs','02_reproduction','03_activity','04_power','05_parasitics','06_causality','07_hypothesis','08_reports','09_scripts','10_logs','scratch','cache','tmp']: (DEST/d).mkdir()
original_literal="pathlib.Path(r'F:\\Research\\PACT\\Gate11')"
new_literal='pathlib.Path('+repr(str(DEST))+')'
new_inputs='P=pathlib.Path('+repr(str(ROOT/'01_inputs/S008/PACT'))+')'
manifest={'status':'STARTED','root':str(ROOT),'new_root':str(DEST),'read_only_shared_inputs':str(ROOT/'01_inputs/S008/PACT'),'transform':'Replace Gate11 output root and P input root only; original sources preserved','sources':[],'commands':[]}
programs=['run_manifest.py','analyze_frozen_outputs.py','followup_01_factor_accounting.py','derive_diagnostics.py','enrich_predicted_transfer.py']
for name in programs:
 src=ROOT/'09_scripts'/name; text=src.read_text(encoding='utf-8-sig')
 assert original_literal in text,name
 transformed=text.replace(original_literal,new_literal).replace("P=R/'01_inputs/S008/PACT'",new_inputs)
 dst=DEST/'09_scripts'/name;dst.write_text(transformed,encoding='utf-8')
 manifest['sources'].append({'original':str(src),'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'transformed':str(dst),'transformed_sha256':hashlib.sha256(dst.read_bytes()).hexdigest()})
protocol=ROOT/'07_hypothesis/followup_01_preregistration.md'
(DEST/'07_hypothesis'/protocol.name).write_bytes(protocol.read_bytes())
env=os.environ.copy()
for k,rel in {'TEMP':'tmp','TMP':'tmp','TMPDIR':'tmp','PIP_CACHE_DIR':'cache/pip','XDG_CACHE_HOME':'cache/xdg','XDG_CONFIG_HOME':'cache/config','PYTHONPYCACHEPREFIX':'cache/pycache','MPLCONFIGDIR':'cache/matplotlib','NUMBA_CACHE_DIR':'cache/numba','HOME':'cache/home'}.items():
 env[k]=str(DEST/rel);(DEST/rel).mkdir(parents=True,exist_ok=True)
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:env[k]='1'
env['PYTHONDONTWRITEBYTECODE']='1';env['PYTHONNOUSERSITE']='1';env['PACT_EXPERIMENT_ROOT']=str(DEST)
mp=DEST/'00_audit/reproduction_manifest.json'
mp.write_text(json.dumps(manifest,indent=2))
for i,name in enumerate(programs[1:]):
 cmd=[sys.executable,'-B',str(DEST/'09_scripts/run_manifest.py'),f'reproduction_{i+1}',sys.executable,'-B',str(DEST/'09_scripts'/name)]
 manifest['commands'].append(cmd);mp.write_text(json.dumps(manifest,indent=2))
 result=subprocess.run(cmd,cwd=DEST,env=env)
 if result.returncode:
  manifest['status']='FAILED';manifest['returncode']=result.returncode;mp.write_text(json.dumps(manifest,indent=2));sys.exit(result.returncode)
original=list(csv.DictReader(open(ROOT/'08_reports/PACT_GATE11_RESULTS.csv',newline='')));replayed=list(csv.DictReader(open(DEST/'08_reports/PACT_GATE11_RESULTS.csv',newline='')))
fields=['design','configuration','E_ff_transitions','H4_ff_transitions','H8_ff_transitions','total_data_transitions','scan_FF_Q_transitions','combinational_transitions','dynamic_w','internal_w','switching_w','shift_dynamic_energy_j','routed_scan_path_um','total_route_wire_um','search_E_ff_transitions','search_H8_ff_transitions']
assert len(original)==len(replayed)==18
for a,b in zip(original,replayed):
 for k in fields:assert a.get(k)==b.get(k),(k,a.get(k),b.get(k))
manifest['status']='PASS';manifest['verified_metric_fields']=fields;manifest['rows']=18;mp.write_text(json.dumps(manifest,indent=2))
print('PASS: exact scientific-column reproduction in',DEST)

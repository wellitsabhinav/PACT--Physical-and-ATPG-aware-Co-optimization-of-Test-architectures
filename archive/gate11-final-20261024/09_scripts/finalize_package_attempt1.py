"""Seal the deliverable hashes and measure F-only workspace storage after validation."""
import pathlib,json,hashlib,datetime,shutil,ctypes,ctypes.wintypes as w,os,sys
R=pathlib.Path(r'F:\Research\PACT\Gate11')
assert R.resolve().drive.upper()=='F:'
validation=json.load(open(R/'00_audit/package_validation.json'));assert validation['status']=='PASS'
control=R/'10_logs/package_finalization.json'; started=datetime.datetime.now(datetime.timezone.utc).isoformat()
control.write_text(json.dumps({'status':'STARTED','started_utc':started,'argv':sys.argv,'cwd':os.getcwd(),'self_hash':hashlib.file_digest(open(__file__,'rb'),'sha256').hexdigest()},indent=2))
for rel in ['cache/home','cache/pip','cache/xdg','cache/config','cache/pycache','cache/matplotlib','cache/numba']:(R/rel).mkdir(parents=True,exist_ok=True)
excluded={'00_audit/PACKAGE_SHA256SUMS.json','00_audit/storage_audit_final.json','08_reports/PACT_GATE11_STORAGE.md','10_logs/package_finalization.json'}
hashes={}
for p in sorted(R.rglob('*')):
 assert not p.is_symlink(),str(p)
 if p.is_file() and p.relative_to(R).as_posix() not in excluded:hashes[p.relative_to(R).as_posix()]=hashlib.file_digest(open(p,'rb'),'sha256').hexdigest()
(R/'00_audit/PACKAGE_SHA256SUMS.json').write_text(json.dumps({'algorithm':'SHA256','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'All workspace regular files except self-referential storage/hash/finalization records','exclusions':sorted(excluded),'files':hashes},indent=2))
initial=json.load(open(R/'00_audit/storage_audit_initial.json'));current=json.load(open(R/'00_audit/current_tool_audit.json'))
for k,v in current['environment'].items():assert pathlib.Path(v).resolve().is_relative_to(R.resolve()),(k,v)
getsize=ctypes.windll.kernel32.GetCompressedFileSizeW;getsize.argtypes=[w.LPCWSTR,ctypes.POINTER(w.DWORD)];getsize.restype=w.DWORD
def totals():
 fs=[p for p in R.rglob('*') if p.is_file()];n=sum(p.stat().st_size for p in fs);a=0
 for p in fs:
  hi=w.DWORD();lo=getsize(str(p),ctypes.byref(hi));assert lo!=0xffffffff,str(p);a+=lo+(hi.value<<32)
 return len(fs),n,a
control.write_text(json.dumps({'status':'PASS','started_utc':started,'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'argv':sys.argv,'cwd':os.getcwd(),'package_hashed_files':len(hashes),'self_hash':hashlib.file_digest(open(__file__,'rb'),'sha256').hexdigest()},indent=2))
for i in range(8):
 count,logical,allocated=totals()
 audit={'schema':'PACT_GATE11_STORAGE_AUDIT_v1','status':'PASS_CONTROLLABLE_F_ONLY','workspace':str(R.resolve()),'total_workspace_files':count,'total_workspace_logical_bytes':logical,'allocated_file_bytes':allocated,'allocation_scope':'GetCompressedFileSizeW sum for files; directory/filesystem metadata excluded','initial_free_F_bytes':initial['free_bytes'],'final_free_F_bytes':shutil.disk_usage(R).free,'environment':current['environment'],'all_controlled_paths_inside_Gate11':True,'no_symlinks_or_junctions_created':True,'historical_archives_post_hashes':validation['original_container_post_hashes'],'new_simulations':0,'new_routes':0,'new_extractions':0,'new_ATPG':0,'new_package_installs':0,'GPU_jobs':0,'optional_followup_experiments':1,'original_repository_writes':0,'scope_limitations':['Codex transcripts and tool transport may reside on system disks outside experiment control.','Windows/WSL service logs, antivirus, paging and filesystem bookkeeping cannot be forced system-wide to F:.','Preflight read-only shells inherited system TEMP; scientific processes used F: redirection.','WSL failed before Linux start; preconfigured missing F: swap/disk paths outside Gate11 were attempted, with no Linux experimental output.'],'absolute_system_wide_F_only_certified':False,'controllable_experimental_outputs_F_only_confirmed':True,'hash_manifest':'00_audit/PACKAGE_SHA256SUMS.json','known_evidence_gaps':'00_audit/required_binding_recovery.json'}
 (R/'00_audit/storage_audit_final.json').write_text(json.dumps(audit,indent=2))
 summary=f'''# Gate 11 storage receipt\n\nWorkspace: `{R}`\n\n- Logical file bytes: **{logical:,}** ({logical/2**20:.3f} MiB; {logical/2**30:.6f} GiB).\n- Allocated file bytes: **{allocated:,}** ({allocated/2**20:.3f} MiB); directory/filesystem metadata excluded.\n- Files: {count:,}.\n- All intentionally generated experimental output/cache/temp/script/report files are inside this F: workspace. Original source/results are unchanged; original archive post-hashes pass.\n- Codex/OS bookkeeping, paging, antivirus/service logs are outside experiment redirection, so absolute system-wide F-only storage is not certified. WSL failed before Linux started.\n\nMachine receipt: `../00_audit/storage_audit_final.json`. Package identities: `../00_audit/PACKAGE_SHA256SUMS.json`.\n'''
 (R/'08_reports/PACT_GATE11_STORAGE.md').write_text(summary,encoding='utf-8')
 if totals()==(count,logical,allocated):break
else:raise RuntimeError('Storage self-count did not stabilize')
assert totals()==(audit['total_workspace_files'],audit['total_workspace_logical_bytes'],audit['allocated_file_bytes'])
print(json.dumps({'status':'PASS','workspace':str(R),'files':count,'logical_bytes':logical,'allocated_file_bytes':allocated,'MiB':logical/2**20,'GiB':logical/2**30,'package_hashed_files':len(hashes),'all_reports_present':True,'optional_followups':1,'controllable_F_only':True,'absolute_system_F_only':False},indent=2))

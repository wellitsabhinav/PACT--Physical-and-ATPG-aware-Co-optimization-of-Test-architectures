import os,sys,pathlib,json,subprocess,time,datetime,ctypes,ctypes.wintypes as w,hashlib
R=pathlib.Path(r'F:\Research\PACT\Gate11')
def disk(): return sum(p.stat().st_size for p in R.rglob('*') if p.is_file())
name=sys.argv[1]; cmd=sys.argv[2:]
manifest=R/'10_logs'/f'{name}.manifest.json'
if manifest.exists(): raise RuntimeError('Refusing to overwrite run '+name)
record={'name':name,'command':cmd,'cwd':str(R),'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'STARTED','environment':{k:os.environ.get(k) for k in ['TEMP','TMP','TMPDIR','PIP_CACHE_DIR','XDG_CACHE_HOME','XDG_CONFIG_HOME','PYTHONPYCACHEPREFIX','PYTHONDONTWRITEBYTECODE','MPLCONFIGDIR','NUMBA_CACHE_DIR','HOME','OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']},'disk_before_bytes':disk()}
record['command_file_hashes']={a:hashlib.sha256(pathlib.Path(a).read_bytes()).hexdigest() for a in cmd if pathlib.Path(a).is_file()}
manifest.write_text(json.dumps(record,indent=2)); start=time.monotonic()
with open(R/'10_logs'/f'{name}.log','w',encoding='utf-8') as log:
 p=subprocess.Popen(cmd,cwd=R,stdout=log,stderr=subprocess.STDOUT,env=os.environ.copy()); p.wait()
 class MC(ctypes.Structure): _fields_=[('cb',w.DWORD),('faults',w.DWORD)]+[(k,ctypes.c_size_t) for k in ['PeakWorkingSetSize','WorkingSetSize','QuotaPeakPagedPoolUsage','QuotaPagedPoolUsage','QuotaPeakNonPagedPoolUsage','QuotaNonPagedPoolUsage','PagefileUsage','PeakPagefileUsage']]
 mc=MC(); mc.cb=ctypes.sizeof(mc)
 ok=ctypes.windll.psapi.GetProcessMemoryInfo(w.HANDLE(int(p._handle)),ctypes.byref(mc),mc.cb)
 ft=[w.FILETIME() for _ in range(4)]
 cpuok=ctypes.windll.kernel32.GetProcessTimes(w.HANDLE(int(p._handle)),*[ctypes.byref(f) for f in ft])
 def secs(f): return (f.dwHighDateTime*2**32+f.dwLowDateTime)/1e7
 record.update(returncode=p.returncode,status='PASS' if p.returncode==0 else 'FAILED',completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),wall_seconds=time.monotonic()-start,cpu_seconds=secs(ft[2])+secs(ft[3]) if cpuok else None,peak_working_set_bytes=int(mc.PeakWorkingSetSize) if ok else None,disk_after_bytes=disk())
 manifest.write_text(json.dumps(record,indent=2))
print(json.dumps(record,indent=2))
print((R/'10_logs'/f'{name}.log').read_text()[-6000:])
sys.exit(p.returncode)

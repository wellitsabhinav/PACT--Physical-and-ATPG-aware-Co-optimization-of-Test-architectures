import pathlib,json,subprocess,sys,os,hashlib,ctypes,ctypes.wintypes as w,importlib.metadata,datetime
R=pathlib.Path(r'F:\Research\PACT\Gate11')
class MS(ctypes.Structure): _fields_=[('dwLength',w.DWORD),('dwMemoryLoad',w.DWORD)]+[(k,ctypes.c_ulonglong) for k in ['ullTotalPhys','ullAvailPhys','ullTotalPageFile','ullAvailPageFile','ullTotalVirtual','ullAvailVirtual','ullAvailExtendedVirtual']]
m=MS();m.dwLength=ctypes.sizeof(m);ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
cmds=[[r'D:\Compiler Cpp\ucrt64\bin\zstd.exe','--version'],[r'C:\WINDOWS\system32\tar.exe','--version'],[r'D:\Compiler Cpp\ucrt64\bin\iverilog.exe','-V'],[r'D:\Compiler Cpp\ucrt64\bin\vvp.exe','-V']]
t=[]
for cmd in cmds:
 try:
  x=subprocess.run(cmd,cwd=R,capture_output=True,timeout=15,env=os.environ.copy()); output=(x.stdout+x.stderr).decode(errors='replace'); (R/'10_logs'/('version_'+pathlib.Path(cmd[0]).stem+'.log')).write_text(output)
  t.append({'command':cmd,'returncode':x.returncode,'version_first_line':output.splitlines()[0] if output.splitlines() else None,'sha256':hashlib.file_digest(open(cmd[0],'rb'),'sha256').hexdigest(),'experimental_use':'archive decompression only' if 'zstd' in cmd[0] else 'capability/version audit only'})
 except Exception as e: t.append({'command':cmd,'error':str(e)})
packages={}
for p in ['numpy','pandas','scipy','matplotlib','numba','jsonschema']:
 try: packages[p]=importlib.metadata.version(p)
 except importlib.metadata.PackageNotFoundError: packages[p]=None
report={'observed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'python':sys.version,'python_executable':sys.executable,'python_sha256':hashlib.file_digest(open(sys.executable,'rb'),'sha256').hexdigest(),'logical_cpus':os.cpu_count(),'RAM_total_bytes':m.ullTotalPhys,'RAM_available_bytes':m.ullAvailPhys,'serial_analysis_threads':1,'packages':packages,'native_tools':t,'WSL_scientific_runtime':'BLOCKED ERROR_PATH_NOT_FOUND: missing ext4.vhdx, failed swap path; no Linux process started','OpenROAD_current':'not on Windows PATH; qualified WSL binary inaccessible','new_simulations':0,'new_routes':0,'new_extractions':0,'new_ATPG':0,'GPU_jobs':0,'new_package_installs':0,'environment':{k:os.environ.get(k) for k in ['TEMP','TMP','TMPDIR','PIP_CACHE_DIR','XDG_CACHE_HOME','XDG_CONFIG_HOME','PYTHONPYCACHEPREFIX','MPLCONFIGDIR','NUMBA_CACHE_DIR','HOME']}}
(R/'00_audit/current_tool_audit.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))

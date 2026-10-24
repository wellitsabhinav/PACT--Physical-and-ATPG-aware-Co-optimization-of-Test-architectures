import json,pathlib,hashlib,subprocess,tarfile,datetime,time,collections,os
ROOT=pathlib.Path(r'F:\Research\PACT\Gate11')
rows=json.loads((ROOT/'00_audit/archive_inventory.json').read_text())
selected=[]
allowed={'AGENTS.md','README.md','pyproject.toml','requirements.txt','src','scripts','docs','reports','results','artifacts','benchmarks','config','experiments','archives','patches'}
for r in rows:
 p=r['RelativePath'].replace('\\','/')
 bits=p.split('/')
 if r['SourceID']=='S008' and len(bits)>1 and bits[0]=='PACT' and bits[1] in allowed and r['Kind']=='file':
  if '__pycache__' in bits or p.endswith(('.pyc','.png','.svg','.pdf','.def','.odb')): continue
  selected.append(r)
(ROOT/'00_audit/selected_inputs_manifest.json').write_text(json.dumps(selected,indent=1))
by_archive=collections.defaultdict(dict)
for r in selected: by_archive[r['ArchivePath']][r['ArchiveMember']]=r
checks={}
for line in pathlib.Path(r'F:\Research_Archives\AUDIT_REPORTS\archive_checksums.sha256').read_text().splitlines():
 if '  ' in line:
  h,p=line.split('  ',1); checks[p]=h
receipts=[]
for archive,wanted in by_archive.items():
 print('EXTRACT',archive,'files',len(wanted),'bytes',sum(int(r['LogicalBytes']) for r in wanted.values()),flush=True)
 start=time.time(); h=hashlib.file_digest(open(archive,'rb'),'sha256').hexdigest()
 if h!=checks.get(archive): raise RuntimeError(('archive checksum',archive,h,checks.get(archive)))
 proc=subprocess.Popen([r'D:\Compiler Cpp\ucrt64\bin\zstd.exe','-dc',archive],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 got=0
 try:
  with tarfile.open(fileobj=proc.stdout,mode='r|') as tf:
   for m in tf:
    r=wanted.get(m.name)
    if r is None: continue
    if not m.isfile(): raise RuntimeError(('not regular',m.name))
    rel=pathlib.PurePosixPath(m.name)
    if rel.is_absolute() or '..' in rel.parts: raise RuntimeError(m.name)
    dest=ROOT/'01_inputs'/'S008'/pathlib.Path(*rel.parts)
    dest.parent.mkdir(parents=True,exist_ok=True)
    if dest.exists(): raise RuntimeError(('would overwrite',str(dest)))
    data=tf.extractfile(m).read()
    if hashlib.sha256(data).hexdigest()!=r['SHA256']: raise RuntimeError(('member checksum',m.name))
    dest.write_bytes(data); got+=1
    if got==len(wanted): break
 finally:
  proc.terminate(); proc.wait(); proc.stdout.close(); err=proc.stderr.read().decode(errors='replace'); proc.stderr.close()
 if got!=len(wanted): raise RuntimeError(('missing',got,len(wanted)))
 rec={'archive':archive,'sha256':h,'archive_hash_verified':True,'extracted_regular_files':got,'elapsed_seconds':time.time()-start,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'links_created':0}
 receipts.append(rec); print(rec,flush=True)
 (ROOT/'00_audit/extraction_receipts.json').write_text(json.dumps(receipts,indent=2))
print('DONE',len(selected),flush=True)

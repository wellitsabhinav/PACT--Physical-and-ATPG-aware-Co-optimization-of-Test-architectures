import json,pathlib,collections,hashlib,subprocess,tarfile,time
R=pathlib.Path(r'F:\Research\PACT\Gate11'); P=R/'01_inputs/S008/PACT'
inv=json.load(open(R/'00_audit/archive_inventory.json')); req=json.load(open(R/'00_audit/required_binding_recovery.json'))
extra=[x['entry'] for x in req['recoverable'] if not x['staged']]
for name in json.load(open(P/'reports/repository_cleanup/retained_evidence_sha256.json')):
 dest=P/pathlib.Path(name)
 if not dest.exists():
  candidates=[x for x in inv if x['SourceID']=='S008' and x['RelativePath'].replace('\\','/')=='PACT/'+name.replace('\\','/') and x['Kind']=='file']
  extra.extend(candidates)
by=collections.defaultdict(dict)
for x in extra: by[x['ArchivePath']][x['ArchiveMember']]=x
receipts=[]
for archive,items in by.items():
 p=subprocess.Popen([r'D:\Compiler Cpp\ucrt64\bin\zstd.exe','-dc',archive],stdout=subprocess.PIPE,stderr=subprocess.DEVNULL); got=0
 try:
  with tarfile.open(fileobj=p.stdout,mode='r|') as tf:
   for m in tf:
    if m.name not in items: continue
    x=items[m.name]; rel=pathlib.PurePosixPath(m.name)
    assert m.isfile() and not rel.is_absolute() and '..' not in rel.parts
    dest=R/'01_inputs'/x['SourceID']/pathlib.Path(*rel.parts)
    assert not dest.exists()
    data=tf.extractfile(m).read(); assert hashlib.sha256(data).hexdigest()==x['SHA256']
    dest.parent.mkdir(parents=True,exist_ok=True); dest.write_bytes(data); got+=1
    receipts.append({'path':str(dest),'sha256':x['SHA256'],'archive':archive,'member':m.name,'bytes':len(data)})
    if got==len(items): break
 finally: p.terminate(); p.wait(); p.stdout.close()
 assert got==len(items)
(R/'00_audit/additional_extraction_receipts.json').write_text(json.dumps(receipts,indent=2)); print('Recovered additional',len(receipts),'bytes',sum(x['bytes'] for x in receipts))

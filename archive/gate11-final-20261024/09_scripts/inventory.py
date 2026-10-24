import csv,json,collections,pathlib,sys,importlib.util
root=pathlib.Path(r'F:\Research\PACT\Gate11')
rows=[]
with open(r'F:\Research_Archives\AUDIT_REPORTS\archive_manifest.csv',encoding='utf-8-sig',newline='') as f:
 for r in csv.DictReader(f):
  if r['Project']=='PACT': rows.append(r)
(root/'00_audit/archive_inventory.json').write_text(json.dumps(rows,indent=1),encoding='utf-8')
counts=collections.defaultdict(lambda:[0,0])
for r in rows:
 key=(r['SourceID'],r['RelativePath'].replace('\\','/').split('/')[0])
 counts[key][0]+=1; counts[key][1]+=int(r['LogicalBytes'] or 0)
summary=[{'source':k[0],'top':k[1],'count':v[0],'bytes':v[1]} for k,v in sorted(counts.items())]
(root/'00_audit/archive_inventory_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print('Python',sys.version,'zstandard available',importlib.util.find_spec('zstandard') is not None)
for r in summary:
 if r['source'] in ['S008','S002','W003','W004','W005']: print(r)
print('GUIDANCE',[(r['SourceID'],r['RelativePath'],r['ArchiveMember']) for r in rows if r['RelativePath'].replace('\\','/').split('/')[-1]=='AGENTS.md'])
print('GATE10',[(r['SourceID'],r['RelativePath'],r['LogicalBytes']) for r in rows if 'gate10' in r['RelativePath'].lower() and r['SourceID']=='S008'][:90])

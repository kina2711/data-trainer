#!/usr/bin/env python3
import argparse,re
from collections import defaultdict
from promote_da_l006_l080_notes import PACK,load
BANNED=('trong bối cảnh hiện đại','đóng vai trò quan trọng','không chỉ là một','trong thế giới ngày nay','một cách toàn diện')
def pars(t):
 t=re.sub(r'^---\n.*?\n---\n','',t,flags=re.S);return [re.sub(r'\s+',' ',p.strip()) for p in re.split(r'\n\s*\n',t) if len(re.sub(r'\s+',' ',p.strip()))>=240 and not p.lstrip().startswith(('|','#','- ','1. '))]
def main(s,e):
 fail=[];seen=defaultdict(list);counts=[]
 for n in range(s,e+1):
  x=load(n);p=PACK/x.filename;t=p.read_text() if p.exists() else '';counts.append(len(re.findall(r'\b\w+[\w-]*\b',t,re.U)))
  for m in ('editorial_pass: humanized-v3','concept_key_status: proposed','## Nỗi Đau & Động Lực','## Cơ Chế Tác Động','## Bản Đồ Quyết Định','## Góc Khuất & Ngộ Nhận','**Hiểu lầm:**','**Thực tế:**','**Vì sao nghe hợp lý:**','## Tự Kiểm Tra Nhanh','## Reference','## Source coverage'):
   if m not in t:fail.append(f'L{n}: missing {m}')
  if counts[-1]<1800:fail.append(f'L{n}: {counts[-1]} words')
  if not x.wiki.exists() or x.wiki.read_bytes()!=p.read_bytes():fail.append(f'L{n}: wiki differs')
  c=(x.folder/'note.md').read_text().lower()
  if 'chua-viet' in c or 'chưa viết' in c:fail.append(f'L{n}: skeleton')
  local=set()
  for q in pars(t):
   if q in local:fail.append(f'L{n}: repeated paragraph')
   local.add(q);seen[q].append(n)
  for b in BANNED:
   if b in t.lower():fail.append(f'L{n}: canned {b}')
 for q,own in seen.items():
  if len(set(own))>1:fail.append(f'cross-note repeat {sorted(set(own))}: {q[:60]}')
 if fail:print('FAIL\n'+'\n'.join('- '+x for x in fail));return 1
 print(f'PASS lessons={e-s+1} range={s:03d}-{e:03d} min_words={min(counts)} max_words={max(counts)} wiki_parity={e-s+1}/{e-s+1} editorial=humanized-v3 repeats=0');return 0
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('start',type=int);p.add_argument('end',type=int);a=p.parse_args();raise SystemExit(main(a.start,a.end))

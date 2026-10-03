#!/usr/bin/env python3
import argparse,re
from collections import defaultdict
from build_remaining_18_book_packs import BOOKS,PACK
BANNED=('trong bối cảnh hiện đại','đóng vai trò quan trọng','không chỉ là một','trong thế giới ngày nay','một cách toàn diện')
def paragraphs(t):
 t=re.sub(r'^---\n.*?\n---\n','',t,flags=re.S);return [re.sub(r'\s+',' ',p.strip()) for p in re.split(r'\n\s*\n',t) if len(re.sub(r'\s+',' ',p.strip()))>=240 and not p.lstrip().startswith(('|','#','- ','1. '))]
def validate(indices):
 fail=[];seen=defaultdict(list);counts=[]
 for bi in indices:
  b=BOOKS[bi-1]
  for i,(s,t,c) in enumerate(b.topics,1):
   p=PACK/b.key/f'{i:02d}-{s}.md';txt=p.read_text() if p.exists() else '';w=len(re.findall(r'\b\w+[\w-]*\b',txt,re.U));counts.append(w)
   for x in ('editorial_pass: humanized-v3','concept_key_status: proposed','## Nỗi Đau & Động Lực','## Cơ Chế Tác Động','## Bản Đồ Quyết Định','## Góc Khuất & Ngộ Nhận','**Hiểu lầm:**','**Thực tế:**','**Vì sao nghe hợp lý:**','## Tự Kiểm Tra Nhanh','## Reference','## Source coverage'):
    if x not in txt:fail.append(f'{b.key}/{s}: missing {x}')
   if w<1800:fail.append(f'{b.key}/{s}: only {w} words')
   local=set()
   for q in paragraphs(txt):
    if q in local:fail.append(f'{b.key}/{s}: repeated paragraph')
    local.add(q);seen[q].append(f'{b.key}/{s}')
   for x in BANNED:
    if x in txt.lower():fail.append(f'{b.key}/{s}: canned {x}')
 for q,owners in seen.items():
  if len(set(owners))>1:fail.append(f'cross-note repeat {owners[:4]}: {q[:70]}')
 if fail:print('FAIL\n'+'\n'.join('- '+x for x in fail));return 1
 print(f'PASS books={len(indices)} notes={len(counts)} min_words={min(counts)} max_words={max(counts)} humanized=all repeats=0');return 0
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('indices',nargs='*',type=int);a=p.parse_args();raise SystemExit(validate(a.indices or list(range(1,19))))

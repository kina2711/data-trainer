#!/usr/bin/env python3
import re
from promote_l241_l245_notes import LESSONS,PACK,ROOT,WIKI,folder
def ids(t):
 m=re.search(r'(?ms)^source_ids:\n(.*?)(?=^[a-z_]+:|^---$)',t);return re.findall(r'(?m)^\s*-\s+(\S+)$',m.group(1)) if m else []
def main():
 f=[];known=set()
 for p in (ROOT/'Docs/Second-Brain/1_Nguon').rglob('*.md'):
  m=re.search(r'(?m)^source_id:\s*(\S+)$',p.read_text());known.add(m.group(1)) if m else None
 req={241:('Ba lớp thay đổi','Quarantine envelope','cursor/primary key'),242:('Bốn tầng oracle','Canonicalization','count-only'),243:('SLI từ consumer deadline','Backfill là workload khác','Admission và isolation'),244:('hard gates','Proof of concept','exit'),245:('Ba nguồn có semantics khác','Failure campaign','Điều kiện bảo vệ')}
 pre='# Phase 7: Ingestion, Transformation, Quality and Governance\n# Module 16: Data Ingestion and Integration Engineering\n'
 for x in LESSONS:
  r=PACK/x.filename
  if not r.exists():f.append(f'L{x.number}: thiếu Reference');continue
  t=r.read_text();n=(folder(x)/'note.md').read_text();a=(folder(x)/'after-note.md').read_text();e=pre+f'# Lesson {x.number}: {x.title}\n'
  if not n.startswith(e) or not a.startswith(e):f.append(f'L{x.number}: sai hierarchy')
  w=len(re.findall(r'\b\w+[\w-]*\b',t,re.UNICODE))
  if w<2200:f.append(f'L{x.number}: chỉ có {w} từ')
  for h in ('## Reference','## Source coverage','## Key takeaways','## 7. Ma trận kiểm chứng từng mệnh đề','## 9. Câu hỏi tự kiểm tra','## 10. Giới hạn và điều chưa cho phép kết luận'):
   if h not in t:f.append(f'L{x.number}: thiếu {h}')
  for q in req[x.number]:
   if q.lower() not in t.lower():f.append(f'L{x.number}: thiếu distinction {q}')
  u=set(ids(t))-known
  if u:f.append(f'L{x.number}: source lạ {sorted(u)}')
  wp=WIKI/f'{x.title}.md'
  if not wp.exists() or wp.read_bytes()!=r.read_bytes():f.append(f'L{x.number}: Wiki lệch Reference')
  for q in ('quiz.md','homework.md','slides.md','lesson.yaml'):
   if not (folder(x)/q).exists():f.append(f'L{x.number}: mất {q}')
 if f:print('FAIL\n'+'\n'.join('- '+x for x in f));return 1
 print('PASS lessons=5 curriculum_files=10 knowledge_notes=5 min_words=2200 wiki_parity=5/5 drift-reconciliation-slo-connector-capstone=checked');return 0
if __name__=='__main__':raise SystemExit(main())

#!/usr/bin/env python3
import re
from promote_l256_l260_notes import LESSONS
from promote_l251_l270_common import PACK,ROOT,WIKI,folder
REQ={256:("failing rows","Threshold","bảng rỗng"),257:("Counterexample shape","Independent oracle","Mutation"),258:("compiled SQL","Abstraction","Interface contract"),259:("Ba điều kiện","equivalence","hard deletes"),260:("Append","Merge","Insert overwrite","Microbatch")}
def main():
 f=[]; known=set()
 for p in (ROOT/'Docs/Second-Brain/1_Nguon').rglob('*.md'):
  m=re.search(r'(?m)^source_id:\s*(\S+)$',p.read_text()); known.add(m.group(1)) if m else None
 for x in LESSONS:
  r=PACK/x.filename
  if not r.exists(): f.append(f'L{x.number}: thiếu Reference'); continue
  t=r.read_text(); w=len(re.findall(r'\b\w+[\w-]*\b',t,re.UNICODE))
  if w<2200:f.append(f'L{x.number}: chỉ có {w} từ')
  for h in ('## Reference','## Source coverage','## Key takeaways','## 7. Ma trận kiểm chứng từng mệnh đề','## 9. Câu hỏi tự kiểm tra','## 10. Giới hạn và điều chưa cho phép kết luận'):
   if h not in t:f.append(f'L{x.number}: thiếu {h}')
  for q in REQ[x.number]:
   if q.lower() not in t.lower():f.append(f'L{x.number}: thiếu distinction {q}')
  u=set(re.findall(r'(?m)^\s*-\s+(src\.\S+)$',t))-known
  if u:f.append(f'L{x.number}: source lạ {sorted(u)}')
  wp=WIKI/f'{x.title}.md'
  if not wp.exists() or wp.read_bytes()!=r.read_bytes():f.append(f'L{x.number}: Wiki lệch Reference')
  if not (folder(x)/'note.md').read_text().startswith(f'# Phase 7: Ingestion, Transformation, Quality and Governance\n# Module 17: ELT, dbt and Workflow Orchestration\n# Lesson {x.number}: {x.title}\n'):f.append(f'L{x.number}: sai hierarchy')
 if f:print('FAIL\n'+'\n'.join('- '+x for x in f));return 1
 print('PASS lessons=5 min_words=2200 wiki_parity=5/5 tests-macros-incremental-strategies=checked');return 0
if __name__=='__main__':raise SystemExit(main())

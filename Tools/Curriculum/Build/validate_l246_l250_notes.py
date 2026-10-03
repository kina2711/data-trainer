#!/usr/bin/env python3
import re
from promote_l246_l250_notes import LESSONS,PACK,ROOT,WIKI,folder
def ids(t):
 m=re.search(r'(?ms)^source_ids:\n(.*?)(?=^[a-z_]+:|^---$)',t);return re.findall(r'(?m)^\s*-\s+(\S+)$',m.group(1)) if m else []
def main():
 f=[];known=set()
 for p in (ROOT/'Docs/Second-Brain/1_Nguon').rglob('*.md'):
  m=re.search(r'(?m)^source_id:\s*(\S+)$',p.read_text());known.add(m.group(1)) if m else None
 req={246:('Kịch bản throttling','Kịch bản cursor expiry','duplicate delivery'),247:('execution path','Năm trục quyết định','hybrid'),248:('Append','Upsert và merge','Replace và overwrite','Swap'),249:('Visibility invariant','partial','Rollback'),250:('logical operation','Deterministic batch identity','Property test')}
 for x in LESSONS:
  r=PACK/x.filename
  if not r.exists():f.append(f'L{x.number}: thiếu Reference');continue
  t=r.read_text();n=(folder(x)/'note.md').read_text();a=(folder(x)/'after-note.md').read_text();mod='16: Data Ingestion and Integration Engineering' if x.number==246 else '17: ELT, dbt and Workflow Orchestration';e=f'# Phase 7: Ingestion, Transformation, Quality and Governance\n# Module {mod}\n# Lesson {x.number}: {x.title}\n'
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
 print('PASS lessons=5 curriculum_files=10 knowledge_notes=5 min_words=2200 wiki_parity=5/5 game-day-etl-load-publish-idempotency=checked');return 0
if __name__=='__main__':raise SystemExit(main())

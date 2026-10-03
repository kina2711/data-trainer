#!/usr/bin/env python3
import re
from promote_l231_l235_notes import LESSONS,PACK,ROOT,WIKI,folder
def ids(t):
 m=re.search(r'(?ms)^source_ids:\n(.*?)(?=^[a-z_]+:|^---$)',t);return re.findall(r'(?m)^\s*-\s+(\S+)$',m.group(1)) if m else []
def main():
 f=[];known=set()
 for p in (ROOT/'Docs/Second-Brain/1_Nguon').rglob('*.md'):
  m=re.search(r'(?m)^source_id:\s*(\S+)$',p.read_text());known.add(m.group(1)) if m else None
 req={231:('Tám nhóm','sentinel','grain','unknown'),232:('Hard delete','Soft delete','before/after','validity interval'),233:('Full snapshot','High watermark','Log CDC','File delivery'),234:('Năm giả định','Composite cursor','Overlap window','Checkpoint ordering'),235:('Offset pagination','Keyset pagination','Opaque cursor','200-with-error')}
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
  wpath=WIKI/f'{x.title}.md'
  if not wpath.exists() or wpath.read_bytes()!=r.read_bytes():f.append(f'L{x.number}: Wiki lệch Reference')
  for q in ('quiz.md','homework.md','slides.md','lesson.yaml'):
   if not (folder(x)/q).exists():f.append(f'L{x.number}: mất {q}')
 if f:print('FAIL\n'+'\n'.join('- '+x for x in f));return 1
 print('PASS lessons=5 curriculum_files=10 knowledge_notes=5 min_words=2200 wiki_parity=5/5 ingestion-discovery-watermark-pagination=checked');return 0
if __name__=='__main__':raise SystemExit(main())

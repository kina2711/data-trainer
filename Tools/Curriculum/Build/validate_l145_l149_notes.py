#!/usr/bin/env python3
"""Validate L145-L149 depth, lineage, curriculum shape and Wiki parity."""
from __future__ import annotations
import re
from promote_l145_l149_notes import ROOT, PACK, WIKI, SPECS, folder
def ids(t):
 m=re.search(r'(?ms)^source_ids:\n(.*?)(?=^[a-z_]+:|^---$)',t)
 return re.findall(r'(?m)^\s*-\s+(\S+)$',m.group(1)) if m else []
def main():
 fail=[]; known=set()
 for p in (ROOT/'Docs/Second-Brain/1_Nguon').rglob('*.md'):
  m=re.search(r'(?m)^source_id:\s*(\S+)$',p.read_text())
  if m: known.add(m.group(1))
 for s in SPECS:
  kp=PACK/s.k.filename; k=kp.read_text(); wp=WIKI/(s.k.title+'.md'); n=(folder(s)/'note.md').read_text(); a=(folder(s)/'after-note.md').read_text()
  pre=f'# Phase {s.phase}: {s.phase_title}\n# Module {s.module}: {s.module_title}\n# Lesson {s.k.number}: {s.k.title}\n'
  if not n.startswith(pre) or not a.startswith(pre): fail.append(f'L{s.k.number}: hierarchy')
  if len(re.findall(r'\b\w+[\w-]*\b',k,re.UNICODE))<1800: fail.append(f'L{s.k.number}: dưới 1800 từ')
  for h in ('## Reference','## Source coverage','## Key takeaways','## 9. Câu hỏi tự kiểm tra','## 10. Giới hạn và điều chưa cho phép kết luận'):
   if h not in k: fail.append(f'L{s.k.number}: thiếu {h}')
  for bad in ('trang_thai: chua-viet','Trạng thái: chưa viết','thoi_luong_phut:','## I. Mục tiêu'):
   if bad in n+a: fail.append(f'L{s.k.number}: scaffold {bad}')
  if set(ids(k))-known: fail.append(f'L{s.k.number}: source ID lạ')
  if not wp.exists() or wp.read_bytes()!=kp.read_bytes(): fail.append(f'L{s.k.number}: Wiki lệch')
 if fail: print('FAIL\n'+'\n'.join('- '+x for x in fail)); return 1
 print('PASS lessons=5 files=10 knowledge_notes=5 min_words=1800 wiki_parity=5/5'); return 0
if __name__=='__main__': raise SystemExit(main())

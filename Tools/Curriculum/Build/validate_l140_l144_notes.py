#!/usr/bin/env python3
"""Validate L140-L144 lineage, depth, curriculum shape and Wiki parity."""
from __future__ import annotations
import re
from promote_l140_l144_notes import BASE, LESSONS, PACK, ROOT, WIKI

def source_ids(text):
    m=re.search(r"(?ms)^source_ids:\n(.*?)(?=^[a-z_]+:|^---$)",text)
    return re.findall(r"(?m)^\s*-\s+(\S+)$",m.group(1)) if m else []

def main():
    failures=[]; known=set()
    for p in (ROOT/'Docs/Second-Brain/1_Nguon').rglob('*.md'):
        m=re.search(r"(?m)^source_id:\s*(\S+)$",p.read_text())
        if m: known.add(m.group(1))
    for x in LESSONS:
        kp=PACK/x.filename; k=kp.read_text(); wp=WIKI/(x.title+'.md')
        n=(BASE/x.directory/'note.md').read_text(); a=(BASE/x.directory/'after-note.md').read_text()
        prefix=f"# Phase 4: SQL and Database Internals\n# Module 10: Storage Engine and Database Operations\n# Lesson {x.number}: {x.title}\n"
        if not n.startswith(prefix) or not a.startswith(prefix): failures.append(f'L{x.number}: hierarchy')
        if len(re.findall(r"\b\w+\b",k,re.UNICODE))<1800: failures.append(f'L{x.number}: dưới 1800 từ')
        for h in ('## Reference','## Source coverage','## Key takeaways','## 9. Câu hỏi tự kiểm tra','## 10. Giới hạn và điều chưa cho phép kết luận'):
            if h not in k: failures.append(f'L{x.number}: thiếu {h}')
        for bad in ('trang_thai: chua-viet','Trạng thái: chưa viết','thoi_luong_phut:','## I. Mục tiêu'):
            if bad in n+a: failures.append(f'L{x.number}: scaffold {bad}')
        for h in ('## Thực hành','## Kiểm tra cuối bài','## Tiêu chí hoàn thành','## Bài làm sau buổi học','## Reference'):
            if h not in a: failures.append(f'L{x.number}: after thiếu {h}')
        unknown=set(source_ids(k))-known
        if unknown: failures.append(f'L{x.number}: source ID lạ {sorted(unknown)}')
        if not wp.exists() or wp.read_bytes()!=kp.read_bytes(): failures.append(f'L{x.number}: Wiki lệch')
    if failures:
        print('FAIL\n'+'\n'.join('- '+x for x in failures)); return 1
    print('PASS lessons=5 files=10 knowledge_notes=5 min_words=1800 wiki_parity=5/5'); return 0
if __name__=='__main__': raise SystemExit(main())

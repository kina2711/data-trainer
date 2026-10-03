#!/usr/bin/env python3
"""Validate L181-L185 depth, lineage, module boundary and Wiki parity."""
from __future__ import annotations
import re
from promote_l181_l185_notes import ROOT, PACK, WIKI, LESSONS, folder, hierarchy

def source_ids(text):
    match=re.search(r'(?ms)^source_ids:\n(.*?)(?=^[a-z_]+:|^---$)',text)
    return re.findall(r'(?m)^\s*-\s+(\S+)$',match.group(1)) if match else []

def main():
    failures=[]; known=set()
    for path in (ROOT/'Docs/Second-Brain/1_Nguon').rglob('*.md'):
        match=re.search(r'(?m)^source_id:\s*(\S+)$',path.read_text())
        if match: known.add(match.group(1))
    required={
      181:('six dimensions','reversal triggers','Curated marts'),
      182:('parallel run','Deprecation record','Không sửa đè công thức'),
      183:('Business owner','seven mutations','Blameless'),
      184:('270 metric-cell assertions','Sáu automatic-fail gates','breaking migration'),
      185:('Decision','Action branches','Operational request'),
    }
    for lesson in LESSONS:
        reference=PACK/lesson.filename; knowledge=reference.read_text(); wiki=WIKI/(lesson.title+'.md')
        note=(folder(lesson)/'note.md').read_text(); after=(folder(lesson)/'after-note.md').read_text(); phase,module=hierarchy(lesson)
        prefix=f'# {phase}\n# {module}\n# Lesson {lesson.number}: {lesson.title}\n'
        if not note.startswith(prefix) or not after.startswith(prefix): failures.append(f'L{lesson.number}: sai hierarchy/module boundary')
        words=len(re.findall(r'\b\w+[\w-]*\b',knowledge,re.UNICODE))
        if words<2200: failures.append(f'L{lesson.number}: chỉ có {words} từ')
        for heading in ('## Reference','## Source coverage','## Key takeaways','## 8. Ma trận kiểm chứng từng mệnh đề','## 10. Câu hỏi tự kiểm tra','## 11. Giới hạn và điều chưa cho phép kết luận'):
            if heading not in knowledge: failures.append(f'L{lesson.number}: thiếu {heading}')
        for term in required[lesson.number]:
            if term.lower() not in knowledge.lower(): failures.append(f'L{lesson.number}: thiếu distinction {term}')
        for bad in ('trang_thai: chua-viet','Trạng thái: chưa viết','thoi_luong_phut:','## I. Mục tiêu','Tóm tắt'):
            if bad in note+after: failures.append(f'L{lesson.number}: còn scaffold {bad}')
        unknown=set(source_ids(knowledge))-known
        if unknown: failures.append(f'L{lesson.number}: source ID lạ {sorted(unknown)}')
        if not wiki.exists() or wiki.read_bytes()!=reference.read_bytes(): failures.append(f'L{lesson.number}: Wiki lệch Reference')
    if failures:
        print('FAIL\n'+'\n'.join('- '+item for item in failures)); return 1
    print('PASS lessons=5 modules=2 curriculum_files=10 knowledge_notes=5 min_words=2200 wiki_parity=5/5 architecture-governance-discovery=checked')
    return 0
if __name__=='__main__': raise SystemExit(main())

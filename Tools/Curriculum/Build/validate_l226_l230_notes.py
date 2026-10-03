#!/usr/bin/env python3
"""Validate L226-L230 depth, lineage, distinctions and Wiki parity."""
from __future__ import annotations
import re
from promote_l226_l230_notes import LESSONS, PACK, ROOT, WIKI, folder

def ids(text):
    match=re.search(r"(?ms)^source_ids:\n(.*?)(?=^[a-z_]+:|^---$)",text)
    return re.findall(r"(?m)^\s*-\s+(\S+)$",match.group(1)) if match else []

def main():
    failures=[]; known=set()
    for path in (ROOT/"Docs/Second-Brain/1_Nguon").rglob("*.md"):
        match=re.search(r"(?m)^source_id:\s*(\S+)$",path.read_text())
        if match: known.add(match.group(1))
    required={226:("publication point","outcome ambiguity","reachability","time travel"),227:("Catalog conflict","File-set conflict","Semantic conflict","Retry budget"),228:("stable field IDs","spec ID","split-plans","drop rồi add"),229:("Snapshot retention","Orphan cleanup","position-delete","maximum write duration"),230:("Evidence pack","critical failure","writer-reader 4-cell","70/100")}
    headings=("## Reference","## Source coverage","## Key takeaways","## 7. Ma trận kiểm chứng từng mệnh đề","## 9. Câu hỏi tự kiểm tra","## 10. Giới hạn và điều chưa cho phép kết luận")
    prefix="# Phase 6: Analytical Storage and Query Engines\n# Module 15: File, Serialization and Open Table Formats\n"
    for lesson in LESSONS:
        ref=PACK/lesson.filename
        if not ref.exists(): failures.append(f"L{lesson.number}: thiếu Reference"); continue
        text=ref.read_text(); note=(folder(lesson)/"note.md").read_text(); after=(folder(lesson)/"after-note.md").read_text(); expected=prefix+f"# Lesson {lesson.number}: {lesson.title}\n"
        if not note.startswith(expected) or not after.startswith(expected): failures.append(f"L{lesson.number}: sai hierarchy")
        words=len(re.findall(r"\b\w+[\w-]*\b",text,re.UNICODE))
        if words<2200: failures.append(f"L{lesson.number}: chỉ có {words} từ")
        for heading in headings:
            if heading not in text: failures.append(f"L{lesson.number}: thiếu {heading}")
        for term in required[lesson.number]:
            if term.lower() not in text.lower(): failures.append(f"L{lesson.number}: thiếu distinction {term}")
        unknown=set(ids(text))-known
        if unknown: failures.append(f"L{lesson.number}: source ID lạ {sorted(unknown)}")
        wiki=WIKI/f"{lesson.title}.md"
        if not wiki.exists() or wiki.read_bytes()!=ref.read_bytes(): failures.append(f"L{lesson.number}: Wiki lệch Reference")
        for name in ("quiz.md","homework.md","slides.md","lesson.yaml"):
            if not (folder(lesson)/name).exists(): failures.append(f"L{lesson.number}: mất {name}")
    if failures: print("FAIL\n"+"\n".join("- "+x for x in failures)); return 1
    print("PASS lessons=5 curriculum_files=10 knowledge_notes=5 min_words=2200 wiki_parity=5/5 iceberg-operations-gate6=checked"); return 0

if __name__=="__main__": raise SystemExit(main())

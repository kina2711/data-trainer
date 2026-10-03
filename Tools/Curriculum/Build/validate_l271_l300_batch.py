#!/usr/bin/env python3
from __future__ import annotations
import importlib
import re
import sys
from promote_l271_l300_common import MODULES, PACK, ROOT, WIKI, folder

def validate(module_name: str, label: str) -> int:
    lessons = importlib.import_module(module_name).LESSONS
    failures=[]; counts=[]; known=set()
    for path in (ROOT / "Docs/Second-Brain/1_Nguon").rglob("*.md"):
        match=re.search(r"(?m)^source_id:\s*(\S+)$",path.read_text())
        if match: known.add(match.group(1))
    for lesson in lessons:
        ref=PACK/lesson.filename
        if not ref.exists(): failures.append(f"L{lesson.number}: missing Reference"); continue
        text=ref.read_text(); words=len(re.findall(r"\b\w+[\w-]*\b",text,re.UNICODE)); counts.append(words)
        if words<2200: failures.append(f"L{lesson.number}: only {words} words")
        for heading in ("## Reference","## Source coverage","## Key takeaways","## 7. Ma trận kiểm chứng từng mệnh đề","## 9. Câu hỏi tự kiểm tra","## 10. Giới hạn và điều chưa cho phép kết luận"):
            if heading not in text: failures.append(f"L{lesson.number}: missing {heading}")
        if "editorial_pass: humanized-v3" not in text: failures.append(f"L{lesson.number}: missing humanizer v3")
        unknown=set(lesson.sources)-known
        if unknown: failures.append(f"L{lesson.number}: unknown sources {sorted(unknown)}")
        wiki=WIKI/f"{lesson.title}.md"
        if not wiki.exists() or wiki.read_bytes()!=ref.read_bytes(): failures.append(f"L{lesson.number}: Wiki differs")
        phase_title=("Ingestion, Transformation, Quality and Governance" if lesson.phase == 7
                     else "Distributed Systems, Streaming and Compute" if lesson.phase == 8
                     else "Cloud Platform and Production Operations" if lesson.phase == 9
                     else "System Design, AI Boundary and Trajectory")
        expected=(f"# Phase {lesson.phase}: {phase_title}\n"
                  f"# Module {lesson.module}: {MODULES[lesson.module][1]}\n# Lesson {lesson.number}: {lesson.title}\n")
        if not (folder(lesson)/"note.md").read_text().startswith(expected): failures.append(f"L{lesson.number}: wrong hierarchy")
    if failures:
        print("FAIL\n"+"\n".join("- "+x for x in failures)); return 1
    print(f"PASS lessons={len(lessons)} min_words={min(counts)} max_words={max(counts)} wiki_parity={len(lessons)}/{len(lessons)} {label}=checked")
    return 0

if __name__=="__main__": raise SystemExit(validate(sys.argv[1],sys.argv[2]))

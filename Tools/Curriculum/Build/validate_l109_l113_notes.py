#!/usr/bin/env python3
"""Validate L109-L113 knowledge, curriculum and Wiki artifacts."""
from __future__ import annotations
import re
from pathlib import Path
from promote_l109_l113_notes import LESSONS, ROOT

WIKI={109:"Docs/Second-Brain/2_Wiki/Distributed-Systems/Transactional Outbox - One Atomic Write.md",110:"Docs/Second-Brain/2_Wiki/Backend-Engineering/Load Testing and Capacity Notes.md",111:"Docs/Second-Brain/2_Wiki/Backend-Engineering/Job Control API Project.md",112:"Docs/Second-Brain/2_Wiki/Software-Engineering/Gate 3 - Correct Service Assessment.md",113:"Docs/Second-Brain/2_Wiki/Database-Systems/Relations Keys and Functional Dependencies.md"}

def ids(text):
    b=re.search(r"(?ms)^source_ids:\n(.*?)(?=^[a-z_]+:|^---$)",text); return re.findall(r"(?m)^\s*-\s+(\S+)$",b.group(1)) if b else []
def main():
    failures=[]; known=set()
    for p in (ROOT/"Docs/Second-Brain/1_Nguon").rglob("*.md"):
        m=re.search(r"(?m)^source_id:\s*(\S+)$",p.read_text(encoding="utf-8"));
        if m: known.add(m.group(1))
    for x in LESSONS:
        d=ROOT/x.directory; n=(d/"note.md").read_text(encoding="utf-8"); a=(d/"after-note.md").read_text(encoding="utf-8"); k=(ROOT/x.source).read_text(encoding="utf-8")
        prefix=f"# Phase {x.phase}: {x.phase_title}\n# Module {x.module}: {x.module_title}\n# Lesson {x.number}: {x.title}\n"
        if not n.startswith(prefix) or not a.startswith(prefix): failures.append(f"L{x.number}: hierarchy")
        for bad in ("trang_thai: chua-viet","Trạng thái: chưa viết","thoi_luong_phut:","## I. Mục tiêu"):
            if bad in n+a: failures.append(f"L{x.number}: scaffold {bad}")
        for h in ("## Mục tiêu bài học","## Source coverage","## Key takeaways","## Reference"):
            if h not in n: failures.append(f"L{x.number}: thiếu {h}")
        for h in ("## Thực hành","## Kiểm tra cuối bài","## Tiêu chí hoàn thành","## Bài làm sau buổi học","## Reference"):
            if h not in a: failures.append(f"L{x.number}: after thiếu {h}")
        if any(s not in known for s in ids(k)): failures.append(f"L{x.number}: source_id lạ")
        if len(re.findall(r"\b\w+\b",k,re.UNICODE))<1100: failures.append(f"L{x.number}: knowledge note ngắn")
        w=ROOT/WIKI[x.number]
        if not w.exists() or w.read_bytes()!=(ROOT/x.source).read_bytes(): failures.append(f"L{x.number}: Wiki lệch")
    if failures: print("FAIL\n"+"\n".join("- "+f for f in failures)); return 1
    print("PASS lessons=5 files=10 knowledge_notes=5"); return 0
if __name__=="__main__": raise SystemExit(main())

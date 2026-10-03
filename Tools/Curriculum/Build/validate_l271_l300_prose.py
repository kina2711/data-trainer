#!/usr/bin/env python3
from __future__ import annotations
import importlib
import re
from collections import defaultdict
from promote_l271_l300_common import PACK

MODULES=("promote_l271_l275_notes","promote_l276_l280_notes","promote_l281_l285_notes","promote_l286_l290_notes","promote_l291_l295_notes","promote_l296_l300_notes")
TELLS=("trong bối cảnh hiện đại","đóng vai trò quan trọng","không chỉ là một","trong thế giới ngày nay","một cách toàn diện")

def paragraphs(text: str):
    body=re.sub(r"^---\n.*?\n---\n","",text,flags=re.S)
    return [re.sub(r"\s+"," ",p.strip()) for p in re.split(r"\n\s*\n",body) if len(re.sub(r"\s+"," ",p.strip()))>=240 and not p.lstrip().startswith(("|","#","- ","1. "))]

def main():
    lessons=[x for name in MODULES for x in importlib.import_module(name).LESSONS]
    failures=[]; global_seen=defaultdict(list); tells=0; within=0
    for lesson in lessons:
        text=(PACK/lesson.filename).read_text(); ps=paragraphs(text); local=set()
        for p in ps:
            if p in local: within+=1; failures.append(f"L{lesson.number}: repeated long paragraph")
            local.add(p); global_seen[p].append(lesson.number)
        for tell in TELLS:
            count=text.lower().count(tell)
            tells+=count
            if count: failures.append(f"L{lesson.number}: canned phrase `{tell}`")
    cross=0
    for paragraph, owners in global_seen.items():
        if len(set(owners))>1:
            cross+=1; failures.append(f"cross-note repeat {sorted(set(owners))}: {paragraph[:90]}")
    if failures:
        print("FAIL\n"+"\n".join("- "+x for x in failures)); return 1
    print(f"PASS checked={len(lessons)} editorial=humanized-v3 within_note_repeats={within} cross_note_repeats={cross} prose_tells={tells}")
    return 0
if __name__=="__main__": raise SystemExit(main())

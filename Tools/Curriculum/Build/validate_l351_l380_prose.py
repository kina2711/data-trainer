#!/usr/bin/env python3
from __future__ import annotations
import importlib,re
from collections import defaultdict
from promote_l271_l300_common import PACK
MODULES=tuple(f"promote_l{x}_l{x+4}_notes" for x in range(351,381,5))
TELLS=("trong bối cảnh hiện đại","đóng vai trò quan trọng","không chỉ là một","trong thế giới ngày nay","một cách toàn diện")
def paragraphs(text):
    text=re.sub(r"^---\n.*?\n---\n","",text,flags=re.S)
    return [re.sub(r"\s+"," ",p.strip()) for p in re.split(r"\n\s*\n",text) if len(re.sub(r"\s+"," ",p.strip()))>=240 and not p.lstrip().startswith(("|","#","- ","1. "))]
def main():
    lessons=[x for m in MODULES for x in importlib.import_module(m).LESSONS]; failures=[]; seen=defaultdict(list); within=tells=0
    for lesson in lessons:
        text=(PACK/lesson.filename).read_text(); local=set()
        for p in paragraphs(text):
            if p in local: within+=1; failures.append(f"L{lesson.number}: repeated long paragraph")
            local.add(p); seen[p].append(lesson.number)
        for tell in TELLS:
            c=text.lower().count(tell); tells+=c
            if c: failures.append(f"L{lesson.number}: canned phrase `{tell}`")
    cross=sum(1 for owners in seen.values() if len(set(owners))>1)
    failures.extend(f"cross-note repeat {sorted(set(owners))}" for owners in seen.values() if len(set(owners))>1)
    if failures: print("FAIL\n"+"\n".join("- "+x for x in failures)); return 1
    print(f"PASS checked={len(lessons)} editorial=humanized-v3 within_note_repeats={within} cross_note_repeats={cross} prose_tells={tells}"); return 0
if __name__=="__main__": raise SystemExit(main())

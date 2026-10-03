#!/usr/bin/env python3
from __future__ import annotations
import importlib,re
from collections import defaultdict
from promote_l271_l300_common import PACK
MODULES=("promote_l401_l405_notes","promote_l406_l410_notes");TELLS=("trong bối cảnh hiện đại","đóng vai trò quan trọng","không chỉ là một","trong thế giới ngày nay","một cách toàn diện")
def paragraphs(text):
 text=re.sub(r"^---\n.*?\n---\n","",text,flags=re.S);return [re.sub(r"\s+"," ",p.strip()) for p in re.split(r"\n\s*\n",text) if len(re.sub(r"\s+"," ",p.strip()))>=240 and not p.lstrip().startswith(("|","#","- ","1. "))]
def main():
 lessons=[x for m in MODULES for x in importlib.import_module(m).LESSONS];fail=[];seen=defaultdict(list);within=tells=0
 for l in lessons:
  text=(PACK/l.filename).read_text();local=set()
  for p in paragraphs(text):
   if p in local:within+=1;fail.append(f"L{l.number}: repeated long paragraph")
   local.add(p);seen[p].append(l.number)
  for tell in TELLS:
   c=text.lower().count(tell);tells+=c
   if c:fail.append(f"L{l.number}: canned phrase `{tell}`")
 cross=sum(1 for o in seen.values() if len(set(o))>1);fail.extend(f"cross-note repeat {sorted(set(o))}" for o in seen.values() if len(set(o))>1)
 if fail:print("FAIL\n"+"\n".join("- "+x for x in fail));return 1
 print(f"PASS checked={len(lessons)} editorial=humanized-v3 within_note_repeats={within} cross_note_repeats={cross} prose_tells={tells}");return 0
if __name__=="__main__":raise SystemExit(main())

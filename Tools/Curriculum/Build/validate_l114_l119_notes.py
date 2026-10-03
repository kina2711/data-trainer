#!/usr/bin/env python3
"""Validate DE L114-L119 artifacts."""
from __future__ import annotations
import re
from pathlib import Path
from promote_l114_l119_notes import LESSONS,ROOT,PACK,folder
WIKI={114:"NULL and Three-Valued Logic.md",115:"Relational Algebra and Logical Equivalence.md",116:"ER Modelling and Database Enforcement.md",117:"Normalization to BCNF and Deliberate Denormalization.md",118:"Logical Query Processing Order.md",119:"Joins Duplicate Multiplication and NULL Behaviour.md"}
def ids(t):
 b=re.search(r"(?ms)^source_ids:\n(.*?)(?=^[a-z_]+:|^---$)",t);return re.findall(r"(?m)^\s*-\s+(\S+)$",b.group(1)) if b else []
def main():
 fail=[];known=set()
 for p in (ROOT/"Docs/Second-Brain/1_Nguon").rglob("*.md"):
  m=re.search(r"(?m)^source_id:\s*(\S+)$",p.read_text(encoding="utf-8"));
  if m:known.add(m.group(1))
 for x in LESSONS:
  n=(folder(x)/"note.md").read_text(encoding="utf-8");a=(folder(x)/"after-note.md").read_text(encoding="utf-8");kp=ROOT/PACK/x.source;k=kp.read_text(encoding="utf-8");prefix=f"# Phase 4: SQL and Database Internals\n# Module 9: Relational Theory and SQL Execution\n# Lesson {x.number}: {x.title}\n"
  if not n.startswith(prefix) or not a.startswith(prefix):fail.append(f"L{x.number}: hierarchy")
  for bad in ("trang_thai: chua-viet","Trạng thái: chưa viết","thoi_luong_phut:","## I. Mục tiêu"):
   if bad in n+a:fail.append(f"L{x.number}: scaffold {bad}")
  for h in ("## Mục tiêu bài học","## Source coverage","## Key takeaways","## Reference"):
   if h not in n:fail.append(f"L{x.number}: thiếu {h}")
  for h in ("## Thực hành","## Kiểm tra cuối bài","## Tiêu chí hoàn thành","## Bài làm sau buổi học","## Reference"):
   if h not in a:fail.append(f"L{x.number}: after thiếu {h}")
  if any(v not in known for v in ids(k)):fail.append(f"L{x.number}: source lạ")
  wp=ROOT/"Docs/Second-Brain/2_Wiki/Database-Systems"/WIKI[x.number]
  if not wp.exists() or wp.read_bytes()!=kp.read_bytes():fail.append(f"L{x.number}: Wiki lệch")
 if fail:print("FAIL\n"+"\n".join("- "+x for x in fail));return 1
 print("PASS lessons=6 files=12 knowledge_notes=6");return 0
if __name__=="__main__":raise SystemExit(main())

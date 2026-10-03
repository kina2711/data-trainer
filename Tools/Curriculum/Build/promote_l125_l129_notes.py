#!/usr/bin/env python3
"""Promote verified L125-L129 knowledge notes into curriculum notes."""
from __future__ import annotations
import argparse,re
from dataclasses import dataclass
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
BASE="Material/DE/Curriculum/Phase_04-sql-and-database-internals/Module_09-relational-theory-and-sql-execution"
PACK="Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01"
@dataclass(frozen=True)
class Lesson: number:int; directory:str; title:str; source:str
LESSONS=(
 Lesson(125,"Lesson_125-dml-ddl-constraints-and-views","DML, DDL, constraints and views","13-dml-ddl-constraints-and-views.md"),
 Lesson(126,"Lesson_126-inside-the-engine-from-parser-to-executor","Inside the engine - from parser to executor","14-inside-the-engine-parser-to-executor.md"),
 Lesson(127,"Lesson_127-physical-operators-and-the-three-join-algorithms","Physical operators and the three join algorithms","15-physical-operators-and-join-algorithms.md"),
 Lesson(128,"Lesson_128-statistics-selectivity-and-cardinality-estimation","Statistics, selectivity and cardinality estimation","16-statistics-selectivity-and-cardinality-estimation.md"),
 Lesson(129,"Lesson_129-indexes-structure-composite-order-and-cost","Indexes - structure, composite order and cost","17-index-structure-composite-order-and-cost.md"),
)
def field(text,name):
 m=re.search(rf"(?m)^\*\*{re.escape(name)}\.\*\*\s*(.+)$",text)
 if not m: raise ValueError(f"Thiếu {name}")
 return m.group(1).strip()
def section(text,h):
 m=re.search(rf"(?ms)^## {re.escape(h)}\n\n(.*?)(?=^## |\Z)",text)
 if not m: raise ValueError(f"Thiếu section {h}")
 return m.group(1).strip()
def strip(text):
 if text.startswith("---\n"): text=text[text.find("\n---\n",4)+5:]
 return re.sub(r"^# .+\n+","",text.strip(),count=1)
def folder(x): return ROOT/BASE/x.directory
def contract(x):
 n=(folder(x)/"note.md").read_text(encoding="utf-8");a=(folder(x)/"after-note.md").read_text(encoding="utf-8")
 if "**Outcome.**" in n:return tuple(field(n,k) for k in ("Outcome","Đánh giá","Lab","Pitfalls","Self-study (2,4 giờ)","Done when"))
 return (field(section(n,"Mục tiêu bài học"),"Năng lực cần chứng minh"),field(section(a,"Tiêu chí hoàn thành"),"Cách đánh giá"),field(section(a,"Thực hành"),"Nhiệm vụ"),field(section(a,"Bài làm sau buổi học"),"Lỗi cần chủ động loại trừ"),field(section(a,"Bài làm sau buổi học"),"Nhiệm vụ"),field(section(n,"Mục tiêu bài học"),"Điều kiện hoàn thành"))
def build(x):
 outcome,assessment,lab,pitfalls,homework,done=contract(x);source=ROOT/PACK/x.source;body=strip(source.read_text(encoding="utf-8"));h=f"# Phase 4: SQL and Database Internals\n# Module 9: Relational Theory and SQL Execution\n# Lesson {x.number}: {x.title}"
 q={125:["Vì sao MERGE chưa tự là idempotent?","NOT VALID và VALIDATE tách rủi ro nào?","View khác materialized view thế nào?","Lock budget cần đo những đại lượng gì?"],126:["Parser khác binder ở lỗi nào?","Rewrite khác planner thế nào?","Cost units có phải milliseconds không?","Tìm node estimation sai đầu tiên ra sao?"],127:["Nested loop phù hợp trường hợp nào?","Hash batches lớn hơn một nói gì?","Index-only scan vẫn fetch heap khi nào?","work_mem nhân theo operations ra sao?"],128:["MCV và histogram giữ thông tin gì?","Giả định độc lập hỏng khi nào?","Extended statistics có ba loại nào?","Error factor được đo ra sao?"],129:["Leftmost rule có skip-scan nuance gì?","INCLUDE khác key columns thế nào?","Vì sao idx_scan bằng zero chưa đủ để drop?","Định lượng read gain và write cost bằng gì?"]}[x.number]
 note=f"{h}\n\n## Mục tiêu bài học\n\n**Năng lực cần chứng minh.** {outcome}\n\n**Điều kiện hoàn thành.** {done}\n\n{body}\n"
 after=f"{h}\n\n## Thực hành\n\n**Nhiệm vụ.** {lab}\n\nLưu SQL, seed/workload, dự đoán trước khi chạy, plan dạng máy đọc được, output thô, đối soát và thông số môi trường. Chỉ chạy DDL/spill/load test trong môi trường cô lập với lock/statement timeout; ảnh chụp không thay artifact tái chạy.\n\n## Kiểm tra cuối bài\n\n"+"\n".join(f"{i}. {v}" for i,v in enumerate(q,1))+f"\n\n## Tiêu chí hoàn thành\n\n**Cách đánh giá.** {assessment}\n\n**Điều kiện đạt.** {done}\n\n## Bài làm sau buổi học\n\n**Nhiệm vụ.** {homework}\n\n**Lỗi cần chủ động loại trừ.** {pitfalls}\n\n## Reference\n\n- Knowledge note: `{source.relative_to(ROOT)}`\n- Nội dung học thuật: `note.md` cùng thư mục.\n"
 return note,after
def main():
 p=argparse.ArgumentParser();p.add_argument("--check",action="store_true");a=p.parse_args();stale=[]
 for x in LESSONS:
  for path,content in zip((folder(x)/"note.md",folder(x)/"after-note.md"),build(x)):
   if a.check:
    if path.read_text(encoding="utf-8")!=content:stale.append(str(path.relative_to(ROOT)))
   else:path.write_text(content,encoding="utf-8")
 if stale:print("STALE\n"+"\n".join(stale));return 1
 print(f"checked={len(LESSONS)*2} stale=0" if a.check else f"written={len(LESSONS)*2}");return 0
if __name__=="__main__":raise SystemExit(main())

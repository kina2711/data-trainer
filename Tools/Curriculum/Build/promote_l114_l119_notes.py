#!/usr/bin/env python3
"""Promote verified L114-L119 knowledge notes into curriculum notes."""
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
 Lesson(114,"Lesson_114-null-and-three-valued-logic","NULL and three-valued logic","02-null-and-three-valued-logic.md"),
 Lesson(115,"Lesson_115-relational-algebra-and-logical-equivalence","Relational algebra and logical equivalence","03-relational-algebra-and-logical-equivalence.md"),
 Lesson(116,"Lesson_116-er-modelling-and-what-the-database-should-enforce","ER modelling and what the database should enforce","04-er-modelling-and-database-enforcement.md"),
 Lesson(117,"Lesson_117-normalization-to-bcnf-and-deliberate-denormalization","Normalization to BCNF, and deliberate denormalization","05-normalization-to-bcnf-and-deliberate-denormalization.md"),
 Lesson(118,"Lesson_118-logical-query-processing-order","Logical query processing order","06-logical-query-processing-order.md"),
 Lesson(119,"Lesson_119-joins-duplicate-multiplication-and-null-behaviour","Joins, duplicate multiplication and NULL behaviour","07-joins-duplicate-multiplication-and-null-behaviour.md"),
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
 n=(folder(x)/"note.md").read_text(encoding="utf-8"); a=(folder(x)/"after-note.md").read_text(encoding="utf-8")
 if "**Outcome.**" in n: return tuple(field(n,k) for k in ("Outcome","Đánh giá","Lab","Pitfalls","Self-study (2,4 giờ)","Done when"))
 return (field(section(n,"Mục tiêu bài học"),"Năng lực cần chứng minh"),field(section(a,"Tiêu chí hoàn thành"),"Cách đánh giá"),field(section(a,"Thực hành"),"Nhiệm vụ"),field(section(a,"Bài làm sau buổi học"),"Lỗi cần chủ động loại trừ"),field(section(a,"Bài làm sau buổi học"),"Nhiệm vụ"),field(section(n,"Mục tiêu bài học"),"Điều kiện hoàn thành"))
def build(x):
 outcome,assessment,lab,pitfalls,homework,done=contract(x); source=ROOT/PACK/x.source; body=strip(source.read_text(encoding="utf-8")); h=f"# Phase 4: SQL and Database Internals\n# Module 9: Relational Theory and SQL Execution\n# Lesson {x.number}: {x.title}"
 q={114:["Vì sao WHERE loại UNKNOWN?","NOT IN có NULL hỏng thế nào?","AVG dùng denominator nào?","Khi nào COALESCE làm sai nghĩa?"],115:["Set và bag semantics khác gì?","Pushdown qua outer join có điều kiện gì?","EXISTS khác inner join thế nào?","Chứng minh equivalence bằng gì?"],116:["Cardinality khác participation thế nào?","M:N cần junction vì sao?","Delete action là policy gì?","Bỏ FK cần controls nào?"],117:["Ba anomaly là gì?","3NF khác BCNF ở đâu?","Lossless khác preservation thế nào?","Denormalization cần writer nào?"],118:["Alias tồn tại ở bước nào?","WHERE khác HAVING thế nào?","Window filter cần query level nào?","Logical khác physical order ra sao?"],119:["Fanout tính thế nào?","LEFT JOIN vẫn nhân row ra sao?","DISTINCT che lỗi grain thế nào?","Reconciliation cần evidence nào?"]}[x.number]
 note=f"{h}\n\n## Mục tiêu bài học\n\n**Năng lực cần chứng minh.** {outcome}\n\n**Điều kiện hoàn thành.** {done}\n\n{body}\n"
 after=f"{h}\n\n## Thực hành\n\n**Nhiệm vụ.** {lab}\n\nLưu SQL, seed data, prediction trước khi chạy, output thô, đối soát và giải thích theo rule. Ảnh chụp không thay artifact chạy lại được.\n\n## Kiểm tra cuối bài\n\n"+"\n".join(f"{i}. {v}" for i,v in enumerate(q,1))+f"\n\n## Tiêu chí hoàn thành\n\n**Cách đánh giá.** {assessment}\n\n**Điều kiện đạt.** {done}\n\n## Bài làm sau buổi học\n\n**Nhiệm vụ.** {homework}\n\n**Lỗi cần chủ động loại trừ.** {pitfalls}\n\n## Reference\n\n- Knowledge note: `{source.relative_to(ROOT)}`\n- Nội dung học thuật: `note.md` cùng thư mục.\n"
 return note,after
def main():
 p=argparse.ArgumentParser();p.add_argument("--check",action="store_true");a=p.parse_args();stale=[]
 for x in LESSONS:
  for path,content in zip((folder(x)/"note.md",folder(x)/"after-note.md"),build(x)):
   if a.check:
    if path.read_text(encoding="utf-8")!=content: stale.append(str(path.relative_to(ROOT)))
   else:path.write_text(content,encoding="utf-8")
 if stale: print("STALE\n"+"\n".join(stale));return 1
 print(f"checked={len(LESSONS)*2} stale=0" if a.check else f"written={len(LESSONS)*2}");return 0
if __name__=="__main__":raise SystemExit(main())

#!/usr/bin/env python3
"""Promote verified L120-L124 knowledge notes into curriculum notes."""
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
 Lesson(120,"Lesson_120-aggregation-having-and-the-grain-statement","Aggregation, HAVING and the grain statement","08-aggregation-having-and-grain-statement.md"),
 Lesson(121,"Lesson_121-subqueries-ctes-and-the-materialization-caveat","Subqueries, CTEs and the materialization caveat","09-subqueries-ctes-and-materialization.md"),
 Lesson(122,"Lesson_122-recursive-ctes-for-hierarchies-and-graphs","Recursive CTEs for hierarchies and graphs","10-recursive-ctes-for-hierarchies-and-graphs.md"),
 Lesson(123,"Lesson_123-window-functions-partition-order-and-frame","Window functions - partition, order and frame","11-window-functions-partition-order-and-frame.md"),
 Lesson(124,"Lesson_124-frames-running-totals-and-period-comparison","Frames, running totals and period comparison","12-window-frames-running-totals-and-period-comparison.md"),
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
 if "**Outcome.**" in n: return tuple(field(n,k) for k in ("Outcome","Đánh giá","Lab","Pitfalls","Self-study (2,4 giờ)","Done when"))
 return (field(section(n,"Mục tiêu bài học"),"Năng lực cần chứng minh"),field(section(a,"Tiêu chí hoàn thành"),"Cách đánh giá"),field(section(a,"Thực hành"),"Nhiệm vụ"),field(section(a,"Bài làm sau buổi học"),"Lỗi cần chủ động loại trừ"),field(section(a,"Bài làm sau buổi học"),"Nhiệm vụ"),field(section(n,"Mục tiêu bài học"),"Điều kiện hoàn thành"))
def build(x):
 outcome,assessment,lab,pitfalls,homework,done=contract(x); source=ROOT/PACK/x.source; body=strip(source.read_text(encoding="utf-8")); h=f"# Phase 4: SQL and Database Internals\n# Module 9: Relational Theory and SQL Execution\n# Lesson {x.number}: {x.title}"
 q={
 120:["Grain trước và sau GROUP BY khác nhau thế nào?","Ba biến thể COUNT trả lời ba câu hỏi nào?","WHERE khác HAVING ở đơn vị lọc nào?","Vì sao aggregate cuối không sửa fanout?"],
 121:["CTE logic khác ranh giới vật lý thế nào?","Khi nào materialization chặn pushdown?","NOT IN gặp NULL có rủi ro gì?","Parity bằng EXCEPT ALL hai chiều chứng minh gì?"],
 122:["Anchor và working table phối hợp ra sao?","UNION vì sao không luôn chặn cycle?","SEARCH có điều khiển evaluation order không?","Unsafe recursion phải được thử dưới lớp bảo vệ nào?"],
 123:["Partition, order và frame khác nhau thế nào?","Bốn ranking functions xử lý tie ra sao?","Vì sao window không đặt trong WHERE cùng level?","Lag có đồng nghĩa kỳ lịch trước không?"],
 124:["ROWS, RANGE và GROUPS khác đơn vị nào?","Vì sao phải dựng calendar scaffold?","Previous zero phải biểu diễn thế nào?","Đối soát rolling metric từng kỳ ra sao?"]}[x.number]
 note=f"{h}\n\n## Mục tiêu bài học\n\n**Năng lực cần chứng minh.** {outcome}\n\n**Điều kiện hoàn thành.** {done}\n\n{body}\n"
 safety_rule="Với bài recursion, mọi truy vấn cố ý không kết thúc phải chạy trong môi trường cô lập dưới `statement_timeout`; không được để query treo không kiểm soát."
 safety=(" "+safety_rule) if x.number==122 and safety_rule not in lab else ""
 after=f"{h}\n\n## Thực hành\n\n**Nhiệm vụ.** {lab}{safety}\n\nLưu SQL, seed data, dự đoán trước khi chạy, output thô, đối soát độc lập và giải thích theo rule. Ảnh chụp không thay artifact chạy lại được.\n\n## Kiểm tra cuối bài\n\n"+"\n".join(f"{i}. {v}" for i,v in enumerate(q,1))+f"\n\n## Tiêu chí hoàn thành\n\n**Cách đánh giá.** {assessment}\n\n**Điều kiện đạt.** {done}\n\n## Bài làm sau buổi học\n\n**Nhiệm vụ.** {homework}\n\n**Lỗi cần chủ động loại trừ.** {pitfalls}\n\n## Reference\n\n- Knowledge note: `{source.relative_to(ROOT)}`\n- Nội dung học thuật: `note.md` cùng thư mục.\n"
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

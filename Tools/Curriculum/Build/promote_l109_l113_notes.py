#!/usr/bin/env python3
"""Promote verified L109-L113 knowledge notes into curriculum notes."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

@dataclass(frozen=True)
class Lesson:
    number: int; phase: int; phase_title: str; module: int; module_title: str
    directory: str; title: str; source: str

LESSONS = (
    Lesson(109,3,"Software and Backend Engineering",8,"Backend and API Engineering","Material/DE/Curriculum/Phase_03-software-and-backend-engineering/Module_08-backend-and-api-engineering/Lesson_109-the-outbox-pattern-one-atomic-write","The outbox pattern - one atomic write","Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/21-transactional-outbox-one-atomic-write.md"),
    Lesson(110,3,"Software and Backend Engineering",8,"Backend and API Engineering","Material/DE/Curriculum/Phase_03-software-and-backend-engineering/Module_08-backend-and-api-engineering/Lesson_110-load-testing-and-capacity-notes","Load testing and capacity notes","Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/22-load-testing-and-capacity-notes.md"),
    Lesson(111,3,"Software and Backend Engineering",8,"Backend and API Engineering","Material/DE/Curriculum/Phase_03-software-and-backend-engineering/Module_08-backend-and-api-engineering/Lesson_111-the-job-control-api-project","The job-control API project","Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/23-job-control-api-project.md"),
    Lesson(112,3,"Software and Backend Engineering",8,"Backend and API Engineering","Material/DE/Curriculum/Phase_03-software-and-backend-engineering/Module_08-backend-and-api-engineering/Lesson_112-gate-3-a-correct-service-under-concurrency-and-failure","Gate 3 - a correct service under concurrency and failure","Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/24-gate-3-correct-service-assessment.md"),
    Lesson(113,4,"SQL and Database Internals",9,"Relational Theory and SQL Execution","Material/DE/Curriculum/Phase_04-sql-and-database-internals/Module_09-relational-theory-and-sql-execution/Lesson_113-relations-keys-and-functional-dependencies","Relations, keys and functional dependencies","Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/01-relations-keys-functional-dependencies.md"),
)

def field(text: str, name: str) -> str:
    m = re.search(rf"(?m)^\*\*{re.escape(name)}\.\*\*\s*(.+)$", text)
    if not m: raise ValueError(f"Thiếu trường {name}")
    return m.group(1).strip()

def strip_frontmatter_and_title(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        text = text[end + 5:]
    return re.sub(r"^# .+\n+", "", text.strip(), count=1)

def section(text: str, heading: str) -> str:
    m=re.search(rf"(?ms)^## {re.escape(heading)}\n\n(.*?)(?=^## |\Z)",text)
    if not m: raise ValueError(f"Thiếu section {heading}")
    return m.group(1).strip()

def contract(folder: Path) -> tuple[str,str,str,str,str,str]:
    note=(folder/"note.md").read_text(encoding="utf-8"); after=(folder/"after-note.md").read_text(encoding="utf-8")
    if "**Outcome.**" in note:
        return field(note,"Outcome"),field(note,"Đánh giá"),field(note,"Lab"),field(note,"Pitfalls"),field(note,"Self-study (2,4 giờ)"),field(note,"Done when")
    return field(section(note,"Mục tiêu bài học"),"Năng lực cần chứng minh"),field(section(after,"Tiêu chí hoàn thành"),"Cách đánh giá"),field(section(after,"Thực hành"),"Nhiệm vụ"),field(section(after,"Bài làm sau buổi học"),"Lỗi cần chủ động loại trừ"),field(section(after,"Bài làm sau buổi học"),"Nhiệm vụ"),field(section(note,"Mục tiêu bài học"),"Điều kiện hoàn thành")

def hierarchy(x: Lesson) -> str:
    return f"# Phase {x.phase}: {x.phase_title}\n# Module {x.module}: {x.module_title}\n# Lesson {x.number}: {x.title}"

def build(x: Lesson) -> tuple[str, str]:
    folder = ROOT / x.directory
    body = strip_frontmatter_and_title((ROOT / x.source).read_text(encoding="utf-8"))
    outcome, assessment, lab, pitfalls, homework, done = contract(folder)
    head = hierarchy(x)
    note = f"{head}\n\n## Mục tiêu bài học\n\n**Năng lực cần chứng minh.** {outcome}\n\n**Điều kiện hoàn thành.** {done}\n\n{body}\n"
    questions = {
      109: ["Failure window nào được outbox loại bỏ, failure window nào vẫn còn?", "Vì sao published-but-not-marked tạo duplicate hợp lệ?", "Thiết kế cleanup thế nào để không xoá pending row?", "Bằng chứng nào cho phép và không cho phép dùng cụm từ exactly-once?"],
      110: ["Vì sao throughput đơn lẻ không phải capacity?", "Phân biệt offered load, throughput và goodput.", "Làm sao chứng minh bottleneck thay vì chỉ nêu correlation?", "Kết luận tối đa nào hợp lệ từ soak test 30 phút?"],
      111: ["Lease hết hạn khi worker cũ còn sống gây race nào?", "Worker chết sau external effect cần protocol gì?", "Cancellation requested khác cancelled thế nào?", "Fault artifact nào chứng minh không mất job?"],
      112: ["Vì sao phần B và C là hard gate?", "Một concurrency test hợp lệ cần barrier và invariant nào?", "Telemetry evidence nào đủ để chẩn đoán injected failure?", "Negative authorization test phải phủ những actor nào?"],
      113: ["Vì sao sample không duplicate không chứng minh candidate key?", "Phân biệt superkey, candidate key và primary key.", "Tính attribute closure dùng để làm gì?", "Vì sao application validation không thay database constraint?"],
    }[x.number]
    after = f"{head}\n\n## Thực hành\n\n**Nhiệm vụ.** {lab}\n\nBài làm phải lưu lệnh tái hiện, dữ liệu đầu vào, đầu ra thô và assertion của invariant. Mọi kết luận phải chỉ được evidence ID tương ứng; ảnh chụp không thay artifact chạy lại được.\n\n## Kiểm tra cuối bài\n\n" + "\n".join(f"{i}. {q}" for i,q in enumerate(questions,1)) + f"\n\n## Tiêu chí hoàn thành\n\n**Cách đánh giá.** {assessment}\n\n**Điều kiện đạt.** {done}\n\n## Bài làm sau buổi học\n\n**Nhiệm vụ.** {homework}\n\n**Lỗi cần chủ động loại trừ.** {pitfalls}\n\n## Reference\n\n- Knowledge note: `{x.source}`\n- Nội dung học thuật: `note.md` cùng thư mục.\n"
    return note, after

def main() -> int:
    parser=argparse.ArgumentParser(); parser.add_argument("--check",action="store_true"); args=parser.parse_args()
    stale=[]
    for x in LESSONS:
        expected=build(x); paths=(ROOT/x.directory/"note.md", ROOT/x.directory/"after-note.md")
        for p,c in zip(paths,expected):
            if args.check:
                if p.read_text(encoding="utf-8") != c: stale.append(str(p.relative_to(ROOT)))
            else: p.write_text(c,encoding="utf-8")
    if stale:
        print("STALE\n"+"\n".join(stale)); return 1
    print(f"checked={len(LESSONS)*2} stale=0" if args.check else f"written={len(LESSONS)*2}"); return 0

if __name__ == "__main__": raise SystemExit(main())

#!/usr/bin/env python3
"""Promote verified L130-L134 knowledge notes into curriculum notes."""
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACK = "Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01"


@dataclass(frozen=True)
class Lesson:
    number: int
    module_number: int
    module_title: str
    base: str
    directory: str
    title: str
    source: str


LESSONS = (
    Lesson(130, 9, "Relational Theory and SQL Execution", "Material/DE/Curriculum/Phase_04-sql-and-database-internals/Module_09-relational-theory-and-sql-execution", "Lesson_130-reading-explain-analyze-with-buffers", "Reading EXPLAIN ANALYZE with buffers", "18-reading-explain-analyze-with-buffers.md"),
    Lesson(131, 9, "Relational Theory and SQL Execution", "Material/DE/Curriculum/Phase_04-sql-and-database-internals/Module_09-relational-theory-and-sql-execution", "Lesson_131-sargability-parameters-and-plan-stability", "Sargability, parameters and plan stability", "19-sargability-parameters-and-plan-stability.md"),
    Lesson(132, 9, "Relational Theory and SQL Execution", "Material/DE/Curriculum/Phase_04-sql-and-database-internals/Module_09-relational-theory-and-sql-execution", "Lesson_132-sql-tuning-project-five-slow-queries", "SQL tuning project - five slow queries", "20-sql-tuning-project-five-slow-queries.md"),
    Lesson(133, 10, "Storage Engine and Database Operations", "Material/DE/Curriculum/Phase_04-sql-and-database-internals/Module_10-storage-engine-and-database-operations", "Lesson_133-pages-heap-files-and-the-buffer-pool", "Pages, heap files and the buffer pool", "21-pages-heap-files-and-buffer-pool.md"),
    Lesson(134, 10, "Storage Engine and Database Operations", "Material/DE/Curriculum/Phase_04-sql-and-database-internals/Module_10-storage-engine-and-database-operations", "Lesson_134-b-tree-internals-fanout-splits-and-clustering", "B-tree internals - fanout, splits and clustering", "22-btree-internals-fanout-splits-and-clustering.md"),
)


def field(text: str, name: str) -> str:
    match = re.search(rf"(?m)^\*\*{re.escape(name)}\.\*\*\s*(.+)$", text)
    if not match:
        raise ValueError(f"Thiếu {name}")
    return match.group(1).strip()


def section(text: str, heading: str) -> str:
    match = re.search(rf"(?ms)^## {re.escape(heading)}\n\n(.*?)(?=^## |\Z)", text)
    if not match:
        raise ValueError(f"Thiếu section {heading}")
    return match.group(1).strip()


def strip_frontmatter_and_title(text: str) -> str:
    if text.startswith("---\n"):
        text = text[text.find("\n---\n", 4) + 5 :]
    return re.sub(r"^# .+\n+", "", text.strip(), count=1)


def folder(lesson: Lesson) -> Path:
    return ROOT / lesson.base / lesson.directory


def contract(lesson: Lesson) -> tuple[str, str, str, str, str, str]:
    note = (folder(lesson) / "note.md").read_text(encoding="utf-8")
    after = (folder(lesson) / "after-note.md").read_text(encoding="utf-8")
    if "**Outcome.**" in note:
        return tuple(field(note, key) for key in ("Outcome", "Đánh giá", "Lab", "Pitfalls", "Self-study (2,4 giờ)", "Done when"))
    return (
        field(section(note, "Mục tiêu bài học"), "Năng lực cần chứng minh"),
        field(section(after, "Tiêu chí hoàn thành"), "Cách đánh giá"),
        field(section(after, "Thực hành"), "Nhiệm vụ"),
        field(section(after, "Bài làm sau buổi học"), "Lỗi cần chủ động loại trừ"),
        field(section(after, "Bài làm sau buổi học"), "Nhiệm vụ"),
        field(section(note, "Mục tiêu bài học"), "Điều kiện hoàn thành"),
    )


def build(lesson: Lesson) -> tuple[str, str]:
    outcome, assessment, lab, pitfalls, homework, done = contract(lesson)
    source = ROOT / PACK / lesson.source
    body = strip_frontmatter_and_title(source.read_text(encoding="utf-8"))
    header = (
        "# Phase 4: SQL and Database Internals\n"
        f"# Module {lesson.module_number}: {lesson.module_title}\n"
        f"# Lesson {lesson.number}: {lesson.title}"
    )
    questions = {
        130: [
            "Vì sao không được cộng thời gian của mọi plan node?",
            "Actual rows và time phải diễn giải cùng loops thế nào?",
            "Shared read có đồng nghĩa physical disk read không?",
            "Node lệch ước lượng đầu tiên giúp định tuyến chẩn đoán ra sao?",
        ],
        131: [
            "Sargability phải được chứng minh bằng evidence nào?",
            "PostgreSQL chọn generic và custom plan theo cơ chế nào?",
            "Vì sao optional-filter pattern có thể làm generic plan khó tối ưu?",
            "Parameterization và plan specialization cùng tồn tại thế nào?",
        ],
        132: [
            "Vì sao bằng nhau về row count chưa chứng minh result parity?",
            "Một tuning dossier tối thiểu cần những artifacts nào?",
            "One-variable discipline giúp thiết lập quan hệ nhân quả ra sao?",
            "Khi nào một cải thiện trên staging chưa đủ để rollout production?",
        ],
        133: [
            "Ba vùng chính của một heap page PostgreSQL là gì?",
            "FSM và VM nằm ở đâu so với main fork?",
            "Shared read khác physical storage read thế nào?",
            "Vì sao buffer hit ratio không thể đứng một mình làm chỉ số hiệu năng?",
        ],
        134: [
            "Fanout ảnh hưởng độ sâu cây B-tree thế nào?",
            "Insert tuần tự và ngẫu nhiên tạo hai profile chi phí nào?",
            "Free space tái sử dụng khác bloat cần reclaim thế nào?",
            "CLUSTER thay đổi locality nhưng không duy trì điều gì?",
        ],
    }[lesson.number]
    note = (
        f"{header}\n\n## Mục tiêu bài học\n\n"
        f"**Năng lực cần chứng minh.** {outcome}\n\n"
        f"**Điều kiện hoàn thành.** {done}\n\n{body}\n"
    )
    after = (
        f"{header}\n\n## Thực hành\n\n**Nhiệm vụ.** {lab}\n\n"
        "Lưu SQL, dữ liệu sinh, tham số, dự đoán trước khi chạy, plan dạng máy đọc được, output thô, đối soát và thông số môi trường. "
        "Chỉ chạy `EXPLAIN ANALYZE`, DML, tải dữ liệu, thao tác cache, `pageinspect` hoặc extension trong PostgreSQL thử nghiệm cô lập; không dùng production để tạo cold cache hay benchmark. Ảnh chụp không thay artifact tái chạy.\n\n"
        "## Kiểm tra cuối bài\n\n"
        + "\n".join(f"{index}. {question}" for index, question in enumerate(questions, 1))
        + f"\n\n## Tiêu chí hoàn thành\n\n**Cách đánh giá.** {assessment}\n\n**Điều kiện đạt.** {done}\n\n"
        f"## Bài làm sau buổi học\n\n**Nhiệm vụ.** {homework}\n\n"
        f"**Lỗi cần chủ động loại trừ.** {pitfalls}\n\n"
        f"## Reference\n\n- Knowledge note: `{source.relative_to(ROOT)}`\n- Nội dung học thuật: `note.md` cùng thư mục.\n"
    )
    return note, after


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale: list[str] = []
    for lesson in LESSONS:
        for path, content in zip((folder(lesson) / "note.md", folder(lesson) / "after-note.md"), build(lesson)):
            if args.check:
                if path.read_text(encoding="utf-8") != content:
                    stale.append(str(path.relative_to(ROOT)))
            else:
                path.write_text(content, encoding="utf-8")
    if stale:
        print("STALE\n" + "\n".join(stale))
        return 1
    print(f"checked={len(LESSONS) * 2} stale=0" if args.check else f"written={len(LESSONS) * 2}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

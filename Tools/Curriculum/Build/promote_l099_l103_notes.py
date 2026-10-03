#!/usr/bin/env python3
"""Promote verified L099-L103 knowledge notes into curriculum notes."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CURRICULUM = ROOT / "Material/DE/Curriculum/Phase_03-software-and-backend-engineering"
PACK = ROOT / "Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01"


@dataclass(frozen=True)
class Lesson:
    number: int
    module_number: int
    module_slug: str
    module_title: str
    directory: str
    title: str
    source: str
    activity_prefixes: tuple[str, ...]
    rubric_prefixes: tuple[str, ...]
    question_prefixes: tuple[str, ...]


LESSONS = (
    Lesson(99, 7, "Module_07-software-design-and-delivery", "Software Design and Delivery", "Lesson_099-monolith-modular-monolith-and-the-cost-of-splitting", "Monolith, modular monolith and the cost of splitting", "11-monolith-modular-monolith-and-cost-of-splitting.md", ("15. Bằng chứng",), (), ("16. Câu hỏi tự kiểm tra",)),
    Lesson(100, 7, "Module_07-software-design-and-delivery", "Software Design and Delivery", "Lesson_100-delivery-project-a-modular-package-with-a-release-path", "Delivery project: a modular package with a release path", "12-delivery-project-modular-package-release-path.md", (), ("12. Ma trận chấm",), ("14. Câu hỏi tự kiểm tra",)),
    Lesson(101, 8, "Module_08-backend-and-api-engineering", "Backend and API Engineering", "Lesson_101-the-request-lifecycle-end-to-end", "The request lifecycle end to end", "13-request-lifecycle-end-to-end.md", ("15. Thí nghiệm", "18. Bằng chứng"), (), ("19. Câu hỏi tự kiểm tra",)),
    Lesson(102, 8, "Module_08-backend-and-api-engineering", "Backend and API Engineering", "Lesson_102-api-contract-resources-errors-and-versioning", "API contracts: resources, errors and versioning", "14-api-contract-resources-errors-versioning.md", ("20. Bằng chứng",), (), ("21. Câu hỏi tự kiểm tra",)),
    Lesson(103, 8, "Module_08-backend-and-api-engineering", "Backend and API Engineering", "Lesson_103-transaction-boundaries-and-the-unit-of-work", "Transaction boundaries and the unit of work", "15-transaction-boundaries-and-unit-of-work.md", ("16. Bằng chứng",), ("17. Ma trận đánh giá",), ("18. Câu hỏi tự kiểm tra",)),
)


def lesson_dir(lesson: Lesson) -> Path:
    return CURRICULUM / lesson.module_slug / lesson.directory


def strip_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end < 0:
            raise ValueError("front matter không đóng")
        return text[end + 5 :]
    return text


def split_sections(text: str) -> tuple[str, list[tuple[str, str]]]:
    text = strip_frontmatter(text).strip() + "\n"
    text = re.sub(r"^# .+\n+", "", text, count=1)
    matches = list(re.finditer(r"(?m)^## (.+)$", text))
    intro = text[: matches[0].start()].strip() if matches else text.strip()
    items = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        items.append((match.group(1).strip(), text[match.end() : end].strip()))
    return intro, items


def scaffold_field(text: str, name: str) -> str:
    match = re.search(rf"(?m)^\*\*{re.escape(name)}\.\*\*\s*(.+)$", text)
    if not match:
        raise ValueError(f"Thiếu trường {name}")
    return match.group(1).strip()


def section_body(text: str, heading: str) -> str:
    match = re.search(rf"(?ms)^## {re.escape(heading)}\n\n(.*?)(?=^## |\Z)", text)
    if not match:
        raise ValueError(f"Thiếu section {heading}")
    return match.group(1).strip()


def bold_field(text: str, label: str) -> str:
    match = re.search(rf"(?m)^\*\*{re.escape(label)}\.\*\*\s*(.+)$", text)
    if not match:
        raise ValueError(f"Thiếu field {label}")
    return match.group(1).strip()


def remove_time_boxes(text: str) -> str:
    parts = []
    for part in text.split("·"):
        clean = re.sub(r"^\s*\d+(?:[,.]\d+)?\s*phút\s*", "", part.strip(), flags=re.IGNORECASE)
        clean = clean.replace("**", "").strip()
        if clean:
            parts.append(clean[0].upper() + clean[1:])
    return "; ".join(parts).rstrip(".") + "."


def selected(title: str, prefixes: tuple[str, ...]) -> bool:
    return any(title.startswith(prefix) for prefix in prefixes)


def render(items: list[tuple[str, str]], level: int = 2) -> str:
    blocks = []
    for title, body in items:
        title = re.sub(r"^\d+\.\s*", "", title)
        block = f"{'#' * level} {title}\n\n{body}".strip()
        if level > 2:
            block = re.sub(r"(?m)^### ", "#### ", block)
        blocks.append(block)
    return "\n\n".join(blocks)


def build(lesson: Lesson) -> tuple[str, str]:
    directory = lesson_dir(lesson)
    old_note = (directory / "note.md").read_text(encoding="utf-8")
    old_after = (directory / "after-note.md").read_text(encoding="utf-8")
    source_path = PACK / lesson.source
    intro, sections = split_sections(source_path.read_text(encoding="utf-8"))

    if "**Outcome.**" in old_note:
        outcome = scaffold_field(old_note, "Outcome")
        assessment = scaffold_field(old_note, "Đánh giá")
        lab = scaffold_field(old_note, "Lab")
        pitfalls = scaffold_field(old_note, "Pitfalls")
        homework = scaffold_field(old_note, "Self-study (2,4 giờ)")
        done = scaffold_field(old_note, "Done when")
    else:
        objective = section_body(old_note, "Mục tiêu bài học")
        outcome = bold_field(objective, "Năng lực cần chứng minh")
        done = bold_field(objective, "Điều kiện hoàn thành")
        lab = bold_field(section_body(old_after, "Thực hành"), "Nhiệm vụ")
        criteria = section_body(old_after, "Tiêu chí hoàn thành")
        assessment = bold_field(criteria, "Cách đánh giá")
        homework_section = section_body(old_after, "Bài làm sau buổi học")
        homework = bold_field(homework_section, "Nhiệm vụ")
        pitfalls = bold_field(homework_section, "Lỗi cần chủ động loại trừ")

    activity, rubric, questions, teaching = [], [], [], []
    for title, body in sections:
        if selected(title, lesson.activity_prefixes):
            activity.append((title, body))
        elif selected(title, lesson.rubric_prefixes):
            rubric.append((title, body))
        elif selected(title, lesson.question_prefixes):
            questions.append((title, body))
        elif "Liên kết chương trình" in title or "Lịch sử biên tập" in title:
            continue
        else:
            teaching.append((title, body))

    hierarchy = f"# Phase 3: Software and Backend Engineering\n# Module {lesson.module_number}: {lesson.module_title}\n# Lesson {lesson.number}: {lesson.title}"
    note = (
        f"{hierarchy}\n\n## Mục tiêu bài học\n\n"
        f"**Năng lực cần chứng minh.** {outcome}\n\n"
        f"**Điều kiện hoàn thành.** {done}\n\n"
        f"{intro}\n\n{render(teaching)}\n"
    )
    after = (
        f"{hierarchy}\n\n## Thực hành\n\n"
        f"**Nhiệm vụ.** {lab}\n\n{render(activity, 3)}\n\n"
        f"## Kiểm tra cuối bài\n\n{render(questions, 3)}\n\n"
        f"## Tiêu chí hoàn thành\n\n**Cách đánh giá.** {assessment}\n\n"
        f"**Điều kiện đạt.** {done}\n\n{render(rubric, 3)}\n\n"
        f"## Bài làm sau buổi học\n\n**Nhiệm vụ.** {remove_time_boxes(homework)}\n\n"
        f"**Lỗi cần chủ động loại trừ.** {pitfalls}\n\n"
        "Bài làm phải kèm lệnh tái hiện, đầu ra kiểm chứng và giải thích cho từng quyết định kỹ thuật. Không dùng ảnh chụp màn hình thay cho artifact có thể chạy lại.\n\n"
        f"## Reference\n\n- Knowledge note: `{source_path.relative_to(ROOT)}`\n- Nội dung lý thuyết của bài: `note.md` cùng thư mục.\n"
    )
    return note.replace("\n\n\n", "\n\n"), after.replace("\n\n\n", "\n\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale = []
    for lesson in LESSONS:
        expected = build(lesson)
        paths = (lesson_dir(lesson) / "note.md", lesson_dir(lesson) / "after-note.md")
        for path, content in zip(paths, expected):
            if args.check:
                if path.read_text(encoding="utf-8") != content:
                    stale.append(str(path.relative_to(ROOT)))
            else:
                path.write_text(content, encoding="utf-8")
    if stale:
        print("Các file chưa đồng bộ với nguồn:")
        print("\n".join(f"- {path}" for path in stale))
        return 1
    print(f"checked={len(LESSONS) * 2} stale=0" if args.check else f"written={len(LESSONS) * 2}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


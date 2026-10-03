#!/usr/bin/env python3
"""Promote the verified Module 07 knowledge notes into curriculum chapters.

This script deliberately keeps the source knowledge note unchanged. It removes only
editorial metadata and moves learner work (lab evidence, rubrics and self-checks) to
after-note.md.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
MODULE = ROOT / "Material/DE/Curriculum/Phase_03-software-and-backend-engineering/Module_07-software-design-and-delivery"
PACK = ROOT / "Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01"


@dataclass(frozen=True)
class Lesson:
    number: int
    directory: str
    title: str
    source: str
    activity_prefixes: tuple[str, ...]
    rubric_prefixes: tuple[str, ...]
    question_prefixes: tuple[str, ...]


LESSONS = (
    Lesson(91, "Lesson_091-ports-and-adapters-in-practice", "Ports and adapters in practice", "03-ports-adapters-data-pipeline.md", ("16. Bằng chứng",), ("17. Ma trận chấm",), ("19. Câu hỏi tự kiểm tra",)),
    Lesson(92, "Lesson_092-error-design-expected-failure-against-defect", "Error design: expected failure against defect", "04-error-design-data-pipeline.md", ("14. Bốn thí nghiệm", "15. Phép kiểm bắt buộc"), ("17. Ma trận chấm",), ("19. Câu hỏi tự kiểm tra",)),
    Lesson(93, "Lesson_093-the-test-pyramid-and-where-to-place-a-double", "The test pyramid and where to place a double", "05-test-strategy-double-boundary.md", ("17. Bằng chứng",), ("18. Ma trận đánh giá",), ("20. Câu hỏi tự kiểm tra",)),
    Lesson(94, "Lesson_094-contract-testing-between-a-producer-and-a-consumer", "Contract testing between a producer and a consumer", "06-consumer-provider-contract-testing.md", ("18. Bằng chứng", "19. Ma trận ba thay đổi"), ("20. Ma trận chấm",), ("22. Câu hỏi tự kiểm tra",)),
    Lesson(95, "Lesson_095-refactoring-in-small-behaviour-preserving-steps", "Refactoring in small behaviour-preserving steps", "07-behavior-preserving-refactoring.md", ("15. Case study",), ("18. Checklist nghiệm thu",), ("16. Bài tự kiểm tra",)),
    Lesson(96, "Lesson_096-static-analysis-dependency-and-security-scanning", "Static analysis, dependency and security scanning", "08-automated-code-and-supply-chain-checks.md", ("8. Bốn phép thử tiêm",), (), ("19. Bài tự kiểm tra",)),
    Lesson(97, "Lesson_097-release-artifacts-versions-and-migration-compatibility", "Release artifacts, versions and migration compatibility", "09-release-artifacts-versioning-and-compatible-migrations.md", ("8. Phép thử có tải",), ("18. Evidence package",), ("20. Bài tự kiểm tra",)),
    Lesson(98, "Lesson_098-deployment-strategies-and-rollback", "Deployment strategies and rollback", "10-deployment-strategies-and-rollback.md", ("8. Rollback drill", "9. Ba tình huống lựa chọn", "20. Thiết kế rollback drill"), (), ("22. Bài tự kiểm tra",)),
)


def strip_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end < 0:
            raise ValueError("front matter không đóng")
        return text[end + 5 :]
    return text


def sections(text: str) -> tuple[str, list[tuple[str, str]]]:
    text = strip_frontmatter(text).strip() + "\n"
    text = re.sub(r"^# .+\n+", "", text, count=1)
    matches = list(re.finditer(r"(?m)^## (.+)$", text))
    intro = text[: matches[0].start()].strip() if matches else text.strip()
    result: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        result.append((match.group(1).strip(), text[match.end() : end].strip()))
    return intro, result


def field(scaffold: str, name: str) -> str:
    match = re.search(rf"(?m)^\*\*{re.escape(name)}\.\*\*\s*(.+)$", scaffold)
    if not match:
        raise ValueError(f"Thiếu trường {name}")
    return match.group(1).strip()


def section_body(text: str, heading: str) -> str:
    match = re.search(
        rf"(?ms)^## {re.escape(heading)}\n\n(.*?)(?=^## |\Z)", text
    )
    if not match:
        raise ValueError(f"Thiếu section {heading}")
    return match.group(1).strip()


def bold_field(text: str, label: str) -> str:
    match = re.search(rf"(?m)^\*\*{re.escape(label)}\.\*\*\s*(.+)$", text)
    if not match:
        raise ValueError(f"Thiếu field {label}")
    return match.group(1).strip()


def starts_with(title: str, prefixes: tuple[str, ...]) -> bool:
    return any(title.startswith(prefix) for prefix in prefixes)


def remove_time_boxes(text: str) -> str:
    parts = []
    for part in text.split("·"):
        clean = re.sub(r"^\s*\d+(?:[,.]\d+)?\s*phút\s*", "", part.strip(), flags=re.IGNORECASE)
        clean = clean.replace("**", "").strip()
        if clean:
            parts.append(clean[0].upper() + clean[1:])
    return "; ".join(parts).rstrip(".") + "."


def render_sections(items: list[tuple[str, str]], level: int = 2) -> str:
    rendered: list[str] = []
    for title, body in items:
        clean = re.sub(r"^\d+\.\s*", "", title)
        block = f"{'#' * level} {clean}\n\n{body}".strip()
        if level > 2:
            block = re.sub(r"(?m)^### ", "#### ", block)
        rendered.append(block)
    return "\n\n".join(rendered)


def build(lesson: Lesson) -> tuple[str, str]:
    lesson_dir = MODULE / lesson.directory
    old_note = (lesson_dir / "note.md").read_text(encoding="utf-8")
    old_after = (lesson_dir / "after-note.md").read_text(encoding="utf-8")
    source_path = PACK / lesson.source
    source_text = source_path.read_text(encoding="utf-8")
    intro, source_sections = sections(source_text)

    if "**Outcome.**" in old_note:
        outcome = field(old_note, "Outcome")
        assessment = field(old_note, "Đánh giá")
        lab = field(old_note, "Lab")
        pitfalls = field(old_note, "Pitfalls")
        self_study = field(old_note, "Self-study (2,4 giờ)")
        done = field(old_note, "Done when")
    else:
        objective_section = section_body(old_note, "Mục tiêu bài học")
        outcome = bold_field(objective_section, "Năng lực cần chứng minh")
        done = bold_field(objective_section, "Điều kiện hoàn thành")
        practice_section = section_body(old_after, "Thực hành")
        criteria_section = section_body(old_after, "Tiêu chí hoàn thành")
        homework_section = section_body(old_after, "Bài làm sau buổi học")
        lab = bold_field(practice_section, "Nhiệm vụ")
        assessment = bold_field(criteria_section, "Cách đánh giá")
        self_study = bold_field(homework_section, "Nhiệm vụ")
        pitfalls = bold_field(homework_section, "Lỗi cần chủ động loại trừ")

    activity: list[tuple[str, str]] = []
    rubric: list[tuple[str, str]] = []
    questions: list[tuple[str, str]] = []
    teaching: list[tuple[str, str]] = []
    editorial = ("Liên kết chương trình", "Lịch sử biên tập")
    for title, body in source_sections:
        if starts_with(title, lesson.activity_prefixes):
            activity.append((title, body))
        elif starts_with(title, lesson.rubric_prefixes):
            rubric.append((title, body))
        elif starts_with(title, lesson.question_prefixes):
            questions.append((title, body))
        elif any(label in title for label in editorial):
            continue
        else:
            teaching.append((title, body))

    hierarchy = (
        "# Phase 3: Software and Backend Engineering\n"
        "# Module 7: Software Design and Delivery\n"
        f"# Lesson {lesson.number}: {lesson.title}"
    )
    objective = (
        "## Mục tiêu bài học\n\n"
        f"**Năng lực cần chứng minh.** {outcome}\n\n"
        f"**Điều kiện hoàn thành.** {done}"
    )
    note = f"{hierarchy}\n\n{objective}\n\n{intro}\n\n{render_sections(teaching)}\n"

    practice_detail = render_sections(activity, level=3) if activity else ""
    rubric_detail = render_sections(rubric, level=3) if rubric else ""
    question_detail = render_sections(questions, level=3) if questions else "Chưa có bộ câu hỏi riêng trong knowledge note nguồn."
    after = (
        f"{hierarchy}\n\n"
        "## Thực hành\n\n"
        f"**Nhiệm vụ.** {lab}\n\n"
        f"{practice_detail}\n\n"
        "## Kiểm tra cuối bài\n\n"
        f"{question_detail}\n\n"
        "## Tiêu chí hoàn thành\n\n"
        f"**Cách đánh giá.** {assessment}\n\n"
        f"**Điều kiện đạt.** {done}\n\n"
        f"{rubric_detail}\n\n"
        "## Bài làm sau buổi học\n\n"
        f"**Nhiệm vụ.** {remove_time_boxes(self_study)}\n\n"
        f"**Lỗi cần chủ động loại trừ.** {pitfalls}\n\n"
        "Bài làm phải kèm lệnh tái hiện, đầu ra kiểm chứng và một đoạn giải thích ngắn cho mỗi quyết định kỹ thuật. Không chấp nhận ảnh chụp màn hình thay cho artifact có thể chạy lại.\n\n"
        "## Reference\n\n"
        f"- Knowledge note: `{source_path.relative_to(ROOT)}`\n"
        f"- Nội dung lý thuyết của bài: `note.md` cùng thư mục.\n"
    )
    return note.replace("\n\n\n", "\n\n"), after.replace("\n\n\n", "\n\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Chỉ so sánh output dự kiến với file hiện tại")
    args = parser.parse_args()
    stale: list[str] = []
    for lesson in LESSONS:
        note, after = build(lesson)
        lesson_dir = MODULE / lesson.directory
        outputs = ((lesson_dir / "note.md", note), (lesson_dir / "after-note.md", after))
        for path, expected in outputs:
            if args.check:
                if path.read_text(encoding="utf-8") != expected:
                    stale.append(str(path.relative_to(ROOT)))
            else:
                path.write_text(expected, encoding="utf-8")
    if stale:
        print("Các file chưa đồng bộ với nguồn:")
        for path in stale:
            print(f"- {path}")
        return 1
    print(f"checked={len(LESSONS) * 2} stale=0" if args.check else f"written={len(LESSONS) * 2}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

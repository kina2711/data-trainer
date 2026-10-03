#!/usr/bin/env python3
"""Promote verified L104-L108 knowledge notes into curriculum notes."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
MODULE = ROOT / "Material/DE/Curriculum/Phase_03-software-and-backend-engineering/Module_08-backend-and-api-engineering"
PACK = ROOT / "Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01"


@dataclass(frozen=True)
class Lesson:
    number: int
    directory: str
    title: str
    source: str
    activity_prefixes: tuple[str, ...]
    evidence_prefixes: tuple[str, ...]
    question_prefixes: tuple[str, ...]


LESSONS = (
    Lesson(104, "Lesson_104-concurrency-control-optimistic-and-pessimistic", "Concurrency control - optimistic and pessimistic", "16-concurrency-control-optimistic-and-pessimistic.md", ("14. Phép thử",), ("16. Bằng chứng",), ("17. Câu hỏi",)),
    Lesson(105, "Lesson_105-idempotency-keys-and-deduplication-state", "Idempotency keys and deduplication state", "17-idempotency-keys-and-deduplication-state.md", ("16. Ba thí nghiệm",), ("17. Ma trận",), ("18. Câu hỏi",)),
    Lesson(106, "Lesson_106-authentication-authorization-and-ownership-checks", "Authentication, authorization and ownership checks", "18-authentication-authorization-and-ownership-checks.md", ("13. Negative test", "14. Đo revocation"), ("17. Bằng chứng",), ("18. Câu hỏi",)),
    Lesson(107, "Lesson_107-resilience-timeouts-circuit-breakers-and-bulkheads", "Resilience - timeouts, circuit breakers and bulkheads", "19-resilience-timeouts-circuit-breakers-and-bulkheads.md", ("15. Ba kịch bản", "16. Đo"), ("18. Bằng chứng",), ("19. Câu hỏi",)),
    Lesson(108, "Lesson_108-observability-for-an-api-red-metrics-and-tracing", "Observability for an API - RED metrics and tracing", "20-api-observability-red-metrics-and-tracing.md", ("18. Instrumentation verification",), ("20. Bằng chứng",), ("21. Câu hỏi",)),
)


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


def field(text: str, name: str) -> str:
    match = re.search(rf"(?m)^\*\*{re.escape(name)}\.\*\*\s*(.+)$", text)
    if not match:
        raise ValueError(f"Thiếu trường {name}")
    return match.group(1).strip()


def section(text: str, heading: str) -> str:
    match = re.search(rf"(?ms)^## {re.escape(heading)}\n\n(.*?)(?=^## |\Z)", text)
    if not match:
        raise ValueError(f"Thiếu section {heading}")
    return match.group(1).strip()


def remove_time_boxes(text: str) -> str:
    parts = []
    for part in text.split("·"):
        clean = re.sub(r"^\s*\d+(?:[,.]\d+)?\s*phút\s*", "", part.strip(), flags=re.IGNORECASE)
        clean = clean.replace("**", "").strip()
        if clean:
            parts.append(clean[0].upper() + clean[1:])
    return "; ".join(parts).rstrip(".") + "."


def matches(title: str, prefixes: tuple[str, ...]) -> bool:
    return any(title.startswith(prefix) for prefix in prefixes)


def render(items: list[tuple[str, str]], level: int = 2) -> str:
    blocks = []
    for title, body in items:
        clean = re.sub(r"^\d+\.\s*", "", title)
        block = f"{'#' * level} {clean}\n\n{body}".strip()
        if level > 2:
            block = re.sub(r"(?m)^### ", "#### ", block)
        blocks.append(block)
    return "\n\n".join(blocks)


def lesson_dir(lesson: Lesson) -> Path:
    return MODULE / lesson.directory


def load_contract(directory: Path) -> tuple[str, str, str, str, str, str]:
    note = (directory / "note.md").read_text(encoding="utf-8")
    after = (directory / "after-note.md").read_text(encoding="utf-8")
    if "**Outcome.**" in note:
        return (
            field(note, "Outcome"),
            field(note, "Đánh giá"),
            field(note, "Lab"),
            field(note, "Pitfalls"),
            field(note, "Self-study (2,4 giờ)"),
            field(note, "Done when"),
        )
    objective = section(note, "Mục tiêu bài học")
    return (
        field(objective, "Năng lực cần chứng minh"),
        field(section(after, "Tiêu chí hoàn thành"), "Cách đánh giá"),
        field(section(after, "Thực hành"), "Nhiệm vụ"),
        field(section(after, "Bài làm sau buổi học"), "Lỗi cần chủ động loại trừ"),
        field(section(after, "Bài làm sau buổi học"), "Nhiệm vụ"),
        field(objective, "Điều kiện hoàn thành"),
    )


def build(lesson: Lesson) -> tuple[str, str]:
    directory = lesson_dir(lesson)
    outcome, assessment, lab, pitfalls, homework, done = load_contract(directory)
    source_path = PACK / lesson.source
    intro, sections = split_sections(source_path.read_text(encoding="utf-8"))
    activity, evidence, questions, teaching = [], [], [], []
    for title, body in sections:
        if matches(title, lesson.activity_prefixes):
            activity.append((title, body))
        elif matches(title, lesson.evidence_prefixes):
            evidence.append((title, body))
        elif matches(title, lesson.question_prefixes):
            questions.append((title, body))
        else:
            teaching.append((title, body))
    hierarchy = f"# Phase 3: Software and Backend Engineering\n# Module 8: Backend and API Engineering\n# Lesson {lesson.number}: {lesson.title}"
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
        f"**Điều kiện đạt.** {done}\n\n{render(evidence, 3)}\n\n"
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


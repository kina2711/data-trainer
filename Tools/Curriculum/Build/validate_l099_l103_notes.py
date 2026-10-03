#!/usr/bin/env python3
"""Validate knowledge and curriculum artifacts for DE-L099 through DE-L103."""

from __future__ import annotations

import re

from promote_l099_l103_notes import LESSONS, PACK, ROOT, lesson_dir


def main() -> int:
    failures = []
    for lesson in LESSONS:
        directory = lesson_dir(lesson)
        note = (directory / "note.md").read_text(encoding="utf-8")
        after = (directory / "after-note.md").read_text(encoding="utf-8")
        knowledge = (PACK / lesson.source).read_text(encoding="utf-8")
        prefix = f"# Phase 3: Software and Backend Engineering\n# Module {lesson.module_number}: {lesson.module_title}\n# Lesson {lesson.number}: {lesson.title}\n"
        if not note.startswith(prefix) or not after.startswith(prefix):
            failures.append(f"L{lesson.number}: hierarchy heading không đúng")
        for marker in ("trang_thai: chua-viet", "Trạng thái: chưa viết", "thoi_luong_phut:", "## I. Mục tiêu"):
            if marker in note:
                failures.append(f"L{lesson.number}: còn scaffold marker {marker!r}")
        for heading in ("## Mục tiêu bài học", "## Source coverage", "## Key takeaways", "## Reference"):
            if heading not in note:
                failures.append(f"L{lesson.number}: note thiếu {heading}")
        for heading in ("## Thực hành", "## Kiểm tra cuối bài", "## Tiêu chí hoàn thành", "## Bài làm sau buổi học", "## Reference"):
            if heading not in after:
                failures.append(f"L{lesson.number}: after-note thiếu {heading}")
        if any(token in note + after for token in ("\\[", "\\]")):
            failures.append(f"L{lesson.number}: delimiter math không hợp lệ")
        note_words = len(re.findall(r"\b\w+\b", note, re.UNICODE))
        knowledge_words = len(re.findall(r"\b\w+\b", knowledge, re.UNICODE))
        if note_words < 1500:
            failures.append(f"L{lesson.number}: curriculum note quá ngắn ({note_words})")
        if knowledge_words < 1900:
            failures.append(f"L{lesson.number}: knowledge note quá ngắn ({knowledge_words})")
        if len(re.findall(r"(?m)^## Source coverage$", knowledge)) != 1:
            failures.append(f"L{lesson.number}: Source coverage không canonical")
    if failures:
        print("FAIL")
        print("\n".join(f"- {item}" for item in failures))
        return 1
    print(f"PASS lessons={len(LESSONS)} files={len(LESSONS) * 2} knowledge_notes={len(LESSONS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

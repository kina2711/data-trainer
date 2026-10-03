#!/usr/bin/env python3
"""Validate the promoted DE-L091..DE-L098 curriculum notes."""

from __future__ import annotations

import re
from pathlib import Path

from promote_module07_notes import LESSONS, MODULE, ROOT


def prose_wrap_errors(text: str) -> list[int]:
    lines = text.splitlines()
    errors: list[int] = []
    in_fence = False
    for index, line in enumerate(lines[:-1], start=1):
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        nxt = lines[index]
        if in_fence or not line.strip() or not nxt.strip():
            continue
        if line.startswith(("#", "- ", "* ", ">", "|", "<", "$$")):
            continue
        if nxt.startswith(("#", "- ", "* ", ">", "|", "<", "```", "$$")):
            continue
        if re.search(r"[.!?:;`)]$", line.strip()):
            continue
        errors.append(index)
    return errors


def main() -> int:
    failures: list[str] = []
    for lesson in LESSONS:
        directory = MODULE / lesson.directory
        note = (directory / "note.md").read_text(encoding="utf-8")
        after = (directory / "after-note.md").read_text(encoding="utf-8")
        prefix = (
            "# Phase 3: Software and Backend Engineering\n"
            "# Module 7: Software Design and Delivery\n"
            f"# Lesson {lesson.number}: {lesson.title}\n"
        )
        if not note.startswith(prefix) or not after.startswith(prefix):
            failures.append(f"L{lesson.number}: sai hierarchy heading")
        for marker in ("trang_thai: chua-viet", "Trạng thái: chưa viết", "## I. Mục tiêu", "thoi_luong_phut:"):
            if marker in note:
                failures.append(f"L{lesson.number}: còn scaffold marker {marker!r}")
        for heading in ("## Mục tiêu bài học", "## Source coverage", "## Key takeaways", "## Reference"):
            if heading not in note:
                failures.append(f"L{lesson.number}: note thiếu {heading}")
        for heading in ("## Thực hành", "## Kiểm tra cuối bài", "## Tiêu chí hoàn thành", "## Bài làm sau buổi học", "## Reference"):
            if heading not in after:
                failures.append(f"L{lesson.number}: after-note thiếu {heading}")
        if "\\[" in note or "\\]" in note or "\\[" in after or "\\]" in after:
            failures.append(f"L{lesson.number}: còn delimiter toán học không hợp lệ")
        note_words = len(re.findall(r"\b\w+\b", note, flags=re.UNICODE))
        if note_words < 1800:
            failures.append(f"L{lesson.number}: note quá ngắn ({note_words} từ)")
        after_words = len(re.findall(r"\b\w+\b", after, flags=re.UNICODE))
        if after_words < 250:
            failures.append(f"L{lesson.number}: after-note quá ngắn ({after_words} từ)")
        wrapped = prose_wrap_errors(note) + prose_wrap_errors(after)
        if wrapped:
            failures.append(f"L{lesson.number}: có {len(wrapped)} vị trí xuống dòng prose đáng ngờ")
    if failures:
        print("FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"PASS lessons={len(LESSONS)} files={len(LESSONS) * 2}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

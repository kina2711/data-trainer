#!/usr/bin/env python3
"""Validate the approved teaching-version authoring standard."""
from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
TEACHING_FILES = sorted(ROOT.glob("Material/DA/Curriculum/**/Lesson_*/teaching.md")) + sorted(
    ROOT.glob("Material/DE/Curriculum/**/Lesson_*/teaching.md")
)
FORBIDDEN_TYPOGRAPHY = re.compile(r"[“”‘’—–]")
FORBIDDEN_ORNAMENT = re.compile(
    r"\b(?:huyền\s+diệu|huyền\s+huyễn|mỹ\s+miều|ma\s+thuật|"
    r"chìa\s+khóa\s+vạn\s+năng|mang\s+tính\s+cách\s+mạng|"
    r"đột\s+phá|tuyệt\s+đỉnh|vũ\s+trụ|bức\s+tranh\s+toàn\s+cảnh)\b",
    re.I,
)
DECORATIVE_ICON = re.compile(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]")
PUBLIC_DURATION = re.compile(
    r"thoi_gian_uoc_tinh|thời\s+lượng\s+(?:học|bài|buổi)|"
    r"thời\s+gian\s+ước\s+tính|\b\d+\s*(?:phút|giờ)\b",
    re.I,
)
STAGED_PROSE = re.compile(
    r"\b(?:hãy\s+tưởng\s+tượng|bây\s+giờ\s+ta|ta\s+sẽ\s+dùng|"
    r"câu\s+cần\s+nhớ|điều\s+quan\s+trọng\s+là|về\s+bản\s+chất|"
    r"tóm\s+lại|hãy\s+cùng)\b",
    re.I,
)
FALSE_CONTRAST = re.compile(
    r"\bkhông\s+(?:chỉ|phải|đơn\s+thuần|đơn\s+giản)\b[^\n.]{0,140}\b(?:mà|nhưng)\b",
    re.I,
)
DECORATIVE_BOLD_LABEL = re.compile(r"(?m)^\s*(?:[-*]|\d+\.)?\s*\*\*[^*\n:]+:\*\*")
WIKI_LINK = re.compile(r"\[\[(wiki\.[^|\]]+)\|[^\]]+\]\]")


def prose_only(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def main() -> int:
    failures: list[str] = []
    if not TEACHING_FILES:
        failures.append("No teaching.md files found")

    index = json.loads((ROOT / "Apps/SecondBrain/web/data/brain-index.json").read_text())
    notes = {item["id"]: item for item in index.get("notes") or []}
    sources = {item["id"]: item for item in index.get("sources") or []}
    books = {item["id"] for item in index.get("books") or []}

    for path in TEACHING_FILES:
        text = path.read_text()
        prose = prose_only(text)
        relative = path.relative_to(ROOT)
        lesson_yaml = path.with_name("lesson.yaml").read_text()

        for expected in (
            r"standard:\s*lesson-authoring-v1",
            r"humanizer:\s*blader/humanizer@3\.1\.0",
            r"editorial:[\s\S]{0,180}status:\s*pass",
        ):
            if not re.search(expected, lesson_yaml):
                failures.append(f"{relative}: missing editorial evidence {expected}")

        if len(re.findall(r"\b\w+[\w-]*\b", prose, re.U)) < 1800:
            failures.append(f"{relative}: fewer than 1800 prose words")
        if "```" not in text:
            failures.append(f"{relative}: missing code or concrete artifact block")
        for heading in ("Dừng và hỏi", "Kiểm tra hiểu bài", "Điều cần mang theo"):
            if not re.search(rf"(?m)^##+\s+{re.escape(heading)}\s*$", text):
                failures.append(f"{relative}: missing heading {heading}")

        for label, pattern in (
            ("curly quote or long dash", FORBIDDEN_TYPOGRAPHY),
            ("ornamental language", FORBIDDEN_ORNAMENT),
            ("decorative icon", DECORATIVE_ICON),
            ("public duration", PUBLIC_DURATION),
            ("staged prose", STAGED_PROSE),
            ("false contrast", FALSE_CONTRAST),
            ("decorative bold label", DECORATIVE_BOLD_LABEL),
        ):
            match = pattern.search(prose)
            if match:
                failures.append(
                    f"{relative}:{line_number(text, match.start())}: {label}: {match.group(0)!r}"
                )

        if prose.count('"') > 4 or prose.count("'") > 4:
            failures.append(f"{relative}: excessive straight quotation marks in prose")

        note_ids = WIKI_LINK.findall(text)
        if len(note_ids) < 3:
            failures.append(f"{relative}: fewer than three labeled Second Brain links")
        for note_id in note_ids:
            note = notes.get(note_id)
            if not note:
                failures.append(f"{relative}: missing indexed Second Brain note {note_id}")
                continue
            book_ids = {
                sources[source_id].get("bookId")
                for source_id in note.get("sourceIds") or []
                if source_id in sources and sources[source_id].get("bookId")
            }
            if not book_ids:
                failures.append(f"{relative}: {note_id} has no direct Library book source")
            for book_id in book_ids:
                if book_id not in books:
                    failures.append(f"{relative}: {note_id} links to missing book {book_id}")

    app = (ROOT / "Apps/SecondBrain/web/app.js").read_text()
    if 'data-open-book="${escapeHtml(source.bookId)}"' not in app:
        failures.append("Web app does not render direct note-to-book controls")
    if 'href="#note=${encodeURIComponent(noteId)}"' not in app:
        failures.append("Web app does not render lesson-to-note links")

    if failures:
        print(f"FAIL count={len(failures)}")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1
    print(
        f"PASS teaching_files={len(TEACHING_FILES)} standard=lesson-authoring-v1 "
        "humanizer=3.1.0 lesson-note-book-links=complete"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Validate the DA/DE L001 editorial pass and governed Library navigation."""
from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
LESSONS = [
    ROOT / "Material/DA/Curriculum/Phase_01-foundations-and-role/Module_01-introduction-to-the-data-analyst-role/Lesson_001-what-a-data-analyst-actually-does-all-day",
    ROOT / "Material/DE/Curriculum/Phase_01-engineering-foundation/Module_01-engineering-thinking-git-and-debugging/Lesson_001-from-a-vague-request-to-a-testable-contract",
]
PUBLIC_ASSETS = ("note.md", "teaching.md", "slides.md", "quiz.md", "homework.md", "after-note.md")
FORBIDDEN_TYPOGRAPHY = re.compile(r"[“”‘’—–]")
FORBIDDEN_ORNAMENT = re.compile(
    r"\b(?:huyền\s+diệu|mỹ\s+miều|ma\s+thuật|chìa\s+khóa\s+vạn\s+năng|"
    r"mang\s+tính\s+cách\s+mạng|đột\s+phá|tuyệt\s+đỉnh|vũ\s+trụ)\b",
    re.I,
)
DECORATIVE_ICON = re.compile(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]")
PUBLIC_DURATION = re.compile(
    r"thoi_gian_uoc_tinh|thời\s+lượng\s+(?:học|bài|buổi)|"
    r"thời\s+gian\s+ước\s+tính|120\s*phút",
    re.I,
)


def main() -> int:
    failures: list[str] = []
    for lesson in LESSONS:
        note = (lesson / "note.md").read_text()
        teaching = (lesson / "teaching.md").read_text()
        if note.count("[[wiki.") < 3:
            failures.append(f"{lesson.name}: fewer than three Second Brain references")
        if len(re.findall(r"\b\w+[\w-]*\b", teaching, re.U)) < 1800:
            failures.append(f"{lesson.name}: teaching version is not deep enough")
        if teaching.count("[[wiki.") < 3:
            failures.append(f"{lesson.name}: teaching version lacks Second Brain references")
        for heading in ("Dừng và hỏi", "Kiểm tra hiểu bài", "Điều cần mang theo"):
            if not re.search(rf"(?m)^##+\s+{re.escape(heading)}\s*$", teaching):
                failures.append(f"{lesson.name}: teaching version missing {heading}")
        if "```" not in teaching:
            failures.append(f"{lesson.name}: teaching version lacks a concrete code or artifact example")
        for filename in PUBLIC_ASSETS:
            path = lesson / filename
            text = path.read_text()
            for label, pattern in (
                ("long dash or curly quote", FORBIDDEN_TYPOGRAPHY),
                ("ornamental language", FORBIDDEN_ORNAMENT),
                ("decorative icon", DECORATIVE_ICON),
                ("public lesson duration", PUBLIC_DURATION),
            ):
                match = pattern.search(text)
                if match:
                    line = text.count("\n", 0, match.start()) + 1
                    failures.append(f"{path.relative_to(ROOT)}:{line}: {label}: {match.group(0)!r}")

    index = json.loads((ROOT / "Apps/SecondBrain/web/data/brain-index.json").read_text())
    books = index.get("books") or []
    sources = {item["id"]: item for item in index.get("sources") or []}
    notes = index.get("notes") or []
    if len(books) < 1:
        failures.append("Library has no books")
    if any("canonicalPath" in book for book in books):
        failures.append("Library exposes a private canonical path")
    book_ids = {book["id"] for book in books}
    for note in notes:
        for source_id in note["sourceIds"]:
            source = sources.get(source_id)
            if source and source.get("bookId") and source["bookId"] not in book_ids:
                failures.append(f"{note['id']}: dangling book source {source_id}")

    app = (ROOT / "Apps/SecondBrain/web/app.js").read_text()
    html = (ROOT / "Apps/SecondBrain/web/index.html").read_text()
    if 'data-space="library"' not in html or "async function openBook" not in app:
        failures.append("Library navigation is incomplete")
    if re.search(r"durationMinutes}\s*(?:phút|′)", app):
        failures.append("Lesson duration remains visible in the web UI")

    if failures:
        print(f"FAIL count={len(failures)}")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1
    print(
        f"PASS lessons=2 public_assets=12 books={len(books)} "
        "wiki-links=present typography=clean duration-ui=absent private-paths=absent"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

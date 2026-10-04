#!/usr/bin/env python3
"""Validate the portal-wide editorial and navigation contract."""
from __future__ import annotations

import json
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[3]
INDEX = ROOT / "Apps/SecondBrain/web/data/brain-index.json"
TYPOGRAPHY = re.compile(r"[“”‘’—–]")
ORNAMENT = re.compile(
    r"huyền\s+diệu|huyền\s+huyễn|mỹ\s+miều|ma\s+thuật|chìa\s+khóa\s+vạn\s+năng|"
    r"mang\s+tính\s+cách\s+mạng|tuyệt\s+đỉnh|bức\s+tranh\s+toàn\s+cảnh|lăng\s+kính|gỡ\s+nút\s+thắt|cám\s+dỗ",
    re.I,
)
COURSE_TIME = re.compile(
    r"thời\s+gian\s+ước\s+tính|thời\s+lượng\s+(?:học|bài|buổi)|"
    r"Buổi\s+\d+(?:[,.]\d+)?\s*phút|In-class\s*\(|Self-study\s*\(|"
    r"Think[^\n]{0,40}\d+\s*phút|Guided practice[^\n]{0,40}\d+\s*phút|Exit ticket[^\n]{0,40}\d+\s*phút",
    re.I,
)
WIKI_LINK = re.compile(r"\[\[(wiki\.[^|\]]+)\|[^\]]+\]\]")


def prose(text: str) -> str:
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    return re.sub(r"```.*?```", "", text, flags=re.S)


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def inspect_file(path: Path, failures: list[str], require_link: bool = False) -> None:
    text = path.read_text()
    body = prose(text)
    for label, pattern in (("forbidden typography", TYPOGRAPHY), ("ornamental language", ORNAMENT), ("course timing", COURSE_TIME)):
        match = pattern.search(body)
        if match:
            failures.append(f"{path.relative_to(ROOT)}:{line_number(text, match.start())}: {label}: {match.group(0)!r}")
    if require_link and not WIKI_LINK.search(body):
        failures.append(f"{path.relative_to(ROOT)}: missing labeled Second Brain link")


def main() -> int:
    failures: list[str] = []
    roadmaps = sorted((ROOT / "Material/DA/Roadmap").rglob("roadmap.md")) + sorted((ROOT / "Material/DE/Roadmap").rglob("roadmap.md"))
    notes = sorted((ROOT / "Docs/Second-Brain/2_Wiki").rglob("*.md"))
    lesson_dirs = sorted((ROOT / "Material/DA/Curriculum").glob("**/Lesson_00[1-5]-*")) + sorted((ROOT / "Material/DE/Curriculum").glob("**/Lesson_00[1-5]-*"))

    if len(roadmaps) != 56:
        failures.append(f"roadmap inventory changed: {len(roadmaps)}")
    if len(notes) != 645:
        failures.append(f"Second Brain inventory changed: {len(notes)}")
    if len(lesson_dirs) != 10:
        failures.append(f"lesson inventory changed: {len(lesson_dirs)}")

    for path in roadmaps:
        inspect_file(path, failures, require_link="Module_" in path.as_posix())

    for path in notes:
        inspect_file(path, failures)
        text = path.read_text()
        fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        data = yaml.safe_load(fm.group(1)) if fm else {}
        body = prose(text)
        if data.get("editorial_pass") != "humanized-v3":
            failures.append(f"{path.relative_to(ROOT)}: missing humanized-v3 evidence")
        if len(re.findall(r"\b\w+[\w-]*\b", body, re.U)) < 1800:
            failures.append(f"{path.relative_to(ROOT)}: fewer than 1800 words")
        if "```mermaid" not in text:
            failures.append(f"{path.relative_to(ROOT)}: missing explanatory diagram")

    for directory in lesson_dirs:
        manifest = yaml.safe_load((directory / "lesson.yaml").read_text()) or {}
        editorial = manifest.get("editorial") or {}
        if editorial.get("humanizer") != "blader/humanizer@3.1.0" or editorial.get("status") != "pass":
            failures.append(f"{directory.relative_to(ROOT)}/lesson.yaml: missing Humanizer evidence")
        if "duration_minutes_estimate" in manifest or any("minutes" in scene for scene in manifest.get("scenes") or []):
            failures.append(f"{directory.relative_to(ROOT)}/lesson.yaml: course timing remains")
        for name in ("note.md", "slides.md", "quiz.md", "homework.md", "after-note.md"):
            inspect_file(directory / name, failures, require_link=True)
        teaching = directory / "teaching.md"
        if teaching.exists():
            inspect_file(teaching, failures, require_link=True)

    index = json.loads(INDEX.read_text())
    notes_by_id = {item["id"]: item for item in index["notes"]}
    sources = {item["id"]: item for item in index["sources"]}
    books = {item["id"] for item in index["books"]}
    for note in index["notes"]:
        for source_id in note["sourceIds"]:
            book_id = sources.get(source_id, {}).get("bookId")
            if book_id and book_id not in books:
                failures.append(f"{note['id']}: unresolved book source {book_id}")
    for lesson in index["lessons"]:
        for asset in lesson["assets"]:
            for note_id in WIKI_LINK.findall(asset["body"]):
                if note_id not in notes_by_id:
                    failures.append(f"{lesson['id']}/{asset['key']}: unresolved Second Brain link {note_id}")

    app = (ROOT / "Apps/SecondBrain/web/app.js").read_text()
    html = (ROOT / "Apps/SecondBrain/web/index.html").read_text()
    builder = (ROOT / "Apps/SecondBrain/tools/build_index.py").read_text()
    forbidden_ui = re.compile(r"Bài giảng|Thư viện sách|Giáo trình|Bản giảng dạy|Bài tập|Sau buổi học")
    for path, text in (("app.js", app), ("index.html", html), ("build_index.py", builder)):
        if forbidden_ui.search(text):
            failures.append(f"{path}: Vietnamese title remains")
    if 'data-open-book="${escapeHtml(source.bookId)}"' not in app:
        failures.append("app.js: note-to-book control missing")

    if failures:
        print(f"FAIL count={len(failures)}")
        print("\n".join(f"- {failure}" for failure in failures[:200]))
        return 1
    print(
        f"PASS roadmaps={len(roadmaps)} notes={len(notes)} lessons={len(lesson_dirs)} "
        "humanizer=blader/humanizer@3.1.0 links=resolved ui_titles=english"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

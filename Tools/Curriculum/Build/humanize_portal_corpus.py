#!/usr/bin/env python3
"""Apply the final Humanizer editorial pass to content published by the portal.

The pass is intentionally conservative. It edits prose while preserving YAML
frontmatter and fenced code. Technical time semantics such as event time,
timeouts, retention and SLO thresholds remain intact. Course schedules and
estimated study durations are removed.
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[3]
WIKI = ROOT / "Docs/Second-Brain/2_Wiki"
ROADMAP_ROOTS = (ROOT / "Material/DA/Roadmap", ROOT / "Material/DE/Roadmap")
LESSON_ROOTS = (
    ROOT / "Material/DA/Curriculum/Phase_01-foundations-and-role/Module_01-introduction-to-the-data-analyst-role",
    ROOT / "Material/DE/Curriculum/Phase_01-engineering-foundation/Module_01-engineering-thinking-git-and-debugging",
)


def split_frontmatter(text: str) -> tuple[str, str]:
    match = re.match(r"^(---\n.*?\n---\n)", text, re.S)
    return (match.group(1), text[match.end():]) if match else ("", text)


def prose_transform(text: str, transform) -> str:
    frontmatter, body = split_frontmatter(text)
    parts = re.split(r"(```.*?```)", body, flags=re.S)
    for index in range(0, len(parts), 2):
        parts[index] = transform(parts[index])
    return frontmatter + "".join(parts)


def editorial_prose(text: str) -> str:
    paired = (
        (r"“([^”\n]+)”", r"\1"),
        (r"‘([^’\n]+)’", r"\1"),
    )
    for pattern, replacement in paired:
        text = re.sub(pattern, replacement, text)
    text = text.translate(str.maketrans({"“": "", "”": "", "‘": "", "’": "", "—": ":", "–": "-"}))
    text = re.sub(r"[ \t]+:[ \t]+", ": ", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    replacements = {
        "## Nỗi Đau & Động Lực": "## Problem Definition and Operational Relevance",
        "## Cơ Chế Tác Động": "## Mechanism",
        "## Bản Đồ Quyết Định": "## Decision Framework",
        "## Góc Khuất & Ngộ Nhận": "## Limits and Common Errors",
        "cám dỗ lớn nhất": "rủi ro trực tiếp",
        " là lăng kính dùng để gỡ nút thắt": " là khung phân tích dùng để xác định sai lệch",
        "điều quan trọng là": "yêu cầu bắt buộc là",
        "Điều quan trọng là": "Yêu cầu bắt buộc là",
    }
    for source, target in replacements.items():
        text = text.replace(source, target)
    text = re.sub(r"(?m)^## Case Study Thực Chiến(?=:|$)", "## Worked Case", text)
    return text


def remove_course_timing(text: str) -> str:
    text = re.sub(r"(?m)^\*\*In-class \([^\n]+\)\.\*\*[^\n]*\n?", "", text)
    text = re.sub(r"(?m)^\*\*Self-study \([^\n]+\)\.\*\*[^\n]*\n?", "", text)
    text = re.sub(r"Buổi\s+\d+(?:[,.]\d+)?\s*phút\s*:[^.]*\.\s*", "", text, flags=re.I)
    text = re.sub(
        r"Trình bày\s+\d+\s*phút,\s*hỏi đáp\s+\d+\s*phút,\s*nhận xét hội đồng\s+\d+\s*phút\.?",
        "Trình bày, bảo vệ dưới chất vấn và nhận xét hội đồng.",
        text,
        flags=re.I,
    )
    text = re.sub(r"phỏng vấn trong\s+\d+\s*phút", "phỏng vấn theo bộ câu hỏi chuẩn", text, flags=re.I)
    text = re.sub(r"(?m)^\*\*Thời gian ước tính:\*\*[^\n]*\n?", "", text)
    return text


def note_title_index() -> dict[str, str]:
    result: dict[str, str] = {}
    duplicates: set[str] = set()
    for path in WIKI.rglob("*.md"):
        frontmatter, body = split_frontmatter(path.read_text())
        if not frontmatter:
            continue
        data = yaml.safe_load(frontmatter.removeprefix("---\n").removesuffix("---\n")) or {}
        note_id = str(data.get("note_id") or "")
        title_match = re.search(r"(?m)^#\s+(.+)$", body)
        if not note_id or not title_match:
            continue
        title = title_match.group(1).strip()
        key = title.casefold()
        if key in result:
            duplicates.add(key)
        else:
            result[key] = note_id
    for key in duplicates:
        result.pop(key, None)
    return result


def link_roadmap_lessons(text: str, titles: dict[str, str]) -> str:
    line_pattern = re.compile(r"(L\d{3}\s*·\s*)([^|\n]+)")

    def replace_line(match: re.Match[str]) -> str:
        title = match.group(2).strip()
        if "[[" in title:
            return match.group(0)
        note_id = titles.get(title.casefold())
        return f"{match.group(1)}[[{note_id}|{title}]]" if note_id else match.group(0)

    text = line_pattern.sub(replace_line, text)
    text = re.sub(r"(?m)^### Bài (\d+):", r"### Lesson \1:", text)
    return text


def write_if_changed(path: Path, updated: str) -> bool:
    current = path.read_text()
    if updated == current:
        return False
    path.write_text(updated)
    return True


def mark_humanized_v3(text: str) -> str:
    if re.search(r"(?m)^editorial_pass:\s*", text):
        return re.sub(r"(?m)^editorial_pass:\s*.*$", "editorial_pass: humanized-v3", text, count=1)
    return re.sub(r"(?m)^(last_verified:\s*.*)$", r"\1\neditorial_pass: humanized-v3", text, count=1)


def sync_reference_mirror(text: str) -> bool:
    frontmatter, _ = split_frontmatter(text)
    if not frontmatter:
        return False
    data = yaml.safe_load(frontmatter.removeprefix("---\n").removesuffix("---\n")) or {}
    reference_path = data.get("reference_path")
    if not reference_path:
        return False
    target = (ROOT / str(reference_path)).resolve()
    target.relative_to(ROOT.resolve())
    if not target.is_file():
        raise FileNotFoundError(target)
    return write_if_changed(target, text)


def ensure_lesson_reference(text: str, lesson_title: str, titles: dict[str, str], fallback_id: str) -> str:
    if re.search(r"\[\[wiki\.[^|\]]+\|[^\]]+\]\]", text):
        return text
    note_id = titles.get(lesson_title.casefold()) or fallback_id
    if not note_id:
        return text
    return text.rstrip() + f"\n\n## References\n\n- [[{note_id}|{lesson_title}]]\n"


def main() -> int:
    changed: list[Path] = []
    titles = note_title_index()

    for path in sorted(WIKI.rglob("*.md")):
        text = path.read_text()
        updated = prose_transform(text, lambda value: remove_course_timing(editorial_prose(value)))
        updated = mark_humanized_v3(updated)
        if write_if_changed(path, updated):
            changed.append(path)
        if sync_reference_mirror(updated):
            changed.append((ROOT / str((yaml.safe_load(split_frontmatter(updated)[0].removeprefix("---\n").removesuffix("---\n")) or {})["reference_path"])))

    for root in ROADMAP_ROOTS:
        for path in sorted(root.rglob("roadmap.md")):
            text = path.read_text()
            updated = prose_transform(text, lambda value: link_roadmap_lessons(remove_course_timing(editorial_prose(value)), titles))
            if write_if_changed(path, updated):
                changed.append(path)

    for root in LESSON_ROOTS:
        for directory in sorted(root.glob("Lesson_00[1-5]-*")):
            manifest = yaml.safe_load((directory / "lesson.yaml").read_text()) or {}
            lesson_title = str(manifest.get("title") or directory.name)
            fallback_id = {
                "DA-L001": "wiki.da.operating-as-a-data-analyst",
                "DE-L002": "wiki.engineering-foundation.decomposition-four-axes",
            }.get(str(manifest.get("lesson_id")), "")
            for name in ("note.md", "teaching.md", "slides.md", "quiz.md", "homework.md", "after-note.md"):
                path = directory / name
                if not path.is_file():
                    continue
                text = path.read_text()
                updated = prose_transform(text, lambda value: remove_course_timing(editorial_prose(value)))
                updated = ensure_lesson_reference(updated, lesson_title, titles, fallback_id)
                if write_if_changed(path, updated):
                    changed.append(path)

    print(f"humanizer-pass changed={len(changed)} wiki={len(list(WIKI.rglob('*.md')))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

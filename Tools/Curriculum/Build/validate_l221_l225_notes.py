#!/usr/bin/env python3
"""Validate L221-L225 depth, lineage, distinctions and Wiki parity."""
from __future__ import annotations

import re

from promote_l221_l225_notes import LESSONS, PACK, ROOT, WIKI, folder


def source_ids(text: str) -> list[str]:
    match = re.search(r"(?ms)^source_ids:\n(.*?)(?=^[a-z_]+:|^---$)", text)
    return re.findall(r"(?m)^\s*-\s+(\S+)$", match.group(1)) if match else []


def main() -> int:
    failures: list[str] = []
    known: set[str] = set()
    for path in (ROOT / "Docs/Second-Brain/1_Nguon").rglob("*.md"):
        match = re.search(r"(?m)^source_id:\s*(\S+)$", path.read_text())
        if match:
            known.add(match.group(1))
    required = {
        221: ("row group", "column chunk", "data pages", "footer", "transferred bytes"),
        222: ("Projection pushdown", "ColumnIndex", "OffsetIndex", "secondary index", "interaction"),
        223: ("definition levels", "repetition levels", "INT96", "unscaled integer", "W_A→R_B"),
        224: ("Object store", "File format", "Table format", "atomic swap", "multi-table"),
        225: ("current metadata location", "manifest list", "manifest entry", "field IDs", "visible in snapshot"),
    }
    headings = ("## Reference", "## Source coverage", "## Key takeaways", "## 7. Ma trận kiểm chứng từng mệnh đề", "## 9. Câu hỏi tự kiểm tra", "## 10. Giới hạn và điều chưa cho phép kết luận")
    prefix = "# Phase 6: Analytical Storage and Query Engines\n# Module 15: File, Serialization and Open Table Formats\n"
    protected = ("quiz.md", "homework.md", "slides.md", "lesson.yaml")
    for lesson in LESSONS:
        reference = PACK / lesson.filename
        if not reference.exists():
            failures.append(f"L{lesson.number}: thiếu Reference note")
            continue
        knowledge = reference.read_text()
        wiki = WIKI / f"{lesson.title}.md"
        note_path = folder(lesson) / "note.md"
        after_path = folder(lesson) / "after-note.md"
        if not note_path.exists() or not after_path.exists():
            failures.append(f"L{lesson.number}: thiếu note.md hoặc after-note.md")
            continue
        note = note_path.read_text()
        after = after_path.read_text()
        expected = prefix + f"# Lesson {lesson.number}: {lesson.title}\n"
        if not note.startswith(expected) or not after.startswith(expected):
            failures.append(f"L{lesson.number}: sai hierarchy")
        words = len(re.findall(r"\b\w+[\w-]*\b", knowledge, re.UNICODE))
        if words < 2200:
            failures.append(f"L{lesson.number}: chỉ có {words} từ")
        for heading in headings:
            if heading not in knowledge:
                failures.append(f"L{lesson.number}: thiếu {heading}")
        for term in required[lesson.number]:
            if term.lower() not in knowledge.lower():
                failures.append(f"L{lesson.number}: thiếu distinction {term}")
        unknown = set(source_ids(knowledge)) - known
        if unknown:
            failures.append(f"L{lesson.number}: source ID lạ {sorted(unknown)}")
        if not wiki.exists() or wiki.read_bytes() != reference.read_bytes():
            failures.append(f"L{lesson.number}: Wiki lệch Reference")
        for name in protected:
            if not (folder(lesson) / name).exists():
                failures.append(f"L{lesson.number}: tệp ngoài phạm vi biến mất {name}")
    if failures:
        print("FAIL\n" + "\n".join("- " + failure for failure in failures))
        return 1
    print("PASS lessons=5 curriculum_files=10 knowledge_notes=5 min_words=2200 wiki_parity=5/5 parquet-iceberg-boundaries=checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

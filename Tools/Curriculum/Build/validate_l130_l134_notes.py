#!/usr/bin/env python3
"""Validate DE L130-L134 curriculum, Reference and Wiki artifacts."""
from __future__ import annotations

import re

from promote_l130_l134_notes import LESSONS, PACK, ROOT, folder

WIKI = {
    130: "Reading EXPLAIN ANALYZE with Buffers.md",
    131: "Sargability Parameters and Plan Stability.md",
    132: "SQL Tuning Project - Five Slow Queries.md",
    133: "Pages Heap Files and Buffer Pool.md",
    134: "B-tree Internals - Fanout Splits and Clustering.md",
}


def source_ids(text: str) -> list[str]:
    block = re.search(r"(?ms)^source_ids:\n(.*?)(?=^[a-z_]+:|^---$)", text)
    return re.findall(r"(?m)^\s*-\s+(\S+)$", block.group(1)) if block else []


def main() -> int:
    failures: list[str] = []
    known_sources: set[str] = set()
    for path in (ROOT / "Docs/Second-Brain/1_Nguon").rglob("*.md"):
        match = re.search(r"(?m)^source_id:\s*(\S+)$", path.read_text(encoding="utf-8"))
        if match:
            known_sources.add(match.group(1))
    for lesson in LESSONS:
        note = (folder(lesson) / "note.md").read_text(encoding="utf-8")
        after = (folder(lesson) / "after-note.md").read_text(encoding="utf-8")
        knowledge_path = ROOT / PACK / lesson.source
        knowledge = knowledge_path.read_text(encoding="utf-8")
        prefix = (
            "# Phase 4: SQL and Database Internals\n"
            f"# Module {lesson.module_number}: {lesson.module_title}\n"
            f"# Lesson {lesson.number}: {lesson.title}\n"
        )
        if not note.startswith(prefix) or not after.startswith(prefix):
            failures.append(f"L{lesson.number}: hierarchy")
        for obsolete in ("trang_thai: chua-viet", "Trạng thái: chưa viết", "thoi_luong_phut:", "## I. Mục tiêu"):
            if obsolete in note + after:
                failures.append(f"L{lesson.number}: scaffold {obsolete}")
        for heading in ("## Mục tiêu bài học", "## Source coverage", "## Key takeaways", "## Reference"):
            if heading not in note:
                failures.append(f"L{lesson.number}: thiếu {heading}")
        for heading in ("## Thực hành", "## Kiểm tra cuối bài", "## Tiêu chí hoàn thành", "## Bài làm sau buổi học", "## Reference"):
            if heading not in after:
                failures.append(f"L{lesson.number}: after thiếu {heading}")
        if any(source_id not in known_sources for source_id in source_ids(knowledge)):
            failures.append(f"L{lesson.number}: source lạ")
        wiki_path = ROOT / "Docs/Second-Brain/2_Wiki/Database-Systems" / WIKI[lesson.number]
        if not wiki_path.exists() or wiki_path.read_bytes() != knowledge_path.read_bytes():
            failures.append(f"L{lesson.number}: Wiki lệch")
    if failures:
        print("FAIL\n" + "\n".join(f"- {failure}" for failure in failures))
        return 1
    print("PASS lessons=5 files=10 knowledge_notes=5")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

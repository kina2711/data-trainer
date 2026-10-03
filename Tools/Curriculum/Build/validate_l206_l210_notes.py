#!/usr/bin/env python3
"""Validate L206-L210 depth, lineage, distinctions and Wiki parity."""
from __future__ import annotations

import re

from promote_l206_l210_notes import LESSONS, PACK, ROOT, WIKI, folder


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
        206: ("false positive", "fail open", "filter pushdown không chứng minh", "dynamic filter đến trễ"),
        207: ("selection vector", "high selectivity", "encoded execution", "JIT khác vectorized execution"),
        208: ("ba tầng", "factorial design", "interaction", "floating reduction"),
        209: ("High cardinality là risk", "Small-file penalty", "file size distribution", "clustering degrade"),
        210: ("Exchange không phải network duy nhất", "compatible partition contract", "Strong scaling", "plan estimate không thay"),
    }
    forbidden_files = ("quiz.md", "homework.md", "slides.md", "lesson.yaml")
    prefix_root = "# Phase 6: Analytical Storage and Query Engines\n# Module 14: OLAP Internals and Analytical Engines\n"
    for lesson in LESSONS:
        reference = PACK / lesson.filename
        knowledge = reference.read_text()
        wiki = WIKI / f"{lesson.title}.md"
        note = (folder(lesson) / "note.md").read_text()
        after = (folder(lesson) / "after-note.md").read_text()
        prefix = prefix_root + f"# Lesson {lesson.number}: {lesson.title}\n"
        if not note.startswith(prefix) or not after.startswith(prefix):
            failures.append(f"L{lesson.number}: sai hierarchy")
        words = len(re.findall(r"\b\w+[\w-]*\b", knowledge, re.UNICODE))
        if words < 2200:
            failures.append(f"L{lesson.number}: chỉ có {words} từ")
        for heading in (
            "## Reference",
            "## Source coverage",
            "## Key takeaways",
            "## 8. Ma trận kiểm chứng từng mệnh đề",
            "## 10. Câu hỏi tự kiểm tra",
            "## 11. Giới hạn và điều chưa cho phép kết luận",
        ):
            if heading not in knowledge:
                failures.append(f"L{lesson.number}: thiếu {heading}")
        for term in required[lesson.number]:
            if term.lower() not in knowledge.lower():
                failures.append(f"L{lesson.number}: thiếu distinction {term}")
        for bad in (
            "trang_thai: chua-viet",
            "Trạng thái: chưa viết",
            "thoi_luong_phut:",
            "## I. Mục tiêu",
            "Tóm tắt",
            "không phải X mà là Y",
        ):
            if bad in note + after:
                failures.append(f"L{lesson.number}: còn scaffold/pattern {bad}")
        unknown = set(source_ids(knowledge)) - known
        if unknown:
            failures.append(f"L{lesson.number}: source ID lạ {sorted(unknown)}")
        if not wiki.exists() or wiki.read_bytes() != reference.read_bytes():
            failures.append(f"L{lesson.number}: Wiki lệch Reference")
        for name in forbidden_files:
            if not (folder(lesson) / name).exists():
                failures.append(f"L{lesson.number}: tệp ngoài phạm vi biến mất {name}")
    if failures:
        print("FAIL\n" + "\n".join("- " + failure for failure in failures))
        return 1
    print("PASS lessons=5 curriculum_files=10 knowledge_notes=5 min_words=2200 wiki_parity=5/5 pruning-vectorization-layout-mpp=checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

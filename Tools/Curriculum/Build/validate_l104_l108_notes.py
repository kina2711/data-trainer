#!/usr/bin/env python3
"""Validate knowledge and curriculum artifacts for DE-L104 through DE-L108."""

from __future__ import annotations

import re
from pathlib import Path

from promote_l104_l108_notes import LESSONS, PACK, ROOT, lesson_dir


def source_ids(text: str) -> list[str]:
    block = re.search(r"(?ms)^source_ids:\n(.*?)(?=^[a-z_]+:|^---$)", text)
    return re.findall(r"(?m)^\s*-\s+([^\s]+)$", block.group(1)) if block else []


def known_sources() -> set[str]:
    found = set()
    for path in (ROOT / "Docs/Second-Brain/1_Nguon").rglob("*.md"):
        match = re.search(r"(?m)^source_id:\s*(\S+)$", path.read_text(encoding="utf-8"))
        if match:
            found.add(match.group(1))
    return found


def main() -> int:
    failures = []
    sources = known_sources()
    wiki_targets = {
        104: ROOT / "Docs/Second-Brain/2_Wiki/Backend-Engineering/Concurrency Control - Optimistic and Pessimistic.md",
        105: ROOT / "Docs/Second-Brain/2_Wiki/Backend-Engineering/Idempotency Keys and Deduplication State.md",
        106: ROOT / "Docs/Second-Brain/2_Wiki/Security/Authentication Authorization and Ownership Checks.md",
        107: ROOT / "Docs/Second-Brain/2_Wiki/Distributed-Systems/Timeouts Circuit Breakers and Bulkheads.md",
        108: ROOT / "Docs/Second-Brain/2_Wiki/Backend-Engineering/API Observability - RED Metrics and Tracing.md",
    }
    for lesson in LESSONS:
        directory = lesson_dir(lesson)
        note = (directory / "note.md").read_text(encoding="utf-8")
        after = (directory / "after-note.md").read_text(encoding="utf-8")
        knowledge_path = PACK / lesson.source
        knowledge = knowledge_path.read_text(encoding="utf-8")
        prefix = f"# Phase 3: Software and Backend Engineering\n# Module 8: Backend and API Engineering\n# Lesson {lesson.number}: {lesson.title}\n"
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
        missing = [source for source in source_ids(knowledge) if source not in sources]
        if missing:
            failures.append(f"L{lesson.number}: source_id chưa có record {missing}")
        wiki = wiki_targets[lesson.number]
        if not wiki.exists() or wiki.read_bytes() != knowledge_path.read_bytes():
            failures.append(f"L{lesson.number}: bản Wiki không giống Reference")
    if failures:
        print("FAIL")
        print("\n".join(f"- {item}" for item in failures))
        return 1
    print(f"PASS lessons={len(LESSONS)} files={len(LESSONS) * 2} knowledge_notes={len(LESSONS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
from __future__ import annotations

import importlib
import json
import re
import sys

from promote_l006_l050_common import MANIFEST, MODULES, PACK, ROOT


REQUIRED_HEADINGS = (
    "## Nỗi Đau & Động Lực",
    "## Cơ Chế Tác Động",
    "## Bản Đồ Quyết Định",
    "## Góc Khuất & Ngộ Nhận",
    "## Nếu Bạn Dạy Lại Điều Này...",
    "## Ma trận kiểm chứng từng mệnh đề",
    "## Tự Kiểm Tra Nhanh",
    "## Giới hạn và điều chưa cho phép kết luận",
    "## Reference",
    "## Source coverage",
    "## Key takeaways",
)


def main(module_name: str) -> int:
    lessons = importlib.import_module(module_name).LESSONS
    manifest = json.loads(MANIFEST.read_text())
    registered_sources = {row["source_id"] for row in manifest["source_registry"]}
    registered_notes = {row["note_id"]: row for row in manifest["note_registry"]}
    retrieval = {(row["query"], row["expected_note_id"]) for row in manifest["retrieval_test_set"]}
    failures: list[str] = []
    counts: list[int] = []

    for lesson in lessons:
        reference = PACK / lesson.filename
        if not reference.exists():
            failures.append(f"L{lesson.number}: missing Reference note")
            continue
        text = reference.read_text()
        words = len(re.findall(r"\b\w+[\w-]*\b", text, re.UNICODE))
        counts.append(words)
        if words < 2200:
            failures.append(f"L{lesson.number}: only {words} words")
        for heading in REQUIRED_HEADINGS:
            if heading not in text:
                failures.append(f"L{lesson.number}: missing {heading}")
        for marker in ("editorial_pass: humanized-v3", "concept_key_status: proposed", "**Hiểu lầm:**", "**Vì sao nghe hợp lý:**"):
            if marker not in text:
                failures.append(f"L{lesson.number}: missing `{marker}`")
        unknown = set(lesson.sources) - registered_sources
        if unknown:
            failures.append(f"L{lesson.number}: unregistered sources {sorted(unknown)}")
        for source_id in lesson.sources:
            if f"— `{source_id}` |" not in text:
                failures.append(f"L{lesson.number}: source coverage missing {source_id}")
        if not lesson.wiki.exists() or lesson.wiki.read_bytes() != reference.read_bytes():
            failures.append(f"L{lesson.number}: Wiki differs")
        expected_header = (
            "# Phase 1: Engineering Foundation\n"
            f"# Module {lesson.module}: {MODULES[lesson.module]}\n"
            f"# Lesson {lesson.number}: {lesson.title}\n"
        )
        curriculum = (lesson.folder / "note.md").read_text()
        after = (lesson.folder / "after-note.md").read_text()
        if not curriculum.startswith(expected_header) or not after.startswith(expected_header):
            failures.append(f"L{lesson.number}: wrong curriculum hierarchy")
        if "chua-viet" in curriculum or "chưa viết" in curriculum.lower():
            failures.append(f"L{lesson.number}: skeleton marker remains")
        expected_registry = {
            "note_id": lesson.note_id,
            "path": f"2_Wiki/{lesson.wiki.parent.name}/{lesson.title}.md",
            "status": "review",
            "source_ids": list(lesson.sources),
            "last_verified": "2026-10-02",
        }
        if registered_notes.get(lesson.note_id) != expected_registry:
            failures.append(f"L{lesson.number}: manifest note drift")
        for query in (
            f"L{lesson.number} decision boundary nào?",
            f"L{lesson.number} counterexample nào?",
            f"L{lesson.number} evidence nào quyết định?",
        ):
            if (query, lesson.note_id) not in retrieval:
                failures.append(f"L{lesson.number}: missing retrieval `{query}`")

    if failures:
        print("FAIL\n" + "\n".join(f"- {item}" for item in failures))
        return 1
    print(
        f"PASS lessons={len(lessons)} min_words={min(counts)} max_words={max(counts)} "
        f"wiki_parity={len(lessons)}/{len(lessons)} manifest=checked humanizer=humanized-v3"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))

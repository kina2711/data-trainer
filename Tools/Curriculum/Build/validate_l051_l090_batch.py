#!/usr/bin/env python3
from __future__ import annotations

import importlib
import json
import re
import sys

from promote_l051_l090_common import MANIFEST, MODULES, PACK, PHASES, WIKI_DIR

REQUIRED = (
    "## Nỗi Đau & Động Lực", "## Cơ Chế Tác Động", "## Bản Đồ Quyết Định",
    "## Case Study Thực Chiến:", "## Góc Khuất & Ngộ Nhận",
    "## Nếu Bạn Dạy Lại Điều Này...", "## Ma trận kiểm chứng từng mệnh đề",
    "## Tự Kiểm Tra Nhanh", "## Giới hạn và điều chưa cho phép kết luận",
    "## Reference", "## Source coverage", "## Key takeaways",
)


def main(module_name: str) -> int:
    lessons = importlib.import_module(module_name).LESSONS
    manifest = json.loads(MANIFEST.read_text())
    source_ids = {row["source_id"] for row in manifest["source_registry"]}
    notes = {row["note_id"]: row for row in manifest["note_registry"]}
    retrieval = {(row["query"], row["expected_note_id"]) for row in manifest["retrieval_test_set"]}
    failures: list[str] = []
    counts: list[int] = []
    for lesson in lessons:
        reference = PACK / lesson.filename
        if not reference.exists():
            failures.append(f"L{lesson.number}: missing Reference")
            continue
        text = reference.read_text()
        words = len(re.findall(r"\b\w+[\w-]*\b", text, re.UNICODE))
        counts.append(words)
        if words < 2200: failures.append(f"L{lesson.number}: only {words} words")
        for heading in REQUIRED:
            if heading not in text: failures.append(f"L{lesson.number}: missing {heading}")
        for marker in ("editorial_pass: humanized-v3", "concept_key_status: proposed", "**Hiểu lầm:**", "**Thực tế:**", "**Vì sao nghe hợp lý:**"):
            if marker not in text: failures.append(f"L{lesson.number}: missing {marker}")
        unknown = set(lesson.sources) - source_ids
        if unknown: failures.append(f"L{lesson.number}: unregistered sources {sorted(unknown)}")
        for source in lesson.sources:
            if f"— `{source}` |" not in text: failures.append(f"L{lesson.number}: coverage missing {source}")
        if not lesson.wiki.exists() or lesson.wiki.read_bytes() != reference.read_bytes(): failures.append(f"L{lesson.number}: Wiki differs")
        header = f"# Phase {lesson.phase}: {PHASES[lesson.phase]}\n# Module {lesson.module}: {MODULES[lesson.module]}\n# Lesson {lesson.number}: {lesson.title}\n"
        if not (lesson.folder / "note.md").read_text().startswith(header): failures.append(f"L{lesson.number}: note hierarchy")
        if not (lesson.folder / "after-note.md").read_text().startswith(header): failures.append(f"L{lesson.number}: after-note hierarchy")
        expected = {"note_id": lesson.note_id, "path": f"2_Wiki/{WIKI_DIR[lesson.module]}/{lesson.title}.md", "status": "review", "source_ids": list(lesson.sources), "last_verified": "2026-10-02"}
        if notes.get(lesson.note_id) != expected: failures.append(f"L{lesson.number}: manifest drift")
        for query in (f"L{lesson.number} decision boundary nào?", f"L{lesson.number} counterexample nào?", f"L{lesson.number} evidence nào quyết định?"):
            if (query, lesson.note_id) not in retrieval: failures.append(f"L{lesson.number}: retrieval missing")
    if failures:
        print("FAIL\n" + "\n".join(f"- {item}" for item in failures)); return 1
    print(f"PASS lessons={len(lessons)} min_words={min(counts)} max_words={max(counts)} wiki_parity={len(lessons)}/{len(lessons)} manifest=checked humanizer=humanized-v3")
    return 0


if __name__ == "__main__": raise SystemExit(main(sys.argv[1]))

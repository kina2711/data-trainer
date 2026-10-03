#!/usr/bin/env python3
import re
from promote_l251_l255_notes import LESSONS
from promote_l251_l270_common import PACK, ROOT, WIKI, folder

REQUIRED = {
    251: ("Watermark", "Allowed lateness", "pane identity"),
    252: ("Isolate workload", "Build candidate", "Promote rollback cleanup"),
    253: ("Parse", "Compile", "Run", "Build"),
    254: ("Staging boundary", "Intermediate", "Marts"),
    255: ("View", "Table", "Incremental", "Ephemeral"),
}

def main():
    failures = []
    known = set()
    for path in (ROOT / "Docs/Second-Brain/1_Nguon").rglob("*.md"):
        match = re.search(r"(?m)^source_id:\s*(\S+)$", path.read_text())
        if match:
            known.add(match.group(1))
    for lesson in LESSONS:
        reference = PACK / lesson.filename
        if not reference.exists():
            failures.append(f"L{lesson.number}: thiếu Reference")
            continue
        text = reference.read_text()
        words = len(re.findall(r"\b\w+[\w-]*\b", text, re.UNICODE))
        if words < 2200:
            failures.append(f"L{lesson.number}: chỉ có {words} từ")
        for heading in ("## Reference", "## Source coverage", "## Key takeaways", "## 7. Ma trận kiểm chứng từng mệnh đề", "## 9. Câu hỏi tự kiểm tra", "## 10. Giới hạn và điều chưa cho phép kết luận"):
            if heading not in text:
                failures.append(f"L{lesson.number}: thiếu {heading}")
        for phrase in REQUIRED[lesson.number]:
            if phrase.lower() not in text.lower():
                failures.append(f"L{lesson.number}: thiếu distinction {phrase}")
        unknown = set(re.findall(r"(?m)^\s*-\s+(src\.\S+)$", text)) - known
        if unknown:
            failures.append(f"L{lesson.number}: source lạ {sorted(unknown)}")
        wiki = WIKI / f"{lesson.title}.md"
        if not wiki.exists() or wiki.read_bytes() != reference.read_bytes():
            failures.append(f"L{lesson.number}: Wiki lệch Reference")
        curriculum = (folder(lesson) / "note.md").read_text()
        expected = f"# Phase 7: Ingestion, Transformation, Quality and Governance\n# Module 17: ELT, dbt and Workflow Orchestration\n# Lesson {lesson.number}: {lesson.title}\n"
        if not curriculum.startswith(expected):
            failures.append(f"L{lesson.number}: sai hierarchy")
    if failures:
        print("FAIL\n" + "\n".join(f"- {item}" for item in failures))
        return 1
    print("PASS lessons=5 min_words=2200 wiki_parity=5/5 time-backfill-dbt-foundations=checked")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

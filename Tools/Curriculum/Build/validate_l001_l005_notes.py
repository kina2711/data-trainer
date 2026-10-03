#!/usr/bin/env python3
from __future__ import annotations

import re
from collections import defaultdict

from promote_l001_l005_notes import LESSONS, PACK, WIKI

BANNED = ("trong bối cảnh hiện đại", "đóng vai trò quan trọng", "không chỉ là một", "trong thế giới ngày nay", "một cách toàn diện")


def paragraphs(text: str) -> list[str]:
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    return [re.sub(r"\s+", " ", p.strip()) for p in re.split(r"\n\s*\n", text) if len(re.sub(r"\s+", " ", p.strip())) >= 240 and not p.lstrip().startswith(("|", "#", "- ", "1. "))]


def main() -> int:
    failures: list[str] = []
    seen: defaultdict[str, list[int]] = defaultdict(list)
    counts: list[int] = []
    for lesson in LESSONS:
        ref = PACK / lesson.filename
        text = ref.read_text() if ref.exists() else ""
        words = len(re.findall(r"\b\w+[\w-]*\b", text, re.UNICODE))
        counts.append(words)
        if words < 1800:
            failures.append(f"L{lesson.number}: only {words} words")
        for heading in ("## Reference", "## Source coverage", "## Key takeaways", "## 9. Ma trận kiểm chứng", "## 11. Giới hạn và điều chưa cho phép kết luận"):
            if heading not in text:
                failures.append(f"L{lesson.number}: missing {heading}")
        if "editorial_pass: humanized-v3" not in text:
            failures.append(f"L{lesson.number}: missing humanizer v3")
        wiki = WIKI / f"{lesson.title}.md"
        if not wiki.exists() or wiki.read_bytes() != ref.read_bytes():
            failures.append(f"L{lesson.number}: Wiki differs")
        curriculum = (lesson.folder / "note.md").read_text()
        expected = f"# Phase 1: Engineering Foundation\n# Module 1: Engineering Thinking, Git and Debugging\n# Lesson {lesson.number}: {lesson.title}\n"
        if not curriculum.startswith(expected):
            failures.append(f"L{lesson.number}: wrong hierarchy")
        if "chua-viet" in curriculum or "chưa viết" in curriculum:
            failures.append(f"L{lesson.number}: skeleton marker remains")
        local: set[str] = set()
        for paragraph in paragraphs(text):
            if paragraph in local:
                failures.append(f"L{lesson.number}: repeated long paragraph")
            local.add(paragraph)
            seen[paragraph].append(lesson.number)
        for phrase in BANNED:
            if phrase in text.lower():
                failures.append(f"L{lesson.number}: canned phrase `{phrase}`")
    for paragraph, owners in seen.items():
        if len(set(owners)) > 1:
            failures.append(f"cross-note repeat {sorted(set(owners))}: {paragraph[:80]}")
    if failures:
        print("FAIL\n" + "\n".join(f"- {item}" for item in failures))
        return 1
    print(f"PASS lessons=5 min_words={min(counts)} max_words={max(counts)} wiki_parity=5/5 editorial=humanized-v3 cross_note_repeats=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

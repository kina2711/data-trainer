#!/usr/bin/env python3
from __future__ import annotations

import re
from collections import defaultdict

from promote_da_l002_l005_notes import LESSONS, PACK, WIKI


BANNED = (
    "trong bối cảnh hiện đại",
    "đóng vai trò quan trọng",
    "không chỉ là một",
    "trong thế giới ngày nay",
    "một cách toàn diện",
)


def paragraphs(text: str) -> list[str]:
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    return [
        re.sub(r"\s+", " ", paragraph.strip())
        for paragraph in re.split(r"\n\s*\n", text)
        if len(re.sub(r"\s+", " ", paragraph.strip())) >= 240
        and not paragraph.lstrip().startswith(("|", "#", "- ", "1. "))
    ]


def main() -> int:
    failures: list[str] = []
    seen: defaultdict[str, list[int]] = defaultdict(list)
    word_counts: list[int] = []
    for lesson in LESSONS:
        path = PACK / lesson.filename
        text = path.read_text() if path.exists() else ""
        words = len(re.findall(r"\b\w+[\w-]*\b", text, re.UNICODE))
        word_counts.append(words)
        if words < 1800:
            failures.append(f"L{lesson.number}: only {words} words")
        required = (
            "editorial_pass: humanized-v3",
            "concept_key_status: proposed",
            "## Nỗi Đau & Động Lực",
            "## Cơ Chế Tác Động",
            "## Bản Đồ Quyết Định",
            "## Góc Khuất & Ngộ Nhận",
            "**Hiểu lầm:**",
            "**Thực tế:**",
            "**Vì sao nghe hợp lý:**",
            "## Tự Kiểm Tra Nhanh",
            "## Reference",
            "## Source coverage",
        )
        for marker in required:
            if marker not in text:
                failures.append(f"L{lesson.number}: missing {marker}")
        wiki = WIKI / f"{lesson.title}.md"
        if not wiki.exists() or wiki.read_bytes() != path.read_bytes():
            failures.append(f"L{lesson.number}: Wiki differs")
        curriculum = (lesson.folder / "note.md").read_text()
        if "chua-viet" in curriculum.lower() or "chưa viết" in curriculum.lower():
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
    print(
        f"PASS lessons=4 min_words={min(word_counts)} max_words={max(word_counts)} "
        "wiki_parity=4/4 editorial=humanized-v3 cross_note_repeats=0"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

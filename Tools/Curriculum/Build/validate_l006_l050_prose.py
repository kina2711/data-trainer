#!/usr/bin/env python3
from __future__ import annotations

import re
from collections import defaultdict

from promote_l006_l050_common import PACK, load_lesson


TELLS = (
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
    within = tells = 0
    for number in range(6, 51):
        lesson = load_lesson(number)
        path = PACK / lesson.filename
        if not path.exists():
            continue
        text = path.read_text()
        local: set[str] = set()
        for paragraph in paragraphs(text):
            if paragraph in local:
                within += 1
                failures.append(f"L{number}: repeated long paragraph")
            local.add(paragraph)
            seen[paragraph].append(number)
        for tell in TELLS:
            count = text.lower().count(tell)
            tells += count
            if count:
                failures.append(f"L{number}: canned phrase `{tell}`")
    repeated = {paragraph: owners for paragraph, owners in seen.items() if len(set(owners)) > 1}
    failures.extend(f"cross-note repeat {sorted(set(owners))}" for owners in repeated.values())
    if failures:
        print("FAIL\n" + "\n".join(f"- {item}" for item in failures))
        return 1
    checked = sum((PACK / load_lesson(number).filename).exists() for number in range(6, 51))
    print(
        f"PASS checked={checked} editorial=humanized-v3 within_note_repeats={within} "
        f"cross_note_repeats={len(repeated)} prose_tells={tells}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

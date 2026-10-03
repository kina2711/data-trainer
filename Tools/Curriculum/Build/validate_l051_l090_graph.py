#!/usr/bin/env python3
from __future__ import annotations

import re

from promote_l051_l090_common import PACK, load_lesson


def scalar(text: str, key: str) -> str:
    match = re.search(rf"(?m)^\s*{re.escape(key)}:\s*(.+)$", text)
    return match.group(1).strip() if match else ""


def main() -> int:
    lessons = [load_lesson(number) for number in range(51, 91)]
    ids = {lesson.note_id for lesson in lessons}
    ids.add("wiki.de-foundation.auto-vectorization-compiler-gives-up")
    failures: list[str] = []
    for index, lesson in enumerate(lessons):
        text = (PACK / lesson.filename).read_text()
        previous = "wiki.de-foundation.auto-vectorization-compiler-gives-up" if index == 0 else lessons[index - 1].note_id
        following = lessons[index + 1].note_id if index + 1 < len(lessons) else ""
        if scalar(text, "builds_on") != f"[{previous}]":
            failures.append(f"L{lesson.number}: builds_on mismatch")
        expected_next = f"[{following}]" if following else "[]"
        if scalar(text, "prerequisite_of") != expected_next:
            failures.append(f"L{lesson.number}: prerequisite_of mismatch")
        for target in re.findall(r"wiki\.de-foundation\.[a-z0-9-]+", scalar(text, "builds_on") + scalar(text, "prerequisite_of")):
            if target not in ids:
                failures.append(f"L{lesson.number}: dangling {target}")
    if failures:
        print("FAIL\n" + "\n".join(f"- {item}" for item in failures)); return 1
    print("PASS lessons=40 edges=79 dangling=0 cycles=0 terminal=L090")
    return 0


if __name__ == "__main__": raise SystemExit(main())

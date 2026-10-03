#!/usr/bin/env python3
"""Mechanical gate for the editorial/humanizer pass on L251-L270."""
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACK = ROOT / "Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01"


def main() -> int:
    failures: list[str] = []
    checked = 0
    corpus_paragraphs: dict[str, list[str]] = {}
    for path in sorted(PACK.glob("*.md")):
        match = re.match(r"(\d+)-", path.name)
        if not match or not 139 <= int(match.group(1)) <= 158:
            continue
        checked += 1
        text = path.read_text()
        if "editorial_pass: humanized-v3" not in text:
            failures.append(f"{path.name}: chưa qua humanized-v3")
        paragraphs = [re.sub(r"\s+", " ", item).strip() for item in re.split(r"\n\s*\n", text)]
        long_paragraphs = [item for item in paragraphs if len(item.split()) >= 25 and not item.startswith("|")]
        repeats = [item for item, count in Counter(long_paragraphs).items() if count > 1]
        if repeats:
            failures.append(f"{path.name}: lặp nguyên {len(repeats)} đoạn dài trong cùng note")
        for item in long_paragraphs:
            corpus_paragraphs.setdefault(item, []).append(path.name)
        for phrase in ("Trong thế giới dữ liệu ngày nay", "Bài viết này sẽ", "Điều quan trọng cần lưu ý là", "Hãy cùng khám phá"):
            if phrase.lower() in text.lower():
                failures.append(f"{path.name}: prose tell `{phrase}`")
    cross_note = {item: paths for item, paths in corpus_paragraphs.items() if len(set(paths)) > 1}
    if cross_note:
        failures.append(f"toàn corpus: {len(cross_note)} đoạn dài trùng giữa nhiều note")
    if failures:
        print("FAIL")
        print("\n".join(f"- {item}" for item in failures))
        return 1
    print(f"PASS checked={checked} editorial=humanized-v3 within_note_repeats=0 cross_note_repeats=0 prose_tells=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Validate note/source lineage and the mandatory deep-coverage contract."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
BRAIN_ROOT = REPO_ROOT / "Docs/Second-Brain"
MANIFEST_PATH = BRAIN_ROOT / "second-brain-manifest.json"


def section(text: str, heading: str) -> str:
    match = re.search(rf"(?m)^## {re.escape(heading)}\s*$", text)
    if not match:
        return ""
    start = match.end()
    end_match = re.search(r"(?m)^## ", text[start:])
    end = start + end_match.start() if end_match else len(text)
    return text[start:end]


def frontmatter_value(text: str, key: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    block = text.split("---\n", 2)[1]
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+)$", block)
    return match.group(1).strip().strip('"') if match else None


def main() -> int:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    source_by_id = {row["source_id"]: row for row in manifest["source_registry"]}
    failures: list[str] = []

    for row in manifest["note_registry"]:
        path = BRAIN_ROOT / row["path"]
        if not path.is_file():
            failures.append(f"missing note: {row['path']}")
            continue
        text = path.read_text(encoding="utf-8")
        note_id = frontmatter_value(text, "note_id")
        if note_id != row["note_id"]:
            failures.append(f"note_id mismatch: {row['path']}")

        coverage = section(text, "Source coverage")
        key_takeaways = section(text, "Key takeaways")
        references = section(text, "Reference")
        if not coverage:
            failures.append(f"missing Source coverage: {row['path']}")
        if "| Source slice |" not in coverage or "| Trạng thái |" not in coverage:
            failures.append(f"invalid coverage matrix: {row['path']}")
        if "Đã" not in coverage:
            failures.append(f"coverage has no explicit state: {row['path']}")
        if not key_takeaways.strip():
            failures.append(f"empty Key takeaways: {row['path']}")
        if not references.strip():
            failures.append(f"empty Reference: {row['path']}")

        for source_id in row["source_ids"]:
            source = source_by_id.get(source_id)
            if source is None:
                failures.append(f"unknown source_id {source_id}: {row['path']}")
                continue
            record_stem = Path(source["record_path"]).stem
            wikilink = f"[[{record_stem}]]"
            if wikilink not in coverage:
                failures.append(f"source missing from coverage {source_id}: {row['path']}")
            if wikilink not in references:
                failures.append(f"source missing from Reference {source_id}: {row['path']}")

        words = len(re.findall(r"\b\w+[\w-]*\b", text, re.UNICODE))
        if words < 1800:
            failures.append(f"note below deep-review floor ({words} words): {row['path']}")
        if len(re.findall(r"(?m)^## ", text)) < 12:
            failures.append(f"note lacks developed section structure: {row['path']}")
        if not frontmatter_value(text, "primary_question"):
            failures.append(f"missing primary_question: {row['path']}")
        if not re.search(r"(?mi)^## .*?(giới hạn|chưa cho phép)", text):
            failures.append(f"missing limitations section: {row['path']}")
        if not re.search(r"(?mi)^## .*?(câu hỏi|tự kiểm tra|ôn tập)", text):
            failures.append(f"missing self-check section: {row['path']}")

    print(f"checked={len(manifest['note_registry'])} failed={len(failures)}")
    for failure in failures:
        print(f"FAIL {failure}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

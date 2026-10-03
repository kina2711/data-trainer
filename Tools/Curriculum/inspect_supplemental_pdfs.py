#!/usr/bin/env python3
"""Inspect PDF structure without modifying source files."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


def run(command: list[str], timeout: int = 45) -> tuple[int, str, str]:
    try:
        result = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            errors="replace",
            timeout=timeout,
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired as exc:
        return 124, exc.stdout or "", "timeout"


def parse_pdfinfo(output: str) -> dict[str, str]:
    parsed: dict[str, str] = {}
    for line in output.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        parsed[key.strip().lower().replace(" ", "_")] = value.strip()
    return parsed


def text_sample(path: str, page: int) -> dict[str, object]:
    code, stdout, stderr = run(
        ["pdftotext", "-f", str(page), "-l", str(page), path, "-"]
    )
    normalized = re.sub(r"\s+", " ", stdout).strip()
    return {
        "page": page,
        "exit_code": code,
        "non_whitespace_characters": len(re.sub(r"\s+", "", stdout)),
        "text_preview": normalized[:240],
        "error": stderr.strip()[:500] or None,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    inventory = json.loads(args.inventory.read_text(encoding="utf-8"))
    pdfs = [item for item in inventory["files"] if item["extension"] == ".pdf"]
    records: list[dict[str, object]] = []
    status_counts: Counter[str] = Counter()

    for item in pdfs:
        path = str(item["path"])
        code, stdout, stderr = run(["pdfinfo", path])
        if code != 0:
            status = "pdfinfo-failed"
            status_counts[status] += 1
            records.append(
                {
                    "path": path,
                    "sha256": item["sha256"],
                    "status": status,
                    "error": stderr.strip()[:1000],
                }
            )
            continue

        metadata = parse_pdfinfo(stdout)
        try:
            pages = int(metadata.get("pages", "0"))
        except ValueError:
            pages = 0
        sample_pages = sorted({page for page in (1, max(1, (pages + 1) // 2), pages) if page})
        samples = [text_sample(path, page) for page in sample_pages]
        character_counts = [int(sample["non_whitespace_characters"]) for sample in samples]
        if samples and all(count == 0 for count in character_counts):
            text_status = "no-text-in-sampled-pages"
        elif any(sample["exit_code"] != 0 for sample in samples):
            text_status = "sample-extraction-error"
        elif samples and min(character_counts) == 0:
            text_status = "partial-text-in-sampled-pages"
        else:
            text_status = "text-present-in-sampled-pages"
        status_counts[text_status] += 1
        records.append(
            {
                "path": path,
                "sha256": item["sha256"],
                "status": "parseable",
                "pages": pages,
                "title": metadata.get("title") or None,
                "author": metadata.get("author") or None,
                "subject": metadata.get("subject") or None,
                "keywords": metadata.get("keywords") or None,
                "creator": metadata.get("creator") or None,
                "producer": metadata.get("producer") or None,
                "creation_date": metadata.get("creationdate") or None,
                "modification_date": metadata.get("moddate") or None,
                "encrypted": metadata.get("encrypted") or None,
                "tagged": metadata.get("tagged") or None,
                "pdf_version": metadata.get("pdf_version") or None,
                "page_size": metadata.get("page_size") or None,
                "text_layer_status": text_status,
                "samples": samples,
            }
        )

    output = {
        "schema_version": "1.0",
        "task_id": "book-inventory-supplemental-source-collection-2026-09-27",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "method": "pdfinfo plus pdftotext samples from beginning, middle and end",
        "summary": {
            "pdf_count": len(pdfs),
            "record_count": len(records),
            "status_counts": dict(sorted(status_counts.items())),
        },
        "records": records,
    }
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

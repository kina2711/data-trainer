#!/usr/bin/env python3
"""Inventory local reference libraries without reading source content."""

from __future__ import annotations

import hashlib
import json
import mimetypes
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "Tools" / "Curriculum" / "Manifests" / "Academic" / "reference-inventory.json"
PROVENANCE_REVIEW = re.compile(r"(?:libgen|z-lib|zlib|oceanofpdf)", re.IGNORECASE)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    records: list[dict[str, object]] = []
    for code in ("DA", "DE"):
        library = ROOT / "Material" / code / "Reference" / "Library"
        for path in sorted(item for item in library.rglob("*") if item.is_file()):
            relative = path.relative_to(ROOT).as_posix()
            records.append(
                {
                    "programme_library": code,
                    "path": relative,
                    "filename": path.name,
                    "extension": path.suffix.lower(),
                    "media_type": mimetypes.guess_type(path.name)[0] or "application/octet-stream",
                    "bytes": path.stat().st_size,
                    "sha256": sha256(path),
                    "provenance_status": (
                        "review-required" if PROVENANCE_REVIEW.search(relative) else "unreviewed"
                    ),
                }
            )

    hash_counts = Counter(record["sha256"] for record in records)
    for record in records:
        record["duplicate_count"] = hash_counts[record["sha256"]]

    payload = {
        "schema_version": 1,
        "inspection_level": "path-size-hash-only",
        "content_read": False,
        "rights_cleared": False,
        "counts": {
            "files": len(records),
            "pdf": sum(record["extension"] == ".pdf" for record in records),
            "duplicate_files": sum(record["duplicate_count"] > 1 for record in records),
            "provenance_review_required": sum(
                record["provenance_status"] == "review-required" for record in records
            ),
            "by_programme_library": dict(Counter(record["programme_library"] for record in records)),
        },
        "records": records,
    }
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload["counts"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

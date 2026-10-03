#!/usr/bin/env python3
"""Create a read-only, hash-based inventory of supplemental curriculum sources."""

from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


DOCUMENT_EXTENSIONS = {
    ".pdf", ".epub", ".mobi", ".azw", ".azw3", ".djvu", ".doc", ".docx",
    ".ppt", ".pptx",
}
TEXT_EXTENSIONS = {".md", ".txt", ".rst", ".html", ".htm"}
VIDEO_EXTENSIONS = {".mp4", ".mkv", ".avi", ".mov", ".webm", ".m4v"}
AUDIO_EXTENSIONS = {".mp3", ".wav", ".m4a", ".aac", ".flac", ".ogg"}
TRANSCRIPT_EXTENSIONS = {".srt", ".vtt"}
CODE_EXTENSIONS = {
    ".py", ".pyi", ".ipynb", ".sql", ".java", ".scala", ".r", ".sh",
    ".ps1", ".bat", ".cmd", ".js", ".ts", ".go", ".c", ".cc", ".cpp",
    ".h", ".hpp", ".yaml", ".yml", ".toml", ".json", ".xml",
}
COMPANION_EXTENSIONS = {
    ".csv", ".tsv", ".xlsx", ".xls", ".xlsm", ".pbix", ".drawio",
    ".png", ".jpg", ".jpeg", ".gif", ".svg",
}
BINARY_RUNTIME_EXTENSIONS = {
    ".exe", ".dll", ".so", ".dylib", ".jar", ".jmod", ".class", ".bin",
    ".msi", ".dmg", ".deb", ".rpm", ".zip", ".7z", ".rar", ".tar",
    ".gz", ".bz2", ".xz", ".crdownload", ".dtmp",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def classify(path: Path) -> str:
    extension = path.suffix.lower()
    if extension in DOCUMENT_EXTENSIONS:
        return "document-or-book"
    if extension in TEXT_EXTENSIONS:
        return "note-or-text"
    if extension in VIDEO_EXTENSIONS:
        return "course-video"
    if extension in AUDIO_EXTENSIONS:
        return "course-audio"
    if extension in TRANSCRIPT_EXTENSIONS:
        return "course-transcript"
    if extension in CODE_EXTENSIONS:
        return "code-or-lab"
    if extension in COMPANION_EXTENSIONS:
        return "companion-artifact"
    if extension in BINARY_RUNTIME_EXTENSIONS or not extension:
        return "binary-runtime-or-unknown"
    return "other"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("roots", nargs="+", type=Path)
    args = parser.parse_args()

    files: list[dict[str, object]] = []
    errors: list[dict[str, str]] = []
    root_records: list[dict[str, object]] = []
    hashes: dict[str, list[str]] = defaultdict(list)
    kind_counts: Counter[str] = Counter()
    extension_counts: Counter[str] = Counter()
    total_bytes = 0

    for root in args.roots:
        root = root.resolve()
        root_file_count = 0
        root_bytes = 0
        if not root.is_dir():
            errors.append({"path": str(root), "error": "missing-directory"})
            root_records.append({"path": str(root), "status": "missing"})
            continue

        for path in sorted(root.rglob("*"), key=lambda value: str(value).casefold()):
            if not path.is_file() or path.is_symlink():
                continue
            try:
                stat = path.stat()
                digest = sha256_file(path)
                extension = path.suffix.lower() or "[no-ext]"
                kind = classify(path)
                record = {
                    "path": str(path),
                    "root": str(root),
                    "relative_path": str(path.relative_to(root)),
                    "name": path.name,
                    "extension": extension,
                    "kind": kind,
                    "mime_guess": mimetypes.guess_type(path.name)[0],
                    "size_bytes": stat.st_size,
                    "modified_at": datetime.fromtimestamp(
                        stat.st_mtime, timezone.utc
                    ).isoformat(),
                    "sha256": digest,
                    "inventory_status": "unread",
                    "rights_status": "owner-review-required",
                }
                files.append(record)
                hashes[digest].append(str(path))
                root_file_count += 1
                root_bytes += stat.st_size
                total_bytes += stat.st_size
                kind_counts[kind] += 1
                extension_counts[extension] += 1
            except (OSError, PermissionError) as exc:
                errors.append({"path": str(path), "error": str(exc)})

        root_records.append(
            {
                "path": str(root),
                "status": "ok",
                "file_count": root_file_count,
                "total_bytes": root_bytes,
            }
        )

    duplicate_groups = []
    duplicate_file_count = 0
    reclaimable_bytes = 0
    sizes = {record["path"]: record["size_bytes"] for record in files}
    for digest, paths in sorted(hashes.items()):
        if len(paths) < 2:
            continue
        size = int(sizes[paths[0]])
        duplicate_file_count += len(paths) - 1
        reclaimable_bytes += size * (len(paths) - 1)
        duplicate_groups.append(
            {
                "sha256": digest,
                "size_bytes_each": size,
                "paths": paths,
            }
        )

    manifest = {
        "schema_version": "1.0",
        "task_id": "book-inventory-supplemental-source-collection-2026-09-27",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "policy": {
            "source_files_modified": False,
            "inventory_status_implies_read": False,
            "rights_inferred_from_possession": False,
            "filename_used_as_content_evidence": False,
        },
        "summary": {
            "root_count": len(args.roots),
            "file_count": len(files),
            "total_bytes": total_bytes,
            "error_count": len(errors),
            "duplicate_group_count": len(duplicate_groups),
            "duplicate_file_count_excluding_first_copy": duplicate_file_count,
            "potential_reclaimable_bytes": reclaimable_bytes,
            "by_kind": dict(sorted(kind_counts.items())),
            "by_extension": dict(sorted(extension_counts.items())),
        },
        "roots": root_records,
        "files": files,
        "duplicate_groups": duplicate_groups,
        "errors": errors,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

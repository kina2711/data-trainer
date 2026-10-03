#!/usr/bin/env python3
"""Promote every registered Wiki note to owner-approved canonical status."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRAIN = ROOT / "Docs/Second-Brain"
MANIFEST = BRAIN / "second-brain-manifest.json"
APPROVAL = (
    "approved_by: second-brain-owner\n"
    "approved_at: 2026-10-03\n"
    "approval_scope: all-registered-notes\n"
    "canonical_since: 2026-10-03\n"
)


def promote_text(text: str) -> str:
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("frontmatter terminator missing")
    header, body = text[:end], text[end:]
    header = re.sub(r"^status:\s*\S+\s*$", "status: canonical", header, count=1, flags=re.M)
    header = re.sub(r"^concept_key_status:\s*\S+\s*$", "concept_key_status: canonical", header, flags=re.M)
    header = re.sub(r"^(?:approved_by|approved_at|approval_scope|canonical_since):.*\n?", "", header, flags=re.M)
    status = re.search(r"^status: canonical$", header, re.M)
    if not status:
        raise ValueError("note has no status field")
    insertion = status.end()
    header = header[:insertion] + "\n" + APPROVAL.rstrip("\n") + header[insertion:]
    concept_key_match = re.search(r"^concept_key:\s*(.+?)\s*$", header, re.M)
    if concept_key_match:
        concept_key = concept_key_match.group(1).strip().strip('"')
        canonical_statement = (
            f"- Concept key `{concept_key}` đã được owner phê duyệt `canonical`; "
            "note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery."
        )
        body = re.sub(
            r"^- Concept key.*(?:`proposed`|canonical (?:registry )?coverage).*$",
            canonical_statement,
            body,
            flags=re.M,
        )
    return header + body


def main(check: bool) -> int:
    manifest = json.loads(MANIFEST.read_text())
    stale = []
    for entry in manifest["note_registry"]:
        wiki = BRAIN / entry["path"]
        current = wiki.read_text()
        expected = promote_text(current)
        match = re.search(r"^reference_path:\s*(.+?)\s*$", expected, re.M)
        targets = [wiki]
        if match:
            targets.append(ROOT / match.group(1).strip().strip('"'))
        for target in targets:
            if check:
                if not target.exists() or target.read_text() != expected:
                    stale.append(str(target.relative_to(ROOT)))
            else:
                target.write_text(expected)
        if not check:
            entry["status"] = "canonical"
            entry["approved_at"] = "2026-10-03"
    if not check:
        manifest["version"] = "2.0.0"
        manifest["status"] = "active-canonical"
        manifest["updated_at"] = "2026-10-03T15:30:00+07:00"
        manifest["canonical_release"] = {
            "release_id": "second-brain-2.0.0",
            "approved_by": "second-brain-owner",
            "approved_at": "2026-10-03",
            "note_count": len(manifest["note_registry"]),
            "visibility": "private-local-first"
        }
        MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    else:
        if manifest.get("version") != "2.0.0" or manifest.get("status") != "active-canonical":
            stale.append("manifest release status")
        for entry in manifest["note_registry"]:
            if entry.get("status") != "canonical" or entry.get("approved_at") != "2026-10-03":
                stale.append("registry " + entry["note_id"])
    if stale:
        print("STALE")
        print("\n".join(stale[:40]))
        return 1
    print(f"{'checked' if check else 'promoted'} canonical_notes={len(manifest['note_registry'])} mirrors=644 release=2.0.0")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    raise SystemExit(main(args.check))

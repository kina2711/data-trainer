#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRAIN = ROOT / "Docs/Second-Brain"
MANIFEST = BRAIN / "second-brain-manifest.json"


def main() -> int:
    manifest = json.loads(MANIFEST.read_text())
    failures = []
    canonical = 0
    parity = 0
    for entry in manifest["note_registry"]:
        path = BRAIN / entry["path"]
        text = path.read_text()
        checks = (
            "status: canonical",
            "approved_by: second-brain-owner",
            "approved_at: 2026-10-03",
            "approval_scope: all-registered-notes",
            "canonical_since: 2026-10-03",
        )
        if not all(value in text[: text.find("\n---\n", 4)] for value in checks):
            failures.append(entry["note_id"] + ": canonical approval metadata")
        else:
            canonical += 1
        if entry.get("status") != "canonical":
            failures.append(entry["note_id"] + ": registry not canonical")
        match = re.search(r"^reference_path:\s*(.+?)\s*$", text, re.M)
        if match:
            reference = ROOT / match.group(1).strip().strip('"')
            if not reference.exists() or reference.read_bytes() != path.read_bytes():
                failures.append(entry["note_id"] + ": parity")
            else:
                parity += 1
    release = manifest.get("canonical_release") or {}
    if manifest.get("version") != "2.0.0" or manifest.get("status") != "active-canonical":
        failures.append("manifest canonical release state")
    if release.get("note_count") != len(manifest["note_registry"]) or release.get("visibility") != "private-local-first":
        failures.append("manifest canonical release contract")
    if failures:
        print("FAIL")
        print("\n".join("- " + item for item in failures[:80]))
        return 1
    print(f"PASS canonical={canonical} registry={len(manifest['note_registry'])} parity={parity} release={manifest['version']} visibility={release['visibility']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

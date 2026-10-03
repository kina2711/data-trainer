#!/usr/bin/env python3
"""Validate completeness, traceability and basic measurability of objective registry."""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
REGISTRY = ROOT / "Tools" / "Curriculum" / "Manifests" / "Academic" / "objectives.json"
EXPECTED = {"programme": 2, "phase": 14, "module": 40, "lesson": 525}
UNOBSERVABLE = re.compile(r"^(hiểu|biết|nắm được|làm quen)(?:\s|$)", re.IGNORECASE)
LESSON_REQUIRED = (
    "objective",
    "evidence",
    "threshold",
    "prerequisites",
    "bloom_level",
    "assessment",
)


def main() -> int:
    payload = json.loads(REGISTRY.read_text(encoding="utf-8"))
    records = payload.get("records", [])
    failures: list[str] = []
    counts = Counter(record.get("kind") for record in records)
    if dict(counts) != EXPECTED:
        failures.append(f"counts: expected {EXPECTED}, got {dict(counts)}")

    ids = [record.get("id") for record in records]
    duplicates = sorted(identifier for identifier, count in Counter(ids).items() if count > 1)
    if duplicates:
        failures.append(f"duplicate IDs: {duplicates}")
    known = set(ids)

    for record in records:
        identifier = record["id"]
        parent = record.get("parent_id")
        if record["kind"] != "programme" and parent not in known:
            failures.append(f"{identifier}: missing parent {parent}")
        source = record.get("source", {})
        source_path = ROOT / source.get("path", "")
        if not source_path.is_file():
            failures.append(f"{identifier}: missing source {source_path}")
        else:
            actual = hashlib.sha256(source_path.read_bytes()).hexdigest()
            if actual != source.get("sha256"):
                failures.append(f"{identifier}: stale source hash")

        objective = str(record.get("objective", "")).strip()
        if not objective:
            failures.append(f"{identifier}: empty objective")
        if UNOBSERVABLE.search(objective):
            failures.append(f"{identifier}: unobservable leading verb: {objective}")

        if record["kind"] == "lesson":
            for field in LESSON_REQUIRED:
                if not str(record.get(field, "")).strip():
                    failures.append(f"{identifier}: missing {field}")
            if record.get("lesson_type") not in {"LT", "TH", "DA", "KT"}:
                failures.append(f"{identifier}: invalid lesson_type {record.get('lesson_type')}")
            phase_id = record.get("phase_id")
            if phase_id not in known:
                failures.append(f"{identifier}: missing phase {phase_id}")

    for code, expected_lessons in (("DA", 85), ("DE", 440)):
        numbers = sorted(
            int(record["id"].rsplit("L", 1)[1])
            for record in records
            if record.get("kind") == "lesson" and record.get("programme") == code
        )
        if numbers != list(range(1, expected_lessons + 1)):
            failures.append(f"{code}: lesson sequence is not 1..{expected_lessons}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print(
        "PASS: objective registry — "
        + " · ".join(f"{kind}={counts[kind]}" for kind in ("programme", "phase", "module", "lesson"))
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Validate source-plan integrity and objective coverage without reading sources."""

import json
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[3]
ACADEMIC = ROOT / "Tools/Curriculum/Manifests/Academic"


def main():
    objectives = json.loads((ACADEMIC / "objectives.json").read_text(encoding="utf-8"))
    catalog = json.loads((ACADEMIC / "source-catalog.json").read_text(encoding="utf-8"))
    plan = json.loads((ACADEMIC / "source-plan.json").read_text(encoding="utf-8"))
    errors = []
    required = {"book": 3, "document": 3, "website": 3, "video": 3, "course": 1}
    if catalog.get("schema_version") != 2: errors.append("source catalog schema must be 2")
    if plan.get("schema_version") != 2: errors.append("source plan schema must be 2")
    sources = catalog["sources"]
    ids = [s["id"] for s in sources]
    if len(ids) != len(set(ids)): errors.append("source catalog contains duplicate ids")
    known = set(ids)
    by_id = {s["id"]: s for s in sources}
    for s in sources:
        parsed = urlparse(s["url"])
        if parsed.scheme != "https" or not parsed.netloc: errors.append(f"{s['id']}: invalid HTTPS URL")
        if s["reading_status"] != "candidate-unread": errors.append(f"{s['id']}: selection falsely claims reading")
        if s.get("local_path") and not (ROOT / s["local_path"]).is_file(): errors.append(f"{s['id']}: missing local file {s['local_path']}")
        if s["access"] == "local-rights-review" and "quyền" not in s.get("note", "").lower(): errors.append(f"{s['id']}: missing explicit rights note")
    objective_ids = {r["id"] for r in objectives["records"]}
    plan_ids = [r["objective_id"] for r in plan["records"]]
    if len(plan_ids) != len(set(plan_ids)): errors.append("source plan contains duplicate objective ids")
    if objective_ids != set(plan_ids): errors.append(f"coverage mismatch: missing={sorted(objective_ids-set(plan_ids))}; extra={sorted(set(plan_ids)-objective_ids)}")
    for r in plan["records"]:
        if not r["source_ids"]: errors.append(f"{r['objective_id']}: no source selected")
        if set(r["source_ids"]) - known: errors.append(f"{r['objective_id']}: unknown source ids")
        if r["locator_status"] != "pending-deep-reading": errors.append(f"{r['objective_id']}: premature locator claim")
        grouped = defaultdict(list)
        for sid in r["source_ids"]:
            if sid in by_id: grouped[by_id[sid]["category"]].append(sid)
        if dict(grouped) != r.get("source_ids_by_category"):
            errors.append(f"{r['objective_id']}: source_ids_by_category does not match source_ids")
        if r["kind"] in {"module", "lesson"}:
            counts = Counter(by_id[sid]["category"] for sid in r["source_ids"] if sid in by_id)
            for category, minimum in required.items():
                if counts[category] < minimum:
                    errors.append(f"{r['objective_id']}: {category}={counts[category]} < {minimum}")
            courses = [by_id[sid] for sid in grouped["course"]]
            for course in courses:
                if course.get("platform") != "Coursera":
                    errors.append(f"{r['objective_id']}: course {course['id']} is not Coursera")
                path = course.get("course_path") or ""
                if not any(token in path for token in ("Module", "Modules", "Week", "Weeks", "Course", "Courses")):
                    errors.append(f"{r['objective_id']}: course {course['id']} lacks a specific module/week path")
    if errors:
        for error in errors: print(f"ERROR: {error}")
        raise SystemExit(1)
    kind_counts = Counter(r["kind"] for r in plan["records"])
    print(
        "PASS: source plan v2 — "
        f"{len(sources)} unique catalog entries · {len(plan_ids)} objective records · "
        f"{kind_counts['module']} modules and {kind_counts['lesson']} lessons each satisfy "
        "3 books + 3 documents + 3 websites + 3 videos + 1 Coursera path · no source marked as read"
    )


if __name__ == "__main__": main()

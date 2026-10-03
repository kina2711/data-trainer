#!/usr/bin/env python3
"""Build the unified Roadmap, Second Brain and lesson portal index."""
from __future__ import annotations

import hashlib
import json
import re
import shutil
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
APP = ROOT / "Apps/SecondBrain"
WEB = APP / "web"
BRAIN = ROOT / "Docs/Second-Brain"
MANIFEST = BRAIN / "second-brain-manifest.json"
PROGRAM_NAMES = {"DA": "Data Analyst", "DE": "Data Engineer"}
LESSON_ASSETS = {
    "note": ("note.md", "Giáo trình"),
    "slides": ("slides.md", "Slide"),
    "quiz": ("quiz.md", "Quiz"),
    "homework": ("homework.md", "Bài tập"),
    "afterNote": ("after-note.md", "Sau buổi học"),
}


def frontmatter(text: str) -> tuple[dict, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise ValueError("frontmatter missing")
    return yaml.safe_load(match.group(1)), text[match.end():]


def strip_optional_frontmatter(text: str) -> str:
    match = re.match(r"^---\n.*?\n---\n", text, re.S)
    return text[match.end():] if match else text


def sanitize_publish_text(text: str) -> str:
    """Remove machine-specific paths while preserving the surrounding prose."""
    text = re.sub(r"`/(?:home|Users)/[^`]+`", "`[local path redacted]`", text)
    text = re.sub(r"`[A-Za-z]:\\\\Users\\\\[^`]+`", "`[local path redacted]`", text)
    return text


def title_from(body: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", body, re.M)
    return match.group(1).strip() if match else fallback


def domain_from(path: str) -> str:
    parts = Path(path).parts
    return parts[1] if len(parts) > 2 else "General"


def text_excerpt(body: str, limit: int = 240) -> str:
    clean = re.sub(r"```.*?```", " ", body, flags=re.S)
    clean = re.sub(r"<[^>]+>|[#>*_`|\[\]()]", " ", clean)
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean[:limit].rstrip() + ("…" if len(clean) > limit else "")


def number_from(value: str, prefix: str) -> int:
    match = re.match(rf"{re.escape(prefix)}_(\d+)", value)
    return int(match.group(1)) if match else 0


def label_from_slug(value: str) -> str:
    value = re.sub(r"^(?:Phase|Module|Lesson)_\d+-", "", value)
    return value.replace("-", " ").strip().capitalize()


def build_brain(manifest: dict) -> tuple[list[dict], list[dict]]:
    notes: list[dict] = []
    seen: set[str] = set()
    domains: Counter[str] = Counter()
    for entry in manifest["note_registry"]:
        path = BRAIN / entry["path"]
        fm, body = frontmatter(path.read_text())
        body = sanitize_publish_text(body)
        note_id = entry["note_id"]
        if note_id in seen:
            raise ValueError(f"duplicate note_id: {note_id}")
        if fm.get("status") != "canonical" or entry.get("status") != "canonical":
            raise ValueError(f"non-canonical note: {note_id}")
        seen.add(note_id)
        domain = domain_from(entry["path"])
        domains[domain] += 1
        relationships = fm.get("relationships") or {}
        tags = fm.get("tags") or []
        aliases = fm.get("aliases") or []
        notes.append({
            "id": note_id,
            "title": title_from(body, note_id),
            "domain": domain,
            "path": entry["path"],
            "question": str(fm.get("primary_question", "")),
            "noteType": str(fm.get("note_type", "")),
            "status": "canonical",
            "approvedAt": str(fm.get("approved_at", "")),
            "lastVerified": str(fm.get("last_verified", "")),
            "reviewAfter": str(fm.get("review_after", "")),
            "sourceIds": list(fm.get("source_ids") or []),
            "tags": list(tags if isinstance(tags, list) else [tags]),
            "aliases": list(aliases if isinstance(aliases, list) else [aliases]),
            "relationships": {
                "buildsOn": list(relationships.get("builds_on") or []),
                "prerequisiteOf": list(relationships.get("prerequisite_of") or []),
                "relatedTo": list(relationships.get("related_to") or []),
            },
            "excerpt": text_excerpt(body),
            "body": body.rstrip() + "\n",
            "wordCount": len(re.findall(r"\b\w+[\w-]*\b", body, re.U)),
        })
    notes.sort(key=lambda item: (item["domain"].lower(), item["title"].lower()))
    return notes, [{"name": name, "count": count} for name, count in sorted(domains.items())]


def build_roadmaps() -> list[dict]:
    roadmaps: list[dict] = []
    for program in PROGRAM_NAMES:
        base = ROOT / "Material" / program / "Roadmap"
        for path in sorted(base.glob("**/roadmap.md")):
            relative = path.relative_to(ROOT).as_posix()
            parts = path.relative_to(base).parts
            body = sanitize_publish_text(path.read_text()).rstrip() + "\n"
            if len(parts) == 1:
                level = "program"
                phase_number = module_number = 0
                item_id = f"roadmap.{program}.program"
                parent_id = None
            elif len(parts) == 2:
                level = "phase"
                phase_number = number_from(parts[0], "Phase")
                module_number = 0
                item_id = f"roadmap.{program}.P{phase_number:02d}"
                parent_id = f"roadmap.{program}.program"
            elif len(parts) == 3:
                level = "module"
                phase_number = number_from(parts[0], "Phase")
                module_number = number_from(parts[1], "Module")
                item_id = f"roadmap.{program}.P{phase_number:02d}.M{module_number:02d}"
                parent_id = f"roadmap.{program}.P{phase_number:02d}"
            else:
                raise ValueError(f"unexpected roadmap depth: {relative}")
            roadmaps.append({
                "id": item_id,
                "program": program,
                "programName": PROGRAM_NAMES[program],
                "level": level,
                "phaseNumber": phase_number,
                "moduleNumber": module_number,
                "parentId": parent_id,
                "title": title_from(body, label_from_slug(path.parent.name)),
                "path": relative,
                "excerpt": text_excerpt(body),
                "body": body,
                "wordCount": len(re.findall(r"\b\w+[\w-]*\b", body, re.U)),
            })
    roadmaps.sort(key=lambda item: (item["program"], item["phaseNumber"], item["moduleNumber"], item["level"]))
    ids = {item["id"] for item in roadmaps}
    if len(ids) != len(roadmaps):
        raise ValueError("duplicate roadmap id")
    for item in roadmaps:
        item["childIds"] = [child["id"] for child in roadmaps if child["parentId"] == item["id"]]
    return roadmaps


def build_lessons() -> list[dict]:
    lessons: list[dict] = []
    for program in PROGRAM_NAMES:
        base = ROOT / "Material" / program / "Curriculum"
        for manifest_path in sorted(base.glob("**/lesson.yaml")):
            data = yaml.safe_load(manifest_path.read_text()) or {}
            if data.get("status") != "ready-for-owner-review":
                continue
            directory = manifest_path.parent
            parts = directory.relative_to(base).parts
            if len(parts) != 3:
                raise ValueError(f"unexpected lesson depth: {directory}")
            phase_dir, module_dir, lesson_dir = parts
            phase_number = number_from(phase_dir, "Phase")
            module_number = number_from(module_dir, "Module")
            lesson_number = number_from(lesson_dir, "Lesson")
            lesson_id = str(data.get("lesson_id") or f"{program}-L{lesson_number:03d}")
            assets: list[dict] = []
            for key, (filename, label) in LESSON_ASSETS.items():
                source = directory / filename
                if not source.is_file():
                    raise ValueError(f"{lesson_id}: missing {filename}")
                assets.append({
                    "key": key,
                    "label": label,
                    "filename": filename,
                    "body": sanitize_publish_text(strip_optional_frontmatter(source.read_text())).rstrip() + "\n",
                })
            lessons.append({
                "id": lesson_id,
                "program": program,
                "programName": PROGRAM_NAMES[program],
                "lessonNumber": lesson_number,
                "phaseNumber": phase_number,
                "moduleNumber": module_number,
                "phaseLabel": label_from_slug(phase_dir),
                "moduleLabel": label_from_slug(module_dir),
                "title": str(data.get("title") or label_from_slug(lesson_dir)),
                "status": str(data["status"]),
                "targetLevel": str(data.get("target_level", "")),
                "durationMinutes": int(data.get("duration_minutes_estimate") or 0),
                "centralQuestion": str(data.get("central_question", "")),
                "objective": str(data.get("objective", "")),
                "sceneCount": len(data.get("scenes") or []),
                "path": directory.relative_to(ROOT).as_posix(),
                "assets": assets,
            })
    lessons.sort(key=lambda item: (item["program"], item["lessonNumber"]))
    ids = [item["id"] for item in lessons]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate lesson id")
    return lessons


def copy_vendor() -> None:
    vendor = WEB / "vendor"
    vendor.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "node_modules/marked/lib/marked.esm.js", vendor / "marked.esm.js")
    shutil.copy2(ROOT / "node_modules/dompurify/dist/purify.es.mjs", vendor / "purify.es.mjs")
    mermaid_source = ROOT / "node_modules/mermaid/dist"
    mermaid_target = vendor / "mermaid"
    mermaid_target.mkdir(parents=True, exist_ok=True)
    shutil.copy2(mermaid_source / "mermaid.esm.min.mjs", mermaid_target / "mermaid.esm.min.mjs")
    chunk_target = mermaid_target / "chunks/mermaid.esm.min"
    chunk_target.mkdir(parents=True, exist_ok=True)
    for source in (mermaid_source / "chunks/mermaid.esm.min").glob("*.mjs"):
        shutil.copy2(source, chunk_target / source.name)


def main() -> int:
    manifest = json.loads(MANIFEST.read_text())
    release = manifest.get("canonical_release") or {}
    if manifest.get("status") != "active-canonical" or release.get("visibility") != "private-local-first":
        raise SystemExit("Refusing to index a non-canonical or non-private manifest")
    notes, domains = build_brain(manifest)
    roadmaps = build_roadmaps()
    lessons = build_lessons()
    payload = {
        "schemaVersion": 2,
        "portalVersion": "1.0.0",
        "brainVersion": manifest["version"],
        "release": release,
        "stats": {
            "notes": len(notes),
            "sources": len(manifest["source_registry"]),
            "retrievalCases": len(manifest["retrieval_test_set"]),
            "domains": len(domains),
            "roadmaps": len(roadmaps),
            "lessons": len(lessons),
            "programs": len(PROGRAM_NAMES),
        },
        "programs": [{"id": key, "name": value} for key, value in PROGRAM_NAMES.items()],
        "domains": domains,
        "roadmaps": roadmaps,
        "lessons": lessons,
        "notes": notes,
    }
    encoded = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode()
    payload["contentHash"] = hashlib.sha256(encoded).hexdigest()
    target = WEB / "data/brain-index.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n")
    copy_vendor()
    print(
        f"built roadmaps={len(roadmaps)} notes={len(notes)} lessons={len(lessons)} "
        f"bytes={target.stat().st_size} hash={payload['contentHash']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

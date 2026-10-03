#!/usr/bin/env python3
"""Validate the runnable DA/DE first-five lecture packages."""
from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
TARGETS = [
    ROOT / "Material/DA/Curriculum/Phase_01-foundations-and-role/Module_01-introduction-to-the-data-analyst-role",
    ROOT / "Material/DE/Curriculum/Phase_01-engineering-foundation/Module_01-engineering-thinking-git-and-debugging",
]
REQUIRED = {"note.md", "lesson.yaml", "slides.md", "quiz.md", "homework.md", "after-note.md"}
TYPES = {"explain", "check", "practice", "decide", "apply"}
PLACEHOLDERS = re.compile(r"Chưa soạn|chua-soan|Sẽ chuyển|TODO|TBD|<tên phần>|Nội dung câu hỏi", re.I)


def note_has_heading(text: str, heading: str) -> bool:
    return bool(re.search(rf"(?m)^#+\s+{re.escape(heading)}\s*$", text))


def main() -> int:
    failures: list[str] = []
    metrics = {"lessons": 0, "scenes": 0, "slides": 0, "quiz_questions": 0, "homework_rubrics": 0}
    for base in TARGETS:
        role = "DA" if "/DA/" in base.as_posix() else "DE"
        for number in range(1, 6):
            matches = sorted(base.glob(f"Lesson_{number:03d}-*"))
            if len(matches) != 1:
                failures.append(f"{role}-L{number:03d}: expected one directory, found {len(matches)}")
                continue
            directory = matches[0]
            missing = REQUIRED - {path.name for path in directory.iterdir() if path.is_file()}
            if missing:
                failures.append(f"{role}-L{number:03d}: missing {sorted(missing)}")
                continue
            metrics["lessons"] += 1
            texts = {name: (directory / name).read_text() for name in REQUIRED}
            for name, text in texts.items():
                if PLACEHOLDERS.search(text):
                    failures.append(f"{role}-L{number:03d}/{name}: placeholder remains")

            try:
                blueprint = yaml.safe_load(texts["lesson.yaml"])
            except Exception as error:
                failures.append(f"{role}-L{number:03d}: invalid lesson.yaml: {error}")
                continue
            if blueprint.get("lesson_id") != f"{role}-L{number:03d}":
                failures.append(f"{role}-L{number:03d}: lesson_id mismatch")
            if blueprint.get("status") != "ready-for-owner-review":
                failures.append(f"{role}-L{number:03d}: invalid status")
            scenes = blueprint.get("scenes") or []
            metrics["scenes"] += len(scenes)
            if len(scenes) != 9 or {scene.get("type") for scene in scenes} != TYPES:
                failures.append(f"{role}-L{number:03d}: scene vocabulary/coverage")
            if sum(scene.get("minutes", 0) for scene in scenes) != 120:
                failures.append(f"{role}-L{number:03d}: scene minutes do not sum to 120")
            ids = {scene.get("id") for scene in scenes}
            for scene in scenes:
                span = scene.get("source_span", "")
                if span.startswith("UNSOURCED"):
                    if scene.get("type") not in {"practice", "decide", "apply"}:
                        failures.append(f"{role}-L{number:03d}/{scene.get('id')}: unexpected unsourced scene")
                else:
                    match = re.search(r"heading '(.+)'$", span)
                    if not match or not note_has_heading(texts["note.md"], match.group(1)):
                        failures.append(f"{role}-L{number:03d}/{scene.get('id')}: source heading not found: {span}")
                if scene.get("type") == "apply":
                    for dependency in scene.get("assumes", []):
                        if dependency not in ids:
                            failures.append(f"{role}-L{number:03d}: dangling scene dependency {dependency}")

            slide_count = len(re.findall(r"(?m)^---\s*$", texts["slides.md"])) - 1
            metrics["slides"] += slide_count
            if slide_count < 15 or "marp: true" not in texts["slides.md"] or "## Luồng kiểm soát" not in texts["slides.md"]:
                failures.append(f"{role}-L{number:03d}: incomplete slide deck ({slide_count} slides)")
            if any(token in texts["slides.md"] for token in (" — ", ";", " → ")):
                failures.append(f"{role}-L{number:03d}: slide copy contains disallowed AI-style punctuation")
            if "UNSOURCED curriculum transfer scenario" not in texts["slides.md"]:
                failures.append(f"{role}-L{number:03d}: transfer provenance missing")

            question_count = len(re.findall(r"(?m)^### Câu \d+$", texts["quiz.md"]))
            answer_count = texts["quiz.md"].count("<details><summary>Đáp án và phản hồi</summary>")
            metrics["quiz_questions"] += question_count
            if question_count != 10 or answer_count != 10 or "nguong_dat: 8" not in texts["quiz.md"]:
                failures.append(f"{role}-L{number:03d}: quiz coverage {question_count}/{answer_count}")

            rubric_points = [int(value) for value in re.findall(r"\| [^|]+ \| (\d+) \|", texts["homework.md"])]
            metrics["homework_rubrics"] += 1
            if sum(rubric_points) != 100:
                failures.append(f"{role}-L{number:03d}: rubric total {sum(rubric_points)}")
            for required in ("Critical-failure rules", "Remediation và retest", "Changed constraint"):
                if required not in texts["homework.md"]:
                    failures.append(f"{role}-L{number:03d}: homework missing {required}")
            for required in ("Feedback protocol", "Novel-scenario retest", "Remediation map", "Giới hạn"):
                if required not in texts["after-note.md"]:
                    failures.append(f"{role}-L{number:03d}: after-note missing {required}")

    if metrics != {"lessons": 10, "scenes": 90, "slides": 170, "quiz_questions": 100, "homework_rubrics": 10}:
        failures.append("aggregate metrics mismatch: " + json.dumps(metrics, ensure_ascii=False, sort_keys=True))
    print("metrics", json.dumps(metrics, ensure_ascii=False, sort_keys=True))
    if failures:
        print(f"FAIL count={len(failures)}")
        print("\n".join(f"- {failure}" for failure in failures[:100]))
        return 1
    print("PASS lessons=10 scenes=90 slides=170 quiz_questions=100 homework_rubrics=10 placeholders=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

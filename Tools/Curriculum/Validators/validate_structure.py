#!/usr/bin/env python3
"""Validate the post-migration curriculum repository structure."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
MATERIAL = ROOT / "Material"
EXPECTED = {
    "DA": {"phases": 4, "modules": 11, "lessons": 85},
    "DE": {"phases": 10, "modules": 29, "lessons": 440},
}

PROGRAMME_HEADINGS = (
    "## Năng lực đích",
    "## Phạm vi",
    "## Điều kiện đầu vào",
    "## Đầu ra chương trình",
    "## Bản đồ giáo trình",
    "## Mô hình phụ thuộc",
    "## Hệ thống đánh giá",
    "## Độ phủ và khả năng truy vết",
    "## Rủi ro của chương trình",
    "## Quyết định",
    "## Tài liệu tham khảo",
)
PHASE_HEADINGS = (
    "## Điều kiện đầu vào",
    "## Đầu ra giai đoạn",
    "## Thứ tự mô-đun",
    "## Lý do sắp xếp",
    "## Bài kiểm tra cuối giai đoạn",
    "## Điểm tích hợp",
    "## Khắc phục",
    "## Rủi ro của giai đoạn",
    "## Tài liệu tham khảo",
)
MODULE_HEADINGS = (
    "## Điều kiện đầu vào",
    "## Đầu ra mô-đun",
    "## Tiêu chí hoàn thành",
    "## Khái niệm và nguyên tắc bất biến",
    "## Các bài trong mô-đun",
    "## Nội dung từng bài",
    "## Lý do sắp xếp",
    "## Ma trận đánh giá",
    "## Bài thực hành bắt buộc",
    "## Ngộ nhận và lỗi loại trực tiếp",
    "## Điểm nối với mô-đun khác",
    "## Tài liệu tham khảo",
)


def count_dirs(root: Path, pattern: str) -> int:
    return sum(1 for path in root.rglob(pattern) if path.is_dir())


def require_headings(path: Path, text: str, headings: tuple[str, ...], failures: list[str]) -> None:
    for heading in headings:
        if heading not in text:
            failures.append(f"{path}: missing heading {heading}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", action="store_true")
    args = parser.parse_args()
    failures: list[str] = []

    for code, expected in EXPECTED.items():
        programme = MATERIAL / code
        for area in ("Curriculum", "Roadmap", "Reference"):
            if not (programme / area).is_dir():
                failures.append(f"missing {programme / area}")

        curriculum = programme / "Curriculum"
        actual = {
            "phases": count_dirs(curriculum, "Phase_*"),
            "modules": count_dirs(curriculum, "Module_*"),
            "lessons": count_dirs(curriculum, "Lesson_*"),
        }
        if actual != expected:
            failures.append(f"{code}: expected {expected}, got {actual}")

        lesson_numbers = sorted(
            int(path.name.split("-", 1)[0].split("_", 1)[1])
            for path in curriculum.rglob("Lesson_*")
        )
        expected_numbers = list(range(1, expected["lessons"] + 1))
        if lesson_numbers != expected_numbers:
            failures.append(f"{code}: lesson sequence is not 1..{expected['lessons']}")

        roadmap_root = programme / "Roadmap"
        programme_roadmap = roadmap_root / "roadmap.md"
        programme_text = programme_roadmap.read_text(encoding="utf-8")
        if not programme_text.startswith(f"# Chương trình "):
            failures.append(f"{programme_roadmap}: invalid programme title")
        require_headings(programme_roadmap, programme_text, PROGRAMME_HEADINGS, failures)
        if programme_text.count("```mermaid") != 1:
            failures.append(
                f"{programme_roadmap}: expected one Mermaid block, "
                f"got {programme_text.count('```mermaid')}"
            )

        phase_roadmaps = sorted(roadmap_root.glob("Phase_*/roadmap.md"))
        module_roadmaps = sorted(roadmap_root.glob("Phase_*/Module_*/roadmap.md"))
        if len(phase_roadmaps) != expected["phases"]:
            failures.append(f"{code}: expected {expected['phases']} phase roadmaps, got {len(phase_roadmaps)}")
        if len(module_roadmaps) != expected["modules"]:
            failures.append(f"{code}: expected {expected['modules']} module roadmaps, got {len(module_roadmaps)}")

        for path in phase_roadmaps:
            text = path.read_text(encoding="utf-8")
            if not re.match(r"^# Giai đoạn \d+: ", text):
                failures.append(f"{path}: invalid phase title")
            require_headings(path, text, PHASE_HEADINGS, failures)
            if text.count("```mermaid") != 1:
                failures.append(f"{path}: expected one Mermaid block, got {text.count('```mermaid')}")

        for path in module_roadmaps:
            text = path.read_text(encoding="utf-8")
            if not re.match(r"^# Mô-đun \d+: ", text):
                failures.append(f"{path}: invalid module title")
            require_headings(path, text, MODULE_HEADINGS, failures)
            if text.count("```mermaid") != 1:
                failures.append(f"{path}: expected one Mermaid block, got {text.count('```mermaid')}")
            table_lessons = [int(value) for value in re.findall(r"^\| L(\d{3}) ·", text, re.MULTILINE)]
            detail_lessons = [int(value) for value in re.findall(r"^### Bài (\d+):", text, re.MULTILINE)]
            diagram_lessons = [int(value) for value in re.findall(r"^\s+L(\d{3}) --> A\d{3}\[", text, re.MULTILINE)]
            manifest_lessons = sorted(
                int(item.parent.name.split("-", 1)[0].split("_", 1)[1])
                for item in path.parent.glob("Lesson_*/roadmap.yaml")
            )
            if not (table_lessons == detail_lessons == diagram_lessons == manifest_lessons):
                failures.append(f"{path}: lesson table, detail, Mermaid and manifests do not match")
            if "**In-class" in text or "**Self-study" in text or "## Lesson specifications" in text:
                failures.append(f"{path}: legacy roadmap format remains")

        if args.inventory:
            print(f"{code}: {actual['phases']} phases · {actual['modules']} modules · {actual['lessons']} lessons")

    roadmaps_md = list(MATERIAL.rglob("Roadmap/**/*.md"))
    roadmaps_drawio = list(MATERIAL.rglob("Roadmap/**/*.drawio"))
    references = [path for path in MATERIAL.rglob("Reference/**/*") if path.is_file()]
    protected_references = [
        path
        for path in references
        if path.name != "sources.yaml"
        and path not in {
            MATERIAL / "DA" / "Reference" / "README.md",
            MATERIAL / "DE" / "Reference" / "README.md",
        }
    ]
    note_files = list(MATERIAL.rglob("Curriculum/**/note.md"))
    after_note_files = list(MATERIAL.rglob("Curriculum/**/after-note.md"))
    lesson_manifests = list(MATERIAL.rglob("Curriculum/**/lesson.yaml"))
    mindmaps = list(MATERIAL.rglob("Curriculum/**/diagrams/mindmap.drawio"))
    lesson_roadmaps = list(MATERIAL.rglob("Roadmap/**/Lesson_*/roadmap.yaml"))
    lesson_sources = list(MATERIAL.rglob("Reference/**/Lesson_*/sources.yaml"))
    diagram_manifest_path = ROOT / "Artifact" / "Rabbit-Data" / "Roadmaps" / "manifest.json"

    for label, actual, expected in (
        ("roadmap Markdown", len(roadmaps_md), 56),
        ("roadmap Draw.io", len(roadmaps_drawio), 42),
        ("lesson note", len(note_files), 525),
        ("protected reference files", len(protected_references), 2126),
        ("after-note scaffold", len(after_note_files), 525),
        ("lesson manifest", len(lesson_manifests), 525),
        ("lesson mindmap", len(mindmaps), 525),
        ("lesson roadmap manifest", len(lesson_roadmaps), 525),
        ("lesson reference manifest", len(lesson_sources), 525),
    ):
        if actual != expected:
            failures.append(f"{label}: expected {expected}, got {actual}")

    for forbidden in (ROOT / "material", ROOT / ".data-2026", ROOT / "Web"):
        if forbidden.exists():
            failures.append(f"legacy path still exists: {forbidden}")

    if not diagram_manifest_path.is_file():
        failures.append(f"missing {diagram_manifest_path}")
    else:
        diagram_manifest = json.loads(diagram_manifest_path.read_text(encoding="utf-8"))
        items = diagram_manifest.get("items", [])
        if diagram_manifest.get("diagram_count") != 56 or len(items) != 56:
            failures.append(f"{diagram_manifest_path}: expected 56 diagram records")
        for item in items:
            source = ROOT / item["source"]
            image = ROOT / item["image"]
            if not source.is_file() or hashlib.sha256(source.read_bytes()).hexdigest() != item["source_sha256"]:
                failures.append(f"{source}: rendered diagram source hash is stale")
            if not image.is_file() or hashlib.sha256(image.read_bytes()).hexdigest() != item["image_sha256"]:
                failures.append(f"{image}: rendered diagram image hash is stale")
                continue
            try:
                ET.parse(image)
            except ET.ParseError as error:
                failures.append(f"{image}: invalid SVG XML: {error}")

    if args.inventory:
        print(f"Roadmap: {len(roadmaps_md)} Markdown · {len(roadmaps_drawio)} Draw.io")
        print(f"Reference: {len(protected_references)} protected files · {len(lesson_sources)} lesson manifests")
        print(f"Lessons: {len(note_files)} notes · {len(after_note_files)} after-notes · {len(lesson_manifests)} manifests")

    approval_path = ROOT / "Tools" / "Curriculum" / "Manifests" / "roadmap-approved.json"
    approvals = json.loads(approval_path.read_text(encoding="utf-8"))
    for approval in approvals:
        for relative_path in approval["scope"]:
            artifact = ROOT / relative_path
            digest = hashlib.sha256(artifact.read_bytes()).hexdigest()
            if digest != approval["artifact_sha256"]:
                print(
                    "WARNING: approval hash is stale: "
                    f"{relative_path} expected {approval['artifact_sha256']} got {digest}"
                )

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("PASS: repository structure is internally consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

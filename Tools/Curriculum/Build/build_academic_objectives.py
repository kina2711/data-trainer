#!/usr/bin/env python3
"""Build the DA/DE objective registry from the hierarchical roadmap sources."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
MATERIAL = ROOT / "Material"
OUTPUT = ROOT / "Tools" / "Curriculum" / "Manifests" / "Academic" / "objectives.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def section(text: str, heading: str) -> str:
    match = re.search(
        rf"^## {re.escape(heading)}\s*$\n(.*?)(?=^## |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not match:
        raise ValueError(f"Thiếu mục: {heading}")
    return match.group(1).strip()


def paragraph(value: str) -> str:
    before_subheading = re.split(r"^### ", value, maxsplit=1, flags=re.MULTILINE)[0]
    blocks = re.split(r"\n\s*\n", before_subheading.strip())
    return " ".join(line.strip() for line in blocks[0].splitlines()) if blocks and blocks[0] else ""


def split_row(line: str) -> list[str]:
    cells = re.split(r"(?<!\\)\|", line.strip().strip("|"))
    return [cell.strip().replace(r"\|", "|") for cell in cells]


def table(value: str) -> list[dict[str, str]]:
    lines = [line for line in value.splitlines() if line.startswith("|")]
    if len(lines) < 2:
        return []
    headers = split_row(lines[0])
    rows: list[dict[str, str]] = []
    for line in lines[2:]:
        cells = split_row(line)
        if len(cells) != len(headers):
            raise ValueError(f"Dòng bảng có {len(cells)} ô, cần {len(headers)}: {line}")
        rows.append(dict(zip(headers, cells, strict=True)))
    return rows


def source_ref(path: Path, locator: str) -> dict[str, str]:
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "locator": locator,
        "sha256": digest(path),
    }


def phase_number(path: Path) -> int:
    return int(path.parent.name.split("_", 1)[1].split("-", 1)[0])


def module_number(path: Path) -> int:
    return int(path.parent.name.split("_", 1)[1].split("-", 1)[0])


def lesson_number(value: str) -> int:
    match = re.search(r"L(\d{3})", value)
    if not match:
        raise ValueError(f"Không đọc được mã lesson từ: {value}")
    return int(match.group(1))


def lesson_numbers(value: str) -> list[int]:
    numbers: list[int] = []
    for match in re.finditer(r"L(\d{3})(?:[–-]L?(\d{3}))?", value):
        first = int(match.group(1))
        last = int(match.group(2)) if match.group(2) else first
        numbers.extend(range(first, last + 1))
    return sorted(set(numbers))


def programme_record(code: str, path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    rows = table(section(text, "Đầu ra chương trình"))
    return {
        "id": code,
        "kind": "programme",
        "programme": code,
        "parent_id": None,
        "title": re.match(r"# (.+)", text).group(1),
        "objective": paragraph(section(text, "Năng lực đích")),
        "outcomes": [
            {
                "id": row["Mã"],
                "action": row["Người hoàn thành có thể"],
                "evidence": row["Bằng chứng"],
                "threshold": row["Ngưỡng đạt"],
            }
            for row in rows
        ],
        "source": source_ref(path, "## Năng lực đích; ## Đầu ra chương trình"),
    }


def phase_record(code: str, path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    number = phase_number(path)
    assessments = table(section(text, "Bài kiểm tra cuối giai đoạn"))
    if len(assessments) != 1:
        raise ValueError(f"{path}: cần đúng một dòng đánh giá phase")
    assessment = assessments[0]
    return {
        "id": f"{code}-P{number:02d}",
        "kind": "phase",
        "programme": code,
        "parent_id": code,
        "title": re.match(r"# Giai đoạn \d+: (.+)", text).group(1),
        "objective": paragraph(section(text, "Đầu ra giai đoạn")),
        "prerequisites": table(section(text, "Điều kiện đầu vào")),
        "assessment": {
            "evidence": assessment["Bằng chứng"],
            "threshold": assessment["Ngưỡng đạt"],
            "critical_failure": assessment["Lỗi loại trực tiếp"],
        },
        "source": source_ref(path, "## Đầu ra giai đoạn; ## Bài kiểm tra cuối giai đoạn"),
    }


def module_and_lessons(code: str, path: Path) -> tuple[dict[str, object], list[dict[str, object]]]:
    text = path.read_text(encoding="utf-8")
    number = module_number(path)
    phase = phase_number(path.parent.parent / "roadmap.md")
    module_id = f"{code}-M{number:02d}"
    module = {
        "id": module_id,
        "kind": "module",
        "programme": code,
        "parent_id": f"{code}-P{phase:02d}",
        "title": re.match(r"# Mô-đun \d+: (.+)", text).group(1),
        "objective": paragraph(section(text, "Đầu ra mô-đun")),
        "prerequisites": table(section(text, "Điều kiện đầu vào")),
        "completion_criteria": table(section(text, "Tiêu chí hoàn thành")),
        "source": source_ref(path, "## Đầu ra mô-đun; ## Tiêu chí hoàn thành"),
    }

    lesson_rows = table(section(text, "Các bài trong mô-đun"))
    assessment_rows = table(section(text, "Ma trận đánh giá"))
    lab_rows = table(section(text, "Bài thực hành bắt buộc"))
    assessments = {lesson_number(row["Mã đầu ra"]): row for row in assessment_rows}
    labs: dict[int, list[dict[str, str]]] = {}
    for row in lab_rows:
        for number_in_row in lesson_numbers(row["Bài liên quan"]):
            labs.setdefault(number_in_row, []).append(row)

    lessons: list[dict[str, object]] = []
    for row in lesson_rows:
        lesson = lesson_number(row["Bài"])
        assessment = assessments.get(lesson)
        lesson_labs = labs.get(lesson, [])
        if not assessment:
            raise ValueError(f"{path}: thiếu assessment cho L{lesson:03d}")
        title = re.sub(r"^L\d{3}\s*·\s*", "", row["Bài"])
        lessons.append(
            {
                "id": f"{code}-L{lesson:03d}",
                "kind": "lesson",
                "programme": code,
                "parent_id": module_id,
                "phase_id": f"{code}-P{phase:02d}",
                "title": title,
                "lesson_type": row["Dạng"],
                "objective": row["Đầu ra"],
                "evidence": row["Bằng chứng"],
                "threshold": assessment["Ngưỡng đạt"],
                "prerequisites": row["Điều kiện tiên quyết"],
                "bloom_level": assessment["Mức độ tư duy"],
                "assessment": assessment["Cách đánh giá"],
                "reassessment": assessment["Hình thức kiểm tra lại"],
                "practice": " · ".join(lab["Sản phẩm bắt buộc"] for lab in lesson_labs)
                or row["Bằng chứng"],
                "critical_failure": " · ".join(
                    lab["Lỗi được cài vào tình huống"] for lab in lesson_labs
                ),
                "source": source_ref(
                    path,
                    f"## Các bài trong mô-đun: L{lesson:03d}; ## Ma trận đánh giá: L{lesson:03d}",
                ),
            }
        )
    return module, lessons


def main() -> int:
    records: list[dict[str, object]] = []
    for code in ("DA", "DE"):
        roadmap_root = MATERIAL / code / "Roadmap"
        records.append(programme_record(code, roadmap_root / "roadmap.md"))
        phase_paths = sorted(roadmap_root.glob("Phase_*/roadmap.md"))
        for phase_path in phase_paths:
            records.append(phase_record(code, phase_path))
            for module_path in sorted(phase_path.parent.glob("Module_*/roadmap.md")):
                module, lessons = module_and_lessons(code, module_path)
                records.append(module)
                records.extend(lessons)

    payload = {
        "schema_version": 1,
        "status": "draft",
        "owner": "kina2711",
        "source_of_truth": "Material/<programme>/Roadmap/**/roadmap.md",
        "scope": ["DA", "DE"],
        "counts": {
            kind: sum(record["kind"] == kind for record in records)
            for kind in ("programme", "phase", "module", "lesson")
        },
        "records": records,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload["counts"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

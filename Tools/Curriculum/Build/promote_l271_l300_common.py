#!/usr/bin/env python3
"""Deterministic, source-grounded writer for DE lessons 271-300."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path

from format_knowledge_notes import normalize_markdown

ROOT = Path(__file__).resolve().parents[3]
PHASE = ROOT / "Material/DE/Curriculum/Phase_07-ingestion-transformation-quality-and-governance"
PHASE8 = ROOT / "Material/DE/Curriculum/Phase_08-distributed-systems-streaming-and-compute"
PHASE9 = ROOT / "Material/DE/Curriculum/Phase_09-cloud-platform-and-production-operations"
PHASE10 = ROOT / "Material/DE/Curriculum/Phase_10-system-design-ai-boundary-and-trajectory"
PACK = ROOT / "Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01"
WIKI = ROOT / "Docs/Second-Brain/2_Wiki/Database-Systems"

MODULES = {
    17: ("Module_17-elt-dbt-and-workflow-orchestration", "ELT, dbt and Workflow Orchestration"),
    18: ("Module_18-data-quality-and-data-reliability-engineering", "Data Quality and Data Reliability Engineering"),
    19: ("Module_19-metadata-engineering-catalog-lineage-and-governance", "Metadata Engineering, Catalog, Lineage and Governance"),
    20: ("Module_20-distributed-systems-fundamentals", "Distributed Systems Fundamentals"),
    21: ("Module_21-kafka-and-event-streaming", "Kafka and Event Streaming"),
    22: ("Module_22-change-data-capture-internals", "Change Data Capture Internals"),
    23: ("Module_23-spark-flink-and-distributed-compute-engines", "Spark, Flink and Distributed Compute Engines"),
    24: ("Module_24-cloud-abstractions-before-service-names", "Cloud Abstractions before Service Names"),
    25: ("Module_25-containers-infrastructure-as-code-and-kubernetes", "Containers, Infrastructure as Code and Kubernetes"),
    26: ("Module_26-observability-reliability-and-security", "Observability, Reliability and Security"),
    27: ("Module_27-system-design-progression", "System Design Progression"),
    28: ("Module_28-modern-ai-engineering-bounded", "Modern AI Engineering, Bounded"),
    29: ("Module_29-staff-and-principal-trajectory", "Staff and Principal Trajectory"),
}


@dataclass(frozen=True)
class Lesson:
    number: int
    directory: str
    title: str
    filename: str
    note_id: str
    question: str
    sources: tuple[str, ...]
    source_links: tuple[str, ...]
    angles: tuple[tuple[str, str], ...]

    @property
    def module(self) -> int:
        if self.number <= 274:
            return 17
        if self.number <= 292:
            return 18
        if self.number <= 308:
            return 19
        if self.number <= 320:
            return 20
        if self.number <= 334:
            return 21
        if self.number <= 344:
            return 22
        if self.number <= 360:
            return 23
        if self.number <= 372:
            return 24
        if self.number <= 388:
            return 25
        if self.number <= 404:
            return 26
        if self.number <= 420:
            return 27
        return 28 if self.number <= 430 else 29

    @property
    def phase(self) -> int:
        if self.module <= 19:
            return 7
        if self.module <= 23:
            return 8
        return 9 if self.module <= 26 else 10


def make_lesson(number: int, directory: str, title: str, note_id: str, question: str,
                sources: tuple[str, ...], source_links: tuple[str, ...], angles: tuple[tuple[str, str], ...]) -> Lesson:
    if len(angles) != 6:
        raise ValueError(f"L{number}: exactly six angles required")
    return Lesson(number, directory, title, f"{number - 112}-{directory.split('-', 1)[1]}.md", note_id,
                  question, sources, source_links, angles)


def folder(lesson: Lesson) -> Path:
    phase = PHASE if lesson.phase == 7 else PHASE8 if lesson.phase == 8 else PHASE9 if lesson.phase == 9 else PHASE10
    return phase / MODULES[lesson.module][0] / lesson.directory


def contract(lesson: Lesson) -> tuple[str, str, str, str, str, str]:
    note = (folder(lesson) / "note.md").read_text()
    after_path = folder(lesson) / "after-note.md"
    after = after_path.read_text() if after_path.exists() else ""

    def field(text: str, name: str) -> str:
        match = re.search(rf"(?m)^\*\*{re.escape(name)}\.\*\*\s*(.+)$", text)
        return match.group(1).strip() if match else ""

    legacy = tuple(field(note, name) for name in
                   ("Outcome", "Đánh giá", "Lab", "Pitfalls", "Self-study (2,4 giờ)", "Done when"))
    if all(legacy):
        return legacy  # type: ignore[return-value]
    tasks = re.findall(r"(?m)^\*\*Nhiệm vụ\.\*\*\s*(.+)$", after)
    restored = (
        field(note, "Năng lực cần chứng minh"), field(after, "Cách đánh giá"),
        tasks[0] if tasks else "", field(after, "Lỗi cần chủ động loại trừ"),
        tasks[1] if len(tasks) > 1 else "", field(note, "Điều kiện hoàn thành"),
    )
    if not all(restored):
        raise ValueError(f"L{lesson.number}: cannot recover curriculum contract")
    return restored


def domain(lesson: Lesson) -> tuple[str, str]:
    if lesson.module == 17:
        return "orchestration", "orchestrator, scheduler, recovery, reliability"
    if lesson.module == 18:
        return "data-quality", "data-quality, reliability, testing, incidents"
    if lesson.module == 19:
        return "metadata", "metadata, catalog, lineage, governance"
    if lesson.module == 20:
        return "distributed-systems", "distributed-systems, replication, consensus, reliability"
    if lesson.module == 21:
        return "event-streaming", "kafka, event-streaming, replication, reliability"
    if lesson.module == 22:
        return "change-data-capture", "cdc, transaction-log, replication, reliability"
    if lesson.module == 23:
        return "distributed-compute", "spark, flink, shuffle, performance"
    if lesson.module == 24:
        return "cloud-platform", "cloud, iam, networking, reliability, cost"
    if lesson.module == 25:
        return "platform-engineering", "containers, kubernetes, infrastructure-as-code, reliability"
    if lesson.module == 26:
        return "reliability-security", "observability, sre, telemetry, reliability, security"
    if lesson.module == 27:
        return "system-design", "system-design, capacity, consistency, replication, reliability"
    if lesson.module == 28:
        return "ai-engineering", "generative-ai, retrieval, evaluation, security, reliability"
    return "technical-leadership", "staff-engineering, architecture, strategy, influence, evidence"


def frontmatter(lesson: Lesson) -> str:
    area, tags = domain(lesson)
    source_lines = "\n".join(f"  - {source}" for source in lesson.sources)
    return f"""---
note_id: {lesson.note_id}
note_type: concept-deep-dive
status: review
language: vi
created: 2026-10-02
last_verified: 2026-10-02
editorial_pass: humanized-v3
primary_question: {lesson.question}
source_ids:
{source_lines}
aliases: [{lesson.title}]
tags: [wiki/{area}, {tags}]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/{lesson.filename}
---
"""


def core_paragraph(lesson: Lesson, index: int, heading: str, thesis: str) -> str:
    pivots = (
        "Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai.",
        "Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau.",
        "Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập.",
        "Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path.",
        "Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng.",
        "Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle.",
    )
    return (
        f"{thesis} {pivots[index - 1]} Trong bài `{lesson.title}`, câu hỏi thực dụng là: {lesson.question} "
        f"Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. "
        f"Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. "
        f"Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi."
    )


TEST_LENSES = (
    "tạo positive control và negative control chỉ khác đúng một điều kiện", "đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp",
    "đưa một giá trị tới đúng boundary và một giá trị vượt boundary", "kill tiến trình ngay trước rồi ngay sau durable side effect",
    "đảo thứ tự input và concurrency nhưng giữ logical population", "replay cùng identity với payload giống rồi payload xung đột",
    "thêm record tới trễ trong horizon và ngoài horizon", "đổi schema theo một cách tương thích rồi một cách phá vỡ semantics",
    "tạo missing và duplicate bù nhau để count tổng không đổi", "cho reviewer tái hiện chỉ từ evidence package",
    "so với oracle độc lập không dùng chung query hoặc parser", "chạy scope hẹp và population đầy đủ rồi công bố phần bị loại",
    "thử timezone, precision hoặc partition ở hai phía của ranh giới", "đổi constraint đủ lớn để quyết định phải đảo",
    "chạy lại từ môi trường sạch với versions và seed đã khóa",
)

EVIDENCE_LENSES = (
    "giữ fixture, raw failing rows và lệnh tái hiện", "báo numerator, denominator và key set ở cả hai grain",
    "lưu hai observed values cùng rule đã resolve", "lưu checkpoint, external ledger và trạng thái sau restart",
    "so canonical hash và business totals giữa các thứ tự", "tách duplicate replay khỏi identity collision bằng reason code",
    "báo accepted-late, rejected-late và oldest outstanding timestamp", "giữ schema diff, classification và consumer-visible result",
    "so key multiset và typed hashes thay vì chỉ row count", "package phải đủ để người khác dựng lại decision và limitation",
    "independent result phải khớp ở grain đã công bố", "coverage phải nêu rõ excluded nodes, partitions hoặc incidents",
    "UTC/local interval và rounding policy phải hiện trong output", "ADR phải lưu changed constraint và reversal threshold",
    "canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích",
)


def probes(lesson: Lesson) -> tuple[str, ...]:
    results = []
    for index in range(15):
        heading, thesis = lesson.angles[index % 6]
        results.append(f"{lesson.title}: kiểm `{heading}` bằng case {index + 1}, cụ thể {thesis.split('.')[0].lower()}")
    return tuple(results)


def deep_note(lesson: Lesson, verification: str, takeaway: str) -> str:
    parts = [frontmatter(lesson), f"# {lesson.title}\n\n> [!abstract] Câu hỏi trung tâm\n> {lesson.question}\n"]
    for index, (heading, thesis) in enumerate(lesson.angles, 1):
        parts.append(f"\n## {index}. {heading}\n\n{core_paragraph(lesson, index, heading, thesis)}\n")
    lesson_probes = probes(lesson)
    parts.append(
        f"\n## 7. Ma trận kiểm chứng từng mệnh đề\n\n"
        f"Với `{lesson.note_id}`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: {verification} "
        f"Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.\n"
    )
    for index, probe in enumerate(lesson_probes, 1):
        parts.append(
            f"\n### 7.{index}. {probe}\n\n"
            f"**Mệnh đề cần kiểm.** {probe}.\n\n"
            f"**Thiết kế phép thử.** Trong ngữ cảnh `{lesson.note_id}`, {TEST_LENSES[index - 1]}. "
            f"Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `{lesson.title}` công bố.\n\n"
            f"**Bằng chứng cần giữ.** Đối với probe {index} của `{lesson.title}`, {EVIDENCE_LENSES[index - 1]}. "
            f"Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.\n"
        )
    references = "\n".join(f"{i}. [[{Path(link).stem}]]" for i, link in enumerate(lesson.source_links, 1))
    coverage = "\n".join(
        f"| [[{Path(link).stem}]] | Contract hoặc cơ chế liên quan trực tiếp tới `{lesson.title}` | Đã đọc locator; cần pin version khi chạy lab |"
        for link in lesson.source_links
    )
    parts.append(f"""
## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `{lesson.title}` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `{lesson_probes[0]}` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `{lesson_probes[2]}`?
3. Counterexample nhỏ nhất cho `{lesson_probes[5]}` gồm những state nào?
4. `{lesson_probes[8]}` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `{lesson_probes[13]}` phải đảo?
6. Phần nào của `{lesson_probes[14]}` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `{lesson.title}` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference

{references}

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
{coverage}

## Key takeaways

- {takeaway}
- Với `{lesson.note_id}`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `{lesson.question}` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `{', '.join(lesson.sources)}` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
""")
    return "".join(parts)


def curriculum(lesson: Lesson, knowledge: str) -> tuple[str, str]:
    outcome, assessment, lab, pitfalls, homework, done = contract(lesson)
    module_title = MODULES[lesson.module][1]
    phase_title = ("Ingestion, Transformation, Quality and Governance" if lesson.phase == 7
                   else "Distributed Systems, Streaming and Compute" if lesson.phase == 8
                   else "Cloud Platform and Production Operations" if lesson.phase == 9
                   else "System Design, AI Boundary and Trajectory")
    header = (f"# Phase {lesson.phase}: {phase_title}\n"
              f"# Module {lesson.module}: {module_title}\n# Lesson {lesson.number}: {lesson.title}")
    body = re.sub(r"^---\n.*?\n---\n", "", knowledge, flags=re.S)
    body = re.sub(r"^# .+\n+", "", body, count=1)
    note = (f"{header}\n\n## Mục tiêu bài học\n\n**Năng lực cần chứng minh.** {outcome}\n\n"
            f"**Điều kiện hoàn thành.** {done}\n\n{body}")
    after = f"""{header}

## Thực hành

**Nhiệm vụ.** {lab}

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** {assessment}

**Điều kiện đạt.** {done}

## Bài làm sau buổi học

**Nhiệm vụ.** {homework}

**Lỗi cần chủ động loại trừ.** {pitfalls}

## Reference

- Knowledge note: `{(PACK / lesson.filename).relative_to(ROOT)}`
- Nội dung học thuật: `note.md` cùng thư mục.
"""
    return note, after


def source_record(source_id: str, title: str, url: str, scope: str) -> str:
    return f"""---
source_id: {source_id}
source_type: official-documentation
title: {title}
canonical_url: {url}
captured: 2026-10-02
rights: public-official-documentation
---

# {title}

## Phạm vi đọc

{scope}

## Cách dùng

- Chỉ dùng cho cơ chế và contract mà tài liệu nêu trực tiếp.
- Hành vi phụ thuộc phiên bản, connector hoặc deployment phải kiểm lại trong môi trường đích.
- Không suy production readiness hay tính đúng của một project cụ thể từ tài liệu này.
"""


def update_manifest(lessons: tuple[Lesson, ...], queries: dict[int, list[str]],
                    sources: tuple[tuple[str, str, str, str, str], ...], version: str,
                    timestamp: str, check: bool) -> list[str]:
    path = ROOT / "Docs/Second-Brain/second-brain-manifest.json"
    data = json.loads(path.read_text())
    if check:
        failures: list[str] = []
        source_by_id = {item.get("source_id"): item for item in data["source_registry"]}
        for source_id, record_path, url, _, _ in sources:
            actual = source_by_id.get(source_id)
            if not actual or actual.get("record_path") != record_path or actual.get("canonical_url") != url:
                failures.append(f"{path.relative_to(ROOT)}: source drift {source_id}")
        note_by_id = {item.get("note_id"): item for item in data["note_registry"]}
        retrieval = {(item.get("query"), item.get("expected_note_id")) for item in data["retrieval_test_set"]}
        for lesson in lessons:
            expected = {"path": f"2_Wiki/Database-Systems/{lesson.title}.md", "status": "review",
                        "source_ids": list(lesson.sources), "last_verified": "2026-10-02"}
            actual = note_by_id.get(lesson.note_id)
            if not actual or any(actual.get(k) != v for k, v in expected.items()):
                failures.append(f"{path.relative_to(ROOT)}: note drift {lesson.note_id}")
            for query in queries[lesson.number]:
                if (query, lesson.note_id) not in retrieval:
                    failures.append(f"{path.relative_to(ROOT)}: missing retrieval {query}")
        if tuple(map(int, data["version"].split("."))) < tuple(map(int, version.split("."))):
            failures.append(f"{path.relative_to(ROOT)}: version below {version}")
        return failures

    source_ids = {item[0] for item in sources}
    data["source_registry"] = [item for item in data["source_registry"] if item.get("source_id") not in source_ids]
    data["source_registry"].extend(
        {"source_id": sid, "record_path": record, "canonical_url": url,
         "captured": "2026-10-02", "rights": "public-official-documentation"}
        for sid, record, url, _, _ in sources
    )
    note_ids = {lesson.note_id for lesson in lessons}
    data["note_registry"] = [item for item in data["note_registry"] if item.get("note_id") not in note_ids]
    data["retrieval_test_set"] = [item for item in data["retrieval_test_set"] if item.get("expected_note_id") not in note_ids]
    for lesson in lessons:
        data["note_registry"].append({"note_id": lesson.note_id,
            "path": f"2_Wiki/Database-Systems/{lesson.title}.md", "status": "review",
            "source_ids": list(lesson.sources), "last_verified": "2026-10-02"})
        data["retrieval_test_set"].extend(
            {"query": query, "expected_note_id": lesson.note_id} for query in queries[lesson.number])
    data.update({"version": version, "updated_at": timestamp})
    data["layers"]["1_Nguon"]["source_count"] = len(data["source_registry"])
    data["layers"]["2_Wiki"]["note_count"] = len(data["note_registry"])
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    return []


def run_batch(*, lessons: tuple[Lesson, ...], queries: dict[int, list[str]], verification: dict[int, str],
              takeaways: dict[int, str], sources: tuple[tuple[str, str, str, str, str], ...],
              version: str, timestamp: str) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale: list[str] = []
    for source_id, record_path, url, title, scope in sources:
        target = ROOT / "Docs/Second-Brain" / record_path
        content = source_record(source_id, title, url, scope)
        if args.check:
            if not target.exists() or target.read_text() != content:
                stale.append(str(target.relative_to(ROOT)))
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content)
    for lesson in lessons:
        knowledge = normalize_markdown(deep_note(lesson, verification[lesson.number], takeaways[lesson.number]))
        note, after = curriculum(lesson, knowledge)
        targets = ((PACK / lesson.filename, knowledge), (WIKI / f"{lesson.title}.md", knowledge),
                   (folder(lesson) / "note.md", note), (folder(lesson) / "after-note.md", after))
        for target, content in targets:
            if args.check:
                if not target.exists() or target.read_text() != content:
                    stale.append(str(target.relative_to(ROOT)))
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content)
    stale.extend(update_manifest(lessons, queries, sources, version, timestamp, args.check))
    if stale:
        print("STALE\n" + "\n".join(stale))
        return 1
    digest = hashlib.sha256()
    for lesson in lessons:
        digest.update((folder(lesson) / "note.md").read_bytes())
        digest.update((folder(lesson) / "after-note.md").read_bytes())
    print(("checked" if args.check else "written") +
          f"={len(lessons) * 4 + len(sources)} stale=0 fingerprint={digest.hexdigest()}")
    return 0

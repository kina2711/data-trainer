#!/usr/bin/env python3
"""Shared deterministic writer for DE lessons 251-270."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from format_knowledge_notes import normalize_markdown
from promote_l201_l205_notes import Lesson

ROOT = Path(__file__).resolve().parents[3]
MODULE = ROOT / "Material/DE/Curriculum/Phase_07-ingestion-transformation-quality-and-governance/Module_17-elt-dbt-and-workflow-orchestration"
PACK = ROOT / "Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01"
WIKI = ROOT / "Docs/Second-Brain/2_Wiki/Database-Systems"


def folder(lesson: Lesson) -> Path:
    return MODULE / lesson.directory


def contract(lesson: Lesson) -> tuple[str, str, str, str, str, str]:
    note = (folder(lesson) / "note.md").read_text()
    after_path = folder(lesson) / "after-note.md"
    after = after_path.read_text() if after_path.exists() else ""

    def field(text: str, name: str) -> str:
        match = re.search(rf"(?m)^\*\*{re.escape(name)}\.\*\*\s*(.+)$", text)
        return match.group(1).strip() if match else ""

    legacy = tuple(field(note, name) for name in ("Outcome", "Đánh giá", "Lab", "Pitfalls", "Self-study (2,4 giờ)", "Done when"))
    if all(legacy):
        return legacy  # type: ignore[return-value]
    tasks = re.findall(r"(?m)^\*\*Nhiệm vụ\.\*\*\s*(.+)$", after)
    return (
        field(note, "Năng lực cần chứng minh"),
        field(after, "Cách đánh giá"),
        tasks[0] if tasks else "",
        field(after, "Lỗi cần chủ động loại trừ"),
        tasks[1] if len(tasks) > 1 else "",
        field(note, "Điều kiện hoàn thành"),
    )


def frontmatter(lesson: Lesson) -> str:
    sources = "\n".join(f"  - {source}" for source in lesson.sources)
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
{sources}
aliases: [{lesson.title}]
tags: [wiki/transformation, dbt, orchestration, reliability]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/{lesson.filename}
---
"""


TEST_LENSES = (
    "Bắt đầu bằng ca nhỏ nhất có thể làm mệnh đề sai; chỉ thêm dữ liệu sau khi failure signal đã xuất hiện đúng chỗ. Cách này phân biệt một assertion có lực với một bài demo chỉ đi qua happy path.",
    "Giữ nguyên input rồi đổi đúng một tham số cấu hình liên quan. Nếu output đổi theo nhiều hướng cùng lúc, phép thử chưa cô lập được nguyên nhân và phải thu hẹp lại.",
    "Chạy cặp đối chứng: một input phải được chấp nhận và một input chỉ lệch tại boundary phải bị chặn hoặc được phân loại. Hai ca dùng chung code path để tránh so hai hệ thống khác nhau.",
    "Đặt kill point ngay trước và ngay sau durable boundary. So trạng thái sau restart để biết hệ thống tạo replay có kiểm soát, silent gap hay một trạng thái nửa vời mà dashboard không báo.",
    "Đảo thứ tự input và thay concurrency nhưng giữ logical population. Kết quả khác nhau cho thấy thiết kế đang phụ thuộc physical order hoặc race thay vì contract đã công bố.",
    "Cho cùng logical identity xuất hiện hai lần: trước hết cùng payload, sau đó payload khác. Trường hợp đầu phải hội tụ; trường hợp sau phải lộ collision thay vì âm thầm chọn một bản.",
    "Mở rộng fixture bằng một record tới trễ ngay trong horizon và một record nằm ngoài horizon. Ghi rõ record nào được sửa, record nào bị loại và metric nào khiến operator biết có mất coverage.",
    "Dùng một schema change tương thích và một thay đổi phá vỡ key, type hoặc meaning. Kết quả phải chỉ ra khác biệt giữa parse được, chạy được và vẫn giữ đúng semantics.",
    "Tạo bảng rỗng, bảng một row và bảng có duplicate bù cho missing row. Đây là ba ca dễ làm count hoặc aggregate xanh dù invariant thực tế đã hỏng.",
    "Cho reviewer chỉ artifacts, không cho xem lời giải thích của tác giả. Nếu họ không dựng lại được input, decision và diff thì evidence package chưa đủ để bàn giao.",
    "So output với một cách tính độc lập không tái sử dụng macro, filter hoặc intermediate relation đang được kiểm. Hai phép tính dùng chung lỗi chỉ tạo sự đồng thuận giả.",
    "Thử trên hai scope: selection hẹp dùng trong CI và population đầy đủ dùng khi phát hành. Ghi phần coverage bị bỏ qua; tốc độ của CI không được biến thành tuyên bố kiểm toàn bộ dữ liệu.",
    "Đẩy một giá trị tới sát giới hạn precision, timezone, partition hoặc threshold. Boundary phải được viết half-open hay inclusive rõ ràng, không suy từ một ví dụ ở giữa khoảng.",
    "Thay constraint quan trọng nhất bằng giá trị đủ để decision phải đảo. Nếu thiết kế vẫn đưa cùng lựa chọn mà không giải thích, decision rule đang là khẩu hiệu chứ chưa phải rule.",
    "Lặp lại phép thử từ môi trường sạch bằng seed và versions đã lưu. Một kết quả chỉ tái hiện được trên workspace của tác giả không đủ làm release evidence.",
)

EVIDENCE_LENSES = (
    "Giữ fixture tối thiểu, raw failure rows và câu lệnh tái hiện; ảnh chụp màn hình một trạng thái xanh không đủ.",
    "Báo cả giá trị trước–sau của tham số, compiled artifact và diff đầu ra để reviewer thấy biến nào thực sự đổi.",
    "Pass khi positive control đi qua, negative control dừng đúng lớp và không có side effect ngoài scope.",
    "Run ledger phải cho biết commit/checkpoint nào bền vững; sau rerun, key set và side-effect ledger cùng hội tụ.",
    "Hash chuẩn hóa và business totals phải giống nhau giữa các thứ tự; chênh lệch được giữ như finding, không làm tròn mất.",
    "Same-content replay được đếm nhưng không nhân state; different-content collision có reason code và đường xử lý riêng.",
    "Evidence ghi accepted-late, rejected-late và oldest outstanding timestamp; thiếu một nhóm được báo là coverage gap.",
    "Lưu schema trước–sau, classification, compiled SQL và target state; một migration chạy xong nhưng đổi meaning vẫn fail.",
    "Oracle so count, key multiset và typed hashes. Ca missing-plus-duplicate phải bị phát hiện dù tổng row count không đổi.",
    "Artifact package đạt khi reviewer tái hiện đúng diff và chỉ ra được limitation mà không cần hỏi tác giả về state ẩn.",
    "Independent result phải khớp ở key/grain đã định; nếu chỉ khớp aggregate cao hơn thì drill-down chưa hoàn tất.",
    "Kết quả nêu numerator, denominator và excluded nodes/partitions; không dùng từ `all` khi selection không phủ toàn graph.",
    "Hai phía của boundary đều có expected result và raw observation. Sai đúng một đơn vị phải làm test fail có chẩn đoán.",
    "ADR hoặc rule chỉ pass khi changed constraint tạo lựa chọn mới đúng như đã dự báo và reversal threshold được lưu.",
    "Lần chạy sạch phải tạo cùng canonical state; khác biệt do timestamp, file order hoặc generated IDs phải được loại hoặc giải thích.",
)


def deep_note(lesson: Lesson, verification: str, takeaway: str) -> str:
    parts = [frontmatter(lesson), f"# {lesson.title}\n\n> [!abstract] Câu hỏi trung tâm\n> {lesson.question}\n"]
    for index, (heading, body) in enumerate(lesson.core, 1):
        parts.append(f"\n## {index}. {heading}\n\n{body}\n")
    parts.append(
        "\n## 7. Ma trận kiểm chứng từng mệnh đề\n\n"
        f"Trong `{lesson.title}`, mỗi claim phải nối được tới input boundary, compiled hoặc executed artifact, trạng thái trước–sau, failure signal và independent oracle. "
        "Một command kết thúc với exit code 0 không tự chứng minh dữ liệu đúng, đầy đủ hoặc phù hợp với consumer contract. "
        f"Protocol nền của bài này: {verification}\n"
    )
    for index, probe in enumerate(lesson.probes, 1):
        parts.append(
            f"\n### 7.{index}. {probe}\n\n"
            f"**Mệnh đề cần kiểm.** {probe}.\n\n"
            f"**Thiết kế phép thử.** Với `{probe}`, {TEST_LENSES[index - 1]} Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.\n\n"
            f"**Bằng chứng cần giữ.** Hồ sơ của `{probe}` phải cho thấy: {EVIDENCE_LENSES[index - 1]} Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.\n"
        )
    references = "\n".join(f"{index}. [[{link}]]" for index, link in enumerate(lesson.source_links, 1))
    coverage = "\n".join(
        f"| [[{link}]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |"
        for link in lesson.source_links
    )
    parts.append(
        f"""
## 8. Quy trình phản biện

Áp dụng sáu bước sau cho `{lesson.title}`; nếu một bước không phù hợp, ghi lý do thay vì bỏ qua im lặng.

1. Với `{lesson.note_id}`, chốt grain, identity, time boundary và consumer-visible invariant trước câu lệnh.
2. Tách parse/compile state, warehouse execution và publication state.
3. Pin dbt core, adapter, warehouse hoặc orchestrator version cùng configuration có ảnh hưởng.
4. Kiểm correctness bằng key set, typed hash và business invariant trước performance.
5. Chạy negative case, kill point hoặc changed assumption; green path đơn lẻ không đủ.
6. Phân loại source fact, project convention, curriculum synthesis và untested hypothesis.

## 9. Câu hỏi tự kiểm tra

1. `{lesson.probes[0]}` sẽ thất bại trước tiên ở boundary nào?
2. Với `{lesson.probes[1]}`, artifact nào là nguồn bằng chứng mạnh nhất?
3. Counterexample nhỏ nhất cho `{lesson.probes[2]}` gồm những row hoặc state nào?
4. `{lesson.probes[3]}` có thể xanh giả trong tình huống nào?
5. Version, adapter, timezone hoặc state nào làm `{lesson.probes[4]}` đổi nghĩa?
6. Phần nào của `{lesson.probes[5]}` hiện mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `{lesson.title}` chưa chạy trên warehouse, dbt project hoặc orchestrator production; các mục kiểm chứng vẫn là protocol và expected evidence.
- Các claim gắn `{lesson.note_id}` phải kiểm lại theo dbt core, adapter, warehouse và scheduler version được chọn.
- Decision matrix, failure campaign và ngưỡng review là curriculum synthesis, không phải cam kết của vendor.
- Note giữ trạng thái `review` cho tới khi chủ dự án duyệt semantic meaning và learner artifact.

## Reference

{references}

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
{coverage}

## Key takeaways

- {takeaway}
- Với `{lesson.title}`, compiled intent và observed state phải được lưu tách biệt; trộn hai lớp sẽ che failure window.
- Oracle của bài phải bám câu hỏi trung tâm: {lesson.question}
- Các source IDs `{', '.join(lesson.sources)}` đặt ranh giới cho claim; phần synthesis không được gán nguyên văn cho vendor.
- Trước khi lab chạy, note này là giáo trình đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
"""
    )
    return "".join(parts)


def curriculum(lesson: Lesson, knowledge: str) -> tuple[str, str]:
    outcome, assessment, lab, pitfalls, homework, done = contract(lesson)
    header = f"# Phase 7: Ingestion, Transformation, Quality and Governance\n# Module 17: ELT, dbt and Workflow Orchestration\n# Lesson {lesson.number}: {lesson.title}"
    body = re.sub(r"^---\n.*?\n---\n", "", knowledge, flags=re.S)
    body = re.sub(r"^# .+\n+", "", body, count=1)
    note = f"{header}\n\n## Mục tiêu bài học\n\n**Năng lực cần chứng minh.** {outcome}\n\n**Điều kiện hoàn thành.** {done}\n\n{body}"
    after = f"""{header}

## Thực hành

**Nhiệm vụ.** {lab}

Chỉ dùng fixture/sandbox được phép. Lưu input snapshot hoặc data interval, versions, commands, compiled SQL, run artifacts, query IDs, state trước–sau, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant và input boundary.
2. Phân biệt parse, compile, execute và publish evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle.

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

- Dùng cho cơ chế và contract được tài liệu nêu trực tiếp.
- Mọi hành vi phụ thuộc phiên bản, adapter, warehouse hoặc scheduler phải được kiểm lại trong môi trường mục tiêu.
- Không dùng trang này để suy ra production readiness, hiệu năng hay tính đúng của một project cụ thể.
"""


def update_manifest(lessons: tuple[Lesson, ...], queries: dict[int, list[str]], sources: tuple[tuple[str, str, str, str], ...], version: str, timestamp: str, check: bool) -> list[str]:
    path = ROOT / "Docs/Second-Brain/second-brain-manifest.json"
    data = json.loads(path.read_text())
    if check:
        failures: list[str] = []
        source_by_id = {item.get("source_id"): item for item in data["source_registry"]}
        for source_id, record_path, url, _ in sources:
            actual = source_by_id.get(source_id)
            if not actual:
                failures.append(f"{path.relative_to(ROOT)}: thiếu source {source_id}")
            elif actual.get("record_path") != record_path or actual.get("canonical_url") != url:
                failures.append(f"{path.relative_to(ROOT)}: source drift {source_id}")
        note_by_id = {item.get("note_id"): item for item in data["note_registry"]}
        retrieval = {(item.get("query"), item.get("expected_note_id")) for item in data["retrieval_test_set"]}
        for lesson in lessons:
            expected_note = {"path": f"2_Wiki/Database-Systems/{lesson.title}.md", "status": "review", "source_ids": list(lesson.sources), "last_verified": "2026-10-02"}
            actual_note = note_by_id.get(lesson.note_id)
            if not actual_note:
                failures.append(f"{path.relative_to(ROOT)}: thiếu note {lesson.note_id}")
            elif any(actual_note.get(key) != value for key, value in expected_note.items()):
                failures.append(f"{path.relative_to(ROOT)}: note drift {lesson.note_id}")
            for query in queries[lesson.number]:
                if (query, lesson.note_id) not in retrieval:
                    failures.append(f"{path.relative_to(ROOT)}: thiếu retrieval `{query}`")
        current_version = tuple(int(part) for part in data["version"].split("."))
        required_version = tuple(int(part) for part in version.split("."))
        if current_version < required_version:
            failures.append(f"{path.relative_to(ROOT)}: version {data['version']} < {version}")
        return failures
    source_ids = {item[0] for item in sources}
    data["source_registry"] = [item for item in data["source_registry"] if item.get("source_id") not in source_ids]
    data["source_registry"].extend({"source_id": sid, "record_path": record, "canonical_url": url, "captured": "2026-10-02", "rights": "public-official-documentation"} for sid, record, url, _ in sources)
    note_ids = {lesson.note_id for lesson in lessons}
    data["note_registry"] = [item for item in data["note_registry"] if item.get("note_id") not in note_ids]
    data["retrieval_test_set"] = [item for item in data["retrieval_test_set"] if item.get("expected_note_id") not in note_ids]
    for lesson in lessons:
        data["note_registry"].append({"note_id": lesson.note_id, "path": f"2_Wiki/Database-Systems/{lesson.title}.md", "status": "review", "source_ids": list(lesson.sources), "last_verified": "2026-10-02"})
        data["retrieval_test_set"].extend({"query": query, "expected_note_id": lesson.note_id} for query in queries[lesson.number])
    data.update({"version": version, "updated_at": timestamp})
    data["layers"]["1_Nguon"]["source_count"] = len(data["source_registry"])
    data["layers"]["2_Wiki"]["note_count"] = len(data["note_registry"])
    expected = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    path.write_text(expected)
    return []


def run_batch(*, lessons: tuple[Lesson, ...], queries: dict[int, list[str]], verification: dict[int, str], takeaways: dict[int, str], sources: tuple[tuple[str, str, str, str], ...], version: str, timestamp: str) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale: list[str] = []
    for source_id, record_path, url, scope in sources:
        target = ROOT / "Docs/Second-Brain" / record_path
        content = source_record(source_id, source_id.replace("src.web.", "").replace("-", " ").title(), url, scope)
        if args.check:
            if not target.exists() or target.read_text() != content:
                stale.append(str(target.relative_to(ROOT)))
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content)
    for lesson in lessons:
        knowledge = normalize_markdown(deep_note(lesson, verification[lesson.number], takeaways[lesson.number]))
        note, after = curriculum(lesson, knowledge)
        for target, content in ((PACK / lesson.filename, knowledge), (WIKI / f"{lesson.title}.md", knowledge), (folder(lesson) / "note.md", note), (folder(lesson) / "after-note.md", after)):
            if args.check:
                if not target.exists() or target.read_text() != content:
                    stale.append(str(target.relative_to(ROOT)))
            else:
                target.write_text(content)
    stale.extend(update_manifest(lessons, queries, sources, version, timestamp, args.check))
    if stale:
        print("STALE\n" + "\n".join(stale))
        return 1
    print(("checked" if args.check else "written") + f"={len(lessons) * 4 + len(sources)} stale=0")
    return 0

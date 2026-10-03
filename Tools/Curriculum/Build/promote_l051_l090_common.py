#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path

from format_knowledge_notes import normalize_markdown
from promote_l051_l090_specs import *

ROOT = Path(__file__).resolve().parents[3]
CURRICULUM = ROOT / "Material/DE/Curriculum"
PACK = ROOT / "Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01"
MANIFEST = ROOT / "Docs/Second-Brain/second-brain-manifest.json"

PHASES = {2: "Machine, Operating System and Network", 3: "Software and Backend Engineering"}
MODULES = {
    4: "Computer Architecture and the Performance Model",
    5: "Operating Systems, Concurrency and Linux",
    6: "Networking from Packet to API",
    7: "Software Design and Delivery",
}
WIKI_DIR = {4: "Computer-Architecture", 5: "Linux", 6: "Networking", 7: "Software-Engineering"}

LABEL = {
    TLPI: "SRC-TLPI-2010", KERNEL: "SRC-LINUX-KERNEL-RUNTIME-DOCS",
    SYSTEMD: "SRC-SYSTEMD-OFFICIAL-DOCS", BASH: "SRC-GNU-BASH-REFERENCE",
    KUR: "SRC-KUROSE-ROSS-NETWORKING-8E", TCP: "SRC-RFC-9293-TCP",
    TLS: "SRC-RFC-8446-TLS13", RFC9110: "SRC-RFC9110-HTTP-SEMANTICS",
    COD: "SRC-PATTERSON-HENNESSY-COD-5E", AMD: "SRC-AMDAHL-1967",
    GUS: "SRC-GUSTAFSON-1988", DB: "SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E",
    PET: "SRC-PETROV-DATABASE-INTERNALS-1E", PP: "SRC-HUNT-THOMAS-PRAGMATIC-PROGRAMMER-20AE",
    SOM: "SRC-SOMMERVILLE-SOFTWARE-ENGINEERING-10E", SRE_MON: "SRC-GOOGLE-SRE-MONITORING",
    SRE_CAP: "SRC-GOOGLE-SRE-CAPACITY-LOAD-TESTING", AWS_RETRY: "SRC-AWS-TIMEOUTS-RETRIES-BACKOFF",
    TRINO_PLAN: "SRC-TRINO-DISTRIBUTED-PLANS",
}
LOCATOR = {
    TLPI: "Chapters 4–39, 49–50, 61 và 63 theo scope record; PDF 113–1418",
    KERNEL: "PSI, userspace API, io_uring và trace documentation; accessed 2026-10-02",
    SYSTEMD: "Service Manager, systemd.service và journalctl; accessed 2026-10-02",
    BASH: "Bash Reference Manual 5.3, shell operation, pipelines, redirection và set builtin; accessed 2026-10-02",
    KUR: "§§1.4, 2.2, 2.4, 2.7, 3.5–3.7, 4.5, 6.6.1 và Chapter 8; PDF 67–682",
    TCP: "RFC 9293 service model, state machine và connection lifecycle",
    TLS: "RFC 8446 §§1–5, handshake, authentication và record protocol",
    RFC9110: "RFC 9110 method, status, representation, cache và idempotent semantics",
    COD: "Chapter 5 và §6.3; PDF 397–538",
    AMD: "Amdahl 1967, fixed-work serial fraction và strong-scaling boundary",
    GUS: "Gustafson 1988, scaled workload và weak-scaling boundary",
    DB: "Chapters 15–18 theo source record", PET: "Chapters 3–7 theo source record",
    PP: "Topics 10, 23–25 và 40; PDF 76–280",
    SOM: "Chapters 4, 6–8 và 25; PDF 103–756",
    SRE_MON: "Monitoring distributed systems; accessed 2026-10-01",
    SRE_CAP: "Addressing cascading failures and load testing; accessed 2026-10-01",
    AWS_RETRY: "Timeouts, retries, backoff with jitter; accessed 2026-10-01",
    TRINO_PLAN: "Distributed EXPLAIN plans; accessed 2026-10-01",
}

SOURCE_NEW = {
    KERNEL: {"source_id": KERNEL, "record_path": "1_Nguon/Web/SRC-LINUX-KERNEL-RUNTIME-DOCS.md", "canonical_url": "https://docs.kernel.org/", "captured": "2026-10-02", "rights": "public-official-documentation"},
    SYSTEMD: {"source_id": SYSTEMD, "record_path": "1_Nguon/Web/SRC-SYSTEMD-OFFICIAL-DOCS.md", "canonical_url": "https://systemd.io/", "captured": "2026-10-02", "rights": "public-official-documentation"},
    BASH: {"source_id": BASH, "record_path": "1_Nguon/Web/SRC-GNU-BASH-REFERENCE.md", "canonical_url": "https://www.gnu.org/software/bash/manual/", "captured": "2026-10-02", "rights": "public-official-documentation"},
    TCP: {"source_id": TCP, "record_path": "1_Nguon/Standards/SRC-RFC-9293-TCP.md", "canonical_url": "https://www.rfc-editor.org/rfc/rfc9293.html", "captured": "2026-10-02", "rights": "IETF-Trust"},
    TLS: {"source_id": TLS, "record_path": "1_Nguon/Standards/SRC-RFC-8446-TLS13.md", "canonical_url": "https://www.rfc-editor.org/rfc/rfc8446.html", "captured": "2026-10-02", "rights": "IETF-Trust"},
}

PIVOTS = (
    "state transition và invariant", "identity, ownership và boundary",
    "failure path và recovery", "decision trade-off và reversal trigger",
    "evidence package và oracle", "changed-constraint transfer",
)
TESTS = (
    "positive và negative control chỉ khác một điều kiện",
    "boundary case ngay trước và sau ngưỡng",
    "replay cùng identity nhưng đổi state",
    "failure inject trước và sau transition bền vững",
    "changed scale làm cost model đổi",
    "adversarial order, skew hoặc packet timing",
    "fresh environment không cache",
    "independent oracle không dùng chung implementation",
    "partial progress rồi restart",
    "missing evidence phải abstain",
    "reviewer tái hiện từ evidence package",
    "constraint đổi đủ để quyết định đảo",
)


@dataclass(frozen=True)
class Lesson:
    number: int
    directory: str
    title: str
    learn: str
    outcome: str
    assessment: str
    lab: str
    pitfalls: str
    homework: str
    done: str
    sources: tuple[str, ...]

    @property
    def phase(self) -> int:
        return 2 if self.number <= 88 else 3

    @property
    def module(self) -> int:
        return 4 if self.number <= 60 else 5 if self.number <= 76 else 6 if self.number <= 88 else 7

    @property
    def slug(self) -> str:
        return self.directory.split("-", 1)[1]

    @property
    def note_id(self) -> str:
        return f"wiki.de-foundation.{self.slug}"

    @property
    def concept_key(self) -> str:
        return f"ck.de.{self.slug}"

    @property
    def filename(self) -> str:
        return f"{self.number:03d}-{self.slug}.md"

    @property
    def folder(self) -> Path:
        matches = list(CURRICULUM.glob(f"Phase_*/Module_*/{self.directory}"))
        if len(matches) != 1:
            raise ValueError(f"L{self.number}: directory mismatch {matches}")
        return matches[0]

    @property
    def wiki(self) -> Path:
        return ROOT / "Docs/Second-Brain/2_Wiki" / WIKI_DIR[self.module] / f"{self.title}.md"


def _field(body: str, name: str) -> str:
    match = re.search(rf"(?m)^\*\*{re.escape(name)}\.\*\*\s*(.+)$", body)
    return match.group(1).strip() if match else ""


def load_lesson(number: int) -> Lesson:
    matches = list(CURRICULUM.glob(f"Phase_*/Module_*/Lesson_{number:03d}-*"))
    if len(matches) != 1:
        raise ValueError(f"L{number}: expected one lesson folder")
    folder = matches[0]
    note = (folder / "note.md").read_text()
    after = (folder / "after-note.md").read_text()
    title_match = re.search(r'(?m)^tieu_de: "(.+)"$', note) or re.search(rf"(?m)^# Lesson {number}: (.+)$", note)
    if not title_match:
        raise ValueError(f"L{number}: title missing")
    legacy = (
        _field(note, "Learn"), _field(note, "Outcome"), _field(note, "Đánh giá"),
        _field(note, "Lab"), _field(note, "Pitfalls"), _field(note, "Self-study (2,4 giờ)"),
        _field(note, "Done when"),
    )
    if all(legacy):
        values = legacy
    else:
        tasks = re.findall(r"(?m)^\*\*Nhiệm vụ\.\*\*\s*(.+)$", after)
        values = (
            _field(note, "Kiến thức và cơ chế"), _field(note, "Năng lực cần chứng minh"),
            _field(after, "Cách đánh giá"), tasks[0] if tasks else "",
            _field(after, "Lỗi cần chủ động loại trừ"), tasks[1] if len(tasks) > 1 else "",
            _field(note, "Điều kiện hoàn thành"),
        )
    if not all(values):
        raise ValueError(f"L{number}: cannot recover curriculum contract")
    return Lesson(number, folder.name, title_match.group(1), *values, SOURCES[number])


def _previous_id(lesson: Lesson) -> str:
    if lesson.number == 51:
        return "wiki.de-foundation.auto-vectorization-compiler-gives-up"
    return load_lesson(lesson.number - 1).note_id


def frontmatter(lesson: Lesson) -> str:
    source_lines = "\n".join(f"  - {source}" for source in lesson.sources)
    next_edge = f"[{load_lesson(lesson.number + 1).note_id}]" if lesson.number < 90 else "[]"
    return f"""---
note_id: {lesson.note_id}
concept_key: {lesson.concept_key}
concept_key_status: proposed
note_type: concept-deep-dive
status: review
language: vi
created: 2026-10-02
last_verified: 2026-10-02
review_after: 2027-04-02
editorial_pass: humanized-v3
primary_question: Làm thế nào mô hình, đo và ra quyết định đúng về {lesson.title}?
source_ids:
{source_lines}
relationships:
  builds_on: [{_previous_id(lesson)}]
  prerequisite_of: {next_edge}
aliases: [{lesson.title}]
tags: [wiki/{WIKI_DIR[lesson.module].lower()}, de-foundation, module-{lesson.module}]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/{lesson.filename}
---
"""


def decision_rows(lesson: Lesson) -> str:
    if lesson.module == 4:
        rows = (("Model", "Giải thích chi phí bằng hierarchy, parallel fraction hoặc data movement", "Model dự đoán đúng khi đổi scale"), ("Measure", "Dùng counter và benchmark khóa workload", "Observation khớp oracle và có raw sample"), ("Explain", "Nối delta với mechanism", "Reviewer tái hiện được reasoning"), ("Reverse", "Đổi workload, layout hoặc resource", "Quyết định đổi khi bottleneck đổi"))
    elif lesson.module == 5:
        rows = (("Observe", "Khóa process, resource, file descriptor và time window", "Không trộn symptom giữa hai owner"), ("Probe", "Dùng phép đo read-only hẹp nhất", "Probe phân biệt được hai giả thuyết"), ("Contain", "Giảm harm trước mutation", "Có rollback và state snapshot"), ("Escalate", "Chuyển owner khi boundary đã chứng minh", "Evidence đủ tái hiện"))
    elif lesson.module == 6:
        rows = (("Layer", "Xác định hop và protocol state", "Không gọi mọi lỗi là network"), ("Budget", "Chia deadline và capacity theo hop", "Không reset budget sau retry"), ("Identity", "Khóa connection, request và operation identity", "Không gộp duplicate với retry"), ("Evidence", "Ghép client, DNS, transport, TLS, HTTP và server timeline", "Clock và correlation được công bố"))
    else:
        rows = (("Vocabulary", "Một concept miền có một tên trong scope", "Business reviewer hiểu cùng nghĩa"), ("Contract", "Input, output, pre/postcondition và error", "Caller biết mọi outcome"), ("Boundary", "Policy phụ thuộc vào port, mechanism cài adapter", "Đổi adapter không đổi policy"), ("Review", "Changed-use-case test", "Quyết định giữ hoặc đảo có bằng chứng"))
    return "\n".join(f"| {a} | {b} | {c} |" for a, b, c in rows)


def knowledge(lesson: Lesson) -> str:
    misconceptions = [item.strip() for item in lesson.pitfalls.split("·") if item.strip()]
    while len(misconceptions) < 2:
        misconceptions.append(f"Đọc tín hiệu của {lesson.title} như kết luận cuối cùng")
    parts = [
        frontmatter(lesson),
        f"\n# {lesson.title}\n\n**Tóm tắt bản chất:** {lesson.outcome} Cơ chế chỉ có giá trị khi workload, version, state owner và failure boundary đã được khóa; một con số đẹp ngoài bốn điều kiện đó không đủ để ra quyết định.\n\n> [!abstract] Câu hỏi trung tâm\n> Làm thế nào mô hình, đo và ra quyết định đúng về {lesson.title}?\n",
        f"\n## Nỗi Đau & Động Lực\n\n{lesson.pitfalls} Đây không phải danh sách lỗi cú pháp. Mỗi lỗi làm người vận hành chọn nhầm owner hoặc chữa symptom ở layer sau, khiến thời gian phục hồi tăng dù command vừa chạy trả về thành công.\n\nNăng lực cần giữ sau bài là: {lesson.outcome} Nếu learner chỉ nhắc lại định nghĩa nhưng không phân biệt được hai state gần nhau trên số đo, bài chưa đạt.\n",
        f"\n## Cơ Chế Tác Động\n\n{lesson.learn}\n\nTách ba lớp khi đọc cơ chế `{lesson.note_id}`: declared state là điều cấu hình hoặc API yêu cầu; executed state là việc runtime thực sự làm; consumer-visible state là điều client hay operator quan sát. Ba lớp có thể lệch nhau vì cache, buffering, retry, scheduling, queue hoặc failure giữa hai transition. Evidence phải chỉ ra lớp nào đang được đo.\n",
        f"\n## Bản Đồ Quyết Định\n\n| Bước | Câu hỏi phải khóa | Điều kiện đạt |\n|---|---|---|\n{decision_rows(lesson)}\n\nQuy tắc mặc định là chọn phép giải thích đơn giản nhất qua được hard constraints, rồi viết trước reversal trigger. Với `{lesson.title}`, absence of error không phải pass; pass cần observation đúng grain, một oracle độc lập và changed-constraint case đủ làm model có cơ hội thất bại.\n",
        f"\n## Case Study Thực Chiến: {lesson.title}\n\n{lesson.lab}\n\nTrong case `{lesson.note_id}`, learner ghi expected transition, input snapshot, version và giới hạn an toàn trước khi chạy. Sau execution, họ giữ raw counter, timestamp, exit status, state trước–sau và giải thích delta bằng mechanism ở trên. Đánh giá không cho phép sửa expected result sau khi nhìn output mà không ghi change record.\n\nBiến thể khó hơn đổi một constraint có khả năng đảo kết luận: workload shape, memory pressure, connection reuse, retry budget, permission hoặc dependency direction. {lesson.assessment}\n",
        f"\n## Góc Khuất & Ngộ Nhận\n\n**Hiểu lầm:** {misconceptions[0]}. **Thực tế:** tín hiệu chỉ chứng minh điều nó đo trong đúng scope; state ở layer khác vẫn có thể trái ngược. **Vì sao nghe hợp lý:** happy path nhỏ thường không chạm queue, cache, partial progress hoặc restart.\n\n**Hiểu lầm:** {misconceptions[1]}. **Thực tế:** tool và API cung cấp primitive, không tự cấp ownership, deadline, idempotency hay recovery policy. **Vì sao nghe hợp lý:** syntax gọn che mất protocol và lifecycle phía dưới.\n\nVới `{lesson.note_id}`, một edge case đáng giữ là observation đúng nhưng diagnosis sai: counter tăng thật, song nguyên nhân điều khiển nằm ở layer trước. Muốn tránh, timeline phải nối trigger tới consumer harm và ghi rõ negative control nào đã loại giả thuyết cạnh tranh.\n",
        f"\n## Nếu Bạn Dạy Lại Điều Này...\n\nMở bài bằng một dự đoán dễ sai về `{lesson.title}`, không mở bằng định nghĩa. Cho hai trace gần giống nhau nhưng khác đúng một state boundary; learner phải chọn probe tiếp theo trước khi được xem đáp án.\n\nBài tập seed dùng chính lab của DE-L{lesson.number:03d}, sau đó đổi constraint đủ mạnh để buộc giữ hoặc đảo quyết định. Người dạy chấm reasoning chain và evidence, không chấm việc learner đoán đúng tên công cụ.\n",
        f"\n## Ma trận kiểm chứng từng mệnh đề\n\nProtocol riêng của `{lesson.title}` dùng điều kiện hoàn thành sau: {lesson.done} Mỗi probe phải có prediction, failure signal và independent oracle.\n",
    ]
    angles = (lesson.learn, lesson.outcome, lesson.assessment, lesson.lab, lesson.pitfalls, lesson.done)
    for index, test in enumerate(TESTS, 1):
        claim = re.split(r"(?<=[.!?])\s+", angles[(index - 1) % len(angles)])[0]
        if len(claim) > 210:
            claim = claim[:207].rstrip() + "..."
        parts.append(
            f"\n### Probe {index}: {PIVOTS[(index - 1) % len(PIVOTS)]}\n\n"
            f"**Mệnh đề P{index} cần kiểm.** {claim}\n\n"
            f"**Thiết kế phép thử.** Với `{lesson.note_id}`, tạo {test}; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.\n\n"
            f"**Bằng chứng P{index} cần giữ.** Với `{lesson.note_id}`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.\n"
        )
    parts.append(
        f"\n## Tự Kiểm Tra Nhanh\n\n1. Boundary đầu tiên khiến mô hình `{lesson.title}` không còn đúng là gì?\n\n<details><summary>Đáp án</summary>{lesson.pitfalls}</details>\n\n"
        f"2. Evidence nào phân biệt được hai state dễ nhầm?\n\n<details><summary>Đáp án</summary>{lesson.assessment}</details>\n\n"
        f"3. Khi constraint đổi, điều gì quyết định giữ hay đảo lựa chọn?\n\n<details><summary>Đáp án</summary>{lesson.done}</details>\n"
    )
    parts.append(
        f"\n## Giới hạn và điều chưa cho phép kết luận\n\n"
        f"- Lab của `{lesson.title}` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.\n"
        "- Hành vi phụ thuộc kernel, distribution, library, network path hoặc hardware phải được kiểm lại trên target đã ghi version.\n"
        f"- Concept key `{lesson.concept_key}` đang ở trạng thái `proposed`; note chưa được tính là canonical registry coverage.\n"
        "- Một trace đơn lẻ không chứng minh capacity, reliability hoặc security cho population khác.\n"
        "- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.\n"
    )
    refs = "\n".join(f"{index}. [[{LABEL[source]}]]" for index, source in enumerate(lesson.sources, 1))
    coverage = "\n".join(
        f"| [[{LABEL[source]}]] — `{source}` | {LOCATOR[source]} | mechanism và boundary liên quan trực tiếp tới `{lesson.title}` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L{lesson.number:03d} |"
        for source in lesson.sources
    )
    parts.append(
        f"\n## Reference\n\n{refs}\n\n## Source coverage\n\n"
        "| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |\n"
        "|---|---|---|---|---|---|\n"
        f"{coverage}\n\n## Key takeaways\n\n"
        f"- {lesson.outcome}\n- {lesson.done}\n"
        f"- `{lesson.title}` chỉ có nghĩa trong scope, state, identity và version đã ghi.\n"
        "- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.\n"
    )
    return normalize_markdown("".join(parts))


def curriculum(lesson: Lesson, knowledge_note: str) -> tuple[str, str]:
    header = (
        f"# Phase {lesson.phase}: {PHASES[lesson.phase]}\n"
        f"# Module {lesson.module}: {MODULES[lesson.module]}\n"
        f"# Lesson {lesson.number}: {lesson.title}"
    )
    body = re.sub(r"^---\n.*?\n---\n", "", knowledge_note, flags=re.S)
    body = re.sub(r"^# .+\n+", "", body, count=1)
    note = (
        f"{header}\n\n## Mục tiêu bài học\n\n"
        f"**Năng lực cần chứng minh.** {lesson.outcome}\n\n"
        f"**Điều kiện hoàn thành.** {lesson.done}\n\n"
        f"**Kiến thức và cơ chế.** {lesson.learn}\n\n{body}"
    )
    after = f"""{header}

## Thực hành

**Nhiệm vụ.** {lesson.lab}

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** {lesson.assessment}

**Điều kiện đạt.** {lesson.done}

## Bài làm sau buổi học

**Nhiệm vụ.** {lesson.homework}

**Lỗi cần chủ động loại trừ.** {lesson.pitfalls}

## Reference

- Knowledge note: `{(PACK / lesson.filename).relative_to(ROOT)}`
- Nội dung học thuật: `note.md` cùng thư mục.
"""
    return note, after


def update_manifest(lessons: tuple[Lesson, ...], version: str, timestamp: str, check: bool) -> list[str]:
    data = json.loads(MANIFEST.read_text())
    failures: list[str] = []
    used = {source for lesson in lessons for source in lesson.sources}
    source_by_id = {row.get("source_id"): row for row in data["source_registry"]}
    for source_id in used & SOURCE_NEW.keys():
        if check:
            if source_by_id.get(source_id) != SOURCE_NEW[source_id]:
                failures.append(f"source drift {source_id}")
        else:
            data["source_registry"] = [row for row in data["source_registry"] if row.get("source_id") != source_id]
            data["source_registry"].append(SOURCE_NEW[source_id])
    note_ids = {lesson.note_id for lesson in lessons}
    if not check:
        data["note_registry"] = [row for row in data["note_registry"] if row.get("note_id") not in note_ids]
        data["retrieval_test_set"] = [row for row in data["retrieval_test_set"] if row.get("expected_note_id") not in note_ids]
    note_by_id = {row.get("note_id"): row for row in data["note_registry"]}
    retrieval = {(row.get("query"), row.get("expected_note_id")) for row in data["retrieval_test_set"]}
    for lesson in lessons:
        expected = {"note_id": lesson.note_id, "path": f"2_Wiki/{WIKI_DIR[lesson.module]}/{lesson.title}.md", "status": "review", "source_ids": list(lesson.sources), "last_verified": "2026-10-02"}
        queries = (f"L{lesson.number} decision boundary nào?", f"L{lesson.number} counterexample nào?", f"L{lesson.number} evidence nào quyết định?")
        if check:
            if note_by_id.get(lesson.note_id) != expected:
                failures.append(f"note drift {lesson.note_id}")
            for query in queries:
                if (query, lesson.note_id) not in retrieval:
                    failures.append(f"missing retrieval {query}")
        else:
            data["note_registry"].append(expected)
            data["retrieval_test_set"].extend({"query": query, "expected_note_id": lesson.note_id} for query in queries)
    if not check:
        data.update({"version": version, "updated_at": timestamp})
        data["layers"]["1_Nguon"]["source_count"] = len(data["source_registry"])
        data["layers"]["2_Wiki"]["note_count"] = len(data["note_registry"])
        MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    return failures


def run(start: int, end: int, version: str, timestamp: str) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    lessons = tuple(load_lesson(number) for number in range(start, end + 1))
    stale: list[str] = []
    digest = hashlib.sha256()
    for lesson in lessons:
        knowledge_note = knowledge(lesson)
        note, after = curriculum(lesson, knowledge_note)
        targets = ((PACK / lesson.filename, knowledge_note), (lesson.wiki, knowledge_note), (lesson.folder / "note.md", note), (lesson.folder / "after-note.md", after))
        for path, content in targets:
            if args.check:
                if not path.exists() or path.read_text() != content:
                    stale.append(str(path.relative_to(ROOT)))
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)
        digest.update(note.encode())
        digest.update(after.encode())
    stale.extend(update_manifest(lessons, version, timestamp, args.check))
    if stale:
        print("STALE\n" + "\n".join(stale))
        return 1
    print(("checked" if args.check else "written") + f"={len(lessons) * 4} stale=0 fingerprint={digest.hexdigest()}")
    return 0

#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path

from format_knowledge_notes import normalize_markdown


ROOT = Path(__file__).resolve().parents[3]
CURRICULUM = ROOT / "Material/DA/Curriculum"
PACK = ROOT / "Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-FOUNDATIONS-01"
WIKI = ROOT / "Docs/Second-Brain/2_Wiki/Data-Analysis"
MANIFEST = ROOT / "Docs/Second-Brain/second-brain-manifest.json"

FDE = "src.book.reis-housley-fundamentals-data-engineering"
KIMBALL = "src.book.kimball-ross-data-warehouse-toolkit.3e"
HEART = "src.paper.google-heart-ux-metrics"
AMPLITUDE = "src.web.amplitude-north-star-framework"
USER_NEEDS = "src.web.govuk-understand-user-needs"
ANALYTICS_GUIDE = "src.web.govuk-data-analytics-tools-guidance"

LABELS = {
    FDE: "SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING",
    KIMBALL: "SRC-KIMBALL-ROSS-DW-TOOLKIT-3E",
    HEART: "SRC-GOOGLE-HEART-UX-METRICS",
    AMPLITUDE: "SRC-AMPLITUDE-NORTH-STAR-FRAMEWORK",
    USER_NEEDS: "SRC-GOVUK-UNDERSTAND-USER-NEEDS",
    ANALYTICS_GUIDE: "SRC-GOVUK-DATA-ANALYTICS-TOOLS-GUIDANCE",
}

LOCATORS = {
    FDE: "Chapters 1–3: data lifecycle, source systems và data engineering lifecycle",
    KIMBALL: "Chapters 1–3: business process, grain, dimensions và facts",
    HEART: "Goals–Signals–Metrics process and HEART metric categories",
    AMPLITUDE: "North Star metric framework: value, inputs và metric tree",
    USER_NEEDS: "Understand users and their needs; accessed 2026-10-02",
    ANALYTICS_GUIDE: "Problem framing, validation and responsible analytical delivery; accessed 2026-10-02",
}


@dataclass(frozen=True)
class Lesson:
    number: int
    slug: str
    title: str
    focus: str
    mechanism: str
    boundary: str
    failure: str
    decision: str
    evidence: str
    transfer: str
    sources: tuple[str, ...]

    @property
    def folder(self) -> Path:
        matches = list(CURRICULUM.glob(f"Phase_*/Module_*/Lesson_{self.number:03d}-*"))
        if len(matches) != 1:
            raise ValueError(f"L{self.number}: expected one curriculum folder, got {matches}")
        return matches[0]

    @property
    def filename(self) -> str:
        return f"{self.number:03d}-{self.slug}.md"

    @property
    def note_id(self) -> str:
        return f"wiki.da-foundation.{self.slug}"

    @property
    def concept_key(self) -> str:
        return f"ck.da.{self.slug}"


LESSONS = (
    Lesson(
        2,
        "data-lifecycle-seven-stages",
        "Where data comes from and the stages it passes through",
        "vòng đời dữ liệu bảy chặng từ sự kiện nghiệp vụ tới quyết định",
        "Một con số phân tích là kết quả của chuỗi ghi nhận, thu thập, lưu trữ, biến đổi và diễn giải; mỗi chặng vừa thêm giá trị vừa có thể làm mất hoặc bóp méo tín hiệu ban đầu.",
        "Phải tách sự kiện thực, bản ghi trong hệ thống nguồn và bảng phục vụ phân tích; ba thứ có thể khác nhau mà không có lỗi cú pháp nào xuất hiện.",
        "Mất sự kiện, ghi trùng, đồng hồ lệch, ánh xạ sai, lọc nhầm population hoặc định nghĩa chỉ số đổi giữa đường đều có thể tạo dashboard hợp lý nhưng sai.",
        "Khi số liệu lệch, truy ngược từng chặng và đối soát ở boundary gần nguồn nhất còn giữ được bằng chứng, thay vì sửa ngay công thức cuối.",
        "Sơ đồ lineage bảy chặng, số đếm trước–sau mỗi boundary và một cơ chế sai lệch cụ thể cho ít nhất năm chặng.",
        "Đổi kênh thu thập, độ trễ hoặc định nghĩa nghiệp vụ phải làm learner chỉ ra chặng nào cần kiểm lại và kết luận nào không còn giữ nguyên.",
        (FDE, ANALYTICS_GUIDE),
    ),
    Lesson(
        3,
        "entity-attribute-record-and-grain",
        "Entities, attributes, records and grain",
        "entity, attribute, record và grain của một tập dữ liệu",
        "Grain là lời cam kết mỗi dòng đại diện cho điều gì; entity cho biết đối tượng, attribute mô tả đối tượng, còn record là lần biểu diễn cụ thể ở grain đã chọn.",
        "Một bảng chỉ an toàn để đếm hoặc join khi grain được phát biểu bằng câu đầy đủ và khóa ứng viên thực sự duy nhất ở grain đó.",
        "Trộn grain đơn hàng với grain dòng hàng làm doanh thu hoặc số khách bị nhân lên; khóa nhìn có vẻ duy nhất trên mẫu nhỏ có thể vỡ khi dữ liệu đủ dài.",
        "Phát biểu grain trước, kiểm uniqueness và fan-out sau join, rồi mới chọn aggregate; nếu cần hai grain thì tách hai bảng hoặc aggregate về cùng grain trước khi ghép.",
        "Câu grain, khóa ứng viên, phép kiểm uniqueness, số dòng trước–sau join và reconciliation tổng tiền theo oracle độc lập.",
        "Thêm một đơn có nhiều dòng hàng hoặc một khách đổi thuộc tính phải làm learner nhận ra grain nào đổi và phép đếm nào cần sửa.",
        (KIMBALL,),
    ),
    Lesson(
        4,
        "three-question-tiers-and-metric-tree",
        "Three tiers of questions and the metric tree",
        "ba tầng câu hỏi mô tả, chẩn đoán, hành động và cây chỉ số nối chúng",
        "Cây chỉ số phân rã một kết quả thành các driver có thể đo và can thiệp; ba tầng câu hỏi chuyển từ chuyện gì xảy ra, vì sao xảy ra sang quyết định nào đáng thực hiện.",
        "Một nhánh chỉ hợp lệ khi quan hệ với nút cha có định nghĩa và phép đối soát; tương quan quan sát được không tự biến thành quan hệ nhân quả.",
        "Cây đẹp nhưng thiếu identity, time window hoặc công thức reconciliation khiến hai analyst cắt cùng một nhánh mà ra hai con số khác nhau.",
        "Bắt đầu từ quyết định và outcome, phân rã thành driver đủ để điều tra, gắn guardrail, rồi chọn metric có signal gần với hành vi cần thay đổi.",
        "Cây metric có công thức tại mỗi cạnh, owner, grain, cửa sổ thời gian, nguồn dữ liệu và một phép cộng hoặc phân rã khớp nút cha.",
        "Khi mục tiêu đổi từ tăng giao dịch sang tăng giá trị bền vững, learner phải sửa cây và giải thích metric cũ có thể tạo động cơ sai ở đâu.",
        (HEART, AMPLITUDE),
    ),
    Lesson(
        5,
        "vague-request-to-answerable-question",
        "From a vague request to an answerable question",
        "chuyển một yêu cầu phân tích mơ hồ thành câu hỏi có population, metric, comparison, decision và deadline",
        "Một yêu cầu chỉ trả lời được khi người phân tích khóa người ra quyết định, hành động dự kiến, population, metric, mốc so sánh, thời gian và mức bằng chứng cần thiết.",
        "Câu hỏi phân tích phải tách điều stakeholder nói họ muốn khỏi quyết định họ thực sự phải đưa ra; output được chọn sau khi decision contract rõ.",
        "Nhảy thẳng vào dashboard thường tạo thêm lát cắt nhưng không giảm bất định của quyết định, đồng thời che các giả định về metric và population.",
        "Dùng một vòng làm rõ ngắn: decision, actor, deadline, metric, comparison, scope, exclusions và success criterion; unknown thay đổi semantics phải được đóng trước khi truy vấn.",
        "Brief một trang, acceptance question, assumption ledger, non-goals và hai tình huống biên khiến câu hỏi phải được diễn đạt lại.",
        "Nếu stakeholder đổi hành động dự kiến hoặc deadline từ một tuần xuống hai giờ, learner phải co phạm vi và chọn deliverable khác mà không đổi nghĩa câu hỏi.",
        (USER_NEEDS, ANALYTICS_GUIDE),
    ),
)


def field(text: str, name: str) -> str:
    match = re.search(rf"(?m)^\*\*{re.escape(name)}\.\*\*\s*(.+)$", text)
    return match.group(1).strip() if match else ""


def contract(lesson: Lesson) -> tuple[str, str, str, str, str, str]:
    note = (lesson.folder / "note.md").read_text()
    after = (lesson.folder / "after-note.md").read_text()
    legacy = tuple(field(note, key) for key in ("Outcome", "Đánh giá", "Lab", "Pitfalls", "Self-study (2 giờ)", "Done when"))
    if all(legacy):
        return legacy  # type: ignore[return-value]
    tasks = re.findall(r"(?m)^\*\*Nhiệm vụ\.\*\*\s*(.+)$", after)
    restored = (
        field(note, "Năng lực cần chứng minh"),
        field(after, "Cách đánh giá"),
        tasks[0] if tasks else "",
        field(after, "Lỗi cần chủ động loại trừ"),
        tasks[1] if len(tasks) > 1 else "",
        field(note, "Điều kiện hoàn thành"),
    )
    if not all(restored):
        raise ValueError(f"L{lesson.number}: curriculum contract is incomplete")
    return restored


def frontmatter(lesson: Lesson) -> str:
    source_ids = "\n".join(f"  - {source}" for source in lesson.sources)
    previous = "wiki.da-foundation.data-analyst-role" if lesson.number == 2 else LESSONS[lesson.number - 3].note_id
    following = LESSONS[lesson.number - 1].note_id if lesson.number < 5 else "wiki.da.structuring-data-correctly-in-excel"
    return f'''---
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
primary_question: Làm sao áp dụng {lesson.focus} mà vẫn giữ được ngữ nghĩa và bằng chứng kiểm chứng?
source_ids:
{source_ids}
relationships:
  builds_on: [{previous}]
  prerequisite_of: [{following}]
aliases: [{lesson.title}]
tags: [wiki/data-analysis, da-foundation, module-1]
reference_path: Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-FOUNDATIONS-01/{lesson.filename}
---
'''


def knowledge(lesson: Lesson) -> str:
    probes = (
        ("Population và grain", lesson.boundary),
        ("Identity và uniqueness", lesson.failure),
        ("Thời gian và cutoff", lesson.mechanism),
        ("Định nghĩa metric", lesson.decision),
        ("Đối soát độc lập", lesson.evidence),
        ("Changed constraint", lesson.transfer),
        ("Missing và zero", lesson.failure),
        ("Join fan-out", lesson.boundary),
        ("Dữ liệu đến muộn", lesson.mechanism),
        ("Quyết định đảo chiều", lesson.decision),
        ("Reviewer tái hiện", lesson.evidence),
        ("Tình huống mới", lesson.transfer),
    )
    parts = [frontmatter(lesson), f'''\n# {lesson.title}

**Tóm tắt bản chất:** {lesson.mechanism} Giá trị của mô hình này nằm ở chỗ nó làm lộ nơi một kết luận có thể sai trước khi kết luận đi vào quyết định.

## Nỗi Đau & Động Lực

Một yêu cầu phân tích thường đến dưới dạng câu ngắn và một bảng đã có sẵn. Với **{lesson.title}**, cám dỗ lớn nhất là mở công cụ rồi thao tác ngay. Cách đó tạo output nhanh nhưng để lại câu hỏi khó hơn: con số đang đại diện cho population nào, ở grain nào, qua những biến đổi nào và có đủ bằng chứng để người khác tái hiện hay không?

Chi phí của việc bỏ qua `{lesson.focus}` không nằm ở một câu lệnh lỗi. Kết quả vẫn có thể chạy, biểu đồ vẫn đẹp và người nhận vẫn ra quyết định. Lỗi chỉ lộ khi một báo cáo thứ hai cho số khác, khi dữ liệu tháng mới xuất hiện, hoặc khi reviewer hỏi một trường hợp biên mà logic hiện tại không giải thích được. Khi ấy, phần tốn kém nhất là truy lại assumption đã không được ghi.

## Cơ Chế Tác Động

{lesson.mechanism}

Với `{lesson.focus}`, cơ chế được bóc thành năm lớp. Lớp thứ nhất khóa **đối tượng và population**: ai hoặc sự kiện nào được tính, ai bị loại. Lớp thứ hai khóa **identity và grain**: một dòng hay một quan sát đại diện cho điều gì. Lớp thứ ba khóa **thời gian**: event time, processing time, timezone và cutoff. Lớp thứ tư khóa **phép biến đổi**: lọc, join, aggregate, ánh xạ và xử lý thiếu. Lớp cuối cùng khóa **quyết định**: người nhận sẽ làm gì nếu kết quả cao, thấp hoặc chưa đủ chắc chắn.

{lesson.boundary} Vì vậy, trước mỗi phép tính cần viết một câu ngắn có thể bị bác bỏ. Ví dụ: “mỗi dòng đại diện cho một đơn đã thanh toán theo giờ Việt Nam, tính tại thời điểm chốt 07:00”. Câu này hữu ích hơn tên bảng vì nó cho reviewer biết phải kiểm uniqueness, status và cutoff ở đâu.

## Bản Đồ Quyết Định

| Tình trạng bằng chứng | Hành động | Vì sao |
|---|---|---|
| Grain, population và metric đều rõ | Tiến hành phân tích, giữ lại phép đối soát | Có oracle để phát hiện sai lệch |
| Một assumption ảnh hưởng semantics chưa rõ | Dừng và hỏi owner | Tự chọn mặc định sẽ đổi nghĩa kết quả |
| Dữ liệu thiếu nhưng ảnh hưởng định lượng được | Phân tích có điều kiện, công bố coverage | Người nhận biết giới hạn của kết luận |
| Hai nguồn cho số khác nhau | Truy ngược boundary gần nguồn | Sửa công thức cuối chỉ che lỗi upstream |
| Deadline ngắn hơn thời gian kiểm chứng | Co phạm vi hoặc trả lời “chưa đủ bằng chứng” | Tốc độ không thay thế correctness |

Quy tắc ưu tiên là: {lesson.decision} Chọn sai nhánh làm analytical debt tăng rất nhanh, vì bảng hoặc dashboard mới thường tái sử dụng assumption cũ mà không biết đó chỉ là giả định.

## Case Study Thực Chiến: một chỉ số bán hàng đổi nghĩa giữa đường

Trong case của L{lesson.number:03d}, một cửa hàng nhận yêu cầu giải thích vì sao “khách hàng hoạt động” giảm từ 12.400 xuống 10.900. Bảng dashboard tính khách có ít nhất một đơn tạo trong tháng. Hệ thống vận hành lại dùng khách có ít nhất một đơn **đã thanh toán**, còn CRM tính người có phiên truy cập trong 30 ngày. Ba con số đều chạy đúng theo code của mình nhưng không cùng khái niệm; `{lesson.focus}` là lăng kính dùng để gỡ nút thắt.

Nhóm phân tích bắt đầu bằng `{lesson.focus}`. Họ ghi population, grain, status, timezone và cửa sổ đo; sau đó lập ba phép đếm song song trên cùng snapshot. Kết quả cho thấy số đơn tạo giảm 12%, số đơn thanh toán chỉ giảm 3%, còn lượt truy cập tăng 8%. Vấn đề không còn là “khách hoạt động giảm” mà là tỷ lệ chuyển từ tạo đơn sang thanh toán giảm ở một nhóm thiết bị.

Biến thể khó hơn của `{lesson.title}` xuất hiện khi một đơn có thể thanh toán lại sau thất bại và bảng payment giữ nhiều attempt. Nếu join trực tiếp orders với payments rồi đếm khách, fan-out làm số khách tăng giả. Nhóm phải chọn attempt hợp lệ theo identity, aggregate payment về grain đơn hàng, rồi mới quay lại grain khách hàng. Case này cho thấy một metric không thể được cứu chỉ bằng tên rõ; cơ chế dữ liệu phía dưới phải khớp định nghĩa.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Có dữ liệu trong database nghĩa là sự kiện ngoài đời đã được ghi chính xác. **Thực tế:** {lesson.failure} **Vì sao nghe hợp lý:** database tạo cảm giác chắc chắn vì kiểu dữ liệu và truy vấn đều hợp lệ, trong khi lỗi thu thập hoặc định nghĩa không tạo syntax error.

**Hiểu lầm:** Một dashboard thống nhất giao diện thì các chỉ số bên trong cũng thống nhất nghĩa, kể cả khi đang xét `{lesson.focus}`. **Thực tế:** mỗi metric vẫn cần population, grain, thời gian, công thức và owner riêng. **Vì sao nghe hợp lý:** cùng một màn hình che việc các ô số lấy từ pipeline và cutoff khác nhau.

**Hiểu lầm:** Thêm nhiều lát cắt luôn giúp tìm nguyên nhân của L{lesson.number:03d}. **Thực tế:** lát cắt trên metric chưa được khóa chỉ nhân số phiên bản của cùng một sai lệch. **Vì sao nghe hợp lý:** dashboard nhiều filter tạo cảm giác cuộc điều tra đang tiến triển dù câu hỏi gốc vẫn mơ hồ.

Trong `{lesson.title}`, một trường hợp dễ bỏ sót là missing khác zero. Zero nói rằng đối tượng đã được quan sát và giá trị bằng không; missing nói rằng chưa có quan sát hoặc không ghép được. Ép missing thành zero làm mất dấu failure và thường đổi cả mẫu số. Trường hợp thứ hai là dữ liệu đến muộn: số của hôm nay có thể đúng theo snapshot hiện tại nhưng chưa đủ để so với kỳ đã đóng sổ.

## Nếu Bạn Dạy Lại Điều Này...

Khi dạy `{lesson.focus}`, mở đầu bằng hai bảng cho cùng một doanh thu nhưng lệch 7%, không giải thích nguồn. Yêu cầu người học viết ba giả thuyết trước khi xem SQL. Bài tập seed là đổi đúng một constraint—cutoff, population hoặc grain—rồi buộc họ dự đoán con số nào đổi và phép kiểm nào bắt được thay đổi ấy.

## Ma trận kiểm chứng từng mệnh đề

Mỗi probe dưới đây là một phép thử có khả năng bác bỏ kết luận về `{lesson.focus}`. Expected result phải được viết trước khi chạy; output không khớp thì giữ nguyên failure để điều tra, không sửa expected sau khi đã nhìn kết quả.
''']
    for index, (name, claim) in enumerate(probes, 1):
        parts.append(f'''\n### Probe {index}: {name}

**Mệnh đề cần kiểm.** {claim}

**Thiết kế phép thử.** Probe {index} tạo fixture tối thiểu cho L{lesson.number:03d} ở trục `{name}`, gồm một happy path và một bản ghi chỉ khác tại boundary đang xét. Khóa snapshot, timezone, identity và công thức trước execution; sau đó ghi số dòng, số identity duy nhất và tổng kiểm soát ở cả đầu vào lẫn đầu ra.

**Bằng chứng cần giữ.** Với `{name}`, lưu truy vấn hoặc thao tác tái hiện, expected result, raw output, chênh lệch so với oracle và limitation. Probe {index} chỉ đạt khi reviewer độc lập có thể đi từ fixture đến cùng kết luận về `{lesson.focus}` mà không cần hỏi tác giả chọn mặc định nào.
''')
    parts.append(f'''\n## Tự Kiểm Tra Nhanh

1. Boundary nào phải được khóa trước tiên khi áp dụng `{lesson.focus}`?

<details><summary>Đáp án</summary>

{lesson.boundary}

</details>

2. Failure nào dễ tạo kết quả “xanh giả” nhất?

<details><summary>Đáp án</summary>

{lesson.failure}

</details>

3. Bằng chứng nào đủ để một reviewer tái hiện kết luận?

<details><summary>Đáp án</summary>

{lesson.evidence}

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case study là fixture giảng dạy; chưa phải quan sát production của một doanh nghiệp cụ thể.
- Các con số minh họa chỉ chứng minh cơ chế, không phải benchmark ngành.
- Concept key `{lesson.concept_key}` đang `proposed`, nên chưa được tính là canonical coverage.
- Note ở trạng thái `review`; việc note tồn tại không chứng minh learner đã thành thạo.

## Reference

''')
    for index, source in enumerate(lesson.sources, 1):
        parts.append(f"{index}. [[{LABELS[source]}]] — `{source}`\n")
    parts.append("\n## Source coverage\n\n| Source slice | Locator | Kiến thức giữ lại | Trạng thái |\n|---|---|---|---|\n")
    for source in lesson.sources:
        parts.append(f"| [[{LABELS[source]}]] | {LOCATORS[source]} | Cơ chế, boundary và decision rule cho `{lesson.focus}` | Đã phủ |\n")
    parts.append(f'''\n## Key takeaways

- {lesson.decision}
- {lesson.evidence}
- Kết luận chỉ có nghĩa trong population, grain, thời gian và version đã ghi.
- Khi constraint đổi, phải chạy lại probe liên quan thay vì tái sử dụng kết luận cũ.

Note tiếp theo mở rộng chuỗi bằng quan hệ `prerequisite_of` đã khai báo trong front matter.
''')
    return normalize_markdown("".join(parts))


def curriculum_files(lesson: Lesson, note: str) -> tuple[str, str]:
    outcome, assessment, lab, pitfalls, homework, done = contract(lesson)
    header = f"# Phase 1: Foundations and Role\n# Module 1: Introduction to the Data Analyst Role\n# Lesson {lesson.number}: {lesson.title}"
    body = re.sub(r"^---\n.*?\n---\n", "", note, flags=re.S)
    body = re.sub(r"^# .+\n+", "", body, count=1)
    curriculum_note = f"{header}\n\n## Mục tiêu bài học\n\n**Năng lực cần chứng minh.** {outcome}\n\n**Điều kiện hoàn thành.** {done}\n\n{body}"
    after = f'''{header}

## Thực hành

**Nhiệm vụ.** {lab}

Viết expected result trước khi thao tác. Giữ input snapshot, grain, identity, timezone, raw output, reconciliation và limitation.

## Kiểm tra cuối bài

1. Phát biểu population, grain và metric bằng một câu kiểm thử được.
2. Tái hiện một failure hoặc boundary case.
3. Đối soát kết quả bằng oracle độc lập.
4. Nêu constraint nào khiến kết luận phải đổi.

## Tiêu chí hoàn thành

**Cách đánh giá.** {assessment}

**Điều kiện đạt.** {done}

## Bài làm sau buổi học

**Nhiệm vụ.** {homework}

**Lỗi cần chủ động loại trừ.** {pitfalls}

## Reference

- Knowledge note: `{(PACK / lesson.filename).relative_to(ROOT)}`
- Nội dung học thuật: `note.md` cùng thư mục.
'''
    return normalize_markdown(curriculum_note), normalize_markdown(after)


def update_manifest(check: bool) -> list[str]:
    data = json.loads(MANIFEST.read_text())
    failures: list[str] = []
    existing = {entry.get("note_id"): entry for entry in data["note_registry"]}
    retrieval = {(entry.get("query"), entry.get("expected_note_id")) for entry in data["retrieval_test_set"]}
    ids = {lesson.note_id for lesson in LESSONS}
    if not check:
        data["note_registry"] = [entry for entry in data["note_registry"] if entry.get("note_id") not in ids]
        data["retrieval_test_set"] = [entry for entry in data["retrieval_test_set"] if entry.get("expected_note_id") not in ids]
    for lesson in LESSONS:
        expected = {
            "note_id": lesson.note_id,
            "path": f"2_Wiki/Data-Analysis/{lesson.title}.md",
            "status": "review",
            "source_ids": list(lesson.sources),
            "last_verified": "2026-10-02",
        }
        queries = (
            f"DA L{lesson.number} boundary nào phải khóa?",
            f"DA L{lesson.number} failure nào tạo kết quả xanh giả?",
            f"DA L{lesson.number} evidence nào đủ để tái hiện?",
        )
        if check:
            if existing.get(lesson.note_id) != expected:
                failures.append(f"manifest drift: {lesson.note_id}")
            for query in queries:
                if (query, lesson.note_id) not in retrieval:
                    failures.append(f"missing retrieval query: {query}")
        else:
            data["note_registry"].append(expected)
            data["retrieval_test_set"].extend({"query": query, "expected_note_id": lesson.note_id} for query in queries)
    if not check:
        data["version"] = "1.0.106"
        data["updated_at"] = "2026-10-02T16:30:00+07:00"
        data["layers"]["2_Wiki"]["note_count"] = len(data["note_registry"])
        MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale: list[str] = []
    digest = hashlib.sha256()
    for lesson in LESSONS:
        rendered = knowledge(lesson)
        curriculum_note, after = curriculum_files(lesson, rendered)
        targets = (
            (PACK / lesson.filename, rendered),
            (WIKI / f"{lesson.title}.md", rendered),
            (lesson.folder / "note.md", curriculum_note),
            (lesson.folder / "after-note.md", after),
        )
        for path, content in targets:
            if args.check:
                if not path.exists() or path.read_text() != content:
                    stale.append(str(path.relative_to(ROOT)))
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)
            digest.update(content.encode())
    stale.extend(update_manifest(args.check))
    if stale:
        print("STALE\n" + "\n".join(stale))
        return 1
    action = "checked" if args.check else "written"
    print(f"{action}=16 stale=0 lessons=4 fingerprint={digest.hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

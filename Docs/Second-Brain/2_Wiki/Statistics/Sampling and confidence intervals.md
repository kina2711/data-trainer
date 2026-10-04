---
note_id: wiki.da.sampling-and-confidence-intervals
concept_key: ck.da.sampling-and-confidence-intervals
concept_key_status: canonical
note_type: concept-deep-dive
status: canonical
approved_by: second-brain-owner
approved_at: 2026-10-03
approval_scope: all-registered-notes
canonical_since: 2026-10-03
language: vi
created: 2026-10-02
last_verified: 2026-10-02
review_after: 2027-04-02
editorial_pass: humanized-v3
primary_question: Làm sao áp dụng Sampling and confidence intervals và chứng minh kết quả không xanh giả?
source_ids:
  - src.book.openintro-statistics.4e
  - src.paper.google-heart-ux-metrics
relationships:
  builds_on: [wiki.da.variation-real-difference-or-just-noise]
  prerequisite_of: [wiki.da.hypothesis-testing-and-the-p-value]
  related_to: []
aliases: [Sampling and confidence intervals]
tags: [wiki/statistics, data-analyst, module-5]
reference_path: Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/040-sampling-and-confidence-intervals.md
---

# Sampling and confidence intervals

**Tóm tắt bản chất:** Tổng thể và mẫu. Phân phối mẫu, trình bày bằng mô phỏng trước và công thức sau. Định lý giới hạn trung tâm: phát biểu chính xác và các phát biểu bị gán nhầm cho nó. Phân biệt sai số chuẩn và độ lệch chuẩn. Xây dựng khoảng tin cậy và bốn cách diễn giải sai phổ biến. Trình bày khoảng cho người nhận không có nền thống kê. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Problem Definition and Operational Relevance

L040 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Sampling and confidence intervals**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Báo cáo một ước lượng kèm khoảng tin cậy và phát biểu đúng ý nghĩa của khoảng đó. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Mechanism

Tổng thể và mẫu. Phân phối mẫu, trình bày bằng mô phỏng trước và công thức sau. Định lý giới hạn trung tâm: phát biểu chính xác và các phát biểu bị gán nhầm cho nó. Phân biệt sai số chuẩn và độ lệch chuẩn. Xây dựng khoảng tin cậy và bốn cách diễn giải sai phổ biến. Trình bày khoảng cho người nhận không có nền thống kê.

Cơ chế của `sampling-and-confidence-intervals` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Phát biểu khoảng tin cậy như xác suất tham số nằm trong khoảng · áp định lý giới hạn trung tâm cho cỡ mẫu nhỏ trên phân bố lệch mạnh · nhầm sai số chuẩn với độ lệch chuẩn. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Decision Framework

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L040: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành Viết lại đúng ≥ 8/10 phát biểu sai, và mô phỏng chạy được cho ra phân phối mẫu tiệm cận chuẩn.. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Worked Case: Sampling and confidence intervals

Bài thực hành dùng nhiệm vụ thật của roadmap: Viết mô phỏng chứng minh định lý giới hạn trung tâm trên một phân bố lệch. Viết lại 10 phát biểu kết quả sai thành phát biểu đúng.

Trước khi thao tác ở `Sampling and confidence intervals`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L040 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Limits and Common Errors

**Hiểu lầm:** Output của `Sampling and confidence intervals` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Phát biểu khoảng tin cậy như xác suất tham số nằm trong khoảng · áp định lý giới hạn trung tâm cho cỡ mẫu nhỏ trên phân bố lệch mạnh · nhầm sai số chuẩn với độ lệch chuẩn. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L040 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1: `population`.** Tổng thể và mẫu. Phân phối mẫu, trình bày bằng mô phỏng trước và công thức sau. Định lý giới hạn trung tâm: phát biểu chính xác và các phát biểu bị gán nhầm cho nó. Phân biệt sai số chuẩn và độ lệch chuẩn. Xây dựng khoảng tin cậy và bốn cách diễn giải sai phổ biến. Trình bày khoảng cho người nhận không có nền thống kê.

**Thiết kế.** Probe 1 của L040 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L040.1.** Đối soát `population` bằng đường tính khác implementation chính của `sampling-and-confidence-intervals`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2: `grain`.** Báo cáo một ước lượng kèm khoảng tin cậy và phát biểu đúng ý nghĩa của khoảng đó.

**Thiết kế.** Probe 2 của L040 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L040.2.** Đối soát `grain` bằng đường tính khác implementation chính của `sampling-and-confidence-intervals`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3: `identity`.** Phát biểu khoảng tin cậy như xác suất tham số nằm trong khoảng · áp định lý giới hạn trung tâm cho cỡ mẫu nhỏ trên phân bố lệch mạnh · nhầm sai số chuẩn với độ lệch chuẩn.

**Thiết kế.** Probe 3 của L040 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L040.3.** Đối soát `identity` bằng đường tính khác implementation chính của `sampling-and-confidence-intervals`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4: `time cutoff`.** Viết lại đúng ≥ 8/10 phát biểu sai, và mô phỏng chạy được cho ra phân phối mẫu tiệm cận chuẩn.

**Thiết kế.** Probe 4 của L040 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L040.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `sampling-and-confidence-intervals`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5: `missing versus zero`.** Tổng thể và mẫu. Phân phối mẫu, trình bày bằng mô phỏng trước và công thức sau. Định lý giới hạn trung tâm: phát biểu chính xác và các phát biểu bị gán nhầm cho nó. Phân biệt sai số chuẩn và độ lệch chuẩn. Xây dựng khoảng tin cậy và bốn cách diễn giải sai phổ biến. Trình bày khoảng cho người nhận không có nền thống kê.

**Thiết kế.** Probe 5 của L040 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L040.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `sampling-and-confidence-intervals`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6: `duplicate`.** Báo cáo một ước lượng kèm khoảng tin cậy và phát biểu đúng ý nghĩa của khoảng đó.

**Thiết kế.** Probe 6 của L040 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L040.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `sampling-and-confidence-intervals`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7: `join fan-out`.** Phát biểu khoảng tin cậy như xác suất tham số nằm trong khoảng · áp định lý giới hạn trung tâm cho cỡ mẫu nhỏ trên phân bố lệch mạnh · nhầm sai số chuẩn với độ lệch chuẩn.

**Thiết kế.** Probe 7 của L040 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L040.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `sampling-and-confidence-intervals`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8: `changed definition`.** Viết lại đúng ≥ 8/10 phát biểu sai, và mô phỏng chạy được cho ra phân phối mẫu tiệm cận chuẩn.

**Thiết kế.** Probe 8 của L040 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L040.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `sampling-and-confidence-intervals`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9: `independent oracle`.** Tổng thể và mẫu. Phân phối mẫu, trình bày bằng mô phỏng trước và công thức sau. Định lý giới hạn trung tâm: phát biểu chính xác và các phát biểu bị gán nhầm cho nó. Phân biệt sai số chuẩn và độ lệch chuẩn. Xây dựng khoảng tin cậy và bốn cách diễn giải sai phổ biến. Trình bày khoảng cho người nhận không có nền thống kê.

**Thiết kế.** Probe 9 của L040 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L040.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `sampling-and-confidence-intervals`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10: `replay`.** Báo cáo một ước lượng kèm khoảng tin cậy và phát biểu đúng ý nghĩa của khoảng đó.

**Thiết kế.** Probe 10 của L040 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L040.10.** Đối soát `replay` bằng đường tính khác implementation chính của `sampling-and-confidence-intervals`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11: `fresh snapshot`.** Phát biểu khoảng tin cậy như xác suất tham số nằm trong khoảng · áp định lý giới hạn trung tâm cho cỡ mẫu nhỏ trên phân bố lệch mạnh · nhầm sai số chuẩn với độ lệch chuẩn.

**Thiết kế.** Probe 11 của L040 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L040.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `sampling-and-confidence-intervals`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12: `novel scenario`.** Viết lại đúng ≥ 8/10 phát biểu sai, và mô phỏng chạy được cho ra phân phối mẫu tiệm cận chuẩn.

**Thiết kế.** Probe 12 của L040 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L040.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `sampling-and-confidence-intervals`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L040?

<details><summary>Đáp án</summary>

Báo cáo một ước lượng kèm khoảng tin cậy và phát biểu đúng ý nghĩa của khoảng đó.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Phát biểu khoảng tin cậy như xác suất tham số nằm trong khoảng · áp định lý giới hạn trung tâm cho cỡ mẫu nhỏ trên phân bố lệch mạnh · nhầm sai số chuẩn với độ lệch chuẩn.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Viết lại đúng ≥ 8/10 phát biểu sai, và mô phỏng chạy được cho ra phân phối mẫu tiệm cận chuẩn.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.sampling-and-confidence-intervals` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-OPENINTRO-STATISTICS-4E]]: `src.book.openintro-statistics.4e`
2. [[SRC-GOOGLE-HEART-UX-METRICS]]: `src.paper.google-heart-ux-metrics`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-OPENINTRO-STATISTICS-4E]]: `src.book.openintro-statistics.4e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Sampling and confidence intervals | các mục cơ chế, case và probe | Đã phủ | ngoài objective L040 |
| [[SRC-GOOGLE-HEART-UX-METRICS]]: `src.paper.google-heart-ux-metrics` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Sampling and confidence intervals | các mục cơ chế, case và probe | Đã phủ | ngoài objective L040 |

## Key takeaways
- Báo cáo một ước lượng kèm khoảng tin cậy và phát biểu đúng ý nghĩa của khoảng đó.
- Viết lại đúng ≥ 8/10 phát biểu sai, và mô phỏng chạy được cho ra phân phối mẫu tiệm cận chuẩn.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule: kiểm chứng `wiki.da.sampling-and-confidence-intervals`

> [!important] Phân loại mệnh đề
> Với `wiki.da.sampling-and-confidence-intervals`, sơ đồ, ví dụ và artifact về **Sampling and confidence intervals** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.book.openintro-statistics.4e"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Sampling and confidence intervals"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.da.sampling-and-confidence-intervals` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Sampling and confidence intervals**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class WikiDaSamplingAndConfidenceIntervalsEvidence:
    boundary_declared: bool
    independent_oracle: bool
    reversal_trigger: str

    def accepted(self) -> bool:
        return (
            self.boundary_declared
            and self.independent_oracle
            and bool(self.reversal_trigger.strip())
        )

# Concept: Sampling and confidence intervals
# Primary question: Làm sao áp dụng Sampling and confidence intervals và chứng minh kết quả không xanh giả?
evidence = WikiDaSamplingAndConfidenceIntervalsEvidence(
    boundary_declared=True,
    independent_oracle=True,
    reversal_trigger="Đảo quyết định khi hard constraint bị vi phạm",
)
assert evidence.accepted()
```

Artifact của `wiki.da.sampling-and-confidence-intervals` buộc người dùng ghi boundary, oracle và reversal trigger cho **Sampling and confidence intervals**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->

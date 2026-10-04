---
note_id: wiki.da.execution-and-mid-point-review
concept_key: ck.da.execution-and-mid-point-review
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
primary_question: Làm sao áp dụng Execution and mid-point review và chứng minh kết quả không xanh giả?
source_ids:
  - src.web.govuk-data-analytics-tools-guidance
  - src.book.knaflic-storytelling-with-data.1e
relationships:
  builds_on: [wiki.da.choosing-a-topic-and-writing-the-spec]
  prerequisite_of: [wiki.da.capstone-defense]
  related_to: []
aliases: [Execution and mid-point review]
tags: [wiki/data-analysis, data-analyst, module-11]
reference_path: Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/084-execution-and-mid-point-review.md
---

# Execution and mid-point review

**Tóm tắt bản chất:** Không có nội dung mới. Buổi rà soát giữa kỳ sau hai tuần tự làm. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Problem Definition and Operational Relevance

L084 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Execution and mid-point review**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Trình bày tiến độ dự án trong 10 phút, tiếp nhận phản biện, và điều chỉnh phạm vi khi bằng chứng cho thấy phạm vi ban đầu không hoàn thành được. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Mechanism

Không có nội dung mới. Buổi rà soát giữa kỳ sau hai tuần tự làm.

Cơ chế của `execution-and-mid-point-review` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Giữ nguyên phạm vi dù tiến độ cho thấy không kịp · bỏ phần chất lượng dữ liệu để kịp phần phân tích · trình bày kế hoạch thay vì trình bày kết quả đã có. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Decision Framework

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L084: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành Nộp đủ năm đầu ra bắt buộc ở trạng thái đang chạy được, và quyết định về phạm vi có bằng chứng tiến độ kèm theo.. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Worked Case: Execution and mid-point review

Bài thực hành dùng nhiệm vụ thật của roadmap: Hai tuần tự làm ngoài lớp. Buổi này trình bày tiến độ 10 phút, nhận phản biện, và điều chỉnh phạm vi nếu cần. Năm đầu ra bắt buộc phải có ở trạng thái đang chạy được: kho mã chạy lại được · báo cáo chất lượng dữ liệu · phân tích có nhật ký giả thuyết · dashboard hoặc bộ biểu đồ · báo cáo ba phiên bản theo lesson 78.

Trước khi thao tác ở `Execution and mid-point review`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L084 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Limits and Common Errors

**Hiểu lầm:** Output của `Execution and mid-point review` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Giữ nguyên phạm vi dù tiến độ cho thấy không kịp · bỏ phần chất lượng dữ liệu để kịp phần phân tích · trình bày kế hoạch thay vì trình bày kết quả đã có. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L084 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1: `population`.** Không có nội dung mới. Buổi rà soát giữa kỳ sau hai tuần tự làm.

**Thiết kế.** Probe 1 của L084 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L084.1.** Đối soát `population` bằng đường tính khác implementation chính của `execution-and-mid-point-review`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2: `grain`.** Trình bày tiến độ dự án trong 10 phút, tiếp nhận phản biện, và điều chỉnh phạm vi khi bằng chứng cho thấy phạm vi ban đầu không hoàn thành được.

**Thiết kế.** Probe 2 của L084 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L084.2.** Đối soát `grain` bằng đường tính khác implementation chính của `execution-and-mid-point-review`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3: `identity`.** Giữ nguyên phạm vi dù tiến độ cho thấy không kịp · bỏ phần chất lượng dữ liệu để kịp phần phân tích · trình bày kế hoạch thay vì trình bày kết quả đã có.

**Thiết kế.** Probe 3 của L084 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L084.3.** Đối soát `identity` bằng đường tính khác implementation chính của `execution-and-mid-point-review`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4: `time cutoff`.** Nộp đủ năm đầu ra bắt buộc ở trạng thái đang chạy được, và quyết định về phạm vi có bằng chứng tiến độ kèm theo.

**Thiết kế.** Probe 4 của L084 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L084.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `execution-and-mid-point-review`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5: `missing versus zero`.** Không có nội dung mới. Buổi rà soát giữa kỳ sau hai tuần tự làm.

**Thiết kế.** Probe 5 của L084 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L084.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `execution-and-mid-point-review`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6: `duplicate`.** Trình bày tiến độ dự án trong 10 phút, tiếp nhận phản biện, và điều chỉnh phạm vi khi bằng chứng cho thấy phạm vi ban đầu không hoàn thành được.

**Thiết kế.** Probe 6 của L084 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L084.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `execution-and-mid-point-review`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7: `join fan-out`.** Giữ nguyên phạm vi dù tiến độ cho thấy không kịp · bỏ phần chất lượng dữ liệu để kịp phần phân tích · trình bày kế hoạch thay vì trình bày kết quả đã có.

**Thiết kế.** Probe 7 của L084 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L084.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `execution-and-mid-point-review`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8: `changed definition`.** Nộp đủ năm đầu ra bắt buộc ở trạng thái đang chạy được, và quyết định về phạm vi có bằng chứng tiến độ kèm theo.

**Thiết kế.** Probe 8 của L084 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L084.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `execution-and-mid-point-review`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9: `independent oracle`.** Không có nội dung mới. Buổi rà soát giữa kỳ sau hai tuần tự làm.

**Thiết kế.** Probe 9 của L084 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L084.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `execution-and-mid-point-review`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10: `replay`.** Trình bày tiến độ dự án trong 10 phút, tiếp nhận phản biện, và điều chỉnh phạm vi khi bằng chứng cho thấy phạm vi ban đầu không hoàn thành được.

**Thiết kế.** Probe 10 của L084 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L084.10.** Đối soát `replay` bằng đường tính khác implementation chính của `execution-and-mid-point-review`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11: `fresh snapshot`.** Giữ nguyên phạm vi dù tiến độ cho thấy không kịp · bỏ phần chất lượng dữ liệu để kịp phần phân tích · trình bày kế hoạch thay vì trình bày kết quả đã có.

**Thiết kế.** Probe 11 của L084 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L084.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `execution-and-mid-point-review`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12: `novel scenario`.** Nộp đủ năm đầu ra bắt buộc ở trạng thái đang chạy được, và quyết định về phạm vi có bằng chứng tiến độ kèm theo.

**Thiết kế.** Probe 12 của L084 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L084.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `execution-and-mid-point-review`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L084?

<details><summary>Đáp án</summary>

Trình bày tiến độ dự án trong 10 phút, tiếp nhận phản biện, và điều chỉnh phạm vi khi bằng chứng cho thấy phạm vi ban đầu không hoàn thành được.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Giữ nguyên phạm vi dù tiến độ cho thấy không kịp · bỏ phần chất lượng dữ liệu để kịp phần phân tích · trình bày kế hoạch thay vì trình bày kết quả đã có.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Nộp đủ năm đầu ra bắt buộc ở trạng thái đang chạy được, và quyết định về phạm vi có bằng chứng tiến độ kèm theo.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.execution-and-mid-point-review` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-GOVUK-DATA-ANALYTICS-TOOLS-GUIDANCE]]: `src.web.govuk-data-analytics-tools-guidance`
2. [[SRC-STORYTELLING-WITH-DATA]]: `src.book.knaflic-storytelling-with-data.1e`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-GOVUK-DATA-ANALYTICS-TOOLS-GUIDANCE]]: `src.web.govuk-data-analytics-tools-guidance` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Execution and mid-point review | các mục cơ chế, case và probe | Đã phủ | ngoài objective L084 |
| [[SRC-STORYTELLING-WITH-DATA]]: `src.book.knaflic-storytelling-with-data.1e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Execution and mid-point review | các mục cơ chế, case và probe | Đã phủ | ngoài objective L084 |

## Key takeaways
- Trình bày tiến độ dự án trong 10 phút, tiếp nhận phản biện, và điều chỉnh phạm vi khi bằng chứng cho thấy phạm vi ban đầu không hoàn thành được.
- Nộp đủ năm đầu ra bắt buộc ở trạng thái đang chạy được, và quyết định về phạm vi có bằng chứng tiến độ kèm theo.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule: kiểm chứng `wiki.da.execution-and-mid-point-review`

> [!important] Phân loại mệnh đề
> Với `wiki.da.execution-and-mid-point-review`, sơ đồ, ví dụ và artifact về **Execution and mid-point review** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.web.govuk-data-analytics-tools-guidance"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Execution and mid-point review"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.da.execution-and-mid-point-review` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Execution and mid-point review**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```yaml
concept_id: "wiki.da.execution-and-mid-point-review"
concept: "Execution and mid-point review"
primary_question: "Làm sao áp dụng Execution and mid-point review và chứng minh kết quả không xanh giả?"
decision_contract:
  input_boundary: "Ghi population, thời điểm, owner và điều chưa biết"
  hard_constraints:
    - "Không vượt quyền hoặc privacy boundary"
    - "Không dùng cùng một assumption làm cả implementation và oracle"
  accept_when: "Có observation phân biệt được các lựa chọn"
  reversal_trigger: "Một hard constraint sai hoặc evidence mới đổi recommendation"
evidence_to_keep:
  - "input snapshot"
  - "chosen and rejected options"
  - "independent review result"
```

Artifact của `wiki.da.execution-and-mid-point-review` buộc người dùng ghi boundary, oracle và reversal trigger cho **Execution and mid-point review**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->

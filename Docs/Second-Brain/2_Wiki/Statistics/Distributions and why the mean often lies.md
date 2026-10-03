---
note_id: wiki.da.distributions-and-why-the-mean-often-lies
concept_key: ck.da.distributions-and-why-the-mean-often-lies
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
primary_question: Làm sao áp dụng Distributions and why the mean often lies và chứng minh kết quả không xanh giả?
source_ids:
  - src.book.openintro-statistics.4e
  - src.paper.google-heart-ux-metrics
relationships:
  builds_on: [wiki.da.reconciliation-and-the-discipline-of-verification]
  prerequisite_of: [wiki.da.variation-real-difference-or-just-noise]
  related_to: []
aliases: [Distributions and why the mean often lies]
tags: [wiki/statistics, data-analyst, module-5]
reference_path: Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/038-distributions-and-why-the-mean-often-lies.md
---

# Distributions and why the mean often lies

**Tóm tắt bản chất:** Bốn chiều mô tả một phân bố: trung tâm, độ trải, hình dạng, giá trị ngoại lai. Trung bình, trung vị và yếu vị, cùng điều kiện chọn giữa ba đại lượng. Phân vị và tứ phân vị; lý do P50, P90 và P99 mang nhiều thông tin hơn trung bình đối với dữ liệu vận hành. Phân bố lệch phải trong dữ liệu doanh thu và thời gian phản hồi. Phân bố đa đỉnh như dấu hiệu hai tổng thể bị trộn. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L038 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Distributions and why the mean often lies**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Mô tả một phân bố trên cả bốn chiều và chọn đại lượng trung tâm phù hợp với hình dạng của nó, nêu lý do. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Bốn chiều mô tả một phân bố: trung tâm, độ trải, hình dạng, giá trị ngoại lai. Trung bình, trung vị và yếu vị, cùng điều kiện chọn giữa ba đại lượng. Phân vị và tứ phân vị; lý do P50, P90 và P99 mang nhiều thông tin hơn trung bình đối với dữ liệu vận hành. Phân bố lệch phải trong dữ liệu doanh thu và thời gian phản hồi. Phân bố đa đỉnh như dấu hiệu hai tổng thể bị trộn.

Cơ chế của `distributions-and-why-the-mean-often-lies` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Báo cáo trung bình cho phân bố lệch mạnh · kết luận từ trung bình và độ lệch chuẩn mà không xem hình dạng · loại giá trị ngoại lai trước khi truy nguyên. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L038: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Mô tả đúng khác biệt của cả bốn tập dữ liệu bằng đại lượng thống kê trước khi vẽ, và chọn đúng đại lượng trung tâm cho từng tập kèm lý do.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Distributions and why the mean often lies

Bài thực hành dùng nhiệm vụ thật của roadmap: Nhận bốn tập dữ liệu có cùng giá trị trung bình nhưng phân bố khác hẳn. Mô tả khác biệt bằng đại lượng thống kê trước khi được phép vẽ đồ thị, sau đó vẽ để đối chiếu.

Trước khi thao tác ở `Distributions and why the mean often lies`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L038 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Distributions and why the mean often lies` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Báo cáo trung bình cho phân bố lệch mạnh · kết luận từ trung bình và độ lệch chuẩn mà không xem hình dạng · loại giá trị ngoại lai trước khi truy nguyên. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L038 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Bốn chiều mô tả một phân bố: trung tâm, độ trải, hình dạng, giá trị ngoại lai. Trung bình, trung vị và yếu vị, cùng điều kiện chọn giữa ba đại lượng. Phân vị và tứ phân vị; lý do P50, P90 và P99 mang nhiều thông tin hơn trung bình đối với dữ liệu vận hành. Phân bố lệch phải trong dữ liệu doanh thu và thời gian phản hồi. Phân bố đa đỉnh như dấu hiệu hai tổng thể bị trộn.

**Thiết kế.** Probe 1 của L038 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L038.1.** Đối soát `population` bằng đường tính khác implementation chính của `distributions-and-why-the-mean-often-lies`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Mô tả một phân bố trên cả bốn chiều và chọn đại lượng trung tâm phù hợp với hình dạng của nó, nêu lý do.

**Thiết kế.** Probe 2 của L038 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L038.2.** Đối soát `grain` bằng đường tính khác implementation chính của `distributions-and-why-the-mean-often-lies`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Báo cáo trung bình cho phân bố lệch mạnh · kết luận từ trung bình và độ lệch chuẩn mà không xem hình dạng · loại giá trị ngoại lai trước khi truy nguyên.

**Thiết kế.** Probe 3 của L038 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L038.3.** Đối soát `identity` bằng đường tính khác implementation chính của `distributions-and-why-the-mean-often-lies`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Mô tả đúng khác biệt của cả bốn tập dữ liệu bằng đại lượng thống kê trước khi vẽ, và chọn đúng đại lượng trung tâm cho từng tập kèm lý do.

**Thiết kế.** Probe 4 của L038 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L038.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `distributions-and-why-the-mean-often-lies`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Bốn chiều mô tả một phân bố: trung tâm, độ trải, hình dạng, giá trị ngoại lai. Trung bình, trung vị và yếu vị, cùng điều kiện chọn giữa ba đại lượng. Phân vị và tứ phân vị; lý do P50, P90 và P99 mang nhiều thông tin hơn trung bình đối với dữ liệu vận hành. Phân bố lệch phải trong dữ liệu doanh thu và thời gian phản hồi. Phân bố đa đỉnh như dấu hiệu hai tổng thể bị trộn.

**Thiết kế.** Probe 5 của L038 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L038.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `distributions-and-why-the-mean-often-lies`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Mô tả một phân bố trên cả bốn chiều và chọn đại lượng trung tâm phù hợp với hình dạng của nó, nêu lý do.

**Thiết kế.** Probe 6 của L038 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L038.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `distributions-and-why-the-mean-often-lies`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Báo cáo trung bình cho phân bố lệch mạnh · kết luận từ trung bình và độ lệch chuẩn mà không xem hình dạng · loại giá trị ngoại lai trước khi truy nguyên.

**Thiết kế.** Probe 7 của L038 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L038.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `distributions-and-why-the-mean-often-lies`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Mô tả đúng khác biệt của cả bốn tập dữ liệu bằng đại lượng thống kê trước khi vẽ, và chọn đúng đại lượng trung tâm cho từng tập kèm lý do.

**Thiết kế.** Probe 8 của L038 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L038.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `distributions-and-why-the-mean-often-lies`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Bốn chiều mô tả một phân bố: trung tâm, độ trải, hình dạng, giá trị ngoại lai. Trung bình, trung vị và yếu vị, cùng điều kiện chọn giữa ba đại lượng. Phân vị và tứ phân vị; lý do P50, P90 và P99 mang nhiều thông tin hơn trung bình đối với dữ liệu vận hành. Phân bố lệch phải trong dữ liệu doanh thu và thời gian phản hồi. Phân bố đa đỉnh như dấu hiệu hai tổng thể bị trộn.

**Thiết kế.** Probe 9 của L038 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L038.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `distributions-and-why-the-mean-often-lies`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Mô tả một phân bố trên cả bốn chiều và chọn đại lượng trung tâm phù hợp với hình dạng của nó, nêu lý do.

**Thiết kế.** Probe 10 của L038 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L038.10.** Đối soát `replay` bằng đường tính khác implementation chính của `distributions-and-why-the-mean-often-lies`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Báo cáo trung bình cho phân bố lệch mạnh · kết luận từ trung bình và độ lệch chuẩn mà không xem hình dạng · loại giá trị ngoại lai trước khi truy nguyên.

**Thiết kế.** Probe 11 của L038 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L038.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `distributions-and-why-the-mean-often-lies`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Mô tả đúng khác biệt của cả bốn tập dữ liệu bằng đại lượng thống kê trước khi vẽ, và chọn đúng đại lượng trung tâm cho từng tập kèm lý do.

**Thiết kế.** Probe 12 của L038 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L038.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `distributions-and-why-the-mean-often-lies`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L038?

<details><summary>Đáp án</summary>

Mô tả một phân bố trên cả bốn chiều và chọn đại lượng trung tâm phù hợp với hình dạng của nó, nêu lý do.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Báo cáo trung bình cho phân bố lệch mạnh · kết luận từ trung bình và độ lệch chuẩn mà không xem hình dạng · loại giá trị ngoại lai trước khi truy nguyên.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Mô tả đúng khác biệt của cả bốn tập dữ liệu bằng đại lượng thống kê trước khi vẽ, và chọn đúng đại lượng trung tâm cho từng tập kèm lý do.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.distributions-and-why-the-mean-often-lies` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-OPENINTRO-STATISTICS-4E]] — `src.book.openintro-statistics.4e`
2. [[SRC-GOOGLE-HEART-UX-METRICS]] — `src.paper.google-heart-ux-metrics`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-OPENINTRO-STATISTICS-4E]] — `src.book.openintro-statistics.4e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Distributions and why the mean often lies | các mục cơ chế, case và probe | Đã phủ | ngoài objective L038 |
| [[SRC-GOOGLE-HEART-UX-METRICS]] — `src.paper.google-heart-ux-metrics` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Distributions and why the mean often lies | các mục cơ chế, case và probe | Đã phủ | ngoài objective L038 |

## Key takeaways
- Mô tả một phân bố trên cả bốn chiều và chọn đại lượng trung tâm phù hợp với hình dạng của nó, nêu lý do.
- Mô tả đúng khác biệt của cả bốn tập dữ liệu bằng đại lượng thống kê trước khi vẽ, và chọn đúng đại lượng trung tâm cho từng tập kèm lý do.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule — kiểm chứng `wiki.da.distributions-and-why-the-mean-often-lies`

> [!important] Phân loại mệnh đề
> Với `wiki.da.distributions-and-why-the-mean-often-lies`, sơ đồ, ví dụ và artifact về **Distributions and why the mean often lies** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.book.openintro-statistics.4e"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Distributions and why the mean often lies"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.da.distributions-and-why-the-mean-often-lies` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Distributions and why the mean often lies**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class WikiDaDistributionsAndWhyTheMeanOftenLieEvidence:
    boundary_declared: bool
    independent_oracle: bool
    reversal_trigger: str

    def accepted(self) -> bool:
        return (
            self.boundary_declared
            and self.independent_oracle
            and bool(self.reversal_trigger.strip())
        )

# Concept: Distributions and why the mean often lies
# Primary question: Làm sao áp dụng Distributions and why the mean often lies và chứng minh kết quả không xanh giả?
evidence = WikiDaDistributionsAndWhyTheMeanOftenLieEvidence(
    boundary_declared=True,
    independent_oracle=True,
    reversal_trigger="Đảo quyết định khi hard constraint bị vi phạm",
)
assert evidence.accepted()
```

Artifact của `wiki.da.distributions-and-why-the-mean-often-lies` buộc người dùng ghi boundary, oracle và reversal trigger cho **Distributions and why the mean often lies**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->

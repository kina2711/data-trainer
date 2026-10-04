---
note_id: wiki.da.slowly-changing-dimensions-and-the-calendar-table
concept_key: ck.da.slowly-changing-dimensions-and-the-calendar-table
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
primary_question: Làm sao áp dụng Slowly changing dimensions and the calendar table và chứng minh kết quả không xanh giả?
source_ids:
  - src.book.kimball-ross-data-warehouse-toolkit.3e
  - src.book.silberschatz-database-system-concepts.7e
relationships:
  builds_on: [wiki.da.dimensional-modeling-and-the-star-schema]
  prerequisite_of: [wiki.da.data-cleaning-in-practice]
  related_to: []
aliases: [Slowly changing dimensions and the calendar table]
tags: [wiki/data-modeling, data-analyst, module-4]
reference_path: Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/035-slowly-changing-dimensions-and-the-calendar-table.md
---

# Slowly changing dimensions and the calendar table

**Tóm tắt bản chất:** Bài toán: thuộc tính chiều thay đổi làm toàn bộ số liệu lịch sử bị gán lại theo giá trị mới. SCD Type 0, 1, 2, 3 và hậu quả báo cáo cụ thể của từng loại. Cài đặt Type 2 bằng ba cột `hieu_luc_tu`, `hieu_luc_den` và cờ bản ghi hiện hành. Truy vấn trạng thái tại một thời điểm trong quá khứ. Bảng lịch: lý do tồn tại và tập thuộc tính tối thiểu. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Problem Definition and Operational Relevance

L035 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Slowly changing dimensions and the calendar table**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Cài đặt một chiều Type 2 và chứng minh rằng một báo cáo lịch sử cho kết quả không đổi sau khi thuộc tính chiều thay đổi. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Mechanism

Bài toán: thuộc tính chiều thay đổi làm toàn bộ số liệu lịch sử bị gán lại theo giá trị mới. SCD Type 0, 1, 2, 3 và hậu quả báo cáo cụ thể của từng loại. Cài đặt Type 2 bằng ba cột `hieu_luc_tu`, `hieu_luc_den` và cờ bản ghi hiện hành. Truy vấn trạng thái tại một thời điểm trong quá khứ. Bảng lịch: lý do tồn tại và tập thuộc tính tối thiểu.

Cơ chế của `slowly-changing-dimensions-and-the-calendar-table` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Cài Type 2 nhưng vẫn ghép theo khoá nghiệp vụ nên vẫn bị gán lại · khoảng hiệu lực chồng lấn làm nhân bản dòng khi ghép · thiếu bảng lịch nên kỳ khuyết biến mất. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Decision Framework

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L035: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành Báo cáo lịch sử cho kết quả giống hệt trước và sau khi thay đổi thuộc tính chiều, và không có khoảng hiệu lực nào chồng lấn.. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Worked Case: Slowly changing dimensions and the calendar table

Bài thực hành dùng nhiệm vụ thật của roadmap: Cài đặt chiều khách hàng Type 2 trên `DS1`. Chạy một báo cáo doanh thu theo vùng, thay đổi vùng của một khách, chạy lại báo cáo và chứng minh số lịch sử không đổi.

Trước khi thao tác ở `Slowly changing dimensions and the calendar table`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L035 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Limits and Common Errors

**Hiểu lầm:** Output của `Slowly changing dimensions and the calendar table` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Cài Type 2 nhưng vẫn ghép theo khoá nghiệp vụ nên vẫn bị gán lại · khoảng hiệu lực chồng lấn làm nhân bản dòng khi ghép · thiếu bảng lịch nên kỳ khuyết biến mất. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L035 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1: `population`.** Bài toán: thuộc tính chiều thay đổi làm toàn bộ số liệu lịch sử bị gán lại theo giá trị mới. SCD Type 0, 1, 2, 3 và hậu quả báo cáo cụ thể của từng loại. Cài đặt Type 2 bằng ba cột `hieu_luc_tu`, `hieu_luc_den` và cờ bản ghi hiện hành. Truy vấn trạng thái tại một thời điểm trong quá khứ. Bảng lịch: lý do tồn tại và tập thuộc tính tối thiểu.

**Thiết kế.** Probe 1 của L035 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L035.1.** Đối soát `population` bằng đường tính khác implementation chính của `slowly-changing-dimensions-and-the-calendar-table`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2: `grain`.** Cài đặt một chiều Type 2 và chứng minh rằng một báo cáo lịch sử cho kết quả không đổi sau khi thuộc tính chiều thay đổi.

**Thiết kế.** Probe 2 của L035 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L035.2.** Đối soát `grain` bằng đường tính khác implementation chính của `slowly-changing-dimensions-and-the-calendar-table`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3: `identity`.** Cài Type 2 nhưng vẫn ghép theo khoá nghiệp vụ nên vẫn bị gán lại · khoảng hiệu lực chồng lấn làm nhân bản dòng khi ghép · thiếu bảng lịch nên kỳ khuyết biến mất.

**Thiết kế.** Probe 3 của L035 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L035.3.** Đối soát `identity` bằng đường tính khác implementation chính của `slowly-changing-dimensions-and-the-calendar-table`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4: `time cutoff`.** Báo cáo lịch sử cho kết quả giống hệt trước và sau khi thay đổi thuộc tính chiều, và không có khoảng hiệu lực nào chồng lấn.

**Thiết kế.** Probe 4 của L035 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L035.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `slowly-changing-dimensions-and-the-calendar-table`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5: `missing versus zero`.** Bài toán: thuộc tính chiều thay đổi làm toàn bộ số liệu lịch sử bị gán lại theo giá trị mới. SCD Type 0, 1, 2, 3 và hậu quả báo cáo cụ thể của từng loại. Cài đặt Type 2 bằng ba cột `hieu_luc_tu`, `hieu_luc_den` và cờ bản ghi hiện hành. Truy vấn trạng thái tại một thời điểm trong quá khứ. Bảng lịch: lý do tồn tại và tập thuộc tính tối thiểu.

**Thiết kế.** Probe 5 của L035 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L035.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `slowly-changing-dimensions-and-the-calendar-table`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6: `duplicate`.** Cài đặt một chiều Type 2 và chứng minh rằng một báo cáo lịch sử cho kết quả không đổi sau khi thuộc tính chiều thay đổi.

**Thiết kế.** Probe 6 của L035 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L035.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `slowly-changing-dimensions-and-the-calendar-table`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7: `join fan-out`.** Cài Type 2 nhưng vẫn ghép theo khoá nghiệp vụ nên vẫn bị gán lại · khoảng hiệu lực chồng lấn làm nhân bản dòng khi ghép · thiếu bảng lịch nên kỳ khuyết biến mất.

**Thiết kế.** Probe 7 của L035 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L035.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `slowly-changing-dimensions-and-the-calendar-table`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8: `changed definition`.** Báo cáo lịch sử cho kết quả giống hệt trước và sau khi thay đổi thuộc tính chiều, và không có khoảng hiệu lực nào chồng lấn.

**Thiết kế.** Probe 8 của L035 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L035.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `slowly-changing-dimensions-and-the-calendar-table`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9: `independent oracle`.** Bài toán: thuộc tính chiều thay đổi làm toàn bộ số liệu lịch sử bị gán lại theo giá trị mới. SCD Type 0, 1, 2, 3 và hậu quả báo cáo cụ thể của từng loại. Cài đặt Type 2 bằng ba cột `hieu_luc_tu`, `hieu_luc_den` và cờ bản ghi hiện hành. Truy vấn trạng thái tại một thời điểm trong quá khứ. Bảng lịch: lý do tồn tại và tập thuộc tính tối thiểu.

**Thiết kế.** Probe 9 của L035 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L035.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `slowly-changing-dimensions-and-the-calendar-table`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10: `replay`.** Cài đặt một chiều Type 2 và chứng minh rằng một báo cáo lịch sử cho kết quả không đổi sau khi thuộc tính chiều thay đổi.

**Thiết kế.** Probe 10 của L035 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L035.10.** Đối soát `replay` bằng đường tính khác implementation chính của `slowly-changing-dimensions-and-the-calendar-table`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11: `fresh snapshot`.** Cài Type 2 nhưng vẫn ghép theo khoá nghiệp vụ nên vẫn bị gán lại · khoảng hiệu lực chồng lấn làm nhân bản dòng khi ghép · thiếu bảng lịch nên kỳ khuyết biến mất.

**Thiết kế.** Probe 11 của L035 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L035.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `slowly-changing-dimensions-and-the-calendar-table`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12: `novel scenario`.** Báo cáo lịch sử cho kết quả giống hệt trước và sau khi thay đổi thuộc tính chiều, và không có khoảng hiệu lực nào chồng lấn.

**Thiết kế.** Probe 12 của L035 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L035.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `slowly-changing-dimensions-and-the-calendar-table`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L035?

<details><summary>Đáp án</summary>

Cài đặt một chiều Type 2 và chứng minh rằng một báo cáo lịch sử cho kết quả không đổi sau khi thuộc tính chiều thay đổi.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Cài Type 2 nhưng vẫn ghép theo khoá nghiệp vụ nên vẫn bị gán lại · khoảng hiệu lực chồng lấn làm nhân bản dòng khi ghép · thiếu bảng lịch nên kỳ khuyết biến mất.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Báo cáo lịch sử cho kết quả giống hệt trước và sau khi thay đổi thuộc tính chiều, và không có khoảng hiệu lực nào chồng lấn.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.slowly-changing-dimensions-and-the-calendar-table` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]]: `src.book.kimball-ross-data-warehouse-toolkit.3e`
2. [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]]: `src.book.silberschatz-database-system-concepts.7e`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]]: `src.book.kimball-ross-data-warehouse-toolkit.3e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Slowly changing dimensions and the calendar table | các mục cơ chế, case và probe | Đã phủ | ngoài objective L035 |
| [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]]: `src.book.silberschatz-database-system-concepts.7e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Slowly changing dimensions and the calendar table | các mục cơ chế, case và probe | Đã phủ | ngoài objective L035 |

## Key takeaways
- Cài đặt một chiều Type 2 và chứng minh rằng một báo cáo lịch sử cho kết quả không đổi sau khi thuộc tính chiều thay đổi.
- Báo cáo lịch sử cho kết quả giống hệt trước và sau khi thay đổi thuộc tính chiều, và không có khoảng hiệu lực nào chồng lấn.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule: kiểm chứng `wiki.da.slowly-changing-dimensions-and-the-calendar-table`

> [!important] Phân loại mệnh đề
> Với `wiki.da.slowly-changing-dimensions-and-the-calendar-table`, sơ đồ, ví dụ và artifact về **Slowly changing dimensions and the calendar table** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.book.kimball-ross-data-warehouse-toolkit.3e"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Slowly changing dimensions and the calendar table"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.da.slowly-changing-dimensions-and-the-calendar-table` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Slowly changing dimensions and the calendar table**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```yaml
concept_id: "wiki.da.slowly-changing-dimensions-and-the-calendar-table"
concept: "Slowly changing dimensions and the calendar table"
primary_question: "Làm sao áp dụng Slowly changing dimensions and the calendar table và chứng minh kết quả không xanh giả?"
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

Artifact của `wiki.da.slowly-changing-dimensions-and-the-calendar-table` buộc người dùng ghi boundary, oracle và reversal trigger cho **Slowly changing dimensions and the calendar table**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->

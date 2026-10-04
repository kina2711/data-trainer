---
note_id: wiki.da.join-2-row-fan-out-and-multi-table-joins
concept_key: ck.da.join-2-row-fan-out-and-multi-table-joins
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
primary_question: Làm sao áp dụng JOIN (2) - row fan-out and multi-table joins và chứng minh kết quả không xanh giả?
source_ids:
  - src.course.hcmut-sql
  - src.book.silberschatz-database-system-concepts.7e
relationships:
  builds_on: [wiki.da.join-1-the-mechanism-and-four-types]
  prerequisite_of: [wiki.da.subqueries-and-ctes]
  related_to: []
aliases: [JOIN (2) - row fan-out and multi-table joins]
tags: [wiki/sql, data-analyst, module-3]
reference_path: Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/024-join-2-row-fan-out-and-multi-table-joins.md
---

# JOIN (2) - row fan-out and multi-table joins

**Tóm tắt bản chất:** Nhân bản dòng: cơ chế bảng bên phải có nhiều dòng khớp làm tổng bị thổi phồng, cách phát hiện bằng đếm và cách xử lý bằng gộp trước khi ghép. `LEFT JOIN` có điều kiện bảng phải đặt trong `WHERE` và cơ chế nó biến thành `INNER JOIN`. Ghép ba bảng trở lên và thứ tự ghép. Tự ghép cho quan hệ phân cấp. Quy trình kiểm chứng bắt buộc: đếm dòng trước và sau mỗi phép ghép. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Problem Definition and Operational Relevance

L024 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **JOIN (2) - row fan-out and multi-table joins**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Viết truy vấn ghép nhiều bảng và chứng minh bằng phép đếm rằng kết quả không mất dòng và không nhân dòng. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Mechanism

Nhân bản dòng: cơ chế bảng bên phải có nhiều dòng khớp làm tổng bị thổi phồng, cách phát hiện bằng đếm và cách xử lý bằng gộp trước khi ghép. `LEFT JOIN` có điều kiện bảng phải đặt trong `WHERE` và cơ chế nó biến thành `INNER JOIN`. Ghép ba bảng trở lên và thứ tự ghép. Tự ghép cho quan hệ phân cấp. Quy trình kiểm chứng bắt buộc: đếm dòng trước và sau mỗi phép ghép.

Cơ chế của `join-2-row-fan-out-and-multi-table-joins` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Ghép bảng chi tiết vào bảng tổng rồi cộng cột tổng · đặt điều kiện bảng phải vào `WHERE` sau `LEFT JOIN` · không đếm dòng trước và sau nên không phát hiện nhân bản. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Decision Framework

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L024: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành Tổng doanh thu từ truy vấn 5 bảng khớp tuyệt đối với tổng từ bảng hoá đơn, và nộp đủ phép đếm dòng tại mỗi bước ghép.. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Worked Case: JOIN (2) - row fan-out and multi-table joins

Bài thực hành dùng nhiệm vụ thật của roadmap: Trên `DS1`, ghép 5 bảng để ra báo cáo doanh thu theo khách hàng × sản phẩm. Chứng minh tổng khớp với tổng tính trực tiếp từ bảng hoá đơn.

Trước khi thao tác ở `JOIN (2) - row fan-out and multi-table joins`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L024 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Limits and Common Errors

**Hiểu lầm:** Output của `JOIN (2) - row fan-out and multi-table joins` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Ghép bảng chi tiết vào bảng tổng rồi cộng cột tổng · đặt điều kiện bảng phải vào `WHERE` sau `LEFT JOIN` · không đếm dòng trước và sau nên không phát hiện nhân bản. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L024 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1: `population`.** Nhân bản dòng: cơ chế bảng bên phải có nhiều dòng khớp làm tổng bị thổi phồng, cách phát hiện bằng đếm và cách xử lý bằng gộp trước khi ghép. `LEFT JOIN` có điều kiện bảng phải đặt trong `WHERE` và cơ chế nó biến thành `INNER JOIN`. Ghép ba bảng trở lên và thứ tự ghép. Tự ghép cho quan hệ phân cấp. Quy trình kiểm chứng bắt buộc: đếm dòng trước và sau mỗi phép ghép.

**Thiết kế.** Probe 1 của L024 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L024.1.** Đối soát `population` bằng đường tính khác implementation chính của `join-2-row-fan-out-and-multi-table-joins`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2: `grain`.** Viết truy vấn ghép nhiều bảng và chứng minh bằng phép đếm rằng kết quả không mất dòng và không nhân dòng.

**Thiết kế.** Probe 2 của L024 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L024.2.** Đối soát `grain` bằng đường tính khác implementation chính của `join-2-row-fan-out-and-multi-table-joins`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3: `identity`.** Ghép bảng chi tiết vào bảng tổng rồi cộng cột tổng · đặt điều kiện bảng phải vào `WHERE` sau `LEFT JOIN` · không đếm dòng trước và sau nên không phát hiện nhân bản.

**Thiết kế.** Probe 3 của L024 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L024.3.** Đối soát `identity` bằng đường tính khác implementation chính của `join-2-row-fan-out-and-multi-table-joins`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4: `time cutoff`.** Tổng doanh thu từ truy vấn 5 bảng khớp tuyệt đối với tổng từ bảng hoá đơn, và nộp đủ phép đếm dòng tại mỗi bước ghép.

**Thiết kế.** Probe 4 của L024 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L024.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `join-2-row-fan-out-and-multi-table-joins`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5: `missing versus zero`.** Nhân bản dòng: cơ chế bảng bên phải có nhiều dòng khớp làm tổng bị thổi phồng, cách phát hiện bằng đếm và cách xử lý bằng gộp trước khi ghép. `LEFT JOIN` có điều kiện bảng phải đặt trong `WHERE` và cơ chế nó biến thành `INNER JOIN`. Ghép ba bảng trở lên và thứ tự ghép. Tự ghép cho quan hệ phân cấp. Quy trình kiểm chứng bắt buộc: đếm dòng trước và sau mỗi phép ghép.

**Thiết kế.** Probe 5 của L024 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L024.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `join-2-row-fan-out-and-multi-table-joins`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6: `duplicate`.** Viết truy vấn ghép nhiều bảng và chứng minh bằng phép đếm rằng kết quả không mất dòng và không nhân dòng.

**Thiết kế.** Probe 6 của L024 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L024.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `join-2-row-fan-out-and-multi-table-joins`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7: `join fan-out`.** Ghép bảng chi tiết vào bảng tổng rồi cộng cột tổng · đặt điều kiện bảng phải vào `WHERE` sau `LEFT JOIN` · không đếm dòng trước và sau nên không phát hiện nhân bản.

**Thiết kế.** Probe 7 của L024 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L024.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `join-2-row-fan-out-and-multi-table-joins`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8: `changed definition`.** Tổng doanh thu từ truy vấn 5 bảng khớp tuyệt đối với tổng từ bảng hoá đơn, và nộp đủ phép đếm dòng tại mỗi bước ghép.

**Thiết kế.** Probe 8 của L024 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L024.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `join-2-row-fan-out-and-multi-table-joins`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9: `independent oracle`.** Nhân bản dòng: cơ chế bảng bên phải có nhiều dòng khớp làm tổng bị thổi phồng, cách phát hiện bằng đếm và cách xử lý bằng gộp trước khi ghép. `LEFT JOIN` có điều kiện bảng phải đặt trong `WHERE` và cơ chế nó biến thành `INNER JOIN`. Ghép ba bảng trở lên và thứ tự ghép. Tự ghép cho quan hệ phân cấp. Quy trình kiểm chứng bắt buộc: đếm dòng trước và sau mỗi phép ghép.

**Thiết kế.** Probe 9 của L024 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L024.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `join-2-row-fan-out-and-multi-table-joins`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10: `replay`.** Viết truy vấn ghép nhiều bảng và chứng minh bằng phép đếm rằng kết quả không mất dòng và không nhân dòng.

**Thiết kế.** Probe 10 của L024 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L024.10.** Đối soát `replay` bằng đường tính khác implementation chính của `join-2-row-fan-out-and-multi-table-joins`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11: `fresh snapshot`.** Ghép bảng chi tiết vào bảng tổng rồi cộng cột tổng · đặt điều kiện bảng phải vào `WHERE` sau `LEFT JOIN` · không đếm dòng trước và sau nên không phát hiện nhân bản.

**Thiết kế.** Probe 11 của L024 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L024.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `join-2-row-fan-out-and-multi-table-joins`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12: `novel scenario`.** Tổng doanh thu từ truy vấn 5 bảng khớp tuyệt đối với tổng từ bảng hoá đơn, và nộp đủ phép đếm dòng tại mỗi bước ghép.

**Thiết kế.** Probe 12 của L024 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L024.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `join-2-row-fan-out-and-multi-table-joins`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L024?

<details><summary>Đáp án</summary>

Viết truy vấn ghép nhiều bảng và chứng minh bằng phép đếm rằng kết quả không mất dòng và không nhân dòng.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Ghép bảng chi tiết vào bảng tổng rồi cộng cột tổng · đặt điều kiện bảng phải vào `WHERE` sau `LEFT JOIN` · không đếm dòng trước và sau nên không phát hiện nhân bản.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Tổng doanh thu từ truy vấn 5 bảng khớp tuyệt đối với tổng từ bảng hoá đơn, và nộp đủ phép đếm dòng tại mỗi bước ghép.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.join-2-row-fan-out-and-multi-table-joins` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-HCMUT-SQL]]: `src.course.hcmut-sql`
2. [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]]: `src.book.silberschatz-database-system-concepts.7e`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-HCMUT-SQL]]: `src.course.hcmut-sql` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới JOIN (2) - row fan-out and multi-table joins | các mục cơ chế, case và probe | Đã phủ | ngoài objective L024 |
| [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]]: `src.book.silberschatz-database-system-concepts.7e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới JOIN (2) - row fan-out and multi-table joins | các mục cơ chế, case và probe | Đã phủ | ngoài objective L024 |

## Key takeaways
- Viết truy vấn ghép nhiều bảng và chứng minh bằng phép đếm rằng kết quả không mất dòng và không nhân dòng.
- Tổng doanh thu từ truy vấn 5 bảng khớp tuyệt đối với tổng từ bảng hoá đơn, và nộp đủ phép đếm dòng tại mỗi bước ghép.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule: kiểm chứng `wiki.da.join-2-row-fan-out-and-multi-table-joins`

> [!important] Phân loại mệnh đề
> Với `wiki.da.join-2-row-fan-out-and-multi-table-joins`, sơ đồ, ví dụ và artifact về **JOIN (2) - row fan-out and multi-table joins** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.course.hcmut-sql"] --> B["Khóa boundary"]
    B --> M["Cơ chế: JOIN (2) - row fan-out and multi-table joins"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.da.join-2-row-fan-out-and-multi-table-joins` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **JOIN (2) - row fan-out and multi-table joins**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```sql
-- Verification harness for: JOIN (2) - row fan-out and multi-table joins
WITH evidence AS (
    SELECT 'wiki.da.join-2-row-fan-out-and-multi-table-joins' AS concept_id,
           'boundary_declared' AS check_name, 1 AS passed
    UNION ALL
    SELECT 'wiki.da.join-2-row-fan-out-and-multi-table-joins', 'independent_oracle', 1
    UNION ALL
    SELECT 'wiki.da.join-2-row-fan-out-and-multi-table-joins', 'reversal_trigger_recorded', 1
)
SELECT concept_id,
       MIN(passed) AS all_hard_checks_pass,
       COUNT(*) AS evidence_items
FROM evidence
GROUP BY concept_id
HAVING MIN(passed) = 1;
```

Artifact của `wiki.da.join-2-row-fan-out-and-multi-table-joins` buộc người dùng ghi boundary, oracle và reversal trigger cho **JOIN (2) - row fan-out and multi-table joins**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->

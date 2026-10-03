---
note_id: wiki.da.window-functions-1-ranking-and-positioning
concept_key: ck.da.window-functions-1-ranking-and-positioning
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
primary_question: Làm sao áp dụng Window functions (1) - ranking and positioning và chứng minh kết quả không xanh giả?
source_ids:
  - src.course.hcmut-sql
  - src.book.silberschatz-database-system-concepts.7e
relationships:
  builds_on: [wiki.da.subqueries-and-ctes]
  prerequisite_of: [wiki.da.window-functions-2-running-totals-and-period-comparison]
  related_to: []
aliases: [Window functions (1) - ranking and positioning]
tags: [wiki/sql, data-analyst, module-3]
reference_path: Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/026-window-functions-1-ranking-and-positioning.md
---

# Window functions (1) - ranking and positioning

**Tóm tắt bản chất:** Khác biệt nền tảng: `GROUP BY` thu gọn số dòng, `OVER` giữ nguyên số dòng. Cấu trúc `OVER (PARTITION BY ... ORDER BY ...)`. `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `NTILE`, với khác biệt chỉ biểu hiện khi tồn tại giá trị trùng. Mẫu lấy N dòng đầu mỗi nhóm. Nguyên nhân không dùng được hàm cửa sổ trong `WHERE` và cách vòng qua bằng truy vấn con hoặc CTE. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L026 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Window functions (1) - ranking and positioning**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Giải bài toán lấy N dòng đầu theo nhóm, và chọn giữa bốn hàm xếp hạng theo yêu cầu nghiệp vụ về cách xử lý giá trị trùng. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Khác biệt nền tảng: `GROUP BY` thu gọn số dòng, `OVER` giữ nguyên số dòng. Cấu trúc `OVER (PARTITION BY ... ORDER BY ...)`. `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `NTILE`, với khác biệt chỉ biểu hiện khi tồn tại giá trị trùng. Mẫu lấy N dòng đầu mỗi nhóm. Nguyên nhân không dùng được hàm cửa sổ trong `WHERE` và cách vòng qua bằng truy vấn con hoặc CTE.

Cơ chế của `window-functions-1-ranking-and-positioning` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Dùng `RANK` khi nghiệp vụ cần đúng N dòng · đặt hàm cửa sổ trong `WHERE` · thiếu `PARTITION BY` nên xếp hạng trên toàn bảng. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L026: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Cả ba bài cho số dòng đúng trên dữ liệu có giá trị trùng, và mỗi bài kèm lý do chọn hàm xếp hạng.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Window functions (1) - ranking and positioning

Bài thực hành dùng nhiệm vụ thật của roadmap: Ba sản phẩm bán chạy nhất mỗi chi nhánh. Đơn hàng gần nhất của mỗi khách. Chia khách thành 5 nhóm ngũ phân vị theo chi tiêu. Dữ liệu có chứa giá trị trùng ở cả ba bài.

Trước khi thao tác ở `Window functions (1) - ranking and positioning`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L026 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Window functions (1) - ranking and positioning` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Dùng `RANK` khi nghiệp vụ cần đúng N dòng · đặt hàm cửa sổ trong `WHERE` · thiếu `PARTITION BY` nên xếp hạng trên toàn bảng. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L026 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Khác biệt nền tảng: `GROUP BY` thu gọn số dòng, `OVER` giữ nguyên số dòng. Cấu trúc `OVER (PARTITION BY ... ORDER BY ...)`. `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `NTILE`, với khác biệt chỉ biểu hiện khi tồn tại giá trị trùng. Mẫu lấy N dòng đầu mỗi nhóm. Nguyên nhân không dùng được hàm cửa sổ trong `WHERE` và cách vòng qua bằng truy vấn con hoặc CTE.

**Thiết kế.** Probe 1 của L026 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L026.1.** Đối soát `population` bằng đường tính khác implementation chính của `window-functions-1-ranking-and-positioning`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Giải bài toán lấy N dòng đầu theo nhóm, và chọn giữa bốn hàm xếp hạng theo yêu cầu nghiệp vụ về cách xử lý giá trị trùng.

**Thiết kế.** Probe 2 của L026 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L026.2.** Đối soát `grain` bằng đường tính khác implementation chính của `window-functions-1-ranking-and-positioning`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Dùng `RANK` khi nghiệp vụ cần đúng N dòng · đặt hàm cửa sổ trong `WHERE` · thiếu `PARTITION BY` nên xếp hạng trên toàn bảng.

**Thiết kế.** Probe 3 của L026 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L026.3.** Đối soát `identity` bằng đường tính khác implementation chính của `window-functions-1-ranking-and-positioning`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Cả ba bài cho số dòng đúng trên dữ liệu có giá trị trùng, và mỗi bài kèm lý do chọn hàm xếp hạng.

**Thiết kế.** Probe 4 của L026 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L026.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `window-functions-1-ranking-and-positioning`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Khác biệt nền tảng: `GROUP BY` thu gọn số dòng, `OVER` giữ nguyên số dòng. Cấu trúc `OVER (PARTITION BY ... ORDER BY ...)`. `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `NTILE`, với khác biệt chỉ biểu hiện khi tồn tại giá trị trùng. Mẫu lấy N dòng đầu mỗi nhóm. Nguyên nhân không dùng được hàm cửa sổ trong `WHERE` và cách vòng qua bằng truy vấn con hoặc CTE.

**Thiết kế.** Probe 5 của L026 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L026.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `window-functions-1-ranking-and-positioning`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Giải bài toán lấy N dòng đầu theo nhóm, và chọn giữa bốn hàm xếp hạng theo yêu cầu nghiệp vụ về cách xử lý giá trị trùng.

**Thiết kế.** Probe 6 của L026 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L026.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `window-functions-1-ranking-and-positioning`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Dùng `RANK` khi nghiệp vụ cần đúng N dòng · đặt hàm cửa sổ trong `WHERE` · thiếu `PARTITION BY` nên xếp hạng trên toàn bảng.

**Thiết kế.** Probe 7 của L026 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L026.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `window-functions-1-ranking-and-positioning`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Cả ba bài cho số dòng đúng trên dữ liệu có giá trị trùng, và mỗi bài kèm lý do chọn hàm xếp hạng.

**Thiết kế.** Probe 8 của L026 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L026.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `window-functions-1-ranking-and-positioning`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Khác biệt nền tảng: `GROUP BY` thu gọn số dòng, `OVER` giữ nguyên số dòng. Cấu trúc `OVER (PARTITION BY ... ORDER BY ...)`. `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `NTILE`, với khác biệt chỉ biểu hiện khi tồn tại giá trị trùng. Mẫu lấy N dòng đầu mỗi nhóm. Nguyên nhân không dùng được hàm cửa sổ trong `WHERE` và cách vòng qua bằng truy vấn con hoặc CTE.

**Thiết kế.** Probe 9 của L026 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L026.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `window-functions-1-ranking-and-positioning`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Giải bài toán lấy N dòng đầu theo nhóm, và chọn giữa bốn hàm xếp hạng theo yêu cầu nghiệp vụ về cách xử lý giá trị trùng.

**Thiết kế.** Probe 10 của L026 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L026.10.** Đối soát `replay` bằng đường tính khác implementation chính của `window-functions-1-ranking-and-positioning`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Dùng `RANK` khi nghiệp vụ cần đúng N dòng · đặt hàm cửa sổ trong `WHERE` · thiếu `PARTITION BY` nên xếp hạng trên toàn bảng.

**Thiết kế.** Probe 11 của L026 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L026.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `window-functions-1-ranking-and-positioning`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Cả ba bài cho số dòng đúng trên dữ liệu có giá trị trùng, và mỗi bài kèm lý do chọn hàm xếp hạng.

**Thiết kế.** Probe 12 của L026 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L026.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `window-functions-1-ranking-and-positioning`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L026?

<details><summary>Đáp án</summary>

Giải bài toán lấy N dòng đầu theo nhóm, và chọn giữa bốn hàm xếp hạng theo yêu cầu nghiệp vụ về cách xử lý giá trị trùng.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Dùng `RANK` khi nghiệp vụ cần đúng N dòng · đặt hàm cửa sổ trong `WHERE` · thiếu `PARTITION BY` nên xếp hạng trên toàn bảng.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Cả ba bài cho số dòng đúng trên dữ liệu có giá trị trùng, và mỗi bài kèm lý do chọn hàm xếp hạng.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.window-functions-1-ranking-and-positioning` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-HCMUT-SQL]] — `src.course.hcmut-sql`
2. [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] — `src.book.silberschatz-database-system-concepts.7e`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-HCMUT-SQL]] — `src.course.hcmut-sql` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Window functions (1) - ranking and positioning | các mục cơ chế, case và probe | Đã phủ | ngoài objective L026 |
| [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] — `src.book.silberschatz-database-system-concepts.7e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Window functions (1) - ranking and positioning | các mục cơ chế, case và probe | Đã phủ | ngoài objective L026 |

## Key takeaways
- Giải bài toán lấy N dòng đầu theo nhóm, và chọn giữa bốn hàm xếp hạng theo yêu cầu nghiệp vụ về cách xử lý giá trị trùng.
- Cả ba bài cho số dòng đúng trên dữ liệu có giá trị trùng, và mỗi bài kèm lý do chọn hàm xếp hạng.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule — kiểm chứng `wiki.da.window-functions-1-ranking-and-positioning`

> [!important] Phân loại mệnh đề
> Với `wiki.da.window-functions-1-ranking-and-positioning`, sơ đồ, ví dụ và artifact về **Window functions (1) - ranking and positioning** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.course.hcmut-sql"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Window functions (1) - ranking and positioning"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.da.window-functions-1-ranking-and-positioning` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Window functions (1) - ranking and positioning**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```sql
-- Verification harness for: Window functions (1) - ranking and positioning
WITH evidence AS (
    SELECT 'wiki.da.window-functions-1-ranking-and-positioning' AS concept_id,
           'boundary_declared' AS check_name, 1 AS passed
    UNION ALL
    SELECT 'wiki.da.window-functions-1-ranking-and-positioning', 'independent_oracle', 1
    UNION ALL
    SELECT 'wiki.da.window-functions-1-ranking-and-positioning', 'reversal_trigger_recorded', 1
)
SELECT concept_id,
       MIN(passed) AS all_hard_checks_pass,
       COUNT(*) AS evidence_items
FROM evidence
GROUP BY concept_id
HAVING MIN(passed) = 1;
```

Artifact của `wiki.da.window-functions-1-ranking-and-positioning` buộc người dùng ghi boundary, oracle và reversal trigger cho **Window functions (1) - ranking and positioning**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->

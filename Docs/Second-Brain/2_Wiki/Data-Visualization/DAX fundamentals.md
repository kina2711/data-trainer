---
note_id: wiki.da.dax-fundamentals
concept_key: ck.da.dax-fundamentals
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
primary_question: Làm sao áp dụng DAX fundamentals và chứng minh kết quả không xanh giả?
source_ids:
  - src.book.knaflic-storytelling-with-data.1e
  - src.book.ferrari-russo-definitive-guide-dax.3e
relationships:
  builds_on: [wiki.da.power-bi-loading-data-and-modeling]
  prerequisite_of: [wiki.da.time-intelligence-in-dax]
  related_to: []
aliases: [DAX fundamentals]
tags: [wiki/data-visualization, data-analyst, module-6]
reference_path: Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/050-dax-fundamentals.md
---

# DAX fundamentals

**Tóm tắt bản chất:** Cột tính toán so với độ đo: khác biệt về thời điểm tính và về dung lượng, cùng tiêu chí chọn. Ngữ cảnh lọc, trình bày bằng ví dụ trước và định nghĩa sau. `SUM`, `COUNTROWS`, `DISTINCTCOUNT`, `AVERAGE`. `CALCULATE` và cơ chế nó thay đổi ngữ cảnh lọc. `FILTER`, `ALL`, `ALLEXCEPT`. Chỉ số dạng tỉ lệ và sai số phát sinh khi tổng hợp tỉ lệ ở hạt khác với hạt tính. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Problem Definition and Operational Relevance

L050 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **DAX fundamentals**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Viết độ đo cho kết quả đúng và giải thích được vì sao giá trị thay đổi khi người dùng chọn một lát cắt. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Mechanism

Cột tính toán so với độ đo: khác biệt về thời điểm tính và về dung lượng, cùng tiêu chí chọn. Ngữ cảnh lọc, trình bày bằng ví dụ trước và định nghĩa sau. `SUM`, `COUNTROWS`, `DISTINCTCOUNT`, `AVERAGE`. `CALCULATE` và cơ chế nó thay đổi ngữ cảnh lọc. `FILTER`, `ALL`, `ALLEXCEPT`. Chỉ số dạng tỉ lệ và sai số phát sinh khi tổng hợp tỉ lệ ở hạt khác với hạt tính.

Cơ chế của `dax-fundamentals` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Dùng cột tính toán ở nơi cần độ đo · tổng hợp tỉ lệ bằng cách lấy trung bình các tỉ lệ · dùng `ALL` xoá cả bộ lọc cần giữ. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Decision Framework

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L050: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành Cả 15 độ đo khớp với SQL ở mức tổng và ở ít nhất ba lát cắt, và giải thích được thay đổi giá trị theo lát cắt cho 5 độ đo bất kỳ.. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Worked Case: DAX fundamentals

Bài thực hành dùng nhiệm vụ thật của roadmap: Viết 15 độ đo: doanh thu thuần, số khách hàng duy nhất, tỉ lệ đơn hoàn, tỉ trọng theo nhóm, giá trị đơn trung bình. Đối chiếu từng độ đo với SQL ở cả mức tổng và mức lát cắt.

Trước khi thao tác ở `DAX fundamentals`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L050 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Limits and Common Errors

**Hiểu lầm:** Output của `DAX fundamentals` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Dùng cột tính toán ở nơi cần độ đo · tổng hợp tỉ lệ bằng cách lấy trung bình các tỉ lệ · dùng `ALL` xoá cả bộ lọc cần giữ. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L050 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1: `population`.** Cột tính toán so với độ đo: khác biệt về thời điểm tính và về dung lượng, cùng tiêu chí chọn. Ngữ cảnh lọc, trình bày bằng ví dụ trước và định nghĩa sau. `SUM`, `COUNTROWS`, `DISTINCTCOUNT`, `AVERAGE`. `CALCULATE` và cơ chế nó thay đổi ngữ cảnh lọc. `FILTER`, `ALL`, `ALLEXCEPT`. Chỉ số dạng tỉ lệ và sai số phát sinh khi tổng hợp tỉ lệ ở hạt khác với hạt tính.

**Thiết kế.** Probe 1 của L050 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L050.1.** Đối soát `population` bằng đường tính khác implementation chính của `dax-fundamentals`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2: `grain`.** Viết độ đo cho kết quả đúng và giải thích được vì sao giá trị thay đổi khi người dùng chọn một lát cắt.

**Thiết kế.** Probe 2 của L050 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L050.2.** Đối soát `grain` bằng đường tính khác implementation chính của `dax-fundamentals`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3: `identity`.** Dùng cột tính toán ở nơi cần độ đo · tổng hợp tỉ lệ bằng cách lấy trung bình các tỉ lệ · dùng `ALL` xoá cả bộ lọc cần giữ.

**Thiết kế.** Probe 3 của L050 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L050.3.** Đối soát `identity` bằng đường tính khác implementation chính của `dax-fundamentals`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4: `time cutoff`.** Cả 15 độ đo khớp với SQL ở mức tổng và ở ít nhất ba lát cắt, và giải thích được thay đổi giá trị theo lát cắt cho 5 độ đo bất kỳ.

**Thiết kế.** Probe 4 của L050 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L050.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `dax-fundamentals`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5: `missing versus zero`.** Cột tính toán so với độ đo: khác biệt về thời điểm tính và về dung lượng, cùng tiêu chí chọn. Ngữ cảnh lọc, trình bày bằng ví dụ trước và định nghĩa sau. `SUM`, `COUNTROWS`, `DISTINCTCOUNT`, `AVERAGE`. `CALCULATE` và cơ chế nó thay đổi ngữ cảnh lọc. `FILTER`, `ALL`, `ALLEXCEPT`. Chỉ số dạng tỉ lệ và sai số phát sinh khi tổng hợp tỉ lệ ở hạt khác với hạt tính.

**Thiết kế.** Probe 5 của L050 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L050.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `dax-fundamentals`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6: `duplicate`.** Viết độ đo cho kết quả đúng và giải thích được vì sao giá trị thay đổi khi người dùng chọn một lát cắt.

**Thiết kế.** Probe 6 của L050 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L050.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `dax-fundamentals`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7: `join fan-out`.** Dùng cột tính toán ở nơi cần độ đo · tổng hợp tỉ lệ bằng cách lấy trung bình các tỉ lệ · dùng `ALL` xoá cả bộ lọc cần giữ.

**Thiết kế.** Probe 7 của L050 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L050.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `dax-fundamentals`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8: `changed definition`.** Cả 15 độ đo khớp với SQL ở mức tổng và ở ít nhất ba lát cắt, và giải thích được thay đổi giá trị theo lát cắt cho 5 độ đo bất kỳ.

**Thiết kế.** Probe 8 của L050 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L050.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `dax-fundamentals`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9: `independent oracle`.** Cột tính toán so với độ đo: khác biệt về thời điểm tính và về dung lượng, cùng tiêu chí chọn. Ngữ cảnh lọc, trình bày bằng ví dụ trước và định nghĩa sau. `SUM`, `COUNTROWS`, `DISTINCTCOUNT`, `AVERAGE`. `CALCULATE` và cơ chế nó thay đổi ngữ cảnh lọc. `FILTER`, `ALL`, `ALLEXCEPT`. Chỉ số dạng tỉ lệ và sai số phát sinh khi tổng hợp tỉ lệ ở hạt khác với hạt tính.

**Thiết kế.** Probe 9 của L050 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L050.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `dax-fundamentals`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10: `replay`.** Viết độ đo cho kết quả đúng và giải thích được vì sao giá trị thay đổi khi người dùng chọn một lát cắt.

**Thiết kế.** Probe 10 của L050 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L050.10.** Đối soát `replay` bằng đường tính khác implementation chính của `dax-fundamentals`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11: `fresh snapshot`.** Dùng cột tính toán ở nơi cần độ đo · tổng hợp tỉ lệ bằng cách lấy trung bình các tỉ lệ · dùng `ALL` xoá cả bộ lọc cần giữ.

**Thiết kế.** Probe 11 của L050 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L050.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `dax-fundamentals`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12: `novel scenario`.** Cả 15 độ đo khớp với SQL ở mức tổng và ở ít nhất ba lát cắt, và giải thích được thay đổi giá trị theo lát cắt cho 5 độ đo bất kỳ.

**Thiết kế.** Probe 12 của L050 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L050.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `dax-fundamentals`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L050?

<details><summary>Đáp án</summary>

Viết độ đo cho kết quả đúng và giải thích được vì sao giá trị thay đổi khi người dùng chọn một lát cắt.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Dùng cột tính toán ở nơi cần độ đo · tổng hợp tỉ lệ bằng cách lấy trung bình các tỉ lệ · dùng `ALL` xoá cả bộ lọc cần giữ.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Cả 15 độ đo khớp với SQL ở mức tổng và ở ít nhất ba lát cắt, và giải thích được thay đổi giá trị theo lát cắt cho 5 độ đo bất kỳ.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.dax-fundamentals` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-STORYTELLING-WITH-DATA]]: `src.book.knaflic-storytelling-with-data.1e`
2. [[SRC-DEFINITIVE-GUIDE-DAX-3E]]: `src.book.ferrari-russo-definitive-guide-dax.3e`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-STORYTELLING-WITH-DATA]]: `src.book.knaflic-storytelling-with-data.1e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới DAX fundamentals | các mục cơ chế, case và probe | Đã phủ | ngoài objective L050 |
| [[SRC-DEFINITIVE-GUIDE-DAX-3E]]: `src.book.ferrari-russo-definitive-guide-dax.3e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới DAX fundamentals | các mục cơ chế, case và probe | Đã phủ | ngoài objective L050 |

## Key takeaways
- Viết độ đo cho kết quả đúng và giải thích được vì sao giá trị thay đổi khi người dùng chọn một lát cắt.
- Cả 15 độ đo khớp với SQL ở mức tổng và ở ít nhất ba lát cắt, và giải thích được thay đổi giá trị theo lát cắt cho 5 độ đo bất kỳ.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule: kiểm chứng `wiki.da.dax-fundamentals`

> [!important] Phân loại mệnh đề
> Với `wiki.da.dax-fundamentals`, sơ đồ, ví dụ và artifact về **DAX fundamentals** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.book.knaflic-storytelling-with-data.1e"] --> B["Khóa boundary"]
    B --> M["Cơ chế: DAX fundamentals"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.da.dax-fundamentals` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **DAX fundamentals**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```yaml
concept_id: "wiki.da.dax-fundamentals"
concept: "DAX fundamentals"
primary_question: "Làm sao áp dụng DAX fundamentals và chứng minh kết quả không xanh giả?"
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

Artifact của `wiki.da.dax-fundamentals` buộc người dùng ghi boundary, oracle và reversal trigger cho **DAX fundamentals**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->

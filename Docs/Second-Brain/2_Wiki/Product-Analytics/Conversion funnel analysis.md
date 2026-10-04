---
note_id: wiki.da.conversion-funnel-analysis
concept_key: ck.da.conversion-funnel-analysis
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
primary_question: Làm sao áp dụng Conversion funnel analysis và chứng minh kết quả không xanh giả?
source_ids:
  - src.web.amplitude-north-star-framework
  - src.paper.google-heart-ux-metrics
relationships:
  builds_on: [wiki.da.event-data-and-the-tracking-plan]
  prerequisite_of: [wiki.da.cohorts-and-retention-analysis]
  related_to: []
aliases: [Conversion funnel analysis]
tags: [wiki/product-analytics, data-analyst, module-7]
reference_path: Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/056-conversion-funnel-analysis.md
---

# Conversion funnel analysis

**Tóm tắt bản chất:** Ba tham số định nghĩa một phễu và tác động của từng tham số lên kết quả: phễu nghiêm ngặt hay lỏng về thứ tự bước, độ dài cửa sổ thời gian, đơn vị đếm theo người dùng hay theo phiên. Phân rã tỉ lệ rơi theo chiều. Phễu ngược để tìm đường đi thực tế của người dùng. So sánh phễu giữa các phân khúc. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Problem Definition and Operational Relevance

L056 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Conversion funnel analysis**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Dựng một phân tích phễu có khai báo đủ ba tham số, định vị bước rơi nghiêm trọng nhất, và định lượng tác động của việc đổi một tham số lên kết quả. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Mechanism

Ba tham số định nghĩa một phễu và tác động của từng tham số lên kết quả: phễu nghiêm ngặt hay lỏng về thứ tự bước, độ dài cửa sổ thời gian, đơn vị đếm theo người dùng hay theo phiên. Phân rã tỉ lệ rơi theo chiều. Phễu ngược để tìm đường đi thực tế của người dùng. So sánh phễu giữa các phân khúc.

Cơ chế của `conversion-funnel-analysis` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Không khai báo cửa sổ thời gian nên kết quả không tái lập được · đếm theo phiên khi câu hỏi hỏi theo người dùng · so sánh phễu giữa hai kỳ có định nghĩa bước khác nhau. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Decision Framework

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L056: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành Phễu khai báo đủ ba tham số, định vị đúng bước rơi nghiêm trọng nhất, và giải thích được chênh lệch 12 điểm giữa hai cửa sổ.. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Worked Case: Conversion funnel analysis

Bài thực hành dùng nhiệm vụ thật của roadmap: Dựng phễu 5 bước trên `DS3` có phân rã theo bốn chiều. Chạy lại với cửa sổ 1 ngày và 7 ngày, và giải thích vì sao tỉ lệ chuyển đổi chênh 12 điểm phần trăm.

Trước khi thao tác ở `Conversion funnel analysis`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L056 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Limits and Common Errors

**Hiểu lầm:** Output của `Conversion funnel analysis` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Không khai báo cửa sổ thời gian nên kết quả không tái lập được · đếm theo phiên khi câu hỏi hỏi theo người dùng · so sánh phễu giữa hai kỳ có định nghĩa bước khác nhau. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L056 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1: `population`.** Ba tham số định nghĩa một phễu và tác động của từng tham số lên kết quả: phễu nghiêm ngặt hay lỏng về thứ tự bước, độ dài cửa sổ thời gian, đơn vị đếm theo người dùng hay theo phiên. Phân rã tỉ lệ rơi theo chiều. Phễu ngược để tìm đường đi thực tế của người dùng. So sánh phễu giữa các phân khúc.

**Thiết kế.** Probe 1 của L056 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L056.1.** Đối soát `population` bằng đường tính khác implementation chính của `conversion-funnel-analysis`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2: `grain`.** Dựng một phân tích phễu có khai báo đủ ba tham số, định vị bước rơi nghiêm trọng nhất, và định lượng tác động của việc đổi một tham số lên kết quả.

**Thiết kế.** Probe 2 của L056 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L056.2.** Đối soát `grain` bằng đường tính khác implementation chính của `conversion-funnel-analysis`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3: `identity`.** Không khai báo cửa sổ thời gian nên kết quả không tái lập được · đếm theo phiên khi câu hỏi hỏi theo người dùng · so sánh phễu giữa hai kỳ có định nghĩa bước khác nhau.

**Thiết kế.** Probe 3 của L056 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L056.3.** Đối soát `identity` bằng đường tính khác implementation chính của `conversion-funnel-analysis`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4: `time cutoff`.** Phễu khai báo đủ ba tham số, định vị đúng bước rơi nghiêm trọng nhất, và giải thích được chênh lệch 12 điểm giữa hai cửa sổ.

**Thiết kế.** Probe 4 của L056 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L056.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `conversion-funnel-analysis`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5: `missing versus zero`.** Ba tham số định nghĩa một phễu và tác động của từng tham số lên kết quả: phễu nghiêm ngặt hay lỏng về thứ tự bước, độ dài cửa sổ thời gian, đơn vị đếm theo người dùng hay theo phiên. Phân rã tỉ lệ rơi theo chiều. Phễu ngược để tìm đường đi thực tế của người dùng. So sánh phễu giữa các phân khúc.

**Thiết kế.** Probe 5 của L056 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L056.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `conversion-funnel-analysis`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6: `duplicate`.** Dựng một phân tích phễu có khai báo đủ ba tham số, định vị bước rơi nghiêm trọng nhất, và định lượng tác động của việc đổi một tham số lên kết quả.

**Thiết kế.** Probe 6 của L056 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L056.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `conversion-funnel-analysis`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7: `join fan-out`.** Không khai báo cửa sổ thời gian nên kết quả không tái lập được · đếm theo phiên khi câu hỏi hỏi theo người dùng · so sánh phễu giữa hai kỳ có định nghĩa bước khác nhau.

**Thiết kế.** Probe 7 của L056 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L056.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `conversion-funnel-analysis`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8: `changed definition`.** Phễu khai báo đủ ba tham số, định vị đúng bước rơi nghiêm trọng nhất, và giải thích được chênh lệch 12 điểm giữa hai cửa sổ.

**Thiết kế.** Probe 8 của L056 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L056.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `conversion-funnel-analysis`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9: `independent oracle`.** Ba tham số định nghĩa một phễu và tác động của từng tham số lên kết quả: phễu nghiêm ngặt hay lỏng về thứ tự bước, độ dài cửa sổ thời gian, đơn vị đếm theo người dùng hay theo phiên. Phân rã tỉ lệ rơi theo chiều. Phễu ngược để tìm đường đi thực tế của người dùng. So sánh phễu giữa các phân khúc.

**Thiết kế.** Probe 9 của L056 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L056.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `conversion-funnel-analysis`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10: `replay`.** Dựng một phân tích phễu có khai báo đủ ba tham số, định vị bước rơi nghiêm trọng nhất, và định lượng tác động của việc đổi một tham số lên kết quả.

**Thiết kế.** Probe 10 của L056 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L056.10.** Đối soát `replay` bằng đường tính khác implementation chính của `conversion-funnel-analysis`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11: `fresh snapshot`.** Không khai báo cửa sổ thời gian nên kết quả không tái lập được · đếm theo phiên khi câu hỏi hỏi theo người dùng · so sánh phễu giữa hai kỳ có định nghĩa bước khác nhau.

**Thiết kế.** Probe 11 của L056 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L056.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `conversion-funnel-analysis`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12: `novel scenario`.** Phễu khai báo đủ ba tham số, định vị đúng bước rơi nghiêm trọng nhất, và giải thích được chênh lệch 12 điểm giữa hai cửa sổ.

**Thiết kế.** Probe 12 của L056 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L056.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `conversion-funnel-analysis`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L056?

<details><summary>Đáp án</summary>

Dựng một phân tích phễu có khai báo đủ ba tham số, định vị bước rơi nghiêm trọng nhất, và định lượng tác động của việc đổi một tham số lên kết quả.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Không khai báo cửa sổ thời gian nên kết quả không tái lập được · đếm theo phiên khi câu hỏi hỏi theo người dùng · so sánh phễu giữa hai kỳ có định nghĩa bước khác nhau.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Phễu khai báo đủ ba tham số, định vị đúng bước rơi nghiêm trọng nhất, và giải thích được chênh lệch 12 điểm giữa hai cửa sổ.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.conversion-funnel-analysis` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-AMPLITUDE-NORTH-STAR-FRAMEWORK]]: `src.web.amplitude-north-star-framework`
2. [[SRC-GOOGLE-HEART-UX-METRICS]]: `src.paper.google-heart-ux-metrics`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-AMPLITUDE-NORTH-STAR-FRAMEWORK]]: `src.web.amplitude-north-star-framework` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Conversion funnel analysis | các mục cơ chế, case và probe | Đã phủ | ngoài objective L056 |
| [[SRC-GOOGLE-HEART-UX-METRICS]]: `src.paper.google-heart-ux-metrics` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Conversion funnel analysis | các mục cơ chế, case và probe | Đã phủ | ngoài objective L056 |

## Key takeaways
- Dựng một phân tích phễu có khai báo đủ ba tham số, định vị bước rơi nghiêm trọng nhất, và định lượng tác động của việc đổi một tham số lên kết quả.
- Phễu khai báo đủ ba tham số, định vị đúng bước rơi nghiêm trọng nhất, và giải thích được chênh lệch 12 điểm giữa hai cửa sổ.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule: kiểm chứng `wiki.da.conversion-funnel-analysis`

> [!important] Phân loại mệnh đề
> Với `wiki.da.conversion-funnel-analysis`, sơ đồ, ví dụ và artifact về **Conversion funnel analysis** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.web.amplitude-north-star-framework"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Conversion funnel analysis"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.da.conversion-funnel-analysis` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Conversion funnel analysis**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```sql
-- Verification harness for: Conversion funnel analysis
WITH evidence AS (
    SELECT 'wiki.da.conversion-funnel-analysis' AS concept_id,
           'boundary_declared' AS check_name, 1 AS passed
    UNION ALL
    SELECT 'wiki.da.conversion-funnel-analysis', 'independent_oracle', 1
    UNION ALL
    SELECT 'wiki.da.conversion-funnel-analysis', 'reversal_trigger_recorded', 1
)
SELECT concept_id,
       MIN(passed) AS all_hard_checks_pass,
       COUNT(*) AS evidence_items
FROM evidence
GROUP BY concept_id
HAVING MIN(passed) = 1;
```

Artifact của `wiki.da.conversion-funnel-analysis` buộc người dùng ghi boundary, oracle và reversal trigger cho **Conversion funnel analysis**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->

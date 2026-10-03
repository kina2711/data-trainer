---
note_id: wiki.da.marketing-and-channel-analytics
concept_key: ck.da.marketing-and-channel-analytics
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
primary_question: Làm sao áp dụng Marketing and channel analytics và chứng minh kết quả không xanh giả?
source_ids:
  - src.web.amplitude-north-star-framework
  - src.paper.google-heart-ux-metrics
relationships:
  builds_on: [wiki.da.revenue-and-commerce-analytics]
  prerequisite_of: [wiki.da.investigating-a-metric-drop]
  related_to: []
aliases: [Marketing and channel analytics]
tags: [wiki/product-analytics, data-analyst, module-7]
reference_path: Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/060-marketing-and-channel-analytics.md
---

# Marketing and channel analytics

**Tóm tắt bản chất:** Phễu tiếp thị và định nghĩa từng tầng. Bốn mô hình quy kết: chạm cuối, chạm đầu, tuyến tính, suy giảm theo thời gian, và bốn kết luận khác nhau chúng cho trên cùng dữ liệu. Giả định mà mọi mô hình quy kết đều phải đặt, và lý do chúng vẫn được dùng dù giả định không thoả. Chi phí thu hút khách và thời gian hoàn vốn. Trùng lặp kênh và cơ chế làm tổng đóng góp vượt 100%. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L060 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Marketing and channel analytics**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Đọc một báo cáo quy kết và định vị giả định nào của mô hình đang chi phối kết luận của báo cáo đó. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Phễu tiếp thị và định nghĩa từng tầng. Bốn mô hình quy kết: chạm cuối, chạm đầu, tuyến tính, suy giảm theo thời gian, và bốn kết luận khác nhau chúng cho trên cùng dữ liệu. Giả định mà mọi mô hình quy kết đều phải đặt, và lý do chúng vẫn được dùng dù giả định không thoả. Chi phí thu hút khách và thời gian hoàn vốn. Trùng lặp kênh và cơ chế làm tổng đóng góp vượt 100%.

Cơ chế của `marketing-and-channel-analytics` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Trình bày một mô hình quy kết như con số khách quan · cộng đóng góp từ hai mô hình khác nhau · bỏ qua kênh không đo được khi kết luận về hiệu quả. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L060: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Bốn bảng đóng góp theo bốn mô hình được tính trên cùng dữ liệu, và giả định gây tổng vượt 100% được chỉ ra cụ thể.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Marketing and channel analytics

Bài thực hành dùng nhiệm vụ thật của roadmap: Tính đóng góp kênh theo cả bốn mô hình quy kết trên cùng dữ liệu. Giải thích vì sao tổng đóng góp vượt 100% và giả định nào gây ra điều đó.

Trước khi thao tác ở `Marketing and channel analytics`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L060 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Marketing and channel analytics` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Trình bày một mô hình quy kết như con số khách quan · cộng đóng góp từ hai mô hình khác nhau · bỏ qua kênh không đo được khi kết luận về hiệu quả. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L060 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Phễu tiếp thị và định nghĩa từng tầng. Bốn mô hình quy kết: chạm cuối, chạm đầu, tuyến tính, suy giảm theo thời gian, và bốn kết luận khác nhau chúng cho trên cùng dữ liệu. Giả định mà mọi mô hình quy kết đều phải đặt, và lý do chúng vẫn được dùng dù giả định không thoả. Chi phí thu hút khách và thời gian hoàn vốn. Trùng lặp kênh và cơ chế làm tổng đóng góp vượt 100%.

**Thiết kế.** Probe 1 của L060 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L060.1.** Đối soát `population` bằng đường tính khác implementation chính của `marketing-and-channel-analytics`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Đọc một báo cáo quy kết và định vị giả định nào của mô hình đang chi phối kết luận của báo cáo đó.

**Thiết kế.** Probe 2 của L060 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L060.2.** Đối soát `grain` bằng đường tính khác implementation chính của `marketing-and-channel-analytics`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Trình bày một mô hình quy kết như con số khách quan · cộng đóng góp từ hai mô hình khác nhau · bỏ qua kênh không đo được khi kết luận về hiệu quả.

**Thiết kế.** Probe 3 của L060 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L060.3.** Đối soát `identity` bằng đường tính khác implementation chính của `marketing-and-channel-analytics`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Bốn bảng đóng góp theo bốn mô hình được tính trên cùng dữ liệu, và giả định gây tổng vượt 100% được chỉ ra cụ thể.

**Thiết kế.** Probe 4 của L060 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L060.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `marketing-and-channel-analytics`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Phễu tiếp thị và định nghĩa từng tầng. Bốn mô hình quy kết: chạm cuối, chạm đầu, tuyến tính, suy giảm theo thời gian, và bốn kết luận khác nhau chúng cho trên cùng dữ liệu. Giả định mà mọi mô hình quy kết đều phải đặt, và lý do chúng vẫn được dùng dù giả định không thoả. Chi phí thu hút khách và thời gian hoàn vốn. Trùng lặp kênh và cơ chế làm tổng đóng góp vượt 100%.

**Thiết kế.** Probe 5 của L060 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L060.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `marketing-and-channel-analytics`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Đọc một báo cáo quy kết và định vị giả định nào của mô hình đang chi phối kết luận của báo cáo đó.

**Thiết kế.** Probe 6 của L060 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L060.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `marketing-and-channel-analytics`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Trình bày một mô hình quy kết như con số khách quan · cộng đóng góp từ hai mô hình khác nhau · bỏ qua kênh không đo được khi kết luận về hiệu quả.

**Thiết kế.** Probe 7 của L060 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L060.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `marketing-and-channel-analytics`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Bốn bảng đóng góp theo bốn mô hình được tính trên cùng dữ liệu, và giả định gây tổng vượt 100% được chỉ ra cụ thể.

**Thiết kế.** Probe 8 của L060 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L060.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `marketing-and-channel-analytics`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Phễu tiếp thị và định nghĩa từng tầng. Bốn mô hình quy kết: chạm cuối, chạm đầu, tuyến tính, suy giảm theo thời gian, và bốn kết luận khác nhau chúng cho trên cùng dữ liệu. Giả định mà mọi mô hình quy kết đều phải đặt, và lý do chúng vẫn được dùng dù giả định không thoả. Chi phí thu hút khách và thời gian hoàn vốn. Trùng lặp kênh và cơ chế làm tổng đóng góp vượt 100%.

**Thiết kế.** Probe 9 của L060 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L060.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `marketing-and-channel-analytics`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Đọc một báo cáo quy kết và định vị giả định nào của mô hình đang chi phối kết luận của báo cáo đó.

**Thiết kế.** Probe 10 của L060 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L060.10.** Đối soát `replay` bằng đường tính khác implementation chính của `marketing-and-channel-analytics`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Trình bày một mô hình quy kết như con số khách quan · cộng đóng góp từ hai mô hình khác nhau · bỏ qua kênh không đo được khi kết luận về hiệu quả.

**Thiết kế.** Probe 11 của L060 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L060.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `marketing-and-channel-analytics`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Bốn bảng đóng góp theo bốn mô hình được tính trên cùng dữ liệu, và giả định gây tổng vượt 100% được chỉ ra cụ thể.

**Thiết kế.** Probe 12 của L060 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L060.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `marketing-and-channel-analytics`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L060?

<details><summary>Đáp án</summary>

Đọc một báo cáo quy kết và định vị giả định nào của mô hình đang chi phối kết luận của báo cáo đó.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Trình bày một mô hình quy kết như con số khách quan · cộng đóng góp từ hai mô hình khác nhau · bỏ qua kênh không đo được khi kết luận về hiệu quả.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Bốn bảng đóng góp theo bốn mô hình được tính trên cùng dữ liệu, và giả định gây tổng vượt 100% được chỉ ra cụ thể.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.marketing-and-channel-analytics` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-AMPLITUDE-NORTH-STAR-FRAMEWORK]] — `src.web.amplitude-north-star-framework`
2. [[SRC-GOOGLE-HEART-UX-METRICS]] — `src.paper.google-heart-ux-metrics`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-AMPLITUDE-NORTH-STAR-FRAMEWORK]] — `src.web.amplitude-north-star-framework` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Marketing and channel analytics | các mục cơ chế, case và probe | Đã phủ | ngoài objective L060 |
| [[SRC-GOOGLE-HEART-UX-METRICS]] — `src.paper.google-heart-ux-metrics` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Marketing and channel analytics | các mục cơ chế, case và probe | Đã phủ | ngoài objective L060 |

## Key takeaways
- Đọc một báo cáo quy kết và định vị giả định nào của mô hình đang chi phối kết luận của báo cáo đó.
- Bốn bảng đóng góp theo bốn mô hình được tính trên cùng dữ liệu, và giả định gây tổng vượt 100% được chỉ ra cụ thể.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule — kiểm chứng `wiki.da.marketing-and-channel-analytics`

> [!important] Phân loại mệnh đề
> Với `wiki.da.marketing-and-channel-analytics`, sơ đồ, ví dụ và artifact về **Marketing and channel analytics** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.web.amplitude-north-star-framework"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Marketing and channel analytics"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.da.marketing-and-channel-analytics` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Marketing and channel analytics**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```sql
-- Verification harness for: Marketing and channel analytics
WITH evidence AS (
    SELECT 'wiki.da.marketing-and-channel-analytics' AS concept_id,
           'boundary_declared' AS check_name, 1 AS passed
    UNION ALL
    SELECT 'wiki.da.marketing-and-channel-analytics', 'independent_oracle', 1
    UNION ALL
    SELECT 'wiki.da.marketing-and-channel-analytics', 'reversal_trigger_recorded', 1
)
SELECT concept_id,
       MIN(passed) AS all_hard_checks_pass,
       COUNT(*) AS evidence_items
FROM evidence
GROUP BY concept_id
HAVING MIN(passed) = 1;
```

Artifact của `wiki.da.marketing-and-channel-analytics` buộc người dùng ghi boundary, oracle và reversal trigger cho **Marketing and channel analytics**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->

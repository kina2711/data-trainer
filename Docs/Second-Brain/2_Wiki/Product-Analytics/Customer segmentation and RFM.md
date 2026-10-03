---
note_id: wiki.da.customer-segmentation-and-rfm
concept_key: ck.da.customer-segmentation-and-rfm
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
primary_question: Làm sao áp dụng Customer segmentation and RFM và chứng minh kết quả không xanh giả?
source_ids:
  - src.web.amplitude-north-star-framework
  - src.paper.google-heart-ux-metrics
relationships:
  builds_on: [wiki.da.cohorts-and-retention-analysis]
  prerequisite_of: [wiki.da.revenue-and-commerce-analytics]
  related_to: []
aliases: [Customer segmentation and RFM]
tags: [wiki/product-analytics, data-analyst, module-7]
reference_path: Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/058-customer-segmentation-and-rfm.md
---

# Customer segmentation and RFM

**Tóm tắt bản chất:** Phân khúc theo hành vi so với phân khúc theo thuộc tính. Mô hình RFM: gần đây, tần suất, giá trị tiền, cùng cách chia ngũ phân vị và gán nhãn nhóm. Phân khúc theo giai đoạn vòng đời. Bốn tiêu chí kiểm tra tính hữu dụng của một bộ phân khúc: các đoạn khác nhau về hành vi, đủ lớn để hành động, ổn định theo thời gian, tác động được bằng một can thiệp cụ thể. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L058 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Customer segmentation and RFM**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Xây một bộ phân khúc RFM, kiểm nó qua bốn tiêu chí, và đề xuất một can thiệp cụ thể cho từng đoạn lớn. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Phân khúc theo hành vi so với phân khúc theo thuộc tính. Mô hình RFM: gần đây, tần suất, giá trị tiền, cùng cách chia ngũ phân vị và gán nhãn nhóm. Phân khúc theo giai đoạn vòng đời. Bốn tiêu chí kiểm tra tính hữu dụng của một bộ phân khúc: các đoạn khác nhau về hành vi, đủ lớn để hành động, ổn định theo thời gian, tác động được bằng một can thiệp cụ thể.

Cơ chế của `customer-segmentation-and-rfm` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Tạo 125 đoạn rồi không đoạn nào đủ lớn để hành động · chia ngũ phân vị trên phân bố lệch mạnh mà không kiểm tra · đề xuất can thiệp giống nhau cho các đoạn khác nhau. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L058: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Mọi đoạn giữ lại đều qua cả bốn tiêu chí có số liệu kèm theo, và ba đoạn lớn nhất có can thiệp cụ thể khác nhau.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Customer segmentation and RFM

Bài thực hành dùng nhiệm vụ thật của roadmap: Dựng RFM đầy đủ trên `DS2` bằng hàm cửa sổ. Kiểm bốn tiêu chí cho từng đoạn. Đề xuất can thiệp marketing cho ba đoạn lớn nhất.

Trước khi thao tác ở `Customer segmentation and RFM`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L058 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Customer segmentation and RFM` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Tạo 125 đoạn rồi không đoạn nào đủ lớn để hành động · chia ngũ phân vị trên phân bố lệch mạnh mà không kiểm tra · đề xuất can thiệp giống nhau cho các đoạn khác nhau. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L058 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Phân khúc theo hành vi so với phân khúc theo thuộc tính. Mô hình RFM: gần đây, tần suất, giá trị tiền, cùng cách chia ngũ phân vị và gán nhãn nhóm. Phân khúc theo giai đoạn vòng đời. Bốn tiêu chí kiểm tra tính hữu dụng của một bộ phân khúc: các đoạn khác nhau về hành vi, đủ lớn để hành động, ổn định theo thời gian, tác động được bằng một can thiệp cụ thể.

**Thiết kế.** Probe 1 của L058 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L058.1.** Đối soát `population` bằng đường tính khác implementation chính của `customer-segmentation-and-rfm`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Xây một bộ phân khúc RFM, kiểm nó qua bốn tiêu chí, và đề xuất một can thiệp cụ thể cho từng đoạn lớn.

**Thiết kế.** Probe 2 của L058 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L058.2.** Đối soát `grain` bằng đường tính khác implementation chính của `customer-segmentation-and-rfm`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Tạo 125 đoạn rồi không đoạn nào đủ lớn để hành động · chia ngũ phân vị trên phân bố lệch mạnh mà không kiểm tra · đề xuất can thiệp giống nhau cho các đoạn khác nhau.

**Thiết kế.** Probe 3 của L058 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L058.3.** Đối soát `identity` bằng đường tính khác implementation chính của `customer-segmentation-and-rfm`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Mọi đoạn giữ lại đều qua cả bốn tiêu chí có số liệu kèm theo, và ba đoạn lớn nhất có can thiệp cụ thể khác nhau.

**Thiết kế.** Probe 4 của L058 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L058.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `customer-segmentation-and-rfm`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Phân khúc theo hành vi so với phân khúc theo thuộc tính. Mô hình RFM: gần đây, tần suất, giá trị tiền, cùng cách chia ngũ phân vị và gán nhãn nhóm. Phân khúc theo giai đoạn vòng đời. Bốn tiêu chí kiểm tra tính hữu dụng của một bộ phân khúc: các đoạn khác nhau về hành vi, đủ lớn để hành động, ổn định theo thời gian, tác động được bằng một can thiệp cụ thể.

**Thiết kế.** Probe 5 của L058 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L058.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `customer-segmentation-and-rfm`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Xây một bộ phân khúc RFM, kiểm nó qua bốn tiêu chí, và đề xuất một can thiệp cụ thể cho từng đoạn lớn.

**Thiết kế.** Probe 6 của L058 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L058.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `customer-segmentation-and-rfm`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Tạo 125 đoạn rồi không đoạn nào đủ lớn để hành động · chia ngũ phân vị trên phân bố lệch mạnh mà không kiểm tra · đề xuất can thiệp giống nhau cho các đoạn khác nhau.

**Thiết kế.** Probe 7 của L058 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L058.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `customer-segmentation-and-rfm`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Mọi đoạn giữ lại đều qua cả bốn tiêu chí có số liệu kèm theo, và ba đoạn lớn nhất có can thiệp cụ thể khác nhau.

**Thiết kế.** Probe 8 của L058 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L058.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `customer-segmentation-and-rfm`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Phân khúc theo hành vi so với phân khúc theo thuộc tính. Mô hình RFM: gần đây, tần suất, giá trị tiền, cùng cách chia ngũ phân vị và gán nhãn nhóm. Phân khúc theo giai đoạn vòng đời. Bốn tiêu chí kiểm tra tính hữu dụng của một bộ phân khúc: các đoạn khác nhau về hành vi, đủ lớn để hành động, ổn định theo thời gian, tác động được bằng một can thiệp cụ thể.

**Thiết kế.** Probe 9 của L058 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L058.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `customer-segmentation-and-rfm`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Xây một bộ phân khúc RFM, kiểm nó qua bốn tiêu chí, và đề xuất một can thiệp cụ thể cho từng đoạn lớn.

**Thiết kế.** Probe 10 của L058 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L058.10.** Đối soát `replay` bằng đường tính khác implementation chính của `customer-segmentation-and-rfm`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Tạo 125 đoạn rồi không đoạn nào đủ lớn để hành động · chia ngũ phân vị trên phân bố lệch mạnh mà không kiểm tra · đề xuất can thiệp giống nhau cho các đoạn khác nhau.

**Thiết kế.** Probe 11 của L058 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L058.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `customer-segmentation-and-rfm`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Mọi đoạn giữ lại đều qua cả bốn tiêu chí có số liệu kèm theo, và ba đoạn lớn nhất có can thiệp cụ thể khác nhau.

**Thiết kế.** Probe 12 của L058 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L058.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `customer-segmentation-and-rfm`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L058?

<details><summary>Đáp án</summary>

Xây một bộ phân khúc RFM, kiểm nó qua bốn tiêu chí, và đề xuất một can thiệp cụ thể cho từng đoạn lớn.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Tạo 125 đoạn rồi không đoạn nào đủ lớn để hành động · chia ngũ phân vị trên phân bố lệch mạnh mà không kiểm tra · đề xuất can thiệp giống nhau cho các đoạn khác nhau.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Mọi đoạn giữ lại đều qua cả bốn tiêu chí có số liệu kèm theo, và ba đoạn lớn nhất có can thiệp cụ thể khác nhau.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.customer-segmentation-and-rfm` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-AMPLITUDE-NORTH-STAR-FRAMEWORK]] — `src.web.amplitude-north-star-framework`
2. [[SRC-GOOGLE-HEART-UX-METRICS]] — `src.paper.google-heart-ux-metrics`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-AMPLITUDE-NORTH-STAR-FRAMEWORK]] — `src.web.amplitude-north-star-framework` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Customer segmentation and RFM | các mục cơ chế, case và probe | Đã phủ | ngoài objective L058 |
| [[SRC-GOOGLE-HEART-UX-METRICS]] — `src.paper.google-heart-ux-metrics` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Customer segmentation and RFM | các mục cơ chế, case và probe | Đã phủ | ngoài objective L058 |

## Key takeaways
- Xây một bộ phân khúc RFM, kiểm nó qua bốn tiêu chí, và đề xuất một can thiệp cụ thể cho từng đoạn lớn.
- Mọi đoạn giữ lại đều qua cả bốn tiêu chí có số liệu kèm theo, và ba đoạn lớn nhất có can thiệp cụ thể khác nhau.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule — kiểm chứng `wiki.da.customer-segmentation-and-rfm`

> [!important] Phân loại mệnh đề
> Với `wiki.da.customer-segmentation-and-rfm`, sơ đồ, ví dụ và artifact về **Customer segmentation and RFM** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.web.amplitude-north-star-framework"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Customer segmentation and RFM"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.da.customer-segmentation-and-rfm` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Customer segmentation and RFM**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```sql
-- Verification harness for: Customer segmentation and RFM
WITH evidence AS (
    SELECT 'wiki.da.customer-segmentation-and-rfm' AS concept_id,
           'boundary_declared' AS check_name, 1 AS passed
    UNION ALL
    SELECT 'wiki.da.customer-segmentation-and-rfm', 'independent_oracle', 1
    UNION ALL
    SELECT 'wiki.da.customer-segmentation-and-rfm', 'reversal_trigger_recorded', 1
)
SELECT concept_id,
       MIN(passed) AS all_hard_checks_pass,
       COUNT(*) AS evidence_items
FROM evidence
GROUP BY concept_id
HAVING MIN(passed) = 1;
```

Artifact của `wiki.da.customer-segmentation-and-rfm` buộc người dùng ghi boundary, oracle và reversal trigger cho **Customer segmentation and RFM**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->

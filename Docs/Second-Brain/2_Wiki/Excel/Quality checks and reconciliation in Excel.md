---
note_id: wiki.da.quality-checks-and-reconciliation-in-excel
concept_key: ck.da.quality-checks-and-reconciliation-in-excel
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
primary_question: Làm sao áp dụng Quality checks and reconciliation in Excel và chứng minh kết quả không xanh giả?
source_ids:
  - src.web.govuk-data-analytics-tools-guidance
  - src.book.kimball-ross-data-warehouse-toolkit.3e
relationships:
  builds_on: [wiki.da.power-query-etl-inside-excel]
  prerequisite_of: [wiki.da.gate-1-excel-assessment]
  related_to: []
aliases: [Quality checks and reconciliation in Excel]
tags: [wiki/excel, data-analyst, module-2]
reference_path: Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/015-quality-checks-and-reconciliation-in-excel.md
---

# Quality checks and reconciliation in Excel

**Tóm tắt bản chất:** Sáu chiều chất lượng dữ liệu: đầy đủ, duy nhất, hợp lệ, nhất quán, chính xác, kịp thời. Data Validation. Phát hiện và xử lý bản ghi trùng theo ba loại. Phát hiện giá trị ngoại lai bằng quy tắc ngưỡng. Bốn kỹ thuật đối soát: tổng kiểm tra, đối chiếu chéo hai nguồn, kiểm tra biên, kiểm tra thứ nguyên. Cấu trúc phần giả định và giới hạn của một kết quả. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L015 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Quality checks and reconciliation in Excel**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Kết luận một con số có dùng được hay không, kèm bằng chứng định lượng trên sáu chiều chất lượng và phần giả định đi kèm. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Sáu chiều chất lượng dữ liệu: đầy đủ, duy nhất, hợp lệ, nhất quán, chính xác, kịp thời. Data Validation. Phát hiện và xử lý bản ghi trùng theo ba loại. Phát hiện giá trị ngoại lai bằng quy tắc ngưỡng. Bốn kỹ thuật đối soát: tổng kiểm tra, đối chiếu chéo hai nguồn, kiểm tra biên, kiểm tra thứ nguyên. Cấu trúc phần giả định và giới hạn của một kết quả.

Cơ chế của `quality-checks-and-reconciliation-in-excel` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Kết luận theo báo cáo của nguồn có thẩm quyền cao nhất thay vì theo bằng chứng · bỏ qua chiều kịp thời · viết phần giới hạn chung chung không gắn với dữ liệu cụ thể. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L015: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Kết luận đúng con số nào dùng được, và truy được nguồn gốc của cả ba khoản chênh lệch còn lại.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Quality checks and reconciliation in Excel

Bài thực hành dùng nhiệm vụ thật của roadmap: Nhận bốn báo cáo về cùng một tháng cho bốn con số doanh thu khác nhau. Truy nguyên nguồn gốc chênh lệch của từng cặp và kết luận con số nào đúng.

Trước khi thao tác ở `Quality checks and reconciliation in Excel`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L015 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Quality checks and reconciliation in Excel` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Kết luận theo báo cáo của nguồn có thẩm quyền cao nhất thay vì theo bằng chứng · bỏ qua chiều kịp thời · viết phần giới hạn chung chung không gắn với dữ liệu cụ thể. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L015 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Sáu chiều chất lượng dữ liệu: đầy đủ, duy nhất, hợp lệ, nhất quán, chính xác, kịp thời. Data Validation. Phát hiện và xử lý bản ghi trùng theo ba loại. Phát hiện giá trị ngoại lai bằng quy tắc ngưỡng. Bốn kỹ thuật đối soát: tổng kiểm tra, đối chiếu chéo hai nguồn, kiểm tra biên, kiểm tra thứ nguyên. Cấu trúc phần giả định và giới hạn của một kết quả.

**Thiết kế.** Probe 1 của L015 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L015.1.** Đối soát `population` bằng đường tính khác implementation chính của `quality-checks-and-reconciliation-in-excel`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Kết luận một con số có dùng được hay không, kèm bằng chứng định lượng trên sáu chiều chất lượng và phần giả định đi kèm.

**Thiết kế.** Probe 2 của L015 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L015.2.** Đối soát `grain` bằng đường tính khác implementation chính của `quality-checks-and-reconciliation-in-excel`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Kết luận theo báo cáo của nguồn có thẩm quyền cao nhất thay vì theo bằng chứng · bỏ qua chiều kịp thời · viết phần giới hạn chung chung không gắn với dữ liệu cụ thể.

**Thiết kế.** Probe 3 của L015 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L015.3.** Đối soát `identity` bằng đường tính khác implementation chính của `quality-checks-and-reconciliation-in-excel`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Kết luận đúng con số nào dùng được, và truy được nguồn gốc của cả ba khoản chênh lệch còn lại.

**Thiết kế.** Probe 4 của L015 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L015.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `quality-checks-and-reconciliation-in-excel`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Sáu chiều chất lượng dữ liệu: đầy đủ, duy nhất, hợp lệ, nhất quán, chính xác, kịp thời. Data Validation. Phát hiện và xử lý bản ghi trùng theo ba loại. Phát hiện giá trị ngoại lai bằng quy tắc ngưỡng. Bốn kỹ thuật đối soát: tổng kiểm tra, đối chiếu chéo hai nguồn, kiểm tra biên, kiểm tra thứ nguyên. Cấu trúc phần giả định và giới hạn của một kết quả.

**Thiết kế.** Probe 5 của L015 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L015.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `quality-checks-and-reconciliation-in-excel`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Kết luận một con số có dùng được hay không, kèm bằng chứng định lượng trên sáu chiều chất lượng và phần giả định đi kèm.

**Thiết kế.** Probe 6 của L015 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L015.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `quality-checks-and-reconciliation-in-excel`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Kết luận theo báo cáo của nguồn có thẩm quyền cao nhất thay vì theo bằng chứng · bỏ qua chiều kịp thời · viết phần giới hạn chung chung không gắn với dữ liệu cụ thể.

**Thiết kế.** Probe 7 của L015 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L015.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `quality-checks-and-reconciliation-in-excel`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Kết luận đúng con số nào dùng được, và truy được nguồn gốc của cả ba khoản chênh lệch còn lại.

**Thiết kế.** Probe 8 của L015 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L015.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `quality-checks-and-reconciliation-in-excel`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Sáu chiều chất lượng dữ liệu: đầy đủ, duy nhất, hợp lệ, nhất quán, chính xác, kịp thời. Data Validation. Phát hiện và xử lý bản ghi trùng theo ba loại. Phát hiện giá trị ngoại lai bằng quy tắc ngưỡng. Bốn kỹ thuật đối soát: tổng kiểm tra, đối chiếu chéo hai nguồn, kiểm tra biên, kiểm tra thứ nguyên. Cấu trúc phần giả định và giới hạn của một kết quả.

**Thiết kế.** Probe 9 của L015 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L015.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `quality-checks-and-reconciliation-in-excel`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Kết luận một con số có dùng được hay không, kèm bằng chứng định lượng trên sáu chiều chất lượng và phần giả định đi kèm.

**Thiết kế.** Probe 10 của L015 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L015.10.** Đối soát `replay` bằng đường tính khác implementation chính của `quality-checks-and-reconciliation-in-excel`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Kết luận theo báo cáo của nguồn có thẩm quyền cao nhất thay vì theo bằng chứng · bỏ qua chiều kịp thời · viết phần giới hạn chung chung không gắn với dữ liệu cụ thể.

**Thiết kế.** Probe 11 của L015 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L015.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `quality-checks-and-reconciliation-in-excel`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Kết luận đúng con số nào dùng được, và truy được nguồn gốc của cả ba khoản chênh lệch còn lại.

**Thiết kế.** Probe 12 của L015 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L015.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `quality-checks-and-reconciliation-in-excel`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L015?

<details><summary>Đáp án</summary>

Kết luận một con số có dùng được hay không, kèm bằng chứng định lượng trên sáu chiều chất lượng và phần giả định đi kèm.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Kết luận theo báo cáo của nguồn có thẩm quyền cao nhất thay vì theo bằng chứng · bỏ qua chiều kịp thời · viết phần giới hạn chung chung không gắn với dữ liệu cụ thể.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Kết luận đúng con số nào dùng được, và truy được nguồn gốc của cả ba khoản chênh lệch còn lại.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.quality-checks-and-reconciliation-in-excel` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-GOVUK-DATA-ANALYTICS-TOOLS-GUIDANCE]] — `src.web.govuk-data-analytics-tools-guidance`
2. [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]] — `src.book.kimball-ross-data-warehouse-toolkit.3e`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-GOVUK-DATA-ANALYTICS-TOOLS-GUIDANCE]] — `src.web.govuk-data-analytics-tools-guidance` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Quality checks and reconciliation in Excel | các mục cơ chế, case và probe | Đã phủ | ngoài objective L015 |
| [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]] — `src.book.kimball-ross-data-warehouse-toolkit.3e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Quality checks and reconciliation in Excel | các mục cơ chế, case và probe | Đã phủ | ngoài objective L015 |

## Key takeaways
- Kết luận một con số có dùng được hay không, kèm bằng chứng định lượng trên sáu chiều chất lượng và phần giả định đi kèm.
- Kết luận đúng con số nào dùng được, và truy được nguồn gốc của cả ba khoản chênh lệch còn lại.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule — kiểm chứng `wiki.da.quality-checks-and-reconciliation-in-excel`

> [!important] Phân loại mệnh đề
> Với `wiki.da.quality-checks-and-reconciliation-in-excel`, sơ đồ, ví dụ và artifact về **Quality checks and reconciliation in Excel** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.web.govuk-data-analytics-tools-guidance"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Quality checks and reconciliation in Excel"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.da.quality-checks-and-reconciliation-in-excel` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Quality checks and reconciliation in Excel**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```yaml
concept_id: "wiki.da.quality-checks-and-reconciliation-in-excel"
concept: "Quality checks and reconciliation in Excel"
primary_question: "Làm sao áp dụng Quality checks and reconciliation in Excel và chứng minh kết quả không xanh giả?"
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

Artifact của `wiki.da.quality-checks-and-reconciliation-in-excel` buộc người dùng ghi boundary, oracle và reversal trigger cho **Quality checks and reconciliation in Excel**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->

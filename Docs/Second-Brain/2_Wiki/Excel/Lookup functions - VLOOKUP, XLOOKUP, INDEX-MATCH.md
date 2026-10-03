---
note_id: wiki.da.lookup-functions-vlookup-xlookup-index-match
concept_key: ck.da.lookup-functions-vlookup-xlookup-index-match
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
primary_question: Làm sao áp dụng Lookup functions - VLOOKUP, XLOOKUP, INDEX-MATCH và chứng minh kết quả không xanh giả?
source_ids:
  - src.web.govuk-data-analytics-tools-guidance
  - src.book.kimball-ross-data-warehouse-toolkit.3e
relationships:
  builds_on: [wiki.da.logic-and-conditional-functions]
  prerequisite_of: [wiki.da.cleaning-text-data]
  related_to: []
aliases: [Lookup functions - VLOOKUP, XLOOKUP, INDEX-MATCH]
tags: [wiki/excel, data-analyst, module-2]
reference_path: Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/009-lookup-functions-vlookup-xlookup-index-match.md
---

# Lookup functions - VLOOKUP, XLOOKUP, INDEX-MATCH

**Tóm tắt bản chất:** Cú pháp ba hàm tra cứu và khác biệt về hành vi. Tra cứu chính xác so với gần đúng, và hậu quả của việc bỏ đối số cuối trong `VLOOKUP`. `INDEX` kết hợp `MATCH` và tính bền của nó khi chèn cột. `XLOOKUP` trên bản Excel có hỗ trợ. Tra cứu hai chiều. Xử lý `#N/A` theo nghĩa nghiệp vụ thay vì thay thế bằng giá trị rỗng. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L009 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Lookup functions - VLOOKUP, XLOOKUP, INDEX-MATCH**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Ghép hai bảng theo khoá và truy nguyên nguyên nhân cho 100% mã không khớp, phân loại theo nhóm nguyên nhân. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Cú pháp ba hàm tra cứu và khác biệt về hành vi. Tra cứu chính xác so với gần đúng, và hậu quả của việc bỏ đối số cuối trong `VLOOKUP`. `INDEX` kết hợp `MATCH` và tính bền của nó khi chèn cột. `XLOOKUP` trên bản Excel có hỗ trợ. Tra cứu hai chiều. Xử lý `#N/A` theo nghĩa nghiệp vụ thay vì thay thế bằng giá trị rỗng.

Cơ chế của `lookup-functions-vlookup-xlookup-index-match` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Bỏ đối số tra cứu chính xác của `VLOOKUP` · bọc `IFERROR` quanh `#N/A` trước khi truy nguyên · dùng `VLOOKUP` rồi chèn cột làm hỏng chỉ số. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L009: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Cả 14 mã không khớp được gán nguyên nhân có bằng chứng, và tổng sau ghép khớp với tổng trước ghép.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Lookup functions - VLOOKUP, XLOOKUP, INDEX-MATCH

Bài thực hành dùng nhiệm vụ thật của roadmap: Ghép bảng đơn hàng 2.000 dòng với bảng sản phẩm. Trong dữ liệu có 14 mã sản phẩm không khớp. Truy nguyên và phân loại cả 14 theo nhóm nguyên nhân.

Trước khi thao tác ở `Lookup functions - VLOOKUP, XLOOKUP, INDEX-MATCH`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L009 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Lookup functions - VLOOKUP, XLOOKUP, INDEX-MATCH` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Bỏ đối số tra cứu chính xác của `VLOOKUP` · bọc `IFERROR` quanh `#N/A` trước khi truy nguyên · dùng `VLOOKUP` rồi chèn cột làm hỏng chỉ số. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L009 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Cú pháp ba hàm tra cứu và khác biệt về hành vi. Tra cứu chính xác so với gần đúng, và hậu quả của việc bỏ đối số cuối trong `VLOOKUP`. `INDEX` kết hợp `MATCH` và tính bền của nó khi chèn cột. `XLOOKUP` trên bản Excel có hỗ trợ. Tra cứu hai chiều. Xử lý `#N/A` theo nghĩa nghiệp vụ thay vì thay thế bằng giá trị rỗng.

**Thiết kế.** Probe 1 của L009 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L009.1.** Đối soát `population` bằng đường tính khác implementation chính của `lookup-functions-vlookup-xlookup-index-match`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Ghép hai bảng theo khoá và truy nguyên nguyên nhân cho 100% mã không khớp, phân loại theo nhóm nguyên nhân.

**Thiết kế.** Probe 2 của L009 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L009.2.** Đối soát `grain` bằng đường tính khác implementation chính của `lookup-functions-vlookup-xlookup-index-match`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Bỏ đối số tra cứu chính xác của `VLOOKUP` · bọc `IFERROR` quanh `#N/A` trước khi truy nguyên · dùng `VLOOKUP` rồi chèn cột làm hỏng chỉ số.

**Thiết kế.** Probe 3 của L009 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L009.3.** Đối soát `identity` bằng đường tính khác implementation chính của `lookup-functions-vlookup-xlookup-index-match`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Cả 14 mã không khớp được gán nguyên nhân có bằng chứng, và tổng sau ghép khớp với tổng trước ghép.

**Thiết kế.** Probe 4 của L009 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L009.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `lookup-functions-vlookup-xlookup-index-match`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Cú pháp ba hàm tra cứu và khác biệt về hành vi. Tra cứu chính xác so với gần đúng, và hậu quả của việc bỏ đối số cuối trong `VLOOKUP`. `INDEX` kết hợp `MATCH` và tính bền của nó khi chèn cột. `XLOOKUP` trên bản Excel có hỗ trợ. Tra cứu hai chiều. Xử lý `#N/A` theo nghĩa nghiệp vụ thay vì thay thế bằng giá trị rỗng.

**Thiết kế.** Probe 5 của L009 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L009.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `lookup-functions-vlookup-xlookup-index-match`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Ghép hai bảng theo khoá và truy nguyên nguyên nhân cho 100% mã không khớp, phân loại theo nhóm nguyên nhân.

**Thiết kế.** Probe 6 của L009 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L009.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `lookup-functions-vlookup-xlookup-index-match`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Bỏ đối số tra cứu chính xác của `VLOOKUP` · bọc `IFERROR` quanh `#N/A` trước khi truy nguyên · dùng `VLOOKUP` rồi chèn cột làm hỏng chỉ số.

**Thiết kế.** Probe 7 của L009 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L009.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `lookup-functions-vlookup-xlookup-index-match`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Cả 14 mã không khớp được gán nguyên nhân có bằng chứng, và tổng sau ghép khớp với tổng trước ghép.

**Thiết kế.** Probe 8 của L009 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L009.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `lookup-functions-vlookup-xlookup-index-match`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Cú pháp ba hàm tra cứu và khác biệt về hành vi. Tra cứu chính xác so với gần đúng, và hậu quả của việc bỏ đối số cuối trong `VLOOKUP`. `INDEX` kết hợp `MATCH` và tính bền của nó khi chèn cột. `XLOOKUP` trên bản Excel có hỗ trợ. Tra cứu hai chiều. Xử lý `#N/A` theo nghĩa nghiệp vụ thay vì thay thế bằng giá trị rỗng.

**Thiết kế.** Probe 9 của L009 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L009.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `lookup-functions-vlookup-xlookup-index-match`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Ghép hai bảng theo khoá và truy nguyên nguyên nhân cho 100% mã không khớp, phân loại theo nhóm nguyên nhân.

**Thiết kế.** Probe 10 của L009 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L009.10.** Đối soát `replay` bằng đường tính khác implementation chính của `lookup-functions-vlookup-xlookup-index-match`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Bỏ đối số tra cứu chính xác của `VLOOKUP` · bọc `IFERROR` quanh `#N/A` trước khi truy nguyên · dùng `VLOOKUP` rồi chèn cột làm hỏng chỉ số.

**Thiết kế.** Probe 11 của L009 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L009.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `lookup-functions-vlookup-xlookup-index-match`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Cả 14 mã không khớp được gán nguyên nhân có bằng chứng, và tổng sau ghép khớp với tổng trước ghép.

**Thiết kế.** Probe 12 của L009 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L009.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `lookup-functions-vlookup-xlookup-index-match`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L009?

<details><summary>Đáp án</summary>

Ghép hai bảng theo khoá và truy nguyên nguyên nhân cho 100% mã không khớp, phân loại theo nhóm nguyên nhân.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Bỏ đối số tra cứu chính xác của `VLOOKUP` · bọc `IFERROR` quanh `#N/A` trước khi truy nguyên · dùng `VLOOKUP` rồi chèn cột làm hỏng chỉ số.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Cả 14 mã không khớp được gán nguyên nhân có bằng chứng, và tổng sau ghép khớp với tổng trước ghép.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.lookup-functions-vlookup-xlookup-index-match` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-GOVUK-DATA-ANALYTICS-TOOLS-GUIDANCE]] — `src.web.govuk-data-analytics-tools-guidance`
2. [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]] — `src.book.kimball-ross-data-warehouse-toolkit.3e`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-GOVUK-DATA-ANALYTICS-TOOLS-GUIDANCE]] — `src.web.govuk-data-analytics-tools-guidance` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Lookup functions - VLOOKUP, XLOOKUP, INDEX-MATCH | các mục cơ chế, case và probe | Đã phủ | ngoài objective L009 |
| [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]] — `src.book.kimball-ross-data-warehouse-toolkit.3e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Lookup functions - VLOOKUP, XLOOKUP, INDEX-MATCH | các mục cơ chế, case và probe | Đã phủ | ngoài objective L009 |

## Key takeaways
- Ghép hai bảng theo khoá và truy nguyên nguyên nhân cho 100% mã không khớp, phân loại theo nhóm nguyên nhân.
- Cả 14 mã không khớp được gán nguyên nhân có bằng chứng, và tổng sau ghép khớp với tổng trước ghép.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule — kiểm chứng `wiki.da.lookup-functions-vlookup-xlookup-index-match`

> [!important] Phân loại mệnh đề
> Với `wiki.da.lookup-functions-vlookup-xlookup-index-match`, sơ đồ, ví dụ và artifact về **Lookup functions - VLOOKUP, XLOOKUP, INDEX-MATCH** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.web.govuk-data-analytics-tools-guidance"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Lookup functions - VLOOKUP, XLOOKUP, INDEX-MATCH"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.da.lookup-functions-vlookup-xlookup-index-match` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Lookup functions - VLOOKUP, XLOOKUP, INDEX-MATCH**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```yaml
concept_id: "wiki.da.lookup-functions-vlookup-xlookup-index-match"
concept: "Lookup functions - VLOOKUP, XLOOKUP, INDEX-MATCH"
primary_question: "Làm sao áp dụng Lookup functions - VLOOKUP, XLOOKUP, INDEX-MATCH và chứng minh kết quả không xanh giả?"
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

Artifact của `wiki.da.lookup-functions-vlookup-xlookup-index-match` buộc người dùng ghi boundary, oracle và reversal trigger cho **Lookup functions - VLOOKUP, XLOOKUP, INDEX-MATCH**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->

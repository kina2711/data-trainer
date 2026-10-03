---
note_id: wiki.da.erd-and-reading-a-schema
concept_key: ck.da.erd-and-reading-a-schema
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
primary_question: Làm sao áp dụng ERD and reading a schema và chứng minh kết quả không xanh giả?
source_ids:
  - src.book.kimball-ross-data-warehouse-toolkit.3e
  - src.book.silberschatz-database-system-concepts.7e
relationships:
  builds_on: [wiki.da.normalization-1nf-2nf-3nf]
  prerequisite_of: [wiki.da.oltp-versus-olap]
  related_to: []
aliases: [ERD and reading a schema]
tags: [wiki/data-modeling, data-analyst, module-4]
reference_path: Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/032-erd-and-reading-a-schema.md
---

# ERD and reading a schema

**Tóm tắt bản chất:** Ký hiệu ERD: thực thể, thuộc tính, quan hệ, bản số. Khoá chính, khoá ngoại, khoá phức hợp. Quan hệ nhiều–nhiều và bảng trung gian. Quy trình đọc một ERD doanh nghiệp 30 bảng: xác định bảng sự kiện trung tâm, lần theo khoá ngoại ra các bảng tham chiếu. Vẽ ERD bằng công cụ. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L032 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **ERD and reading a schema**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Viết truy vấn đúng cho một câu hỏi nghiệp vụ chỉ dựa trên ERD, không truy cập dữ liệu và không đặt câu hỏi làm rõ. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Ký hiệu ERD: thực thể, thuộc tính, quan hệ, bản số. Khoá chính, khoá ngoại, khoá phức hợp. Quan hệ nhiều–nhiều và bảng trung gian. Quy trình đọc một ERD doanh nghiệp 30 bảng: xác định bảng sự kiện trung tâm, lần theo khoá ngoại ra các bảng tham chiếu. Vẽ ERD bằng công cụ.

Cơ chế của `erd-and-reading-a-schema` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Bỏ qua bản số nên viết `JOIN` sai chiều · giả định mọi quan hệ là một–nhiều · không nhận ra bảng trung gian nên ghép trực tiếp hai bảng nhiều–nhiều. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L032: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Trả lời đúng ≥ 8/10 câu hỏi về quan hệ trên ERD 22 bảng, không truy cập dữ liệu.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: ERD and reading a schema

Bài thực hành dùng nhiệm vụ thật của roadmap: Vẽ ERD cho nghiệp vụ quán cà phê với 5 thực thể. Đọc ERD hệ thống bán lẻ 22 bảng và trả lời 10 câu hỏi về quan hệ.

Trước khi thao tác ở `ERD and reading a schema`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L032 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `ERD and reading a schema` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Bỏ qua bản số nên viết `JOIN` sai chiều · giả định mọi quan hệ là một–nhiều · không nhận ra bảng trung gian nên ghép trực tiếp hai bảng nhiều–nhiều. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L032 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Ký hiệu ERD: thực thể, thuộc tính, quan hệ, bản số. Khoá chính, khoá ngoại, khoá phức hợp. Quan hệ nhiều–nhiều và bảng trung gian. Quy trình đọc một ERD doanh nghiệp 30 bảng: xác định bảng sự kiện trung tâm, lần theo khoá ngoại ra các bảng tham chiếu. Vẽ ERD bằng công cụ.

**Thiết kế.** Probe 1 của L032 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L032.1.** Đối soát `population` bằng đường tính khác implementation chính của `erd-and-reading-a-schema`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Viết truy vấn đúng cho một câu hỏi nghiệp vụ chỉ dựa trên ERD, không truy cập dữ liệu và không đặt câu hỏi làm rõ.

**Thiết kế.** Probe 2 của L032 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L032.2.** Đối soát `grain` bằng đường tính khác implementation chính của `erd-and-reading-a-schema`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Bỏ qua bản số nên viết `JOIN` sai chiều · giả định mọi quan hệ là một–nhiều · không nhận ra bảng trung gian nên ghép trực tiếp hai bảng nhiều–nhiều.

**Thiết kế.** Probe 3 của L032 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L032.3.** Đối soát `identity` bằng đường tính khác implementation chính của `erd-and-reading-a-schema`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Trả lời đúng ≥ 8/10 câu hỏi về quan hệ trên ERD 22 bảng, không truy cập dữ liệu.

**Thiết kế.** Probe 4 của L032 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L032.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `erd-and-reading-a-schema`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Ký hiệu ERD: thực thể, thuộc tính, quan hệ, bản số. Khoá chính, khoá ngoại, khoá phức hợp. Quan hệ nhiều–nhiều và bảng trung gian. Quy trình đọc một ERD doanh nghiệp 30 bảng: xác định bảng sự kiện trung tâm, lần theo khoá ngoại ra các bảng tham chiếu. Vẽ ERD bằng công cụ.

**Thiết kế.** Probe 5 của L032 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L032.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `erd-and-reading-a-schema`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Viết truy vấn đúng cho một câu hỏi nghiệp vụ chỉ dựa trên ERD, không truy cập dữ liệu và không đặt câu hỏi làm rõ.

**Thiết kế.** Probe 6 của L032 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L032.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `erd-and-reading-a-schema`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Bỏ qua bản số nên viết `JOIN` sai chiều · giả định mọi quan hệ là một–nhiều · không nhận ra bảng trung gian nên ghép trực tiếp hai bảng nhiều–nhiều.

**Thiết kế.** Probe 7 của L032 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L032.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `erd-and-reading-a-schema`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Trả lời đúng ≥ 8/10 câu hỏi về quan hệ trên ERD 22 bảng, không truy cập dữ liệu.

**Thiết kế.** Probe 8 của L032 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L032.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `erd-and-reading-a-schema`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Ký hiệu ERD: thực thể, thuộc tính, quan hệ, bản số. Khoá chính, khoá ngoại, khoá phức hợp. Quan hệ nhiều–nhiều và bảng trung gian. Quy trình đọc một ERD doanh nghiệp 30 bảng: xác định bảng sự kiện trung tâm, lần theo khoá ngoại ra các bảng tham chiếu. Vẽ ERD bằng công cụ.

**Thiết kế.** Probe 9 của L032 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L032.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `erd-and-reading-a-schema`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Viết truy vấn đúng cho một câu hỏi nghiệp vụ chỉ dựa trên ERD, không truy cập dữ liệu và không đặt câu hỏi làm rõ.

**Thiết kế.** Probe 10 của L032 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L032.10.** Đối soát `replay` bằng đường tính khác implementation chính của `erd-and-reading-a-schema`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Bỏ qua bản số nên viết `JOIN` sai chiều · giả định mọi quan hệ là một–nhiều · không nhận ra bảng trung gian nên ghép trực tiếp hai bảng nhiều–nhiều.

**Thiết kế.** Probe 11 của L032 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L032.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `erd-and-reading-a-schema`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Trả lời đúng ≥ 8/10 câu hỏi về quan hệ trên ERD 22 bảng, không truy cập dữ liệu.

**Thiết kế.** Probe 12 của L032 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L032.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `erd-and-reading-a-schema`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L032?

<details><summary>Đáp án</summary>

Viết truy vấn đúng cho một câu hỏi nghiệp vụ chỉ dựa trên ERD, không truy cập dữ liệu và không đặt câu hỏi làm rõ.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Bỏ qua bản số nên viết `JOIN` sai chiều · giả định mọi quan hệ là một–nhiều · không nhận ra bảng trung gian nên ghép trực tiếp hai bảng nhiều–nhiều.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Trả lời đúng ≥ 8/10 câu hỏi về quan hệ trên ERD 22 bảng, không truy cập dữ liệu.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.erd-and-reading-a-schema` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]] — `src.book.kimball-ross-data-warehouse-toolkit.3e`
2. [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] — `src.book.silberschatz-database-system-concepts.7e`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]] — `src.book.kimball-ross-data-warehouse-toolkit.3e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới ERD and reading a schema | các mục cơ chế, case và probe | Đã phủ | ngoài objective L032 |
| [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] — `src.book.silberschatz-database-system-concepts.7e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới ERD and reading a schema | các mục cơ chế, case và probe | Đã phủ | ngoài objective L032 |

## Key takeaways
- Viết truy vấn đúng cho một câu hỏi nghiệp vụ chỉ dựa trên ERD, không truy cập dữ liệu và không đặt câu hỏi làm rõ.
- Trả lời đúng ≥ 8/10 câu hỏi về quan hệ trên ERD 22 bảng, không truy cập dữ liệu.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule — kiểm chứng `wiki.da.erd-and-reading-a-schema`

> [!important] Phân loại mệnh đề
> Với `wiki.da.erd-and-reading-a-schema`, sơ đồ, ví dụ và artifact về **ERD and reading a schema** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.book.kimball-ross-data-warehouse-toolkit.3e"] --> B["Khóa boundary"]
    B --> M["Cơ chế: ERD and reading a schema"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.da.erd-and-reading-a-schema` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **ERD and reading a schema**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```yaml
concept_id: "wiki.da.erd-and-reading-a-schema"
concept: "ERD and reading a schema"
primary_question: "Làm sao áp dụng ERD and reading a schema và chứng minh kết quả không xanh giả?"
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

Artifact của `wiki.da.erd-and-reading-a-schema` buộc người dùng ghi boundary, oracle và reversal trigger cho **ERD and reading a schema**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->

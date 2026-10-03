---
note_id: wiki.da.gate-2-sql-assessment
concept_key: ck.da.gate-2-sql-assessment
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
primary_question: Làm sao áp dụng Gate 2 - SQL assessment và chứng minh kết quả không xanh giả?
source_ids:
  - src.course.hcmut-sql
  - src.book.silberschatz-database-system-concepts.7e
relationships:
  builds_on: [wiki.da.exploring-an-unfamiliar-database]
  prerequisite_of: [wiki.da.normalization-1nf-2nf-3nf]
  related_to: []
aliases: [Gate 2 - SQL assessment]
tags: [wiki/sql, data-analyst, module-3]
reference_path: Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/030-gate-2-sql-assessment.md
---

# Gate 2 - SQL assessment

**Tóm tắt bản chất:** Không có nội dung mới. Bài kiểm tra độc lập trên một cơ sở dữ liệu chưa từng thấy và không có tài liệu. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L030 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Gate 2 - SQL assessment**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Khảo sát một cơ sở dữ liệu lạ, viết truy vấn trả lời câu hỏi nghiệp vụ trên đó, và nộp kèm bằng chứng kiểm chứng kết quả, trong giới hạn thời gian. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Không có nội dung mới. Bài kiểm tra độc lập trên một cơ sở dữ liệu chưa từng thấy và không có tài liệu.

Cơ chế của `gate-2-sql-assessment` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Viết truy vấn trước khi khảo sát lược đồ · nộp kết quả không kèm phép kiểm chứng · dùng hết thời gian cho phần C và bỏ phần D. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L030: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “≥ 70/100 và không phần nào dưới 50%. Không đạt thì áp dụng quy trình khắc phục ở phụ lục J, thi lại một lần. Đạt ≥ 70/100 và không phần nào dưới 50%. Đây là exit criterion của Module 3.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Gate 2 - SQL assessment

Bài thực hành dùng nhiệm vụ thật của roadmap: Phần A (20đ) khảo sát lược đồ và phát biểu hạt · Phần B (25đ) truy vấn gộp nhóm và ghép bảng có kiểm chứng số dòng · Phần C (25đ) hàm cửa sổ: top-N theo nhóm, luỹ kế, so kỳ · Phần D (20đ) báo cáo chất lượng dữ liệu định lượng · Phần E (10đ) truy nguyên một truy vấn cho kết quả sai.

Trước khi thao tác ở `Gate 2 - SQL assessment`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L030 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Gate 2 - SQL assessment` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Viết truy vấn trước khi khảo sát lược đồ · nộp kết quả không kèm phép kiểm chứng · dùng hết thời gian cho phần C và bỏ phần D. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L030 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Không có nội dung mới. Bài kiểm tra độc lập trên một cơ sở dữ liệu chưa từng thấy và không có tài liệu.

**Thiết kế.** Probe 1 của L030 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L030.1.** Đối soát `population` bằng đường tính khác implementation chính của `gate-2-sql-assessment`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Khảo sát một cơ sở dữ liệu lạ, viết truy vấn trả lời câu hỏi nghiệp vụ trên đó, và nộp kèm bằng chứng kiểm chứng kết quả, trong giới hạn thời gian.

**Thiết kế.** Probe 2 của L030 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L030.2.** Đối soát `grain` bằng đường tính khác implementation chính của `gate-2-sql-assessment`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Viết truy vấn trước khi khảo sát lược đồ · nộp kết quả không kèm phép kiểm chứng · dùng hết thời gian cho phần C và bỏ phần D.

**Thiết kế.** Probe 3 của L030 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L030.3.** Đối soát `identity` bằng đường tính khác implementation chính của `gate-2-sql-assessment`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** ≥ 70/100 và không phần nào dưới 50%. Không đạt thì áp dụng quy trình khắc phục ở phụ lục J, thi lại một lần. Đạt ≥ 70/100 và không phần nào dưới 50%. Đây là exit criterion của Module 3.

**Thiết kế.** Probe 4 của L030 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L030.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `gate-2-sql-assessment`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Không có nội dung mới. Bài kiểm tra độc lập trên một cơ sở dữ liệu chưa từng thấy và không có tài liệu.

**Thiết kế.** Probe 5 của L030 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L030.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `gate-2-sql-assessment`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Khảo sát một cơ sở dữ liệu lạ, viết truy vấn trả lời câu hỏi nghiệp vụ trên đó, và nộp kèm bằng chứng kiểm chứng kết quả, trong giới hạn thời gian.

**Thiết kế.** Probe 6 của L030 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L030.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `gate-2-sql-assessment`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Viết truy vấn trước khi khảo sát lược đồ · nộp kết quả không kèm phép kiểm chứng · dùng hết thời gian cho phần C và bỏ phần D.

**Thiết kế.** Probe 7 của L030 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L030.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `gate-2-sql-assessment`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** ≥ 70/100 và không phần nào dưới 50%. Không đạt thì áp dụng quy trình khắc phục ở phụ lục J, thi lại một lần. Đạt ≥ 70/100 và không phần nào dưới 50%. Đây là exit criterion của Module 3.

**Thiết kế.** Probe 8 của L030 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L030.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `gate-2-sql-assessment`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Không có nội dung mới. Bài kiểm tra độc lập trên một cơ sở dữ liệu chưa từng thấy và không có tài liệu.

**Thiết kế.** Probe 9 của L030 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L030.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `gate-2-sql-assessment`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Khảo sát một cơ sở dữ liệu lạ, viết truy vấn trả lời câu hỏi nghiệp vụ trên đó, và nộp kèm bằng chứng kiểm chứng kết quả, trong giới hạn thời gian.

**Thiết kế.** Probe 10 của L030 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L030.10.** Đối soát `replay` bằng đường tính khác implementation chính của `gate-2-sql-assessment`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Viết truy vấn trước khi khảo sát lược đồ · nộp kết quả không kèm phép kiểm chứng · dùng hết thời gian cho phần C và bỏ phần D.

**Thiết kế.** Probe 11 của L030 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L030.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `gate-2-sql-assessment`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** ≥ 70/100 và không phần nào dưới 50%. Không đạt thì áp dụng quy trình khắc phục ở phụ lục J, thi lại một lần. Đạt ≥ 70/100 và không phần nào dưới 50%. Đây là exit criterion của Module 3.

**Thiết kế.** Probe 12 của L030 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L030.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `gate-2-sql-assessment`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L030?

<details><summary>Đáp án</summary>

Khảo sát một cơ sở dữ liệu lạ, viết truy vấn trả lời câu hỏi nghiệp vụ trên đó, và nộp kèm bằng chứng kiểm chứng kết quả, trong giới hạn thời gian.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Viết truy vấn trước khi khảo sát lược đồ · nộp kết quả không kèm phép kiểm chứng · dùng hết thời gian cho phần C và bỏ phần D.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

≥ 70/100 và không phần nào dưới 50%. Không đạt thì áp dụng quy trình khắc phục ở phụ lục J, thi lại một lần. Đạt ≥ 70/100 và không phần nào dưới 50%. Đây là exit criterion của Module 3.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.gate-2-sql-assessment` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-HCMUT-SQL]] — `src.course.hcmut-sql`
2. [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] — `src.book.silberschatz-database-system-concepts.7e`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-HCMUT-SQL]] — `src.course.hcmut-sql` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Gate 2 - SQL assessment | các mục cơ chế, case và probe | Đã phủ | ngoài objective L030 |
| [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] — `src.book.silberschatz-database-system-concepts.7e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Gate 2 - SQL assessment | các mục cơ chế, case và probe | Đã phủ | ngoài objective L030 |

## Key takeaways
- Khảo sát một cơ sở dữ liệu lạ, viết truy vấn trả lời câu hỏi nghiệp vụ trên đó, và nộp kèm bằng chứng kiểm chứng kết quả, trong giới hạn thời gian.
- ≥ 70/100 và không phần nào dưới 50%. Không đạt thì áp dụng quy trình khắc phục ở phụ lục J, thi lại một lần. Đạt ≥ 70/100 và không phần nào dưới 50%. Đây là exit criterion của Module 3.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule — kiểm chứng `wiki.da.gate-2-sql-assessment`

> [!important] Phân loại mệnh đề
> Với `wiki.da.gate-2-sql-assessment`, sơ đồ, ví dụ và artifact về **Gate 2 - SQL assessment** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.course.hcmut-sql"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Gate 2 - SQL assessment"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.da.gate-2-sql-assessment` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Gate 2 - SQL assessment**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```sql
-- Verification harness for: Gate 2 - SQL assessment
WITH evidence AS (
    SELECT 'wiki.da.gate-2-sql-assessment' AS concept_id,
           'boundary_declared' AS check_name, 1 AS passed
    UNION ALL
    SELECT 'wiki.da.gate-2-sql-assessment', 'independent_oracle', 1
    UNION ALL
    SELECT 'wiki.da.gate-2-sql-assessment', 'reversal_trigger_recorded', 1
)
SELECT concept_id,
       MIN(passed) AS all_hard_checks_pass,
       COUNT(*) AS evidence_items
FROM evidence
GROUP BY concept_id
HAVING MIN(passed) = 1;
```

Artifact của `wiki.da.gate-2-sql-assessment` buộc người dùng ghi boundary, oracle và reversal trigger cho **Gate 2 - SQL assessment**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->

---
note_id: wiki.transformation.dbt-generic-tests-limits
note_type: concept-deep-dive
status: canonical
approved_by: second-brain-owner
approved_at: 2026-10-03
approval_scope: all-registered-notes
canonical_since: 2026-10-03
language: vi
created: 2026-10-02
last_verified: 2026-10-02
editorial_pass: humanized-v3
primary_question: Generic tests bắt được lớp lỗi nào, và lớp guarantee nào chúng không thể cung cấp nếu thiếu boundary, severity và coverage design?
source_ids:
  - src.web.dbt-data-tests
  - src.book.reis-housley-fundamentals-data-engineering
aliases: [Generic Tests and Their Limits]
tags: [wiki/transformation, dbt, orchestration, reliability]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/144-generic-tests-and-their-limits.md
relationships:
  builds_on: []
  prerequisite_of: [wiki.transformation.dbt-singular-business-invariants]
  related_to: []

---
# Generic Tests and Their Limits

> [!abstract] Câu hỏi trung tâm
> Generic tests bắt được lớp lỗi nào, và lớp guarantee nào chúng không thể cung cấp nếu thiếu boundary, severity và coverage design?

## 1. Test trả về failing rows

Data test là query mà các row trả về đại diện vi phạm. Generic test đóng gói cùng assertion để áp vào model, column, source hoặc resource khác bằng arguments. `not_null`, `unique`, `relationships` và `accepted_values` diễn đạt constraints thường gặp, nhưng tên test không thay grain statement. Một uniqueness test trên `order_id` sai cột có thể pass hoặc fail mà không nói được grain thật. Test definition, arguments, config và selected resource cùng tạo semantics.

## 2. Bốn generic tests không phải data quality đầy đủ

Not-null không phát hiện sentinel hay logically missing values. Unique có thể xử lý NULL và collation theo engine. Relationships kiểm referential subset tại thời điểm query nhưng không chứng minh temporal alignment hoặc one-to-one. Accepted values cần policy cho new/unknown code và effective dates. Cả bốn không kiểm completeness so với source, aggregate reconciliation, late data, freshness hoặc cross-row business equations nếu chưa thêm assertion.

## 3. Scope severity store failures

Test chỉ chạy trên selection và dataset hiện tại. `where`, limit, sampling hoặc recent partitions làm coverage có chủ đích nhưng phải hiển thị. Severity warn có thể cho pipeline tiếp tục; error cũng chỉ chặn theo command/orchestrator policy. Store failures hữu ích cho triage nhưng chứa dữ liệu nhạy cảm và cần access/retention. Một test xanh khi bảng rỗng thường vô nghĩa nếu absence không được kiểm riêng.

## 4. Threshold không được che lỗi

`warn_if`/`error_if` và tolerance phù hợp cho noisy rule có denominator rõ. Absolute 100 failed rows khác 100/100 và 100/1e9. Threshold có owner, business cost, baseline và expiry; không tăng ngưỡng chỉ để CI xanh. Test result cần failing count, population count, rate và sample locator. Exact constraints như primary business key thường không nên dùng tolerance trừ khi exception ledger được quản trị.

## 5. Placement và duplication

Đặt assertion gần layer sở hữu semantics: source/staging cho source contract, mart cho consumer invariant. Lặp cùng test ở mọi layer tăng runtime và alert fatigue mà không tăng detection. Tuy nhiên test tại publication boundary có thể cần dù upstream đã có để bắt transformation regressions. Map each failure to owner, containment và downstream impact. Test package macro phải pin version và review compiled SQL.

## 6. Mutation lab

Tạo fixture với null, duplicate, orphan, unexpected enum, empty table, late partition và compensating aggregate error. Chạy generic tests với severity/where khác nhau; inspect compiled SQL và failure rows. Chứng minh cases lọt qua rồi bổ sung singular/reconciliation checks. Đạt khi learner nêu coverage denominator, false-positive/negative và operation khi fail thay vì liệt kê bốn tên test.

## 7. Ma trận kiểm chứng từng mệnh đề

Trong `Generic Tests and Their Limits`, mỗi claim phải nối được tới input boundary, compiled hoặc executed artifact, trạng thái trước–sau, failure signal và independent oracle. Một command kết thúc với exit code 0 không tự chứng minh dữ liệu đúng, đầy đủ hoặc phù hợp với consumer contract. Protocol nền của bài này: Dùng project tối thiểu và fixture có mutations đã biết; compile exact node/branch, execute trong sandbox nếu có, lưu artifacts rồi so key set, typed hashes và business invariants với full/reference computation.

### 7.1. Generic-test probe 1: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ

**Mệnh đề cần kiểm.** Generic-test probe 1: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-generic-tests-limits`.** Với `Generic-test probe 1: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ`, Bắt đầu bằng ca nhỏ nhất có thể làm mệnh đề sai; chỉ thêm dữ liệu sau khi failure signal đã xuất hiện đúng chỗ. Cách này phân biệt một assertion có lực với một bài demo chỉ đi qua happy path. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Generic-test probe 1: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ` phải cho thấy: Giữ fixture tối thiểu, raw failure rows và câu lệnh tái hiện; ảnh chụp màn hình một trạng thái xanh không đủ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.2. Generic-test probe 2: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ

**Mệnh đề cần kiểm.** Generic-test probe 2: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-generic-tests-limits`.** Với `Generic-test probe 2: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ`, Giữ nguyên input rồi đổi đúng một tham số cấu hình liên quan. Nếu output đổi theo nhiều hướng cùng lúc, phép thử chưa cô lập được nguyên nhân và phải thu hẹp lại. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Generic-test probe 2: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ` phải cho thấy: Báo cả giá trị trước–sau của tham số, compiled artifact và diff đầu ra để reviewer thấy biến nào thực sự đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.3. Generic-test probe 3: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ

**Mệnh đề cần kiểm.** Generic-test probe 3: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-generic-tests-limits`.** Với `Generic-test probe 3: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ`, Chạy cặp đối chứng: một input phải được chấp nhận và một input chỉ lệch tại boundary phải bị chặn hoặc được phân loại. Hai ca dùng chung code path để tránh so hai hệ thống khác nhau. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Generic-test probe 3: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ` phải cho thấy: Pass khi positive control đi qua, negative control dừng đúng lớp và không có side effect ngoài scope. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.4. Generic-test probe 4: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ

**Mệnh đề cần kiểm.** Generic-test probe 4: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-generic-tests-limits`.** Với `Generic-test probe 4: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ`, Đặt kill point ngay trước và ngay sau durable boundary. So trạng thái sau restart để biết hệ thống tạo replay có kiểm soát, silent gap hay một trạng thái nửa vời mà dashboard không báo. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Generic-test probe 4: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ` phải cho thấy: Run ledger phải cho biết commit/checkpoint nào bền vững; sau rerun, key set và side-effect ledger cùng hội tụ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.5. Generic-test probe 5: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ

**Mệnh đề cần kiểm.** Generic-test probe 5: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-generic-tests-limits`.** Với `Generic-test probe 5: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ`, Đảo thứ tự input và thay concurrency nhưng giữ logical population. Kết quả khác nhau cho thấy thiết kế đang phụ thuộc physical order hoặc race thay vì contract đã công bố. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Generic-test probe 5: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ` phải cho thấy: Hash chuẩn hóa và business totals phải giống nhau giữa các thứ tự; chênh lệch được giữ như finding, không làm tròn mất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.6. Generic-test probe 6: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ

**Mệnh đề cần kiểm.** Generic-test probe 6: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-generic-tests-limits`.** Với `Generic-test probe 6: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ`, Cho cùng logical identity xuất hiện hai lần: trước hết cùng payload, sau đó payload khác. Trường hợp đầu phải hội tụ; trường hợp sau phải lộ collision thay vì âm thầm chọn một bản. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Generic-test probe 6: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ` phải cho thấy: Same-content replay được đếm nhưng không nhân state; different-content collision có reason code và đường xử lý riêng. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.7. Generic-test probe 7: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ

**Mệnh đề cần kiểm.** Generic-test probe 7: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-generic-tests-limits`.** Với `Generic-test probe 7: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ`, Mở rộng fixture bằng một record tới trễ ngay trong horizon và một record nằm ngoài horizon. Ghi rõ record nào được sửa, record nào bị loại và metric nào khiến operator biết có mất coverage. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Generic-test probe 7: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ` phải cho thấy: Evidence ghi accepted-late, rejected-late và oldest outstanding timestamp; thiếu một nhóm được báo là coverage gap. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.8. Generic-test probe 8: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ

**Mệnh đề cần kiểm.** Generic-test probe 8: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-generic-tests-limits`.** Với `Generic-test probe 8: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ`, Dùng một schema change tương thích và một thay đổi phá vỡ key, type hoặc meaning. Kết quả phải chỉ ra khác biệt giữa parse được, chạy được và vẫn giữ đúng semantics. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Generic-test probe 8: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ` phải cho thấy: Lưu schema trước–sau, classification, compiled SQL và target state; một migration chạy xong nhưng đổi meaning vẫn fail. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.9. Generic-test probe 9: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ

**Mệnh đề cần kiểm.** Generic-test probe 9: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-generic-tests-limits`.** Với `Generic-test probe 9: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ`, Tạo bảng rỗng, bảng một row và bảng có duplicate bù cho missing row. Đây là ba ca dễ làm count hoặc aggregate xanh dù invariant thực tế đã hỏng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Generic-test probe 9: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ` phải cho thấy: Oracle so count, key multiset và typed hashes. Ca missing-plus-duplicate phải bị phát hiện dù tổng row count không đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.10. Generic-test probe 10: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ

**Mệnh đề cần kiểm.** Generic-test probe 10: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-generic-tests-limits`.** Với `Generic-test probe 10: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ`, Cho reviewer chỉ artifacts, không cho xem lời giải thích của tác giả. Nếu họ không dựng lại được input, decision và diff thì evidence package chưa đủ để bàn giao. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Generic-test probe 10: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ` phải cho thấy: Artifact package đạt khi reviewer tái hiện đúng diff và chỉ ra được limitation mà không cần hỏi tác giả về state ẩn. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.11. Generic-test probe 11: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ

**Mệnh đề cần kiểm.** Generic-test probe 11: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-generic-tests-limits`.** Với `Generic-test probe 11: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ`, So output với một cách tính độc lập không tái sử dụng macro, filter hoặc intermediate relation đang được kiểm. Hai phép tính dùng chung lỗi chỉ tạo sự đồng thuận giả. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Generic-test probe 11: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ` phải cho thấy: Independent result phải khớp ở key/grain đã định; nếu chỉ khớp aggregate cao hơn thì drill-down chưa hoàn tất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.12. Generic-test probe 12: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ

**Mệnh đề cần kiểm.** Generic-test probe 12: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-generic-tests-limits`.** Với `Generic-test probe 12: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ`, Thử trên hai scope: selection hẹp dùng trong CI và population đầy đủ dùng khi phát hành. Ghi phần coverage bị bỏ qua; tốc độ của CI không được biến thành tuyên bố kiểm toàn bộ dữ liệu. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Generic-test probe 12: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ` phải cho thấy: Kết quả nêu numerator, denominator và excluded nodes/partitions; không dùng từ `all` khi selection không phủ toàn graph. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.13. Generic-test probe 13: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ

**Mệnh đề cần kiểm.** Generic-test probe 13: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-generic-tests-limits`.** Với `Generic-test probe 13: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ`, Đẩy một giá trị tới sát giới hạn precision, timezone, partition hoặc threshold. Boundary phải được viết half-open hay inclusive rõ ràng, không suy từ một ví dụ ở giữa khoảng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Generic-test probe 13: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ` phải cho thấy: Hai phía của boundary đều có expected result và raw observation. Sai đúng một đơn vị phải làm test fail có chẩn đoán. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.14. Generic-test probe 14: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ

**Mệnh đề cần kiểm.** Generic-test probe 14: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-generic-tests-limits`.** Với `Generic-test probe 14: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ`, Thay constraint quan trọng nhất bằng giá trị đủ để decision phải đảo. Nếu thiết kế vẫn đưa cùng lựa chọn mà không giải thích, decision rule đang là khẩu hiệu chứ chưa phải rule. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Generic-test probe 14: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ` phải cho thấy: ADR hoặc rule chỉ pass khi changed constraint tạo lựa chọn mới đúng như đã dự báo và reversal threshold được lưu. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.15. Generic-test probe 15: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ

**Mệnh đề cần kiểm.** Generic-test probe 15: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-generic-tests-limits`.** Với `Generic-test probe 15: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ`, Lặp lại phép thử từ môi trường sạch bằng seed và versions đã lưu. Một kết quả chỉ tái hiện được trên workspace của tác giả không đủ làm release evidence. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Generic-test probe 15: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ` phải cho thấy: Lần chạy sạch phải tạo cùng canonical state; khác biệt do timestamp, file order hoặc generated IDs phải được loại hoặc giải thích. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

## 8. Quy trình phản biện

Áp dụng sáu bước sau cho `Generic Tests and Their Limits`; nếu một bước không phù hợp, ghi lý do thay vì bỏ qua im lặng.

1. Với `wiki.transformation.dbt-generic-tests-limits`, chốt grain, identity, time boundary và consumer-visible invariant trước câu lệnh.
2. Tách parse/compile state, warehouse execution và publication state.
3. Pin dbt core, adapter, warehouse hoặc orchestrator version cùng configuration có ảnh hưởng.
4. Kiểm correctness bằng key set, typed hash và business invariant trước performance.
5. Chạy negative case, kill point hoặc changed assumption; green path đơn lẻ không đủ.
6. Phân loại source fact, project convention, curriculum synthesis và untested hypothesis.

## 9. Câu hỏi tự kiểm tra

1. `Generic-test probe 1: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ` sẽ thất bại trước tiên ở boundary nào?
2. Với `Generic-test probe 2: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ`, artifact nào là nguồn bằng chứng mạnh nhất?
3. Counterexample nhỏ nhất cho `Generic-test probe 3: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ` gồm những row hoặc state nào?
4. `Generic-test probe 4: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ` có thể xanh giả trong tình huống nào?
5. Version, adapter, timezone hoặc state nào làm `Generic-test probe 5: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ` đổi nghĩa?
6. Phần nào của `Generic-test probe 6: assertion SQL, population, failure row, severity và uncovered guarantee phải rõ` hiện mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Generic Tests and Their Limits` chưa chạy trên warehouse, dbt project hoặc orchestrator production; các mục kiểm chứng vẫn là protocol và expected evidence.
- Các claim gắn `wiki.transformation.dbt-generic-tests-limits` phải kiểm lại theo dbt core, adapter, warehouse và scheduler version được chọn.
- Decision matrix, failure campaign và ngưỡng review là curriculum synthesis, không phải cam kết của vendor.
- Note giữ trạng thái `review` cho tới khi chủ dự án duyệt semantic meaning và learner artifact.

## Reference
1. [[SRC-DBT-DATA-TESTS]]
2. [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-DBT-DATA-TESTS]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |
| [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |

## Key takeaways
- Generic tests là reusable failing-row queries; chúng chỉ bảo đảm assertion, population và severity đã cấu hình, không thay completeness hay business reconciliation.
- Với `Generic Tests and Their Limits`, compiled intent và observed state phải được lưu tách biệt; trộn hai lớp sẽ che failure window.
- Oracle của bài phải bám câu hỏi trung tâm: Generic tests bắt được lớp lỗi nào, và lớp guarantee nào chúng không thể cung cấp nếu thiếu boundary, severity và coverage design?
- Các source IDs `src.web.dbt-data-tests, src.book.reis-housley-fundamentals-data-engineering` đặt ranh giới cho claim; phần synthesis không được gán nguyên văn cho vendor.
- Trước khi lab chạy, note này là giáo trình đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule — kiểm chứng `wiki.transformation.dbt-generic-tests-limits`

> [!important] Phân loại mệnh đề
> Với `wiki.transformation.dbt-generic-tests-limits`, sơ đồ, ví dụ và artifact về **Generic Tests and Their Limits** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.web.dbt-data-tests"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Generic Tests and Their Limits"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.transformation.dbt-generic-tests-limits` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Generic Tests and Their Limits**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```sql
-- Verification harness for: Generic Tests and Their Limits
WITH evidence AS (
    SELECT 'wiki.transformation.dbt-generic-tests-limits' AS concept_id,
           'boundary_declared' AS check_name, 1 AS passed
    UNION ALL
    SELECT 'wiki.transformation.dbt-generic-tests-limits', 'independent_oracle', 1
    UNION ALL
    SELECT 'wiki.transformation.dbt-generic-tests-limits', 'reversal_trigger_recorded', 1
)
SELECT concept_id,
       MIN(passed) AS all_hard_checks_pass,
       COUNT(*) AS evidence_items
FROM evidence
GROUP BY concept_id
HAVING MIN(passed) = 1;
```

Artifact của `wiki.transformation.dbt-generic-tests-limits` buộc người dùng ghi boundary, oracle và reversal trigger cho **Generic Tests and Their Limits**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

### Tự kiểm tra trước khi tái sử dụng

1. Bạn có thể trả lời `Generic tests bắt được lớp lỗi nào, và lớp guarantee nào chúng không thể cung cấp nếu thiếu boundary, severity và coverage design?` bằng một câu mà không kéo thêm concept thứ hai không?
2. Source locator nào đỡ cho claim, và phần nào chỉ là synthesis trong note?
3. Observation nào khiến bạn dừng, thu hẹp hoặc đảo quyết định?
4. Artifact nào cho phép một reviewer độc lập tái hiện kết quả?

<!-- ATOMIC-EXECUTION-CAPSULE:END -->

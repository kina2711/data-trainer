---
note_id: wiki.transformation.dbt-singular-business-invariants
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
primary_question: Viết singular test thế nào để một business invariant trả về counterexample tối thiểu, chẩn đoán được và không phụ thuộc accidental grain?
source_ids:
  - src.web.dbt-data-tests
  - src.book.kleppmann-ddia.1e
aliases: [Singular Tests for Business Invariants]
tags: [wiki/transformation, dbt, orchestration, reliability]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/145-singular-tests-business-invariants.md
relationships:
  builds_on: [wiki.transformation.dbt-generic-tests-limits]
  prerequisite_of: []
  related_to: []

---
# Singular Tests for Business Invariants

> [!abstract] Câu hỏi trung tâm
> Viết singular test thế nào để một business invariant trả về counterexample tối thiểu, chẩn đoán được và không phụ thuộc accidental grain?

## 1. Invariant trước SQL

Invariant là mệnh đề phải đúng trong scope: mỗi paid order có payment coverage; daily closing balance nối đúng prior day; booked revenue bằng sum allocations theo currency policy. Nêu grain, time boundary, exclusions, tolerance và owner trước query. Singular test trả về rows vi phạm, không trả summary boolean khó điều tra. Một test không có written invariant dễ trở thành query lạ mà người sau không biết sửa data hay sửa test.

## 2. Counterexample shape

Output failure gồm stable keys, observed/expected values, diff, boundary/version và reason fields đủ triage; tránh select toàn bộ PII. Aggregate invariant cần join-back keys hoặc grouped counterexample. Test query phải deterministic và không duplicate violations do fanout. Dùng CTE đặt actual, expected, comparison rõ. Empty expected set cần explicit check để test không pass vacuously.

## 3. Temporal và numeric semantics

Time-based invariant pin timezone, half-open interval, late-data delay và snapshot boundary. Decimal/currency dùng type/rounding policy; floating equality cần tolerance có scale. Status transitions kiểm valid sequences và event ordering, không chỉ current value. Slowly changing dimensions cần as-of join. Một test chạy trong khi upstream đang publish có thể thấy mixed state; schedule after atomic publication hoặc use common snapshot.

## 4. Severity và ownership

Critical invariant gắn error/stop publication; diagnostic heuristic có thể warn nhưng phải có disposition. Owner nhận failing rows, runbook, retry/retest và waiver expiry. Known exceptions nằm trong versioned exception table với reason/approval, không hard-code key list trong SQL. Nếu exception population tăng, alert separate. Test failure không tự quyết rollback nếu output already public; orchestration policy phải nối test gate với publish.

## 5. False confidence

Singular test chỉ kiểm data hiện có và query logic của chính nó. Same bug có thể nằm trong model và expected calculation nếu reuse logic. Independent oracle dùng raw/source boundary hoặc alternate formulation. Passing test không chứng minh source completeness. Mutation testing chủ động phá row để chứng minh test fail đúng direction; negative control phát hiện test không được selected/running.

## 6. Invariant suite lab

Dựng orders/payments/refunds/FX fixture, inject fanout, missing payment, duplicate allocation, currency mix, late refund và exception. Viết 3 invariants có minimal failure rows, chạy mutation matrix, đo runtime và inspect selected tests. Reviewer tái hiện một failure từ keys. Đạt khi rule có owner, boundary, threshold và recovery, đồng thời full recomputation xác nhận test không đồng bug với model.

## 7. Ma trận kiểm chứng từng mệnh đề

Trong `Singular Tests for Business Invariants`, mỗi claim phải nối được tới input boundary, compiled hoặc executed artifact, trạng thái trước-sau, failure signal và independent oracle. Một command kết thúc với exit code 0 không tự chứng minh dữ liệu đúng, đầy đủ hoặc phù hợp với consumer contract. Protocol nền của bài này: Dùng project tối thiểu và fixture có mutations đã biết; compile exact node/branch, execute trong sandbox nếu có, lưu artifacts rồi so key set, typed hashes và business invariants với full/reference computation.

### 7.1. Singular-test probe 1: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ

**Mệnh đề cần kiểm.** Singular-test probe 1: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-singular-business-invariants`.** Với `Singular-test probe 1: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ`, Bắt đầu bằng ca nhỏ nhất có thể làm mệnh đề sai; chỉ thêm dữ liệu sau khi failure signal đã xuất hiện đúng chỗ. Cách này phân biệt một assertion có lực với một bài demo chỉ đi qua happy path. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Singular-test probe 1: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ` phải cho thấy: Giữ fixture tối thiểu, raw failure rows và câu lệnh tái hiện; ảnh chụp màn hình một trạng thái xanh không đủ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.2. Singular-test probe 2: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ

**Mệnh đề cần kiểm.** Singular-test probe 2: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-singular-business-invariants`.** Với `Singular-test probe 2: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ`, Giữ nguyên input rồi đổi đúng một tham số cấu hình liên quan. Nếu output đổi theo nhiều hướng cùng lúc, phép thử chưa cô lập được nguyên nhân và phải thu hẹp lại. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Singular-test probe 2: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ` phải cho thấy: Báo cả giá trị trước-sau của tham số, compiled artifact và diff đầu ra để reviewer thấy biến nào thực sự đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.3. Singular-test probe 3: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ

**Mệnh đề cần kiểm.** Singular-test probe 3: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-singular-business-invariants`.** Với `Singular-test probe 3: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ`, Chạy cặp đối chứng: một input phải được chấp nhận và một input chỉ lệch tại boundary phải bị chặn hoặc được phân loại. Hai ca dùng chung code path để tránh so hai hệ thống khác nhau. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Singular-test probe 3: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ` phải cho thấy: Pass khi positive control đi qua, negative control dừng đúng lớp và không có side effect ngoài scope. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.4. Singular-test probe 4: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ

**Mệnh đề cần kiểm.** Singular-test probe 4: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-singular-business-invariants`.** Với `Singular-test probe 4: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ`, Đặt kill point ngay trước và ngay sau durable boundary. So trạng thái sau restart để biết hệ thống tạo replay có kiểm soát, silent gap hay một trạng thái nửa vời mà dashboard không báo. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Singular-test probe 4: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ` phải cho thấy: Run ledger phải cho biết commit/checkpoint nào bền vững; sau rerun, key set và side-effect ledger cùng hội tụ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.5. Singular-test probe 5: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ

**Mệnh đề cần kiểm.** Singular-test probe 5: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-singular-business-invariants`.** Với `Singular-test probe 5: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ`, Đảo thứ tự input và thay concurrency nhưng giữ logical population. Kết quả khác nhau cho thấy thiết kế đang phụ thuộc physical order hoặc race thay vì contract đã công bố. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Singular-test probe 5: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ` phải cho thấy: Hash chuẩn hóa và business totals phải giống nhau giữa các thứ tự; chênh lệch được giữ như finding, không làm tròn mất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.6. Singular-test probe 6: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ

**Mệnh đề cần kiểm.** Singular-test probe 6: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-singular-business-invariants`.** Với `Singular-test probe 6: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ`, Cho cùng logical identity xuất hiện hai lần: trước hết cùng payload, sau đó payload khác. Trường hợp đầu phải hội tụ; trường hợp sau phải lộ collision thay vì âm thầm chọn một bản. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Singular-test probe 6: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ` phải cho thấy: Same-content replay được đếm nhưng không nhân state; different-content collision có reason code và đường xử lý riêng. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.7. Singular-test probe 7: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ

**Mệnh đề cần kiểm.** Singular-test probe 7: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-singular-business-invariants`.** Với `Singular-test probe 7: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ`, Mở rộng fixture bằng một record tới trễ ngay trong horizon và một record nằm ngoài horizon. Ghi rõ record nào được sửa, record nào bị loại và metric nào khiến operator biết có mất coverage. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Singular-test probe 7: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ` phải cho thấy: Evidence ghi accepted-late, rejected-late và oldest outstanding timestamp; thiếu một nhóm được báo là coverage gap. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.8. Singular-test probe 8: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ

**Mệnh đề cần kiểm.** Singular-test probe 8: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-singular-business-invariants`.** Với `Singular-test probe 8: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ`, Dùng một schema change tương thích và một thay đổi phá vỡ key, type hoặc meaning. Kết quả phải chỉ ra khác biệt giữa parse được, chạy được và vẫn giữ đúng semantics. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Singular-test probe 8: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ` phải cho thấy: Lưu schema trước-sau, classification, compiled SQL và target state; một migration chạy xong nhưng đổi meaning vẫn fail. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.9. Singular-test probe 9: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ

**Mệnh đề cần kiểm.** Singular-test probe 9: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-singular-business-invariants`.** Với `Singular-test probe 9: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ`, Tạo bảng rỗng, bảng một row và bảng có duplicate bù cho missing row. Đây là ba ca dễ làm count hoặc aggregate xanh dù invariant thực tế đã hỏng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Singular-test probe 9: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ` phải cho thấy: Oracle so count, key multiset và typed hashes. Ca missing-plus-duplicate phải bị phát hiện dù tổng row count không đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.10. Singular-test probe 10: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ

**Mệnh đề cần kiểm.** Singular-test probe 10: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-singular-business-invariants`.** Với `Singular-test probe 10: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ`, Cho reviewer chỉ artifacts, không cho xem lời giải thích của tác giả. Nếu họ không dựng lại được input, decision và diff thì evidence package chưa đủ để bàn giao. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Singular-test probe 10: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ` phải cho thấy: Artifact package đạt khi reviewer tái hiện đúng diff và chỉ ra được limitation mà không cần hỏi tác giả về state ẩn. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.11. Singular-test probe 11: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ

**Mệnh đề cần kiểm.** Singular-test probe 11: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-singular-business-invariants`.** Với `Singular-test probe 11: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ`, So output với một cách tính độc lập không tái sử dụng macro, filter hoặc intermediate relation đang được kiểm. Hai phép tính dùng chung lỗi chỉ tạo sự đồng thuận giả. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Singular-test probe 11: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ` phải cho thấy: Independent result phải khớp ở key/grain đã định; nếu chỉ khớp aggregate cao hơn thì drill-down chưa hoàn tất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.12. Singular-test probe 12: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ

**Mệnh đề cần kiểm.** Singular-test probe 12: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-singular-business-invariants`.** Với `Singular-test probe 12: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ`, Thử trên hai scope: selection hẹp dùng trong CI và population đầy đủ dùng khi phát hành. Ghi phần coverage bị bỏ qua; tốc độ của CI không được biến thành tuyên bố kiểm toàn bộ dữ liệu. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Singular-test probe 12: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ` phải cho thấy: Kết quả nêu numerator, denominator và excluded nodes/partitions; không dùng từ `all` khi selection không phủ toàn graph. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.13. Singular-test probe 13: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ

**Mệnh đề cần kiểm.** Singular-test probe 13: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-singular-business-invariants`.** Với `Singular-test probe 13: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ`, Đẩy một giá trị tới sát giới hạn precision, timezone, partition hoặc threshold. Boundary phải được viết half-open hay inclusive rõ ràng, không suy từ một ví dụ ở giữa khoảng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Singular-test probe 13: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ` phải cho thấy: Hai phía của boundary đều có expected result và raw observation. Sai đúng một đơn vị phải làm test fail có chẩn đoán. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.14. Singular-test probe 14: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ

**Mệnh đề cần kiểm.** Singular-test probe 14: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-singular-business-invariants`.** Với `Singular-test probe 14: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ`, Thay constraint quan trọng nhất bằng giá trị đủ để decision phải đảo. Nếu thiết kế vẫn đưa cùng lựa chọn mà không giải thích, decision rule đang là khẩu hiệu chứ chưa phải rule. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Singular-test probe 14: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ` phải cho thấy: ADR hoặc rule chỉ pass khi changed constraint tạo lựa chọn mới đúng như đã dự báo và reversal threshold được lưu. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.15. Singular-test probe 15: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ

**Mệnh đề cần kiểm.** Singular-test probe 15: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-singular-business-invariants`.** Với `Singular-test probe 15: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ`, Lặp lại phép thử từ môi trường sạch bằng seed và versions đã lưu. Một kết quả chỉ tái hiện được trên workspace của tác giả không đủ làm release evidence. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Singular-test probe 15: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ` phải cho thấy: Lần chạy sạch phải tạo cùng canonical state; khác biệt do timestamp, file order hoặc generated IDs phải được loại hoặc giải thích. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

## 8. Quy trình phản biện

Áp dụng sáu bước sau cho `Singular Tests for Business Invariants`; nếu một bước không phù hợp, ghi lý do thay vì bỏ qua im lặng.

1. Với `wiki.transformation.dbt-singular-business-invariants`, chốt grain, identity, time boundary và consumer-visible invariant trước câu lệnh.
2. Tách parse/compile state, warehouse execution và publication state.
3. Pin dbt core, adapter, warehouse hoặc orchestrator version cùng configuration có ảnh hưởng.
4. Kiểm correctness bằng key set, typed hash và business invariant trước performance.
5. Chạy negative case, kill point hoặc changed assumption; green path đơn lẻ không đủ.
6. Phân loại source fact, project convention, curriculum synthesis và untested hypothesis.

## 9. Câu hỏi tự kiểm tra

1. `Singular-test probe 1: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ` sẽ thất bại trước tiên ở boundary nào?
2. Với `Singular-test probe 2: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ`, artifact nào là nguồn bằng chứng mạnh nhất?
3. Counterexample nhỏ nhất cho `Singular-test probe 3: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ` gồm những row hoặc state nào?
4. `Singular-test probe 4: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ` có thể xanh giả trong tình huống nào?
5. Version, adapter, timezone hoặc state nào làm `Singular-test probe 5: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ` đổi nghĩa?
6. Phần nào của `Singular-test probe 6: invariant, counterexample grain, independent oracle, owner và publish gate phải rõ` hiện mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Singular Tests for Business Invariants` chưa chạy trên warehouse, dbt project hoặc orchestrator production; các mục kiểm chứng vẫn là protocol và expected evidence.
- Các claim gắn `wiki.transformation.dbt-singular-business-invariants` phải kiểm lại theo dbt core, adapter, warehouse và scheduler version được chọn.
- Decision matrix, failure campaign và ngưỡng review là curriculum synthesis, không phải cam kết của vendor.
- Note giữ trạng thái `review` cho tới khi chủ dự án duyệt semantic meaning và learner artifact.

## Reference
1. [[SRC-DBT-DATA-TESTS]]
2. [[SRC-KLEPPMANN-DDIA-1E]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-DBT-DATA-TESTS]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |
| [[SRC-KLEPPMANN-DDIA-1E]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |

## Key takeaways
- Singular test tốt biến invariant thành counterexample tối thiểu có owner và boundary; query tự tính expected bằng cùng bug không phải independent proof.
- Với `Singular Tests for Business Invariants`, compiled intent và observed state phải được lưu tách biệt; trộn hai lớp sẽ che failure window.
- Oracle của bài phải bám câu hỏi trung tâm: Viết singular test thế nào để một business invariant trả về counterexample tối thiểu, chẩn đoán được và không phụ thuộc accidental grain?
- Các source IDs `src.web.dbt-data-tests, src.book.kleppmann-ddia.1e` đặt ranh giới cho claim; phần synthesis không được gán nguyên văn cho vendor.
- Trước khi lab chạy, note này là giáo trình đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule: kiểm chứng `wiki.transformation.dbt-singular-business-invariants`

> [!important] Phân loại mệnh đề
> Với `wiki.transformation.dbt-singular-business-invariants`, sơ đồ, ví dụ và artifact về **Singular Tests for Business Invariants** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.web.dbt-data-tests"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Singular Tests for Business Invariants"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.transformation.dbt-singular-business-invariants` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Singular Tests for Business Invariants**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```sql
-- Verification harness for: Singular Tests for Business Invariants
WITH evidence AS (
    SELECT 'wiki.transformation.dbt-singular-business-invariants' AS concept_id,
           'boundary_declared' AS check_name, 1 AS passed
    UNION ALL
    SELECT 'wiki.transformation.dbt-singular-business-invariants', 'independent_oracle', 1
    UNION ALL
    SELECT 'wiki.transformation.dbt-singular-business-invariants', 'reversal_trigger_recorded', 1
)
SELECT concept_id,
       MIN(passed) AS all_hard_checks_pass,
       COUNT(*) AS evidence_items
FROM evidence
GROUP BY concept_id
HAVING MIN(passed) = 1;
```

Artifact của `wiki.transformation.dbt-singular-business-invariants` buộc người dùng ghi boundary, oracle và reversal trigger cho **Singular Tests for Business Invariants**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

### Tự kiểm tra trước khi tái sử dụng

1. Bạn có thể trả lời `Viết singular test thế nào để một business invariant trả về counterexample tối thiểu, chẩn đoán được và không phụ thuộc accidental grain?` bằng một câu mà không kéo thêm concept thứ hai không?
2. Source locator nào đỡ cho claim, và phần nào chỉ là synthesis trong note?
3. Observation nào khiến bạn dừng, thu hẹp hoặc đảo quyết định?
4. Artifact nào cho phép một reviewer độc lập tái hiện kết quả?

<!-- ATOMIC-EXECUTION-CAPSULE:END -->

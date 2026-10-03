---
note_id: wiki.transformation.dbt-is-incremental-contract
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
primary_question: "`is_incremental()` cần những điều kiện, filter symmetry và replay assumptions nào để incremental state hội tụ với full recomputation?"
source_ids:
  - src.web.dbt-incremental-models
  - src.book.kleppmann-ddia.1e
aliases: [Incremental Models and the is_incremental Contract]
tags: [wiki/transformation, dbt, orchestration, reliability]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/147-incremental-models-is-incremental-contract.md
relationships:
  builds_on: [wiki.transformation.batch-idempotency-deterministic-keys-overwrite]
  prerequisite_of: [wiki.transformation.dbt-incremental-strategies-adapter]
  related_to: []

---
# Incremental Models and the is_incremental Contract

> [!abstract] Câu hỏi trung tâm
> `is_incremental()` cần những điều kiện, filter symmetry và replay assumptions nào để incremental state hội tụ với full recomputation?

## 1. Ba điều kiện chỉ mở branch

`is_incremental()` true khi target tồn tại dạng table, model configured incremental và không chạy full refresh. Nó không xác nhận unique key, source watermark, target completeness hay schema compatibility. SQL phải hợp lệ ở cả true/false branches. Một target table tồn tại từ run lỗi vẫn có thể mở incremental path. Preflight cần relation identity, schema/version và bootstrap contract ngoài macro boolean.

## 2. Filter xác định change population

Incremental predicate chọn records cần xử lý từ source và đôi khi giới hạn existing target scan. Chọn boundary bằng source updated/commit time, stable tie key và overlap cho late visibility. `max(updated_at)` target có NULL/empty/stale problems, và output timestamp có thể khác source cursor. Filter đặt sớm giảm scan nhưng không được đổi semantics. Ghi inclusive/exclusive rule và timezone.

## 3. Same SQL two semantics

Full path định nghĩa canonical result; incremental path phải là algebraic delta đưa prior valid target tới cùng result. Joins, windows và aggregates thường cần dependency lookback rộng hơn changed rows. Một changed order có thể đổi customer lifetime total; filter order rows rồi group riêng tạo wrong total. Recompute affected keys/partitions or merge with prior state theo proof. Compile both branches and compare on change scenarios.

## 4. Unique key delete schema

Unique key ổn định theo model grain; nonunique/null keys gây nondeterministic merge hoặc duplicate. Updates need precedence/version; hard deletes need tombstone, invalidation or partition replacement. `on_schema_change` behavior không backfill historical values và tùy adapter. Column logic change có thể yêu cầu full refresh. Contract nêu policy cho add/drop/type/semantic changes.

## 5. Checkpoint và target state

Target đôi khi đóng vai checkpoint qua max value; coupling này dễ hỏng khi partial publish, manual edit hoặc retention. Better track input boundary/run ledger where needed. Atomic materialization semantics phụ thuộc adapter. Crash before/after merge, hook và artifact upload cần rerun convergence. Side effects ngoài target cũng cần idempotency identity.

## 6. Equivalence lab

Generate mutable entities/events with late update, delete, duplicate key, same timestamp ties, schema add và logic change. Run full baseline; then incremental sequences with kills/reorders; compare key set, typed row hash and aggregates. Periodically full-refresh/reconcile. Đạt khi documented horizon covers observed late data, every divergence maps to recovery and incremental output equals full under stated assumptions.

## 7. Ma trận kiểm chứng từng mệnh đề

Trong `Incremental Models and the is_incremental Contract`, mỗi claim phải nối được tới input boundary, compiled hoặc executed artifact, trạng thái trước–sau, failure signal và independent oracle. Một command kết thúc với exit code 0 không tự chứng minh dữ liệu đúng, đầy đủ hoặc phù hợp với consumer contract. Protocol nền của bài này: Dùng project tối thiểu và fixture có mutations đã biết; compile exact node/branch, execute trong sandbox nếu có, lưu artifacts rồi so key set, typed hashes và business invariants với full/reference computation.

### 7.1. is_incremental probe 1: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ

**Mệnh đề cần kiểm.** is_incremental probe 1: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-is-incremental-contract`.** Với `is_incremental probe 1: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ`, Bắt đầu bằng ca nhỏ nhất có thể làm mệnh đề sai; chỉ thêm dữ liệu sau khi failure signal đã xuất hiện đúng chỗ. Cách này phân biệt một assertion có lực với một bài demo chỉ đi qua happy path. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `is_incremental probe 1: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ` phải cho thấy: Giữ fixture tối thiểu, raw failure rows và câu lệnh tái hiện; ảnh chụp màn hình một trạng thái xanh không đủ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.2. is_incremental probe 2: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ

**Mệnh đề cần kiểm.** is_incremental probe 2: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-is-incremental-contract`.** Với `is_incremental probe 2: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ`, Giữ nguyên input rồi đổi đúng một tham số cấu hình liên quan. Nếu output đổi theo nhiều hướng cùng lúc, phép thử chưa cô lập được nguyên nhân và phải thu hẹp lại. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `is_incremental probe 2: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ` phải cho thấy: Báo cả giá trị trước–sau của tham số, compiled artifact và diff đầu ra để reviewer thấy biến nào thực sự đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.3. is_incremental probe 3: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ

**Mệnh đề cần kiểm.** is_incremental probe 3: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-is-incremental-contract`.** Với `is_incremental probe 3: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ`, Chạy cặp đối chứng: một input phải được chấp nhận và một input chỉ lệch tại boundary phải bị chặn hoặc được phân loại. Hai ca dùng chung code path để tránh so hai hệ thống khác nhau. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `is_incremental probe 3: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ` phải cho thấy: Pass khi positive control đi qua, negative control dừng đúng lớp và không có side effect ngoài scope. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.4. is_incremental probe 4: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ

**Mệnh đề cần kiểm.** is_incremental probe 4: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-is-incremental-contract`.** Với `is_incremental probe 4: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ`, Đặt kill point ngay trước và ngay sau durable boundary. So trạng thái sau restart để biết hệ thống tạo replay có kiểm soát, silent gap hay một trạng thái nửa vời mà dashboard không báo. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `is_incremental probe 4: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ` phải cho thấy: Run ledger phải cho biết commit/checkpoint nào bền vững; sau rerun, key set và side-effect ledger cùng hội tụ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.5. is_incremental probe 5: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ

**Mệnh đề cần kiểm.** is_incremental probe 5: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-is-incremental-contract`.** Với `is_incremental probe 5: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ`, Đảo thứ tự input và thay concurrency nhưng giữ logical population. Kết quả khác nhau cho thấy thiết kế đang phụ thuộc physical order hoặc race thay vì contract đã công bố. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `is_incremental probe 5: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ` phải cho thấy: Hash chuẩn hóa và business totals phải giống nhau giữa các thứ tự; chênh lệch được giữ như finding, không làm tròn mất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.6. is_incremental probe 6: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ

**Mệnh đề cần kiểm.** is_incremental probe 6: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-is-incremental-contract`.** Với `is_incremental probe 6: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ`, Cho cùng logical identity xuất hiện hai lần: trước hết cùng payload, sau đó payload khác. Trường hợp đầu phải hội tụ; trường hợp sau phải lộ collision thay vì âm thầm chọn một bản. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `is_incremental probe 6: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ` phải cho thấy: Same-content replay được đếm nhưng không nhân state; different-content collision có reason code và đường xử lý riêng. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.7. is_incremental probe 7: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ

**Mệnh đề cần kiểm.** is_incremental probe 7: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-is-incremental-contract`.** Với `is_incremental probe 7: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ`, Mở rộng fixture bằng một record tới trễ ngay trong horizon và một record nằm ngoài horizon. Ghi rõ record nào được sửa, record nào bị loại và metric nào khiến operator biết có mất coverage. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `is_incremental probe 7: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ` phải cho thấy: Evidence ghi accepted-late, rejected-late và oldest outstanding timestamp; thiếu một nhóm được báo là coverage gap. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.8. is_incremental probe 8: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ

**Mệnh đề cần kiểm.** is_incremental probe 8: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-is-incremental-contract`.** Với `is_incremental probe 8: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ`, Dùng một schema change tương thích và một thay đổi phá vỡ key, type hoặc meaning. Kết quả phải chỉ ra khác biệt giữa parse được, chạy được và vẫn giữ đúng semantics. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `is_incremental probe 8: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ` phải cho thấy: Lưu schema trước–sau, classification, compiled SQL và target state; một migration chạy xong nhưng đổi meaning vẫn fail. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.9. is_incremental probe 9: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ

**Mệnh đề cần kiểm.** is_incremental probe 9: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-is-incremental-contract`.** Với `is_incremental probe 9: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ`, Tạo bảng rỗng, bảng một row và bảng có duplicate bù cho missing row. Đây là ba ca dễ làm count hoặc aggregate xanh dù invariant thực tế đã hỏng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `is_incremental probe 9: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ` phải cho thấy: Oracle so count, key multiset và typed hashes. Ca missing-plus-duplicate phải bị phát hiện dù tổng row count không đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.10. is_incremental probe 10: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ

**Mệnh đề cần kiểm.** is_incremental probe 10: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-is-incremental-contract`.** Với `is_incremental probe 10: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ`, Cho reviewer chỉ artifacts, không cho xem lời giải thích của tác giả. Nếu họ không dựng lại được input, decision và diff thì evidence package chưa đủ để bàn giao. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `is_incremental probe 10: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ` phải cho thấy: Artifact package đạt khi reviewer tái hiện đúng diff và chỉ ra được limitation mà không cần hỏi tác giả về state ẩn. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.11. is_incremental probe 11: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ

**Mệnh đề cần kiểm.** is_incremental probe 11: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-is-incremental-contract`.** Với `is_incremental probe 11: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ`, So output với một cách tính độc lập không tái sử dụng macro, filter hoặc intermediate relation đang được kiểm. Hai phép tính dùng chung lỗi chỉ tạo sự đồng thuận giả. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `is_incremental probe 11: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ` phải cho thấy: Independent result phải khớp ở key/grain đã định; nếu chỉ khớp aggregate cao hơn thì drill-down chưa hoàn tất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.12. is_incremental probe 12: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ

**Mệnh đề cần kiểm.** is_incremental probe 12: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-is-incremental-contract`.** Với `is_incremental probe 12: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ`, Thử trên hai scope: selection hẹp dùng trong CI và population đầy đủ dùng khi phát hành. Ghi phần coverage bị bỏ qua; tốc độ của CI không được biến thành tuyên bố kiểm toàn bộ dữ liệu. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `is_incremental probe 12: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ` phải cho thấy: Kết quả nêu numerator, denominator và excluded nodes/partitions; không dùng từ `all` khi selection không phủ toàn graph. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.13. is_incremental probe 13: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ

**Mệnh đề cần kiểm.** is_incremental probe 13: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-is-incremental-contract`.** Với `is_incremental probe 13: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ`, Đẩy một giá trị tới sát giới hạn precision, timezone, partition hoặc threshold. Boundary phải được viết half-open hay inclusive rõ ràng, không suy từ một ví dụ ở giữa khoảng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `is_incremental probe 13: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ` phải cho thấy: Hai phía của boundary đều có expected result và raw observation. Sai đúng một đơn vị phải làm test fail có chẩn đoán. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.14. is_incremental probe 14: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ

**Mệnh đề cần kiểm.** is_incremental probe 14: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-is-incremental-contract`.** Với `is_incremental probe 14: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ`, Thay constraint quan trọng nhất bằng giá trị đủ để decision phải đảo. Nếu thiết kế vẫn đưa cùng lựa chọn mà không giải thích, decision rule đang là khẩu hiệu chứ chưa phải rule. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `is_incremental probe 14: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ` phải cho thấy: ADR hoặc rule chỉ pass khi changed constraint tạo lựa chọn mới đúng như đã dự báo và reversal threshold được lưu. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.15. is_incremental probe 15: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ

**Mệnh đề cần kiểm.** is_incremental probe 15: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-is-incremental-contract`.** Với `is_incremental probe 15: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ`, Lặp lại phép thử từ môi trường sạch bằng seed và versions đã lưu. Một kết quả chỉ tái hiện được trên workspace của tác giả không đủ làm release evidence. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `is_incremental probe 15: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ` phải cho thấy: Lần chạy sạch phải tạo cùng canonical state; khác biệt do timestamp, file order hoặc generated IDs phải được loại hoặc giải thích. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

## 8. Quy trình phản biện

Áp dụng sáu bước sau cho `Incremental Models and the is_incremental Contract`; nếu một bước không phù hợp, ghi lý do thay vì bỏ qua im lặng.

1. Với `wiki.transformation.dbt-is-incremental-contract`, chốt grain, identity, time boundary và consumer-visible invariant trước câu lệnh.
2. Tách parse/compile state, warehouse execution và publication state.
3. Pin dbt core, adapter, warehouse hoặc orchestrator version cùng configuration có ảnh hưởng.
4. Kiểm correctness bằng key set, typed hash và business invariant trước performance.
5. Chạy negative case, kill point hoặc changed assumption; green path đơn lẻ không đủ.
6. Phân loại source fact, project convention, curriculum synthesis và untested hypothesis.

## 9. Câu hỏi tự kiểm tra

1. `is_incremental probe 1: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ` sẽ thất bại trước tiên ở boundary nào?
2. Với `is_incremental probe 2: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ`, artifact nào là nguồn bằng chứng mạnh nhất?
3. Counterexample nhỏ nhất cho `is_incremental probe 3: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ` gồm những row hoặc state nào?
4. `is_incremental probe 4: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ` có thể xanh giả trong tình huống nào?
5. Version, adapter, timezone hoặc state nào làm `is_incremental probe 5: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ` đổi nghĩa?
6. Phần nào của `is_incremental probe 6: branch condition, source filter, affected state, rerun và full-equivalence oracle phải rõ` hiện mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Incremental Models and the is_incremental Contract` chưa chạy trên warehouse, dbt project hoặc orchestrator production; các mục kiểm chứng vẫn là protocol và expected evidence.
- Các claim gắn `wiki.transformation.dbt-is-incremental-contract` phải kiểm lại theo dbt core, adapter, warehouse và scheduler version được chọn.
- Decision matrix, failure campaign và ngưỡng review là curriculum synthesis, không phải cam kết của vendor.
- Note giữ trạng thái `review` cho tới khi chủ dự án duyệt semantic meaning và learner artifact.

## Reference
1. [[SRC-DBT-INCREMENTAL-MODELS]]
2. [[SRC-KLEPPMANN-DDIA-1E]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-DBT-INCREMENTAL-MODELS]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |
| [[SRC-KLEPPMANN-DDIA-1E]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |

## Key takeaways
- Incremental correctness là equivalence claim với canonical full result dưới stated mutations, lateness và delete assumptions; `is_incremental()` chỉ chọn branch.
- Với `Incremental Models and the is_incremental Contract`, compiled intent và observed state phải được lưu tách biệt; trộn hai lớp sẽ che failure window.
- Oracle của bài phải bám câu hỏi trung tâm: `is_incremental()` cần những điều kiện, filter symmetry và replay assumptions nào để incremental state hội tụ với full recomputation?
- Các source IDs `src.web.dbt-incremental-models, src.book.kleppmann-ddia.1e` đặt ranh giới cho claim; phần synthesis không được gán nguyên văn cho vendor.
- Trước khi lab chạy, note này là giáo trình đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule — kiểm chứng `wiki.transformation.dbt-is-incremental-contract`

> [!important] Phân loại mệnh đề
> Với `wiki.transformation.dbt-is-incremental-contract`, sơ đồ, ví dụ và artifact về **Incremental Models and the is_incremental Contract** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.web.dbt-incremental-models"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Incremental Models and the is_incremental Contract"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.transformation.dbt-is-incremental-contract` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Incremental Models and the is_incremental Contract**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```sql
-- Verification harness for: Incremental Models and the is_incremental Contract
WITH evidence AS (
    SELECT 'wiki.transformation.dbt-is-incremental-contract' AS concept_id,
           'boundary_declared' AS check_name, 1 AS passed
    UNION ALL
    SELECT 'wiki.transformation.dbt-is-incremental-contract', 'independent_oracle', 1
    UNION ALL
    SELECT 'wiki.transformation.dbt-is-incremental-contract', 'reversal_trigger_recorded', 1
)
SELECT concept_id,
       MIN(passed) AS all_hard_checks_pass,
       COUNT(*) AS evidence_items
FROM evidence
GROUP BY concept_id
HAVING MIN(passed) = 1;
```

Artifact của `wiki.transformation.dbt-is-incremental-contract` buộc người dùng ghi boundary, oracle và reversal trigger cho **Incremental Models and the is_incremental Contract**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

### Tự kiểm tra trước khi tái sử dụng

1. Bạn có thể trả lời ``is_incremental()` cần những điều kiện, filter symmetry và replay assumptions nào để incremental state hội tụ với full recomputation?` bằng một câu mà không kéo thêm concept thứ hai không?
2. Source locator nào đỡ cho claim, và phần nào chỉ là synthesis trong note?
3. Observation nào khiến bạn dừng, thu hẹp hoặc đảo quyết định?
4. Artifact nào cho phép một reviewer độc lập tái hiện kết quả?

<!-- ATOMIC-EXECUTION-CAPSULE:END -->

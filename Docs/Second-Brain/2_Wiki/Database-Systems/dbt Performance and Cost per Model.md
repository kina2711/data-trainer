---
note_id: wiki.transformation.dbt-performance-cost-per-model
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
primary_question: Đo performance và cost per model thế nào để tách compile/orchestrator time, warehouse execution, queueing, scans và shared downstream value?
source_ids:
  - src.web.dbt-artifacts
  - src.book.reis-housley-fundamentals-data-engineering
aliases: [dbt Performance and Cost per Model]
tags: [wiki/transformation, dbt, orchestration, reliability]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/156-dbt-performance-cost-per-model.md
relationships:
  builds_on: [wiki.transformation.dbt-artifacts-manifest-results-catalog]
  prerequisite_of: []
  related_to: []

---
# dbt Performance and Cost per Model

> [!abstract] Câu hỏi trung tâm
> Đo performance và cost per model thế nào để tách compile/orchestrator time, warehouse execution, queueing, scans và shared downstream value?

## 1. Wall clock không phải cost model

Run results execution time includes dbt-observed node duration, nhưng warehouse queue, compile, transfer or async behavior vary. Cost depends platform billing: bytes scanned, slot/credit/warehouse time, storage/write and concurrency. One fast query on an already-running warehouse can still share sunk capacity; one slow queued query may consume little compute. Define allocation rule and confidence before ranking models.

## 2. Identity và tagging

Map dbt unique_id/invocation to warehouse query IDs using query comments/tags or adapter response where available. Persist compiled SQL hash, target, role/warehouse, start/end and parent build state. Without join, cost attributed by SQL text/name is fragile. One model materialization may emit multiple statements; hooks/tests/snapshots add queries. Sum exact statement set and avoid double counting shared warehouse intervals.

## 3. Four measurement layers

Layer 1 compile/graph overhead. Layer 2 orchestrator wait/thread/queue. Layer 3 warehouse query profile: scan, shuffle/spill, CPU/slots/credits, bytes written and lock. Layer 4 downstream cost/value: consumer query savings, freshness and incidents. Optimize the current bottleneck. A model with high build cost may reduce hundreds of downstream scans; per-build ranking alone recommends the wrong deletion.

## 4. Controlled benchmark

Pin data snapshot, warehouse size, concurrency, cache state, materialization and cluster/partition config. Separate cold/warm runs, randomize order and repeat. Compare explain/profile plus raw billing/query history. Correctness hash and freshness gate before performance. When engine auto-scales or result cache intervenes, report whole-system outcome with confounders rather than pretend query-level causality.

## 5. Cost allocation và budgets

Choose direct query cost where available; for shared capacity, allocate by measured compute/slot time or keep unallocated pool. Do not invent precise per-model dollars from elapsed seconds. Budgets can flag regression relative baseline and forecast cadence, with minimum sample and seasonal workload. Separate build, test, docs and ad-hoc costs. Owner reviews outliers with opportunity and change risk.

## 6. Optimization decision

Start with semantic waste: accidental full refresh, unbounded scan, repeated fanout, missing predicate, overly persistent intermediate or too-frequent schedule. Then physical tuning/materialization. Record before/after plans, resource counters, cost and downstream latency under same workload. Reversal if savings disappear under changed volume/concurrency or maintenance complexity rises. Fast but stale/wrong output is not improvement.

## 7. Ma trận kiểm chứng từng mệnh đề

Trong `dbt Performance and Cost per Model`, mỗi claim phải nối được tới input boundary, compiled hoặc executed artifact, trạng thái trước–sau, failure signal và independent oracle. Một command kết thúc với exit code 0 không tự chứng minh dữ liệu đúng, đầy đủ hoặc phù hợp với consumer contract. Protocol nền của bài này: Dựng artifact/workflow fixture có exact versions và intervals; inject one failure or changed assumption; capture resolved graph/state/query IDs or scheduler context and compare with independent coverage oracle.

### 7.1. Performance probe 1: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ

**Mệnh đề cần kiểm.** Performance probe 1: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-performance-cost-per-model`.** Với `Performance probe 1: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ`, Bắt đầu bằng ca nhỏ nhất có thể làm mệnh đề sai; chỉ thêm dữ liệu sau khi failure signal đã xuất hiện đúng chỗ. Cách này phân biệt một assertion có lực với một bài demo chỉ đi qua happy path. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Performance probe 1: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ` phải cho thấy: Giữ fixture tối thiểu, raw failure rows và câu lệnh tái hiện; ảnh chụp màn hình một trạng thái xanh không đủ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.2. Performance probe 2: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ

**Mệnh đề cần kiểm.** Performance probe 2: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-performance-cost-per-model`.** Với `Performance probe 2: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ`, Giữ nguyên input rồi đổi đúng một tham số cấu hình liên quan. Nếu output đổi theo nhiều hướng cùng lúc, phép thử chưa cô lập được nguyên nhân và phải thu hẹp lại. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Performance probe 2: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ` phải cho thấy: Báo cả giá trị trước–sau của tham số, compiled artifact và diff đầu ra để reviewer thấy biến nào thực sự đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.3. Performance probe 3: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ

**Mệnh đề cần kiểm.** Performance probe 3: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-performance-cost-per-model`.** Với `Performance probe 3: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ`, Chạy cặp đối chứng: một input phải được chấp nhận và một input chỉ lệch tại boundary phải bị chặn hoặc được phân loại. Hai ca dùng chung code path để tránh so hai hệ thống khác nhau. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Performance probe 3: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ` phải cho thấy: Pass khi positive control đi qua, negative control dừng đúng lớp và không có side effect ngoài scope. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.4. Performance probe 4: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ

**Mệnh đề cần kiểm.** Performance probe 4: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-performance-cost-per-model`.** Với `Performance probe 4: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ`, Đặt kill point ngay trước và ngay sau durable boundary. So trạng thái sau restart để biết hệ thống tạo replay có kiểm soát, silent gap hay một trạng thái nửa vời mà dashboard không báo. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Performance probe 4: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ` phải cho thấy: Run ledger phải cho biết commit/checkpoint nào bền vững; sau rerun, key set và side-effect ledger cùng hội tụ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.5. Performance probe 5: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ

**Mệnh đề cần kiểm.** Performance probe 5: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-performance-cost-per-model`.** Với `Performance probe 5: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ`, Đảo thứ tự input và thay concurrency nhưng giữ logical population. Kết quả khác nhau cho thấy thiết kế đang phụ thuộc physical order hoặc race thay vì contract đã công bố. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Performance probe 5: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ` phải cho thấy: Hash chuẩn hóa và business totals phải giống nhau giữa các thứ tự; chênh lệch được giữ như finding, không làm tròn mất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.6. Performance probe 6: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ

**Mệnh đề cần kiểm.** Performance probe 6: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-performance-cost-per-model`.** Với `Performance probe 6: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ`, Cho cùng logical identity xuất hiện hai lần: trước hết cùng payload, sau đó payload khác. Trường hợp đầu phải hội tụ; trường hợp sau phải lộ collision thay vì âm thầm chọn một bản. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Performance probe 6: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ` phải cho thấy: Same-content replay được đếm nhưng không nhân state; different-content collision có reason code và đường xử lý riêng. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.7. Performance probe 7: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ

**Mệnh đề cần kiểm.** Performance probe 7: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-performance-cost-per-model`.** Với `Performance probe 7: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ`, Mở rộng fixture bằng một record tới trễ ngay trong horizon và một record nằm ngoài horizon. Ghi rõ record nào được sửa, record nào bị loại và metric nào khiến operator biết có mất coverage. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Performance probe 7: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ` phải cho thấy: Evidence ghi accepted-late, rejected-late và oldest outstanding timestamp; thiếu một nhóm được báo là coverage gap. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.8. Performance probe 8: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ

**Mệnh đề cần kiểm.** Performance probe 8: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-performance-cost-per-model`.** Với `Performance probe 8: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ`, Dùng một schema change tương thích và một thay đổi phá vỡ key, type hoặc meaning. Kết quả phải chỉ ra khác biệt giữa parse được, chạy được và vẫn giữ đúng semantics. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Performance probe 8: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ` phải cho thấy: Lưu schema trước–sau, classification, compiled SQL và target state; một migration chạy xong nhưng đổi meaning vẫn fail. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.9. Performance probe 9: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ

**Mệnh đề cần kiểm.** Performance probe 9: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-performance-cost-per-model`.** Với `Performance probe 9: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ`, Tạo bảng rỗng, bảng một row và bảng có duplicate bù cho missing row. Đây là ba ca dễ làm count hoặc aggregate xanh dù invariant thực tế đã hỏng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Performance probe 9: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ` phải cho thấy: Oracle so count, key multiset và typed hashes. Ca missing-plus-duplicate phải bị phát hiện dù tổng row count không đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.10. Performance probe 10: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ

**Mệnh đề cần kiểm.** Performance probe 10: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-performance-cost-per-model`.** Với `Performance probe 10: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ`, Cho reviewer chỉ artifacts, không cho xem lời giải thích của tác giả. Nếu họ không dựng lại được input, decision và diff thì evidence package chưa đủ để bàn giao. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Performance probe 10: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ` phải cho thấy: Artifact package đạt khi reviewer tái hiện đúng diff và chỉ ra được limitation mà không cần hỏi tác giả về state ẩn. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.11. Performance probe 11: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ

**Mệnh đề cần kiểm.** Performance probe 11: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-performance-cost-per-model`.** Với `Performance probe 11: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ`, So output với một cách tính độc lập không tái sử dụng macro, filter hoặc intermediate relation đang được kiểm. Hai phép tính dùng chung lỗi chỉ tạo sự đồng thuận giả. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Performance probe 11: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ` phải cho thấy: Independent result phải khớp ở key/grain đã định; nếu chỉ khớp aggregate cao hơn thì drill-down chưa hoàn tất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.12. Performance probe 12: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ

**Mệnh đề cần kiểm.** Performance probe 12: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-performance-cost-per-model`.** Với `Performance probe 12: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ`, Thử trên hai scope: selection hẹp dùng trong CI và population đầy đủ dùng khi phát hành. Ghi phần coverage bị bỏ qua; tốc độ của CI không được biến thành tuyên bố kiểm toàn bộ dữ liệu. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Performance probe 12: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ` phải cho thấy: Kết quả nêu numerator, denominator và excluded nodes/partitions; không dùng từ `all` khi selection không phủ toàn graph. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.13. Performance probe 13: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ

**Mệnh đề cần kiểm.** Performance probe 13: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-performance-cost-per-model`.** Với `Performance probe 13: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ`, Đẩy một giá trị tới sát giới hạn precision, timezone, partition hoặc threshold. Boundary phải được viết half-open hay inclusive rõ ràng, không suy từ một ví dụ ở giữa khoảng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Performance probe 13: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ` phải cho thấy: Hai phía của boundary đều có expected result và raw observation. Sai đúng một đơn vị phải làm test fail có chẩn đoán. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.14. Performance probe 14: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ

**Mệnh đề cần kiểm.** Performance probe 14: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-performance-cost-per-model`.** Với `Performance probe 14: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ`, Thay constraint quan trọng nhất bằng giá trị đủ để decision phải đảo. Nếu thiết kế vẫn đưa cùng lựa chọn mà không giải thích, decision rule đang là khẩu hiệu chứ chưa phải rule. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Performance probe 14: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ` phải cho thấy: ADR hoặc rule chỉ pass khi changed constraint tạo lựa chọn mới đúng như đã dự báo và reversal threshold được lưu. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.15. Performance probe 15: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ

**Mệnh đề cần kiểm.** Performance probe 15: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-performance-cost-per-model`.** Với `Performance probe 15: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ`, Lặp lại phép thử từ môi trường sạch bằng seed và versions đã lưu. Một kết quả chỉ tái hiện được trên workspace của tác giả không đủ làm release evidence. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Performance probe 15: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ` phải cho thấy: Lần chạy sạch phải tạo cùng canonical state; khác biệt do timestamp, file order hoặc generated IDs phải được loại hoặc giải thích. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

## 8. Quy trình phản biện

Áp dụng sáu bước sau cho `dbt Performance and Cost per Model`; nếu một bước không phù hợp, ghi lý do thay vì bỏ qua im lặng.

1. Với `wiki.transformation.dbt-performance-cost-per-model`, chốt grain, identity, time boundary và consumer-visible invariant trước câu lệnh.
2. Tách parse/compile state, warehouse execution và publication state.
3. Pin dbt core, adapter, warehouse hoặc orchestrator version cùng configuration có ảnh hưởng.
4. Kiểm correctness bằng key set, typed hash và business invariant trước performance.
5. Chạy negative case, kill point hoặc changed assumption; green path đơn lẻ không đủ.
6. Phân loại source fact, project convention, curriculum synthesis và untested hypothesis.

## 9. Câu hỏi tự kiểm tra

1. `Performance probe 1: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ` sẽ thất bại trước tiên ở boundary nào?
2. Với `Performance probe 2: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ`, artifact nào là nguồn bằng chứng mạnh nhất?
3. Counterexample nhỏ nhất cho `Performance probe 3: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ` gồm những row hoặc state nào?
4. `Performance probe 4: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ` có thể xanh giả trong tình huống nào?
5. Version, adapter, timezone hoặc state nào làm `Performance probe 5: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ` đổi nghĩa?
6. Phần nào của `Performance probe 6: model-query identity, controlled workload, physical counter, cost rule và correctness gate phải rõ` hiện mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `dbt Performance and Cost per Model` chưa chạy trên warehouse, dbt project hoặc orchestrator production; các mục kiểm chứng vẫn là protocol và expected evidence.
- Các claim gắn `wiki.transformation.dbt-performance-cost-per-model` phải kiểm lại theo dbt core, adapter, warehouse và scheduler version được chọn.
- Decision matrix, failure campaign và ngưỡng review là curriculum synthesis, không phải cam kết của vendor.
- Note giữ trạng thái `review` cho tới khi chủ dự án duyệt semantic meaning và learner artifact.

## Reference
1. [[SRC-DBT-ARTIFACTS]]
2. [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-DBT-ARTIFACTS]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |
| [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |

## Key takeaways
- Cost per model cần query identity và platform counters; elapsed time là một signal, không phải hóa đơn, còn correctness/freshness luôn là gate trước tối ưu.
- Với `dbt Performance and Cost per Model`, compiled intent và observed state phải được lưu tách biệt; trộn hai lớp sẽ che failure window.
- Oracle của bài phải bám câu hỏi trung tâm: Đo performance và cost per model thế nào để tách compile/orchestrator time, warehouse execution, queueing, scans và shared downstream value?
- Các source IDs `src.web.dbt-artifacts, src.book.reis-housley-fundamentals-data-engineering` đặt ranh giới cho claim; phần synthesis không được gán nguyên văn cho vendor.
- Trước khi lab chạy, note này là giáo trình đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule — kiểm chứng `wiki.transformation.dbt-performance-cost-per-model`

> [!important] Phân loại mệnh đề
> Với `wiki.transformation.dbt-performance-cost-per-model`, sơ đồ, ví dụ và artifact về **dbt Performance and Cost per Model** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.web.dbt-artifacts"] --> B["Khóa boundary"]
    B --> M["Cơ chế: dbt Performance and Cost per Model"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.transformation.dbt-performance-cost-per-model` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **dbt Performance and Cost per Model**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```sql
-- Verification harness for: dbt Performance and Cost per Model
WITH evidence AS (
    SELECT 'wiki.transformation.dbt-performance-cost-per-model' AS concept_id,
           'boundary_declared' AS check_name, 1 AS passed
    UNION ALL
    SELECT 'wiki.transformation.dbt-performance-cost-per-model', 'independent_oracle', 1
    UNION ALL
    SELECT 'wiki.transformation.dbt-performance-cost-per-model', 'reversal_trigger_recorded', 1
)
SELECT concept_id,
       MIN(passed) AS all_hard_checks_pass,
       COUNT(*) AS evidence_items
FROM evidence
GROUP BY concept_id
HAVING MIN(passed) = 1;
```

Artifact của `wiki.transformation.dbt-performance-cost-per-model` buộc người dùng ghi boundary, oracle và reversal trigger cho **dbt Performance and Cost per Model**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

### Tự kiểm tra trước khi tái sử dụng

1. Bạn có thể trả lời `Đo performance và cost per model thế nào để tách compile/orchestrator time, warehouse execution, queueing, scans và shared downstream value?` bằng một câu mà không kéo thêm concept thứ hai không?
2. Source locator nào đỡ cho claim, và phần nào chỉ là synthesis trong note?
3. Observation nào khiến bạn dừng, thu hẹp hoặc đảo quyết định?
4. Artifact nào cho phép một reviewer độc lập tái hiện kết quả?

<!-- ATOMIC-EXECUTION-CAPSULE:END -->

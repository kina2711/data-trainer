# Phase 6: Analytical Storage and Query Engines
# Module 14: OLAP Internals and Analytical Engines
# Lesson 213: Shared Nothing and Separated Storage Compute

## Mục tiêu bài học

**Năng lực cần chứng minh.** Chỉ ra hệ quả vận hành của mỗi kiến trúc và thiết kế được một phép đo công bằng về trạng thái đệm.

**Điều kiện hoàn thành.** Chênh lệch đệm nóng và đệm lạnh được định lượng, và quy trình đo nêu rõ cách đặt trạng thái đệm trước mỗi lần chạy.

> [!abstract] Câu hỏi trung tâm
> So sánh shared-nothing với separated storage/compute bằng failure, scaling, cache và metadata boundaries nào để tránh benchmark nóng-lạnh sai?

## 1. Shared-nothing contract

Mỗi node sở hữu compute, memory và local data partitions; parallel scan tận dụng locality, distributed join dựa distribution contract. Scale/membership change có thể yêu cầu redistribute/rebalance persistent data, nhưng mức độ và online behavior phụ thuộc engine: replication, elastic resize, remote tier hay managed automation có thể thay đổi. Không đồng nhất mọi MPP provisioned system với pure shared-nothing. Đánh giá bằng locality hit, redistribution bytes/time, degraded capacity, recovery semantics và operational procedure.

## 2. Separated storage and compute

Persistent table data nằm ở shared durable storage; ephemeral/elastic compute đọc ranges và giữ local caches/temp. Compute groups có thể scale và isolate independently trong giới hạn service. Câu 'mọi lần đọc qua network' quá thô: cache hit đọc local, metadata/result cache có thể tránh data scan, còn cache miss đọc remote. Network vẫn là boundary chính để populate cache. Ghi source bytes, local cache bytes/hit, remote requests, temp spill và result reuse; không suy cache state từ runtime một mình.

## 3. Ba lớp cache

Result cache trả prior result khi text, data freshness, role/session và engine rules phù hợp; data cache giữ table files/columns/blocks; metadata/plan cache giữ catalog/statistics/compiled state. Chúng có invalidation và scope khác nhau. Result-cache hit không đo engine execution. Data-cache warm không bảo đảm metadata warm hoặc warehouse process đã khởi động. Benchmark cần disable/bypass result cache khi có thể, log hit flag, và định nghĩa cold/warm riêng cho từng layer.

## 4. Cold không có một nghĩa duy nhất

Cold warehouse có thể gồm compute resume/provision, empty local cache, cold object/CDN path, cold metadata/JIT và DNS/TLS setup. Người dùng thường chỉ kiểm một phần. Không được tuyên bố globally cold nếu service không cung cấp eviction/isolated fresh warehouse. Dùng operational definitions: fresh compute identifier, no result-cache hit, first access to immutable snapshot, measured remote bytes. Warm series chạy same snapshot/query family trên same warehouse sau priming. Báo unknown layers thay vì giả vờ kiểm soát.

## 5. Isolation và shared control plane

Tách compute groups giảm competition CPU/memory/cache giữa workloads, nhưng storage service, catalog, metadata, transaction manager, identity, quota và network có thể vẫn shared. Vì vậy isolation không tuyệt đối. Test cross-workload interference ở compute, remote storage throughput và metadata latency. Một warehouse riêng có thể làm cache duplication và cost tăng. Shared-nothing cũng có WLM queues và resource groups; architecture không tự quyết toàn bộ isolation policy.

## 6. Scaling và data movement

Pure shared-nothing scale-out cần rebalance persistent partitions hoặc chỉ dùng capacity mới cho future data/replicas tùy product. Shared-data scale-out tránh base-data rebalance nhưng phải provision workers, schedule splits và warm local cache; resize có thể giảm cache affinity. Scale-in cần drain/cancel semantics và temp state handling. So time-to-capacity, bytes moved/read, cache recovery, availability và cost during transition. Không chỉ đo steady-state query.

## 7. Metadata là data path

Catalog maps snapshots/tables to files, statistics, permissions, transactions và pruning. Shared-data compute phụ thuộc control/metadata services để lập kế hoạch; shared-nothing cũng cần catalogs/coordinators. Bottleneck có thể xuất hiện ở listing, manifest, planning, locks hoặc service quotas trước scan. Capture planning/queue separately from execution, catalog request count/latency nếu có. Cache metadata có consistency contract; stale cache không được dùng để đổi correctness lấy speed.

## 8. Phép đo công bằng

Chọn immutable snapshot và query suite, khóa engine/version/region/worker shape/concurrency. Tạo four cells: cold-result/cold-data theo operational definition, result-cache disabled; warm-data; explicit result-cache case; resize/resume case. Interleave trials để tránh diurnal drift, log provisioning separately, verify result hash. Với shared-nothing, thêm after-rebalance state. Với shared-data, ghi remote/local bytes. Kết luận cần distributions, cost và reversal conditions; một cold run với một warm run không hợp lệ.

## 9. Ma trận kiểm chứng từng mệnh đề

Mỗi mệnh đề về latency, scaling, cache, concurrency hoặc cost cần counterfactual, correctness oracle và counter ở đúng boundary. Tên kiến trúc, plan label, elapsed time hoặc rate card riêng lẻ chưa đủ để quy nguyên nhân.

### 9.1. pure shared nothing gắn persistent partitions với nodes

**Mệnh đề cần kiểm.** pure shared nothing gắn persistent partitions với nodes.

**Cách kiểm.** Định nghĩa result/data/metadata cache states; chạy interleaved cold/warm/result-cache/resize cells, lưu remote/local bytes, provisioning, planning và output hash. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.2. managed variants có thể không cần full eager rebalance

**Mệnh đề cần kiểm.** managed variants có thể không cần full eager rebalance.

**Cách kiểm.** Định nghĩa result/data/metadata cache states; chạy interleaved cold/warm/result-cache/resize cells, lưu remote/local bytes, provisioning, planning và output hash. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.3. shared data không có nghĩa mọi read luôn từ remote storage

**Mệnh đề cần kiểm.** shared data không có nghĩa mọi read luôn từ remote storage.

**Cách kiểm.** Định nghĩa result/data/metadata cache states; chạy interleaved cold/warm/result-cache/resize cells, lưu remote/local bytes, provisioning, planning và output hash. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.4. result data metadata và plan caches phải tách

**Mệnh đề cần kiểm.** result data metadata và plan caches phải tách.

**Cách kiểm.** Định nghĩa result/data/metadata cache states; chạy interleaved cold/warm/result-cache/resize cells, lưu remote/local bytes, provisioning, planning và output hash. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.5. result cache hit không đo query execution

**Mệnh đề cần kiểm.** result cache hit không đo query execution.

**Cách kiểm.** Định nghĩa result/data/metadata cache states; chạy interleaved cold/warm/result-cache/resize cells, lưu remote/local bytes, provisioning, planning và output hash. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.6. cold cache cần operational definition

**Mệnh đề cần kiểm.** cold cache cần operational definition.

**Cách kiểm.** Định nghĩa result/data/metadata cache states; chạy interleaved cold/warm/result-cache/resize cells, lưu remote/local bytes, provisioning, planning và output hash. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.7. không có eviction authority thì không tuyên bố globally cold

**Mệnh đề cần kiểm.** không có eviction authority thì không tuyên bố globally cold.

**Cách kiểm.** Định nghĩa result/data/metadata cache states; chạy interleaved cold/warm/result-cache/resize cells, lưu remote/local bytes, provisioning, planning và output hash. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.8. fresh compute có thể thêm provisioning latency

**Mệnh đề cần kiểm.** fresh compute có thể thêm provisioning latency.

**Cách kiểm.** Định nghĩa result/data/metadata cache states; chạy interleaved cold/warm/result-cache/resize cells, lưu remote/local bytes, provisioning, planning và output hash. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.9. warm cache phải giữ same snapshot và warehouse identity

**Mệnh đề cần kiểm.** warm cache phải giữ same snapshot và warehouse identity.

**Cách kiểm.** Định nghĩa result/data/metadata cache states; chạy interleaved cold/warm/result-cache/resize cells, lưu remote/local bytes, provisioning, planning và output hash. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.10. compute isolation không tách shared metadata storage và quotas

**Mệnh đề cần kiểm.** compute isolation không tách shared metadata storage và quotas.

**Cách kiểm.** Định nghĩa result/data/metadata cache states; chạy interleaved cold/warm/result-cache/resize cells, lưu remote/local bytes, provisioning, planning và output hash. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.11. separate warehouses có cache duplication cost

**Mệnh đề cần kiểm.** separate warehouses có cache duplication cost.

**Cách kiểm.** Định nghĩa result/data/metadata cache states; chạy interleaved cold/warm/result-cache/resize cells, lưu remote/local bytes, provisioning, planning và output hash. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.12. scale out shared data vẫn có provisioning và cache warmup

**Mệnh đề cần kiểm.** scale out shared data vẫn có provisioning và cache warmup.

**Cách kiểm.** Định nghĩa result/data/metadata cache states; chạy interleaved cold/warm/result-cache/resize cells, lưu remote/local bytes, provisioning, planning và output hash. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.13. resize có thể đổi cache affinity

**Mệnh đề cần kiểm.** resize có thể đổi cache affinity.

**Cách kiểm.** Định nghĩa result/data/metadata cache states; chạy interleaved cold/warm/result-cache/resize cells, lưu remote/local bytes, provisioning, planning và output hash. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.14. planning metadata time phải tách execution

**Mệnh đề cần kiểm.** planning metadata time phải tách execution.

**Cách kiểm.** Định nghĩa result/data/metadata cache states; chạy interleaved cold/warm/result-cache/resize cells, lưu remote/local bytes, provisioning, planning và output hash. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.15. fair comparison cần interleaved repetitions và result oracle

**Mệnh đề cần kiểm.** fair comparison cần interleaved repetitions và result oracle.

**Cách kiểm.** Định nghĩa result/data/metadata cache states; chạy interleaved cold/warm/result-cache/resize cells, lưu remote/local bytes, provisioning, planning và output hash. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

## 10. Quy trình phản biện

1. Viết câu hỏi đo lường và decision cần hỗ trợ trước khi chọn metric.
2. Khóa query semantics, snapshot, output oracle và unit của mọi số.
3. Vẽ boundaries: client, queue, planner, source, worker, exchange, cache, spill và billing.
4. Thay một cơ chế; ghi mọi thay đổi algorithm/config do engine tự thực hiện.
5. Dùng distribution và critical path; không để average che tails hoặc skew.
6. Viết counterexample, reversal condition và stop threshold trước khi chạy.
7. Tách estimate, configured intent, runtime observation và invoice fact.
8. Nếu không kiểm soát được cache, resource hoặc rate contract, ghi giới hạn thay vì kết luận nhân quả.

## 11. Câu hỏi tự kiểm tra

1. Mệnh đề đang nằm ở tầng kiến trúc, scheduler, operator, hardware hay billing?
2. Counter nào quan sát trực tiếp cơ chế đó và proxy nào dễ gây nhầm?
3. Correctness/SLO nào phải giữ trước khi gọi một phương án tốt hơn?
4. Cache, concurrency, statistics, data shape hay rate card nào có thể đảo kết luận?
5. Intervention nào bác bỏ diagnosis hiện tại?
6. Kết luận nào mới là protocol, chưa phải observation?

## 12. Giới hạn và điều chưa cho phép kết luận

- Chưa chạy cluster scaling, join/spill, cache, concurrency hoặc billing reconciliation lab; note mô tả protocol và evidence contract.
- Tài liệu sản phẩm được kiểm ngày 2026-10-01; field, feature, pricing và behavior có thể đổi theo version, region và contract.
- Amdahl, Gustafson, workload matrices và cost equations là mô hình; chúng không thay runtime counters hay invoice export.
- Không suy vendor superiority từ paper hoặc một benchmark; workload, correctness, SLO, operation và price contract phải cùng phạm vi.
- Note giữ trạng thái `review` cho tới khi chủ dự án duyệt semantic meaning.

## Reference
1. [[SRC-SNOWFLAKE-ELASTIC-DATA-WAREHOUSE]]
2. [[SRC-PRESTO-SQL-ON-EVERYTHING]]
3. [[SRC-TRINO-DISTRIBUTED-PLANS]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-SNOWFLAKE-ELASTIC-DATA-WAREHOUSE]] | Khái niệm, mechanism hoặc evidence boundary liên quan | Đã đọc locator trong source record; không suy ngoài phạm vi |
| [[SRC-PRESTO-SQL-ON-EVERYTHING]] | Khái niệm, mechanism hoặc evidence boundary liên quan | Đã đọc locator trong source record; không suy ngoài phạm vi |
| [[SRC-TRINO-DISTRIBUTED-PLANS]] | Khái niệm, mechanism hoặc evidence boundary liên quan | Đã đọc locator trong source record; không suy ngoài phạm vi |

## Key takeaways
- So kiến trúc chỉ hợp lệ khi result, data, metadata cache và provisioning state có operational definition.
- Estimate và configured intent phải được tách khỏi runtime observation và invoice fact.
- Correctness oracle, units, cache state, workload shape và controlled variables đi trước performance/cost claim.
- Average phải đi cùng distributions, tails, critical path và per-class hoặc per-task counters.
- Chưa chạy lab thì artifact là giáo trình đã kiểm cấu trúc, chưa phải benchmark hay production certification.

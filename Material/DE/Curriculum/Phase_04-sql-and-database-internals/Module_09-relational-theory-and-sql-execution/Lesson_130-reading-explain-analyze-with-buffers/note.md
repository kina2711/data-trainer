# Phase 4: SQL and Database Internals
# Module 9: Relational Theory and SQL Execution
# Lesson 130: Reading EXPLAIN ANALYZE with buffers

## Mục tiêu bài học

**Năng lực cần chứng minh.** Đọc một kế hoạch và định vị nút tốn nhất cùng nguyên nhân, dẫn bằng bốn con số chứ bằng cảm nhận.

**Điều kiện hoàn thành.** Định vị đúng nút tốn nhất ở ≥ 4/5 kế hoạch và quy đúng nguyên nhân ở ≥ 3/5, kèm bốn con số dẫn chứng.

> [!abstract] Câu hỏi trung tâm
> Node nào tạo phần work quyết định, estimate sai bắt đầu ở đâu, pages đến từ cache hay storage, và bằng chứng nào đủ để quy nguyên nhân?

## 1. Plan là bằng chứng, không phải toàn bộ sự thật

Execution plan là bằng chứng trực tiếp về plan PostgreSQL chọn và metrics mà instrumentation ghi trong lần chạy đó. Nó không phải “nguồn sự thật duy nhất” cho mọi latency: pool wait, lock wait, network, client fetch, concurrent I/O, storage throttling và cache state có thể nằm ngoài hoặc cần evidence khác.

Khi chẩn đoán query, plan là artifact trung tâm vì nối estimates với operators và actual work. Nhưng kết luận phải gắn query text, parameters, data snapshot, schema/indexes, statistics, settings, PostgreSQL version và load.

Một plan không có `ANALYZE` chỉ chứa estimates; một plan có `ANALYZE` đã thực thi statement. Không trộn hai loại evidence.

## 2. EXPLAIN và EXPLAIN ANALYZE

`EXPLAIN` lập plan nhưng không chạy statement. Nó an toàn hơn để xem DML nhưng không có actual rows/time. `EXPLAIN (ANALYZE)` chạy và trả actual measurements. Với `INSERT/UPDATE/DELETE/MERGE`, cần transaction rollback hoặc clone/test environment; trigger và external effects vẫn phải được xét.

Các options thường dùng: `BUFFERS`, `WAL`, `SETTINGS`, `VERBOSE`, `SUMMARY`, `TIMING`, format JSON. `BUFFERS` khi ANALYZE cho block activity; PostgreSQL 17 có thể báo planning buffers khi option phù hợp. `WAL` giúp write query.

Không bật mọi option trong production tùy tiện. `ANALYZE` gây workload thật; `TIMING` từng node có overhead trên hệ có clock-read đắt.

## 3. Đọc từ lá lên nhưng nhìn root contract

Leaves tạo rows; parents tiêu thụ. Đọc lá lên giúp thấy scan → filter → join → sort/aggregate → result. Tuy nhiên root nói output contract và total execution; bắt đầu bằng query/result expectation, rồi lần xuống leaves, không chỉ “node con chạy trước” một cách máy móc.

Plan là iterator tree; parent có thể gọi child nhiều lần. `loops` biến một inner scan nhỏ thành work lớn. Parallel plans có workers và per-worker metrics; CTE/subplans/initplans có execution pattern riêng.

Không cộng thời gian mọi node vì parent time thường bao gồm descendants. Tìm critical path/work, không tính tổng inclusive time.

## 4. Cost, rows, width

`cost=startup..total` là estimated dimensionless units. `rows` là estimated rows mỗi execution của node; `width` estimated bytes/row. Startup quan trọng cho LIMIT/first-row; total cho full consumption.

Costs không phải milliseconds và không so trực tiếp với actual time. Chúng chỉ hữu ích trong cùng planner model/config để hiểu tại sao path được chọn.

Width sai có thể làm memory/sort/hash cost sai. Projection rộng tăng I/O/network. Đừng chỉ nhìn rows.

## 5. Actual time, rows và loops

`actual time=a..b rows=r loops=l`: a là thời gian đến first row, b đến completion, trung bình mỗi loop; rows cũng là trung bình mỗi loop theo output presentation. Total row work gần `r × l`, nhưng parallel/rounding và node semantics cần thận trọng.

Một index scan `rows=1 loops=100000` làm 100000 lookups. Nhìn rows=1 rồi bỏ loops là lỗi phổ biến. Một node không executed có marker tương ứng.

Actual time là wall-clock instrumentation trong server cho node, chịu overhead. Không cộng times parent/child. Dùng buffers/loops/rows để củng cố.

## 6. Estimated versus actual cardinality

So estimated rows với actual rows tại mỗi node, đặc biệt node thấp nhất lệch mạnh. Underestimate có thể làm planner chọn nested loop, hash memory quá nhỏ hoặc join order sai; overestimate có thể tránh index/parallelize không cần.

Tính factor và hướng: actual/estimate nếu under; estimate/actual nếu over. Zero xử lý riêng. Với loops, so cùng đơn vị per-loop hoặc total rõ ràng.

Root khớp không chứng minh internals khớp vì errors có thể bù. Node đầu tiên lệch thường gần nguyên nhân statistics/predicate.

## 7. Shared, local và temp buffers

`shared hit` là block tìm thấy trong PostgreSQL shared buffers; `shared read` là block PostgreSQL phải đọc vào shared buffers. `local` dành cho local buffers của temporary relations; `temp read/written` là temporary work files, thường sort/hash/materialize spill.

Hit không đồng nghĩa zero physical I/O toàn hệ: page có thể từng được đọc trước, và OS page cache là tầng khác. Read không chắc là physical disk miss vì kernel có thể phục vụ từ page cache. `track_io_timing`/system/storage metrics giúp phân biệt thêm.

Số blocks × `block_size` cho volume gần đúng của database blocks, nhưng compressed/remote/filesystem behavior phức tạp. Buffers là work evidence, không tự là latency.

## 8. Cache ấm và cache nguội

Chạy lần hai thường nhanh vì PostgreSQL shared buffers, OS page cache, storage cache, JIT/plan/session effects. Không phải lúc nào “luôn nhanh hơn”: concurrent load, eviction, checkpoints hoặc variance có thể đảo.

Benchmark phải định nghĩa regime. Warm-cache test phản ánh repeated workload; cold-cache test cần môi trường cô lập/restart/eviction có kiểm soát, không phá production cache. `pg_prewarm`/`pg_buffercache_evict` là công cụ đặc quyền, không dùng tùy tiện.

Báo hit/read và elapsed distribution cho nhiều runs, không chọn run đẹp.

## 9. Scan diagnosis

Seq Scan: xem table size, rows removed by filter, buffers và selectivity. Index Scan: `Index Cond` vs `Filter`, heap buffers. Index-only: Heap Fetches. Bitmap: exact/lossy heap blocks và recheck.

Node “tốn nhất” không nhất thiết là node có dòng time lớn nhất do inclusive time. Một scan tạo quá nhiều rows có thể làm join/sort phía trên tốn; nguyên nhân gốc là predicate/index/estimate ở scan.

Sargability và parameter type phải kiểm cùng plan.

## 10. Join diagnosis

Nested loop: inner loops, outer actual, index lookup. Hash join: build rows, buckets/batches/memory/temp. Merge join: input ordering/sorts và rows. Join Filter/Rows Removed by Join Filter giúp thấy work thừa.

Fanout có thể là semantics đúng hoặc lỗi grain. Plan không quyết định business correctness. So expected match cardinality và result parity.

Nếu algorithm khác dự đoán, giải thích estimates/cost/available paths trước khi ép method.

## 11. Sort, hash và spill

Sort node báo method, memory hoặc disk. External merge/disk là bằng chứng spill. Hash báo batches; batches >1 thường cho thấy partitioning/temp work. Temp blocks read/written củng cố.

Spill không tự là root cause: input rows estimate sai, row width, work_mem, query shape hoặc concurrency budget đều có thể. Tăng work_mem global có rủi ro nhân memory.

Đo before/after cùng data/settings; session-local experiment.

## 12. Planning và execution time

Planning Time và Execution Time tách hai phase. Prepared statements/generic plans thay planning behavior. Client-perceived duration còn parse/protocol/network/fetch/queue.

`EXPLAIN ANALYZE` execution time có instrumentation overhead và có thể không gồm output transmission như application. `TIMING OFF` vẫn thu rows/loops và tổng execution, giảm per-node clock overhead; buffers vẫn dùng được.

So application timing với plan timing chỉ khi ranh giới đo được định nghĩa. Chênh lệch là tín hiệu điều tra, không lỗi tự thân.

## 13. Quy trình chẩn đoán bốn bước

1. Xác nhận semantics/result, parameters, environment và baseline distribution. 2. Đọc estimates/actual từ root đến node lệch đầu tiên và grain changes. 3. Đọc physical work: loops, buffers, temp, filters, heap fetches. 4. Viết một giả thuyết falsifiable, thay một thứ, rerun parity + plan + timing.

Mỗi bước ghi evidence. Không bắt đầu bằng thêm index. Không sửa stats/index/query/work_mem cùng lúc.

Nếu symptom là lock wait, plan alone thiếu; thêm pg_stat_activity/locks. Nếu client fetch, đo client.

## 14. Năm nguyên nhân lab

Tạo năm plans: stale/correlated estimate; missing index; wrong composite order; non-sargable predicate; sort/hash spill. Với mỗi plan, học viên ghi four-number card: estimate/actual factor, rows×loops, shared hit/read, node time/total context; thêm temp/heap fetch nếu liên quan.

Nguyên nhân phải nối observation. “Seq scan nên thêm index” không đủ. Plan có seq scan trên table nhỏ có thể đúng.

Rubric tách locate node và root-cause reasoning. Một người khác phải tái hiện từ artifacts.

## 15. JSON plan và plan diff

Text plan tốt cho học, JSON/YAML/XML cho automation. JSON giữ fields/children rõ, dễ tính ratios và lưu baseline. Nhưng field/version thay đổi; parser cần test theo PostgreSQL version.

Plan hash/shape change không tự là regression. So SLO, result, rows/work/buffers. Parameter classes cần nhiều baselines.

Không lưu secrets/literals nhạy cảm vào artifact công khai.

## 15.1. Ví dụ truy vết nguyên nhân

Một plan có root Aggregate 100 rows, phía dưới Nested Loop được ước lượng 500 rows nhưng thực tế 500.000 rows. Inner Index Scan báo 1 row mỗi loop và 500.000 loops; shared hit rất lớn, read gần zero. Node có elapsed đáng kể là Aggregate, nhưng nguyên nhân đầu tiên không phải aggregate hay storage: outer predicate bị underestimate 1.000 lần, làm inner lookup lặp nửa triệu lần. Hit ratio cao không cứu CPU và traversal work.

Giả thuyết “statistics của hai cột tương quan thiếu” dự đoán extended statistics làm outer estimate gần actual, planner có thể đổi join, tổng loops/buffers giảm. Sau thay đổi, phải kiểm estimate factor, plan, buffers, elapsed distribution và multiset parity. Nếu chỉ elapsed giảm ở lần chạy cache ấm nhưng estimate/loops không đổi, chưa chứng minh giả thuyết. Ví dụ này cho thấy “node tốn nhất” và “node tạo nguyên nhân” có thể khác; dossier phải ghi cả critical work lẫn earliest controllable cause.

## 16. Câu hỏi tự kiểm tra

1. Vì sao không cộng thời gian tất cả nodes?
2. `rows` và `actual time` liên hệ `loops` thế nào?
3. `shared hit` có chứng minh không physical I/O không?
4. Temp blocks và Hash Batches chỉ ra gì?
5. EXPLAIN ANALYZE có rủi ro gì với DML?
6. Bốn bước chẩn đoán ngăn trial-and-error ra sao?

## 17. Giới hạn và điều chưa cho phép kết luận

- Plan là evidence trung tâm cho server execution, không bao trùm pool/network/client/lock.
- Buffer counters không trực tiếp phân biệt OS cache với storage.
- Per-node timing có overhead và parent time thường inclusive.
- Một run không đủ kết luận performance distribution.
- Năm plans lab chưa được chạy; evidence thuộc `after-note.md`.

## Reference
1. [[SRC-POSTGRESQL-17-10-MANUAL]] — EXPLAIN/ANALYZE/BUFFERS semantics.
2. [[SRC-MASTERING-POSTGRESQL-17-6E]] — cost, plans và runtime statistics.
3. [[SRC-ROGOV-POSTGRESQL-14-INTERNALS]] — scan/join/buffer mechanisms.

## Source coverage

| Source slice | Nội dung phải giữ | Vị trí trong note | Trạng thái |
|---|---|---|---|
| [[SRC-POSTGRESQL-17-10-MANUAL]], PDF 559–580 | costs, actual rows/time/loops, BUFFERS | §§2–12 | Đã giữ measurement caveats |
| [[SRC-MASTERING-POSTGRESQL-17-6E]], PDF 223–270 | plan/cost/joins | §§4–14 | Đã nối với diagnosis |
| [[SRC-ROGOV-POSTGRESQL-14-INTERNALS]], PDF 330–407 | physical node mechanics | §§9–11 | Đã neo lại PostgreSQL 17 |
| Tổng hợp DE-L130 | four-step workflow, five-plan rubric | §§13–15 | Đã thành evidence protocol |

## Key takeaways
- Đọc plan theo cây, nhưng luôn giữ output contract và full environment.
- Estimate/actual phải đọc cùng loops; tìm node lệch đầu tiên.
- Buffers đo database block work, không tự chứng minh disk I/O.
- Parent time thường inclusive; không cộng toàn bộ node times.
- Mỗi tối ưu phải xuất phát từ một observation và giữ result parity.

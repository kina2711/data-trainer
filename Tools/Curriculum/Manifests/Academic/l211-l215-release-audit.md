# L211–L215 release audit

## Phạm vi

- L211: strong/weak scaling, Amdahl/Gustafson và chuỗi MIMD–SPMD–batch–SIMD.
- L212: broadcast, repartition, nhiều loại skew, spill lifecycle và causal diagnosis.
- L213: shared-nothing, shared-data, ba lớp cache, resize/rebalance và metadata boundary.
- L214: admission, queue/execution clocks, isolation, concurrency scaling và cache-safe load test.
- L215: workload-weighted TCO, pricing archetypes, allocation, reconciliation và reversal point.

## Kiểm tra đã chạy

- Generator: `checked=20 stale=0`.
- Batch validator: `PASS lessons=5 curriculum_files=10 knowledge_notes=5 min_words=2200 wiki_parity=5/5`.
- Formatter: `checked=388 failed=0`.
- Whole-vault coverage: `checked=138 failed=0`.
- Word counts: 2780, 2627, 2531, 2583, 2573.
- Manifest: version `1.0.42`, 110 sources, 138 notes, 461 retrieval tests.

## Ranh giới học thuật đã giữ

- MIMD, SPMD, vector batches và SIMD là bốn khái niệm ở các tầng khác nhau.
- Amdahl là fixed-work boundary; effective serial fraction không tự chỉ ra root cause.
- Weak scaling/Gustafson trả lời capacity, không thay fixed-query latency.
- Broadcast phải fit build representation sau filter/projection trên mỗi memory domain liên quan.
- Skew, spill và broadcast/repartition có thể đồng thời xuất hiện.
- Shared-data không đồng nghĩa mọi read đều đi tới remote storage vì còn local/result/metadata caches.
- Cold cache chỉ được dùng khi có operational definition; không có eviction authority thì ghi unknown.
- Queue time và execution time dẫn tới remediation khác nhau.
- Result cache được phát hiện riêng để không làm sai load test.
- Cost function là piecewise, workload-weighted và phải reconcile với billing export.
- Bytes saved không mặc nhiên làm invoice giảm khi capacity đã committed/fixed.

## Chưa kiểm bằng thực thi

- Chưa chạy strong/weak-scaling cluster lab hoặc inspect batch/SIMD code path.
- Chưa force join distributions, inject hot keys hoặc đo spill I/O trên engine thật.
- Chưa chạy cold/warm cache matrix với quyền tạo fresh compute.
- Chưa chạy concurrency load test và wrong-fix experiments.
- Chưa reconcile cost ledger với billing export/rate contract thật.
- Chưa có owner approval; artifacts giữ trạng thái `review`.

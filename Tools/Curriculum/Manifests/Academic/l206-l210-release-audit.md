# L206–L210 release audit

## Phạm vi

- L206: zone maps, statistics, năm tầng pruning, predicate blockers, safety và dynamic filtering.
- L207: vector batches, selection vectors, late materialization, encoded execution và reversal cases.
- L208: tách engine vectorization, compiler vectorization và SIMD hardware bằng counterfactual có proof.
- L209: partitioning, clustering và sort order như bài toán Pareto theo workload và write maintenance.
- L210: coordinator, fragments, exchanges, join distribution, skew, critical path và scaling laws.

## Kiểm tra đã chạy

- Generator: `checked=20 stale=0`.
- Batch validator: `PASS lessons=5 curriculum_files=10 knowledge_notes=5 min_words=2200 wiki_parity=5/5`.
- Formatter: `checked=369 failed=0`.
- Whole-vault coverage: `checked=133 failed=0`.
- Word counts: 2827, 2711, 2825, 2823, 2804.
- Manifest: version `1.0.41`, 101 sources, 133 notes, 446 retrieval tests.

## Ranh giới học thuật đã giữ

- Pruning chỉ an toàn khi chứng minh unit không thể khớp; false positive được phép, false negative không được phép.
- Filter hoặc dynamic-filter annotation trong plan không chứng minh physical skip đã xảy ra.
- Function wrapping và casts có thể chặn pruning, nhưng kết quả phụ thuộc optimizer, semantics và phiên bản.
- Vector batches, compiler vectorization và SIMD instructions là ba tầng khác nhau.
- Lợi ích batching và SIMD có interaction; không cộng hai tỷ lệ phần trăm như hai phần độc lập.
- Late materialization, encoded execution và clustering đều có reversal cases.
- High-cardinality partitioning tạo rủi ro fragmentation; không tự động suy ra một số lượng file cố định.
- Exchange là boundary phân phối trung gian quan trọng, nhưng không phải nơi duy nhất data có thể đi qua network.
- Thêm worker không bảo đảm query nhanh hơn vì critical path, skew, serial fraction, split count và coordinator overhead.

## Chưa kiểm bằng thực thi

- Chưa chạy full-scan oracle và pruning counters trên engine thật.
- Chưa inspect compiler remarks/disassembly hoặc PMU counters cho ba cấu hình vectorization/SIMD.
- Chưa benchmark layout matrix với file-size distribution và write-maintenance cost.
- Chưa chạy MPP query để đo exchange bytes, skew, blocked time và strong/weak scaling.
- Chưa có owner approval; artifacts giữ trạng thái `review`.

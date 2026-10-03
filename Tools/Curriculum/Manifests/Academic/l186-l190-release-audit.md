# L186–L190 release audit

## Phạm vi

- L186: question decomposition and metric tree.
- L187: bidirectional requirements traceability.
- L188: data-product anatomy and maturity.
- L189: analytical public interface design.
- L190: consumer-observed contract compatibility.

## Kiểm tra đã chạy

- Generator: `checked=20 stale=0`.
- Batch validator: `PASS lessons=5 curriculum_files=10 knowledge_notes=5 min_words=2200 wiki_parity=5/5`.
- Formatter: `checked=302 failed=0`.
- Whole-vault coverage: `checked=113 failed=0`.
- Word counts: 2627, 2538, 2510, 2477, 2454.
- Manifest: version `1.0.37`, 74 sources, 113 notes, 386 retrieval tests.

## Ranh giới học thuật đã giữ

- Metric-tree identity, partition và causal edges được phân biệt; cân bằng đại số không chứng minh quan hệ nhân quả.
- External driver có thể hữu ích nhưng không bị gọi là controllable lever.
- OpenLineage technical graph không được gọi là decision traceability hoàn chỉnh.
- Dataset, mart, dashboard, semantic model, metric API và data product được giữ thành sáu khái niệm riêng.
- Tám thuộc tính data product là rubric tổng hợp của giáo trình, không gán nguyên văn cho Data Mesh.
- Public surface tối thiểu vẫn phải lộ trust metadata cần thiết như version/cutoff/completeness.
- Additive schema change không mặc nhiên an toàn với mọi consumer.

## Chưa kiểm bằng thực thi

- Chưa kiểm causal edges bằng experiment hoặc field evidence.
- Chưa chạy traceability matrix trên catalog/lineage system thật.
- Chưa chấm ba products thật hoặc phỏng vấn consumers.
- Chưa chạy strict/tolerant consumer workload qua expand–migrate–contract.
- Chưa có owner approval; artifacts giữ trạng thái `review`.

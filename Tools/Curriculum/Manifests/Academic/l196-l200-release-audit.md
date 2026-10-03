# L196–L200 release audit

## Phạm vi

- L196: policy parity, negative authorization, workload contract, overload và de-identification trên BI, SQL, API.
- L197: adoption, retention, task success, decision evidence, support dependence và chống gaming.
- L198: boundary, direct/shared/unallocated cost, labor evidence, unit economics và retirement safeguards.
- L199: reverse ETL, state authority, identity, idempotency, purpose limitation và feedback loop.
- L200: lifecycle state machine, certification, operating ownership, feedback, deprecation và removal.

## Kiểm tra đã chạy

- Generator: `checked=20 stale=0`.
- Batch validator: `PASS lessons=5 curriculum_files=10 knowledge_notes=5 min_words=2200 wiki_parity=5/5`.
- Formatter: `checked=337 failed=0`.
- Whole-vault coverage: `checked=123 failed=0`.
- Word counts: 2865, 2816, 2837, 2793, 2819; tất cả vượt 2200 từ.
- Manifest: version `1.0.39`, 89 sources, 123 notes, 416 retrieval tests.

## Ranh giới học thuật đã giữ

- Policy intent được thống nhất giữa ba bề mặt nhưng implementation và error text không bị ép giống nhau.
- p95 chỉ được diễn giải cùng workload, data, cache state, concurrency và observation window.
- Masking direct identifiers không được trình bày như bằng chứng đủ về de-identification.
- Dashboard count là activity/output count; không khẳng định có tương quan nghịch với chất lượng khi chưa có dữ liệu.
- Cross-check rate không được coi là nghịch đảo trực tiếp của trust; lý do kiểm lại phải được phân loại.
- Labor cost lớn nhất chỉ là giả thuyết cần time evidence, không phải quy luật.
- Reverse ETL không tự biến warehouse thành system of record; side-effect command được tách khỏi state upsert.
- Câu hỏi lặp lại là tín hiệu điều tra, không tự động là design defect hay training failure.
- Catalog entry không tự tạo certification; lifecycle transitions cần bằng chứng và owner.

## Chưa kiểm bằng thực thi

- Chưa chạy authorization parity và load/overload test trên ba hệ thống thật.
- Chưa đo adoption bằng event stream của người dùng đại diện hoặc đánh giá tác động nhân quả.
- Chưa reconcile billing, labor logs và shared-cost allocation của một sản phẩm thật.
- Chưa fault-inject một reverse-ETL destination hoặc kiểm privacy/legal approval.
- Chưa diễn tập lifecycle, on-call, deprecation và hidden-consumer removal với một đội vận hành thật.
- Chưa có owner approval; artifacts giữ trạng thái `review`.

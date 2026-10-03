# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 16: Data Ingestion and Integration Engineering
# Lesson 231: Source Discovery and the Extraction Contract

## Mục tiêu bài học

**Năng lực cần chứng minh.** Nộp hợp đồng trích xuất đủ tám nhóm cho một nguồn thật và chỉ ra rủi ro của từng nhóm còn trống.

**Điều kiện hoàn thành.** ≥ 6/8 nhóm có câu trả lời cụ thể, giá trị canh chừng được dò bằng thống kê thật, và mọi nhóm trống kèm chế độ hỏng dự đoán.

> [!abstract] Câu hỏi trung tâm
> Một hợp đồng trích xuất cần trả lời gì trước khi chọn connector hoặc viết pipeline?

## 1. Tám nhóm bắt buộc

Hợp đồng gồm: owner/access; entities/grain/keys; schema/types/nullable semantics; change semantics; extraction interface and ordering; volume/rate/latency; quality/reconciliation; security/retention/deletion. Mỗi nhóm ghi source fact, evidence locator, verified date, unknown và owner. Tên endpoint hoặc bảng chưa phải contract. Một ô trống phải dẫn tới failure hypothesis cụ thể để ưu tiên discovery.

## 2. Owner và access boundary

Ghi system owner, business owner, read account, scopes, environments, network path, credential rotation và support/escalation. “Có quyền đọc” không chứng minh được consistent snapshot, log retention hoặc API historical access. Least privilege và production load budget là constraints. Secret value không nằm trong note; chỉ lưu secret reference và rotation procedure.

## 3. Entity grain và identity

Mỗi stream/table nêu một record đại diện gì, natural/technical key, key stability, duplicate policy, parent-child cardinality và ordering. API object ID có thể tái sử dụng hoặc scoped theo tenant. Composite keys và mutable identifiers cần fixture. Grain sai làm dedup/upsert/reconciliation vô nghĩa dù pipeline chạy xanh.

## 4. Change và time contract

Xác định insert, in-place update, backdated correction, hard delete, soft delete, restore, merge/split và schema change. Phân biệt event time, source commit time, updated_at và extraction time. Cursor phải có ordering, granularity, tie rule, timezone, mutability và retention. Unknown được dò bằng repeated snapshots/change logs, không đoán từ column name.

## 5. Capacity và quality

Đo rows/bytes distribution theo ngày/hour, peak, max record, pagination, rate limits, source query budget và expected latency. Dò sentinel values bằng full or statistically justified profile: null tokens, zero dates, magic IDs, truncation, invalid enum. Reconciliation thiết kế trước extraction: count, key set, aggregates và canonical hash at immutable boundary.

## 6. Discovery deliverable

Nộp contract versioned cùng evidence: docs locator, schema dump, sample hashes, profile queries/results, permission test và open questions. ≥6/8 groups cụ thể chưa đủ production approval; remaining unknowns có owner/deadline/containment. Chọn one representative entity để dry-run snapshot and rerun. Contract changes trigger compatibility and backfill assessment.

## 7. Ma trận kiểm chứng từng mệnh đề

Mỗi claim phải gắn source/entity boundary, exact fixture, checkpoint/input state, counterexample và independent reconciliation oracle. Connector chạy thành công hoặc API trả 2xx chưa chứng minh completeness.

### 7.1. Extraction-contract probe 1: evidence, unknown, failure mode, owner và verification test phải đủ

**Mệnh đề cần kiểm.** Extraction-contract probe 1: evidence, unknown, failure mode, owner và verification test phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.2. Extraction-contract probe 2: evidence, unknown, failure mode, owner và verification test phải đủ

**Mệnh đề cần kiểm.** Extraction-contract probe 2: evidence, unknown, failure mode, owner và verification test phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.3. Extraction-contract probe 3: evidence, unknown, failure mode, owner và verification test phải đủ

**Mệnh đề cần kiểm.** Extraction-contract probe 3: evidence, unknown, failure mode, owner và verification test phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.4. Extraction-contract probe 4: evidence, unknown, failure mode, owner và verification test phải đủ

**Mệnh đề cần kiểm.** Extraction-contract probe 4: evidence, unknown, failure mode, owner và verification test phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.5. Extraction-contract probe 5: evidence, unknown, failure mode, owner và verification test phải đủ

**Mệnh đề cần kiểm.** Extraction-contract probe 5: evidence, unknown, failure mode, owner và verification test phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.6. Extraction-contract probe 6: evidence, unknown, failure mode, owner và verification test phải đủ

**Mệnh đề cần kiểm.** Extraction-contract probe 6: evidence, unknown, failure mode, owner và verification test phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.7. Extraction-contract probe 7: evidence, unknown, failure mode, owner và verification test phải đủ

**Mệnh đề cần kiểm.** Extraction-contract probe 7: evidence, unknown, failure mode, owner và verification test phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.8. Extraction-contract probe 8: evidence, unknown, failure mode, owner và verification test phải đủ

**Mệnh đề cần kiểm.** Extraction-contract probe 8: evidence, unknown, failure mode, owner và verification test phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.9. Extraction-contract probe 9: evidence, unknown, failure mode, owner và verification test phải đủ

**Mệnh đề cần kiểm.** Extraction-contract probe 9: evidence, unknown, failure mode, owner và verification test phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.10. Extraction-contract probe 10: evidence, unknown, failure mode, owner và verification test phải đủ

**Mệnh đề cần kiểm.** Extraction-contract probe 10: evidence, unknown, failure mode, owner và verification test phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.11. Extraction-contract probe 11: evidence, unknown, failure mode, owner và verification test phải đủ

**Mệnh đề cần kiểm.** Extraction-contract probe 11: evidence, unknown, failure mode, owner và verification test phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.12. Extraction-contract probe 12: evidence, unknown, failure mode, owner và verification test phải đủ

**Mệnh đề cần kiểm.** Extraction-contract probe 12: evidence, unknown, failure mode, owner và verification test phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.13. Extraction-contract probe 13: evidence, unknown, failure mode, owner và verification test phải đủ

**Mệnh đề cần kiểm.** Extraction-contract probe 13: evidence, unknown, failure mode, owner và verification test phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.14. Extraction-contract probe 14: evidence, unknown, failure mode, owner và verification test phải đủ

**Mệnh đề cần kiểm.** Extraction-contract probe 14: evidence, unknown, failure mode, owner và verification test phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.15. Extraction-contract probe 15: evidence, unknown, failure mode, owner và verification test phải đủ

**Mệnh đề cần kiểm.** Extraction-contract probe 15: evidence, unknown, failure mode, owner và verification test phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

## 8. Quy trình phản biện

1. Chốt entity, grain, identity và immutable boundary.
2. Tách source fact, documentation claim và observed behavior.
3. Viết delete, retry, checkpoint và replay semantics trước code.
4. Dùng key/typed-hash reconciliation, không chỉ row count.
5. Pin version, retention, timezone, ordering và rate limits.
6. Ghi assumption bị falsify và extraction pattern thay thế.

## 9. Câu hỏi tự kiểm tra

1. Source thay đổi row/entity theo những operation nào?
2. Boundary nào định nghĩa complete?
3. Delete có xuất hiện trong interface không?
4. Cursor/order có total và immutable không?
5. Crash ở checkpoint boundary gây replay hay gap?
6. Bằng chứng nào chưa được chạy?

## 10. Giới hạn và điều chưa cho phép kết luận

- Chưa chạy mutation/pagination/watermark lab trên source thật.
- Product behavior phải pin version, retention và configuration.
- Decision matrices và failure protocols là synthesis của giáo trình.
- Note giữ trạng thái `review` tới khi chủ dự án duyệt.

## Reference
1. [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]]
2. [[SRC-KLEPPMANN-DDIA-1E]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]] | Source/change/API contract hoặc engineering context | Đã đọc locator; không suy ngoài phạm vi |
| [[SRC-KLEPPMANN-DDIA-1E]] | Source/change/API contract hoặc engineering context | Đã đọc locator; không suy ngoài phạm vi |

## Key takeaways
- Extraction pattern chỉ đúng khi source assumptions đúng.
- Completeness cần immutable boundary và reconciliation oracle.
- Retry/checkpoint ưu tiên replay có kiểm soát hơn silent gap.
- Connector không chuyển giao ownership về tính đúng.

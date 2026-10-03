# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 16: Data Ingestion and Integration Engineering
# Lesson 240: Atomic Landing and Checkpoint Ordering

## Mục tiêu bài học

**Năng lực cần chứng minh.** Chứng minh bằng thực nghiệm rằng hỏng ở mọi ranh giới đều không mất dữ liệu và không trùng ngoài giới hạn đã nêu.

**Điều kiện hoàn thành.** Mọi ranh giới hỏng đều phục hồi được với đối soát khớp, và bản đảo thứ tự được chứng minh mất dữ liệu kèm số dòng cụ thể.

> [!abstract] Câu hỏi trung tâm
> Tại sao thứ tự land–validate–publish–checkpoint quyết định replay thay vì silent loss?

## 1. Four-step invariant

Acquire source interval/page/chunk; write immutable staging/raw object; validate integrity/schema/reconciliation and atomically publish accepted batch; only then advance source checkpoint. Durable publication includes manifest/catalog pointer or target transaction according to design. Checkpoint points to highest fully published/recoverable boundary, never highest fetched. State transition and idempotency key are persisted.

## 2. Failure windows

Crash before land: refetch. After land before validate: resume validation or discard staging. After validate before publish: retry publish same batch. After publish before checkpoint: replay source but dedup recognizes already published batch. Checkpoint before publish is fatal gap: source resumes past missing data with no error. Table lists every boundary, observable artifacts and recovery action.

## 3. Atomic publication

Single database transaction can couple target rows and checkpoint if same system. Object storage uses immutable objects plus atomic manifest/catalog pointer; multi-object existence alone is not atomic. Cross-system landing and checkpoint cannot use local transaction; choose outbox/state machine/reconciliation so ambiguity leads to replay, not skip. Exactly-once claim is scoped and proven.

## 4. Idempotency ledger

Batch identity derives from source, entity, interval/cursor and schema/config version; content hash detects collision. Ledger states prepared, landed, validated, published, checkpointed with compare-and-set/unique constraints. Retry same identity resumes. Same identity different hash quarantines. Garbage collection only after publication/checkpoint and retention evidence.

## 5. Reconciliation

After publish compare expected source-at-boundary counts/key hashes/aggregates with accepted batch and target. Checkpoint advance condition includes required validation; tolerances need owner and named cause. Metrics: pending age, gap between published and checkpointed, replay count, collision, quarantine and residual. A green job status without boundary reconciliation is insufficient.

## 6. Kill-point lab

Implement correct and intentionally inverted flows. Kill between every adjacent step, restart and compare canonical key/hash with fixed source boundary. Correct flow may replay but never gaps; dedup bounds duplicates. In inverted flow advance checkpoint then kill before publish; quantify missing keys/rows and show subsequent runs skip them. Preserve state ledger and exact kill point as evidence.

## 7. Ma trận kiểm chứng từng mệnh đề

Mỗi claim phải gắn source/entity boundary, exact fixture, checkpoint/input state, counterexample và independent reconciliation oracle. Connector chạy thành công hoặc API trả 2xx chưa chứng minh completeness.

### 7.1. Atomic-landing probe 1: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ

**Mệnh đề cần kiểm.** Atomic-landing probe 1: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.2. Atomic-landing probe 2: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ

**Mệnh đề cần kiểm.** Atomic-landing probe 2: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.3. Atomic-landing probe 3: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ

**Mệnh đề cần kiểm.** Atomic-landing probe 3: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.4. Atomic-landing probe 4: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ

**Mệnh đề cần kiểm.** Atomic-landing probe 4: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.5. Atomic-landing probe 5: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ

**Mệnh đề cần kiểm.** Atomic-landing probe 5: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.6. Atomic-landing probe 6: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ

**Mệnh đề cần kiểm.** Atomic-landing probe 6: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.7. Atomic-landing probe 7: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ

**Mệnh đề cần kiểm.** Atomic-landing probe 7: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.8. Atomic-landing probe 8: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ

**Mệnh đề cần kiểm.** Atomic-landing probe 8: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.9. Atomic-landing probe 9: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ

**Mệnh đề cần kiểm.** Atomic-landing probe 9: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.10. Atomic-landing probe 10: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ

**Mệnh đề cần kiểm.** Atomic-landing probe 10: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.11. Atomic-landing probe 11: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ

**Mệnh đề cần kiểm.** Atomic-landing probe 11: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.12. Atomic-landing probe 12: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ

**Mệnh đề cần kiểm.** Atomic-landing probe 12: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.13. Atomic-landing probe 13: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ

**Mệnh đề cần kiểm.** Atomic-landing probe 13: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.14. Atomic-landing probe 14: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ

**Mệnh đề cần kiểm.** Atomic-landing probe 14: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.15. Atomic-landing probe 15: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ

**Mệnh đề cần kiểm.** Atomic-landing probe 15: source boundary, durable state, kill point, restart path và no-gap oracle phải đủ.

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
1. [[SRC-KLEPPMANN-DDIA-1E]]
2. [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]]
3. [[SRC-AWS-S3-MULTIPART-UPLOAD]]
4. [[SRC-AWS-S3-OBJECT-CHECKSUMS]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-KLEPPMANN-DDIA-1E]] | Source/change/API contract hoặc engineering context | Đã đọc locator; không suy ngoài phạm vi |
| [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]] | Source/change/API contract hoặc engineering context | Đã đọc locator; không suy ngoài phạm vi |
| [[SRC-AWS-S3-MULTIPART-UPLOAD]] | Source/change/API contract hoặc engineering context | Đã đọc locator; không suy ngoài phạm vi |
| [[SRC-AWS-S3-OBJECT-CHECKSUMS]] | Source/change/API contract hoặc engineering context | Đã đọc locator; không suy ngoài phạm vi |

## Key takeaways
- Extraction pattern chỉ đúng khi source assumptions đúng.
- Completeness cần immutable boundary và reconciliation oracle.
- Retry/checkpoint ưu tiên replay có kiểm soát hơn silent gap.
- Connector không chuyển giao ownership về tính đúng.

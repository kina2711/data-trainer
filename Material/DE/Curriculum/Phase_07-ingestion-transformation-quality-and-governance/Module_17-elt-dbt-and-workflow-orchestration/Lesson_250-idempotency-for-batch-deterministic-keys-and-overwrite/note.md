# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 250: Batch Idempotency Deterministic Keys and Overwrite

## Mục tiêu bài học

**Năng lực cần chứng minh.** Chọn và cài cơ chế luỹ đẳng cho bốn đường dẫn, chứng minh chạy lại nhiều lần cho cùng trạng thái.

**Điều kiện hoàn thành.** Trạng thái sau 20 lần chạy chồng chéo khớp trạng thái của một lần chạy sạch ở cả bốn đường dẫn.

> [!abstract] Câu hỏi trung tâm
> Một batch rerun cần identity, deterministic computation và publication protocol nào để cho cùng accepted state?

## 1. Định nghĩa đúng phạm vi

Idempotency nghĩa là áp cùng logical operation nhiều lần tạo cùng externally observable accepted state trong scope/time window đã nêu. Nó không có nghĩa mọi lần chạy tạo byte-identical files, không phát log hay không tốn compute. Chốt target grain, history policy, side effects và observation boundary trước test.

## 2. Deterministic batch identity

Identity ghép source/entity, immutable interval/snapshot, contract/schema version và transformation code/config version; content hash phát hiện collision. Scheduler run ID không phải logical identity vì retry sinh run mới. Same identity same input resumes/dedups; same identity different hash quarantines. Idempotency retention phải phủ retry/backfill horizon.

## 3. Deterministic rows

Key từ stable business/source identity và grain; tránh random UUID/current time/unordered row_number. Canonical timezone, decimal, null, sort/tie rules và nondeterministic SQL functions. Dedup có total ordering; nếu two records tie hoàn toàn, contract phải quarantine hoặc define deterministic rule, không chọn tùy physical order.

## 4. Overwrite safely

Build complete partition/table version separately, validate, then atomic swap/pointer. `delete where` rồi insert trong separate commits không idempotent dưới crash. Insert overwrite phụ thuộc adapter/partition predicate and transaction semantics. Re-running exact batch replaces same logical scope, không xóa dữ liệu ngoài interval.

## 5. Side effects và checkpoint

Audit, notification, downstream trigger và checkpoint cũng cần operation identity/outbox/dedup. Data table đúng nhưng gửi notification hai lần vẫn chưa idempotent end-to-end. Checkpoint advances after durable publish; crash after publish before checkpoint causes replay absorbed by ledger. External sinks có idempotency key hoặc reconciliation/manual state.

## 6. Property test

Run same batch twice, kill at each step, reorder inputs, vary worker count và replay overlapping batches. Compare canonical key set/typed hashes/current-history views and side-effect ledger. Inject same ID different content. Pass only when state converges, no out-of-scope deletion and every duplicate/collision explainable. Preserve input/version/fingerprint.

## 7. Ma trận kiểm chứng từng mệnh đề

Mỗi claim phải gắn source/entity boundary, exact fixture, checkpoint/input state, counterexample và independent reconciliation oracle. Connector chạy thành công hoặc API trả 2xx chưa chứng minh completeness.

### 7.1. Batch-idempotency probe 1: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ

**Mệnh đề cần kiểm.** Batch-idempotency probe 1: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.2. Batch-idempotency probe 2: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ

**Mệnh đề cần kiểm.** Batch-idempotency probe 2: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.3. Batch-idempotency probe 3: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ

**Mệnh đề cần kiểm.** Batch-idempotency probe 3: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.4. Batch-idempotency probe 4: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ

**Mệnh đề cần kiểm.** Batch-idempotency probe 4: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.5. Batch-idempotency probe 5: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ

**Mệnh đề cần kiểm.** Batch-idempotency probe 5: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.6. Batch-idempotency probe 6: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ

**Mệnh đề cần kiểm.** Batch-idempotency probe 6: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.7. Batch-idempotency probe 7: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ

**Mệnh đề cần kiểm.** Batch-idempotency probe 7: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.8. Batch-idempotency probe 8: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ

**Mệnh đề cần kiểm.** Batch-idempotency probe 8: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.9. Batch-idempotency probe 9: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ

**Mệnh đề cần kiểm.** Batch-idempotency probe 9: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.10. Batch-idempotency probe 10: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ

**Mệnh đề cần kiểm.** Batch-idempotency probe 10: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.11. Batch-idempotency probe 11: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ

**Mệnh đề cần kiểm.** Batch-idempotency probe 11: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.12. Batch-idempotency probe 12: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ

**Mệnh đề cần kiểm.** Batch-idempotency probe 12: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.13. Batch-idempotency probe 13: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ

**Mệnh đề cần kiểm.** Batch-idempotency probe 13: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.14. Batch-idempotency probe 14: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ

**Mệnh đề cần kiểm.** Batch-idempotency probe 14: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.15. Batch-idempotency probe 15: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ

**Mệnh đề cần kiểm.** Batch-idempotency probe 15: logical identity, deterministic key/order, kill point, side-effect ledger và convergence oracle phải đủ.

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
1. [[SRC-DBT-INCREMENTAL-MODELS]]
2. [[SRC-STRIPE-IDEMPOTENT-REQUESTS]]
3. [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]]
4. [[SRC-KLEPPMANN-DDIA-1E]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-DBT-INCREMENTAL-MODELS]] | Source/change/API contract hoặc engineering context | Đã đọc locator; không suy ngoài phạm vi |
| [[SRC-STRIPE-IDEMPOTENT-REQUESTS]] | Source/change/API contract hoặc engineering context | Đã đọc locator; không suy ngoài phạm vi |
| [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]] | Source/change/API contract hoặc engineering context | Đã đọc locator; không suy ngoài phạm vi |
| [[SRC-KLEPPMANN-DDIA-1E]] | Source/change/API contract hoặc engineering context | Đã đọc locator; không suy ngoài phạm vi |

## Key takeaways
- Extraction pattern chỉ đúng khi source assumptions đúng.
- Completeness cần immutable boundary và reconciliation oracle.
- Retry/checkpoint ưu tiên replay có kiểm soát hơn silent gap.
- Connector không chuyển giao ownership về tính đúng.

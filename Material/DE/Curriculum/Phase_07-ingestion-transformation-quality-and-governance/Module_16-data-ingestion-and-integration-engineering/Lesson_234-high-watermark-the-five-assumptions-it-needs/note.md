# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 16: Data Ingestion and Integration Engineering
# Lesson 234: High Watermark Assumptions and Overlap Deduplication

## Mục tiêu bài học

**Năng lực cần chứng minh.** Cài trích xuất theo mốc tiến độ vượt qua cả năm giả định và chứng minh không mất cũng không trùng.

**Điều kiện hoàn thành.** Số dòng, tổng và tập khoá khớp nguồn ở cả năm ca biên, và độ rộng cửa sổ chồng lấn dẫn được từ độ trễ đo được.

> [!abstract] Câu hỏi trung tâm
> Một high-watermark extractor cần năm giả định nào và kiểm chúng bằng failure injection ra sao?

## 1. Năm giả định

Một: cursor orders every relevant row/change in extraction scope. Hai: every relevant mutation advances cursor. Ba: boundary ties have deterministic unique tie-breaker or inclusive replay. Bốn: deletions are visible elsewhere or explicitly out of scope. Năm: bootstrap, target publication and checkpoint advance form recoverable protocol. Timezone, precision and source retention qualify assumptions one–three.

## 2. Composite cursor

Use lexicographic `(cursor, stable_key)` when possible. Predicate requests greater than last tuple, ordered by same tuple. If cursor alone coarse/nonunique, `>` loses tied rows; `>=` replays boundary and demands idempotent dedup. Mutable key/cursor can move backward and evade query. Store typed values, source timezone and schema version, not formatted string only.

## 3. Overlap window

Query from checkpoint minus lookback to cover measured late visibility/clock skew, then dedup/upsert by key and source version. Window derives from observed latency distribution plus safety margin and incident/backfill policy. Larger window increases load and cannot fix unbounded late changes, hard deletes or mutation with unchanged cursor. Track oldest observed lateness and reconciliation misses to revise.

## 4. Checkpoint ordering

Extract page/chunk, validate/land durably, publish/reconcile according to contract, then atomically advance checkpoint. Advancing before durable publication creates silent gap on crash. Saving checkpoint too late replays data; idempotency should absorb. Checkpoint includes cursor/tie, source boundary, schema/config version and run ID. Empty target bootstrap is explicit state, not max(NULL) accident.

## 5. Five failure fixtures

Inject clock/cursor decrease, update without cursor change, many rows with identical boundary, hard delete and first run empty target. Also kill process before/after landing and checkpoint. For each run compare count, key set, per-field hash and delete state against source at fixed boundary. A passing row count can hide missing+duplicate cancellation; key/hash oracles required.

## 6. Operational limits

Monitor watermark lag, overlap rows, dedup rate, late-beyond-window count, source query duration and reconciliation residual. Pause when checkpoint falls outside CDC/source retention. Document maximum supported lateness and delete gap. If probes falsify assumptions, migrate to CDC, periodic snapshot diff or source-side audit rather than enlarging window indefinitely.

## 7. Ma trận kiểm chứng từng mệnh đề

Mỗi claim phải gắn source/entity boundary, exact fixture, checkpoint/input state, counterexample và independent reconciliation oracle. Connector chạy thành công hoặc API trả 2xx chưa chứng minh completeness.

### 7.1. Watermark probe 1: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ

**Mệnh đề cần kiểm.** Watermark probe 1: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.2. Watermark probe 2: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ

**Mệnh đề cần kiểm.** Watermark probe 2: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.3. Watermark probe 3: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ

**Mệnh đề cần kiểm.** Watermark probe 3: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.4. Watermark probe 4: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ

**Mệnh đề cần kiểm.** Watermark probe 4: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.5. Watermark probe 5: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ

**Mệnh đề cần kiểm.** Watermark probe 5: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.6. Watermark probe 6: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ

**Mệnh đề cần kiểm.** Watermark probe 6: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.7. Watermark probe 7: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ

**Mệnh đề cần kiểm.** Watermark probe 7: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.8. Watermark probe 8: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ

**Mệnh đề cần kiểm.** Watermark probe 8: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.9. Watermark probe 9: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ

**Mệnh đề cần kiểm.** Watermark probe 9: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.10. Watermark probe 10: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ

**Mệnh đề cần kiểm.** Watermark probe 10: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.11. Watermark probe 11: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ

**Mệnh đề cần kiểm.** Watermark probe 11: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.12. Watermark probe 12: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ

**Mệnh đề cần kiểm.** Watermark probe 12: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.13. Watermark probe 13: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ

**Mệnh đề cần kiểm.** Watermark probe 13: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.14. Watermark probe 14: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ

**Mệnh đề cần kiểm.** Watermark probe 14: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.15. Watermark probe 15: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ

**Mệnh đề cần kiểm.** Watermark probe 15: assumption, injected violation, checkpoint state, dedup identity và reconciliation evidence phải đủ.

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
1. [[SRC-AIRBYTE-INCREMENTAL-APPEND-DEDUPED]]
2. [[SRC-MICROSOFT-SQL-SERVER-CDC]]
3. [[SRC-KLEPPMANN-DDIA-1E]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-AIRBYTE-INCREMENTAL-APPEND-DEDUPED]] | Source/change/API contract hoặc engineering context | Đã đọc locator; không suy ngoài phạm vi |
| [[SRC-MICROSOFT-SQL-SERVER-CDC]] | Source/change/API contract hoặc engineering context | Đã đọc locator; không suy ngoài phạm vi |
| [[SRC-KLEPPMANN-DDIA-1E]] | Source/change/API contract hoặc engineering context | Đã đọc locator; không suy ngoài phạm vi |

## Key takeaways
- Extraction pattern chỉ đúng khi source assumptions đúng.
- Completeness cần immutable boundary và reconciliation oracle.
- Retry/checkpoint ưu tiên replay có kiểm soát hơn silent gap.
- Connector không chuyển giao ownership về tính đúng.

# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 16: Data Ingestion and Integration Engineering
# Lesson 245: Three Source Ingestion Capstone

## Mục tiêu bài học

**Năng lực cần chứng minh.** Nộp hệ nạp ba nguồn chạy được cả ba chế độ, với đối soát độc lập đạt cho cả ba.

**Điều kiện hoàn thành.** Ba nguồn đối soát khớp trong ngân sách đã duyệt, ba chế độ vận hành chạy được, và giết tiến trình ở mọi chế độ đều phục hồi đúng.

> [!abstract] Câu hỏi trung tâm
> Capstone ba nguồn phải tạo chuỗi bằng chứng nào để chứng minh raw zone complete, replayable và vận hành được?

## 1. Ba nguồn có semantics khác

Case gồm API có cursor/rate limit, database snapshot plus changes và file drop có manifest. Mỗi nguồn có extraction contract riêng; không ép chung một watermark. Raw zone dùng shared envelope nhưng giữ source-native boundary, identity, schema/version và payload fidelity. Capstone chấm tính đúng của từng path và khả năng quan sát chung.

## 2. Hồ sơ kiến trúc

Nộp source contracts, decision ADR, sequence/failure diagrams, schema registry/diffs, landing envelope, checkpoint ledger, manifest/object map, access/retention policy và runbook. Mỗi artifact có locator/version/owner. Diagram không thay executable evidence. Secret chỉ là reference; test data synthetic hoặc đã được phê duyệt.

## 3. Pipeline invariant

Thứ tự acquire, land immutable, validate/reconcile, publish và checkpoint. API page, DB chunk/log interval và file batch đều có deterministic ingestion identity. Retry có thể replay nhưng không tạo silent gap; same identity different content bị quarantine. Publication chỉ mở dữ liệu đã đủ manifest/schema/integrity checks.

## 4. Failure campaign

Inject 429, lost response, cursor expiry, snapshot chunk retry, replica lag, schema breaking change, incomplete file batch, checksum mismatch, duplicate delivery và crash ở mỗi checkpoint boundary. Expected state/action viết trước. Một job tự recover nhưng làm mất key vẫn fail. Lưu timeline, state transitions, raw hashes, metrics và reconciliation diffs.

## 5. SLO và vận hành

Định nghĩa per-source freshness/completeness/correctness cùng common incident severity. Backfill có quota riêng. Dashboard thể hiện boundary lag, pending/quarantine, retry amplification, source impact và validation residual. Runbook có triage, containment, replay, revalidation, rollback và communication. Game day có observer và stop rules.

## 6. Điều kiện bảo vệ

Đạt khi ba source boundaries truy được tới published objects; rerun cùng input cho cùng accepted state; injected loss/collision bị phát hiện; daily path giữ SLO trong test envelope; reviewer độc lập tái hiện một failure. Chưa chạy production load, security review hay legal approval thì không gọi production-ready.

## 7. Ma trận kiểm chứng từng mệnh đề

Mỗi claim phải gắn source/entity boundary, exact fixture, checkpoint/input state, counterexample và independent reconciliation oracle. Connector chạy thành công hoặc API trả 2xx chưa chứng minh completeness.

### 7.1. Capstone probe 1: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ

**Mệnh đề cần kiểm.** Capstone probe 1: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.2. Capstone probe 2: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ

**Mệnh đề cần kiểm.** Capstone probe 2: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.3. Capstone probe 3: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ

**Mệnh đề cần kiểm.** Capstone probe 3: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.4. Capstone probe 4: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ

**Mệnh đề cần kiểm.** Capstone probe 4: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.5. Capstone probe 5: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ

**Mệnh đề cần kiểm.** Capstone probe 5: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.6. Capstone probe 6: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ

**Mệnh đề cần kiểm.** Capstone probe 6: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.7. Capstone probe 7: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ

**Mệnh đề cần kiểm.** Capstone probe 7: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.8. Capstone probe 8: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ

**Mệnh đề cần kiểm.** Capstone probe 8: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.9. Capstone probe 9: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ

**Mệnh đề cần kiểm.** Capstone probe 9: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.10. Capstone probe 10: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ

**Mệnh đề cần kiểm.** Capstone probe 10: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.11. Capstone probe 11: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ

**Mệnh đề cần kiểm.** Capstone probe 11: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.12. Capstone probe 12: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ

**Mệnh đề cần kiểm.** Capstone probe 12: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.13. Capstone probe 13: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ

**Mệnh đề cần kiểm.** Capstone probe 13: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.14. Capstone probe 14: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ

**Mệnh đề cần kiểm.** Capstone probe 14: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.15. Capstone probe 15: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ

**Mệnh đề cần kiểm.** Capstone probe 15: source boundary, invariant, injected failure, evidence locator và independent oracle phải đủ.

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
2. [[SRC-AWS-DMS-DATA-VALIDATION]]
3. [[SRC-AIRBYTE-SCHEMA-CHANGE-MANAGEMENT]]
4. [[SRC-AIRBYTE-INCREMENTAL-APPEND-DEDUPED]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]] | Source/change/API contract hoặc engineering context | Đã đọc locator; không suy ngoài phạm vi |
| [[SRC-AWS-DMS-DATA-VALIDATION]] | Source/change/API contract hoặc engineering context | Đã đọc locator; không suy ngoài phạm vi |
| [[SRC-AIRBYTE-SCHEMA-CHANGE-MANAGEMENT]] | Source/change/API contract hoặc engineering context | Đã đọc locator; không suy ngoài phạm vi |
| [[SRC-AIRBYTE-INCREMENTAL-APPEND-DEDUPED]] | Source/change/API contract hoặc engineering context | Đã đọc locator; không suy ngoài phạm vi |

## Key takeaways
- Extraction pattern chỉ đúng khi source assumptions đúng.
- Completeness cần immutable boundary và reconciliation oracle.
- Retry/checkpoint ưu tiên replay có kiểm soát hơn silent gap.
- Connector không chuyển giao ownership về tính đúng.

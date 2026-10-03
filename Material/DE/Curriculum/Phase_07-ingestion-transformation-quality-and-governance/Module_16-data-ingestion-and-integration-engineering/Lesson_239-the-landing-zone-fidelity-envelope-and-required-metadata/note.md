# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 16: Data Ingestion and Integration Engineering
# Lesson 239: Landing Zone Fidelity Envelope and Metadata

## Mục tiêu bài học

**Năng lực cần chứng minh.** Thiết kế phong bì vùng thô đủ sáu trường và nêu chính sách dữ liệu nhạy cảm đi kèm.

**Điều kiện hoàn thành.** Sáu trường có mặt ở cả ba thiết kế, mỗi trường kèm câu hỏi vận hành nó trả lời, và chính sách dữ liệu nhạy cảm đủ bốn phần.

> [!abstract] Câu hỏi trung tâm
> Vùng raw cần giữ payload và metadata nào để replay, audit, privacy và reconciliation?

## 1. Fidelity envelope

Landing preserves source payload or lossless canonical representation plus metadata needed to interpret it. It is immutable/versioned evidence, not a cleaned serving table. Six minimum fields: source/entity identity, extraction boundary/cursor, ingestion/run/batch identity, event/extract/land times, schema/format/version, content checksum/object lineage. Add producer, file/page/chunk and privacy classification as required.

## 2. Why each field exists

Source/entity answers ownership and connector route. Boundary/cursor supports completeness/replay. Run/batch ID ties retries and logs. Multiple timestamps diagnose lateness without conflating clocks. Schema/version makes bytes interpretable. Checksum/lineage proves identity and integrity. If one is absent, document exact operational question that becomes unanswerable and containment.

## 3. Payload fidelity

Keep original bytes for files/API responses where rights/security allow, or record deterministic transformation and original hash. Do not silently coerce null/empty, timestamps, decimals, encodings or unknown fields. Raw can add envelope columns but must avoid collision with source names. Quarantine retains failed payload securely with reason and retry lineage.

## 4. Privacy and security

Classify sensitive fields/payloads before landing. Apply encryption in transit/at rest, least privilege, key rotation, audit, retention and deletion propagation. Raw access is narrower, not wider. Tokenization/masking may be required before persistence; then “raw” means earliest policy-compliant representation and transformation evidence. Secrets never land in payload/logs.

## 5. Retention and deletion

Retention separates active replay window, legal/audit requirements and source deletion obligations. Object lifecycle alone may delete evidence before downstream recovery. Erasure propagates across raw, manifests, backups and derived layers according to policy, with tombstone/audit where permitted. Immutable storage does not exempt privacy obligations; legal owner decides conflicts.

## 6. Three-source design

Design envelopes for API pages, database chunks/CDC and file batches. For each field map producer, format, validation, nullable conditions and operator query. Demonstrate replay from envelope without hidden scheduler state. Negative fixtures: duplicate batch, schema unknown, checksum mismatch, sensitive field, missing boundary. List content excluded: credentials, uncontrolled debug dumps and unbounded secrets/PII copies.

## 7. Ma trận kiểm chứng từng mệnh đề

Mỗi claim phải gắn source/entity boundary, exact fixture, checkpoint/input state, counterexample và independent reconciliation oracle. Connector chạy thành công hoặc API trả 2xx chưa chứng minh completeness.

### 7.1. Landing-envelope probe 1: metadata field, operational question, validation, privacy control và replay evidence phải rõ

**Mệnh đề cần kiểm.** Landing-envelope probe 1: metadata field, operational question, validation, privacy control và replay evidence phải rõ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.2. Landing-envelope probe 2: metadata field, operational question, validation, privacy control và replay evidence phải rõ

**Mệnh đề cần kiểm.** Landing-envelope probe 2: metadata field, operational question, validation, privacy control và replay evidence phải rõ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.3. Landing-envelope probe 3: metadata field, operational question, validation, privacy control và replay evidence phải rõ

**Mệnh đề cần kiểm.** Landing-envelope probe 3: metadata field, operational question, validation, privacy control và replay evidence phải rõ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.4. Landing-envelope probe 4: metadata field, operational question, validation, privacy control và replay evidence phải rõ

**Mệnh đề cần kiểm.** Landing-envelope probe 4: metadata field, operational question, validation, privacy control và replay evidence phải rõ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.5. Landing-envelope probe 5: metadata field, operational question, validation, privacy control và replay evidence phải rõ

**Mệnh đề cần kiểm.** Landing-envelope probe 5: metadata field, operational question, validation, privacy control và replay evidence phải rõ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.6. Landing-envelope probe 6: metadata field, operational question, validation, privacy control và replay evidence phải rõ

**Mệnh đề cần kiểm.** Landing-envelope probe 6: metadata field, operational question, validation, privacy control và replay evidence phải rõ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.7. Landing-envelope probe 7: metadata field, operational question, validation, privacy control và replay evidence phải rõ

**Mệnh đề cần kiểm.** Landing-envelope probe 7: metadata field, operational question, validation, privacy control và replay evidence phải rõ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.8. Landing-envelope probe 8: metadata field, operational question, validation, privacy control và replay evidence phải rõ

**Mệnh đề cần kiểm.** Landing-envelope probe 8: metadata field, operational question, validation, privacy control và replay evidence phải rõ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.9. Landing-envelope probe 9: metadata field, operational question, validation, privacy control và replay evidence phải rõ

**Mệnh đề cần kiểm.** Landing-envelope probe 9: metadata field, operational question, validation, privacy control và replay evidence phải rõ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.10. Landing-envelope probe 10: metadata field, operational question, validation, privacy control và replay evidence phải rõ

**Mệnh đề cần kiểm.** Landing-envelope probe 10: metadata field, operational question, validation, privacy control và replay evidence phải rõ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.11. Landing-envelope probe 11: metadata field, operational question, validation, privacy control và replay evidence phải rõ

**Mệnh đề cần kiểm.** Landing-envelope probe 11: metadata field, operational question, validation, privacy control và replay evidence phải rõ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.12. Landing-envelope probe 12: metadata field, operational question, validation, privacy control và replay evidence phải rõ

**Mệnh đề cần kiểm.** Landing-envelope probe 12: metadata field, operational question, validation, privacy control và replay evidence phải rõ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.13. Landing-envelope probe 13: metadata field, operational question, validation, privacy control và replay evidence phải rõ

**Mệnh đề cần kiểm.** Landing-envelope probe 13: metadata field, operational question, validation, privacy control và replay evidence phải rõ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.14. Landing-envelope probe 14: metadata field, operational question, validation, privacy control và replay evidence phải rõ

**Mệnh đề cần kiểm.** Landing-envelope probe 14: metadata field, operational question, validation, privacy control và replay evidence phải rõ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.15. Landing-envelope probe 15: metadata field, operational question, validation, privacy control và replay evidence phải rõ

**Mệnh đề cần kiểm.** Landing-envelope probe 15: metadata field, operational question, validation, privacy control và replay evidence phải rõ.

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
2. [[SRC-AWS-S3-OBJECT-CHECKSUMS]]
3. [[SRC-NIST-SP-800-188-DEIDENTIFICATION]]
4. [[SRC-KLEPPMANN-DDIA-1E]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]] | Source/change/API contract hoặc engineering context | Đã đọc locator; không suy ngoài phạm vi |
| [[SRC-AWS-S3-OBJECT-CHECKSUMS]] | Source/change/API contract hoặc engineering context | Đã đọc locator; không suy ngoài phạm vi |
| [[SRC-NIST-SP-800-188-DEIDENTIFICATION]] | Source/change/API contract hoặc engineering context | Đã đọc locator; không suy ngoài phạm vi |
| [[SRC-KLEPPMANN-DDIA-1E]] | Source/change/API contract hoặc engineering context | Đã đọc locator; không suy ngoài phạm vi |

## Key takeaways
- Extraction pattern chỉ đúng khi source assumptions đúng.
- Completeness cần immutable boundary và reconciliation oracle.
- Retry/checkpoint ưu tiên replay có kiểm soát hơn silent gap.
- Connector không chuyển giao ownership về tính đúng.

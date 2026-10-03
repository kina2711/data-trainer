# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 16: Data Ingestion and Integration Engineering
# Lesson 241: Schema Drift Detection Classification and Quarantine

## Mục tiêu bài học

**Năng lực cần chứng minh.** Cài phát hiện và phân loại lệch lược đồ ba mức, chứng minh mỗi mức đi đúng đường xử lý.

**Điều kiện hoàn thành.** Phân loại đúng ≥ 5/6 thay đổi, không lô nào bị bỏ im lặng, và lô cách ly nạp lại được với đối soát khớp.

> [!abstract] Câu hỏi trung tâm
> Schema drift được phát hiện, phân loại và cô lập thế nào để tránh vừa mất dữ liệu vừa phát tán sai nghĩa?

## 1. Ba lớp thay đổi

Tách physical schema, logical contract và semantic meaning. Thêm cột nullable có thể compatible ở storage nhưng làm downstream `select *` đổi shape; đổi enum meaning không đổi type nhưng là semantic break. Snapshot schema phải gồm field path, type, nullable, default, key/cursor role, constraints và version. Diff tên cột đơn thuần không đủ.

## 2. Phân loại theo tác động

Nhóm additive, restrictive, destructive, identity/order breaking và semantic-only. Với từng change, đánh giá reader/writer compatibility, lịch sử, backfill, downstream dependency và privacy. Xóa cursor/primary key là critical vì phá incremental identity; widening type có thể an toàn ở source nhưng không ở target. Classification dẫn tới action, không chỉ severity label.

## 3. Detect và version

Discover trước sync theo cadence có SLO, lưu canonical schema hash và diff với approved version. Event schema cũng cần registry compatibility và subject/version policy. Detection lag là một metric vì change có thể đi qua trước lần discover. Manual refresh, connector upgrade và config change đều có thể tạo diff, nên provenance của change phải được lưu.

## 4. Quarantine envelope

Quarantine giữ raw payload, source boundary, schema observed/expected, reason code, connector version, first/last seen, count/bytes và retry lineage trong vùng truy cập hẹp. Không drop record lặng lẽ, cũng không cho unknown field/type đi thẳng vào curated table. Quarantine là state có owner, TTL, disposition và replay path; không phải thư mục rác vô hạn.

## 5. Decision table

Compatible additive có thể land raw và mở field sau approval; coercible change cần explicit transform và loss test; incompatible type/key/cursor dừng affected stream; semantic-only cần owner xác nhận và downstream versioning. Backfill quyết định riêng với propagation. Same field name đổi unit/currency/timezone là breaking dù parser vẫn xanh.

## 6. Failure lab

Inject add/drop/rename/type narrowing, key removal, nested-path change, enum meaning change và connector major upgrade. Assert exact classification, pause/continue policy, zero silent loss, quarantine evidence và deterministic replay after approval. So raw count/hash trước–sau; chứng minh old readers behavior. Lưu schema snapshots, diff, decision và downstream test results.

## 7. Ma trận kiểm chứng từng mệnh đề

Mỗi claim phải gắn source/entity boundary, exact fixture, checkpoint/input state, counterexample và independent reconciliation oracle. Connector chạy thành công hoặc API trả 2xx chưa chứng minh completeness.

### 7.1. Schema-drift probe 1: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ

**Mệnh đề cần kiểm.** Schema-drift probe 1: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.2. Schema-drift probe 2: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ

**Mệnh đề cần kiểm.** Schema-drift probe 2: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.3. Schema-drift probe 3: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ

**Mệnh đề cần kiểm.** Schema-drift probe 3: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.4. Schema-drift probe 4: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ

**Mệnh đề cần kiểm.** Schema-drift probe 4: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.5. Schema-drift probe 5: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ

**Mệnh đề cần kiểm.** Schema-drift probe 5: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.6. Schema-drift probe 6: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ

**Mệnh đề cần kiểm.** Schema-drift probe 6: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.7. Schema-drift probe 7: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ

**Mệnh đề cần kiểm.** Schema-drift probe 7: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.8. Schema-drift probe 8: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ

**Mệnh đề cần kiểm.** Schema-drift probe 8: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.9. Schema-drift probe 9: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ

**Mệnh đề cần kiểm.** Schema-drift probe 9: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.10. Schema-drift probe 10: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ

**Mệnh đề cần kiểm.** Schema-drift probe 10: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.11. Schema-drift probe 11: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ

**Mệnh đề cần kiểm.** Schema-drift probe 11: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.12. Schema-drift probe 12: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ

**Mệnh đề cần kiểm.** Schema-drift probe 12: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.13. Schema-drift probe 13: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ

**Mệnh đề cần kiểm.** Schema-drift probe 13: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.14. Schema-drift probe 14: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ

**Mệnh đề cần kiểm.** Schema-drift probe 14: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ.

**Thiết kế phép thử.** Khóa source/API version, entity, grain/key, time boundary, schema, pagination/cursor configuration và failure schedule. Tạo positive, boundary và negative fixtures; thay đổi đúng một assumption. Lưu request/query, response/raw extract hash, checkpoint trước/sau, landing objects, target state và source-at-boundary oracle.

**Điều kiện chấp nhận.** Count, key set, typed field hash và delete state khớp contract; duplicates được giải thích và dedup có identity rõ. Observation, inference và unknown được báo riêng. Lab chưa chạy chỉ là protocol.

### 7.15. Schema-drift probe 15: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ

**Mệnh đề cần kiểm.** Schema-drift probe 15: observed diff, compatibility class, action, quarantine evidence và replay oracle phải đủ.

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
1. [[SRC-AIRBYTE-SCHEMA-CHANGE-MANAGEMENT]]
2. [[SRC-CONFLUENT-SCHEMA-EVOLUTION]]
3. [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-AIRBYTE-SCHEMA-CHANGE-MANAGEMENT]] | Source/change/API contract hoặc engineering context | Đã đọc locator; không suy ngoài phạm vi |
| [[SRC-CONFLUENT-SCHEMA-EVOLUTION]] | Source/change/API contract hoặc engineering context | Đã đọc locator; không suy ngoài phạm vi |
| [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]] | Source/change/API contract hoặc engineering context | Đã đọc locator; không suy ngoài phạm vi |

## Key takeaways
- Extraction pattern chỉ đúng khi source assumptions đúng.
- Completeness cần immutable boundary và reconciliation oracle.
- Retry/checkpoint ưu tiên replay có kiểm soát hơn silent gap.
- Connector không chuyển giao ownership về tính đúng.

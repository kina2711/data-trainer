# Phase 6: Analytical Storage and Query Engines
# Module 15: File, Serialization and Open Table Formats
# Lesson 223: Nested Timestamp and Decimal Interoperability

## Mục tiêu bài học

**Năng lực cần chứng minh.** Chạy phép thử vòng tròn ba kiểu dữ liệu nhạy cảm qua nhiều engine và phát hiện ít nhất một chỗ lệch.

**Điều kiện hoàn thành.** Ít nhất một chỗ lệch được phát hiện và chẩn đoán đúng, và phép thử vòng tròn chạy tự động.

> [!abstract] Câu hỏi trung tâm
> Round-trip nested data, timestamp và decimal qua nhiều engine thế nào để phát hiện sai nghĩa?

## 1. Interoperability là typed equality

Cùng đọc được file chỉ chứng minh parser chấp nhận bytes. Interoperability cần canonical logical schema, value semantics và equality oracle. So row count hoặc aggregate có thể che nested order, null versus empty, precision loss và timezone shift. Fixture phải có stable row key; mỗi engine xuất canonical representation để so từng field. Mismatch được phân loại thành schema mapping, writer encoding, reader conversion, API representation hoặc application normalization.

## 2. Nested levels

Parquet lưu leaf values cùng definition levels để biểu diễn optionality và repetition levels để biểu diễn list boundaries trong cấu trúc lồng. Các LIST/MAP encodings lịch sử và generated schemas có thể khác shape dù nhìn gần giống. Fixture phải phân biệt missing parent, null child, empty list, list containing null, empty map và nested repeated records. Flatten rồi rebuild không phải oracle nếu nó làm mất parent/position identity. So canonical JSON có explicit states và stable ordering rule.

## 3. Timestamp semantics

Timestamp cần unit, timezone adjustment contract và meaning. Milliseconds, microseconds và nanoseconds khác precision; một engine có thể truncate hoặc reject. Instant with offset, local wall-clock time và calendar date là ba concepts. DST gap/overlap, pre-epoch values, leap-related boundaries và writer timezone cần fixture. Legacy INT96 có engine-specific behavior; nếu xuất hiện phải pin reader options. So epoch instant cho instant fields và local components plus zone policy cho local fields.

## 4. Decimal semantics

Decimal mang precision và scale; physical storage có thể là int32, int64 hoặc fixed/byte array. Reader mapping sang binary floating point làm mất exactness. Fixture gồm max/min precision, trailing zeros, negative, rounding boundary và overflow. Equality business có thể quan tâm numeric value hoặc representation scale; contract phải chọn. Writer không được silently round nếu policy yêu cầu reject. Canonical oracle dùng unscaled integer cùng scale hoặc decimal string chuẩn hóa theo rule đã công bố.

## 5. Cross-engine matrix

Chọn ít nhất hai engines nhưng ghi exact versions, connectors, session timezone, schema options và language driver. Mỗi engine vừa làm writer vừa làm reader để tạo W_A→R_A, W_A→R_B, W_B→R_A, W_B→R_B. Lưu file hash, footer schema, inferred schema, typed output và warnings. Một mismatch được sửa ở writer contract nếu có thể; workaround chỉ ở reader phải được ghi như compatibility debt và có test ngăn regression.

## 6. Automation

Golden corpus nhỏ nhưng bao phủ states được version control cùng expected canonical values. Pipeline đọc tất cả files bằng tất cả supported readers, normalize theo contract rồi diff per key/field. Negative fixtures phải reject: decimal overflow, unsupported timestamp precision, invalid nested schema. Khi nâng engine/library, chạy lại matrix trước deploy. Không tự regenerate expected output bằng code đang được kiểm; owner duyệt thay đổi oracle và ghi migration rationale.

## 7. Ma trận kiểm chứng từng mệnh đề

Mỗi claim phải chỉ rõ metadata scope, writer/reader version, exact fixture, counterexample và oracle. File parse được, plan có predicate hoặc metadata tồn tại chưa đủ để kết luận physical I/O hay semantic result đúng.

### 7.1. Interoperability probe 1: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ

**Mệnh đề cần kiểm.** Interoperability probe 1: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.2. Interoperability probe 2: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ

**Mệnh đề cần kiểm.** Interoperability probe 2: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.3. Interoperability probe 3: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ

**Mệnh đề cần kiểm.** Interoperability probe 3: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.4. Interoperability probe 4: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ

**Mệnh đề cần kiểm.** Interoperability probe 4: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.5. Interoperability probe 5: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ

**Mệnh đề cần kiểm.** Interoperability probe 5: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.6. Interoperability probe 6: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ

**Mệnh đề cần kiểm.** Interoperability probe 6: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.7. Interoperability probe 7: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ

**Mệnh đề cần kiểm.** Interoperability probe 7: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.8. Interoperability probe 8: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ

**Mệnh đề cần kiểm.** Interoperability probe 8: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.9. Interoperability probe 9: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ

**Mệnh đề cần kiểm.** Interoperability probe 9: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.10. Interoperability probe 10: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ

**Mệnh đề cần kiểm.** Interoperability probe 10: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.11. Interoperability probe 11: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ

**Mệnh đề cần kiểm.** Interoperability probe 11: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.12. Interoperability probe 12: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ

**Mệnh đề cần kiểm.** Interoperability probe 12: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.13. Interoperability probe 13: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ

**Mệnh đề cần kiểm.** Interoperability probe 13: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.14. Interoperability probe 14: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ

**Mệnh đề cần kiểm.** Interoperability probe 14: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.15. Interoperability probe 15: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ

**Mệnh đề cần kiểm.** Interoperability probe 15: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

## 8. Quy trình phản biện

1. Xác định tầng đang nói: object store, file, table metadata, catalog hay engine.
2. Viết identity và publication boundary trước khi bàn hiệu năng.
3. Tách metadata presence, planner intent, executed pruning và physical I/O.
4. Kiểm semantic result bằng typed oracle trước benchmark.
5. Pin version, configuration, cache state và metric definition.
6. Ghi counterexample, limitation và reversal condition cho recommendation.

## 9. Câu hỏi tự kiểm tra

1. Đơn vị đang xét là file, row group, column chunk, page, manifest hay snapshot?
2. Metadata nào authoritative và lấy từ locator nào?
3. Reader có dùng metadata hay chỉ có khả năng dùng?
4. Parse/decode thành công có che semantic mismatch không?
5. Failure ở trước hay sau publication boundary?
6. Bằng chứng nào còn là protocol chưa chạy?

## 10. Giới hạn và điều chưa cho phép kết luận

- Chưa chạy Parquet footer/page-index lab hoặc Iceberg metadata trace trên engine/catalog thật.
- Đặc tả được kiểm ngày 2026-10-02; implementation behavior phải pin version.
- Matrices và lab protocols là synthesis của giáo trình, không gán nguyên văn cho một nguồn.
- Note giữ trạng thái `review` tới khi chủ dự án duyệt.

## Reference
1. [[SRC-APACHE-PARQUET-FILE-FORMAT]]
2. [[SRC-APACHE-ICEBERG-SPEC]]
3. [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-APACHE-PARQUET-FILE-FORMAT]] | Format/table contract, implementation boundary hoặc workload context | Đã đọc locator; không suy ngoài phạm vi |
| [[SRC-APACHE-ICEBERG-SPEC]] | Format/table contract, implementation boundary hoặc workload context | Đã đọc locator; không suy ngoài phạm vi |
| [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]] | Format/table contract, implementation boundary hoặc workload context | Đã đọc locator; không suy ngoài phạm vi |

## Key takeaways
- Mọi claim phải đúng tầng và đúng granularity.
- Metadata hiện diện, planner intent, executed pruning và physical I/O là bốn bằng chứng khác nhau.
- Semantic oracle được kiểm trước performance attribution.
- Chưa chạy lab thì note cung cấp giáo trình và protocol, chưa phải certification cho production.

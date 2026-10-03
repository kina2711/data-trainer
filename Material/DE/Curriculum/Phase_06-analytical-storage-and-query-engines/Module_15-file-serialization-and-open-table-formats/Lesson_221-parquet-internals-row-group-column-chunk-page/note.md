# Phase 6: Analytical Storage and Query Engines
# Module 15: File, Serialization and Open Table Formats
# Lesson 221: Parquet File Row Group Column Chunk and Page

## Mục tiêu bài học

**Năng lực cần chứng minh.** Đọc siêu dữ liệu thật của một tệp và giải thích đơn vị nào được cắt tỉa, đơn vị nào được đọc.

**Điều kiện hoàn thành.** Siêu dữ liệu chân tệp của ba phương án được đọc và ghi lại, và lựa chọn kích thước nhóm hàng dẫn được từ ba số đo.

> [!abstract] Câu hỏi trung tâm
> Đọc footer Parquet thế nào để phân biệt đơn vị bố trí, pruning và I/O thực tế?

## 1. Bốn tầng vật lý

Một Parquet file chứa nhiều row groups. Trong mỗi row group, mỗi leaf column có một column chunk liên tục; column chunk lại gồm data pages và có thể có dictionary page. Page là đơn vị encoding/compression nhỏ, row group là horizontal partition logic của file, còn column chunk là phần dữ liệu của một cột trong đúng row group. Gọi row group là block lưu trữ vật lý hoặc gọi page là cột đều làm sai phép đo. Nested field được hạ xuống leaf columns kèm definition/repetition levels, nên số cột logic và số column chunks không luôn trùng cách người học nhìn schema.

## 2. Footer và đường đọc

File bắt đầu và kết thúc bằng magic bytes; ngay trước magic cuối là độ dài footer và FileMetaData. Reader thường lấy phần đuôi để biết schema, row groups, column chunk offsets, codecs, encodings, statistics và các index locations có mặt. Footer cho biết nơi cần đọc, không phải bằng chứng bytes đã đi qua network. Một engine có thể prefetch, cache, coalesce ranges hoặc đọc metadata qua catalog. Báo cáo phải tách logical bytes, compressed bytes, requested ranges, transferred bytes và bytes decoded.

## 3. Statistics và pruning boundary

Min, max, null count và distinct count nếu có được gắn ở scope cụ thể. Row-group statistics có thể loại cả row group khi predicate chứng minh không giao miền; page index có thể loại pages khi writer tạo index và reader sử dụng. Thiếu statistics, truncated bounds, NaN, null semantics hoặc collation khác làm pruning yếu hay không an toàn. Statistics là conservative evidence: giữ thêm false positives được, bỏ false negatives thì sai dữ liệu. Footer inspection phải ghi cột nào có statistic và scope nào thực sự được reader dùng.

## 4. Kích thước row group

Row group lớn tăng sequential I/O và thường cải thiện compression do nhiều giá trị chung, nhưng writer cần buffer lớn hơn, selective query có granularity thô hơn và parallelism bị giới hạn khi có ít groups. Row group nhỏ tăng scheduling/metadata overhead và có thể làm dictionary kém hiệu quả, nhưng tạo nhiều đơn vị pruning và tasks. Con số 512 MB–1 GB trong tài liệu Parquet gắn bối cảnh HDFS; object store, memory, query selectivity và engine concurrency cần benchmark riêng. Quyết định phải dựa vào workload, không sao chép default.

## 5. Page, encoding và codec

Writer chọn encoding theo page/column behavior; dictionary có thể fallback, RLE/delta/plain phục vụ shapes khác nhau. Sau encoding, codec nén page hoặc chunk theo format/version. Page size cân bằng header overhead, decoding granularity và point/range read. Page không nhất thiết là network I/O request: engine có thể đọc range lớn chứa nhiều pages. Footer chỉ mô tả selected metadata; xác nhận encoding bằng metadata tool, xác nhận decode/I/O bằng profiler hoặc engine counters.

## 6. Lab ba cấu hình

Ghi cùng canonical dataset với ba target row-group sizes bằng một writer/version đã pin. Đọc footer, ghi file size, group count, rows/group, column compressed/uncompressed sizes, encodings, statistics và page-index presence. Chạy full scan, projection-only, selective filter và combined query ở cold/warm states được định nghĩa. Đối soát typed result hash trước performance. Chọn cấu hình bằng bytes transferred, pruned groups/pages, peak memory và latency distribution; nếu metric page pruning không quan sát được thì ghi unknown, không suy từ latency.

## 7. Ma trận kiểm chứng từng mệnh đề

Mỗi claim phải chỉ rõ metadata scope, writer/reader version, exact fixture, counterexample và oracle. File parse được, plan có predicate hoặc metadata tồn tại chưa đủ để kết luận physical I/O hay semantic result đúng.

### 7.1. Parquet hierarchy probe 1: scope, metadata, counterexample và observed I/O phải khớp

**Mệnh đề cần kiểm.** Parquet hierarchy probe 1: scope, metadata, counterexample và observed I/O phải khớp.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.2. Parquet hierarchy probe 2: scope, metadata, counterexample và observed I/O phải khớp

**Mệnh đề cần kiểm.** Parquet hierarchy probe 2: scope, metadata, counterexample và observed I/O phải khớp.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.3. Parquet hierarchy probe 3: scope, metadata, counterexample và observed I/O phải khớp

**Mệnh đề cần kiểm.** Parquet hierarchy probe 3: scope, metadata, counterexample và observed I/O phải khớp.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.4. Parquet hierarchy probe 4: scope, metadata, counterexample và observed I/O phải khớp

**Mệnh đề cần kiểm.** Parquet hierarchy probe 4: scope, metadata, counterexample và observed I/O phải khớp.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.5. Parquet hierarchy probe 5: scope, metadata, counterexample và observed I/O phải khớp

**Mệnh đề cần kiểm.** Parquet hierarchy probe 5: scope, metadata, counterexample và observed I/O phải khớp.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.6. Parquet hierarchy probe 6: scope, metadata, counterexample và observed I/O phải khớp

**Mệnh đề cần kiểm.** Parquet hierarchy probe 6: scope, metadata, counterexample và observed I/O phải khớp.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.7. Parquet hierarchy probe 7: scope, metadata, counterexample và observed I/O phải khớp

**Mệnh đề cần kiểm.** Parquet hierarchy probe 7: scope, metadata, counterexample và observed I/O phải khớp.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.8. Parquet hierarchy probe 8: scope, metadata, counterexample và observed I/O phải khớp

**Mệnh đề cần kiểm.** Parquet hierarchy probe 8: scope, metadata, counterexample và observed I/O phải khớp.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.9. Parquet hierarchy probe 9: scope, metadata, counterexample và observed I/O phải khớp

**Mệnh đề cần kiểm.** Parquet hierarchy probe 9: scope, metadata, counterexample và observed I/O phải khớp.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.10. Parquet hierarchy probe 10: scope, metadata, counterexample và observed I/O phải khớp

**Mệnh đề cần kiểm.** Parquet hierarchy probe 10: scope, metadata, counterexample và observed I/O phải khớp.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.11. Parquet hierarchy probe 11: scope, metadata, counterexample và observed I/O phải khớp

**Mệnh đề cần kiểm.** Parquet hierarchy probe 11: scope, metadata, counterexample và observed I/O phải khớp.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.12. Parquet hierarchy probe 12: scope, metadata, counterexample và observed I/O phải khớp

**Mệnh đề cần kiểm.** Parquet hierarchy probe 12: scope, metadata, counterexample và observed I/O phải khớp.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.13. Parquet hierarchy probe 13: scope, metadata, counterexample và observed I/O phải khớp

**Mệnh đề cần kiểm.** Parquet hierarchy probe 13: scope, metadata, counterexample và observed I/O phải khớp.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.14. Parquet hierarchy probe 14: scope, metadata, counterexample và observed I/O phải khớp

**Mệnh đề cần kiểm.** Parquet hierarchy probe 14: scope, metadata, counterexample và observed I/O phải khớp.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.

### 7.15. Parquet hierarchy probe 15: scope, metadata, counterexample và observed I/O phải khớp

**Mệnh đề cần kiểm.** Parquet hierarchy probe 15: scope, metadata, counterexample và observed I/O phải khớp.

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
2. [[SRC-APACHE-PARQUET-ENCODINGS]]
3. [[SRC-DUCKDB-PARQUET-PUSHDOWN]]
4. [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-APACHE-PARQUET-FILE-FORMAT]] | Format/table contract, implementation boundary hoặc workload context | Đã đọc locator; không suy ngoài phạm vi |
| [[SRC-APACHE-PARQUET-ENCODINGS]] | Format/table contract, implementation boundary hoặc workload context | Đã đọc locator; không suy ngoài phạm vi |
| [[SRC-DUCKDB-PARQUET-PUSHDOWN]] | Format/table contract, implementation boundary hoặc workload context | Đã đọc locator; không suy ngoài phạm vi |
| [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]] | Format/table contract, implementation boundary hoặc workload context | Đã đọc locator; không suy ngoài phạm vi |

## Key takeaways
- Mọi claim phải đúng tầng và đúng granularity.
- Metadata hiện diện, planner intent, executed pruning và physical I/O là bốn bằng chứng khác nhau.
- Semantic oracle được kiểm trước performance attribution.
- Chưa chạy lab thì note cung cấp giáo trình và protocol, chưa phải certification cho production.

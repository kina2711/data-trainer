# Phase 6: Analytical Storage and Query Engines
# Module 14: OLAP Internals and Analytical Engines
# Lesson 204: Row and Column Layout - Isolating Physical Layout

## Mục tiêu bài học

**Năng lực cần chứng minh.** Đo riêng phần đóng góp của bố cục cột trên cùng dữ liệu, tách khỏi nén và cắt tỉa.

**Điều kiện hoàn thành.** Quan hệ số cột chọn với byte đọc tuyến tính ở bố cục cột và phẳng ở bố cục hàng, và có số đo chi phí cập nhật một dòng.

> [!abstract] Câu hỏi trung tâm
> Thiết kế phép đo nào cô lập phần đóng góp của row/column layout khỏi compression, pruning, cache, metadata và khác biệt engine?

## 1. Logical table và physical layout

Row layout đặt fields của một tuple gần nhau trong page/record, thuận lợi khi lấy hoặc sửa phần lớn fields của ít rows. Column layout đặt values cùng column thành contiguous column chunks/segments trong row groups, thuận lợi cho projection hẹp trên nhiều rows. Triển khai hiện đại không nhất thiết tạo một OS file cho mỗi column; Parquet có row groups, column chunks và pages trong file. Row identity được giữ qua position/definition levels và metadata. Vì vậy mô hình 'mỗi cột một tệp' chỉ là hình minh họa.

## 2. Projection saving không bằng tỷ lệ cột

Bytes cần đọc phụ thuộc physical width, variable-length offsets, null/definition metadata, dictionary, page/header/footer, row-group boundaries, prefetch và filesystem/object-store ranges. Chọn 3/100 columns không đảm bảo đọc 3% file. Nếu ba columns chiếm 40% encoded bytes, lower bound đã khác. Engine có thể đọc metadata cho mọi query và fetch page lớn hơn requested slice. Phép đo phải có expected bytes từ metadata và observed bytes theo một định nghĩa rõ, rồi giải thích residual.

## 3. Cô lập biến layout

Dùng cùng logical generator, row count, data values, column types/order và query semantics. Tắt compression hoặc dùng uncompressed format ở cả hai; tắt/neutralize filter pruning bằng full-row predicate hoặc không predicate; không dùng index/materialized view. Chạy cold-cache và warm-cache rounds riêng, cố định threads/memory và randomized query order. So within one engine/reader nếu có thể; nếu dùng hai engines, kết luận là whole-stack result chứ không riêng layout. Lưu file sizes, explain plan, projected columns và scan bytes.

## 4. Bốn projection widths

Query 1, 3, 10 và 100 columns trên bảng 100 columns nhưng chọn columns có encoded width đã biết. Tạo hai series: contiguous narrow columns và mixed-width columns để chứng minh column count không đủ. Row layout kỳ vọng read bytes gần phẳng khi scan tất cả rows vì records chứa fields đi kèm, nhưng buffer/page behavior vẫn gây lệch. Column layout kỳ vọng tăng theo tổng physical bytes của selected column chunks cộng fixed overhead; không ép tuyến tính tuyệt đối theo số cột.

## 5. Update cost cần mô hình đúng

Khẳng định 'update một row phải chạm mọi tệp cột' quá rộng. Engine có thể dùng delta store, delete bitmap, MVCC update segments, append-new-version hoặc rewrite column pages/row groups; update một field không nhất thiết rewrite mọi column file ngay. Chi phí có thể xuất hiện trễ ở merge/compaction và read amplification. Lab phải đo foreground latency, bytes written/WAL, storage delta và background merge over a defined window. So final correctness và space reclamation, không chỉ statement latency.

## 6. Lợi ích ngoài I/O

Values cùng type/pattern cải thiện encoding; compact columns đưa nhiều values vào cache và hỗ trợ vectorized loops/SIMD. Nhưng projection pushdown, compression và vectorization là mechanisms tách biệt dù thường đi cùng column stores. Bài này giữ compression off để đo layout; vectorized execution có thể còn khác giữa readers và phải ghi như confounder. Reconstruct full rows từ nhiều columns có gather/materialization cost; `SELECT *` hoặc point fetch có thể làm row layout cạnh tranh tốt hơn.

## 7. Đọc kết quả và giữ giới hạn

Bảng kết quả có logical rows, projected logical bytes, file bytes, storage bytes fetched, engine scan bytes, elapsed CPU/wall time, cache state và repetitions. Median cùng dispersion thay một run. Nếu bytes không như dự đoán, kiểm projection pushdown trong plan, page/range granularity, cache và instrumentation trước khi kết luận. Done khi người học quy phần tiết kiệm cho layout với residual được giải thích, đồng thời tách rõ compression/pruning. Không kết luận mọi column store nhanh hơn mọi row store.

## 8. Ma trận kiểm chứng từng mệnh đề

Mỗi kết luận cần input, observation và failure signal có thể lưu. Tên sản phẩm, file nhỏ, query nhanh hoặc presentation thuyết phục không tự chứng minh cơ chế hay năng lực.

### 8.1. column layout thường dùng row groups column chunks và pages

**Mệnh đề cần kiểm.** column layout thường dùng row groups column chunks và pages.

**Cách kiểm.** Giữ logical data/query cố định; tắt compression/pruning, tách cold/warm cache, inspect projected columns và đo logical/file/storage/engine bytes. Với update, theo dõi cả foreground lẫn merge window. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.2. ba trên một trăm cột không đồng nghĩa ba phần trăm bytes

**Mệnh đề cần kiểm.** ba trên một trăm cột không đồng nghĩa ba phần trăm bytes.

**Cách kiểm.** Giữ logical data/query cố định; tắt compression/pruning, tách cold/warm cache, inspect projected columns và đo logical/file/storage/engine bytes. Với update, theo dõi cả foreground lẫn merge window. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.3. physical width và metadata thuộc byte model

**Mệnh đề cần kiểm.** physical width và metadata thuộc byte model.

**Cách kiểm.** Giữ logical data/query cố định; tắt compression/pruning, tách cold/warm cache, inspect projected columns và đo logical/file/storage/engine bytes. Với update, theo dõi cả foreground lẫn merge window. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.4. projection pushdown khác filter pruning

**Mệnh đề cần kiểm.** projection pushdown khác filter pruning.

**Cách kiểm.** Giữ logical data/query cố định; tắt compression/pruning, tách cold/warm cache, inspect projected columns và đo logical/file/storage/engine bytes. Với update, theo dõi cả foreground lẫn merge window. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.5. compression phải tắt khi cô lập layout

**Mệnh đề cần kiểm.** compression phải tắt khi cô lập layout.

**Cách kiểm.** Giữ logical data/query cố định; tắt compression/pruning, tách cold/warm cache, inspect projected columns và đo logical/file/storage/engine bytes. Với update, theo dõi cả foreground lẫn merge window. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.6. cold cache và warm cache là hai experiments

**Mệnh đề cần kiểm.** cold cache và warm cache là hai experiments.

**Cách kiểm.** Giữ logical data/query cố định; tắt compression/pruning, tách cold/warm cache, inspect projected columns và đo logical/file/storage/engine bytes. Với update, theo dõi cả foreground lẫn merge window. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.7. khác engine làm kết quả thành whole stack comparison

**Mệnh đề cần kiểm.** khác engine làm kết quả thành whole stack comparison.

**Cách kiểm.** Giữ logical data/query cố định; tắt compression/pruning, tách cold/warm cache, inspect projected columns và đo logical/file/storage/engine bytes. Với update, theo dõi cả foreground lẫn merge window. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.8. query order cần randomized để giảm warmup bias

**Mệnh đề cần kiểm.** query order cần randomized để giảm warmup bias.

**Cách kiểm.** Giữ logical data/query cố định; tắt compression/pruning, tách cold/warm cache, inspect projected columns và đo logical/file/storage/engine bytes. Với update, theo dõi cả foreground lẫn merge window. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.9. mixed-width columns phá giả định tuyến tính theo count

**Mệnh đề cần kiểm.** mixed-width columns phá giả định tuyến tính theo count.

**Cách kiểm.** Giữ logical data/query cố định; tắt compression/pruning, tách cold/warm cache, inspect projected columns và đo logical/file/storage/engine bytes. Với update, theo dõi cả foreground lẫn merge window. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.10. row-layout scan bytes chỉ kỳ vọng gần phẳng trong setup

**Mệnh đề cần kiểm.** row-layout scan bytes chỉ kỳ vọng gần phẳng trong setup.

**Cách kiểm.** Giữ logical data/query cố định; tắt compression/pruning, tách cold/warm cache, inspect projected columns và đo logical/file/storage/engine bytes. Với update, theo dõi cả foreground lẫn merge window. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.11. column-layout bytes tăng theo selected chunks cộng overhead

**Mệnh đề cần kiểm.** column-layout bytes tăng theo selected chunks cộng overhead.

**Cách kiểm.** Giữ logical data/query cố định; tắt compression/pruning, tách cold/warm cache, inspect projected columns và đo logical/file/storage/engine bytes. Với update, theo dõi cả foreground lẫn merge window. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.12. update một row không mặc nhiên rewrite mọi column file

**Mệnh đề cần kiểm.** update một row không mặc nhiên rewrite mọi column file.

**Cách kiểm.** Giữ logical data/query cố định; tắt compression/pruning, tách cold/warm cache, inspect projected columns và đo logical/file/storage/engine bytes. Với update, theo dõi cả foreground lẫn merge window. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.13. delta store chuyển chi phí sang merge hoặc read path

**Mệnh đề cần kiểm.** delta store chuyển chi phí sang merge hoặc read path.

**Cách kiểm.** Giữ logical data/query cố định; tắt compression/pruning, tách cold/warm cache, inspect projected columns và đo logical/file/storage/engine bytes. Với update, theo dõi cả foreground lẫn merge window. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.14. vectorization là confounder riêng với layout

**Mệnh đề cần kiểm.** vectorization là confounder riêng với layout.

**Cách kiểm.** Giữ logical data/query cố định; tắt compression/pruning, tách cold/warm cache, inspect projected columns và đo logical/file/storage/engine bytes. Với update, theo dõi cả foreground lẫn merge window. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.15. full-row reconstruction có gather materialization cost

**Mệnh đề cần kiểm.** full-row reconstruction có gather materialization cost.

**Cách kiểm.** Giữ logical data/query cố định; tắt compression/pruning, tách cold/warm cache, inspect projected columns và đo logical/file/storage/engine bytes. Với update, theo dõi cả foreground lẫn merge window. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

## 9. Quy trình phản biện

1. Chốt decision hoặc workload, grain, version và constraints trước khi chọn implementation.
2. Tách logical semantics, physical mechanism, observed metric và business conclusion.
3. Khóa controlled variables; ghi rõ confounders còn lại và instrumentation boundary.
4. Kiểm correctness trước performance, đồng thời giữ negative và changed-constraint cases.
5. Phân loại source fact, curriculum synthesis, engine-specific behavior và untested hypothesis.
6. Dùng raw artifacts và independent oracle khi kết quả do chính implementation sinh ra.
7. Chưa có execution evidence thì giữ trạng thái `review`.

## 10. Câu hỏi tự kiểm tra

1. Invariant, decision hoặc workload characteristic trung tâm là gì?
2. Biến nào được giữ cố định và biến nào được thay đổi?
3. Counter nào đo đúng mechanism thay vì chỉ đo wall-clock?
4. Một kết quả xanh nhưng sai semantics có thể xuất hiện bằng cách nào?
5. Điều kiện nào làm lựa chọn hiện tại phải đảo?
6. Kết luận nào mới là protocol, chưa phải evidence quan sát được?

## 11. Giới hạn và điều chưa cho phép kết luận

- Chưa chạy capstone với người dùng thật, Gate 5 với hội đồng, benchmark engines hoặc compression matrix; note mô tả protocol và expected evidence.
- Tài liệu web được kiểm ngày 2026-10-01; format, encoding support, storage version và engine behavior có thể đổi.
- Rubric, tám hạng mục capstone và ma trận kiểm chứng là curriculum synthesis; không gán nguyên văn cho một nguồn.
- Kết quả microbenchmark chỉ áp cho dataset, version, configuration, cache và workload đã ghi; không chứng minh ưu thế phổ quát.
- Note giữ trạng thái `review` cho tới khi chủ dự án duyệt semantic meaning.

## Reference
1. [[SRC-KLEPPMANN-DDIA-1E]]
2. [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]]
3. [[SRC-CSTORE-COLUMN-ORIENTED-DBMS]]
4. [[SRC-DUCKDB-PARQUET-PUSHDOWN]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-KLEPPMANN-DDIA-1E]] | Khái niệm, mechanism hoặc evidence boundary liên quan | Đã đọc locator được ghi trong source record; không suy ngoài phạm vi |
| [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] | Khái niệm, mechanism hoặc evidence boundary liên quan | Đã đọc locator được ghi trong source record; không suy ngoài phạm vi |
| [[SRC-CSTORE-COLUMN-ORIENTED-DBMS]] | Khái niệm, mechanism hoặc evidence boundary liên quan | Đã đọc locator được ghi trong source record; không suy ngoài phạm vi |
| [[SRC-DUCKDB-PARQUET-PUSHDOWN]] | Khái niệm, mechanism hoặc evidence boundary liên quan | Đã đọc locator được ghi trong source record; không suy ngoài phạm vi |

## Key takeaways
- Layout chỉ được quy công khi compression, pruning, cache và engine differences đã được kiểm soát hoặc ghi thành confounders.
- Correctness, scope và exact version đi trước performance hoặc approval.
- Một proxy dễ lấy không được dùng thay consumer outcome, physical counter hoặc independent reconciliation.
- Counterexample và changed constraint phải làm kết luận đảo khi assumptions không còn đúng.
- Chưa chạy lab thì artifact là giáo trình đã kiểm cấu trúc, không phải chứng nhận production hay benchmark result.

# Phase 5: Modeling, Semantics and Analytical Product
# Module 12: Semantic Layer and Metrics Engineering
# Lesson 166: From a Business Question to a Metric Contract

## Mục tiêu bài học

**Năng lực cần chứng minh.** Viết hợp đồng sáu phần cho một chỉ số và chứng minh hai người đọc độc lập cho ra cùng một con số.

**Điều kiện hoàn thành.** Ba cặp con số từ hai người cài độc lập đều khớp tuyệt đối, và tám cách hiểu của câu đầu được liệt kê đủ.

> [!abstract] Câu hỏi trung tâm
> Một câu hỏi nghiệp vụ phải được chốt thành sáu quyết định nào để hai người cài độc lập tạo cùng tập bản ghi và cùng con số?

## 1. Vì sao tên chỉ số chưa phải định nghĩa

Câu “doanh thu tháng trước” còn thiếu đối tượng được tính, loại doanh thu, mốc thời gian, ranh giới kỳ, loại trừ, currency và cách gộp. Hai query đều đúng SQL có thể cho số khác mà không query nào tự báo lỗi. Metric contract biến tranh luận về con số thành sáu quyết định có owner và phép kiểm. Contract không phải đoạn mô tả marketing; nó phải đủ chính xác để người khác dựng executable logic mà không hỏi tác giả.

## 2. Phần một: population

Population mô tả universe bản ghi đủ điều kiện trước khi tính: loại giao dịch, trạng thái, product/channel/region, entity identity, nguồn được phép và coverage period. Ghi cả inclusion lẫn exclusion. Cancelled order, test account, internal transfer, fraudulent transaction, tax, refund và chargeback phải có disposition. Population là intrinsic semantics; filter do người dùng chọn như region=`North` là query parameter, không được lẫn vào định nghĩa trừ khi metric thực sự chỉ dành cho North.

## 3. Phần hai và ba: grain, time

Grain nêu một observation ở mức nào trước aggregate: order, order line, invoice line, payment hay recognized-revenue event. Metric grain nêu kết quả theo entity/time grain nào và khả năng slice hợp lệ. Time contract chỉ rõ timestamp role dùng để quy kỳ, timezone, calendar/fiscal period, cutoff và late-data/restatement. `created_at`, `paid_at`, `shipped_at` và `recognized_at` trả lời bốn câu khác nhau; chọn mốc phải theo business event chứ không theo cột tiện nhất.

## 4. Phần bốn và năm: filters, aggregation

Intrinsic filter là điều kiện luôn thuộc definition, như exclude test orders; user filter là dimension người hỏi có thể thay đổi mà không đổi identity của metric. Aggregation contract ghi base expression, operator, grouping, additivity, unit, null/zero policy và numerator/denominator nếu là ratio. Với gross margin, phải sum gross profit và revenue ở target grain rồi divide; average của row-level percentages hoặc sum ratios không bảo toàn nghĩa.

## 5. Phần sáu: ownership và change

Owner có quyền nghiệp vụ phê duyệt meaning, không nhất thiết là người viết SQL. Contract cần metric ID, version, effective date, steward/technical owner, approver, change reason, compatibility và consumers. Thay filter/refund/time role có thể là breaking semantic change dù tên cột không đổi. Version mới cần parallel run, semantic diff, communication và deprecation; không overwrite definition cũ rồi sửa lịch sử dashboard âm thầm.

## 6. Tám cách hiểu của một câu hỏi

Để tạo tám cách hiểu có kiểm soát, chọn ba quyết định nhị phân thật sự độc lập: gross hay net; order date hay recognized date; booked hay completed population. Tổ hợp tạo tám contracts, mỗi contract có tên riêng và query riêng. Đây là bài tập phơi bày ambiguity, không phải khẳng định mọi câu hỏi luôn có đúng tám nghĩa. Nếu các trục phụ thuộc nhau hoặc có nhiều hơn hai lựa chọn, số cách hiểu thay đổi.

## 7. Phép thử hai implementation

Khóa cùng source snapshot, cutoff và contract version; hai người không trao đổi query. So compiled SQL/logic, eligible-row set, numerator, denominator, time buckets và final values. Chỉ so con số cuối có thể che hai lỗi triệt tiêu nhau. Nếu khác, phân loại defect: contract mơ hồ, dữ liệu/engine khác, implementation sai hoặc rounding. Sửa contract trước retest; không hướng dẫn miệng vì knowledge ngoài contract làm phép thử mất ý nghĩa.

## 8. Ma trận kiểm chứng từng mệnh đề

Các mệnh đề dưới đây phải được kiểm bằng fixture, invariant và output có thể chạy lại. Việc công cụ compile được YAML hoặc sinh SQL không tự chứng minh metric đúng nghĩa.

### 8.1. population phải ghi inclusion và exclusion

**Mệnh đề cần kiểm.** population phải ghi inclusion và exclusion.

**Cách kiểm.** Khóa một snapshot và cutoff; hai người độc lập triển khai contract. So eligible-row IDs, buckets, numerator/denominator và result. Tạo tám contracts bằng ba trục nhị phân đã ghi, không chỉ liệt kê tám câu chữ. Với mệnh đề này, ghi rõ dữ liệu phản ví dụ, expected result và failure signal. Tách validation cấu trúc khỏi xác nhận meaning của owner.

**Bằng chứng đạt.** Lưu contract/graph, snapshot, query hoặc compiled SQL, output thô, semantic diff và assumptions. Chỉ đánh dấu đạt khi cùng artifact cho kết quả lặp lại ở cùng version/cutoff; nếu chưa chạy, đây là test protocol chứ chưa phải kết quả production.

### 8.2. grain phải mô tả observation trước aggregate

**Mệnh đề cần kiểm.** grain phải mô tả observation trước aggregate.

**Cách kiểm.** Khóa một snapshot và cutoff; hai người độc lập triển khai contract. So eligible-row IDs, buckets, numerator/denominator và result. Tạo tám contracts bằng ba trục nhị phân đã ghi, không chỉ liệt kê tám câu chữ. Với mệnh đề này, ghi rõ dữ liệu phản ví dụ, expected result và failure signal. Tách validation cấu trúc khỏi xác nhận meaning của owner.

**Bằng chứng đạt.** Lưu contract/graph, snapshot, query hoặc compiled SQL, output thô, semantic diff và assumptions. Chỉ đánh dấu đạt khi cùng artifact cho kết quả lặp lại ở cùng version/cutoff; nếu chưa chạy, đây là test protocol chứ chưa phải kết quả production.

### 8.3. metric output grain khác source row grain

**Mệnh đề cần kiểm.** metric output grain khác source row grain.

**Cách kiểm.** Khóa một snapshot và cutoff; hai người độc lập triển khai contract. So eligible-row IDs, buckets, numerator/denominator và result. Tạo tám contracts bằng ba trục nhị phân đã ghi, không chỉ liệt kê tám câu chữ. Với mệnh đề này, ghi rõ dữ liệu phản ví dụ, expected result và failure signal. Tách validation cấu trúc khỏi xác nhận meaning của owner.

**Bằng chứng đạt.** Lưu contract/graph, snapshot, query hoặc compiled SQL, output thô, semantic diff và assumptions. Chỉ đánh dấu đạt khi cùng artifact cho kết quả lặp lại ở cùng version/cutoff; nếu chưa chạy, đây là test protocol chứ chưa phải kết quả production.

### 8.4. time role phải gắn business event

**Mệnh đề cần kiểm.** time role phải gắn business event.

**Cách kiểm.** Khóa một snapshot và cutoff; hai người độc lập triển khai contract. So eligible-row IDs, buckets, numerator/denominator và result. Tạo tám contracts bằng ba trục nhị phân đã ghi, không chỉ liệt kê tám câu chữ. Với mệnh đề này, ghi rõ dữ liệu phản ví dụ, expected result và failure signal. Tách validation cấu trúc khỏi xác nhận meaning của owner.

**Bằng chứng đạt.** Lưu contract/graph, snapshot, query hoặc compiled SQL, output thô, semantic diff và assumptions. Chỉ đánh dấu đạt khi cùng artifact cho kết quả lặp lại ở cùng version/cutoff; nếu chưa chạy, đây là test protocol chứ chưa phải kết quả production.

### 8.5. timezone và fiscal calendar thuộc contract

**Mệnh đề cần kiểm.** timezone và fiscal calendar thuộc contract.

**Cách kiểm.** Khóa một snapshot và cutoff; hai người độc lập triển khai contract. So eligible-row IDs, buckets, numerator/denominator và result. Tạo tám contracts bằng ba trục nhị phân đã ghi, không chỉ liệt kê tám câu chữ. Với mệnh đề này, ghi rõ dữ liệu phản ví dụ, expected result và failure signal. Tách validation cấu trúc khỏi xác nhận meaning của owner.

**Bằng chứng đạt.** Lưu contract/graph, snapshot, query hoặc compiled SQL, output thô, semantic diff và assumptions. Chỉ đánh dấu đạt khi cùng artifact cho kết quả lặp lại ở cùng version/cutoff; nếu chưa chạy, đây là test protocol chứ chưa phải kết quả production.

### 8.6. intrinsic filter khác user-selected filter

**Mệnh đề cần kiểm.** intrinsic filter khác user-selected filter.

**Cách kiểm.** Khóa một snapshot và cutoff; hai người độc lập triển khai contract. So eligible-row IDs, buckets, numerator/denominator và result. Tạo tám contracts bằng ba trục nhị phân đã ghi, không chỉ liệt kê tám câu chữ. Với mệnh đề này, ghi rõ dữ liệu phản ví dụ, expected result và failure signal. Tách validation cấu trúc khỏi xác nhận meaning của owner.

**Bằng chứng đạt.** Lưu contract/graph, snapshot, query hoặc compiled SQL, output thô, semantic diff và assumptions. Chỉ đánh dấu đạt khi cùng artifact cho kết quả lặp lại ở cùng version/cutoff; nếu chưa chạy, đây là test protocol chứ chưa phải kết quả production.

### 8.7. aggregation phải ghi operator theo dimension

**Mệnh đề cần kiểm.** aggregation phải ghi operator theo dimension.

**Cách kiểm.** Khóa một snapshot và cutoff; hai người độc lập triển khai contract. So eligible-row IDs, buckets, numerator/denominator và result. Tạo tám contracts bằng ba trục nhị phân đã ghi, không chỉ liệt kê tám câu chữ. Với mệnh đề này, ghi rõ dữ liệu phản ví dụ, expected result và failure signal. Tách validation cấu trúc khỏi xác nhận meaning của owner.

**Bằng chứng đạt.** Lưu contract/graph, snapshot, query hoặc compiled SQL, output thô, semantic diff và assumptions. Chỉ đánh dấu đạt khi cùng artifact cho kết quả lặp lại ở cùng version/cutoff; nếu chưa chạy, đây là test protocol chứ chưa phải kết quả production.

### 8.8. ratio cần numerator và denominator

**Mệnh đề cần kiểm.** ratio cần numerator và denominator.

**Cách kiểm.** Khóa một snapshot và cutoff; hai người độc lập triển khai contract. So eligible-row IDs, buckets, numerator/denominator và result. Tạo tám contracts bằng ba trục nhị phân đã ghi, không chỉ liệt kê tám câu chữ. Với mệnh đề này, ghi rõ dữ liệu phản ví dụ, expected result và failure signal. Tách validation cấu trúc khỏi xác nhận meaning của owner.

**Bằng chứng đạt.** Lưu contract/graph, snapshot, query hoặc compiled SQL, output thô, semantic diff và assumptions. Chỉ đánh dấu đạt khi cùng artifact cho kết quả lặp lại ở cùng version/cutoff; nếu chưa chạy, đây là test protocol chứ chưa phải kết quả production.

### 8.9. null và divide-by-zero policy phải rõ

**Mệnh đề cần kiểm.** null và divide-by-zero policy phải rõ.

**Cách kiểm.** Khóa một snapshot và cutoff; hai người độc lập triển khai contract. So eligible-row IDs, buckets, numerator/denominator và result. Tạo tám contracts bằng ba trục nhị phân đã ghi, không chỉ liệt kê tám câu chữ. Với mệnh đề này, ghi rõ dữ liệu phản ví dụ, expected result và failure signal. Tách validation cấu trúc khỏi xác nhận meaning của owner.

**Bằng chứng đạt.** Lưu contract/graph, snapshot, query hoặc compiled SQL, output thô, semantic diff và assumptions. Chỉ đánh dấu đạt khi cùng artifact cho kết quả lặp lại ở cùng version/cutoff; nếu chưa chạy, đây là test protocol chứ chưa phải kết quả production.

### 8.10. currency và unit phải được quản trị

**Mệnh đề cần kiểm.** currency và unit phải được quản trị.

**Cách kiểm.** Khóa một snapshot và cutoff; hai người độc lập triển khai contract. So eligible-row IDs, buckets, numerator/denominator và result. Tạo tám contracts bằng ba trục nhị phân đã ghi, không chỉ liệt kê tám câu chữ. Với mệnh đề này, ghi rõ dữ liệu phản ví dụ, expected result và failure signal. Tách validation cấu trúc khỏi xác nhận meaning của owner.

**Bằng chứng đạt.** Lưu contract/graph, snapshot, query hoặc compiled SQL, output thô, semantic diff và assumptions. Chỉ đánh dấu đạt khi cùng artifact cho kết quả lặp lại ở cùng version/cutoff; nếu chưa chạy, đây là test protocol chứ chưa phải kết quả production.

### 8.11. owner phê duyệt meaning không chỉ SQL

**Mệnh đề cần kiểm.** owner phê duyệt meaning không chỉ SQL.

**Cách kiểm.** Khóa một snapshot và cutoff; hai người độc lập triển khai contract. So eligible-row IDs, buckets, numerator/denominator và result. Tạo tám contracts bằng ba trục nhị phân đã ghi, không chỉ liệt kê tám câu chữ. Với mệnh đề này, ghi rõ dữ liệu phản ví dụ, expected result và failure signal. Tách validation cấu trúc khỏi xác nhận meaning của owner.

**Bằng chứng đạt.** Lưu contract/graph, snapshot, query hoặc compiled SQL, output thô, semantic diff và assumptions. Chỉ đánh dấu đạt khi cùng artifact cho kết quả lặp lại ở cùng version/cutoff; nếu chưa chạy, đây là test protocol chứ chưa phải kết quả production.

### 8.12. semantic change cần version và effective date

**Mệnh đề cần kiểm.** semantic change cần version và effective date.

**Cách kiểm.** Khóa một snapshot và cutoff; hai người độc lập triển khai contract. So eligible-row IDs, buckets, numerator/denominator và result. Tạo tám contracts bằng ba trục nhị phân đã ghi, không chỉ liệt kê tám câu chữ. Với mệnh đề này, ghi rõ dữ liệu phản ví dụ, expected result và failure signal. Tách validation cấu trúc khỏi xác nhận meaning của owner.

**Bằng chứng đạt.** Lưu contract/graph, snapshot, query hoặc compiled SQL, output thô, semantic diff và assumptions. Chỉ đánh dấu đạt khi cùng artifact cho kết quả lặp lại ở cùng version/cutoff; nếu chưa chạy, đây là test protocol chứ chưa phải kết quả production.

### 8.13. hai implementation dùng cùng snapshot/cutoff

**Mệnh đề cần kiểm.** hai implementation dùng cùng snapshot/cutoff.

**Cách kiểm.** Khóa một snapshot và cutoff; hai người độc lập triển khai contract. So eligible-row IDs, buckets, numerator/denominator và result. Tạo tám contracts bằng ba trục nhị phân đã ghi, không chỉ liệt kê tám câu chữ. Với mệnh đề này, ghi rõ dữ liệu phản ví dụ, expected result và failure signal. Tách validation cấu trúc khỏi xác nhận meaning của owner.

**Bằng chứng đạt.** Lưu contract/graph, snapshot, query hoặc compiled SQL, output thô, semantic diff và assumptions. Chỉ đánh dấu đạt khi cùng artifact cho kết quả lặp lại ở cùng version/cutoff; nếu chưa chạy, đây là test protocol chứ chưa phải kết quả production.

### 8.14. eligible-row diff quan trọng hơn chỉ final value

**Mệnh đề cần kiểm.** eligible-row diff quan trọng hơn chỉ final value.

**Cách kiểm.** Khóa một snapshot và cutoff; hai người độc lập triển khai contract. So eligible-row IDs, buckets, numerator/denominator và result. Tạo tám contracts bằng ba trục nhị phân đã ghi, không chỉ liệt kê tám câu chữ. Với mệnh đề này, ghi rõ dữ liệu phản ví dụ, expected result và failure signal. Tách validation cấu trúc khỏi xác nhận meaning của owner.

**Bằng chứng đạt.** Lưu contract/graph, snapshot, query hoặc compiled SQL, output thô, semantic diff và assumptions. Chỉ đánh dấu đạt khi cùng artifact cho kết quả lặp lại ở cùng version/cutoff; nếu chưa chạy, đây là test protocol chứ chưa phải kết quả production.

### 8.15. tám cách hiểu là tổ hợp của các trục đã công bố

**Mệnh đề cần kiểm.** tám cách hiểu là tổ hợp của các trục đã công bố.

**Cách kiểm.** Khóa một snapshot và cutoff; hai người độc lập triển khai contract. So eligible-row IDs, buckets, numerator/denominator và result. Tạo tám contracts bằng ba trục nhị phân đã ghi, không chỉ liệt kê tám câu chữ. Với mệnh đề này, ghi rõ dữ liệu phản ví dụ, expected result và failure signal. Tách validation cấu trúc khỏi xác nhận meaning của owner.

**Bằng chứng đạt.** Lưu contract/graph, snapshot, query hoặc compiled SQL, output thô, semantic diff và assumptions. Chỉ đánh dấu đạt khi cùng artifact cho kết quả lặp lại ở cùng version/cutoff; nếu chưa chạy, đây là test protocol chứ chưa phải kết quả production.

## 9. Quy trình phản biện

1. Viết business question, population, grain, identity, time và unit trước syntax.
2. Chỉ ra artifact canonical, owner, version và change process.
3. Tách source fact, product-version detail và curriculum synthesis.
4. Dựng normal case cùng phản ví dụ: denominator lệch, fanout, sparse period, timezone boundary hoặc non-additive rollup.
5. So eligible rows và intermediate components trước final value; hai lỗi có thể triệt tiêu ở số cuối.
6. Chạy negative tests song song với valid controls để phát hiện cả false negative và false positive.
7. Lưu failed run, limitations và conditions khiến kết luận phải đổi.

## 10. Câu hỏi tự kiểm tra

1. Metric đang trả lời câu hỏi nào, trên population và grain nào?
2. Entity/dimension nào reachable qua path nào, cardinality gì?
3. Aggregation nào hợp lệ theo từng dimension và time grain?
4. Ca biên nào cho kết quả hợp lệ cú pháp nhưng sai nghĩa?
5. Chi tiết nào là khái niệm ổn định, chi tiết nào phụ thuộc phiên bản sản phẩm?
6. Bằng chứng nào cho phép người khác bác bỏ implementation?

## 11. Giới hạn và điều chưa cho phép kết luận

- Chưa chạy lab hai người, semantic graph planner, ratio rollup, aggregation rejection hoặc calendar fixture; note mô tả protocol cần thực thi.
- dbt/MetricFlow là ví dụ sản phẩm được kiểm ngày 2026-10-01; syntax và availability có thể đổi theo version/tier.
- PostgreSQL documentation mô tả SQL mechanics, không tự cung cấp business semantics hay metric governance.
- Kimball–Ross hỗ trợ grain, additivity và calendar modeling; semantic-layer enforcement là phần tổng hợp có đối chiếu tài liệu hiện hành.
- Owner chưa phê duyệt meaning nên note giữ trạng thái `review`.

## Reference
1. [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]]
2. [[SRC-DBT-SEMANTIC-MODELS]]
3. [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]] | Khái niệm, cơ chế, product detail hoặc SQL behavior liên quan | Đã đọc phạm vi có locator; không suy ngoài phạm vi |
| [[SRC-DBT-SEMANTIC-MODELS]] | Khái niệm, cơ chế, product detail hoặc SQL behavior liên quan | Đã đọc phạm vi có locator; không suy ngoài phạm vi |
| [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]] | Khái niệm, cơ chế, product detail hoặc SQL behavior liên quan | Đã đọc phạm vi có locator; không suy ngoài phạm vi |

## Key takeaways
- Metric contract bắt đầu từ population, grain, time, filters, aggregation và ownership; tên metric không đủ.
- Semantic graph phải mã hóa identity, cardinality và path semantics để phát hiện fanout hoặc ambiguity.
- Ratio, cumulative, distinct và semi-additive metrics cần state/behavior riêng; không roll up như số cộng được.
- Time comparison đúng cần dense calendar, timezone, fiscal policy, partial-period và leap-day rules.
- Chưa chạy protocol thì note là tài liệu học thuật có truy nguồn, không phải chứng nhận production.

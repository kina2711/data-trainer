# Phase 5: Modeling, Semantics and Analytical Product
# Module 12: Semantic Layer and Metrics Engineering
# Lesson 165: The Layers That Must Be Distinguished

## Mục tiêu bài học

**Năng lực cần chứng minh.** Phân loại năm tầng cho một kiến trúc cho trước và chỉ ra định nghĩa chỉ số đang nằm ở đâu.

**Điều kiện hoàn thành.** Phân đúng năm tầng ở ≥ 2/3 kiến trúc, và đếm được số chỗ trùng định nghĩa ở kiến trúc có vấn đề.

> [!abstract] Câu hỏi trung tâm
> Bảng vật lý, mart, semantic model, metric contract và công cụ tiêu thụ khác nhau ở artifact, trách nhiệm và failure mode nào?

## 1. Tại sao phải tách năm tầng

Một dashboard hiển thị revenue không cho biết logic nằm trong SQL view, mart, BI calculated field hay semantic service. Khi cùng tên được định nghĩa ở nhiều nơi, sửa filter/refund/currency ở một chỗ không cập nhật các chỗ còn lại. Tách tầng không nhằm tăng số công cụ; nó tạo ranh giới để biết dữ liệu nằm đâu, structure được chuẩn bị ở đâu, nghĩa được khai báo ở đâu, metric được quản trị ở đâu và người dùng đặt câu hỏi ở đâu.

## 2. Tầng một: bảng vật lý

Physical table/file/view là nơi rows và columns tồn tại trên engine cụ thể. Nó có schema, types, keys, partition, clustering, retention, permissions và storage format. Một bảng có cột `revenue` không tự biến thành metric contract; cột có thể là atomic amount, allocated amount hay pre-aggregated number. Physical optimization có thể đổi mà business meaning không đổi, miễn lineage và contract được bảo toàn.

## 3. Tầng hai: mô hình mart

Mart tổ chức physical artifacts cho một domain/use case: facts, dimensions, wide product tables hoặc aggregate tables. Nó quyết định grain, joins, conformance, history và exposure boundary. Mart có dữ liệu, khác semantic model là metadata/declarations về cách consumer hiểu và kết nối model. Một mart tốt vẫn có thể bị dùng sai nếu metric filter, time grain và additivity không được quản trị.

## 4. Tầng ba và bốn: semantic model, metric contract

Semantic model khai báo entities, dimensions, measures, relationships, time dimensions và join behavior trên marts. Metric contract đặt tên cho phép tính: expression, source measure, entity/grain, filters, time window, aggregation, unit, null/late-data policy, owner và version. Tùy sản phẩm, metric có thể nằm trong cùng YAML/repository với semantic model, nhưng hai trách nhiệm vẫn phân biệt được. “Một nơi” nghĩa một governed source of truth có version và API/build path, không phải một file bất biến.

## 5. Tầng năm: công cụ tiêu thụ

BI, notebook, spreadsheet, reverse-ETL app hoặc API là nơi người dùng hỏi và trình bày. Tool có thể giữ layout, chart calculation chỉ dành cho hiển thị và parameters, nhưng shared business metric không nên được chép lại ở từng workbook/query. Ba triệu chứng phân tán là cùng tên cho nhiều số, sửa định nghĩa phải tìm nhiều assets, và không truy ra owner/version. Migration bắt đầu bằng inventory definitions, semantic diff, chọn canonical contract, redirect consumers rồi deprecate duplicates.

## 6. Ma trận kiểm chứng từng mệnh đề

Mỗi mệnh đề dưới đây cần một dữ liệu phản ví dụ, một invariant và một bằng chứng chạy lại được. Tên pattern, sơ đồ hoặc một query chạy thành công không đủ để xác nhận đúng ngữ nghĩa.

### 6.1. physical table có rows và engine-specific schema

**Mệnh đề cần kiểm.** physical table có rows và engine-specific schema.

**Cách kiểm.** Lấy ba kiến trúc, inventory mọi physical object, mart, semantic declaration, metric definition và consumer. Chọn một metric, đếm definitions, semantic-diff chúng và chứng minh canonical contract có owner/version cùng consumers được redirect. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.2. mart quyết định grain và prepared joins

**Mệnh đề cần kiểm.** mart quyết định grain và prepared joins.

**Cách kiểm.** Lấy ba kiến trúc, inventory mọi physical object, mart, semantic declaration, metric definition và consumer. Chọn một metric, đếm definitions, semantic-diff chúng và chứng minh canonical contract có owner/version cùng consumers được redirect. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.3. semantic model là declaration không phải bản sao dữ liệu

**Mệnh đề cần kiểm.** semantic model là declaration không phải bản sao dữ liệu.

**Cách kiểm.** Lấy ba kiến trúc, inventory mọi physical object, mart, semantic declaration, metric definition và consumer. Chọn một metric, đếm definitions, semantic-diff chúng và chứng minh canonical contract có owner/version cùng consumers được redirect. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.4. entity khác dimension và measure

**Mệnh đề cần kiểm.** entity khác dimension và measure.

**Cách kiểm.** Lấy ba kiến trúc, inventory mọi physical object, mart, semantic declaration, metric definition và consumer. Chọn một metric, đếm definitions, semantic-diff chúng và chứng minh canonical contract có owner/version cùng consumers được redirect. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.5. metric contract phải có formula và filters

**Mệnh đề cần kiểm.** metric contract phải có formula và filters.

**Cách kiểm.** Lấy ba kiến trúc, inventory mọi physical object, mart, semantic declaration, metric definition và consumer. Chọn một metric, đếm definitions, semantic-diff chúng và chứng minh canonical contract có owner/version cùng consumers được redirect. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.6. time grain và timezone thuộc metric semantics

**Mệnh đề cần kiểm.** time grain và timezone thuộc metric semantics.

**Cách kiểm.** Lấy ba kiến trúc, inventory mọi physical object, mart, semantic declaration, metric definition và consumer. Chọn một metric, đếm definitions, semantic-diff chúng và chứng minh canonical contract có owner/version cùng consumers được redirect. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.7. semantic model và metric có thể cùng repository nhưng khác trách nhiệm

**Mệnh đề cần kiểm.** semantic model và metric có thể cùng repository nhưng khác trách nhiệm.

**Cách kiểm.** Lấy ba kiến trúc, inventory mọi physical object, mart, semantic declaration, metric definition và consumer. Chọn một metric, đếm definitions, semantic-diff chúng và chứng minh canonical contract có owner/version cùng consumers được redirect. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.8. consumption tool không nên sở hữu shared metric

**Mệnh đề cần kiểm.** consumption tool không nên sở hữu shared metric.

**Cách kiểm.** Lấy ba kiến trúc, inventory mọi physical object, mart, semantic declaration, metric definition và consumer. Chọn một metric, đếm definitions, semantic-diff chúng và chứng minh canonical contract có owner/version cùng consumers được redirect. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.9. calculation chỉ cho visual phải được phân loại riêng

**Mệnh đề cần kiểm.** calculation chỉ cho visual phải được phân loại riêng.

**Cách kiểm.** Lấy ba kiến trúc, inventory mọi physical object, mart, semantic declaration, metric definition và consumer. Chọn một metric, đếm definitions, semantic-diff chúng và chứng minh canonical contract có owner/version cùng consumers được redirect. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.10. cùng metric name nhiều numbers là drift symptom

**Mệnh đề cần kiểm.** cùng metric name nhiều numbers là drift symptom.

**Cách kiểm.** Lấy ba kiến trúc, inventory mọi physical object, mart, semantic declaration, metric definition và consumer. Chọn một metric, đếm definitions, semantic-diff chúng và chứng minh canonical contract có owner/version cùng consumers được redirect. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.11. definition inventory phải tìm SQL BI và notebook

**Mệnh đề cần kiểm.** definition inventory phải tìm SQL BI và notebook.

**Cách kiểm.** Lấy ba kiến trúc, inventory mọi physical object, mart, semantic declaration, metric definition và consumer. Chọn một metric, đếm definitions, semantic-diff chúng và chứng minh canonical contract có owner/version cùng consumers được redirect. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.12. canonical source cần owner và version

**Mệnh đề cần kiểm.** canonical source cần owner và version.

**Cách kiểm.** Lấy ba kiến trúc, inventory mọi physical object, mart, semantic declaration, metric definition và consumer. Chọn một metric, đếm definitions, semantic-diff chúng và chứng minh canonical contract có owner/version cùng consumers được redirect. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.13. redirect consumers phải có equivalence test

**Mệnh đề cần kiểm.** redirect consumers phải có equivalence test.

**Cách kiểm.** Lấy ba kiến trúc, inventory mọi physical object, mart, semantic declaration, metric definition và consumer. Chọn một metric, đếm definitions, semantic-diff chúng và chứng minh canonical contract có owner/version cùng consumers được redirect. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.14. tool installation không tạo semantic governance

**Mệnh đề cần kiểm.** tool installation không tạo semantic governance.

**Cách kiểm.** Lấy ba kiến trúc, inventory mọi physical object, mart, semantic declaration, metric definition và consumer. Chọn một metric, đếm definitions, semantic-diff chúng và chứng minh canonical contract có owner/version cùng consumers được redirect. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.15. năm tầng là logical responsibilities không bắt buộc năm products

**Mệnh đề cần kiểm.** năm tầng là logical responsibilities không bắt buộc năm products.

**Cách kiểm.** Lấy ba kiến trúc, inventory mọi physical object, mart, semantic declaration, metric definition và consumer. Chọn một metric, đếm definitions, semantic-diff chúng và chứng minh canonical contract có owner/version cùng consumers được redirect. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

## 7. Quy trình làm bài và phản biện

1. Viết business question, phạm vi, vocabulary, grain, identity và time semantics trước khi chọn bảng hoặc công cụ.
2. Gắn từng định nghĩa với context, owner, version và canonical artifact; không dùng tên cột thay nghĩa.
3. Tách nội dung lấy trực tiếp từ nguồn, quyết định thiết kế và phần tổng hợp của giáo trình.
4. Dựng normal case cùng các ca biên có thể tạo kết quả hợp lệ cú pháp nhưng sai nghĩa.
5. Đo row count, distinct keys, unmatched/disposition counts, control totals và semantic diff trước–sau transform.
6. Thử replay, late correction hoặc schema/contract change phù hợp với bài; ghi change blast radius.
7. Giữ failed run, assumptions và limitation trong hồ sơ. Chúng cho người khác khả năng bác bỏ kết luận.

## 8. Câu hỏi tự kiểm tra

1. Artifact nào giữ dữ liệu, artifact nào giữ nghĩa và ai có quyền thay đổi?
2. Một row/term/metric đại diện điều gì trong context và khoảng thời gian nào?
3. Ca biên nào làm con số sai nhưng pipeline hoặc dashboard vẫn xanh?
4. Phép kiểm nào xác nhận cấu trúc; phần nào vẫn cần owner xác nhận?
5. Khi contract thay đổi, consumer nào bị ảnh hưởng và migration được kiểm ra sao?
6. Phần nào của note là source fact, phần nào là synthesis có điều kiện?

## 9. Giới hạn và điều chưa cho phép kết luận

- Chưa chạy các lab, handover test hoặc benchmark mô tả trong note; chúng là giao thức kiểm chứng, không phải số đo đã thu.
- Nguồn sách cung cấp khái niệm và patterns; lựa chọn cho một doanh nghiệp còn phụ thuộc domain, engine, workload, policy và owner.
- Tài liệu web được kiểm ngày 2026-10-01 và có thể thay đổi theo phiên bản sản phẩm.
- Không suy một tool, model hay kiến trúc là chuẩn duy nhất từ ví dụ của nguồn.
- Không có owner review thì trạng thái vẫn là `review`, chưa phải policy được phê duyệt.

## Reference
1. [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]]
2. [[SRC-DBT-SEMANTIC-MODELS]]
3. [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]] | Khái niệm, cơ chế và giới hạn liên quan trực tiếp | Đã đọc phạm vi có locator; không suy ngoài phạm vi |
| [[SRC-DBT-SEMANTIC-MODELS]] | Khái niệm, cơ chế và giới hạn liên quan trực tiếp | Đã đọc phạm vi có locator; không suy ngoài phạm vi |
| [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] | Khái niệm, cơ chế và giới hạn liên quan trực tiếp | Đã đọc phạm vi có locator; không suy ngoài phạm vi |

## Key takeaways
- Bắt đầu từ nghĩa, context, grain, identity, time và ownership; schema và công cụ là phần triển khai.
- Mọi trường hợp unmatched, unknown hoặc duplicated definition phải có trạng thái quan sát được, không được mất trong im lặng.
- Tài liệu chỉ đạt khi một người khác dùng đúng mà không dựa vào trí nhớ của tác giả.
- So sánh mô hình chỉ hợp lệ sau khi kết quả ngữ nghĩa đã được đối chiếu trên cùng dữ liệu và cutoff.
- Chưa chạy phép kiểm thì note là tài liệu học thuật có truy nguồn, không phải chứng nhận production.

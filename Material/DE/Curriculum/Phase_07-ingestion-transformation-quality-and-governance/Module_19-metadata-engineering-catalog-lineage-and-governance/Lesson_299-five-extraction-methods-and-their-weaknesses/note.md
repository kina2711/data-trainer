# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 19: Metadata Engineering, Catalog, Lineage and Governance
# Lesson 299: Five extraction methods and their weaknesses

## Mục tiêu bài học

**Năng lực cần chứng minh.** Lấy dòng dõi bằng ít nhất ba cách, hợp nhất, và định lượng độ phủ cùng vùng mù của từng cách.

**Điều kiện hoàn thành.** Ba cách đều có tỉ lệ phủ đo được trên cùng tập tài sản, và phần không cách nào phủ được đánh dấu trạng thái không rõ.

> [!abstract] Câu hỏi trung tâm
> Năm phương pháp extraction lineage có coverage, freshness và failure modes khác nhau thế nào?

## 1. Declared configuration

DAG/dbt/config graph cho intended dependencies nhưng có thể bỏ dynamic behavior và chưa chứng minh run xảy ra. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `Five extraction methods and their weaknesses`, câu hỏi thực dụng là: Năm phương pháp extraction lineage có coverage, freshness và failure modes khác nhau thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Static parsing

SQL/code parser rẻ và pre-run nhưng dialect, macros, UDF, dynamic identifiers và procedural logic tạo unknown edges. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `Five extraction methods and their weaknesses`, câu hỏi thực dụng là: Năm phương pháp extraction lineage có coverage, freshness và failure modes khác nhau thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Runtime instrumentation

Events/hooks thấy executed inputs/outputs và run context nhưng cần adoption, delivery và version compatibility. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `Five extraction methods and their weaknesses`, câu hỏi thực dụng là: Năm phương pháp extraction lineage có coverage, freshness và failure modes khác nhau thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Query-log inference

Warehouse history phản ánh execution thật song retention, permissions, temp objects và parser limits làm coverage không đầy đủ. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `Five extraction methods and their weaknesses`, câu hỏi thực dụng là: Năm phương pháp extraction lineage có coverage, freshness và failure modes khác nhau thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Manual curation

Chuyên gia bổ sung semantic edge nhưng freshness, scale và conflict với automated producers cần governance. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `Five extraction methods and their weaknesses`, câu hỏi thực dụng là: Năm phương pháp extraction lineage có coverage, freshness và failure modes khác nhau thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Hybrid evaluation

So methods trên signed fixture, đo precision/recall/unknown, latency và cost; merge theo producer authority, không union mù. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `Five extraction methods and their weaknesses`, câu hỏi thực dụng là: Năm phương pháp extraction lineage có coverage, freshness và failure modes khác nhau thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.metadata.lineage-extraction-methods`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Chạy connector/parser/event fixture có expected entity-edge manifest, tiêm partial failure hoặc ambiguity và đo missing/extra/unknown theo producer. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. Five extraction methods and their weaknesses: kiểm `Declared configuration` bằng case 1, cụ thể dag/dbt/config graph cho intended dependencies nhưng có thể bỏ dynamic behavior và chưa chứng minh run xảy ra

**Mệnh đề cần kiểm.** Five extraction methods and their weaknesses: kiểm `Declared configuration` bằng case 1, cụ thể dag/dbt/config graph cho intended dependencies nhưng có thể bỏ dynamic behavior và chưa chứng minh run xảy ra.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-extraction-methods`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Five extraction methods and their weaknesses` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `Five extraction methods and their weaknesses`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. Five extraction methods and their weaknesses: kiểm `Static parsing` bằng case 2, cụ thể sql/code parser rẻ và pre-run nhưng dialect, macros, udf, dynamic identifiers và procedural logic tạo unknown edges

**Mệnh đề cần kiểm.** Five extraction methods and their weaknesses: kiểm `Static parsing` bằng case 2, cụ thể sql/code parser rẻ và pre-run nhưng dialect, macros, udf, dynamic identifiers và procedural logic tạo unknown edges.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-extraction-methods`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Five extraction methods and their weaknesses` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `Five extraction methods and their weaknesses`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. Five extraction methods and their weaknesses: kiểm `Runtime instrumentation` bằng case 3, cụ thể events/hooks thấy executed inputs/outputs và run context nhưng cần adoption, delivery và version compatibility

**Mệnh đề cần kiểm.** Five extraction methods and their weaknesses: kiểm `Runtime instrumentation` bằng case 3, cụ thể events/hooks thấy executed inputs/outputs và run context nhưng cần adoption, delivery và version compatibility.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-extraction-methods`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Five extraction methods and their weaknesses` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `Five extraction methods and their weaknesses`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. Five extraction methods and their weaknesses: kiểm `Query-log inference` bằng case 4, cụ thể warehouse history phản ánh execution thật song retention, permissions, temp objects và parser limits làm coverage không đầy đủ

**Mệnh đề cần kiểm.** Five extraction methods and their weaknesses: kiểm `Query-log inference` bằng case 4, cụ thể warehouse history phản ánh execution thật song retention, permissions, temp objects và parser limits làm coverage không đầy đủ.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-extraction-methods`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Five extraction methods and their weaknesses` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `Five extraction methods and their weaknesses`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. Five extraction methods and their weaknesses: kiểm `Manual curation` bằng case 5, cụ thể chuyên gia bổ sung semantic edge nhưng freshness, scale và conflict với automated producers cần governance

**Mệnh đề cần kiểm.** Five extraction methods and their weaknesses: kiểm `Manual curation` bằng case 5, cụ thể chuyên gia bổ sung semantic edge nhưng freshness, scale và conflict với automated producers cần governance.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-extraction-methods`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Five extraction methods and their weaknesses` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `Five extraction methods and their weaknesses`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. Five extraction methods and their weaknesses: kiểm `Hybrid evaluation` bằng case 6, cụ thể so methods trên signed fixture, đo precision/recall/unknown, latency và cost; merge theo producer authority, không union mù

**Mệnh đề cần kiểm.** Five extraction methods and their weaknesses: kiểm `Hybrid evaluation` bằng case 6, cụ thể so methods trên signed fixture, đo precision/recall/unknown, latency và cost; merge theo producer authority, không union mù.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-extraction-methods`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Five extraction methods and their weaknesses` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `Five extraction methods and their weaknesses`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. Five extraction methods and their weaknesses: kiểm `Declared configuration` bằng case 7, cụ thể dag/dbt/config graph cho intended dependencies nhưng có thể bỏ dynamic behavior và chưa chứng minh run xảy ra

**Mệnh đề cần kiểm.** Five extraction methods and their weaknesses: kiểm `Declared configuration` bằng case 7, cụ thể dag/dbt/config graph cho intended dependencies nhưng có thể bỏ dynamic behavior và chưa chứng minh run xảy ra.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-extraction-methods`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Five extraction methods and their weaknesses` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `Five extraction methods and their weaknesses`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. Five extraction methods and their weaknesses: kiểm `Static parsing` bằng case 8, cụ thể sql/code parser rẻ và pre-run nhưng dialect, macros, udf, dynamic identifiers và procedural logic tạo unknown edges

**Mệnh đề cần kiểm.** Five extraction methods and their weaknesses: kiểm `Static parsing` bằng case 8, cụ thể sql/code parser rẻ và pre-run nhưng dialect, macros, udf, dynamic identifiers và procedural logic tạo unknown edges.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-extraction-methods`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Five extraction methods and their weaknesses` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `Five extraction methods and their weaknesses`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. Five extraction methods and their weaknesses: kiểm `Runtime instrumentation` bằng case 9, cụ thể events/hooks thấy executed inputs/outputs và run context nhưng cần adoption, delivery và version compatibility

**Mệnh đề cần kiểm.** Five extraction methods and their weaknesses: kiểm `Runtime instrumentation` bằng case 9, cụ thể events/hooks thấy executed inputs/outputs và run context nhưng cần adoption, delivery và version compatibility.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-extraction-methods`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Five extraction methods and their weaknesses` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `Five extraction methods and their weaknesses`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. Five extraction methods and their weaknesses: kiểm `Query-log inference` bằng case 10, cụ thể warehouse history phản ánh execution thật song retention, permissions, temp objects và parser limits làm coverage không đầy đủ

**Mệnh đề cần kiểm.** Five extraction methods and their weaknesses: kiểm `Query-log inference` bằng case 10, cụ thể warehouse history phản ánh execution thật song retention, permissions, temp objects và parser limits làm coverage không đầy đủ.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-extraction-methods`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Five extraction methods and their weaknesses` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `Five extraction methods and their weaknesses`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. Five extraction methods and their weaknesses: kiểm `Manual curation` bằng case 11, cụ thể chuyên gia bổ sung semantic edge nhưng freshness, scale và conflict với automated producers cần governance

**Mệnh đề cần kiểm.** Five extraction methods and their weaknesses: kiểm `Manual curation` bằng case 11, cụ thể chuyên gia bổ sung semantic edge nhưng freshness, scale và conflict với automated producers cần governance.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-extraction-methods`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Five extraction methods and their weaknesses` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `Five extraction methods and their weaknesses`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. Five extraction methods and their weaknesses: kiểm `Hybrid evaluation` bằng case 12, cụ thể so methods trên signed fixture, đo precision/recall/unknown, latency và cost; merge theo producer authority, không union mù

**Mệnh đề cần kiểm.** Five extraction methods and their weaknesses: kiểm `Hybrid evaluation` bằng case 12, cụ thể so methods trên signed fixture, đo precision/recall/unknown, latency và cost; merge theo producer authority, không union mù.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-extraction-methods`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Five extraction methods and their weaknesses` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `Five extraction methods and their weaknesses`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. Five extraction methods and their weaknesses: kiểm `Declared configuration` bằng case 13, cụ thể dag/dbt/config graph cho intended dependencies nhưng có thể bỏ dynamic behavior và chưa chứng minh run xảy ra

**Mệnh đề cần kiểm.** Five extraction methods and their weaknesses: kiểm `Declared configuration` bằng case 13, cụ thể dag/dbt/config graph cho intended dependencies nhưng có thể bỏ dynamic behavior và chưa chứng minh run xảy ra.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-extraction-methods`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Five extraction methods and their weaknesses` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `Five extraction methods and their weaknesses`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. Five extraction methods and their weaknesses: kiểm `Static parsing` bằng case 14, cụ thể sql/code parser rẻ và pre-run nhưng dialect, macros, udf, dynamic identifiers và procedural logic tạo unknown edges

**Mệnh đề cần kiểm.** Five extraction methods and their weaknesses: kiểm `Static parsing` bằng case 14, cụ thể sql/code parser rẻ và pre-run nhưng dialect, macros, udf, dynamic identifiers và procedural logic tạo unknown edges.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-extraction-methods`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Five extraction methods and their weaknesses` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `Five extraction methods and their weaknesses`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. Five extraction methods and their weaknesses: kiểm `Runtime instrumentation` bằng case 15, cụ thể events/hooks thấy executed inputs/outputs và run context nhưng cần adoption, delivery và version compatibility

**Mệnh đề cần kiểm.** Five extraction methods and their weaknesses: kiểm `Runtime instrumentation` bằng case 15, cụ thể events/hooks thấy executed inputs/outputs và run context nhưng cần adoption, delivery và version compatibility.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-extraction-methods`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Five extraction methods and their weaknesses` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `Five extraction methods and their weaknesses`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `Five extraction methods and their weaknesses` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `Five extraction methods and their weaknesses: kiểm `Declared configuration` bằng case 1, cụ thể dag/dbt/config graph cho intended dependencies nhưng có thể bỏ dynamic behavior và chưa chứng minh run xảy ra` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `Five extraction methods and their weaknesses: kiểm `Runtime instrumentation` bằng case 3, cụ thể events/hooks thấy executed inputs/outputs và run context nhưng cần adoption, delivery và version compatibility`?
3. Counterexample nhỏ nhất cho `Five extraction methods and their weaknesses: kiểm `Hybrid evaluation` bằng case 6, cụ thể so methods trên signed fixture, đo precision/recall/unknown, latency và cost; merge theo producer authority, không union mù` gồm những state nào?
4. `Five extraction methods and their weaknesses: kiểm `Runtime instrumentation` bằng case 9, cụ thể events/hooks thấy executed inputs/outputs và run context nhưng cần adoption, delivery và version compatibility` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `Five extraction methods and their weaknesses: kiểm `Static parsing` bằng case 14, cụ thể sql/code parser rẻ và pre-run nhưng dialect, macros, udf, dynamic identifiers và procedural logic tạo unknown edges` phải đảo?
6. Phần nào của `Five extraction methods and their weaknesses: kiểm `Runtime instrumentation` bằng case 15, cụ thể events/hooks thấy executed inputs/outputs và run context nhưng cần adoption, delivery và version compatibility` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Five extraction methods and their weaknesses` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-OPENLINEAGE-OVERVIEW]]
2. [[SRC-OPENLINEAGE-FACETS]]
3. [[SRC-DATAHUB-LINEAGE]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-OPENLINEAGE-OVERVIEW]] | Contract hoặc cơ chế liên quan trực tiếp tới `Five extraction methods and their weaknesses` | Đã đọc locator; cần pin version khi chạy lab |
| [[SRC-OPENLINEAGE-FACETS]] | Contract hoặc cơ chế liên quan trực tiếp tới `Five extraction methods and their weaknesses` | Đã đọc locator; cần pin version khi chạy lab |
| [[SRC-DATAHUB-LINEAGE]] | Contract hoặc cơ chế liên quan trực tiếp tới `Five extraction methods and their weaknesses` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Extraction methods có bias khác nhau và cần hybrid evaluation có unknown state.
- Với `wiki.metadata.lineage-extraction-methods`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Năm phương pháp extraction lineage có coverage, freshness và failure modes khác nhau thế nào?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.web.openlineage-overview, src.web.openlineage-facets, src.web.datahub-lineage` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.

# Phase 8: Distributed Systems, Streaming and Compute
# Module 23: Spark, Flink and Distributed Compute Engines
# Lesson 347: Narrow and wide dependencies, and why exchange creates a stage

## Mục tiêu bài học

**Năng lực cần chứng minh.** Phân loại phép biến đổi theo hai loại phụ thuộc và giảm được số bước xáo trộn của một công việc thật.

**Điều kiện hoàn thành.** Số bước trao đổi giảm ≥ 1 với thời gian giảm có số đo, và kết quả đối soát khớp bản gốc tuyệt đối.

> [!abstract] Câu hỏi trung tâm
> Narrow/wide dependency và Exchange giải thích stage boundary, pipelining và recomputation ra sao?

## 1. Narrow dependency

Một child partition cần ít parent partitions xác định, cho phép pipeline transformations trong cùng stage. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `Narrow and wide dependencies, and why exchange creates a stage`, câu hỏi thực dụng là: Narrow/wide dependency và Exchange giải thích stage boundary, pipelining và recomputation ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Wide dependency

Output partition phụ thuộc nhiều parent partitions, thường đòi redistribution và materialized shuffle boundary. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `Narrow and wide dependencies, and why exchange creates a stage`, câu hỏi thực dụng là: Narrow/wide dependency và Exchange giải thích stage boundary, pipelining và recomputation ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Exchange

Physical Exchange mô tả repartition/broadcast requirement; scheduler materializes shuffle stages quanh dependency boundary. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `Narrow and wide dependencies, and why exchange creates a stage`, câu hỏi thực dụng là: Narrow/wide dependency và Exchange giải thích stage boundary, pipelining và recomputation ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Tasks and partitions

Mỗi stage tạo tasks theo partitions của stage output/input; task count không phải số records hay executors. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `Narrow and wide dependencies, and why exchange creates a stage`, câu hỏi thực dụng là: Narrow/wide dependency và Exchange giải thích stage boundary, pipelining và recomputation ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Failure recovery

Narrow lineage có thể recompute partition chain; lost shuffle blocks có thể buộc rerun upstream map outputs. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `Narrow and wide dependencies, and why exchange creates a stage`, câu hỏi thực dụng là: Narrow/wide dependency và Exchange giải thích stage boundary, pipelining và recomputation ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Plan lab

So map/filter với groupBy/repartition/join, chụp plan và UI rồi nối Exchange IDs với stages và shuffle metrics. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `Narrow and wide dependencies, and why exchange creates a stage`, câu hỏi thực dụng là: Narrow/wide dependency và Exchange giải thích stage boundary, pipelining và recomputation ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.spark.dependencies-exchange-stage`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Run a version-pinned Spark fixture with fixed inputs, capture explain/UI/event-log evidence, inject one changed constraint and reconcile output hashes plus operator/task metrics. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. Narrow and wide dependencies, and why exchange creates a stage: kiểm `Narrow dependency` bằng case 1, cụ thể một child partition cần ít parent partitions xác định, cho phép pipeline transformations trong cùng stage

**Mệnh đề cần kiểm.** Narrow and wide dependencies, and why exchange creates a stage: kiểm `Narrow dependency` bằng case 1, cụ thể một child partition cần ít parent partitions xác định, cho phép pipeline transformations trong cùng stage.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.dependencies-exchange-stage`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Narrow and wide dependencies, and why exchange creates a stage` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `Narrow and wide dependencies, and why exchange creates a stage`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. Narrow and wide dependencies, and why exchange creates a stage: kiểm `Wide dependency` bằng case 2, cụ thể output partition phụ thuộc nhiều parent partitions, thường đòi redistribution và materialized shuffle boundary

**Mệnh đề cần kiểm.** Narrow and wide dependencies, and why exchange creates a stage: kiểm `Wide dependency` bằng case 2, cụ thể output partition phụ thuộc nhiều parent partitions, thường đòi redistribution và materialized shuffle boundary.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.dependencies-exchange-stage`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Narrow and wide dependencies, and why exchange creates a stage` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `Narrow and wide dependencies, and why exchange creates a stage`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. Narrow and wide dependencies, and why exchange creates a stage: kiểm `Exchange` bằng case 3, cụ thể physical exchange mô tả repartition/broadcast requirement; scheduler materializes shuffle stages quanh dependency boundary

**Mệnh đề cần kiểm.** Narrow and wide dependencies, and why exchange creates a stage: kiểm `Exchange` bằng case 3, cụ thể physical exchange mô tả repartition/broadcast requirement; scheduler materializes shuffle stages quanh dependency boundary.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.dependencies-exchange-stage`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Narrow and wide dependencies, and why exchange creates a stage` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `Narrow and wide dependencies, and why exchange creates a stage`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. Narrow and wide dependencies, and why exchange creates a stage: kiểm `Tasks and partitions` bằng case 4, cụ thể mỗi stage tạo tasks theo partitions của stage output/input; task count không phải số records hay executors

**Mệnh đề cần kiểm.** Narrow and wide dependencies, and why exchange creates a stage: kiểm `Tasks and partitions` bằng case 4, cụ thể mỗi stage tạo tasks theo partitions của stage output/input; task count không phải số records hay executors.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.dependencies-exchange-stage`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Narrow and wide dependencies, and why exchange creates a stage` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `Narrow and wide dependencies, and why exchange creates a stage`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. Narrow and wide dependencies, and why exchange creates a stage: kiểm `Failure recovery` bằng case 5, cụ thể narrow lineage có thể recompute partition chain; lost shuffle blocks có thể buộc rerun upstream map outputs

**Mệnh đề cần kiểm.** Narrow and wide dependencies, and why exchange creates a stage: kiểm `Failure recovery` bằng case 5, cụ thể narrow lineage có thể recompute partition chain; lost shuffle blocks có thể buộc rerun upstream map outputs.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.dependencies-exchange-stage`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Narrow and wide dependencies, and why exchange creates a stage` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `Narrow and wide dependencies, and why exchange creates a stage`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. Narrow and wide dependencies, and why exchange creates a stage: kiểm `Plan lab` bằng case 6, cụ thể so map/filter với groupby/repartition/join, chụp plan và ui rồi nối exchange ids với stages và shuffle metrics

**Mệnh đề cần kiểm.** Narrow and wide dependencies, and why exchange creates a stage: kiểm `Plan lab` bằng case 6, cụ thể so map/filter với groupby/repartition/join, chụp plan và ui rồi nối exchange ids với stages và shuffle metrics.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.dependencies-exchange-stage`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Narrow and wide dependencies, and why exchange creates a stage` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `Narrow and wide dependencies, and why exchange creates a stage`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. Narrow and wide dependencies, and why exchange creates a stage: kiểm `Narrow dependency` bằng case 7, cụ thể một child partition cần ít parent partitions xác định, cho phép pipeline transformations trong cùng stage

**Mệnh đề cần kiểm.** Narrow and wide dependencies, and why exchange creates a stage: kiểm `Narrow dependency` bằng case 7, cụ thể một child partition cần ít parent partitions xác định, cho phép pipeline transformations trong cùng stage.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.dependencies-exchange-stage`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Narrow and wide dependencies, and why exchange creates a stage` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `Narrow and wide dependencies, and why exchange creates a stage`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. Narrow and wide dependencies, and why exchange creates a stage: kiểm `Wide dependency` bằng case 8, cụ thể output partition phụ thuộc nhiều parent partitions, thường đòi redistribution và materialized shuffle boundary

**Mệnh đề cần kiểm.** Narrow and wide dependencies, and why exchange creates a stage: kiểm `Wide dependency` bằng case 8, cụ thể output partition phụ thuộc nhiều parent partitions, thường đòi redistribution và materialized shuffle boundary.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.dependencies-exchange-stage`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Narrow and wide dependencies, and why exchange creates a stage` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `Narrow and wide dependencies, and why exchange creates a stage`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. Narrow and wide dependencies, and why exchange creates a stage: kiểm `Exchange` bằng case 9, cụ thể physical exchange mô tả repartition/broadcast requirement; scheduler materializes shuffle stages quanh dependency boundary

**Mệnh đề cần kiểm.** Narrow and wide dependencies, and why exchange creates a stage: kiểm `Exchange` bằng case 9, cụ thể physical exchange mô tả repartition/broadcast requirement; scheduler materializes shuffle stages quanh dependency boundary.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.dependencies-exchange-stage`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Narrow and wide dependencies, and why exchange creates a stage` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `Narrow and wide dependencies, and why exchange creates a stage`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. Narrow and wide dependencies, and why exchange creates a stage: kiểm `Tasks and partitions` bằng case 10, cụ thể mỗi stage tạo tasks theo partitions của stage output/input; task count không phải số records hay executors

**Mệnh đề cần kiểm.** Narrow and wide dependencies, and why exchange creates a stage: kiểm `Tasks and partitions` bằng case 10, cụ thể mỗi stage tạo tasks theo partitions của stage output/input; task count không phải số records hay executors.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.dependencies-exchange-stage`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Narrow and wide dependencies, and why exchange creates a stage` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `Narrow and wide dependencies, and why exchange creates a stage`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. Narrow and wide dependencies, and why exchange creates a stage: kiểm `Failure recovery` bằng case 11, cụ thể narrow lineage có thể recompute partition chain; lost shuffle blocks có thể buộc rerun upstream map outputs

**Mệnh đề cần kiểm.** Narrow and wide dependencies, and why exchange creates a stage: kiểm `Failure recovery` bằng case 11, cụ thể narrow lineage có thể recompute partition chain; lost shuffle blocks có thể buộc rerun upstream map outputs.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.dependencies-exchange-stage`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Narrow and wide dependencies, and why exchange creates a stage` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `Narrow and wide dependencies, and why exchange creates a stage`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. Narrow and wide dependencies, and why exchange creates a stage: kiểm `Plan lab` bằng case 12, cụ thể so map/filter với groupby/repartition/join, chụp plan và ui rồi nối exchange ids với stages và shuffle metrics

**Mệnh đề cần kiểm.** Narrow and wide dependencies, and why exchange creates a stage: kiểm `Plan lab` bằng case 12, cụ thể so map/filter với groupby/repartition/join, chụp plan và ui rồi nối exchange ids với stages và shuffle metrics.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.dependencies-exchange-stage`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Narrow and wide dependencies, and why exchange creates a stage` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `Narrow and wide dependencies, and why exchange creates a stage`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. Narrow and wide dependencies, and why exchange creates a stage: kiểm `Narrow dependency` bằng case 13, cụ thể một child partition cần ít parent partitions xác định, cho phép pipeline transformations trong cùng stage

**Mệnh đề cần kiểm.** Narrow and wide dependencies, and why exchange creates a stage: kiểm `Narrow dependency` bằng case 13, cụ thể một child partition cần ít parent partitions xác định, cho phép pipeline transformations trong cùng stage.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.dependencies-exchange-stage`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Narrow and wide dependencies, and why exchange creates a stage` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `Narrow and wide dependencies, and why exchange creates a stage`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. Narrow and wide dependencies, and why exchange creates a stage: kiểm `Wide dependency` bằng case 14, cụ thể output partition phụ thuộc nhiều parent partitions, thường đòi redistribution và materialized shuffle boundary

**Mệnh đề cần kiểm.** Narrow and wide dependencies, and why exchange creates a stage: kiểm `Wide dependency` bằng case 14, cụ thể output partition phụ thuộc nhiều parent partitions, thường đòi redistribution và materialized shuffle boundary.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.dependencies-exchange-stage`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Narrow and wide dependencies, and why exchange creates a stage` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `Narrow and wide dependencies, and why exchange creates a stage`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. Narrow and wide dependencies, and why exchange creates a stage: kiểm `Exchange` bằng case 15, cụ thể physical exchange mô tả repartition/broadcast requirement; scheduler materializes shuffle stages quanh dependency boundary

**Mệnh đề cần kiểm.** Narrow and wide dependencies, and why exchange creates a stage: kiểm `Exchange` bằng case 15, cụ thể physical exchange mô tả repartition/broadcast requirement; scheduler materializes shuffle stages quanh dependency boundary.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.dependencies-exchange-stage`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Narrow and wide dependencies, and why exchange creates a stage` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `Narrow and wide dependencies, and why exchange creates a stage`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `Narrow and wide dependencies, and why exchange creates a stage` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `Narrow and wide dependencies, and why exchange creates a stage: kiểm `Narrow dependency` bằng case 1, cụ thể một child partition cần ít parent partitions xác định, cho phép pipeline transformations trong cùng stage` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `Narrow and wide dependencies, and why exchange creates a stage: kiểm `Exchange` bằng case 3, cụ thể physical exchange mô tả repartition/broadcast requirement; scheduler materializes shuffle stages quanh dependency boundary`?
3. Counterexample nhỏ nhất cho `Narrow and wide dependencies, and why exchange creates a stage: kiểm `Plan lab` bằng case 6, cụ thể so map/filter với groupby/repartition/join, chụp plan và ui rồi nối exchange ids với stages và shuffle metrics` gồm những state nào?
4. `Narrow and wide dependencies, and why exchange creates a stage: kiểm `Exchange` bằng case 9, cụ thể physical exchange mô tả repartition/broadcast requirement; scheduler materializes shuffle stages quanh dependency boundary` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `Narrow and wide dependencies, and why exchange creates a stage: kiểm `Wide dependency` bằng case 14, cụ thể output partition phụ thuộc nhiều parent partitions, thường đòi redistribution và materialized shuffle boundary` phải đảo?
6. Phần nào của `Narrow and wide dependencies, and why exchange creates a stage: kiểm `Exchange` bằng case 15, cụ thể physical exchange mô tả repartition/broadcast requirement; scheduler materializes shuffle stages quanh dependency boundary` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Narrow and wide dependencies, and why exchange creates a stage` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-APACHE-SPARK-RDD-GUIDE]]
2. [[SRC-APACHE-SPARK-SQL-PERFORMANCE]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-APACHE-SPARK-RDD-GUIDE]] | Contract hoặc cơ chế liên quan trực tiếp tới `Narrow and wide dependencies, and why exchange creates a stage` | Đã đọc locator; cần pin version khi chạy lab |
| [[SRC-APACHE-SPARK-SQL-PERFORMANCE]] | Contract hoặc cơ chế liên quan trực tiếp tới `Narrow and wide dependencies, and why exchange creates a stage` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Exchange marks a distribution requirement that commonly creates a shuffle stage boundary.
- Với `wiki.spark.dependencies-exchange-stage`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Narrow/wide dependency và Exchange giải thích stage boundary, pipelining và recomputation ra sao?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.web.apache-spark-rdd-guide, src.web.apache-spark-sql-performance` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.

# Phase 8: Distributed Systems, Streaming and Compute
# Module 23: Spark, Flink and Distributed Compute Engines
# Lesson 345: Cluster roles and the execution hierarchy

## Mục tiêu bài học

**Năng lực cần chứng minh.** Ánh xạ năm từ vựng thực thi vào một ứng dụng thật và đếm đúng số tác vụ của từng giai đoạn.

**Điều kiện hoàn thành.** Đếm đúng số giai đoạn và tác vụ cho ba công việc, và giải thích được số tác vụ đến từ số phân vùng.

> [!abstract] Câu hỏi trung tâm
> Driver, cluster manager, executors, jobs, stages và tasks liên hệ thế nào trong một Spark application?

## 1. Application boundary

Mỗi Spark application có driver và executor processes riêng; cache và execution state không mặc nhiên chia sẻ giữa applications. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `Cluster roles and the execution hierarchy`, câu hỏi thực dụng là: Driver, cluster manager, executors, jobs, stages và tasks liên hệ thế nào trong một Spark application? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Driver

Driver chạy user main, tạo context/session, xây execution và điều phối work; mất driver thường kết thúc application theo deploy mode. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `Cluster roles and the execution hierarchy`, câu hỏi thực dụng là: Driver, cluster manager, executors, jobs, stages và tasks liên hệ thế nào trong một Spark application? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Cluster manager

Standalone, YARN hoặc Kubernetes cấp resources; scheduler backend biến allocation thành executors cho application. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `Cluster roles and the execution hierarchy`, câu hỏi thực dụng là: Driver, cluster manager, executors, jobs, stages và tasks liên hệ thế nào trong một Spark application? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Executor

Executor chạy tasks và giữ data/cache cho application; mất executor làm mất block và có thể khiến task recompute. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `Cluster roles and the execution hierarchy`, câu hỏi thực dụng là: Driver, cluster manager, executors, jobs, stages và tasks liên hệ thế nào trong một Spark application? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Hierarchy

Action tạo job, shuffle boundaries chia stages, partition thường ánh xạ thành task; SQL có thêm plan/operator layer. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `Cluster roles and the execution hierarchy`, câu hỏi thực dụng là: Driver, cluster manager, executors, jobs, stages và tasks liên hệ thế nào trong một Spark application? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Evidence

Spark UI/event log phải nối application, job, stage, task, executor, attempt và failure reason thay vì chỉ báo elapsed time. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `Cluster roles and the execution hierarchy`, câu hỏi thực dụng là: Driver, cluster manager, executors, jobs, stages và tasks liên hệ thế nào trong một Spark application? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.spark.cluster-roles-execution-hierarchy`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Run a version-pinned CDC or Spark fixture, inject the declared mutation/failure and reconcile identities, positions, attempts and final state against an independent oracle. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. Cluster roles and the execution hierarchy: kiểm `Application boundary` bằng case 1, cụ thể mỗi spark application có driver và executor processes riêng; cache và execution state không mặc nhiên chia sẻ giữa applications

**Mệnh đề cần kiểm.** Cluster roles and the execution hierarchy: kiểm `Application boundary` bằng case 1, cụ thể mỗi spark application có driver và executor processes riêng; cache và execution state không mặc nhiên chia sẻ giữa applications.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.cluster-roles-execution-hierarchy`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Cluster roles and the execution hierarchy` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `Cluster roles and the execution hierarchy`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. Cluster roles and the execution hierarchy: kiểm `Driver` bằng case 2, cụ thể driver chạy user main, tạo context/session, xây execution và điều phối work; mất driver thường kết thúc application theo deploy mode

**Mệnh đề cần kiểm.** Cluster roles and the execution hierarchy: kiểm `Driver` bằng case 2, cụ thể driver chạy user main, tạo context/session, xây execution và điều phối work; mất driver thường kết thúc application theo deploy mode.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.cluster-roles-execution-hierarchy`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Cluster roles and the execution hierarchy` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `Cluster roles and the execution hierarchy`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. Cluster roles and the execution hierarchy: kiểm `Cluster manager` bằng case 3, cụ thể standalone, yarn hoặc kubernetes cấp resources; scheduler backend biến allocation thành executors cho application

**Mệnh đề cần kiểm.** Cluster roles and the execution hierarchy: kiểm `Cluster manager` bằng case 3, cụ thể standalone, yarn hoặc kubernetes cấp resources; scheduler backend biến allocation thành executors cho application.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.cluster-roles-execution-hierarchy`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Cluster roles and the execution hierarchy` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `Cluster roles and the execution hierarchy`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. Cluster roles and the execution hierarchy: kiểm `Executor` bằng case 4, cụ thể executor chạy tasks và giữ data/cache cho application; mất executor làm mất block và có thể khiến task recompute

**Mệnh đề cần kiểm.** Cluster roles and the execution hierarchy: kiểm `Executor` bằng case 4, cụ thể executor chạy tasks và giữ data/cache cho application; mất executor làm mất block và có thể khiến task recompute.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.cluster-roles-execution-hierarchy`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Cluster roles and the execution hierarchy` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `Cluster roles and the execution hierarchy`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. Cluster roles and the execution hierarchy: kiểm `Hierarchy` bằng case 5, cụ thể action tạo job, shuffle boundaries chia stages, partition thường ánh xạ thành task; sql có thêm plan/operator layer

**Mệnh đề cần kiểm.** Cluster roles and the execution hierarchy: kiểm `Hierarchy` bằng case 5, cụ thể action tạo job, shuffle boundaries chia stages, partition thường ánh xạ thành task; sql có thêm plan/operator layer.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.cluster-roles-execution-hierarchy`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Cluster roles and the execution hierarchy` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `Cluster roles and the execution hierarchy`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. Cluster roles and the execution hierarchy: kiểm `Evidence` bằng case 6, cụ thể spark ui/event log phải nối application, job, stage, task, executor, attempt và failure reason thay vì chỉ báo elapsed time

**Mệnh đề cần kiểm.** Cluster roles and the execution hierarchy: kiểm `Evidence` bằng case 6, cụ thể spark ui/event log phải nối application, job, stage, task, executor, attempt và failure reason thay vì chỉ báo elapsed time.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.cluster-roles-execution-hierarchy`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Cluster roles and the execution hierarchy` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `Cluster roles and the execution hierarchy`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. Cluster roles and the execution hierarchy: kiểm `Application boundary` bằng case 7, cụ thể mỗi spark application có driver và executor processes riêng; cache và execution state không mặc nhiên chia sẻ giữa applications

**Mệnh đề cần kiểm.** Cluster roles and the execution hierarchy: kiểm `Application boundary` bằng case 7, cụ thể mỗi spark application có driver và executor processes riêng; cache và execution state không mặc nhiên chia sẻ giữa applications.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.cluster-roles-execution-hierarchy`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Cluster roles and the execution hierarchy` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `Cluster roles and the execution hierarchy`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. Cluster roles and the execution hierarchy: kiểm `Driver` bằng case 8, cụ thể driver chạy user main, tạo context/session, xây execution và điều phối work; mất driver thường kết thúc application theo deploy mode

**Mệnh đề cần kiểm.** Cluster roles and the execution hierarchy: kiểm `Driver` bằng case 8, cụ thể driver chạy user main, tạo context/session, xây execution và điều phối work; mất driver thường kết thúc application theo deploy mode.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.cluster-roles-execution-hierarchy`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Cluster roles and the execution hierarchy` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `Cluster roles and the execution hierarchy`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. Cluster roles and the execution hierarchy: kiểm `Cluster manager` bằng case 9, cụ thể standalone, yarn hoặc kubernetes cấp resources; scheduler backend biến allocation thành executors cho application

**Mệnh đề cần kiểm.** Cluster roles and the execution hierarchy: kiểm `Cluster manager` bằng case 9, cụ thể standalone, yarn hoặc kubernetes cấp resources; scheduler backend biến allocation thành executors cho application.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.cluster-roles-execution-hierarchy`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Cluster roles and the execution hierarchy` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `Cluster roles and the execution hierarchy`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. Cluster roles and the execution hierarchy: kiểm `Executor` bằng case 10, cụ thể executor chạy tasks và giữ data/cache cho application; mất executor làm mất block và có thể khiến task recompute

**Mệnh đề cần kiểm.** Cluster roles and the execution hierarchy: kiểm `Executor` bằng case 10, cụ thể executor chạy tasks và giữ data/cache cho application; mất executor làm mất block và có thể khiến task recompute.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.cluster-roles-execution-hierarchy`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Cluster roles and the execution hierarchy` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `Cluster roles and the execution hierarchy`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. Cluster roles and the execution hierarchy: kiểm `Hierarchy` bằng case 11, cụ thể action tạo job, shuffle boundaries chia stages, partition thường ánh xạ thành task; sql có thêm plan/operator layer

**Mệnh đề cần kiểm.** Cluster roles and the execution hierarchy: kiểm `Hierarchy` bằng case 11, cụ thể action tạo job, shuffle boundaries chia stages, partition thường ánh xạ thành task; sql có thêm plan/operator layer.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.cluster-roles-execution-hierarchy`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Cluster roles and the execution hierarchy` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `Cluster roles and the execution hierarchy`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. Cluster roles and the execution hierarchy: kiểm `Evidence` bằng case 12, cụ thể spark ui/event log phải nối application, job, stage, task, executor, attempt và failure reason thay vì chỉ báo elapsed time

**Mệnh đề cần kiểm.** Cluster roles and the execution hierarchy: kiểm `Evidence` bằng case 12, cụ thể spark ui/event log phải nối application, job, stage, task, executor, attempt và failure reason thay vì chỉ báo elapsed time.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.cluster-roles-execution-hierarchy`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Cluster roles and the execution hierarchy` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `Cluster roles and the execution hierarchy`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. Cluster roles and the execution hierarchy: kiểm `Application boundary` bằng case 13, cụ thể mỗi spark application có driver và executor processes riêng; cache và execution state không mặc nhiên chia sẻ giữa applications

**Mệnh đề cần kiểm.** Cluster roles and the execution hierarchy: kiểm `Application boundary` bằng case 13, cụ thể mỗi spark application có driver và executor processes riêng; cache và execution state không mặc nhiên chia sẻ giữa applications.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.cluster-roles-execution-hierarchy`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Cluster roles and the execution hierarchy` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `Cluster roles and the execution hierarchy`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. Cluster roles and the execution hierarchy: kiểm `Driver` bằng case 14, cụ thể driver chạy user main, tạo context/session, xây execution và điều phối work; mất driver thường kết thúc application theo deploy mode

**Mệnh đề cần kiểm.** Cluster roles and the execution hierarchy: kiểm `Driver` bằng case 14, cụ thể driver chạy user main, tạo context/session, xây execution và điều phối work; mất driver thường kết thúc application theo deploy mode.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.cluster-roles-execution-hierarchy`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Cluster roles and the execution hierarchy` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `Cluster roles and the execution hierarchy`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. Cluster roles and the execution hierarchy: kiểm `Cluster manager` bằng case 15, cụ thể standalone, yarn hoặc kubernetes cấp resources; scheduler backend biến allocation thành executors cho application

**Mệnh đề cần kiểm.** Cluster roles and the execution hierarchy: kiểm `Cluster manager` bằng case 15, cụ thể standalone, yarn hoặc kubernetes cấp resources; scheduler backend biến allocation thành executors cho application.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.cluster-roles-execution-hierarchy`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Cluster roles and the execution hierarchy` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `Cluster roles and the execution hierarchy`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `Cluster roles and the execution hierarchy` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `Cluster roles and the execution hierarchy: kiểm `Application boundary` bằng case 1, cụ thể mỗi spark application có driver và executor processes riêng; cache và execution state không mặc nhiên chia sẻ giữa applications` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `Cluster roles and the execution hierarchy: kiểm `Cluster manager` bằng case 3, cụ thể standalone, yarn hoặc kubernetes cấp resources; scheduler backend biến allocation thành executors cho application`?
3. Counterexample nhỏ nhất cho `Cluster roles and the execution hierarchy: kiểm `Evidence` bằng case 6, cụ thể spark ui/event log phải nối application, job, stage, task, executor, attempt và failure reason thay vì chỉ báo elapsed time` gồm những state nào?
4. `Cluster roles and the execution hierarchy: kiểm `Cluster manager` bằng case 9, cụ thể standalone, yarn hoặc kubernetes cấp resources; scheduler backend biến allocation thành executors cho application` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `Cluster roles and the execution hierarchy: kiểm `Driver` bằng case 14, cụ thể driver chạy user main, tạo context/session, xây execution và điều phối work; mất driver thường kết thúc application theo deploy mode` phải đảo?
6. Phần nào của `Cluster roles and the execution hierarchy: kiểm `Cluster manager` bằng case 15, cụ thể standalone, yarn hoặc kubernetes cấp resources; scheduler backend biến allocation thành executors cho application` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Cluster roles and the execution hierarchy` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-APACHE-SPARK-RDD-GUIDE]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-APACHE-SPARK-RDD-GUIDE]] | Contract hoặc cơ chế liên quan trực tiếp tới `Cluster roles and the execution hierarchy` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Spark evidence becomes actionable only when application, job, stage, task and executor identities are connected.
- Với `wiki.spark.cluster-roles-execution-hierarchy`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Driver, cluster manager, executors, jobs, stages và tasks liên hệ thế nào trong một Spark application?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.web.apache-spark-rdd-guide` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
